# Dify文档链接检查工具

这个工具可以自动检查Dify文档中的链接，并生成详细的检查报告。

## 工具版本

本目录包含三个版本的链接检查工具：

1. `doc_link_checker.py` - 原始自动检查器，多线程模式
2. `interactive_link_checker.py` - 交互式检查器，可以手动确认并查看每个链接
3. `auto_link_checker.py` - 新版自动检查器，使用浏览器检查图片和子链接

## 特色功能

### 新版自动检查器特点 (auto_link_checker.py)

- 使用浏览器引擎检查所有链接
- 支持有头/无头浏览器模式
- 自动检查图片是否可以正常加载
- 自动检测页面内的子链接
- 生成包含图片和子链接状态的详细报告

### 交互式检查器特点 (interactive_link_checker.py)

- 逐个检查链接，交互式确认
- 可以直接在浏览器中打开链接查看
- 彩色输出，清晰显示问题
- 可手动标记具体问题类型和描述
- 按文件交互式检查，可选择跳过文件

### 原始自动检查器特点 (doc_link_checker.py)

- 扫描Markdown文件中的所有链接
- 检测链接跳转问题
- 识别README链接自动跳转到首页的情况
- 检测图片引用情况
- 生成详细的Markdown报告
- 支持并发检查提高效率

## 使用方法

### 安装依赖

```bash
pip install -r requirements.txt
```

### 使用新版自动检查器

1. 直接运行自动检查脚本：

```bash
python auto_link_checker.py
```

2. 按照提示输入：
   - 链接文件路径
   - 选择浏览器模式（有头/无头）
   - 可选择自定义输出报告路径

3. 或使用快速运行脚本：

```bash
chmod +x run_auto_checker.sh
./run_auto_checker.sh
```

### 交互式检查

```bash
python interactive_link_checker.py
```

### 自动检查

```bash
python doc_link_checker.py --file /path/to/your/file.md --output report.md
```

## 输出报告

报告采用Markdown格式，包含以下内容：

- 检查总结（链接总数、正常数量、异常数量）
- 异常情况记录（跳转、错误、超时等）
- README链接跳转问题总结
- 对于新版自动检查器，还包含图片和子链接状态
- 详细检查结果表格

## 注意事项

- 脚本默认只检查docs.dify.dev域名下的链接
- 新版自动检查器需要安装Chrome浏览器
- 可通过修改代码中的`base_url`参数来检查其他域名
