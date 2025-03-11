# 打包为本地文件与分享

完成插件开发后，你可以将插件项目打包为一个本地文件并分享给他人，通过插件文件后即可安装至 Dify Workspace 内。

* **特点**：
  * 便于**版本管理**和**开源共享**。
  * 用户可通过插件链接直接安装，无需平台审核。
* **发布流程**：
  * 将插件代码推送至 GitHub 仓库。
  * 分享仓库链接，用户可通过链接将插件集成至 **Dify Workspace**。

本文将介绍如何将插件项目打包为本地文件，以及如何使用本地文件安装插件。

### 前置准备

* **Dify 插件开发工具**，详细说明请参考[初始化开发工具](../quick-start/develop-plugins/initialize-development-tools.md)。

配置完成后，在终端输入 `dify version` 命令，检查是否输出版本号信息以确认已安装必要的开发工具。

### 打包插件

> 打包插件前，请确保插件的 `manifest.yaml` 文件和 `/provider` 路径下的 `.yaml` 文件中的 `author` 字段与 GitHub ID 保持一致。

插件项目开发完成后，请确保已完成[远程连接测试](../quick-start/develop-plugins/extension-plugin.md#tiao-shi-cha-jian)。需前往插件项目的上一级目录，运行以下插件打包命令：

```bash
dify plugin package ./your_plugin_project
```

运行命令后将在当前路径下生成以 `.difypkg` 后缀结尾的文件。

![生成插件文件](https://assets-docs.dify.ai/2024/12/98e09c04273eace8fe6e5ac976443cca.png)

### 安装插件

访问 Dify 插件管理页，轻点右上角的**安装插件** → **通过本地文件**安装，或将插件文件拖拽至页面空白处安装插件。

![安装插件文件](https://assets-docs.dify.ai/2024/12/8c31c4025a070f23455799f942b91a57.png)

### 发布插件

你可以将插件文件分享给他人，或上传至互联网供他人下载。



