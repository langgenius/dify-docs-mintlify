# Model

Reverse Model Request refers to the plugin's ability to make reverse requests to LLM capabilities within Dify, including all model types and features on the platform, such as TTS, Rerank, etc.

Note that requesting models requires passing a ModelConfig type parameter. Its structure can be referenced in Common Specification Definitions, and this structure will have slight differences for different types of models.

For example, for LLM type models, it needs to include `completion_params` and `mode` parameters. You can manually build this structure or use `model-selector` type parameters or configuration.

### **Request LLM**

#### Entry

```python
self.session.model.llm
```

#### Endpoint:

```python
def invoke(
    self,
    model_config: LLMModelConfig,
    prompt_messages: list[PromptMessage],
    tools: list[PromptMessageTool] | None = None,
    stop: list[str] | None = None,
    stream: bool = True,
) -> Generator[LLMResultChunk, None, None] | LLMResult:
    pass
```

Note: If the model you're requesting doesn't have tool\_call capability, the tools passed here won't take effect.

#### **Example**

If you want to request OpenAI's gpt-4o-mini model in a Tool, refer to the following example code:

```python
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.model.llm import LLMModelConfig
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.entities.model.message import SystemPromptMessage, UserPromptMessage

class LLMTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        response = self.session.model.llm.invoke(
            model_config=LLMModelConfig(
                provider='openai',
                model='gpt-4o-mini',
                mode='chat',
                completion_params={}
            ),
            prompt_messages=[
                SystemPromptMessage(
                    content='you are a helpful assistant'
                ),
                UserPromptMessage(
                    content=tool_parameters.get('query')
                )
            ],
            stream=True
        )

        for chunk in response:
            if chunk.delta.message:
                assert isinstance(chunk.delta.message.content, str)
                yield self.create_text_message(text=chunk.delta.message.content)
```

Notice that the `query` parameter from `tool_parameters` is passed in the code.

### **Best Practices**

It's not recommended to manually build `LLMModelConfig`. Instead, allow users to select their desired model in the UI. In this case, you can modify the tool's parameter list by adding a `model` parameter according to the following configuration:

```yaml
identity:
  name: llm
  author: Dify
  label:
    en_US: LLM
    zh_Hans: LLM
    pt_BR: LLM
description:
  human:
    en_US: A tool for invoking a large language model
    zh_Hans: 用于调用大型语言模型的工具
    pt_BR: A tool for invoking a large language model
  llm: A tool for invoking a large language model
parameters:
  - name: prompt
    type: string
    required: true
    label:
      en_US: Prompt string
      zh_Hans: 提示字符串
      pt_BR: Prompt string
    human_description:
      en_US: used for searching
      zh_Hans: 用于搜索网页内容
      pt_BR: used for searching
    llm_description: key words for searching
    form: llm
  - name: model
    type: model-selector
    scope: llm
    required: true
    label:
      en_US: Model
      zh_Hans: 使用的模型
      pt_BR: Model
    human_description:
      en_US: Model
      zh_Hans: 使用的模型
      pt_BR: Model
    llm_description: which Model to invoke
    form: form
extra:
  python:
    source: tools/llm.py
```

Note that in this example, the model's scope is specified as llm, so users can only select `llm` type parameters. This allows you to modify the above example code as follows:

```python
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.model.llm import LLMModelConfig
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.entities.model.message import SystemPromptMessage, UserPromptMessage

class LLMTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        response = self.session.model.llm.invoke(
            model_config=tool_parameters.get('model'),
            prompt_messages=[
                SystemPromptMessage(
                    content='you are a helpful assistant'
                ),
                UserPromptMessage(
                    content=tool_parameters.get('query')
                )
            ],
            stream=True
        )

        for chunk in response:
            if chunk.delta.message:
                assert isinstance(chunk.delta.message.content, str)
                yield self.create_text_message(text=chunk.delta.message.content)
```

### **Request Summary**

You can request this endpoint to summarize a text. It will use the system model in your current workspace to summarize the text.

**Entry**:

```python
self.session.model.summary
```

**Endpoint**:

* `text`: The text to be summarized
* `instruction`: Additional instructions you want to add, allowing you to stylize the summary

```python
def invoke(
    self, text: str, instruction: str,
) -> str:
```

**Request TextEmbedding**

**Entry**

```python
self.session.model.text_embedding
```

**Endpoint**

```python
def invoke(
    self, model_config: TextEmbeddingResult, texts: list[str]
) -> TextEmbeddingResult:
    pass
```

### **Request Rerank**

#### Entry

```python
self.session.model.rerank
```

#### Endpoint

```python
def invoke(
    self, model_config: RerankModelConfig, docs: list[str], query: str
) -> RerankResult:
    pass
```

### **Request TTS**

#### Entry

```python
self.session.model.tts
```

#### Endpoint

```python
def invoke(
    self, model_config: TTSModelConfig, content_text: str
) -> Generator[bytes, None, None]:
    pass
```

Note: The bytes stream returned by the TTS endpoint is an mp3 audio byte stream, with each iteration returning a complete audio. If you want to perform more in-depth processing tasks, please select an appropriate library.

### **Request Speech2Text**

**Entry**:

```python
self.session.model.speech2text
```

**Endpoint**:

```python
def invoke(
    self, model_config: Speech2TextModelConfig, file: IO[bytes]
) -> str:
    pass
```

Where file is an mp3-encoded audio file.

### **Request Moderation**

**Entry**:

```python
self.session.model.moderation
```

**Endpoint**:

```python
def invoke(self, model_config: ModerationModelConfig, text: str) -> bool:
    pass
```

If this endpoint returns `true`, it indicates that the `text` contains sensitive content.
