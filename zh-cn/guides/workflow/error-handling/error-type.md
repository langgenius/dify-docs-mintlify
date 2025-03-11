# 错误类型

本文总结了不同类型节点可能发生的异常和对应的错误类型。

### 通用错误

*   系统错误（System Error）

    通常由系统问题引起，例如沙盒服务未开启、网络连接异常等。
*   操作错误（Operational Error）

    应用开发者无法正常配置或运行节点时发生的错误。

### 代码节点

[代码节点](https://docs.dify.ai/guides/workflow/node/code) 支持运行 Python 和 JavaScript 代码，用于在工作流或聊天流中对数据进行改造。以下是常见的 4 种运行错误：

1.  **代码节点错误（CodeNodeError）**

    此错误是由于开发者编写代码中的异常引起的，例如：缺少变量、计算逻辑错误、将字符串数组输入作为字符串变量处理等。你可以通过错误信息和精确的行号定位问题。



    ![代码错误](https://assets-docs.dify.ai/2024/12/c86b11af7f92368180ea1bac38d77083.png)
2.  **沙盒网络问题（System Error）**\
    此错误常见于网络流量或连接异常时，例如沙盒服务未开启，代理服务中断了网络。你可以通过以下方式解决：

    1. 检查网络服务质量
    2. 开启沙盒服务
    3. 验证代理设置



    ![沙盒网络问题](https://assets-docs.dify.ai/2024/12/d95007adf67c4f232e46ec455c348e2c.PNG)
3.  **深度限制错误（DepthLimitError）**

    当前节点的默认配置最多仅支持 5 层嵌套结构。如果超过 5 层，则会报错。



    ![OutputValidationError](https://assets-docs.dify.ai/2024/12/5649d52a6e80ddd4180b336266701f7b.png)


4.  **输出验证错误（OutputValidationError）**

    如果实际输出变量类型与所选输出变量类型不一致将报错。开发者需要更改所选的输出变量类型规避此问题。



    ![](https://assets-docs.dify.ai/2024/12/ab8cae01a590b037017dfe9ea4dbbb8b.png)

### LLM 节点

[LLM 节点](https://docs.dify.ai/guides/workflow/node/llm)是 Chatflow 和 Workflow 的核心组件，利用大语言模型的对话、生成、分类和处理能力，基于使用者输入的指令完成各种任务。

以下是运行时常见的 6 种错误：

1.  **未找到对应变量（VariableNotFoundError）**

    如果 LLM 找不到系统提示词或在上下文中设置的变量，则会出现此错误。应用开发者可以通过替换异常变量来解决此问题。



    ![VariableNotFoundError](https://assets-docs.dify.ai/2024/12/f20c5fbde345144de6183374ab277662.png)
2.  **上下文结构无效（InvalidContextStructureError）**

    LLM 节点内的 [上下文](https://docs.dify.ai/guides/workflow/node/llm#explanation-of-special-variables) 接收到非法数据结构（如 `array[object]`）时会报错。

    > 上下文仅支持字符串（String）数据结构。



    ![InvalidContextStructureError](https://assets-docs.dify.ai/2024/12/f20c5fbde345144de6183374ab277662.png)
3.  **错误的参数类型（InvalidVariableTypeError）**

    系统提示词的类型不为常规的 Prompt 文本或 Jinja 语法格式，则出现此错误。
4.  **模型不存在（ModelNotExistError）**

    每个 LLM 节点都需要配置一个模型，如果未选中模型将出现此错误。
5.  **LLM 需授权（LLMModeRequiredError）**

    LLM 节点所选中的模型未配置 API Key，你可以阅读 [此文档](https://docs.dify.ai/guides/tools/tool-configuration) 授权模型。
6.  **未找到提示词（NoPromptFoundError）**

    LLM 节点的提示词不能为空，否则异常。



    ![NoPromptFoundError](https://assets-docs.dify.ai/2024/12/9882f7a5ee544508ba11b51fb469a911.png)

### HTTP

[HTTP 节点](https://docs.dify.ai/guides/workflow/node/http-request)允许通过发送 HTTP 请求获取数据、触发Webhook、生成图像或下载文件，从而通过可定制的请求与外部服务无缝集成。以下是该节点常见的 5 种错误：

1.  **授权配置错误（AuthorizationConfigError）**

    未配置认证信息（Auth）时出现此报错。
2.  **文件获取错误（FileFetchError）**

    无法获取文件变量时出现此报错。
3.  **无效的 HTTP 请求方法（InvalidHttpMethodError）**

    请求头非以下方法：GET、HEAD、POST、PUT、PATCH 或 DELETE，出现报错。
4.  **响应大小超限（ResponseSizeError）**

    HTTP 返回的响应大小限制为 10MB，如果响应超出限制，出现报错。
5.  **HTTP 响应代码错误（HTTPResponseCodeError）**

    当请求响应返回非 2 开头的代码时（例如 200, 201）将报错。如果开启了异常处理，当返回的状态码为 400、404、500 时将报错，否则不会报错。

### 工具

运行时常见以下 3 种错误：

1.  **工具执行异常（ToolNodeError）**

    工具本身执行的异常报错，例如达到了目标 API 的请求限制。

![](https://assets-docs.dify.ai/2024/12/84af0831b7cb23e64159dfbba80e9b28.jpg)

2.  **工具参数异常（ToolParameterError）**

    所配置的工具节点参数存在异常，传入了不符合工具节点所定义的参数。
3.  **工具文件处理异常（ToolFileError）**

    工具节点未找到所需的文件，出现报错。





