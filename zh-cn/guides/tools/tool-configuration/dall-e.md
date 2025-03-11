# Dall-e

> 工具作者 @Dify。

{% hint style="warning" %}
“工具”已全面升级为“插件”生态，详细的使用说明请参考[插件开发](https://docs.dify.ai/zh-hans/plugins/quick-start/install-plugins)。以下内容已归档。
{% endhint %}

DALL-E 是由 OpenAI 开发的一种基于文本提示生成图像的工具。Dify 已接入 DALL-E 工具，以下是在 Dify 中配置和使用 DALL-E 绘图工具的步骤。

## 1. 申请 OpenAI 的 API Key

请在 [OpenAI Platform](https://platform.openai.com/)申请 API Key，并确保账户内有足够的 Credits。

## 2. 在 Dify 内填写配置

在 Dify 导航页内轻点 `工具 > DALL-E > 去授权` 填写 API Key。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/e14d1190c5b8dc6c7e6b9c8d3e9d4eca.png)

## 3. 使用工具

* **Chatflow / Workflow 应用**

Chatflow 和 Workflow 应用均支持添加 `DALL-E 绘图` 工具节点。添加后，需要在节点内的 “输入变量 → 提示词” 内填写[变量](https://docs.dify.ai/v/zh-hans/guides/workflow/variables)引用用户输入的提示词，或者是上一节点生成的内容。最后在 “结束” 节点内使用变量引用 `DALL-E 绘图` 输出的图像。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/742014125d01f001a3f8e542b53130ce.png)

* **Agent 应用**

在 Agent 应用内添加 `DALL-E` 工具，然后在对话框内发送图片描述，调用工具生成 AI 图像。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/7adb47ad645fb7f1bd95848e78cb6a0f.png)
