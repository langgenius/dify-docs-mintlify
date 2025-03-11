# 发布至个人 GitHub 仓库

支持通过 GitHub 仓库链接安装插件。插件开发完成后，你可以选择将插件发布至公开 GitHub 仓库供其他人下载和使用。该方式具备以下优势：

• **个人管理**：你可以完全控制插件的代码和更新

• **快速分享**：通过 GitHub 链接即可轻松分享给其他用户或团队成员，便于测试和使用

• **协作与反馈**：将插件开源后，有可能会吸引 GitHub 上潜在的协作者，帮助您快速改进插件

本文将指导你如何将插件发布到 GitHub 仓库。

### 准备工作

* GitHub 账号
* 创建一个新的公开 GitHub 仓库
* 本地已安装 Git 工具

关于 GitHub 的基础知识，请参考 [GitHub 文档](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)。

### 1. 完善插件项目

将上传至公开的 GitHub 意味着你将公开插件。请确保你已完成插件的调试和验证，并已完善插件的 `README.md` 文件说明。

建议说明文件包含以下内容：

* 插件的简介和功能描述
* 安装和配置步骤
* 使用示例
* 联系方式或贡献指南

### 2. 初始化本地插件仓库

将插件公开上传至 GitHub 之前，请确保已完成插件的调试和验证工作。在终端中导航到插件项目文件夹，并运行以下命令：

```bash
git init
git add .
git commit -m "Initial commit: Add plugin files"
```

如果你是第一次使用 Git，可能还需要配置 Git 用户名和邮箱：

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. 连接远程仓库

使用以下命令，将本地仓库连接到 GitHub 仓库：

```bash
git remote add origin https://github.com/<your-username>/<repository-name>.git
```

### 4. 上传插件文件

> 打包插件前，请确保插件的 `manifest.yaml` 文件和 `/provider` 路径下的 `.yaml` 文件中的 author 字段与 GitHub ID 保持一致。

将插件项目推送到 GitHub 仓库：

```bash
git branch -M main
git push -u origin main
```

上传代码时建议附上标签，以便后续打包代码。

```bash
git tag -a v0.0.1 -m "Release version 0.0.1"

git push origin v0.0.1
```

### 5. 打包插件代码

前往 GitHub 代码仓库的 Releases 页，创建一个新的版本发布。发布版本时需上传插件文件。关于如何打包插件文件，详细说明请阅读[打包插件](broken-reference)。

![打包插件](https://assets-docs.dify.ai/2024/12/5cb4696348cc6903e380287fce8f529d.png)

### 通过 GitHub 安装插件

其他人可以通过 GitHub 仓库地址安装该插件。访问 Dify 平台的插件管理页，选择通过 GitHub 安装插件，输入仓库地址后，选择版本号和包文件完成安装。

![](https://assets-docs.dify.ai/2024/12/3c2612349c67e6898a1f33a7cc320468.png)



