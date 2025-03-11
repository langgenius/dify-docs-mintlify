# Perplexity Search

> 工具作者 @Dify。

{% hint style="warning" %}
“工具”已全面升级为“插件”生态，详细的使用说明请参考[插件开发](https://docs.dify.ai/zh-hans/plugins/quick-start/install-plugins)。以下内容已归档。
{% endhint %}


Perplexity 是一个基于 AI 的搜索引擎，能够理解复杂的查询并提供准确、相关的实时答案。以下是在 Dify 中配置和使用 Perplexity Search 工具的步骤。

## 1. 申请 Perplexity API Key

请在 [Perplexity](https://www.perplexity.ai/settings/api)申请 API Key，并确保账户内有足够的 Credits。

## 2. 在 Dify 内填写配置

在 Dify 导航页内轻点 `工具 > Perplexity > 去授权` 填写 API Key。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/310e39c00848e882c4c90d0c43ae972f.png)

## 3. 使用工具

你可以在以下应用类型中使用 Perplexity Search 工具。

* **Chatflow / Workflow 应用**

Chatflow 和 Workflow 应用均支持添加 Perplexity 工具节点。将用户输入的内容通过变量传递至 Perplexity 工具节点内的“查询”框中，按照需求调整 Perplexity 工具的内置参数，最后在“结束”节点的回复框中选中 Perplexity 工具节点的输出内容。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/fdf3f7b69c2117e09631f66fc56e250d.png)

* **Agent 应用**

在 Agent 应用内添加 `Perplexity Search` 工具，然后输入相关指令即可调用此工具。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/d505c0109581c07375e9563def4309a6.png)
