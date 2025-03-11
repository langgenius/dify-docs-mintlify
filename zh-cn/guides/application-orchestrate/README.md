# 构建应用

在 Dify 中，一个“应用”是指基于 GPT 等大语言模型构建的实际场景应用。通过创建应用，你可以将智能 AI 技术应用于特定的需求。它既包含了开发 AI 应用的工程范式，也包含了具体的交付物。

简而言之，一个应用为开发者交付了：

* 封装友好的 API，可由后端或前端应用直接调用，通过 Token 鉴权
* 开箱即用、美观且托管的 WebApp，你可以 WebApp 的模版进行二次开发
* 一套包含提示词工程、上下文管理、日志分析和标注的易用界面

你可以任选**其中之一**或**全部**，来支撑你的 AI 应用开发。

### 应用类型 <a href="#application_type" id="application_type"></a>

Dify 中提供了五种应用类型：

* **聊天助手**：基于 LLM 构建对话式交互的助手
* **文本生成应用**：面向文本生成类任务的助手，例如撰写故事、文本分类、翻译等
* **Agent**：能够分解任务、推理思考、调用工具的对话式智能助手
* **对话流**：适用于定义等复杂流程的多轮对话场景，具有记忆功能的应用编排方式
* **工作流**：适用于自动化、批处理等单轮生成类任务的场景的应用编排方式

文本生成应用与聊天助手的区别见下表：

<table><thead><tr><th width="180.33333333333331"></th><th>文本生成应用</th><th>聊天助手</th></tr></thead><tbody><tr><td>WebApp 界面</td><td>表单+结果式</td><td>聊天式</td></tr><tr><td>WebAPI 端点</td><td><code>completion-messages</code></td><td><code>chat-messages</code></td></tr><tr><td>交互方式</td><td>一问一答</td><td>多轮对话</td></tr><tr><td>流式结果返回</td><td>支持</td><td>支持</td></tr><tr><td>上下文保存</td><td>当次</td><td>持续</td></tr><tr><td>用户输入表单</td><td>支持</td><td>支持</td></tr><tr><td>知识库与插件</td><td>支持</td><td>支持</td></tr><tr><td>AI 开场白</td><td>不支持</td><td>支持</td></tr><tr><td>情景举例</td><td>翻译、判断、索引</td><td>聊天</td></tr></tbody></table>

