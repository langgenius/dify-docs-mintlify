---
description: 'Author: Allen'
---

# 安装与使用插件

### 安装插件

点击 Dify 平台右上角的“插件”，前往插件管理页，支持通过 **Marketplace、GitHub、上传本地文件**三种方式安装插件。

![安装插件](https://assets-docs.dify.ai/2025/01/a56c40245090d9252557dcc6f4064a14.png)

#### Marketplace

你可以选择任意插件，点&#x51FB;**“安装”**&#x6309;钮将插件安装至当前 Workspace 内。

![通过 Marketplace 安装插件](https://assets-docs.dify.ai/2025/01/6ae8b661b7fa01b228a954d00ef552f3.png)

#### GitHub

你可以直接通过 GitHub 代码仓库链接安装插件，使用此方法安装插件时需确保插件满足代码规范。插件代码仓库需创建 Release 并在附件中包含 `.difypkg` 后缀的文件包。详细说明请参考[发布插件：GitHub](../publish-plugins/publish-plugin-on-personal-github-repo.md)。

![通过 GitHub 安装](https://assets-docs.dify.ai/2025/01/4026a12a915e3fe9bd057d8827acfdce.png)

**上传本地文件**

本地文件指的是 `.difypkg` 后缀的文件包，常用于离线环境或测试环境。开发者可通过此方式安装除官方市场以外的插件文件。对于组织而言，可以开发维护内部插件并通过本地上传的方式安装，避免公开敏感信息。

关于如何打包插件并获取 `.difypkg` 文件，详细说明请参考[打包插件](../publish-plugins/package-plugin-file-and-publish.md)。

### 使用插件

将插件安装至 Workspace 后即可在 Dify 应用内进行使用。下文将简要介绍不同类型的插件对应不同的使用方法。

#### 模型插件

以 `OpenAI` 为例，安装模型插件后，点击右上角的**头像页 → 设置 → 模型供应商**，配置 API Key 即可激活该模型供应商。

![授权 OpenAI API Key](https://assets-docs.dify.ai/2025/01/3bf32d49975931e5924baa749aa7812f.png)

授权后可以在所有应用类型内选择并使用该大语言模型。

![使用模型类型插件](https://assets-docs.dify.ai/2024/12/4a38b1ea534ca68515839c518c250d2f.png)

#### 工具插件

工具插件支持在 Chatflow、Workflow、Agent 应用内使用。部分插件在安装后可能还要求进行 API Key 或其它形式的授权，手动添加授权后才能正常使用。

> API Key 属敏感信息，授权仅对当前用户有效。团队中的其他人使用该插件时仍需手动输入授权密钥。

本章节将以 `Google Search` 工具为例，介绍如何使用工具插件。在 Dify Marketplace 搜索并安装插件后，按照页面提示输入 API Key 完成插件授权过程。

![授权插件](https://assets-docs.dify.ai/2024/11/972de4c9fa00f792a1ab734b080aafdc.png)

#### Agent

创建 Agent 应用后，在应用编排页下方找到 **“工具”** 选项。选中已安装的工具插件。

使用应用时，输入使用工具的指令文本，例如输入 “当日新闻” 即可调用插件使用谷歌搜索引擎进行在线内容检索。

![Agent 工具](https://assets-docs.dify.ai/2024/12/78f833811cb0c3d5cbbb1a941cffc769.png)

#### Chatflow / Workflow

Chatflow 和 Workflow 类型应用共用一套工作流编排画布，因此工具插件的使用方法一致。

你可以点击节点末尾的 + 号，选择已安装的谷歌插件工具，并将节点与上游节点相连线。

![Chatflow / Workflow 工具](https://assets-docs.dify.ai/2024/12/7e7bcf1f9e3acf72c6917ea9de4e4613.png)

在插件的输入变量中填写用户输入的查询内容 query 变量，或其它需要在线检索的信息。

![Tools 输入项](https://assets-docs.dify.ai/2024/12/a67c4cffd8fdf33297d462b2e6d01d27.png)

你已了解如何使用 `Google Search` 工具。如需了解其它插件的使用方法，请参考插件详情页的指导使用插件。

![使用插件](https://assets-docs.dify.ai/2025/01/9d826302637638f705a94f73bd653958.png)

### 阅读更多

如需了解如何上手开发插件，请阅读以下内容：

{% content-ref url="develop-plugins/" %}
[develop-plugins](develop-plugins/)
{% endcontent-ref %}
