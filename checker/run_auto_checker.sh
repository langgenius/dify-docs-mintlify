#!/bin/bash
# 运行自动文档链接检查工具

# 安装必要依赖
pip install -r requirements.txt

# 安装Playwright浏览器
python -m playwright install chromium

# 运行检查脚本
echo "启动自动链接检查工具..."
python auto_link_checker.py
