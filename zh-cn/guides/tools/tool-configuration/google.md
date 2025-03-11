# Google

> 工具作者 @Dify。

{% hint style="warning" %}
“工具”已全面升级为“插件”生态，详细的使用说明请参考[插件开发](https://docs.dify.ai/zh-hans/plugins/quick-start/install-plugins)。以下内容已归档。
{% endhint %}

Google 搜索工具能够帮助你在使用 LLM 应用的时候，获取联网搜索结果。以下是在 Dify 中配置和使用 Google 搜索工具的步骤。

## 1. 申请 Serp API Key

请在 [Serp 平台](https://serpapi.com/dashboard)申请 API Key。

## 2. 在 Dify 内填写配置

在 Dify 导航页内轻点 `工具 > Google > 去授权` 填写 API Key。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/b702fecd142ed154c50645922a24b82a.png)

## 3. 使用工具

你可以在以下应用类型中使用 Google 工具。

* **Chatflow / Workflow 应用**

Chatflow 和 Workflow 应用均支持添加 `Google` 工具节点。

* **Agent 应用**

在 Agent 应用内添加 `Google` 工具，然后输入在线搜索指令，调用此工具。
