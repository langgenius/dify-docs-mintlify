# 开始

### 定义

**"开始"** 节点是每个工作流应用（Chatflow / Workflow）必备的预设节点，为后续工作流节点以及应用的正常流转提供必要的初始信息，例如应用使用者所输入的内容、以及[上传的文件](../file-upload.md)等。

### 配置节点

在开始节点的设置页，你可以看到两部分设置，分别是 **“输入字段”** 和预设的[**系统变量**](../variables.md#xi-tong-bian-liang)。

![Chatflow 和 Workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/workflow/node/c4a9bb46f636807f0b59710724fddc40.png)

### 输入字段

输入字段功能由应用开发者设置，通常用于让应用使用者主动补全更多信息。例如在周报应用中要求使用者按照格式预先提供更多背景信息，如姓名、工作日期区间、工作详情等。这些前置信息将有助于 LLM 生成质量更高的答复。

支持以下六种类型输入变量，所有变量均可设置为必填项：

*   **文本**

    短文本，由应用使用者自行填写内容，最大长度 256 字符。
*   **段落**

    长文本，允许应用使用者输入较长字符。
*   **下拉选项**

    由应用开发者固定选项，应用使用者仅能选择预设选项，无法自行填写内容。
*   **数字**

    仅允许用户输入数字。
*   **单文件**

    允许应用使用者单独上传文件，支持文档类型文件、图片、音频、视频和其它文件类型。支持通过本地上传文件或粘贴文件 URL。详细用法请参考[文件上传](../file-upload.md)。
*   **文件列表**

    允许应用使用者批量上传文件，支持文档类型文件、图片、音频、视频和其它文件类型。支持通过本地上传文件或粘贴文件 URL。详细用法请参考[文件上传](../file-upload.md)。

{% hint style="info" %}
Dify 内置的文档提取器节点只能够处理部分格式的文档文件。如需处理图片、音频或视频类型文件，请参考[外部数据工具](../../extension/api-based-extension/external-data-tool.md)搭建对应文件的处理节点。
{% endhint %}

配置完成后，用户在使用应用前将按照输入项指引，向 LLM 提供必要信息。更多的信息将有助于 LLM 提升问答效率。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/workflow/node/400679ae5cbbcd5dc0f84ec5861efc85.png)

### 系统变量

系统变量指的是在 Chatflow / Workflow 应用内预设的系统级参数，可以被应用内的其它节点全局读取。通常用于进阶开发场景，例如搭建多轮次对话应用、收集应用日志与监控、记录不同应用和用户的使用行为等。

**Workflow**

Workflow 类型应用提供以下系统变量：

<table><thead><tr><th width="193">变量名称</th><th width="116">数据类型</th><th width="278">说明</th><th>备注</th></tr></thead><tbody><tr><td><p><code>sys.files</code></p><p><code>[LEGACY]</code></p></td><td>Array[File]</td><td>文件参数，存储用户初始使用应用时上传的图片</td><td>图片上传功能需在应用编排页右上角的 “功能” 处开启</td></tr><tr><td><code>sys.user_id</code></td><td>String</td><td>用户 ID，每个用户在使用工作流应用时，系统会自动向用户分配唯一标识符，用以区分不同的对话用户</td><td></td></tr><tr><td><code>sys.app_id</code></td><td>String</td><td>应用 ID，系统会向每个 Workflow 应用分配一个唯一的标识符，用以区分不同的应用，并通过此参数记录当前应用的基本信息</td><td>面向具备开发能力的用户，通过此参数区分并定位不同的 Workflow 应用</td></tr><tr><td><code>sys.workflow_id</code></td><td>String</td><td>Workflow ID，用于记录当前 Workflow 应用内所包含的所有节点信息</td><td>面向具备开发能力的用户，可以通过此参数追踪并记录 Workflow 内的包含节点信息</td></tr><tr><td><code>sys.workflow_run_id</code></td><td>String</td><td>Workflow 应用运行 ID，用于记录 Workflow 应用中的运行情况</td><td>面向具备开发能力的用户，可以通过此参数追踪应用的历次运行情况</td></tr></tbody></table>

![Workflow 类型应用系统变量](https://docs.dify.ai/~gitbook/image?url=https%3A%2F%2F1288284732-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCdDIVDY6AtAz028MFT4d%252Fuploads%252FrN6uw5MOfjV2xsDnQsV1%252Fimage.png%3Falt%3Dmedia%26token%3D309a9336-7bd7-4ef6-8621-779538245e25&width=768&dpr=4&quality=100&sign=9d7d625a&sv=1)

**Chatflow**

Chatflow 类型应用提供以下系统变量：

<table><thead><tr><th>变量名称</th><th width="127">数据类型</th><th width="283">说明</th><th>备注</th></tr></thead><tbody><tr><td><code>sys.query</code></td><td>String</td><td>用户在对话框中初始输入的内容</td><td></td></tr><tr><td><code>sys.files</code></td><td>Array[File]</td><td>用户在对话框内上传的图片</td><td>图片上传功能需在应用编排页右上角的 “功能” 处开启</td></tr><tr><td><code>sys.dialogue_count</code></td><td>Number</td><td><p>用户在与 Chatflow 类型应用交互时的对话轮数。每轮对话后自动计数增加 1，可以和 if-else 节点搭配出丰富的分支逻辑。</p><p>例如到第 X 轮对话时，回顾历史对话并给出分析</p></td><td></td></tr><tr><td><code>sys.conversation_id</code></td><td>String</td><td>对话框交互会话的唯一标识符，将所有相关的消息分组到同一个对话中，确保 LLM 针对同一个主题和上下文持续对话</td><td></td></tr><tr><td><code>sys.user_id</code></td><td>String</td><td>分配给每个应用用户的唯一标识符，用以区分不同的对话用户</td><td></td></tr><tr><td><code>sys.app_id</code></td><td>String</td><td>应用 ID，系统会向每个 Workflow 应用分配一个唯一的标识符，用以区分不同的应用，并通过此参数记录当前应用的基本信息</td><td>面向具备开发能力的用户，通过此参数区分并定位不同的 Workflow 应用</td></tr><tr><td><code>sys.workflow_id</code></td><td>String</td><td>Workflow ID，用于记录当前 Workflow 应用内所包含的所有节点信息</td><td>面向具备开发能力的用户，可以通过此参数追踪并记录 Workflow 内的包含节点信息</td></tr><tr><td><code>sys.workflow_run_id</code></td><td>String</td><td>Workflow 应用运行 ID，用于记录 Workflow 应用中的运行情况</td><td>面向具备开发能力的用户，可以通过此参数追踪应用的历次运行情况</td></tr></tbody></table>

![Chatflow 类型应用系统变量](https://docs.dify.ai/~gitbook/image?url=https%3A%2F%2F1288284732-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCdDIVDY6AtAz028MFT4d%252Fuploads%252FnEabPflR315QnAEeLhLN%252Fimage.png%3Falt%3Dmedia%26token%3D1f475f55-7d2f-4a79-afa0-ca4b1b803e49&width=768&dpr=4&quality=100&sign=c46697af&sv=1)
