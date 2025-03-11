# Youtube

> 工具作者 @Dify。

{% hint style="warning" %}
“工具”已全面升级为“插件”生态，详细的使用说明请参考[插件开发](https://docs.dify.ai/zh-hans/plugins/quick-start/install-plugins)。以下内容已归档。
{% endhint %}

[Youtube](https://www.youtube.com/) 是最大的在线视频分享平台。目前 Dify.ai 有两个相关工具 `Video Statisctics` 和 `Free YouTube Transcript API`，可通过输入网址或关键字来分析视频信息。

## 1. 确保你允许使用 Google Cloud Service

> 如果你没有帐户，请转到 [Google 凭据网站](https://console.cloud.google.com/apis/credentials) 并按照其说明创建帐户。

如果你有帐户，请转到 API 和服务页面并单击“创建凭据 -> API 密钥”以创建 API 密钥。

![](/img/en-google-api.jpg)

按照步骤操作并单击“启用 API 和服务 -> YouTube 数据 API v3”以启用 Youtube 数据 API。

## 2. 在 Dify 内填写配置

在 [Dify 工具页](https://cloud.dify.ai/tools) 内轻点 ` Youtube > 去授权` 填写从第一阶段获取到的 API Key。

![](/img/en-set-youtube-api.jpeg)

## 3. 使用工具

你可以在以下应用类型中使用 Youtube 工具。

- **Chatflow / Workflow 应用**

Chatflow 和 Workflow 应用均支持添加 `视频统计` 工具节点。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/abaa685d6ffa5fbb8c295869eecfd721.jpeg)

- **Agent 应用**

在 Agent 应用内添加 `免费获取 YouTube 转录` 工具，然后输入在线搜索指令，调用此工具。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/a5dc28b46d00cb523268bf51399476b6.png)
