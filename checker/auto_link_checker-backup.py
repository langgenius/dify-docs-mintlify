#!/usr/bin/env python3
"""
Dify文档链接自动检查工具

这个脚本会扫描文档文件中的链接，然后自动检查它们是否存在跳转问题、子链接和图片可用性问题。
使用方法：
    python auto_link_checker.py
"""

import re
import os
import sys
import time
import argparse
import requests
from datetime import datetime
from urllib.parse import urlparse
from colorama import init, Fore, Style
import asyncio
from playwright.async_api import async_playwright

# 初始化colorama以支持跨平台的彩色输出
init()

# 设置一个User-Agent头，避免被某些网站封锁
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

# 超时时间设置为10秒
TIMEOUT = 10000  # playwright使用的是毫秒

# 结果类别
RESULT_OK = "正常"
RESULT_REDIRECT = "跳转"
RESULT_ERROR = "错误"
RESULT_TIMEOUT = "超时"
RESULT_IMAGES_BROKEN = "图片问题"
RESULT_SUBLINKS_ISSUE = "子链接问题"

class AutoLinkChecker:
    def __init__(self, base_url="https://docs.dify.dev", headless=True):
        self.base_url = base_url
        self.results = []
        self.visited = set()
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.headless = headless
        self.browser = None
        self.page = None
    
    async def setup_browser(self):
        """设置浏览器"""
        try:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=self.headless)
            self.page = await self.browser.new_page(
                user_agent=HEADERS["User-Agent"],
                viewport={"width": 1280, "height": 800}
            )
            await self.page.set_default_timeout(TIMEOUT)
            print(f"{Fore.GREEN}浏览器启动成功{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}浏览器启动失败: {e}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}将仅使用HTTP请求检查重定向问题{Style.RESET_ALL}")
            return False
    
    async def close_browser(self):
        """关闭浏览器"""
        if self.browser:
            try:
                await self.browser.close()
                await self.playwright.stop()
                print(f"{Fore.GREEN}浏览器已关闭{Style.RESET_ALL}")
            except:
                pass
    
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
    
    def check_redirect(self, url):
        """检查链接是否有重定向"""
        try:
            response = self.session.get(url, timeout=TIMEOUT/1000, allow_redirects=False)
            if 300 <= response.status_code < 400:
                redirect_url = response.headers.get('Location', '')
                return True, redirect_url
            return False, None
        except Exception as e:
            return False, str(e)
    
    async def check_images(self, url):
        """检查页面中的图片是否可以加载"""
        if not self.page:
            return True, "浏览器未启动，无法检查图片"
            
        try:
            # 使用playwright导航到页面
            response = await self.page.goto(url)
            await self.page.wait_for_load_state('domcontentloaded')
            await asyncio.sleep(2)  # 给图片一些加载时间
            
            # 查找所有图片
            images = await self.page.query_selector_all('img')
            broken_images = []
            
            for img in images:
                img_src = await img.get_attribute("src")
                if not img_src:
                    continue
                    
                # 检查图片是否加载成功 (使用JS检查)
                img_complete = await self.page.evaluate("""img => {
                    return img.complete && 
                           typeof img.naturalWidth != 'undefined' && 
                           img.naturalWidth > 0
                }""", img)
                
                if not img_complete:
                    broken_images.append(img_src)
            
            if broken_images:
                return False, f"发现{len(broken_images)}张损坏的图片: {', '.join(broken_images[:3])}..."
            
            total_images = len(images)
            return True, f"所有{total_images}张图片正常加载" if total_images > 0 else "页面没有图片"
            
        except Exception as e:
            return False, f"检查图片时出错: {str(e)}"
    
    async def check_sublinks(self, url):
        """检查页面是否包含子链接"""
        if not self.page:
            return True, "浏览器未启动，无法检查子链接"
            
        try:
            # 页面应该在check_images中已经加载
            current_url = self.page.url
            if current_url != url:
                await self.page.goto(url)
                await self.page.wait_for_load_state('domcontentloaded')
            
            # 查找所有链接
            links = await self.page.query_selector_all('a')
            internal_links = []
            
            for link in links:
                href = await link.get_attribute("href")
                if href and self.base_url in href:
                    internal_links.append(href)
            
            return True, f"找到{len(internal_links)}个内部链接"
            
        except Exception as e:
            return False, f"检查子链接时出错: {str(e)}"
    
    async def check_link_automated(self, text, url):
        """自动检查单个链接"""
        if url in self.visited:
            return
        
        self.visited.add(url)
        
        print(f"\n{Fore.CYAN}检查链接: {url}{Style.RESET_ALL}")
        
        result = {
            "文本": text,
            "链接": url,
            "状态": RESULT_OK,
            "问题列表": [],
            "细节": {}
        }
        
        # 检查重定向
        is_redirect, redirect_info = self.check_redirect(url)
        if is_redirect:
            parsed_original = urlparse(url)
            parsed_redirect = urlparse(redirect_info)
            result["状态"] = RESULT_REDIRECT
            result["细节"]["重定向目标"] = redirect_info
            
            if parsed_original.path != parsed_redirect.path and parsed_redirect.path == '/':
                result["问题列表"].append("页面自动跳转到首页")
                print(f"{Fore.RED}问题: 页面自动跳转到首页{Style.RESET_ALL}")
            else:
                result["问题列表"].append(f"重定向到 {redirect_info}")
                print(f"{Fore.YELLOW}发现重定向: {redirect_info}{Style.RESET_ALL}")
                
        # 如果没有重定向，检查图片和子链接
        if not is_redirect and self.page:
            # 检查图片
            images_ok, images_info = await self.check_images(url)
            if not images_ok:
                result["状态"] = RESULT_IMAGES_BROKEN
                result["问题列表"].append(f"图片问题: {images_info}")
                print(f"{Fore.RED}图片问题: {images_info}{Style.RESET_ALL}")
            else:
                result["细节"]["图片状态"] = images_info
                print(f"{Fore.GREEN}图片状态: {images_info}{Style.RESET_ALL}")
            
            # 检查子链接
            sublinks_ok, sublinks_info = await self.check_sublinks(url)
            if not sublinks_ok:
                result["状态"] = RESULT_SUBLINKS_ISSUE
                result["问题列表"].append(f"子链接问题: {sublinks_info}")
                print(f"{Fore.RED}子链接问题: {sublinks_info}{Style.RESET_ALL}")
            else:
                result["细节"]["子链接状态"] = sublinks_info
                print(f"{Fore.GREEN}子链接状态: {sublinks_info}{Style.RESET_ALL}")
        
        self.results.append(result)
    
    async def check_links_from_file(self, file_path):
        """从文件中自动检查所有链接"""
        links = self.extract_links_from_file(file_path)
        print(f"{Fore.CYAN}在 {file_path} 中找到 {len(links)} 个链接{Style.RESET_ALL}")
        
        for i, (text, url) in enumerate(links):
            print(f"{Fore.CYAN}[{i+1}/{len(links)}] 检查链接{Style.RESET_ALL}")
            await self.check_link_automated(text, url)
    
    def generate_report(self, output_file=None):
        """生成检查报告"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 统计各种问题
        total = len(self.results)
        redirects = sum(1 for r in self.results if r["状态"] == RESULT_REDIRECT)
        image_issues = sum(1 for r in self.results if r["状态"] == RESULT_IMAGES_BROKEN)
        sublink_issues = sum(1 for r in self.results if r["状态"] == RESULT_SUBLINKS_ISSUE)
        ok_links = total - redirects - image_issues - sublink_issues
        
        report = [
            f"# Dify 文档链接自动检查报告",
            f"日期: {now}",
            f"",
            f"## 检查总结",
            f"",
            f"- 检查链接总数: {total}",
            f"- 正常链接: {ok_links}",
            f"- 重定向链接: {redirects}",
            f"- 图片问题链接: {image_issues}",
            f"- 子链接问题: {sublink_issues}",
            f"",
        ]
        
        # 添加问题汇总
        report.append("## 问题链接汇总")
        report.append("")
        report.append("| 链接 | 问题类型 | 问题描述 |")
        report.append("|------|----------|----------|")
        
        for result in self.results:
            if result["状态"] != RESULT_OK and result["问题列表"]:
                link = result["链接"]
                status = result["状态"]
                issues = ", ".join(result["问题列表"])
                report.append(f"| {link} | {status} | {issues} |")
        
        # 添加README链接跳转问题总结
        readme_redirects = [r for r in self.results if '/README' in r["链接"] and r["状态"] == RESULT_REDIRECT]
        if readme_redirects:
            report.append("")
            report.append("### README链接跳转问题")
            report.append("")
            report.append("发现以下链接包含README但会自动跳转到首页:")
            report.append("")
            for r in readme_redirects:
                report.append(f"- {r['链接']}")
        
        # 添加详细检查结果
        report.append("")
        report.append("## 详细检查结果")
        report.append("")
        report.append("| 链接 | 状态 | 详细信息 |")
        report.append("|------|------|----------|")
        
        for result in self.results:
            link = result["链接"]
            status = result["状态"]
            details = []
            
            if "重定向目标" in result["细节"]:
                details.append(f"重定向到: {result['细节']['重定向目标']}")
            
            if "图片状态" in result["细节"]:
                details.append(f"图片: {result['细节']['图片状态']}")
            
            if "子链接状态" in result["细节"]:
                details.append(f"子链接: {result['细节']['子链接状态']}")
                
            if result["问题列表"]:
                details.append(f"问题: {', '.join(result['问题列表'])}")
            
            detail_text = "<br>".join(details)
            report.append(f"| {link} | {status} | {detail_text} |")
        
        report_text = "\n".join(report)
        
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(report_text)
                print(f"{Fore.GREEN}报告已保存至 {output_file}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}保存报告到 {output_file} 时出错: {e}{Style.RESET_ALL}")
        
        return report_text

async def main_async():
    print(f"{Fore.CYAN}\n欢迎使用 Dify 文档链接自动检查工具!{Style.RESET_ALL}")
    
    # 获取链接文件路径
    file_path = input(f"{Fore.YELLOW}请输入链接文件的路径: {Style.RESET_ALL}")
    if not file_path or not os.path.isfile(file_path):
        print(f"{Fore.RED}错误: 无效的文件路径 '{file_path}'{Style.RESET_ALL}")
        return
    
    # 选择浏览器模式
    headless_mode = input(f"{Fore.YELLOW}选择浏览器模式 [1]无头浏览器(默认) [2]有头浏览器: {Style.RESET_ALL}")
    headless = headless_mode != "2"
    
    # 设置输出报告文件
    output_file = f"link_check_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    custom_output = input(f"{Fore.YELLOW}请输入输出报告文件路径 (直接回车使用默认值 '{output_file}'): {Style.RESET_ALL}")
    if custom_output:
        output_file = custom_output
    
    # 创建检查器并运行检查
    checker = AutoLinkChecker(headless=headless)
    
    try:
        # 设置浏览器
        browser_ok = await checker.setup_browser()
        
        print(f"{Fore.CYAN}开始检查链接...{Style.RESET_ALL}")
        await checker.check_links_from_file(file_path)
        checker.generate_report(output_file)
        
        print(f"\n{Fore.GREEN}检查完成!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}总共检查了 {len(checker.results)} 个链接{Style.RESET_ALL}")
        print(f"{Fore.GREEN}报告已保存至 {output_file}{Style.RESET_ALL}")
    finally:
        # 确保浏览器正确关闭
        await checker.close_browser()

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
