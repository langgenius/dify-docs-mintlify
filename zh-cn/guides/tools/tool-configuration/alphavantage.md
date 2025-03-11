# AlphaVantage 股票分析

> 工具作者 [@zhuhao](https://github.com/hwzhuhao)。

{% hint style="warning" %}
“工具”已全面升级为“插件”生态，详细的使用说明请参考[插件开发](https://docs.dify.ai/zh-hans/plugins/quick-start/install-plugins)。以下内容已归档。
{% endhint %}

AlphaVantage 一个在线平台，它提供金融市场数据和API，便于个人投资者和开发者获取股票报价、技术指标和股票分析。本

## 1. 申请 AlphaVantage API Key

请在 [AlphaVantage](https://www.alphavantage.co/support/#api-key)申请 API Key。

## 2. 在 Dify 内填写配置

在 Dify 导航页内轻点 `工具 > AlphaVantage > 去授权` 填写 API Key。

## 3. 使用工具

- **Chatflow / Workflow 应用**

Chatflow 和 Workflow 应用均支持添加 `AlphaVantage` 工具节点。添加后，需要在节点内的 “输入变量 → 股票代码” 通过[变量](https://docs.dify.ai/v/zh-hans/guides/workflow/variables)引用用户输入的查询内容。最后在 “结束” 节点内使用变量引用 `AlphaVantage` 节点输出的内容。

- **Agent 应用**

在 Agent 应用内添加 `AlphaVantage` 工具，然后在对话框内发送股票代码或大致描述，调用工具得到准确的金融数据。
