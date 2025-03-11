---
description: 'Author: Yeuoly, Allen'
---

# 功能简介

> 如需在社区版中体验插件功能，请将版本号升级至 v1.0.0。

### 什么是插件？

这是一个对开发者更加友好，可扩展性更强的第三方服务扩展模块。虽然 Dify 平台已内置多个由官方维护与社区贡献者开发的工具，但现有的工具难以全面覆盖各类细分场景的需求，而一个新工具的开发到嵌入 至平台又需要较长周期。

为了让开发过程更加敏捷，我们决定开放生态并提供完善的插件开发 SDK，让每位开发者都能够轻松地打造属于自己的工具，轻松使用**第三方模型与工具**，显著提升应用能力。

### 插件有哪些优势？

新的插件系统突破了原有框架的限制，提供更丰富和强大的扩展能力。提供五种类型插件，每一种类型对应成熟的场景解决方案，赋予开发者用无限的创意改造 Dify 应用的空间。

同时，插件系统还具备更加友好的传播属性，你可以通过 [Dify Marketplace](https://marketplace.dify.ai/) 或 [GitHub](publish-plugins/publish-plugin-on-personal-github-repo.md) 以及[本地文件](publish-plugins/package-and-publish-plugin-file.md)的形式分享你的插件，让其他开发者能够便捷地安装插件。

> Dify Marketplace 是一个面向开发者的开放生态系统，提供模型、工具、AI Agent、Extensions 和插件包等丰富的资源。通过 Marketplace，你可以为现有 Dify 应用无缝接入第三方服务，增强现有应用的能力，共同推动 Dify 生态的发展。

无论你是想要接入新的模型、添加特定工具帮助扩展 Dify 平台的现有功能，都可以在丰富的插件市场里找到所需资源。**我们希望更多的开发者能够参与共建 Dify 生态并从中获益。**

![Dify Plugin Marketplace](https://assets-docs.dify.ai/2025/01/83f9566063db7ae4886f6a139f3f81ff.png)

### 插件有哪些类型？

*   **Models（模型）**

    各类 AI 模型的接入插件，支持[模型服务商](quick-start/develop-plugins/model-plugin/integrate-the-predefined-model.md)和[自定义模型](quick-start/develop-plugins/model-plugin/customizable-model.md)两种类型，能够极大降低配置和调用 LLM API 的门槛。关于模型插件的开发详情，请参考[快速开始： Model 插件](quick-start/develop-plugins/model-plugin/)。
*   **Tools（工具）**

    工具指的是能够被 Chatflow / Workflow / Agent 类型应用所调用的第三方服务。提供完整的 API 实现能力，用于增强 Dify 应用的能力。例如开发一个 Google 搜索插件，详情请参考[快速开始：Tool 插件](quick-start/develop-plugins/tool-type-plugin.md)。
*   **Agent 策略**

    Agent 策略插件能够定义 [Agent 节点](../guides/workflow/node/agent.md)内部的推理和决策逻辑，包括 LLM 对于工具选择、调用以及对返回结果的处理逻辑。关于更多开发指引，请参考[快速开始： Agent 策略插件](quick-start/develop-plugins/agent-strategy-plugin.md)。
*   **Extensions（扩展）**

    仅提供 Endpoint 能力，为简单场景设计的轻量级方案。仅通过调用 HTTP 服务即可调用扩展功能，适用于只需要基础 API 调用的简单集成场景。关于扩展插件的开发详情，请参考[快速开始：Extension 插件](quick-start/develop-plugins/extension-plugin.md)。
*   **Bundle（插件包）**

    插件包是一系列插件的组合。通过安装插件集可以批量安装预选插件，告别手动逐个安装插件的繁琐过程。关于插件包的开发详情，请参考[插件开发：Bundle 插件](quick-start/develop-plugins/bundle.md)。

### 插件有哪些新特性？

*   **增强 LLM 的多模态能力**

    插件系统可以增强 LLM 处理多媒体内容的能力。开发者可以根据场景，通过插件辅助 LLM 完成图片处理、视频处理等任务，包括但不限于图片裁切、背景处理、人物图像处理等。
*   **开发者友好的调试能力**

    插件系统提供了完善的开发和调试支持：

    * 支持主流 IDE 和调试工具，仅需配置一些简单的环境变量，即可远程连接一个 Dify 实例。甚至支持连接 Dify 的 SaaS 服务，此时你在 Dify 中对该插件的任何操作都会被转发至你的本地运行
*   **持久化存储数据**

    为支持复杂应用场景，插件系统全新引入了数据持久化存储能力：

    * 插件级别的数据存储
      * Workspace 级别的数据共享，你可以向插件传递当前工作空间的信息，帮助插件提供更多自定义功能。
      * 内置的数据管理机制，这使得插件能够可靠地保存和管理应用数据，支持更复杂的业务场景。
*   **便捷地反向调用**

    插件能够与 Dify 平台内的功能组件进行双向互动，它能够按照指令主动调用 Dify 的核心功能，包括：

    * AI 模型调用
    * 工具使用
    * 应用访问
    * 知识库交互
    * 功能节点调用（如问题分类、参数提取等）

    双向调用机制让插件具备了更强大的功能整合能力，这意味着不仅可以使用已有的 Dify 应用能力全面增强插件能力，你还可以将插件作为一个独立的 Dify 应用请求网关，扩充更多的应用使用场景。
*   **更自由的 API 接口自定义能力**

    除了 Dify 应用内原有的 API（例如 Chatbot 应用 API，Workflow 应用 API 等），插件系统新增了自定义 API 的能力。开发者可以根据业务需求，将业务代码封装为插件并托管至 [Dify Marketplace](https://marketplace.dify.ai/)，并自动提供请求端点，实现数据处理、请求响应等自定义逻辑。

### 阅读更多

**快速开始**

如果你想要快速安装与使用插件，请参考以下内容：

{% content-ref url="quick-start/install-plugins.md" %}
[install-plugins.md](quick-start/install-plugins.md)
{% endcontent-ref %}

如果你想要上手插件开发，请参考以下内容：

{% content-ref url="quick-start/develop-plugins/" %}
[develop-plugins](quick-start/develop-plugins/)
{% endcontent-ref %}

**发布插件**

如果想要将插件发布至 [Dify Marketplace](https://marketplace.dify.ai/)，请根据指引填写完整插件信息和相关使用文档。将插件代码投稿至 [GitHub 仓库](https://github.com/langgenius/dify-plugins)，审核通过后将在插件市场中上线。

{% content-ref url="publish-plugins/publish-to-dify-marketplace/" %}
[publish-to-dify-marketplace](publish-plugins/publish-to-dify-marketplace/)
{% endcontent-ref %}

除了将插件发布至 Dify 官方插件市场以外，你也可以发布至个人 GitHub 项目内或打包为文件包，以文件的形式分享。

{% content-ref url="publish-plugins/publish-plugin-on-personal-github-repo.md" %}
[publish-plugin-on-personal-github-repo.md](publish-plugins/publish-plugin-on-personal-github-repo.md)
{% endcontent-ref %}

{% content-ref url="publish-plugins/package-plugin-file-and-publish.md" %}
[package-plugin-file-and-publish.md](publish-plugins/package-plugin-file-and-publish.md)
{% endcontent-ref %}
