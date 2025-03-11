# 直接回复

### 定义

定义一个 Chatflow 流程中的回复内容。

你可以在文本编辑器中自由定义回复格式，包括自定义一段固定的文本内容、使用前置步骤中的输出变量作为回复内容、或者将自定义文本与变量组合后回复。

可随时加入节点将内容流式输出至对话回复，支持所见即所得配置模式并支持图文混排，如：

1. 输出 LLM 节点回复内容
2. 输出生成图片
3. 输出纯文本

**示例1：** 输出纯文本

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/workflow/node/1b1fadb8f838963134fc5c9eb14b5632.png)

**示例2：** 输出图片+LLM回复

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/workflow/node/16279b70829e308bcc0c1e73aa1c870f.png)

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/workflow/node/19b19eddfb50fdbe880da598e43c24c9.png)

{% hint style="info" %}
直接回复节点可以不作为最终的输出节点，作为流程过程节点时，可以在中间步骤流式输出结果。
{% endhint %}
