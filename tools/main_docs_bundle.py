import os
import sys

from rename_by_dimensions import main_rename_by_dimensions
from contributing_in_page import main_contributing_in_page
from apply_docs_json import main_apply_docs_json


def set_github_output(name, value):
    github_output = os.environ.get('GITHUB_OUTPUT')
    if github_output:
        with open(github_output, 'a') as f:
            if '\n' in str(value):
                f.write(f"{name}<<EOF\n")
                f.write(f"{value}\n")
                f.write("EOF\n")
            else:
                f.write(f"{name}={value}\n")
    else:
        print(f"[GitHub Output] {name}={value}")

def main():
    total_message = " \n"
    success_count = 0
    error_count = 0

    try:
        result_rename = main_rename_by_dimensions()
        if result_rename == "success":
            success_count += 1
        else:
            error_count += 1
            total_message += f"Rename operation failed: {result_rename}\n"
    except Exception as e:
        error_count += 1
        total_message += f"Rename operation error: {str(e)}\n"
    
    try:
        result_contributing = main_contributing_in_page()
        if result_contributing == "success":
            success_count += 1
        else:
            error_count += 1
            total_message += f"Contributing guide processing failed: {result_contributing}\n"
    except Exception as e:
        error_count += 1
        total_message += f"Contributing guide processing error: {str(e)}\n"
    
    try:
        result_apply = main_apply_docs_json()
        if result_apply == "success":
            success_count += 1
        else:
            error_count += 1
            total_message += f"Docs JSON application failed: {result_apply}\n"
    except Exception as e:
        error_count += 1
        total_message += f"Docs JSON application error: {str(e)}\n"
    
    if error_count == 0:
        commit_message = f"Docs tools: Successfully completed {success_count} operations"
        print("All tools executed successfully.")
    else:
        commit_message = f"Docs tools: {success_count} succeeded, some failed"
        print("Some tools encountered issues:")
        print(total_message)
    
    set_github_output("commit_message", commit_message)
    set_github_output("detailed_message", total_message)
    set_github_output("success_count", str(success_count))
    set_github_output("error_count", str(error_count))

if __name__ == "__main__":
    main()