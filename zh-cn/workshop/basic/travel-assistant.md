# AI Agent 实战：搭建个人在线旅游助手

> 作者: Steven Lynn。 Dify Technical Writer。

在上一个实验 [如何搭建 AI 图片生成应用](build-ai-image-generation-app.md) 中，我们已初步了解了 Agent 的概念，并且尝试动手写了系统提示词。

本次实验中，我们将继续探索 Agent 的提示词，学习更加规范的提示词撰写方法。

### 本实验中你将掌握的知识点

* 使用 Dify 构建 Agent 的方法
* 结构化的提示词撰写技巧
* 变量的使用方法

### 1. 准备

在新建 Agent 之前，请先确保以下步骤已经完成：

* 注册和登录 [Dify](https://dify.ai)，如果你想要进行本地部署，可以参考 [社区版 - Docker Compose 部署](../../getting-started/install-self-hosted/docker-compose.md)
* 至少配置一个模型供应商（Dify 赠送 200 条 OpenAI 消息额度，但为了确保实验顺利建议自行配置 LLM 的 API Key）

### 2. 配置工具

#### Google

搭建在线旅游助手需要使用联网的搜索引擎作为参考资料来源，本文中将以 Google 作为示例。

当然，你也可以使用其他的搜索引擎，例如[必应](https://docs.dify.ai/zh-hans/guides/tools/tool-configuration/bing)，甚至是由 AI 驱动的 [Perplexity](https://docs.dify.ai/zh-hans/guides/tools/tool-configuration/perplexity)。

Dify 提供的 Google 工具基于 SerpAPI，因此需要提前进入 SerpAPI 的 API Key 管理页申请 API Key 并粘贴到 `Dify - 工具` 的对应位置。

具体操作步骤如下：

1. 新增 SerpAPI 的 API Key：

进入[SerpAPI - API Key](https://serpapi.com/manage-api-key)，如果你尚未注册，会被跳转至进入注册页。

SerpAPI提供一个月100次的免费调用次数，这足够我们完成本次实验了。如果你需要更多的额度，可以增加余额，或者使用其他的开源方案。

点击复制

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/cf8870ff01bfb944da7ddbd073e9cc41.png)

2. 前往 **Dify - 工具 - Google**：

点击 `去授权` ，填入API Key并保存。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/e9726a2e68cbe8f957f8394b5ca47049.png)

#### webscraper

本次实验中，我们需要一个爬虫工具从指定的网页中抓取内容，Dify 已提供内置工具，无需额外配置。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/516c649bc0d8f2d1c81ba8b5bb28638c.png)

#### Wikipedia

我们还希望 Agent 能够准确介绍目的地知识，Wikipedia 是一个比较好知识来源，Dify 也内置了该工具，无需额外配置。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/53ebce24e49543b83d6c5581525d4e30.png)

### 3. 构建 Agent

首先我们选择 `创建空白应用 - Agent`：

添加工具：`Google`、`webscraper`和`wikipedia`并启用。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/6799204e6259ab41f22f85e285466c22.png)

4. **示例输出**

示例输出不是必要的部分。示例输出的目的是为了给 Agent 一个书写格式的参考，以确保 Agent 的输出更接近我们的期望。

以下是旅游助手的示例输出：

```
## 示例

### 详细旅行计划

**酒店推荐**
1. 肯辛顿酒店 (了解更多：www.doylecollection.com/hotels/the-kensington-hotel)
- 评分：4.6⭐
- 价格：每晚约350美元
- 简介：坐落在一座摄政时期的联排别墅中，这家优雅的酒店距离南肯辛顿地铁站5分钟步行路程，距离维多利亚和阿尔伯特博物馆10分钟步行路程。

2. 伦勃朗酒店 (了解更多：www.sarova-rembrandthotel.com)
- 评分：4.3⭐
- 价格：每晚约130美元
- 简介：建于1911年，最初是哈罗德百货公司（距离0.4英里）的公寓，这家现代化酒店坐落在维多利亚和阿尔伯特博物馆对面，距离南肯辛顿地铁站（直达希思罗机场）5分钟步行路程。

**第1天 - 抵达和安顿**
- **上午**：抵达机场。欢迎来到你的冒险之旅！我们的代表将在机场迎接你，确保你顺利入住。
- **下午**：入住酒店，稍作休息，恢复精力。
- **晚上**：在住宿周边进行轻松的步行游览，熟悉当地环境。发现附近的用餐选择，享受愉快的第一顿晚餐。

**第2天 - 文化与自然之旅**
- **上午**：从帝国理工学院开始你的一天，这是世界顶尖的学府之一。享受一次校园导览。
- **下午**：选择参观自然历史博物馆（以其引人入胜的展览而闻名）或维多利亚和阿尔伯特博物馆（庆祝艺术和设计）。之后，在宁静的海德公园放松，也许还可以在蛇形湖上乘船游览。
- **晚上**：探索当地美食。我们推荐你在传统的英国酒吧享用晚餐。

**附加服务：**
- **礼宾服务**：在你停留期间，我们的礼宾服务随时可以协助预订餐厅、购买门票、安排交通，以及满足任何特殊要求，以提升你的体验。
- **24/7支持**：我们提供全天候支持，以解决你在旅行中可能遇到的任何问题或需求。

祝你旅途愉快，满载丰富经历和美好回忆！
```

### 思考题 1: 如何规范化用户输入？

通常我们输入 Agent 内容都是自然语言，而自然语言的一个缺点是很难规范化，有可能包含了一些 Agent不需要的信息或者没有价值的信息，这个时候我们可以引入变量来规范化输入。

Dify 目前支持`文本`、`段落`、`下拉选项`、`数字`、`基于 API 的变量`这几种类型的变量。

在本实验中，我们只需要选用`文本`类型的变量即可。

在**变量**中，选择合适的变量类型，我们可以询问用户目的地、旅行天数、预算。

| 变量Key       | 变量类型 | 字段名称 | 可选 |
| ----------- | ---- | ---- | -- |
| destination | 文本   | 目的地  | 是  |
| day         | 文本   | 旅行天数 | 是  |
| budget      | 文本   | 旅行预算 | 是  |

需要注意的是，`变量 Key`，也就是变量的名称，仅支持大小写英文、数字、下划线。`字段名称`是用户可以看到的提示内容。

添加变量后，用户可以按照应用开发者的意图向应用提供必要的背景信息，实现的效果如下：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/927260e8e6198b98f3b9406f856c0240.png)
