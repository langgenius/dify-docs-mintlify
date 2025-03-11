# Bing 搜索

> 工具作者 @Dify。

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

Bing 搜索工具能够帮助你在使用 LLM 应用的时候，获取联网搜索结果。以下是在 Dify 中配置和使用 Bing 搜索工具的步骤。

## 1. 申请 Bing API Key

请在 [Azure 平台](https://platform.openai.com/)申请 API Key。

## 2. 在 Dify 内填写配置

在 Dify 导航页内轻点 `工具 > Azure > 去授权` 填写 API Key。

![](../../../../img/zh-tools-bing.png)

## 3. 使用工具

你可以在以下应用类型中使用 Bing 工具。

- **Chatflow / Workflow 应用**

Chatflow 和 Workflow 应用均支持添加 `Bing` 工具节点。

- **Agent 应用**

在 Agent 应用内添加 `Bing` 工具，然后输入在线搜索指令，调用此工具。
