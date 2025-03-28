#!/usr/bin/env python3
"""
Dify文档链接交互式检查工具

这个脚本会扫描文档文件中的链接，然后交互式地检查它们是否存在跳转问题或其他异常。
使用方法：
    python interactive_link_checker.py [--file FILE_PATH] [--output OUTPUT_FILE]
"""

import re
import os
import sys
import time
import argparse
import requests
import webbrowser
from datetime import datetime
from urllib.parse import urlparse
from colorama import init, Fore, Style

# 初始化colorama以支持跨平台的彩色输出
init()

# 设置一个User-Agent头，避免被某些网站封锁
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
RESULT_SKIPPED = "跳过"

class InteractiveLinkChecker:
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
            print(f"{Fore.RED}Error reading file {file_path}: {e}{Style.RESET_ALL}")
        
        return links
    
    def check_link_interactive(self, text, url):
        """交互式检查单个链接"""
        if url in self.visited:
            return
        
        self.visited.add(url)
        
        while True:
            print("\n" + "=" * 80)
            print(f"{Fore.CYAN}正在检查链接:{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}文本:{Style.RESET_ALL} {text}")
            print(f"{Fore.YELLOW}URL:{Style.RESET_ALL} {url}")
            
            action = input(f"\n{Fore.GREEN}操作选项:{Style.RESET_ALL} [c]检查 [o]在浏览器中打开 [s]跳过 [q]退出: ").lower()
            
            if action == 'q':
                print(f"{Fore.YELLOW}退出检查程序...{Style.RESET_ALL}")
                sys.exit(0)
            elif action == 's':
                self.results.append({
                    "文本": text,
                    "链接": url,
                    "结果": RESULT_SKIPPED,
                    "问题描述": "用户跳过"
                })
                break
            elif action == 'o':
                print(f"{Fore.BLUE}在浏览器中打开链接...{Style.RESET_ALL}")
                webbrowser.open(url)
                continue
            elif action == 'c' or action == '':
                print(f"{Fore.BLUE}正在检查链接...{Style.RESET_ALL}")
                
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
                        
                        print(f"{Fore.YELLOW}状态: 重定向 ({response.status_code}){Style.RESET_ALL}")
                        print(f"{Fore.YELLOW}重定向到: {redirect_url}{Style.RESET_ALL}")
                        
                        if redirect_url:
                            parsed_original = urlparse(url)
                            parsed_redirect = urlparse(redirect_url)
                            if parsed_original.path != parsed_redirect.path and parsed_redirect.path == '/':
                                result["问题描述"] = "页面自动跳转到首页"
                                print(f"{Fore.RED}问题: 页面自动跳转到首页{Style.RESET_ALL}")
                            else:
                                result["问题描述"] = f"重定向到 {redirect_url}"
                    elif response.status_code >= 400:
                        result["结果"] = RESULT_ERROR
                        result["问题描述"] = f"HTTP错误 {response.status_code}"
                        print(f"{Fore.RED}状态: 错误 ({response.status_code}){Style.RESET_ALL}")
                    else:
                        result["结果"] = RESULT_OK
                        result["问题描述"] = "正常访问"
                        print(f"{Fore.GREEN}状态: 正常 ({response.status_code}){Style.RESET_ALL}")
                        print(f"{Fore.GREEN}响应时间: {elapsed:.2f}秒{Style.RESET_ALL}")
                        
                        # 检查页面内容中的图片
                        if '/README' not in url:  # 避免检查会重定向的README页面
                            try:
                                full_response = self.session.get(url, timeout=TIMEOUT)
                                img_tags = re.findall(r'<img[^>]+src="([^"]+)"', full_response.text)
                                if img_tags:
                                    result["图片"] = f"包含 {len(img_tags)} 张图片"
                                    print(f"{Fore.BLUE}包含 {len(img_tags)} 张图片{Style.RESET_ALL}")
                            except Exception as e:
                                print(f"{Fore.RED}检查图片时出错: {e}{Style.RESET_ALL}")

                    # 是否手动标记问题
                    mark = input(f"\n{Fore.YELLOW}是否标记此链接有问题? (y/N): {Style.RESET_ALL}").lower()
                    if mark == 'y':
                        issue_type = input(f"{Fore.YELLOW}问题类型: [1]跳转 [2]错误 [3]其他: {Style.RESET_ALL}")
                        if issue_type == '1':
                            result["结果"] = RESULT_REDIRECT
                        elif issue_type == '2':
                            result["结果"] = RESULT_ERROR
                        
                        custom_desc = input(f"{Fore.YELLOW}请输入问题描述 (可选): {Style.RESET_ALL}")
                        if custom_desc:
                            result["问题描述"] = custom_desc
                    
                    self.results.append(result)
                    
                except requests.exceptions.Timeout:
                    print(f"{Fore.RED}状态: 超时{Style.RESET_ALL}")
                    self.results.append({
                        "文本": text,
                        "链接": url,
                        "结果": RESULT_TIMEOUT,
                        "问题描述": "请求超时"
                    })
                except Exception as e:
                    print(f"{Fore.RED}状态: 错误 - {str(e)}{Style.RESET_ALL}")
                    self.results.append({
                        "文本": text,
                        "链接": url,
                        "结果": RESULT_ERROR,
                        "问题描述": f"请求错误: {str(e)}"
                    })
                
                break
            else:
                print(f"{Fore.RED}无效的操作，请重试{Style.RESET_ALL}")
    
    def check_links_from_file(self, file_path):
        """从文件中交互式检查所有链接"""
        links = self.extract_links_from_file(file_path)
        print(f"{Fore.CYAN}在 {file_path} 中找到 {len(links)} 个链接{Style.RESET_ALL}")
        
        for i, (text, url) in enumerate(links):
            print(f"\n{Fore.CYAN}[{i+1}/{len(links)}] 检查链接{Style.RESET_ALL}")
            self.check_link_interactive(text, url)
    
    def generate_report(self, output_file=None):
        """生成检查报告"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 按结果类型分类统计
        stats = {
            RESULT_OK: 0,
            RESULT_REDIRECT: 0,
            RESULT_ERROR: 0,
            RESULT_TIMEOUT: 0,
            RESULT_SKIPPED: 0
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
            f"- 跳过链接: {stats[RESULT_SKIPPED]}",
            f"",
        ]
        
        # 添加异常情况记录
        report.append("## 异常情况记录")
        report.append("")
        report.append("| 链接 | 问题类型 | 问题描述 |")
        report.append("|------|----------|----------|")
        
        for result in self.results:
            if result.get("结果") not in [RESULT_OK, RESULT_SKIPPED]:
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
                print(f"{Fore.GREEN}报告已保存至 {output_file}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}保存报告到 {output_file} 时出错: {e}{Style.RESET_ALL}")
        
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
    parser = argparse.ArgumentParser(description='交互式检查文档中的链接')
    parser.add_argument('--file', help='要检查的文件路径')
    parser.add_argument('--dir', help='要递归检查的目录路径')
    parser.add_argument('--output', default='link_check_report.md', help='输出报告文件路径')
    parser.add_argument('--pattern', help='只检查包含特定模式的链接 (如 README)')
    
    args = parser.parse_args()
    
    checker = InteractiveLinkChecker()
    
    # 如果没有指定文件或目录，交互式询问用户
    if not args.file and not args.dir:
        print(f"{Fore.CYAN}\n欢迎使用 Dify 文档链接交互式检查器!{Style.RESET_ALL}")
        check_type = input(f"{Fore.YELLOW}\n您希望检查: [1]单个文件 [2]整个目录: {Style.RESET_ALL}")
        
        if check_type == '1':
            file_path = input(f"{Fore.YELLOW}请输入要检查的文件路径: {Style.RESET_ALL}")
            if file_path:
                args.file = file_path
            else:
                print(f"{Fore.RED}错误: 没有提供有效的文件路径{Style.RESET_ALL}")
                return
        elif check_type == '2':
            dir_path = input(f"{Fore.YELLOW}请输入要检查的目录路径: {Style.RESET_ALL}")
            if dir_path:
                args.dir = dir_path
            else:
                print(f"{Fore.RED}错误: 没有提供有效的目录路径{Style.RESET_ALL}")
                return
        else:
            print(f"{Fore.RED}错误: 无效的选择{Style.RESET_ALL}")
            return
            
        # 询问输出文件
        output_file = input(f"{Fore.YELLOW}请输入输出报告文件路径 (直接回车使用默认值 '{args.output}'): {Style.RESET_ALL}")
        if output_file:
            args.output = output_file
    
    # 检查文件或目录是否存在
    if args.file and not os.path.isfile(args.file):
        print(f"{Fore.RED}错误: 文件 '{args.file}' 不存在{Style.RESET_ALL}")
        return
    
    if args.dir and not os.path.isdir(args.dir):
        print(f"{Fore.RED}错误: 目录 '{args.dir}' 不存在{Style.RESET_ALL}")
        return
    
    if args.file:
        checker.check_links_from_file(args.file)
    elif args.dir:
        markdown_files = find_markdown_files(args.dir)
        print(f"{Fore.CYAN}在 {args.dir} 中找到 {len(markdown_files)} 个Markdown文件{Style.RESET_ALL}")
        
        for i, file_path in enumerate(markdown_files):
            print(f"\n{Fore.CYAN}[{i+1}/{len(markdown_files)}] 检查文件: {file_path}{Style.RESET_ALL}")
            proceed = input(f"{Fore.YELLOW}是否检查此文件? (Y/n/q): {Style.RESET_ALL}").lower()
            
            if proceed == 'q':
                print(f"{Fore.YELLOW}退出检查程序...{Style.RESET_ALL}")
                break
            elif proceed == 'n':
                print(f"{Fore.YELLOW}跳过此文件{Style.RESET_ALL}")
                continue
            else:
                checker.check_links_from_file(file_path)
    
    report = checker.generate_report(args.output)
    print(f"\n{Fore.CYAN}检查总结:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}总链接数: {len(checker.results)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}报告已保存至 {args.output}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
