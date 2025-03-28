#!/usr/bin/env python3
"""
Dify文档链接检查工具

这个脚本会扫描文档文件中的链接，然后检查它们是否存在跳转问题或其他异常。
使用方法：
    python doc_link_checker.py [--file FILE_PATH] [--output OUTPUT_FILE]
"""

import re
import os
import sys
import time
import argparse
import requests
from datetime import datetime
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

# 设置一个 User-Agent 头，避免被某些网站封锁
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

# 超时时间设置为10秒
TIMEOUT = 10

# 结果类别
RESULT_OK = "正常"
RESULT_REDIRECT = "跳转"
RESULT_ERROR = "错误"
RESULT_TIMEOUT = "超时"

class LinkChecker:
    def __init__(self, base_url="https://docs.dify.dev"):
        self.base_url = base_url
        self.results = []
        self.visited = set()
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
    
    def extract_links_from_file(self, file_path):
        """从文件中提取链接"""
        links = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # 使用正则表达式匹配Markdown链接格式 [text](url)
                matches = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
                for match in matches:
                    text, url = match
                    # 只检查docs.dify.dev域名下的链接
                    if self.base_url in url:
                        links.append((text, url))
                
                # 也匹配HTML格式的链接 <a href="url">text</a>
                html_matches = re.findall(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"', content)
                for url in html_matches:
                    if self.base_url in url:
                        links.append(("HTML链接", url))
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
        
        return links
    
    def check_link(self, text, url):
        """检查单个链接"""
        if url in self.visited:
            return
        
        self.visited.add(url)
        
        try:
            start_time = time.time()
            response = self.session.get(url, timeout=TIMEOUT, allow_redirects=False)
            elapsed = time.time() - start_time
            
            result = {
                "文本": text,
                "链接": url,
                "状态码": response.status_code,
                "响应时间": f"{elapsed:.2f}秒"
            }
            
            if 300 <= response.status_code < 400:
                redirect_url = response.headers.get('Location', '')
                result["结果"] = RESULT_REDIRECT
                result["重定向URL"] = redirect_url
                if redirect_url:
                    parsed_original = urlparse(url)
                    parsed_redirect = urlparse(redirect_url)
                    if parsed_original.path != parsed_redirect.path and parsed_redirect.path == '/':
                        result["问题描述"] = "页面自动跳转到首页"
                    else:
                        result["问题描述"] = f"重定向到 {redirect_url}"
            elif response.status_code >= 400:
                result["结果"] = RESULT_ERROR
                result["问题描述"] = f"HTTP错误 {response.status_code}"
            else:
                result["结果"] = RESULT_OK
                result["问题描述"] = "正常访问"
                
                # 检查页面内容中的图片
                if '/README' not in url:  # 避免检查会重定向的README页面
                    try:
                        full_response = self.session.get(url, timeout=TIMEOUT)
                        img_tags = re.findall(r'<img[^>]+src="([^"]+)"', full_response.text)
                        if img_tags:
                            result["图片"] = f"包含 {len(img_tags)} 张图片"
                    except Exception as e:
                        print(f"Error checking images in {url}: {e}")
            
            self.results.append(result)
            
        except requests.exceptions.Timeout:
            self.results.append({
                "文本": text,
                "链接": url,
                "结果": RESULT_TIMEOUT,
                "问题描述": "请求超时"
            })
        except Exception as e:
            self.results.append({
                "文本": text,
                "链接": url,
                "结果": RESULT_ERROR,
                "问题描述": f"请求错误: {str(e)}"
            })
    
    def check_links_from_file(self, file_path, max_workers=5):
        """从文件中检查所有链接"""
        links = self.extract_links_from_file(file_path)
        print(f"Found {len(links)} links in {file_path}")
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_link = {
                executor.submit(self.check_link, text, url): (text, url) 
                for text, url in links
            }
            
            for future in as_completed(future_to_link):
                text, url = future_to_link[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"Error checking link {url}: {e}")
    
    def generate_report(self, output_file=None):
        """生成检查报告"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 按结果类型分类统计
        stats = {
            RESULT_OK: 0,
            RESULT_REDIRECT: 0,
            RESULT_ERROR: 0,
            RESULT_TIMEOUT: 0
        }
        
        for result in self.results:
            stats[result.get("结果", RESULT_ERROR)] += 1
        
        report = [
            f"# Dify 文档链接检查报告",
            f"日期: {now}",
            f"",
            f"## 检查总结",
            f"",
            f"- 检查链接总数: {len(self.results)}",
            f"- 正常链接: {stats[RESULT_OK]}",
            f"- 重定向链接: {stats[RESULT_REDIRECT]}",
            f"- 错误链接: {stats[RESULT_ERROR]}",
            f"- 超时链接: {stats[RESULT_TIMEOUT]}",
            f"",
        ]
        
        # 添加异常情况记录
        report.append("## 异常情况记录")
        report.append("")
        report.append("| 链接 | 问题类型 | 问题描述 |")
        report.append("|------|----------|----------|")
        
        for result in self.results:
            if result.get("结果") != RESULT_OK:
                link = result.get("链接", "")
                result_type = result.get("结果", "未知")
                description = result.get("问题描述", "")
                report.append(f"| {link} | {result_type} | {description} |")
        
        # 添加README链接跳转问题总结
        readme_redirects = [r for r in self.results if '/README' in r.get("链接", "") and r.get("结果") == RESULT_REDIRECT]
        if readme_redirects:
            report.append("")
            report.append("### README链接跳转问题")
            report.append("")
            report.append("发现以下链接包含README但会自动跳转到首页:")
            report.append("")
            for r in readme_redirects:
                report.append(f"- {r.get('链接')}")
        
        # 添加详细结果表格
        report.append("")
        report.append("## 详细检查结果")
        report.append("")
        report.append("| 链接文本 | 链接URL | 状态 | 响应时间 | 问题描述 |")
        report.append("|----------|---------|------|----------|----------|")
        
        for result in self.results:
            text = result.get("文本", "").replace("|", "\\|")[:30]  # 截断过长的文本
            url = result.get("链接", "")
            status = result.get("结果", "未知")
            time = result.get("响应时间", "")
            desc = result.get("问题描述", "")
            
            report.append(f"| {text} | {url} | {status} | {time} | {desc} |")
        
        report_text = "\n".join(report)
        
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(report_text)
                print(f"Report saved to {output_file}")
            except Exception as e:
                print(f"Error saving report to {output_file}: {e}")
        
        return report_text

def find_markdown_files(directory):
    """递归查找目录下的所有Markdown文件"""
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def main():
    parser = argparse.ArgumentParser(description='检查文档中的链接')
    parser.add_argument('--file', help='要检查的文件路径')
    parser.add_argument('--dir', help='要递归检查的目录路径')
    parser.add_argument('--output', default='link_check_report.md', help='输出报告文件路径')
    parser.add_argument('--workers', type=int, default=5, help='并发检查工作线程数')
    
    args = parser.parse_args()
    
    if not args.file and not args.dir:
        parser.error("需要指定 --file 或 --dir 参数")
    
    checker = LinkChecker()
    
    if args.file:
        checker.check_links_from_file(args.file, max_workers=args.workers)
    elif args.dir:
        markdown_files = find_markdown_files(args.dir)
        print(f"Found {len(markdown_files)} markdown files in {args.dir}")
        
        for file_path in markdown_files:
            print(f"Checking links in {file_path}")
            checker.check_links_from_file(file_path, max_workers=args.workers)
    
    report = checker.generate_report(args.output)
    print("\nSummary:")
    print(f"Total links: {len(checker.results)}")
    print(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()
