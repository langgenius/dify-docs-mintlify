# 反向调用 Dify 服务

插件可以自由调用 Dify 主平台内的部分服务，用以提升插件的能力。

### 可被调用的 Dify 模块

*   [App](app.md)

    插件能够访问 Dify 平台内 App 的数据。
*   [Model](model.md)

    插件能够反向调用 Dify 平台内的 LLM 能力，包括平台内的所有模型类型与功能，例如 TTS、Rerank 等。
*   [Tool](tool.md)

    插件能够调用 Dify 平台内的其它工具类型插件。
*   [Node](node.md)

    插件能够调用 Dify 平台内某个 Chatflow/Workflow 应用内的节点。