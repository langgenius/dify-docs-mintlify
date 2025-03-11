# Tool

Before reading the detailed interface documentation, make sure you have read [Quick start: Tools](../develop-plugins/tool-plugin.md) and have a general understanding of the Dify plugin's tool access process.

### **Data Structures**

#### **Message Returns**

Dify supports multiple message types including `text`, `links`, `images`, `file BLOBs`, and `JSON`. You can return different types of messages through various interfaces.

By default, a tool's output in a `workflow` contains three fixed variables: `files`, `text`, and `json`. You can return data for these three variables using the methods below.

For example, use `create_image_message` to return images. Tools also support custom output variables for easier reference in `workflow`.

#### **Image URL**

Simply pass the image URL, and Dify will automatically download and return the image to users.

```python
def create_image_message(self, image: str) -> ToolInvokeMessage:
    pass
```

#### **Links**

Use this interface to return a link:

```python
def create_link_message(self, link: str) -> ToolInvokeMessage:
    pass
```

#### **Text**

Use this interface to return a text message:

```python
def create_text_message(self, text: str) -> ToolInvokeMessage:
    pass
```

#### **Files**

Use this interface to return raw file data (images, audio, video, PPT, Word, Excel, etc.):

* `blob`: Raw file data in bytes
* `meta`: File metadata. Specify `mime_type` if needed, otherwise Dify uses `octet/stream` as default

```python
def create_blob_message(self, blob: bytes, meta: dict = None) -> ToolInvokeMessage:
    pass
```

#### **JSON**

Use this interface to return formatted JSON. Commonly used for data transfer between workflow nodes. Most large models can read and understand JSON in agent mode.

```python
def create_json_message(self, json: dict) -> ToolInvokeMessage:
    pass
```

#### **Variables**

For non-streaming output variables, use this interface. Later values override earlier ones:

```python
def create_variable_message(self, variable_name: str, variable_value: Any) -> ToolInvokeMessage:
    pass
```

#### **Streaming Variables**

For typewriter-effect text output, use streaming variables. If you reference this variable in a chatflow application's answer node, text will display with a typewriter effect. Currently only supports string data:

```python
def create_stream_variable_message(
    self, variable_name: str, variable_value: str
) -> ToolInvokeMessage:
```

#### **Return Variable Definitions**

To reference tool output variables in workflow applications, you need to define possible output variables beforehand. Dify plugins support `json_schema` format output variable definitions. Here's a simple example:

```yaml
identity:
  author: author
  name: tool
  label:
    en_US: label
    zh_Hans: 标签
    ja_JP: ラベル
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

This example defines a simple tool with an `output_schema` containing a `name` field that can be referenced in `workflow`. Note that you still need to return a variable in the tool's implementation code for actual use, otherwise it will return `None`.
