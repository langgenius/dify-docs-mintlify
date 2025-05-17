import json
import os
import re

# {new_doc_href} 将被替换为新文档的实际链接
DEPRECATION_NOTICE_TEMPLATE = """{{/* 
  コントリビューター注:
  ----------------
  これはレガシードキュメントであり、非推奨になります。
  このバージョンに変更を加えないでください。
  すべての更新は新しいバージョンに向けられるべきです：
  {new_doc_href}
*/}}

<Card title="このドキュメントはまもなく非推奨になります" icon="circle-exclamation" href="{new_doc_href}">
  <p>ドキュメント再編の一環として、このページは段階的に廃止されます。</p>
  
  <p><u><b>このカードをクリックして</b></u>、最新情報が含まれる更新版にリダイレクトしてください。</p>
  
  <p>新しいドキュメントに不一致や改善が必要な箇所を見つけた場合は、ページ下部の「問題を報告」ボタンを使用してください。</p>
</Card>"""

def load_mappings(json_full_path):
    """加载并解析 JSON 配置文件"""
    try:
        with open(json_full_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"错误：JSON 配置文件未找到 {json_full_path}")
    except json.JSONDecodeError:
        print(f"错误：JSON 配置文件解析失败 {json_full_path}")
    return None

def generate_href(dev_path_str):
    """根据 dev_path 生成新文档的 href"""
    if not isinstance(dev_path_str, str):
        print(f"警告：dev_path 不是字符串: {dev_path_str}")
        return "/default-path-error"
        
    path_part = dev_path_str
    if dev_path_str.endswith(".mdx"):
        path_part = dev_path_str[:-len(".mdx")]
    
    return "/" + path_part

def add_deprecation_notice_to_file_content(target_file_full_path, new_doc_href):
    """向指定文件添加弃用通告"""
    try:
        with open(target_file_full_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：文件未找到 {target_file_full_path}。跳过。")
        return
    except Exception as e:
        print(f"错误：读取文件失败 {target_file_full_path}。{e}。跳过。")
        return

    # 使用正则表达式查找 frontmatter (--- 开头和结尾的块)
    # 确保它在文件的开头
    frontmatter_match = re.match(r'^---\s*$.*?^---\s*$', content, re.MULTILINE | re.DOTALL)

    if not frontmatter_match:
        print(f"警告：在 {target_file_full_path} 文件开头未找到 frontmatter。跳过。")
        return

    frontmatter_end_index = frontmatter_match.end()
    frontmatter_text = content[:frontmatter_end_index]
    rest_of_content = content[frontmatter_end_index:]

    # 准备通告内容
    notice_body = DEPRECATION_NOTICE_TEMPLATE.format(new_doc_href=new_doc_href).strip()

    # 检查是否已存在通告 (基于标题和链接)，避免重复添加
    # "このドキュメントはまもなく非推奨になります" 是 Card 的日文标题
    if 'このドキュメントはまもなく非推奨になります' in rest_of_content and new_doc_href in rest_of_content:
        print(f"情報：通知 (リンク先 {new_doc_href}) は既に {target_file_full_path} に存在します。スキップします。") # 日语提示
        return

    # 组装新内容：frontmatter + 两个换行 + 通告 + 两个换行 + 原有内容（去除开头的换行）
    # 以确保通告前后各有一个空行
    new_content_parts = [frontmatter_text]
    new_content_parts.append("\n\n")  # frontmatter后的空行
    new_content_parts.append(notice_body)
    
    trimmed_original_content = rest_of_content.lstrip('\n')
    if trimmed_original_content:
        new_content_parts.append("\n\n")  # 原有内容前的空行
        new_content_parts.append(trimmed_original_content)
    else:
        # 如果原有内容为空或仅包含换行符，则在通告后添加一个换行符
        new_content_parts.append("\n") 
        
    new_full_content = "".join(new_content_parts)

    try:
        with open(target_file_full_path, 'w', encoding='utf-8') as f:
            f.write(new_full_content)
        print(f"信息：已向 {target_file_full_path} 添加弃用通告。")
    except IOError as e:
        print(f"错误：无法写入文件 {target_file_full_path}。{e}")
    except Exception as e:
        print(f"错误：写入文件时发生未知错误 {target_file_full_path}。{e}")

def main():
    # 脚本位于 tools/ 目录下，所以 base_dir 是上一级目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir) # 项目根目录

    # JSON 配置文件相对于 base_dir 的路径
    json_file_relative_path = "plugin_dev_ja/sync/plugin_mappings.json"  # 更新为日文版路径
    json_full_path = os.path.join(base_dir, json_file_relative_path)

    mappings_data = load_mappings(json_full_path)
    if not mappings_data:
        print("错误：无法加载映射数据，脚本终止。")
        return

    processed_count = 0
    for item in mappings_data.get("mappings", []):
        plugin_path_relative = item.get("plugin_path") # 旧文档路径 (相对于 base_dir)
        dev_path_relative = item.get("dev_path")       # 新文档路径 (相对于 base_dir)

        if plugin_path_relative and dev_path_relative:
            target_file_full_path = os.path.join(base_dir, plugin_path_relative)
            
            if not os.path.exists(target_file_full_path):
                print(f"警告：plugin_path 指定的文件 {target_file_full_path} 不存在。跳过。")
                continue
            if not os.path.isfile(target_file_full_path):
                print(f"警告：plugin_path 指定的路径 {target_file_full_path} 不是一个文件。跳过。")
                continue

            new_doc_href = generate_href(dev_path_relative)
            add_deprecation_notice_to_file_content(target_file_full_path, new_doc_href)
            processed_count +=1
        else:
            # 可以选择记录被跳过的条目
            # print(f"信息：因 plugin_path 或 dev_path 缺失而跳过映射条目: {item}")
            pass
    
    print(f"\n处理完成。共检查了 {len(mappings_data.get('mappings', []))} 条映射，对 {processed_count} 个文件尝试了操作。")

if __name__ == "__main__":
    main()
