---
description: 'Author: Yeuoly, Allen'
---

# 插件开发

### 快速开始

你可以通过以下**插件开发示例**，了解如何开发不同类型的插件，快速上手并掌握插件开发过程中可能涉及的功能组件。正式开始插件开发前，需要在本地环境中安装并初始化开发脚手架。请参考以下内容：

{% content-ref url="initialize-development-tools.md" %}
[initialize-development-tools.md](initialize-development-tools.md)
{% endcontent-ref %}

以 **GoogleSearch** 工具为例，介绍如何开发工具类插件。开发示例请参考以下内容：

{% content-ref url="tool-plugin.md" %}
[tool-plugin.md](tool-plugin.md)
{% endcontent-ref %}

以 **Anthropic** 和 **Xinference** 模型为例，分别介绍如何开发**模型插件**（又称为**模型供应商**），其中包含预定义模型和自定义模型插件两种类型。

* 预定义模型是指已经由 AI 厂商训练好并面向市场的模型，通常是闭源模型（例如 GPT 系列模型和 Claude 系列模型），你可以直接调用这些模型能力完成特定任务，无需进行额外的训练或配置。
* 自定义模型插件允许开发者集成私有训练或已进行特定配置的私有模型，以满足本地场景要求。

开发示例请参考以下内容：

{% content-ref url="model-plugin/" %}
[model-plugin](model-plugin/)
{% endcontent-ref %}

Extension 插件允许开发者将业务代码封装为插件，并自动提供 Endpoint 请求入口，可以被理解为托管在 Dify 平台内的 API 服务。开发示例请参考以下内容：

{% content-ref url="extension-plugin.md" %}
[extension-plugin.md](extension-plugin.md)
{% endcontent-ref %}

### 接口文档

如果你想阅读插件项目的详细接口文档，请阅读以下标准规范文档：

1. [通用结构标准定义](../../schema-definition/general-specifications.md)
2. [Manifest 标准定义](../../schema-definition/manifest.md)
3. [工具接入标准定义](../../schema-definition/tool.md)
4. [模型接入简介](../../schema-definition/model/)
5. [Endpoint 标准定义](../../schema-definition/endpoint.md)
6. [扩展 Agent 策略](../../schema-definition/agent.md)
7. 反向调用 Dify 平台能力
   1. 反向调用 [app.md](../../schema-definition/reverse-invocation-of-the-dify-service/app.md "mention")
   2. 反向调用 [model.md](../../schema-definition/reverse-invocation-of-the-dify-service/model.md "mention")
   3. 反向调用节点 [node.md](../../schema-definition/reverse-invocation-of-the-dify-service/node.md "mention")
   4. 反向调用工具 [tool.md](../../schema-definition/reverse-invocation-of-the-dify-service/tool.md "mention")
8. [插件持久化存储能力](../../schema-definition/persistent-storage.md)

### 贡献指南

想为官方插件市场贡献更多插件，或面向社区开源插件？请参考以下详细的插件贡献指南：

*   [Marketplace 发布指南](../../publish-plugins/publish-to-dify-marketplace/)

    了解如何将你的插件发布至 Dify Marketplace，向更多 Dify 用户分享你的成果。
*   [GitHub 发布指南](../../publish-plugins/publish-plugin-on-personal-github-repo.md)

    学习如何在 GitHub 上发布和管理插件，确保插件的持续优化和社区协作。

欢迎加入贡献者行列，与全球开发者共同完善 Dify 生态系统！
