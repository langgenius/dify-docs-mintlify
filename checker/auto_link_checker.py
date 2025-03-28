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
import atexit  # 用于注册退出时的清理函数

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
    def __init__(self, base_url="https://docs.dify.dev", headless=True, output_file=None):
        self.base_url = base_url
        self.results = []
        self.visited = set()
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.headless = headless
        self.browser = None
        self.page = None
        self.playwright = None
        self.output_file = output_file
        self.report_file = None
        self.total_links_checked = 0
        
        # 创建日志文件
        self._init_report_file()
        
        # 注册退出处理函数，确保即使程序异常终止也能保存报告
        atexit.register(self._cleanup_on_exit)
    
    def _init_report_file(self):
        """初始化报告文件，实现多层级的错误处理和回退机制"""
        if self.output_file:
            try:
                # 确保目录存在
                dir_path = os.path.dirname(self.output_file)
                if dir_path and not os.path.exists(dir_path):
                    try:
                        os.makedirs(dir_path, exist_ok=True)
                        print(f"{Fore.GREEN}已创建目录: {dir_path}{Style.RESET_ALL}")
                    except PermissionError:
                        print(f"{Fore.RED}无权限创建目录: {dir_path}{Style.RESET_ALL}")
                    except Exception as e:
                        print(f"{Fore.RED}创建目录失败: {e}{Style.RESET_ALL}")
                
                # 尝试打开文件
                self.report_file = open(self.output_file, 'w', encoding='utf-8')
                self._write_report_header()
                print(f"{Fore.GREEN}检测日志文件已创建: {self.output_file}{Style.RESET_ALL}")
            except (PermissionError, OSError) as e:
                print(f"{Fore.RED}无法创建输出文件 {self.output_file}: {e}{Style.RESET_ALL}")
                self._try_fallback_locations()
            except Exception as e:
                print(f"{Fore.RED}创建输出文件时发生未知错误: {e}{Style.RESET_ALL}")
                self._try_fallback_locations()
        else:
            # 如果没有指定输出文件，使用默认文件名
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.output_file = f"link_check_report_{timestamp}.md"
            try:
                self.report_file = open(self.output_file, 'w', encoding='utf-8')
                self._write_report_header()
                print(f"{Fore.GREEN}检测日志文件已创建: {self.output_file}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}创建默认输出文件时出错: {e}{Style.RESET_ALL}")
                self._try_fallback_locations()
    def _try_fallback_locations(self):
        """尝试在多个位置创建报告文件的回退机制"""
        # 尝试的位置列表
        fallback_locations = [
            ".",  # 当前目录
            os.path.expanduser("~"),  # 用户主目录
            os.path.expanduser("~/Documents"),  # 用户文档目录
            "/tmp" if sys.platform != "win32" else os.environ.get("TEMP", "C:\\Temp")  # 临时目录
        ]
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        for location in fallback_locations:
            try:
                fallback_path = os.path.join(location, f"link_check_report_{timestamp}.md")
                self.report_file = open(fallback_path, 'w', encoding='utf-8')
                self.output_file = fallback_path
                self._write_report_header()
                print(f"{Fore.GREEN}使用备选位置创建日志文件: {fallback_path}{Style.RESET_ALL}")
                return
            except Exception as e:
                print(f"{Fore.YELLOW}尝试在 {location} 创建文件失败: {e}{Style.RESET_ALL}")
        
        print(f"{Fore.RED}无法在任何位置创建报告文件，将只在控制台显示结果{Style.RESET_ALL}")
        self.report_file = None
    
    def _write_report_header(self):
        """写入报告头部"""
        if not self.report_file:
            return
            
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.report_file.write(f"# Dify 文档链接自动检查报告\n")
        self.report_file.write(f"日期: {now}\n\n")
        self.report_file.write(f"## 检查总结\n\n")
        self.report_file.write(f"*注意：总结将在检查结束后更新*\n\n")
        self.report_file.write(f"## 检查进度\n\n")
        self.report_file.write(f"*此部分会实时更新*\n\n")
        self.report_file.write(f"## 问题链接汇总\n\n")
        self.report_file.write(f"| 链接 | 问题类型 | 问题描述 |\n")
        self.report_file.write(f"|------|----------|----------|\n")
        self.report_file.flush()
    
    def _cleanup_on_exit(self):
        """在程序退出时进行清理操作，确保报告被保存"""
        if hasattr(self, 'results') and self.results:
            try:
                # 如果结果非空，确保生成最终报告
                self._generate_final_report()
                print(f"{Fore.GREEN}程序退出前已保存检测报告{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}在退出前保存报告时出错: {e}{Style.RESET_ALL}")
        
        if hasattr(self, 'report_file') and self.report_file:
            try:
                self.report_file.close()
            except:
                pass
    
    def _generate_final_report(self):
        """在程序退出前生成最终报告"""
        if not self.report_file or not self.output_file:
            return
            
        try:
            # 关闭当前文件并重新打开以更新内容
            self.report_file.close()
            self.report_file = open(self.output_file, 'w', encoding='utf-8')
            
            # 生成报告并写入
            report_text = self.generate_report()
            self.report_file.write(report_text)
            self.report_file.flush()
            self.report_file.close()
            
        except Exception as e:
            print(f"{Fore.RED}生成最终报告时出错: {e}{Style.RESET_ALL}")
    
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
            
            # 更新并写入进度信息
            self._update_progress_info(f"从文件 {file_path} 中提取出 {len(links)} 个链接")
            
        except Exception as e:
            print(f"{Fore.RED}读取文件 {file_path} 时出错: {e}{Style.RESET_ALL}")
            self._update_progress_info(f"读取文件 {file_path} 时出错: {e}")
        
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
            
    def _update_progress_info(self, message):
        """更新进度信息到报告文件"""
        if not self.report_file:
            return
            
        try:
            # 先获取文件当前位置
            current_pos = self.report_file.tell()
            
            # 打开临时文件，复制内容和添加新内容
            temp_filename = f"{self.output_file}.temp"
            with open(self.output_file, 'r', encoding='utf-8') as src, open(temp_filename, 'w', encoding='utf-8') as dst:
                # 查找进度部分
                found_progress = False
                in_progress_section = False
                
                for line in src:
                    dst.write(line)
                    
                    if "## 检查进度" in line:
                        in_progress_section = True
                    elif in_progress_section and line.startswith("## "):
                        # 在进度部分结束前，添加新的进度消息
                        if not found_progress:
                            now = datetime.now().strftime("%H:%M:%S")
                            dst.write(f"- [{now}] {message}\n")
                            found_progress = True
                        in_progress_section = False
                
                # 如果没有找到合适的位置，就在文件末尾添加
                if not found_progress:
                    dst.seek(0, 2)  # 移到文件末尾
                    now = datetime.now().strftime("%H:%M:%S")
                    dst.write(f"\n- [{now}] {message}\n")
            
            # 替换原文件
            self.report_file.close()
            os.replace(temp_filename, self.output_file)
            
            # 重新打开文件并移动到之前的位置
            self.report_file = open(self.output_file, 'a', encoding='utf-8')
            
        except Exception as e:
            print(f"{Fore.YELLOW}更新进度信息时出错: {e}{Style.RESET_ALL}")
            # 如果出错，尝试重新打开文件
            try:
                if self.report_file.closed:
                    self.report_file = open(self.output_file, 'a', encoding='utf-8')
            except:
                pass
    async def check_link_automated(self, text, url):
        """自动检查单个链接"""
        if url in self.visited:
            return
        
        self.visited.add(url)
        self.total_links_checked += 1
        
        print(f"\n{Fore.CYAN}检查链接 [{self.total_links_checked}]: {url}{Style.RESET_ALL}")
        
        # 更新进度到日志
        self._update_progress_info(f"正在检查链接: {url}")
        
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
        
        # 将结果添加到列表
        self.results.append(result)
        
        # 实时写入问题到日志文件
        if result["状态"] != RESULT_OK and result["问题列表"]:
            self._write_issue_to_report(result)
        
        # 每检查10个链接，就更新一次总结报告
        if self.total_links_checked % 10 == 0:
            self._update_progress_info(f"已检查 {self.total_links_checked} 个链接，更新检查报告")
            self._generate_interim_summary()
    
    def _write_issue_to_report(self, result):
        """将问题写入报告文件"""
        if not self.report_file:
            return
            
        try:
            link = result["链接"]
            status = result["状态"]
            issues = ", ".join(result["问题列表"])
            
            # 检查文件是否可写
            if self.report_file.closed:
                self.report_file = open(self.output_file, 'a', encoding='utf-8')
                
            # 写入问题信息
            self.report_file.write(f"| {link} | {status} | {issues} |\n")
            self.report_file.flush()
        except Exception as e:
            print(f"{Fore.RED}写入问题到日志文件时出错: {e}{Style.RESET_ALL}")
            # 尝试恢复文件句柄
            try:
                if self.report_file.closed:
                    self.report_file = open(self.output_file, 'a', encoding='utf-8')
            except:
                pass
    
    def _generate_interim_summary(self):
        """生成中间总结报告"""
        if not self.report_file or not self.output_file:
            return
            
        try:
            # 统计各种问题
            total = len(self.results)
            redirects = sum(1 for r in self.results if r["状态"] == RESULT_REDIRECT)
            image_issues = sum(1 for r in self.results if r["状态"] == RESULT_IMAGES_BROKEN)
            sublink_issues = sum(1 for r in self.results if r["状态"] == RESULT_SUBLINKS_ISSUE)
            ok_links = total - redirects - image_issues - sublink_issues
            
            # 创建临时文件来更新总结部分
            temp_filename = f"{self.output_file}.temp"
            with open(self.output_file, 'r', encoding='utf-8') as src, open(temp_filename, 'w', encoding='utf-8') as dst:
                in_summary_section = False
                summary_updated = False
                
                for line in src:
                    # 当找到总结部分，更新内容
                    if "## 检查总结" in line:
                        in_summary_section = True
                        dst.write(line)  # 写入"## 检查总结"行
                        
                        # 写入更新后的总结
                        dst.write("\n")
                        dst.write(f"*最后更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
                        dst.write(f"- 已检查链接总数: {total}\n")
                        dst.write(f"- 正常链接: {ok_links}\n")
                        dst.write(f"- 重定向链接: {redirects}\n")
                        dst.write(f"- 图片问题链接: {image_issues}\n")
                        dst.write(f"- 子链接问题: {sublink_issues}\n")
                        dst.write("\n")
                        
                        # 跳过原有的总结内容
                        summary_updated = True
                    elif in_summary_section and line.startswith("## "):
                        # 退出总结部分
                        in_summary_section = False
                        dst.write(line)
                    elif not (in_summary_section and summary_updated):
                        # 如果不在总结部分或者总结已更新，则正常写入行
                        dst.write(line)
            
            # 替换原文件
            self.report_file.close()
            os.replace(temp_filename, self.output_file)
            
            # 重新打开文件
            self.report_file = open(self.output_file, 'a', encoding='utf-8')
            
        except Exception as e:
            print(f"{Fore.YELLOW}更新中间总结报告时出错: {e}{Style.RESET_ALL}")
            # 如果出错，尝试重新打开文件
            try:
                if self.report_file.closed:
                    self.report_file = open(self.output_file, 'a', encoding='utf-8')
            except:
                pass
    
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
                
                # 尝试在当前目录创建
                fallback_file = os.path.basename(output_file)
                try:
                    with open(fallback_file, 'w', encoding='utf-8') as f:
                        f.write(report_text)
                    print(f"{Fore.GREEN}报告已保存至当前目录: {fallback_file}{Style.RESET_ALL}")
                except Exception as e2:
                    print(f"{Fore.RED}保存到当前目录也失败: {e2}{Style.RESET_ALL}")
        
        return report_text

async def main_async():
    print(f"{Fore.CYAN}\n欢迎使用 Dify 文档链接自动检查工具!{Style.RESET_ALL}")
    
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Dify文档链接自动检查工具')
    parser.add_argument('--file', '-f', help='要检查的文件路径')
    parser.add_argument('--url', '-u', help='要检查的URL')
    parser.add_argument('--output', '-o', help='输出报告文件路径')
    parser.add_argument('--headless', '-l', action='store_true', help='使用无头浏览器模式')
    parser.add_argument('--visible', '-v', action='store_true', help='使用有头浏览器模式')
    args = parser.parse_args()
    
    file_path = args.file
    output_file = args.output
    
    # 如果命令行没有提供参数，则交互式获取
    if not file_path:
        file_path = input(f"{Fore.YELLOW}请输入链接文件的路径: {Style.RESET_ALL}")
    
    if not file_path or not os.path.isfile(file_path):
        print(f"{Fore.RED}错误: 无效的文件路径 '{file_path}'{Style.RESET_ALL}")
        return
    
    # 确定浏览器模式
    headless = True  # 默认使用无头模式
    
    if args.visible:
        headless = False
    elif args.headless:
        headless = True
    else:
        # 如果命令行没有指定，则交互式获取
        headless_mode = input(f"{Fore.YELLOW}选择浏览器模式 [1]无头浏览器(默认) [2]有头浏览器: {Style.RESET_ALL}")
        headless = headless_mode != "2"
    
    # 设置输出报告文件
    if not output_file:
        default_output = f"link_check_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        custom_output = input(f"{Fore.YELLOW}请输入输出报告文件路径 (直接回车使用默认值 '{default_output}'): {Style.RESET_ALL}")
        output_file = custom_output if custom_output else default_output
    
    # 创建检查器并运行检查
    checker = AutoLinkChecker(headless=headless, output_file=output_file)
    
    try:
        # 设置浏览器
        browser_ok = await checker.setup_browser()
        
        print(f"{Fore.CYAN}开始检查链接...{Style.RESET_ALL}")
        start_time = time.time()
        
        # 检查URL或文件
        if args.url:
            await checker.check_link_automated("命令行指定URL", args.url)
        else:
            await checker.check_links_from_file(file_path)
        
        # 生成报告
        final_report = checker.generate_report(output_file)
        end_time = time.time()
        
        print(f"\n{Fore.GREEN}检查完成!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}总共检查了 {len(checker.results)} 个链接{Style.RESET_ALL}")
        print(f"{Fore.CYAN}耗时: {round(end_time - start_time, 2)}秒{Style.RESET_ALL}")
        print(f"{Fore.GREEN}报告已保存至 {output_file}{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}检查被用户中断{Style.RESET_ALL}")
        print(f"{Fore.CYAN}正在保存已完成的检查结果...{Style.RESET_ALL}")
        checker.generate_report(output_file)
        print(f"{Fore.GREEN}部分检查报告已保存至 {output_file}{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}检查过程中发生错误: {e}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}正在保存已完成的检查结果...{Style.RESET_ALL}")
        checker.generate_report(output_file)
        print(f"{Fore.GREEN}部分检查报告已保存至 {output_file}{Style.RESET_ALL}")
    finally:
        # 确保浏览器正确关闭
        await checker.close_browser()

def main():
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}程序被用户中断{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}程序执行出错: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()