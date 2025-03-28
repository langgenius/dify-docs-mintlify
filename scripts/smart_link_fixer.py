#!/usr/bin/env python3
import os
import re
import json
import sys
import difflib
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Any

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("link_conversion.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ANSI 颜色代码
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_docs_json(docs_json_path: str) -> dict:
    """加载 docs.json 文件并解析其中的路径信息"""
    try:
        with open(docs_json_path, 'r', encoding='utf-8') as f:
            docs_data = json.load(f)
        return docs_data
    except Exception as e:
        logger.error(f"加载 docs.json 时出错: {e}")
        raise

def extract_valid_paths(docs_data: dict) -> Tuple[Set[str], Dict[str, Set[str]]]:
    """从 docs.json 中提取所有有效的文档路径，并创建语言映射"""
    valid_paths = set()
    
    # 递归函数用于处理嵌套结构
    def extract_paths_from_object(obj: Any) -> None:
        if isinstance(obj, dict):
            # 检查是否有页面路径
            if "pages" in obj:
                for page in obj["pages"]:
                    if isinstance(page, str) and not page.startswith(("http://", "https://")):
                        valid_paths.add(page)
                    elif isinstance(page, dict):
                        extract_paths_from_object(page)
            # 处理其他可能的字典键
            for key, value in obj.items():
                if key != "pages":  # 避免重复处理
                    extract_paths_from_object(value)
        elif isinstance(obj, list):
            # 处理列表中的每个元素
            for item in obj:
                extract_paths_from_object(item)
    
    # 开始提取
    extract_paths_from_object(docs_data)
    
    # 创建一个语言版本到路径的映射
    lang_path_map = {}
    for path in valid_paths:
        parts = path.split('/')
        if len(parts) > 1:
            lang = parts[0]  # 第一部分通常是语言代码 (en, zh-hans 等)
            # 创建无语言前缀的版本
            no_lang_path = '/'.join(parts[1:])
            # 添加到映射
            if no_lang_path not in lang_path_map:
                lang_path_map[no_lang_path] = set()
            lang_path_map[no_lang_path].add(path)
    
    return valid_paths, lang_path_map

def find_closest_path(target_path: str, valid_paths: Set[str], lang_path_map: Dict[str, Set[str]], current_lang: str = "en") -> Optional[str]:
    """查找最接近的有效路径"""
    # 清理路径，移除 .md 和 .mdx 扩展名
    target_path_clean = target_path
    if target_path.endswith(('.md', '.mdx')):
        target_path_clean = target_path[:-3] if target_path.endswith('.md') else target_path[:-4]
    
    # 尝试直接匹配
    if target_path_clean in valid_paths:
        return target_path_clean
    if target_path in valid_paths:
        return target_path
    
    # 移除扩展名
    target_without_ext, ext = os.path.splitext(target_path_clean)
    # 只有在扩展名不是已经处理过的 .md/.mdx 时才进一步处理
    if ext and ext not in ['.md', '.mdx']:
        target_without_ext = target_path_clean
    
    # 尝试匹配无扩展名版本
    if target_without_ext in valid_paths:
        return target_without_ext
    
    # 检查是否是 README 或 index 文件 - 尝试匹配到目录
    basename = os.path.basename(target_without_ext).lower()
    if basename in ["readme", "index"]:
        dir_path = os.path.dirname(target_without_ext)
        # 直接匹配目录
        if dir_path in valid_paths:
            return dir_path
        # 尝试匹配目录下的 README 文件
        for path in valid_paths:
            if path.startswith(dir_path + '/') and path.lower().endswith(('/readme', '/index')):
                return path
    
    # 检查无语言前缀的匹配
    target_parts = target_path.split('/')
    if len(target_parts) > 1 and target_parts[0] in ["en", "zh-hans", "ja-jp"]:
        # 移除语言前缀
        no_lang_target = '/'.join(target_parts[1:])
        # 查找是否有匹配的路径
        if no_lang_target in lang_path_map:
            # 优先返回当前语言的路径
            for path in lang_path_map[no_lang_target]:
                if path.startswith(f"{current_lang}/"):
                    return path
            # 否则返回第一个匹配
            return next(iter(lang_path_map[no_lang_target]))
    
    # 没有前缀的情况下，尝试添加语言前缀后匹配
    if not target_path.startswith(("en/", "zh-hans/", "ja-jp/")):
        prefixed_path = f"{current_lang}/{target_path}"
        if prefixed_path in valid_paths:
            return prefixed_path
        # 移除扩展名再试
        prefixed_without_ext = f"{current_lang}/{target_without_ext}"
        if prefixed_without_ext in valid_paths:
            return prefixed_without_ext
    
    # 使用相似度算法进行模糊匹配
    best_match = None
    best_score = 0
    
    # 优先匹配文件名
    target_filename = os.path.basename(target_without_ext).lower()
    
    for path in valid_paths:
        path_filename = os.path.basename(path).lower()
        
        # 如果文件名匹配，增加相似度分数
        filename_match = False
        if target_filename == path_filename:
            filename_match = True
        
        # 计算整体路径的相似度
        path_without_ext, _ = os.path.splitext(path)
        score = difflib.SequenceMatcher(None, target_without_ext.lower(), path_without_ext.lower()).ratio()
        
        # 文件名匹配时增加分数
        if filename_match:
            score += 0.3
        
        # 如果当前语言匹配，增加分数
        if path.startswith(f"{current_lang}/"):
            score += 0.1
        
        if score > best_score:
            best_score = score
            best_match = path
    
    # 只有当相似度够高时才返回匹配结果
    if best_score > 0.6:
        return best_match
    
    return None

def find_md_files(path: str) -> List[Path]:
    """查找指定路径下的所有 .md 和 .mdx 文件"""
    path_obj = Path(path)
    if path_obj.is_file() and (path_obj.suffix in ['.md', '.mdx']):
        return [path_obj]
    
    md_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(('.md', '.mdx')):
                md_files.append(Path(os.path.join(root, file)))
    
    return md_files

def detect_file_language(file_path: Path) -> str:
    """根据文件路径检测语言"""
    path_str = str(file_path)
    if "/en/" in path_str:
        return "en"
    elif "/zh-hans/" in path_str:
        return "zh-hans"
    elif "/ja-jp/" in path_str:
        return "ja-jp"
    else:
        # 默认为英文
        return "en"

def convert_links_in_file(file_path: Path, valid_paths: Set[str], lang_path_map: Dict[str, Set[str]], base_dir: str) -> Tuple[List[dict], str]:
    """转换文件中的链接"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        logger.error(f"读取文件 {file_path} 时出错: {e}")
        return [], ""
    
    # 检测文件语言
    current_lang = detect_file_language(file_path)
    
    # 提取当前文件的相对路径（相对于基础目录）
    relative_file_path = os.path.relpath(file_path, base_dir)
    file_dir = os.path.dirname(relative_file_path)
    
    # 找出所有 Markdown 链接 - 支持带属性的链接
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)(\s+"[^"]*")?\)')
    matches = link_pattern.findall(content)
    
    changes = []
    for match in matches:
        link_text, link_url, link_attr = match
        
        # 修正link_attr（可能为空）
        link_attr = link_attr or ""
        
        # 跳过锚点链接、邮件链接和图片资源链接
        if link_url.startswith(('#', 'mailto:')):
            continue
        
        # 跳过图片和其他资源链接
        if any(link_url.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.pdf', '.mp4']):
            continue
        
        # 跳过资源服务器的链接
        if "assets-docs.dify.ai" in link_url:
            continue
        
        # 跳过外部链接，但保留 docs.dify.ai 链接进行处理
        if link_url.startswith(('http://', 'https://')) and "docs.dify.ai" not in link_url:
            continue
        
        # 已经是正确格式的链接（以 /en/ 或 /zh-hans/ 或 /ja-jp/ 开头）可以跳过
        if link_url.startswith(('/en/', '/zh-hans/', '/ja-jp/')):
            # 可选：验证链接是否有效
            clean_url = link_url.lstrip('/')
            if clean_url in valid_paths:
                continue
        
        matched_path = None
        match_type = ""
        
        # 处理 docs.dify.ai 链接 - 只处理指向文档的链接
        if "docs.dify.ai" in link_url and not any(link_url.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.pdf', '.mp4']):
            match_type = "docs.dify.ai"
            
            # 从 docs.dify.ai 链接中提取路径部分
            docs_path = link_url.split("docs.dify.ai/")[-1] if "docs.dify.ai/" in link_url else ""
            
            # 检查是否是图片或资源URL
            if any(segment in docs_path for segment in ['assets', 'images', 'assets-docs']):
                continue
            
            if docs_path:
                # 查找最接近的有效路径
                matched_path = find_closest_path(docs_path, valid_paths, lang_path_map, current_lang)
        
        # 处理相对路径链接
        elif link_url.startswith(('../', './')) or not link_url.startswith('/'):
            match_type = "relative"
            
            # 对路径做一些标准化
            if link_url.startswith('./'):
                link_url = link_url[2:]  # 移除开头的 ./
            
            # 计算目标文件的完整路径
            target_path = os.path.normpath(os.path.join(file_dir, link_url))
            target_path = target_path.replace('\\', '/')  # 统一路径分隔符
            
            # 处理可能的扩展名
            target_path_no_ext, ext = os.path.splitext(target_path)
            if ext in ['.md', '.mdx']:
                target_path = target_path_no_ext
            
            # 特殊处理 README/index 文件
            basename = os.path.basename(target_path).lower()
            if basename in ["readme", "index", "readme.md", "index.md", "readme.mdx", "index.mdx"]:
                dir_path = os.path.dirname(target_path)
                # 检查目录是否在有效路径中
                dir_match = find_closest_path(dir_path, valid_paths, lang_path_map, current_lang)
                if dir_match:
                    matched_path = dir_match
                    continue
            
            # 查找最接近的有效路径
            matched_path = find_closest_path(target_path, valid_paths, lang_path_map, current_lang)
        
        # 处理带有语言前缀但没有前导斜杠的路径
        elif any(link_url.startswith(prefix) for prefix in ["en/", "zh-hans/", "ja-jp/"]):
            match_type = "lang-prefixed"
            # 添加前导斜杠
            matched_path = find_closest_path(link_url, valid_paths, lang_path_map, current_lang)
        
        # 处理其他类型的链接
        else:
            match_type = "other"
            # 尝试将链接作为路径的一部分进行匹配
            matched_path = find_closest_path(link_url, valid_paths, lang_path_map, current_lang)
        
        # 如果找到了匹配路径，创建新链接
        if matched_path:
            # 构造新链接 URL，确保有前导斜杠
            new_link_url = f"/{matched_path}" if not matched_path.startswith('/') else matched_path
            
            old_link = f"[{link_text}]({link_url}{link_attr})"
            new_link = f"[{link_text}]({new_link_url}{link_attr})"
            
            changes.append({
                "old_link": old_link, 
                "new_link": new_link,
                "old_url": link_url,
                "new_url": new_link_url,
                "match_type": match_type,
                "match_path": matched_path,
                "confidence": "high"
            })
        else:
            # 未找到匹配路径，根据链接类型做通用处理
            generic_url = None
            
            if match_type == "docs.dify.ai":
                # 对于 docs.dify.ai 链接，使用路径部分
                # 但我们现在更谨慎，如果没有匹配到就不对它做任何改变
                continue  # 由于大部分 docs.dify.ai 链接可能指向资源，如果没有精确匹配，我们不做任何更改
            
            elif match_type == "relative":
                # 对于相对路径，标准化并添加语言前缀
                target_path = os.path.normpath(os.path.join(file_dir, link_url))
                target_path = target_path.replace('\\', '/')
                target_without_ext, _ = os.path.splitext(target_path)
                
                if target_without_ext.startswith(f"{current_lang}/"):
                    generic_url = f"/{target_without_ext}"
                else:
                    generic_url = f"/{current_lang}/{target_without_ext}"
            
            elif match_type == "lang-prefixed":
                # 已经有语言前缀，只需添加斜杠
                generic_url = f"/{link_url}"
            
            else:
                # 其他类型，尝试使用当前语言
                link_without_ext, _ = os.path.splitext(link_url)
                generic_url = f"/{current_lang}/{link_without_ext}"
            
            if generic_url:
                old_link = f"[{link_text}]({link_url}{link_attr})"
                new_link = f"[{link_text}]({generic_url}{link_attr})"
                
                changes.append({
                    "old_link": old_link, 
                    "new_link": new_link,
                    "old_url": link_url,
                    "new_url": generic_url,
                    "match_type": f"{match_type} (generic)",
                    "match_path": None,
                    "confidence": "low"
                })
    
    return changes, content

def apply_changes(content: str, changes: List[dict]) -> str:
    """应用更改到内容中"""
    modified_content = content
    for change in changes:
        modified_content = modified_content.replace(change["old_link"], change["new_link"])
    return modified_content

def main():
    """主函数"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    docs_json_path = os.path.join(base_dir, 'docs.json')
    
    # 显示脚本标题
    print(f"\n{Colors.CYAN}{Colors.BOLD}===== Dify 文档链接修复工具 ====={Colors.RESET}\n")
    
    # 加载 docs.json
    try:
        print(f"{Colors.BLUE}正在加载 docs.json...{Colors.RESET}")
        docs_data = load_docs_json(docs_json_path)
        valid_paths, lang_path_map = extract_valid_paths(docs_data)
        print(f"{Colors.GREEN}从 docs.json 中提取了 {Colors.YELLOW}{len(valid_paths)}{Colors.GREEN} 个有效路径{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}加载 docs.json 时出错: {e}{Colors.RESET}")
        sys.exit(1)
    
    # 获取用户输入的路径
    path_input = input(f"{Colors.CYAN}请输入要处理的文件或目录路径（相对于当前目录）: {Colors.RESET}")
    target_path = os.path.join(base_dir, path_input)
    
    if not os.path.exists(target_path):
        print(f"{Colors.RED}路径不存在: {target_path}{Colors.RESET}")
        sys.exit(1)
    
    # 查找 Markdown 文件
    md_files = find_md_files(target_path)
    print(f"{Colors.GREEN}找到 {Colors.YELLOW}{len(md_files)}{Colors.GREEN} 个 Markdown 文件{Colors.RESET}")
    
    # 用户选项
    auto_apply = input(f"{Colors.CYAN}是否自动应用所有高置信度的更改? (y/n): {Colors.RESET}").lower() == 'y'
    review_all = not auto_apply and input(f"{Colors.CYAN}是否审查所有更改? (y/n，默认仅审查低置信度更改): {Colors.RESET}").lower() == 'y'
    review_individual = not auto_apply and input(f"{Colors.CYAN}是否需要逐个审查每个链接? (y/n): {Colors.RESET}").lower() == 'y'
    
    # 处理每个文件
    total_changed = 0
    total_files_changed = 0
    total_files_processed = 0
    
    for file_path in md_files:
        total_files_processed += 1
        print(f"\n{Colors.BLUE}{Colors.BOLD}处理文件 ({total_files_processed}/{len(md_files)}): {Colors.RESET}{Colors.YELLOW}{file_path}{Colors.RESET}")
        
        changes, content = convert_links_in_file(file_path, valid_paths, lang_path_map, base_dir)
        
        if not changes:
            print(f"{Colors.GREEN}未发现需要修改的链接{Colors.RESET}")
            continue
        
        high_confidence_changes = [c for c in changes if c["confidence"] == "high"]
        low_confidence_changes = [c for c in changes if c["confidence"] == "low"]
        
        print(f"{Colors.MAGENTA}{Colors.BOLD}发现 {len(changes)} 个链接需要修改 ({len(high_confidence_changes)} 高置信度, {len(low_confidence_changes)} 低置信度){Colors.RESET}")
        
        # 显示更改
        apply_changes_to_file = False
        
        # 将要应用的更改收集到一个列表中
        changes_to_apply = []
        
        # 处理高置信度更改
        if high_confidence_changes:
            print(f"\n{Colors.GREEN}{Colors.BOLD}高置信度更改:{Colors.RESET}")
            for i, change in enumerate(high_confidence_changes, 1):
                print(f"{Colors.YELLOW}{i}. {Colors.RESET}[{change['match_type']}] {change['old_link']} -> {change['new_link']}")
            
            if auto_apply:
                # 自动应用所有高置信度更改
                changes_to_apply.extend(high_confidence_changes)
            elif review_individual:
                # 逐个审查每个链接
                for i, change in enumerate(high_confidence_changes, 1):
                    confirm = input(f"\n{Colors.CYAN}应用更改 {i}? (y/n/q-退出): {Colors.RESET}").lower()
                    if confirm == 'q':
                        break
                    if confirm == 'y':
                        changes_to_apply.append(change)
            elif review_all:
                # 整体审查高置信度更改
                if input(f"\n{Colors.CYAN}应用这些高置信度更改? (y/n): {Colors.RESET}").lower() == 'y':
                    changes_to_apply.extend(high_confidence_changes)
            else:
                # 默认应用高置信度更改
                changes_to_apply.extend(high_confidence_changes)
        
        # 处理低置信度更改
        if low_confidence_changes:
            print(f"\n{Colors.RED}{Colors.BOLD}低置信度更改:{Colors.RESET}")
            for i, change in enumerate(low_confidence_changes, 1):
                print(f"{Colors.YELLOW}{i}. {Colors.RESET}[{change['match_type']}] {change['old_link']} -> {change['new_link']}")
            
            if auto_apply:
                # 自动模式下不应用低置信度更改
                pass
            elif review_individual:
                # 逐个审查每个链接
                for i, change in enumerate(low_confidence_changes, 1):
                    confirm = input(f"\n{Colors.CYAN}应用更改 {i}? (y/n/q-退出): {Colors.RESET}").lower()
                    if confirm == 'q':
                        break
                    if confirm == 'y':
                        changes_to_apply.append(change)
            else:
                # 整体审查低置信度更改
                if input(f"\n{Colors.CYAN}应用这些低置信度更改? (y/n): {Colors.RESET}").lower() == 'y':
                    changes_to_apply.extend(low_confidence_changes)
        
        # 判断是否需要应用更改
        apply_changes_to_file = len(changes_to_apply) > 0
        
        if apply_changes_to_file:
            # 应用更改
            modified_content = apply_changes(content, changes_to_apply)
            
            # 备份原文件
            backup_path = str(file_path) + '.bak'
            try:
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"{Colors.BLUE}已备份原文件到: {backup_path}{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.RED}备份文件失败: {e}{Colors.RESET}")
                if not input(f"{Colors.YELLOW}是否继续修改? (y/n): {Colors.RESET}").lower() == 'y':
                    print(f"{Colors.YELLOW}跳过此文件{Colors.RESET}")
                    continue
            
            # 写回文件
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
            except Exception as e:
                print(f"{Colors.RED}写入文件失败: {e}{Colors.RESET}")
                # 尝试从备份恢复
                try:
                    with open(backup_path, 'r', encoding='utf-8') as f_bak:
                        bak_content = f_bak.read()
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(bak_content)
                    print(f"{Colors.GREEN}已从备份恢复文件{Colors.RESET}")
                except Exception as restore_err:
                    print(f"{Colors.RED}恢复文件失败: {restore_err}{Colors.RESET}")
                continue
            
            total_changed += len(changes_to_apply)
            total_files_changed += 1
            print(f"{Colors.GREEN}文件已更新: {file_path}{Colors.RESET}")
            print(f"{Colors.GREEN}应用了 {len(changes_to_apply)} 个链接更改{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}跳过此文件{Colors.RESET}")
    
    # 显示总结
    print(f"\n{Colors.CYAN}{Colors.BOLD}===== 转换完成 ====={Colors.RESET}")
    print(f"{Colors.GREEN}共处理了 {Colors.YELLOW}{total_files_processed}{Colors.GREEN} 个文件")
    print(f"修改了 {Colors.YELLOW}{total_files_changed}{Colors.GREEN} 个文件，{Colors.YELLOW}{total_changed}{Colors.GREEN} 个链接{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}用户中断，程序退出{Colors.RESET}")
        sys.exit(0)
