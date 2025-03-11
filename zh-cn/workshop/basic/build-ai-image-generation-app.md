# 如何搭建 AI 图片生成应用

> 作者：Steven Lynn。Dify Technical Writer。

随着图像生成技术的兴起，涌现了许多优秀的图像生成产品，比如 Dall-e、Flux、Stable Diffusion 等。

本文将使用图像生成模型，指导你使用 Dify 快速开发一个 AI 图片生成应用。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/05ff829cf382e82c9ece2676032d2383.png)

### 本实验中你将掌握的知识点

* 使用 Dify 构建 Agent 的方法
* Agent 的基本概念
* 提示词工程的基础知识
* 工具的使用
* 大模型的幻觉的概念

### 1. 获取和填入 Stablility API 密钥

[点击这里](https://platform.stability.ai/account/keys) 即可跳转至 Stability 的 API 密钥管理页。

如果你尚未注册，会被要求先注册再进入管理页。

进入管理页后，点击复制密钥即可。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/f73d82756bdf93c8863ac0b1f55fa5af.png)

接下来，你需要通过以下步骤把密钥填入 [Dify - 工具 - Stability](https://cloud.dify.ai/tools) 中：

* 登录 Dify
* 进入工具
* 选择 Stability
* 点击授权

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/c943c374a89b5ba08683f0eb6c501664.png)

* 填入密钥并保存

### 2. 配置模型供应商

为了优化交互，我们需要LLM来将用户的指令具体化，也就是让LLM来撰写生成图片的提示词（Prompt）。接下来，我们按照如下的步骤在 Dify 配置模型供应商。

Free 版本的 Dify 提供了免费 200 条 OpenAI 的消息额度

如果消息额度不够用，你可以参考下图步骤, 自定义其它模型供应商:

点击**右上角头像 - 设置 - 模型供应商**

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/52f3f299b05ff94ee0421604dd810e35.png)

如果尚未找到合适的模型供应商，groq 平台提供了 Llama 等 LLM 的免费调用额度。

登录 [groq API 管理页](https://console.groq.com/keys)

点击 **Create API Key**，设置一个想要的名称并且复制 API Key。

回到**Dify - 模型供应商**，选择**groqcloud**，点击 **设置**。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/1c4f0a7081fc6f5644203baf2f703b49.png)

粘贴 API Key 并保存。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/0a0593676651be79b9b322c48938f042.png)

### 3. 构建 Agent

回到**Dify - 工作室**，选择**创建空白应用**。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/494bd8427dce548ce56b5b1cd52bffbd.png)

在本实验中，我们只需要了解 Agent 的基础用法即可。

{% hint style="info" %}
**什么是 Agent**

Agent 是一种模拟人类行为和能力的 AI 系统，它通过自然语言处理与环境交互，能够理解输入信息并生成相应的输出。Agent 还具有 "感知" 能力，可以处理和分析各种形式的数据。此外，Agent 能够调用和使用各种外部工具和 API 来完成任务，扩展其功能范围。这种设计使 Agent 能够更灵活地应对复杂情况，在一定程度上模拟人类的思考和行为模式。

因此，很多人都会将 Agent 称为“智能体”。
{% endhint %}

选择 **Agent**，填写名称即可。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/c428f040fe117670abbc0e268227fcc9.png)

接下来你会进入到如下图的 Agent 编排界面

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/c24024b10f76b5a2bf416c9411f3cc55.png)

我们选择 LLM，本篇教程中我们使用 groq 提供的 Llama-3.1-70B 为例：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/5f6c6837cbee213d8adbc71ce41467c2.png)

在**工具**中添加 AI 绘图工具 Stability：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/c963eb9ae55b035631f32ebd6ad23f4b.png)

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/20f37184597aac61463297cae9485055.png)

#### 撰写提示词

提示词（Prompt）是 Agent 的灵魂，直接影响到输出的效果。通常来说越具体的提示词输出的效果越好，但是过冗长的提示词也会导致一些负面效果。

调整提示词的工程，我们称之为提示词工程（Prompt Engineering）

在本次实验中，你不必担心没有掌握提示词工程，我们会在后面循序渐进地学习它。

让我们从最简单的提示词开始：

```
根据用户的提示，使用工具 stability_text2image 绘画指定内容
```

用户每次输入命令的时候，Agent 都会知晓这样的系统级的指令，从而了解要执行用户绘画的任务的时候需要调用一个叫 stability 的工具。

例如：画一个女孩，手中拿着一本打开的书

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/5a1742b0580a960bfc476651720662c4.png)

#### 不想撰写提示词？当然可以！

点击提示词的右上角**生成**。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/145ce8b15faff3b116ecc48086a12dcb.png)

在**指令**中输入你的需求，点击**生成**，右侧生成的提示词中会出现由AI生成的提示词。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/efcb66dc935f5d5d954c936847af2496.png)

不过，为了养成对提示词良好的理解，我们在初期最好不要依赖这一项功能。

### 发布

点击右上角的发布按钮，发布后选择**运行**就可以获得一个在线运行的 Agent 的网页。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/bd178b3530f90400a1eeb0ca824ccbd2.png)

复制这个网页的 URL，可以分享给其他好友使用。

### 思考题 1：如何指定生成图片的画风？

我们可以在用户输入的命令中加上画风的指令，例如：二次元风格，画一个女孩，手中拿着一本打开的书

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/ebed02c8f6643427f0ba83e63c9fcaa8.png)

但是如果我们希望风格默认都是二次元风格呢，那么我们加在系统提示词里就行了，因为我们之前了解到系统提示词是每次执行用户命令都会知晓的，优先级更高。

```
根据用户的提示，使用工具 stability_text2image 绘画指定内容，画面是二次元风格
```

### 思考题 2: 如何拒绝部分用户的某些请求？

在许多业务场景中，我们需要避免输出一些不合理的内容，但是 LLM 很多时候比较 “傻”，用户下指令时会照做不误，即使输出的内容是错的，这种模型为了努力回答用户而编造虚假内容的现象称为模型幻觉（Hallucinations），那么我们需要让模型必要的时候拒绝用户的请求。

此外，用户也可能提一些和业务无关的内容，我们也需要让 Agent 这个时候拒绝请求。

我们可以使用 markdown 格式给不同的提示词进行划分，将上述教 Agent 拒绝不合理内容的提示词写到 “约束” 标题下。当然，这样的格式仅仅是为了规范化，你可以有自己的格式。

```
## 任务
根据用户的提示，使用工具 stability_text2image 绘画指定内容，画面是二次元风格。

## 约束
如果用户在请求和绘画无关的内容，回复：“对不起，我不明白你在说什么”
```

例如，我们尝试提问：今晚吃什么

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/ad342ddc00acc1aa0ad81f335e32a625.png)

在一些更正式的业务场景中，我们可以调用敏感词库来拒绝用户的请求。

在**添加功能 - 内容审查**中添加关键词 “晚饭”，当用户输入关键词时，则 Agent 应用输出 “对不起，我不明白你在说什么”。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/workshop/basic/e9d6e1a7f3a13c88dc98eef89f221949.png)
