import json
import os
import re
from collections import defaultdict
from pathlib import Path

# --- Script Base Paths ---
SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent

# --- Configuration ---
refresh = False # Flag to control whether to clear existing tabs before processing
DOCS_JSON_PATH = BASE_DIR / "docs.json" # Path to the main documentation structure JSON file

# --- Language Configurations ---
# These configurations define how documentation files for different languages are processed.
# IMPORTANT: The string values for LANGUAGE_CODE, TARGET_TAB_NAME, and content within
# PWX_TO_GROUP_MAP and DESIRED_GROUP_ORDER are i18n-specific and MUST NOT be translated.
PLUGIN_DEV_ZH = {
    "DOCS_DIR_RELATIVE": "plugin_dev_zh", "LANGUAGE_CODE": "简体中文", "FILE_EXTENSION_SUFFIX": ".zh",
    "TARGET_TAB_NAME": "插件开发", "FILENAME_PATTERN": re.compile(r"^(\d{4})-(.*?)\.zh\.mdx$"),
    "PWX_TO_GROUP_MAP": { # Maps (P, W, X) prefixes from filenames to (Tab Name, Group Name, Optional Nested Group Name)
        ("0", "1", "1"): ("插件开发", "概念与入门", "概览"), ("0", "1", "3"): ("插件开发", "概念与入门", None),
        ("0", "2", "1"): ("插件开发", "开发实践", "快速开始"),("0", "2", "2"): ("插件开发", "开发实践", "开发 Dify 插件"),
        ("0", "3", "1"): ("插件开发", "贡献与发布", "行为准则与规范"),("0", "3", "2"): ("插件开发", "贡献与发布", "发布与上架"),("0", "3", "3"): ("插件开发", "贡献与发布", "常见问题解答"),
        ("0", "4", "3"): ("插件开发", "实践案例与示例", "开发示例"),
        ("9", "2", "2"): ("插件开发", "高级开发", "Extension 与 Agent"),("9", "2", "3"): ("插件开发", "高级开发", "Extension 与 Agent"),("9", "4", "3"): ("插件开发", "高级开发", "Extension 与 Agent"),("9", "2", "4"): ("插件开发", "高级开发", "反向调用"),
        ("0", "4", "1"): ("插件开发", "Reference & Specifications", "核心规范与功能"),
    },
    "DESIRED_GROUP_ORDER": ["概念与入门", "开发实践", "贡献与发布", "实践案例与示例", "高级开发", "Reference & Specifications"],
}
PLUGIN_DEV_EN = {
    "DOCS_DIR_RELATIVE": "plugin_dev_en", "LANGUAGE_CODE": "English", "FILE_EXTENSION_SUFFIX": ".en",
    "TARGET_TAB_NAME": "Plugin Development", "FILENAME_PATTERN": re.compile(r"^(\d{4})-(.*?)\.en\.mdx$"),
    "PWX_TO_GROUP_MAP": {
        ("0", "1", "1"): ("Plugin Development", "Concepts & Getting Started", "Overview"),("0", "1", "3"): ("Plugin Development", "Concepts & Getting Started", None),
        ("0", "2", "1"): ("Plugin Development", "Development Practices", "Quick Start"),("0", "2", "2"): ("Plugin Development", "Development Practices", "Developing Dify Plugins"),
        ("0", "3", "1"): ("Plugin Development", "Contribution & Publishing", "Code of Conduct & Standards"),("0", "3", "2"): ("Plugin Development", "Contribution & Publishing", "Publishing & Listing"),("0", "3", "3"): ("Plugin Development", "Contribution & Publishing", "FAQ"),
        ("0", "4", "3"): ("Plugin Development", "Examples & Use Cases", "Development Examples"),
        ("9", "2", "2"): ("Plugin Development", "Advanced Development", "Extension & Agent"),("9", "2", "3"): ("Plugin Development", "Advanced Development", "Extension & Agent"),("9", "4", "3"): ("Plugin Development", "Advanced Development", "Extension & Agent"),("9", "2", "4"): ("Plugin Development", "Advanced Development", "Reverse Calling"),
        ("0", "4", "1"): ("Plugin Development", "Reference & Specifications", "Core Specifications & Features"),
    },
    "DESIRED_GROUP_ORDER": ["Concepts & Getting Started", "Development Practices", "Contribution & Publishing", "Examples & Use Cases", "Advanced Development", "Reference & Specifications"],
}
PLUGIN_DEV_JA = {
    "DOCS_DIR_RELATIVE": "plugin_dev_ja", "LANGUAGE_CODE": "日本語", "FILE_EXTENSION_SUFFIX": ".ja",
    "TARGET_TAB_NAME": "プラグイン開発", "FILENAME_PATTERN": re.compile(r"^(\d{4})-(.*?)\.ja\.mdx$"),
    "PWX_TO_GROUP_MAP": {
        ("0", "1", "1"): ("プラグイン開発", "概念と概要", "概要"),("0", "1", "3"): ("プラグイン開発", "概念と概要", None),
        ("0", "2", "1"): ("プラグイン開発", "開発実践", "クイックスタート"),("0", "2", "2"): ("プラグイン開発", "開発実践", "Difyプラグインの開発"),
        ("0", "3", "1"): ("プラグイン開発", "貢献と公開", "行動規範と基準"),("0", "3", "2"): ("プラグイン開発", "貢献と公開", "公開と掲載"),("0", "3", "3"): ("プラグイン開発", "貢献と公開", "よくある質問 (FAQ)"),
        ("0", "4", "3"): ("プラグイン開発", "実践例とユースケース", "開発例"),
        ("9", "2", "2"): ("プラグイン開発", "高度な開発", "Extension と Agent"),("9", "2", "3"): ("プラグイン開発", "高度な開発", "Extension と Agent"),("9", "4", "3"): ("プラグイン開発", "高度な開発", "Extension と Agent"),("9", "2", "4"): ("プラグイン開発", "高度な開発", "リバースコール"),
        ("0", "4", "1"): ("プラグイン開発", "リファレンスと仕様", "コア仕様と機能"),
    },
    "DESIRED_GROUP_ORDER": ["概念と概要", "開発実践", "貢献と公開", "実践例とユースケース", "高度な開発", "リファレンスと仕様"],
}

# --- Helper Functions ---

# Defines log issue types considered critical enough to be included in the commit message summary.
CRITICAL_ISSUE_TYPES = {"Error", "Critical", "ConfigError", "SeriousWarning"}

def _log_issue(reports_list_for_commit_message: list, lang_code: str, issue_type: str, message: str, details: str = ""):
    """
    Logs a detailed message to the console and adds a concise version to a list for commit messages
    if the issue_type is critical.

    Args:
        reports_list_for_commit_message: List to accumulate messages for the commit summary.
        lang_code: Language code or identifier for the context of the log (e.g., "简体中文", "GLOBAL").
        issue_type: Type of the issue (e.g., "Info", "Warning", "Error", "Critical").
        message: The main message of the log.
        details: Optional additional details for the log.
    """
    full_log_message = f"[{issue_type.upper()}] Lang '{lang_code}': {message}"
    if details:
        full_log_message += f" Details: {details}"
    print(full_log_message) # Always print the detailed log message to console.

    if issue_type in CRITICAL_ISSUE_TYPES:
        # Prepare a more concise message for the commit summary.
        commit_msg_part = f"- Lang '{lang_code}': [{issue_type}] {message}"
        reports_list_for_commit_message.append(commit_msg_part)
    # INFO and non-critical Warning logs are only printed to console, not added to the commit summary list.


# Note: The following helper functions call `_log_issue`. Their docstrings will describe their primary purpose.
# The `commit_message_reports_list` parameter passed to them is for `_log_issue`.

def clear_tabs_if_refresh(navigation_data: dict, version_code: str, target_tab_name: str, do_refresh: bool, commit_message_reports_list: list) -> bool:
    """
    Clears groups within a specific tab in the navigation data if `do_refresh` is True.

    Args:
        navigation_data: The main navigation data structure.
        version_code: The language code or version identifier (e.g., "简体中文").
        target_tab_name: The name of the tab to clear.
        do_refresh: Boolean flag; if True, groups in the tab will be cleared.
        commit_message_reports_list: List for accumulating critical issue messages.

    Returns:
        True if the tab was found and cleared, False otherwise.
    """
    if not do_refresh:
        return False
    if not navigation_data or "versions" not in navigation_data:
        _log_issue(commit_message_reports_list, version_code, "Warning", "'navigation.versions' not found, cannot clear tabs.")
        return False

    version_found, tab_cleared = False, False
    for version_nav in navigation_data.get("versions", []):
        if version_nav.get("version") == version_code:
            version_found = True
            target_tab = next((t for t in version_nav.get("tabs", []) if isinstance(t, dict) and t.get("tab") == target_tab_name), None)
            if target_tab:
                target_tab["groups"] = []
                _log_issue(commit_message_reports_list, version_code, "Info", f"Cleared groups for Tab '{target_tab_name}'.")
                tab_cleared = True
            else:
                # This might be an Info log if we expect the tab to be created later.
                # If refresh implies the tab must exist, it could be a Warning.
                _log_issue(commit_message_reports_list, version_code, "Info", f"Tab '{target_tab_name}' not found to clear groups (will be created if needed).")
            break
    if not version_found:
        _log_issue(commit_message_reports_list, version_code, "Warning", f"Version '{version_code}' not found, cannot clear any Tab.")
    return tab_cleared

def get_page_path_from_filename(filename: str, docs_dir_name: str) -> str:
    """
    Constructs the documentation page path from its filename and directory name.
    Example: "0001-intro.en.mdx", "plugin_dev_en" -> "plugin_dev_en/0001-intro.en"

    Args:
        filename: The .mdx filename (e.g., "0001-intro.en.mdx").
        docs_dir_name: The relative directory name for this set of docs (e.g., "plugin_dev_en").

    Returns:
        The page path string used in docs.json.

    Raises:
        ValueError: If the filename does not end with ".mdx" (internal error if this happens).
    """
    if not filename.endswith(".mdx"):
        # This case should ideally be filtered out before calling this function.
        # If it reaches here, it indicates an internal logic error.
        raise ValueError(f"Internal Error: Filename '{filename}' received by get_page_path_from_filename does not end with '.mdx'.")
    base_filename = filename[:-len(".mdx")] # Remove ".mdx"
    return f"{docs_dir_name}/{base_filename}"


def extract_existing_pages(navigation_data: dict, version_code: str, target_tab_name: str, commit_message_reports_list: list):
    """
    Extracts all existing page paths from a specific tab within a version in the navigation data.

    Args:
        navigation_data: The main navigation data structure.
        version_code: The language code or version identifier.
        target_tab_name: The name of the tab to extract pages from.
        commit_message_reports_list: List for accumulating critical issue messages (passed to helpers, not used directly).

    Returns:
        A tuple: (set_of_existing_page_paths, target_version_nav_dict, target_tab_nav_dict).
        Returns (set(), None, None) if the version or tab is not found.
    """
    existing_pages = set()
    target_version_nav, target_tab_nav = None, None

    if not navigation_data or "versions" not in navigation_data:
        return existing_pages, None, None # No versions structure, so no pages

    target_version_nav = next((v for v in navigation_data.get("versions", []) if v.get("version") == version_code), None)
    if not target_version_nav:
        return existing_pages, None, None # Version not found

    if "tabs" in target_version_nav and isinstance(target_version_nav["tabs"], list):
        target_tab_nav = next((t for t in target_version_nav["tabs"] if isinstance(t,dict) and t.get("tab") == target_tab_name), None)
        if target_tab_nav:
            for group in target_tab_nav.get("groups", []):
                if isinstance(group, dict):
                    _recursive_extract(group, existing_pages)
    
    return existing_pages, target_version_nav, target_tab_nav

def _recursive_extract(group_item: dict, pages_set: set):
    """
    Recursively extracts page paths from a group item and its nested groups.
    (Helper for extract_existing_pages).

    Args:
        group_item: A dictionary representing a group, which may contain pages or nested groups.
        pages_set: A set to which extracted page paths are added.
    """
    if not isinstance(group_item, dict): return # Safety check
    for page in group_item.get("pages", []):
        if isinstance(page, str):
            pages_set.add(page)
        elif isinstance(page, dict) and "group" in page: # It's a nested group
            _recursive_extract(page, pages_set)


def remove_obsolete_pages(target_tab_data: dict, pages_to_remove: set, commit_message_reports_list: list, lang_code: str):
    """
    Removes obsolete page paths from the groups within the target tab data.
    Modifies `target_tab_data` in place.

    Args:
        target_tab_data: The dictionary for the specific tab being processed.
        pages_to_remove: A set of page path strings that should be removed.
        commit_message_reports_list: List for accumulating critical issue messages.
        lang_code: Language code for logging purposes.
    """
    if not isinstance(target_tab_data, dict) or "groups" not in target_tab_data or not isinstance(target_tab_data.get("groups"), list):
        _log_issue(commit_message_reports_list, lang_code, "Warning", "Attempted to remove obsolete pages from invalid target_tab_data structure.", f"Tab data: {target_tab_data}")
        return

    groups = target_tab_data["groups"]
    i = 0
    while i < len(groups): # Iterate with index to handle potential removal of empty groups (currently retains structure)
        group_item = groups[i]
        if isinstance(group_item, dict):
            _remove_obsolete_from_group(group_item, pages_to_remove, commit_message_reports_list, lang_code)
            if not group_item.get("pages"): # Check if the group became empty
                 _log_issue(commit_message_reports_list, lang_code, "Info", f"Group '{group_item.get('group', 'Unknown')}' emptied after removing obsolete pages; structure retained.")
            i += 1
        else: 
            _log_issue(commit_message_reports_list, lang_code, "Warning", f"Encountered non-dict item in groups list of Tab '{target_tab_data.get('tab','Unknown')}' during obsolete page removal. Item: {group_item}")
            i += 1

def _remove_obsolete_from_group(group_dict: dict, pages_to_remove: set, commit_message_reports_list: list, lang_code: str):
    """
    Recursively removes obsolete page paths from a group dictionary and its nested groups.
    Modifies `group_dict` in place. (Helper for remove_obsolete_pages).

    Args:
        group_dict: The dictionary representing a group.
        pages_to_remove: A set of page path strings to remove.
        commit_message_reports_list: List for accumulating critical issue messages.
        lang_code: Language code for logging.
    """
    if not isinstance(group_dict, dict) or "pages" not in group_dict or not isinstance(group_dict.get("pages"), list):
        group_name_for_log_err = group_dict.get('group', 'Unnamed Group with structural issue') if isinstance(group_dict, dict) else 'Non-dict item'
        _log_issue(commit_message_reports_list, lang_code, "Warning", f"Group '{group_name_for_log_err}' has invalid 'pages' structure; cannot remove obsolete pages from it. Structure: {group_dict}")
        return

    new_pages = []
    group_name_for_log = group_dict.get('group', 'Unknown') # For logging context
    for page_item in group_dict["pages"]:
        if isinstance(page_item, str): # It's a page path
            if page_item not in pages_to_remove:
                new_pages.append(page_item)
            else:
                _log_issue(commit_message_reports_list, lang_code, "Info", f"Removed obsolete page '{page_item}' from Group '{group_name_for_log}'.")
        elif isinstance(page_item, dict) and "group" in page_item: # It's a nested group
            _remove_obsolete_from_group(page_item, pages_to_remove, commit_message_reports_list, lang_code)
            # Retain nested group even if it becomes empty.
            if page_item.get("pages"): 
                new_pages.append(page_item)
            else:
                 _log_issue(commit_message_reports_list, lang_code, "Info", f"Nested group '{page_item.get('group', 'Unknown')}' in Group '{group_name_for_log}' emptied; structure retained.")
                 new_pages.append(page_item) # Still append the empty nested group structure
        else: # Unknown item type, preserve it
            _log_issue(commit_message_reports_list, lang_code, "Warning", f"Encountered unexpected item type in 'pages' list of Group '{group_name_for_log}'. Preserving item: {page_item}")
            new_pages.append(page_item)
    group_dict["pages"] = new_pages


def find_or_create_target_group(target_version_nav: dict, tab_name: str, group_name: str, nested_group_name: str | None, commit_message_reports_list: list, lang_code: str) -> list:
    """
    Finds or creates the target group (and nested group, if specified) within the navigation data
    and returns the 'pages' list where new pages should be added.
    Modifies `target_version_nav` in place by adding new structures if they don't exist.

    Args:
        target_version_nav: The dictionary for the specific version being processed.
        tab_name: The name of the target tab.
        group_name: The name of the primary group.
        nested_group_name: The name of the nested group (optional, can be None).
        commit_message_reports_list: List for accumulating critical issue messages.
        lang_code: Language code for logging.

    Returns:
        The 'pages' list (mutable) of the target group or nested group.
    """
    target_version_nav.setdefault("tabs", [])
    if not isinstance(target_version_nav["tabs"], list): 
        _log_issue(commit_message_reports_list, lang_code, "Critical", f"Internal state error: version.tabs is not a list for version '{target_version_nav.get('version')}'. Attempting to recover by creating a new list.")
        target_version_nav["tabs"] = [] 

    target_tab = next((t for t in target_version_nav["tabs"] if isinstance(t,dict) and t.get("tab") == tab_name), None)
    if not target_tab:
        target_tab = {"tab": tab_name, "groups": []}
        target_version_nav["tabs"].append(target_tab)
        _log_issue(commit_message_reports_list, lang_code, "Info", f"Created new Tab '{tab_name}'.")

    target_tab.setdefault("groups", [])
    if not isinstance(target_tab["groups"], list): 
        _log_issue(commit_message_reports_list, lang_code, "Critical", f"Internal state error: tab.groups is not a list for Tab '{tab_name}'. Attempting to recover.")
        target_tab["groups"] = [] 

    target_group = next((g for g in target_tab["groups"] if isinstance(g,dict) and g.get("group") == group_name), None)
    if not target_group:
        target_group = {"group": group_name, "pages": []}
        target_tab["groups"].append(target_group)
        _log_issue(commit_message_reports_list, lang_code, "Info", f"Created new Group '{group_name}' in Tab '{tab_name}'.")

    target_group.setdefault("pages", [])
    if not isinstance(target_group["pages"], list): 
         _log_issue(commit_message_reports_list, lang_code, "Critical", f"Internal state error: group.pages is not a list for Group '{group_name}'. Attempting to recover.")
         target_group["pages"] = [] 

    container_for_pages = target_group["pages"] 

    if nested_group_name:
        nested_group = next((item for item in target_group["pages"] if isinstance(item, dict) and item.get("group") == nested_group_name), None)
        if not nested_group:
            nested_group = {"group": nested_group_name, "pages": []}
            target_group["pages"].append(nested_group) 
            _log_issue(commit_message_reports_list, lang_code, "Info", f"Created new Nested Group '{nested_group_name}' in Group '{group_name}'.")
        
        nested_group.setdefault("pages", []) 
        if not isinstance(nested_group["pages"], list): 
            _log_issue(commit_message_reports_list, lang_code, "Critical", f"Internal state error: nested_group.pages is not a list for Nested Group '{nested_group_name}'. Attempting to recover.")
            nested_group["pages"] = [] 
        container_for_pages = nested_group["pages"] 
    
    return container_for_pages 

def get_group_sort_key(group_dict: dict, desired_order_list: list) -> int:
    """
    Calculates a sort key for a group based on its desired order.
    Groups not in the desired_order_list will be placed at the end.

    Args:
        group_dict: The group dictionary, expected to have a "group" key with its name.
        desired_order_list: A list of group names in their desired display order.

    Returns:
        An integer sort key. Lower numbers sort earlier.
    """
    group_name = group_dict.get("group", "") 
    try:
        return desired_order_list.index(group_name) 
    except ValueError:
        return len(desired_order_list) 

# --- Main Logic ---
def process_single_config(docs_config: dict, navigation_data: dict, commit_message_reports_list: list):
    """
    Processes a single language/documentation configuration.
    It updates the `navigation_data` by adding new pages, removing obsolete ones,
    and structuring them according to the configuration.

    Args:
        docs_config: A dictionary containing the configuration for a specific documentation set (e.g., PLUGIN_DEV_EN).
        navigation_data: The mutable main navigation data structure (specifically, the 'navigation' dict from docs_data).
        commit_message_reports_list: List for accumulating critical issue messages.
    """
    lang_code = docs_config["LANGUAGE_CODE"] 
    docs_dir_relative = docs_config["DOCS_DIR_RELATIVE"]
    docs_dir_abs = BASE_DIR / docs_dir_relative
    pwx_map = docs_config["PWX_TO_GROUP_MAP"]
    filename_pattern = docs_config["FILENAME_PATTERN"]
    target_tab_name = docs_config["TARGET_TAB_NAME"] 
    desired_group_order = docs_config["DESIRED_GROUP_ORDER"]

    _log_issue(commit_message_reports_list, lang_code, "Info", f"Processing Tab '{target_tab_name}'. Docs dir: '{docs_dir_abs}'")

    clear_tabs_if_refresh(navigation_data, lang_code, target_tab_name, refresh, commit_message_reports_list)
    
    existing_pages, target_version_nav, target_tab_nav = extract_existing_pages(navigation_data, lang_code, target_tab_name, commit_message_reports_list)

    if target_version_nav is None:
        _log_issue(commit_message_reports_list, lang_code, "Info", f"Version '{lang_code}' not found in docs.json, creating it.")
        navigation_data.setdefault("versions", []) 
        if not isinstance(navigation_data["versions"], list): 
            _log_issue(commit_message_reports_list, lang_code, "Critical", "Top-level 'navigation.versions' is not a list. Re-initializing.")
            navigation_data["versions"] = [] 
        target_version_nav = {"version": lang_code, "tabs": []}
        navigation_data["versions"].append(target_version_nav)
        existing_pages = set() 
        target_tab_nav = None  

    if target_tab_nav is None: 
        _log_issue(commit_message_reports_list, lang_code, "Info", f"Tab '{target_tab_name}' not found in version '{lang_code}'. It will be created if pages are added to it.")
        existing_pages = set()
        # Ensure target_version_nav.tabs exists for find_or_create_target_group
        target_version_nav.setdefault("tabs", [])
        if not isinstance(target_version_nav["tabs"], list):
            _log_issue(commit_message_reports_list, lang_code, "Critical", f"Version '{lang_code}' 'tabs' attribute is not a list. Re-initializing.")
            target_version_nav["tabs"] = []
        # Tab structure will be fully created by find_or_create_target_group when the first page is added.
        # If no pages are added, the tab might not appear unless explicitly created empty for sorting.
        # For now, rely on find_or_create_target_group.

    _log_issue(commit_message_reports_list, lang_code, "Info", f"{len(existing_pages)} existing pages found in docs.json for Tab '{target_tab_name}'.")

    filesystem_pages_map = {} 
    valid_filenames_for_processing = [] 

    if not docs_dir_abs.is_dir():
        _log_issue(commit_message_reports_list, lang_code, "Error", f"Documentation directory '{docs_dir_abs}' not found. Skipping file processing for this configuration.")
        return 

    for filename in os.listdir(docs_dir_abs):
        if not filename.endswith(".mdx"):
            continue 

        if filename_pattern.match(filename):
            try:
                page_path = get_page_path_from_filename(filename, docs_dir_relative)
                filesystem_pages_map[filename] = page_path
                valid_filenames_for_processing.append(filename)
            except ValueError as e: 
                _log_issue(commit_message_reports_list, lang_code, "Error", f"Error generating page path for '{filename}': {e}. Skipping this file.")
        else:
            _log_issue(commit_message_reports_list, lang_code, "SeriousWarning", f"File '{filename}' in '{docs_dir_relative}' is .mdx but does not match FILENAME_PATTERN. Skipping this file.")
    
    filesystem_page_paths_set = set(filesystem_pages_map.values())
    _log_issue(commit_message_reports_list, lang_code, "Info", f"{len(filesystem_page_paths_set)} valid .mdx files matching pattern found in '{docs_dir_relative}'.")

    new_page_paths = filesystem_page_paths_set - existing_pages
    removed_page_paths = existing_pages - filesystem_page_paths_set

    if new_page_paths:
        _log_issue(commit_message_reports_list, lang_code, "Info", f"{len(new_page_paths)} new page(s) to add to Tab '{target_tab_name}'.")
    if removed_page_paths:
        _log_issue(commit_message_reports_list, lang_code, "Info", f"{len(removed_page_paths)} obsolete page(s) to remove from Tab '{target_tab_name}'.")

    # Re-fetch target_tab_nav as it might have been None if the tab was new
    # This ensures we operate on the correct tab structure, especially if it was just created by find_or_create_target_group
    # or if it was pre-existing.
    # This ensures 'remove_obsolete_pages' gets the correct tab object.
    # Note: find_or_create_target_group modifies target_version_nav in-place.
    # We need to find the tab object within target_version_nav *after* any potential modifications.
    # This will be done before adding new pages and before sorting groups.

    _current_tab_for_removal = next((t for t in target_version_nav.get("tabs", []) if isinstance(t, dict) and t.get("tab") == target_tab_name), None)
    if removed_page_paths and _current_tab_for_removal: 
        remove_obsolete_pages(_current_tab_for_removal, removed_page_paths, commit_message_reports_list, lang_code)
    elif removed_page_paths: # Means there were pages to remove, but the tab itself wasn't found (edge case)
        _log_issue(commit_message_reports_list, lang_code, "Warning", f"Obsolete pages detected for Tab '{target_tab_name}', but the tab was not found in the current version structure. Removal skipped.")
        
    if new_page_paths:
        files_to_add_sorted = sorted([fn for fn, pp in filesystem_pages_map.items() if pp in new_page_paths])

        for filename in files_to_add_sorted:
            match = filename_pattern.match(filename)
            if not match: 
                _log_issue(commit_message_reports_list, lang_code, "InternalError", f"File '{filename}' was marked for addition but failed pattern match. Skipping.")
                continue

            pwxy_str = match.group(1) 
            page_path = filesystem_pages_map[filename] 

            if len(pwxy_str) < 3: 
                _log_issue(commit_message_reports_list, lang_code, "Error", f"File '{filename}' has an invalid PWXY prefix '{pwxy_str}' (too short). Skipping this file.")
                continue
            
            p, w, x = pwxy_str[0], pwxy_str[1], pwxy_str[2] 
            group_key = (p, w, x)

            if group_key in pwx_map:
                map_val = pwx_map[group_key]
                if not (isinstance(map_val, tuple) and (len(map_val) == 2 or len(map_val) == 3)):
                    _log_issue(commit_message_reports_list, lang_code, "ConfigError", f"PWX_TO_GROUP_MAP entry for key {group_key} has invalid format: {map_val}. Expected tuple of 2 or 3 strings. Skipping file '{filename}'.")
                    continue

                _tab_name_in_map, group_name_from_map = map_val[0], map_val[1]
                nested_group_name_from_map = map_val[2] if len(map_val) == 3 else None

                if _tab_name_in_map != target_tab_name:
                    _log_issue(commit_message_reports_list, lang_code, "Warning", f"File '{filename}' (PWX key {group_key}) maps to Tab '{_tab_name_in_map}' in PWX_TO_GROUP_MAP, but current processing is for Tab '{target_tab_name}'. Page will be added to '{target_tab_name}' under group '{group_name_from_map}'.")
                
                target_pages_container_list = find_or_create_target_group(
                    target_version_nav, target_tab_name, group_name_from_map, nested_group_name_from_map,
                    commit_message_reports_list, lang_code
                )
                if page_path not in target_pages_container_list:
                    target_pages_container_list.append(page_path)
                    _log_issue(commit_message_reports_list, lang_code, "Info", f"Added page '{page_path}' to Group '{group_name_from_map}' (Nested: {nested_group_name_from_map or 'No'}).")
                else:
                     _log_issue(commit_message_reports_list, lang_code, "Info", f"Page '{page_path}' already exists in Group '{group_name_from_map}' (Nested: {nested_group_name_from_map or 'No'}). Skipping addition.")
            else:
                _log_issue(commit_message_reports_list, lang_code, "SeriousWarning", f"File '{filename}' (PWX prefix ({p},{w},{x})) has no corresponding entry in PWX_TO_GROUP_MAP. Skipping this file.")

    # Final check for sorting: target_tab_nav needs to be the current state of the tab object.
    final_target_tab_nav = next((t for t in target_version_nav.get("tabs", []) if isinstance(t, dict) and t.get("tab") == target_tab_name), None)

    if final_target_tab_nav and "groups" in final_target_tab_nav and isinstance(final_target_tab_nav["groups"], list):
        if final_target_tab_nav["groups"]: 
            final_target_tab_nav["groups"].sort(key=lambda g: get_group_sort_key(g, desired_group_order))
            _log_issue(commit_message_reports_list, lang_code, "Info", f"Sorted groups in Tab '{target_tab_name}'.")
        else:
            _log_issue(commit_message_reports_list, lang_code, "Info", f"No groups to sort in Tab '{target_tab_name}' (tab is empty or contains no group structures).")
    elif final_target_tab_nav: 
         _log_issue(commit_message_reports_list, lang_code, "Warning", f"Tab '{target_tab_name}' exists but has no valid 'groups' list to sort.")
    else: # Tab was not created (e.g., no new pages and it didn't exist before)
        _log_issue(commit_message_reports_list, lang_code, "Info", f"Tab '{target_tab_name}' does not exist in the final structure; no sorting needed.")


def load_docs_data_robust(path: Path, commit_message_reports_list: list, lang_for_report: str = "GLOBAL") -> dict:
    """
    Loads docs.json data robustly. If file doesn't exist or is invalid, returns a default structure.

    Args:
        path: Path object to the docs.json file.
        commit_message_reports_list: List for accumulating critical issue messages.
        lang_for_report: Identifier for logging context (defaults to "GLOBAL").

    Returns:
        A dictionary with the loaded data or a default structure on failure.
    """
    default_structure = {"navigation": {"versions": []}}
    try:
        if not path.exists():
            _log_issue(commit_message_reports_list, lang_for_report, "Info", f"File '{path}' not found. Initializing with a new default structure.")
            return default_structure
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict) or \
               "navigation" not in data or not isinstance(data["navigation"], dict) or \
               "versions" not in data["navigation"] or not isinstance(data["navigation"]["versions"], list):
                _log_issue(commit_message_reports_list, lang_for_report, "Error", f"File '{path}' has an invalid root structure. Key 'navigation.versions' (as a list) is missing or malformed. Using default structure.")
                return default_structure
            return data
    except json.JSONDecodeError as e:
        _log_issue(commit_message_reports_list, lang_for_report, "Error", f"Failed to parse JSON from '{path}': {e}. Using default structure.")
        return default_structure
    except Exception as e: 
        _log_issue(commit_message_reports_list, lang_for_report, "Critical", f"Unexpected error loading file '{path}': {e}. Using default structure.")
        return default_structure

def save_docs_data_robust(path: Path, data: dict, commit_message_reports_list: list, lang_for_report: str = "GLOBAL") -> bool:
    """
    Saves data to docs.json robustly.

    Args:
        path: Path object to the docs.json file.
        data: The dictionary data to save.
        commit_message_reports_list: List for accumulating critical issue messages.
        lang_for_report: Identifier for logging context.

    Returns:
        True if save was successful, False otherwise.
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        _log_issue(commit_message_reports_list, lang_for_report, "Info", f"Successfully saved updates to '{path}'.")
        return True
    except Exception as e:
        _log_issue(commit_message_reports_list, lang_for_report, "Critical", f"Failed to save updates to '{path}': {e}.")
        return False

def validate_config(config: dict, config_name: str, commit_message_reports_list: list) -> bool:
    """
    Validates a single documentation configuration dictionary.

    Args:
        config: The configuration dictionary to validate.
        config_name: A name/identifier for the configuration (e.g., language code), used for logging.
        commit_message_reports_list: List for accumulating critical issue messages.

    Returns:
        True if the configuration is valid, False otherwise.
    """
    is_valid = True
    required_keys = [
        "DOCS_DIR_RELATIVE", "LANGUAGE_CODE", "FILE_EXTENSION_SUFFIX",
        "TARGET_TAB_NAME", "FILENAME_PATTERN", "PWX_TO_GROUP_MAP", "DESIRED_GROUP_ORDER"
    ]
    for key in required_keys:
        if key not in config:
            _log_issue(commit_message_reports_list, config_name, "ConfigError", f"Configuration is missing required key '{key}'.")
            is_valid = False
    
    if not is_valid: 
        _log_issue(commit_message_reports_list, config_name, "Info", f"Skipping configuration '{config_name}' due to missing required keys.")
        return False

    if not (isinstance(config["DOCS_DIR_RELATIVE"], str) and config["DOCS_DIR_RELATIVE"]):
        _log_issue(commit_message_reports_list, config_name, "ConfigError", f"Key 'DOCS_DIR_RELATIVE' must be a non-empty string. Found: '{config.get('DOCS_DIR_RELATIVE')}'.")
        is_valid = False
    if not isinstance(config["FILENAME_PATTERN"], re.Pattern): 
        _log_issue(commit_message_reports_list, config_name, "ConfigError", f"Key 'FILENAME_PATTERN' must be a compiled regular expression (re.Pattern). Found type: {type(config.get('FILENAME_PATTERN'))}.")
        is_valid = False
    if not (isinstance(config["PWX_TO_GROUP_MAP"], dict) and config["PWX_TO_GROUP_MAP"]): 
        _log_issue(commit_message_reports_list, config_name, "ConfigError", f"Key 'PWX_TO_GROUP_MAP' must be a non-empty dictionary. Found: '{config.get('PWX_TO_GROUP_MAP')}'.")
        is_valid = False
    if not isinstance(config["DESIRED_GROUP_ORDER"], list): 
        _log_issue(commit_message_reports_list, config_name, "ConfigError", f"Key 'DESIRED_GROUP_ORDER' must be a list. Found type: {type(config.get('DESIRED_GROUP_ORDER'))}.")
        is_valid = False

    if not is_valid:
        _log_issue(commit_message_reports_list, config_name, "Info", f"Skipping configuration '{config_name}' due to type or content errors in its definition.")
    return is_valid


def process_all_configs(configs_to_process: list[dict], docs_json_path: Path) -> list[str]:
    """
    Main orchestrator for processing all provided documentation configurations.
    Loads existing docs.json, processes each config, and saves the result.

    Args:
        configs_to_process: A list of configuration dictionaries.
        docs_json_path: Path to the docs.json file.

    Returns:
        A list of strings, where each string is a critical issue message formatted for a commit summary.
        Returns an empty list if no critical issues occurred.
    """
    commit_message_reports = [] 
    
    docs_data = load_docs_data_robust(docs_json_path, commit_message_reports) 
    
    navigation_data_to_modify = docs_data.setdefault("navigation", {})
    if not isinstance(navigation_data_to_modify, dict): 
        _log_issue(commit_message_reports, "GLOBAL", "Critical", "'navigation' key in docs.json is not a dictionary. Resetting to default structure.")
        docs_data["navigation"] = {"versions": []} 
        navigation_data_to_modify = docs_data["navigation"]

    navigation_data_to_modify.setdefault("versions", [])
    if not isinstance(navigation_data_to_modify.get("versions"), list): 
        _log_issue(commit_message_reports, "GLOBAL", "Error", "'navigation.versions' in docs.json was not a list. Resetting it to an empty list.")
        navigation_data_to_modify["versions"] = []

    processed_any_config_successfully = False
    for i, config_item in enumerate(configs_to_process):
        config_id = config_item.get("LANGUAGE_CODE", f"UnnamedConfig_{i+1}")
        
        _log_issue(commit_message_reports, config_id, "Info", f"Starting validation for configuration '{config_id}'.")
        if validate_config(config_item, config_id, commit_message_reports):
            _log_issue(commit_message_reports, config_id, "Info", f"Configuration '{config_id}' validated successfully. Starting processing.")
            try:
                process_single_config(config_item, navigation_data_to_modify, commit_message_reports)
                processed_any_config_successfully = True 
            except Exception as e:
                _log_issue(commit_message_reports, config_id, "Critical", f"Unhandled exception during processing of configuration '{config_id}': {e}.")
                import traceback
                tb_str = traceback.format_exc()
                print(f"TRACEBACK for configuration '{config_id}':\n{tb_str}")
        else:
            _log_issue(commit_message_reports, config_id, "Info", f"Configuration '{config_id}' failed validation. Skipping processing.")


    if processed_any_config_successfully: 
        _log_issue(commit_message_reports, "GLOBAL", "Info", "Attempting to save changes to docs.json.")
        save_docs_data_robust(docs_json_path, docs_data, commit_message_reports)
    elif not configs_to_process:
        _log_issue(commit_message_reports, "GLOBAL", "Info", "No configurations were provided to process.")
    else: 
        _log_issue(commit_message_reports, "GLOBAL", "Info", "No valid configurations were processed successfully. docs.json will not be modified.")

    return commit_message_reports 

def main_apply_docs_json() -> str:
    """
    Entry point for the script. Initializes configurations, processes them,
    and returns a status message for commit purposes.

    Returns:
        "success" if no critical issues were reported, otherwise a formatted string
        summarizing critical issues for a commit message.
    """
    print(f"Script base directory: {BASE_DIR}")
    print(f"Docs JSON path: {DOCS_JSON_PATH}")
    print(f"Refresh mode: {refresh}") 

    CONFIGS_TO_PROCESS = [
        PLUGIN_DEV_ZH,
        PLUGIN_DEV_EN,
        PLUGIN_DEV_JA,
    ]
    
    commit_message_parts = process_all_configs(CONFIGS_TO_PROCESS, DOCS_JSON_PATH)

    if not commit_message_parts: 
        return "success" 
    else:
        num_critical_issues = len(commit_message_parts)
        commit_summary_line = f"docs.json processed with {num_critical_issues} critical issue(s) reported."
        
        max_lines_for_commit_detail = 10 
        if len(commit_message_parts) > max_lines_for_commit_detail:
            detailed_issues_str = "\n".join(commit_message_parts[:max_lines_for_commit_detail]) + \
                                  f"\n... and {len(commit_message_parts) - max_lines_for_commit_detail} more critical issues (see full console logs for details)."
        else:
            detailed_issues_str = "\n".join(commit_message_parts)

        return f"{commit_summary_line}\n\nDetails of critical issues:\n{detailed_issues_str}"


if __name__ == "__main__":
    result_message = main_apply_docs_json()
    print("\n--- Script Execution Result ---")
    print(result_message)