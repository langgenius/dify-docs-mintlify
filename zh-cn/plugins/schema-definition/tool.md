# Tool

在阅读详细的接口文档之前，请确保你已经阅读过[快速开始开发插件：工具](../quick-start/develop-plugins/tool-type-plugin.md)，并对 Dify 插件的工具接入流程已有大致了解。

### 数据结构

#### 消息返回

Dify 支持`文本` `链接` `图片` `文件BLOB` `JSON` 等多种消息类型，你可以通过以下不同的接口返回不同类型的消息。

在默认情况下，一个工具在 `workflow` 中的输出会包含 `files` `text` `json` 三个固定变量，且你可以通过下面的方法来返回这三个变量的数据。

例如使用 `create_image_message` 来返回图片，但是同时工具也支持自定义的输出变量，从而可以更方便地在 `workflow` 中引用这些变量。

#### **图片 URL**

只需要传递图片的 URL，Dify 将通过链接自动下载图片并返回给用户。

```python
    def create_image_message(self, image: str) -> ToolInvokeMessage:
        pass
```

#### **链接**

如果你需要返回一个链接，使用以下接口。

```python
    def create_link_message(self, link: str) -> ToolInvokeMessage:
        pass
```

#### **文本**

如果你需要返回一个文本消息，使用以下接口。

```python
    def create_text_message(self, text: str) -> ToolInvokeMessage:
        pass
```

**文件**

如果你需要返回文件的原始数据，如图片、音频、视频、PPT、Word、Excel 等，可以使用以下接口。

* `blob` 文件的原始数据，bytes 类型。
* `meta` 文件的元数据。如果开发者需要明确的文件类型，请指定`mime_type`，否则 Dify 将使用`octet/stream`作为默认类型。

```python
    def create_blob_message(self, blob: bytes, meta: dict = None) -> ToolInvokeMessage:
        pass
```

#### **JSON**

如果你需要返回一个格式化的 JSON，可以使用以下接口。这通常用于 workflow 中的节点间的数据传递。在 agent 模式中，大部分大模型也都能够阅读和理解 JSON。

* `object` 一个 Python 的字典对象，会被自动序列化为 JSON。

```python
    def create_json_message(self, json: dict) -> ToolInvokeMessage:
        pass
```

#### **变量**

对于非流式输出的变量，你可以使用以下接口返回，如创建多份，后者将覆盖前者。

```python
    def create_variable_message(self, variable_name: str, variable_value: Any) -> ToolInvokeMessage:
        pass
```

#### **流式变量**

如果你想以“打字机”效果输出一段文字，可以使用流式变量输出文本。如果你在 `chatflow` 应用中使用 `answer` 节点并引用了该变量，那么文本将以“打字机”的效果输出。但目前该方法仅支持字符串类型的数据。

```python
    def create_stream_variable_message(
        self, variable_name: str, variable_value: str
    ) -> ToolInvokeMessage:
```

#### 返回变量定义

如果想要在 `workflow` 应用中引用 `tool` 的输出变量，则有必要提前定义有哪些变量可能被输出。Dify 插件支持使用 [`json_schema`](https://json-schema.org/)格式的输出变量定义，以下是一个简单的示例：

```yaml
identity:
  author: author
  name: tool
  label:
    en_US: label
    zh_Hans: 标签
    ja_JP: レベル
    pt_BR: etiqueta
description:
  human:
    en_US: description
    zh_Hans: 描述
    ja_JP: 説明
    pt_BR: descrição
  llm: description
output_schema:
  type: object
  properties:
    name:
      type: string
```

上述示例代码定义了一个简单的工具，并为它指定了 `output_schema`，其中包含一个 `name` 字段，此时可以在 `workflow` 中引用该字段。但是请注意，还需要在工具的实现代码中返回一个变量才可以真正使用，否则将得到一个 `None` 返回结果。
