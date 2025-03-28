#!/bin/bash
# 运行交互式文档链接检查工具

# 设置Python环境（按需修改）
# export PYTHONPATH=/path/to/your/python

# 安装必要依赖
pip install requests colorama

# 设置输出文件
OUTPUT_FILE="link_check_report_$(date +%Y%m%d_%H%M%S).md"

# 运行检查脚本
echo "开始交互式检查文档链接..."

# 检查单个文件模式
python interactive_link_checker.py --file ../checker/gitbook-all-doc-links-mintlify.md --output $OUTPUT_FILE

# 检查目录模式（注释掉上面的命令，取消注释下面的命令）
# python interactive_link_checker.py --dir .. --output $OUTPUT_FILE

echo "检查完成，报告已保存至: $OUTPUT_FILE"
