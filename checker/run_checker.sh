#!/bin/bash
# 运行文档链接检查工具

# 设置Python环境（按需修改）
# export PYTHONPATH=/path/to/your/python

# 安装必要依赖
pip install requests

# 设置输出文件
OUTPUT_FILE="link_check_report_$(date +%Y%m%d_%H%M%S).md"

# 运行检查脚本
echo "开始检查文档链接..."
python doc_link_checker.py --dir .. --output $OUTPUT_FILE

echo "检查完成，报告已保存至: $OUTPUT_FILE"
