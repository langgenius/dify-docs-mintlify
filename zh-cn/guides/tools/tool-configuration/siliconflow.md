# SiliconFlow (支持 Flux 绘图)

> 工具作者 @hjlarry

{% hint style="warning" %}
“工具”已全面升级为“插件”生态，详细的使用说明请参考[插件开发](https://docs.dify.ai/zh-hans/plugins/quick-start/install-plugins)。以下内容已归档。
{% endhint %}

SiliconCloud 基于优秀的开源基础模型，提供高性价比的 GenAI 服务。你可以通过 **SiliconFlow** 在 Dify 内调用 Flux 、Stable Diffusion 绘图模型，搭建你的专属 AI 绘图应用。以下是在 Dify 中配置 SiliconFlow 工具的步骤。

### 1. 申请 SiliconCloud API Key

请在 [SiliconCloud API 管理页面](https://cloud.siliconflow.cn/account/ak) 新建 API Key 并保证有足够余额。

### 2. 在 Dify 内填写配置

在 Dify 的工具页中点击 `SiliconCloud > 去授权` 填写 API Key。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/0304594b8cdee83931102b39fd014a75.png)

### 3. 使用工具

* **Chatflow / Workflow 应用**

Chatflow 和 Workflow 应用均支持添加 `SiliconFlow` 工具节点。

将用户输入的内容通过[变量](../../workflow/variables.md)传递至 Siliconflow 工具的 Flux 或 Stable Diffusion 节点内的“提示词”“负面提示词”框中，按照需求调整内置参数，最后在“结束”节点的回复框中选中 Siliconflow 工具节点的输出内容（文本、图片等）。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/81d0ed042a4a7226aa22dcff0dca2ed3.png)

* **Agent 应用**

在 Agent 应用内添加 `Stable Diffusion` 或 `Flux` 工具，然后在对话框内发送图片描述，调用工具生成 AI 图像。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/b2d005656378c8e7c29f9686c603c7ed.png)

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/17b184d96920fd8c6b891e903166be38.png)
