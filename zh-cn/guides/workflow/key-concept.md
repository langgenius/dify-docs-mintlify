# 关键概念

### 节点

**节点是工作流的关键构成**，通过连接不同功能的节点，执行工作流的一系列操作。

工作流的核心节点请查看[节点说明](node/)。

***

### 变量

**变量用于串联工作流内前后节点的输入与输出**，实现流程中的复杂处理逻辑，包含系统变量、环境变量和会话变量。详细说明请参考 [《变量》](variables.md)。

***

### Chatflow

**适用场景：**

面向对话类情景，包括客户服务、语义搜索、以及其他需要在构建响应时进行多步逻辑的对话式应用程序。该类型应用的特点在于支持对生成的结果进行多轮对话交互，调整生成的结果。

常见的交互路径：给出指令 → 生成内容 → 就内容进行多次讨论 → 重新生成结果 → 结束

![Chatflow 入口](https://assets-docs.dify.ai/2024/12/224b6bcd750ff0b83e3a5dac5cf24d7d.png)

### 工作流（Workflow）

**适用场景：**

面向自动化和批处理情景，适合高质量翻译、数据分析、内容生成、电子邮件自动化等应用程序。该类型应用无法对生成的结果进行多轮对话交互。

常见的交互路径：给出指令 → 生成内容 → 结束

![](https://assets-docs.dify.ai/2024/12/26a9fc809854fe51d946c148587fc1cf.png)

**应用类型差异**

1. [End 节点](node/end.md)属于 Workflow 的结束节点，仅可在流程结束时选择。
2. [Answer 节点](node/answer.md)属于 Chatflow ，用于流式输出文本内容，并支持在流程中间步骤输出。
3. Chatflow 内置聊天记忆（Memory），用于存储和传递多轮对话的历史消息，可在 [LLM](node/llm.md) 、[问题分类](node/question-classifier.md)等节点内开启，Workflow 无 Memory 相关配置，无法开启。
4. Chatflow 的开始节点内置变量包括：`sys.query`，`sys.files`，`sys.conversation_id`，`sys.user_id`。Workflow 的开始节点内置变量包括：`sys.files`，`sys.user_id` ，详见[变量](key-concept.md#bian-liang)。
