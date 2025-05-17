import yaml  # pip install pyyaml
import re
import datetime
from pathlib import Path
import shutil
import sys


class Config:
    # --- Path Setup ---
    BASE_DIR = Path(__file__).resolve().parent.parent
    LANGUAGES = ["zh", "en", "ja"]  # Languages to process
    TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # --- Directory Naming Templates ---
    LANG_DIR_TEMPLATE = "plugin_dev_{lang}"
    ARCHIVE_LANG_DIR_PREFIX_TEMPLATE = "plugin_dev_{lang}_archive_pre_processing_"

    # --- PWXY Mappings ---
    PRIMARY_TYPE_MAP = {
        "conceptual": 1, "implementation": 2, "operational": 3, "reference": 4,
    }
    DEFAULT_W = 0
    DETAIL_TYPE_MAPS = {
        "conceptual": {"introduction": 1, "principles": 2, "architecture": 3},
        "implementation": {"basic": 1, "standard": 2, "high": 3, "advanced": 4},
        "operational": {"setup": 1, "deployment": 2, "maintenance": 3},
        "reference": {"core": 1, "configuration": 2, "examples": 3},
    }
    DEFAULT_X = 0
    LEVEL_MAP = {
        "beginner": 1, "intermediate": 2, "advanced": 3,
    }
    DEFAULT_Y = 0
    PRIORITY_NORMAL = 0
    PRIORITY_HIGH = 9
    PRIORITY_ADVANCED_LEVEL_KEY = "advanced"
    PRIORITY_IMPLEMENTATION_PRIMARY_KEY = "implementation"
    PRIORITY_IMPLEMENTATION_DETAIL_KEYS = {"high", "advanced"}

# --- Helper Functions ---

def extract_front_matter(content: str):
    match = re.match(r"^\s*---\s*$(.*?)^---\s*$(.*)",
                     content, re.DOTALL | re.MULTILINE)
    if match:
        yaml_str = match.group(1).strip()
        markdown_content = match.group(2).strip()
        try:
            front_matter = yaml.safe_load(yaml_str)
            if front_matter is None: front_matter = {} # Ensure it's a dict for empty YAML
            return (front_matter if isinstance(front_matter, dict) else {}), markdown_content
        except yaml.YAMLError as e:
            # This print is fine here as it's an early, critical parsing failure for a single file.
            print(f"  [Error] YAML Parsing Failed: {e}")
            return None, content # Indicate error
    return {}, content # No front matter found


def sanitize_filename_part(part: str) -> str:
    if not isinstance(part, str):
        part = str(part)
    part = part.lower().replace("&", "and").replace("@", "at")
    part = re.sub(r"\s+", "-", part)
    part = re.sub(r"[^\w\-.]+", "", part) # Allow dots
    part = part.strip(".-_")
    return part or "untitled"


def _calculate_pwxy_and_warnings(front_matter: dict, config: Config) -> tuple[int, int, int, int, list[str]]:
    warnings_messages = []
    dimensions = front_matter.get("dimensions", {})
    type_info = dimensions.get("type", {})
    primary = type_info.get("primary") # Will be present due to compliance check if we reach here
    detail = type_info.get("detail")   # Will be present
    level = dimensions.get("level")     # Will be present

    P = config.PRIORITY_NORMAL
    if level == config.PRIORITY_ADVANCED_LEVEL_KEY or \
       (primary == config.PRIORITY_IMPLEMENTATION_PRIMARY_KEY and detail in config.PRIORITY_IMPLEMENTATION_DETAIL_KEYS):
        P = config.PRIORITY_HIGH

    W = config.PRIMARY_TYPE_MAP.get(primary, config.DEFAULT_W)
    primary_detail_map = config.DETAIL_TYPE_MAPS.get(primary, {})
    X = primary_detail_map.get(detail, config.DEFAULT_X)
    Y = config.LEVEL_MAP.get(level, config.DEFAULT_Y)

    # Warnings for unmapped values (fields are assumed present from compliance check)
    if W == config.DEFAULT_W and primary is not None : # primary being None shouldn't happen if compliant
        warnings_messages.append(f"Unmapped primary type: '{primary}'. Using W={config.DEFAULT_W}")
    
    if X == config.DEFAULT_X and detail is not None: # detail being None shouldn't happen
        if primary in config.DETAIL_TYPE_MAPS:
             warnings_messages.append(f"Unmapped detail type: '{detail}' for primary '{primary}'. Using X={config.DEFAULT_X}")
        elif primary is not None: # Should always be true
             warnings_messages.append(f"No detail map defined for primary type: '{primary}'. Using X={config.DEFAULT_X}")
    
    if Y == config.DEFAULT_Y and level is not None: # level being None shouldn't happen
        warnings_messages.append(f"Unmapped level: '{level}'. Using Y={config.DEFAULT_Y}")

    return P, W, X, Y, warnings_messages


def _generate_filename_parts(
    P: int, W: int, X: int, Y: int,
    front_matter: dict,
    original_filename_stem: str
) -> tuple[str | None, str, str, list[str]]:
    warnings_messages = []
    prefix_str = f"{P}{W}{X}{Y}"
    try:
        padded_prefix = f"{int(prefix_str):04d}"
    except ValueError:
        warnings_messages.append(f"Could not form numeric prefix from P{P}W{W}X{X}Y{Y}. Using '0000'.")
        padded_prefix = "0000"

    standard_title = front_matter.get("standard_title") # Assumed present (not None) by compliance check
    title_part_to_use = standard_title
    if not title_part_to_use: # Handles standard_title: "" (empty string)
        warnings_messages.append("Empty 'standard_title'. Using original filename stem as fallback.")
        title_part_to_use = original_filename_stem
    sanitized_title = sanitize_filename_part(title_part_to_use)

    lang_suffix = ""
    language_fm = front_matter.get("language")
    if language_fm is not None: # Check for presence
        lang_code = str(language_fm).strip().lower()
        if lang_code: lang_suffix = f".{lang_code}"
        else: warnings_messages.append("Empty 'language' field in frontmatter. Omitting language suffix.")
    else: # language field is missing
        warnings_messages.append("Missing 'language' field in frontmatter. Omitting language suffix.")
    return padded_prefix, sanitized_title, lang_suffix, warnings_messages

# --- Core Processing Functions ---

def get_or_create_lang_dir(lang: str, config: Config) -> tuple[Path | None, bool]:
    lang_dir_path = config.BASE_DIR / config.LANG_DIR_TEMPLATE.format(lang=lang)
    was_newly_created = False
    if lang_dir_path.exists():
        if not lang_dir_path.is_dir():
            print(f"[ERROR] Path '{lang_dir_path}' exists but is not a directory. Skipping '{lang}'.")
            return None, False
        print(f"Using existing directory '{lang_dir_path.name}' for '{lang}'.")
    else:
        print(f"Directory '{lang_dir_path.name}' not found for '{lang}'. Creating it.")
        try:
            lang_dir_path.mkdir(parents=True, exist_ok=False)
            was_newly_created = True
            print(f"Created directory: '{lang_dir_path.name}' for '{lang}'.")
        except Exception as e: # Catch any OS or File system error
            print(f"[ERROR] Failed to create directory '{lang_dir_path}': {e}. Skipping '{lang}'.")
            return None, False
    return lang_dir_path, was_newly_created


def process_single_mdx_file(mdx_filepath: Path, config: Config) -> dict:
    stats = {
        "status": "processed", "all_file_warnings": [], "error_message": None, # all_file_warnings replaces warnings
        "old_filename_stem_for_replace": None, "new_filename_stem_for_replace": None,
        "problem_file_display_path": None, "problem_file_target_name": None,
        "non_compliant_reason": None,
    }

    try:
        if mdx_filepath.is_relative_to(config.BASE_DIR):
             # Show path relative to BASE_DIR's parent for context (e.g. "lang_dir/file.mdx")
            display_path = mdx_filepath.relative_to(config.BASE_DIR.parent).as_posix()
        else:
            display_path = mdx_filepath.name # Fallback
    except ValueError: # Should not happen if path is under BASE_DIR
        display_path = mdx_filepath.name
    stats["problem_file_display_path"] = display_path


    try:
        content = mdx_filepath.read_text(encoding="utf-8")
        front_matter, _ = extract_front_matter(content)

        if front_matter is None: # YAML Parsing Error from extract_front_matter
            stats["status"] = "error"; stats["error_message"] = "YAML Error in file."
            # The extract_front_matter already printed details
            print(f"\nProcessing: {display_path} -> (skipped due to YAML error)")
            return stats

        # --- Check for critical missing frontmatter for renaming compliance ---
        missing_critical_fields = []
        fm_dimensions = front_matter.get("dimensions", {})
        fm_type = fm_dimensions.get("type", {})

        if fm_type.get("primary") is None: missing_critical_fields.append("dimensions.type.primary")
        if fm_type.get("detail") is None: missing_critical_fields.append("dimensions.type.detail")
        if fm_dimensions.get("level") is None: missing_critical_fields.append("dimensions.level")
        if front_matter.get("standard_title") is None: missing_critical_fields.append("standard_title")

        if missing_critical_fields:
            stats["status"] = "skipped_non_compliant"
            reason = f"\nMissing critical frontmatter fields for renaming: {', '.join(missing_critical_fields)}."
            stats["non_compliant_reason"] = reason
            # This skip will be reported as a problem, so print concise info here
            print(f"\nProcessing: {display_path} -> (skipped, non-compliant)")
            print(f"  [Skipping Reason] {reason}")
            return stats # No further processing or warning generation for this file

        # --- If compliant, proceed to calculate and generate parts ---
        P, W, X, Y, pwxy_warnings = _calculate_pwxy_and_warnings(front_matter, config)
        stats["all_file_warnings"].extend(pwxy_warnings)

        original_stem_for_title_fallback = mdx_filepath.stem
        padded_prefix, sanitized_title, lang_suffix, fname_warnings = _generate_filename_parts(
            P, W, X, Y, front_matter, original_stem_for_title_fallback)
        stats["all_file_warnings"].extend(fname_warnings)

        new_filename = f"{padded_prefix}-{sanitized_title}{lang_suffix}.mdx"
        stats["problem_file_target_name"] = new_filename
        new_filepath = mdx_filepath.with_name(new_filename)

        if new_filepath == mdx_filepath:
            stats["status"] = "skipped_no_change"
        elif new_filepath.exists():
            stats["status"] = "skipped_target_exists"
        else:
            try:
                original_stem_before_rename = mdx_filepath.stem
                mdx_filepath.rename(new_filepath)
                stats["status"] = "processed"
                stats["old_filename_stem_for_replace"] = original_stem_before_rename
                stats["new_filename_stem_for_replace"] = new_filepath.stem
            except Exception as rename_error:
                stats["status"] = "error"
                stats["error_message"] = f"Failed to rename to '{new_filename}': {rename_error}"
        
        # Print details if warnings, actual change, error, or specific skips (except non-compliant already printed)
        action_taken = new_filepath != mdx_filepath and stats["status"] == "processed"
        if stats["all_file_warnings"] or action_taken or stats["status"].startswith("error") or stats["status"] == "skipped_target_exists":
            print(f"\nProcessing: {display_path} -> {new_filename if action_taken else '(no change or skipped/error)'}")
            for warning_msg in stats["all_file_warnings"]: print(f"  [Warning] {warning_msg}") # These will now be problem reports
            if stats["status"] == "skipped_target_exists": print(f"  [Skipping] Target '{new_filename}' already exists.")
            if stats["error_message"]: print(f"  [Error] {stats['error_message']}")


    except FileNotFoundError: # Should be rare if mdx_filepath comes from rglob
        stats["status"] = "error"; stats["error_message"] = f"File not found: {mdx_filepath.name}"
        print(f"\nProcessing: {display_path}"); print(f"  [Error] {stats['error_message']}")
    except Exception as e:
        stats["status"] = "error"; stats["error_message"] = f"Unexpected error: {e}"
        print(f"\nProcessing: {display_path}"); print(f"  [Error] Unexpected error processing file: {e}")
        import traceback; traceback.print_exc()
    return stats


def run_processing_for_language(lang_dir_path: Path, config: Config) -> dict:
    print(f"Starting in-place processing for: {lang_dir_path.name}")
    lang_stats = {
        "processed_count": 0, "skipped_no_change_count": 0,
        "skipped_target_exists_count": 0, "error_count": 0,
        "warning_files_count": 0, # This counts files that HAD warnings.
        "status": "OK",
        "dir_path_str": str(lang_dir_path.relative_to(config.BASE_DIR)), # Path relative to project root
        "content_replacements_made_count": 0, "content_replacement_errors_count": 0,
        "error_file_details": [], "skipped_target_exists_details": [],
        "content_replacement_error_details": [],
        "skipped_non_compliant_count": 0,
        "skipped_non_compliant_details": [],
        "files_with_processing_warnings_details": [], # New: to store path and specific warnings
    }

    if not lang_dir_path.exists() or not lang_dir_path.is_dir():
        lang_stats["status"] = "LANG_DIR_ERROR"
        print(f"[Error] Language directory '{lang_dir_path.name}' issue (not found or not a dir).")
        return lang_stats

    print(f"\n--- Phase 1: Renaming files in '{lang_dir_path.name}' ---")
    mdx_files = sorted(list(lang_dir_path.rglob("*.mdx")))
    total_files = len(mdx_files)
    print(f"Found {total_files} MDX files for renaming phase.")
    rename_mappings = []

    for i, mdx_filepath in enumerate(mdx_files):
        result = process_single_mdx_file(mdx_filepath, config)
        status = result["status"]

        if status == "processed":
            lang_stats["processed_count"] += 1
            old, new = result.get("old_filename_stem_for_replace"), result.get("new_filename_stem_for_replace")
            if old and new and old != new: rename_mappings.append((old, new))
        elif status == "skipped_no_change": lang_stats["skipped_no_change_count"] += 1
        elif status == "skipped_target_exists":
            lang_stats["skipped_target_exists_count"] += 1
            lang_stats["skipped_target_exists_details"].append({
                "original_display_path": result["problem_file_display_path"],
                "target_name": result["problem_file_target_name"]
            })
        elif status == "skipped_non_compliant":
            lang_stats["skipped_non_compliant_count"] += 1
            lang_stats["skipped_non_compliant_details"].append({
                "path": result["problem_file_display_path"],
                "reason": result["non_compliant_reason"]
            })
        elif status == "error":
            lang_stats["error_count"] += 1
            lang_stats["error_file_details"].append({
                "path": result["problem_file_display_path"], "message": result["error_message"]
            })
        
        if result["all_file_warnings"]: # If there were any warnings for this file
            lang_stats["warning_files_count"] += 1 # Increment count of files with warnings
            lang_stats["files_with_processing_warnings_details"].append({ # Store details for problem reporting
                "path": result["problem_file_display_path"],
                "warnings": result["all_file_warnings"]
            })

        if total_files > 0: print(f"Rename Progress ({lang_dir_path.name}): {i+1}/{total_files} ({((i+1)/total_files*100):.1f}%)", end="\r")

    if total_files > 0: print() # Newline after progress
    print("--- Phase 1: Renaming files complete. ---")

    if rename_mappings:
        print(f"\n--- Phase 2: Updating content references in '{lang_dir_path.name}' ({len(rename_mappings)} filename changes to propagate) ---")
        all_mdx_after_rename = sorted(list(lang_dir_path.rglob("*.mdx")))
        total_replace_scan = len(all_mdx_after_rename)
        print(f"Scanning {total_replace_scan} .mdx files for content updates.")
        updated_count = 0
        for i, scan_path in enumerate(all_mdx_after_rename):
            display_scan_path = scan_path.relative_to(config.BASE_DIR.parent).as_posix() # Consistent display path
            try:
                content, changed = scan_path.read_text(encoding="utf-8"), False
                mod_content = content
                for old, new in rename_mappings:
                    if old in mod_content: mod_content, changed = mod_content.replace(old, new), True
                if changed:
                    scan_path.write_text(mod_content, encoding="utf-8")
                    updated_count +=1; print(f"  Updated references in: {display_scan_path}")
            except Exception as e:
                err_msg = f"Failed to update references in {display_scan_path}: {e}"
                print(f"  [Error] {err_msg}")
                lang_stats["content_replacement_errors_count"] += 1
                lang_stats["content_replacement_error_details"].append({"path": display_scan_path, "error": str(e)})
            if total_replace_scan > 0: print(f"Content Update Progress ({lang_dir_path.name}): {i+1}/{total_replace_scan} ({((i+1)/total_replace_scan*100):.1f}%)", end="\r")
        if total_replace_scan > 0: print() # Newline after progress
        lang_stats["content_replacements_made_count"] = updated_count
        print(f"Content replacement phase: {updated_count} files had their content updated.")
        print("--- Phase 2: Content references update complete. ---")
    else: print("\nNo renames occurred, skipping content reference update phase.")

    print("-" * 20 + f"\nLanguage Processing Summary ({lang_dir_path.name}):")
    print(f"  Processed (renamed): {lang_stats['processed_count']}")
    print(f"  Skipped (no change): {lang_stats['skipped_no_change_count']}")
    print(f"  Skipped (target exists): {lang_stats['skipped_target_exists_count']}")
    print(f"  Skipped (non-compliant for rename): {lang_stats['skipped_non_compliant_count']}")
    print(f"  Files generating warnings: {lang_stats['warning_files_count']}") # Renamed for clarity
    print(f"  Errors (renaming phase): {lang_stats['error_count']}")
    if rename_mappings or lang_stats['content_replacement_errors_count'] > 0 or lang_stats['content_replacements_made_count'] > 0:
        print(f"  Content updated (references): {lang_stats['content_replacements_made_count']}")
        print(f"  Errors (content update): {lang_stats['content_replacement_errors_count']}")
    print("-" * 20)

    # A language dir has errors if file errors or content replacement errors occurred.
    # Non-compliant skips or warnings are now also reported as "problems" at main level,
    # but don't change the "ERRORS_IN_PROCESSING" status of the language itself here.
    # The main problem report will cover those.
    if lang_stats["error_count"] > 0 or lang_stats["content_replacement_errors_count"] > 0:
        lang_stats["status"] = "ERRORS_IN_PROCESSING"
    return lang_stats


def main_rename_by_dimensions() -> str: # Return type is now str
    config = Config()
    print(f"Base directory: {config.BASE_DIR}\nTimestamp for this run: {config.TIMESTAMP}")
    overall_summary, lang_dir_created_flags, lang_dirs_map = {}, {}, {}
    problem_reports_list = [] # Internal list to build up problem strings

    for lang in config.LANGUAGES:
        print(f"\n{'='*10} Processing Language: {lang.upper()} {'='*10}")
        current_lang_dir, was_newly_created = get_or_create_lang_dir(lang, config)
        lang_dir_created_flags[lang], lang_dirs_map[lang] = was_newly_created, current_lang_dir

        if not current_lang_dir:
            msg = f"Failed to get or create language directory for '{lang}'."
            overall_summary[lang] = {"status": "SETUP_ERROR", "message": msg}
            problem_reports_list.append(f"- Lang '{lang}': Setup Error - {msg}")
            continue
        
        lang_results = run_processing_for_language(current_lang_dir, config)
        overall_summary[lang] = lang_results

        # Cleanup empty newly created directory
        if current_lang_dir and was_newly_created and current_lang_dir.exists() and not any(current_lang_dir.iterdir()):
            try:
                current_lang_dir.rmdir(); print(f"  Removed empty newly created language directory: {current_lang_dir.name}")
                lang_dirs_map[lang] = None # Mark as gone
                # No need to add to lang_results["message"] as it's a normal cleanup
            except OSError as e: print(f"  Note: Could not remove empty newly created directory '{current_lang_dir.name}': {e}")

    print("\n\n" + "=" * 20 + " Overall Script Summary " + "=" * 20)
    for lang_code in config.LANGUAGES:
        summary = overall_summary.get(lang_code, {})
        lang_dir_path_obj = lang_dirs_map.get(lang_code)

        print(f"\nLanguage: {lang_code.upper()}\n  Status: {summary.get('status', 'UNKNOWN')}")
        
        if "message" in summary and summary['status'] in ["SETUP_ERROR", "LANG_DIR_ERROR"]: # Critical setup messages
            print(f"  Message: {summary['message']}")
        
        if summary.get('status') not in ["SETUP_ERROR", "LANG_DIR_ERROR"]:
            print(f"  Directory: {summary.get('dir_path_str', 'N/A')}")
            for key, label in [
                ("processed_count", "Processed (renamed)"),
                ("skipped_no_change_count", "Skipped (no change)"),
                ("skipped_target_exists_count", "Skipped (target exists)"),
                ("skipped_non_compliant_count", "Skipped (non-compliant for rename)"),
                ("warning_files_count", "Files generating warnings"),
                ("error_count", "Errors (renaming phase)"),
                ("content_replacements_made_count", "Content updated (references)"),
                ("content_replacement_errors_count", "Errors (content update)")
            ]: # Iterate common stats
                if key in summary: print(f"  {label}: {summary.get(key, 0)}")

            # Collect problem reports for return
            for detail in summary.get("error_file_details", []):
                problem_reports_list.append(f"- Lang '{lang_code}': File '{detail['path']}' - Renaming error: {detail['message']}")
            for detail in summary.get("skipped_target_exists_details", []):
                problem_reports_list.append(f"- Lang '{lang_code}': File '{detail['original_display_path']}' could not be renamed to '{detail['target_name']}' (target exists).")
            for detail in summary.get("skipped_non_compliant_details", []): # Now a problem
                problem_reports_list.append(f"- Lang '{lang_code}': File '{detail['path']}' - Skipped (non-compliant): {detail['reason']}")
            for detail in summary.get("files_with_processing_warnings_details", []): # Now a problem
                warnings_str = "; ".join(detail['warnings'])
                problem_reports_list.append(f"- Lang '{lang_code}': File '{detail['path']}' - Processing Warnings: {warnings_str}")
            for detail in summary.get("content_replacement_error_details", []):
                problem_reports_list.append(f"- Lang '{lang_code}': File '{detail['path']}' - Content replacement error: {detail['error']}")
        
        if lang_dir_path_obj and lang_dir_path_obj.exists():
            print(f"  Final directory location: {lang_dir_path_obj.name}")
        elif lang_dir_created_flags.get(lang_code) and not lang_dir_path_obj: # Was new, now gone
            print("  Note: Empty newly created directory was removed as expected.")
        elif not lang_dir_path_obj and summary.get('status') != "SETUP_ERROR": # Not a setup error, but dir is gone
            print(f"  Note: Language directory '{config.LANG_DIR_TEMPLATE.format(lang=lang_code)}' may have been archived or removed by other means.")
            
    print("=" * (40 + len(" Overall Script Summary ")))

    if not problem_reports_list:
        return "success"
    else:
        return "\n".join(problem_reports_list)


if __name__ == "__main__":
    result_message = main_rename_by_dimensions()
    print("\n--- Script Execution Result ---")
    print(result_message)