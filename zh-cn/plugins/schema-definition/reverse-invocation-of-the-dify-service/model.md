# Model

反向调用 Model 指的是插件能够反向调用 Dify 内 LLM 的能力，包括平台内的所有模型类型与功能，例如 TTS、Rerank 等。

不过请注意，调用模型需要传入一个 `ModelConfig` 类型的参数，它的结构可以参考 [通用规范定义](../general-specifications.md)，并且对于不同类型的模型，该结构会存在细微的差别。

例如对于 `LLM` 类型的模型，还需要包含 `completion_params` 与 `mode` 参数，你可以手动构建该结构，或者使用 `model-selector` 类型的参数或配置。

### 调用 LLM

#### **入口**

```python
    self.session.model.llm
```

#### **接口**

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

请注意，如果你调用的模型不具备 `tool_call` 的能力，那么此处传入的 `tools` 将不会生效。

#### **用例**

如果想在 `Tool` 中调用 `OpenAI` 的 `gpt-4o-mini` 模型，请参考以下示例代码：

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

可以留意到代码中传入了 `tool_parameters` 中的 `query` 参数。

### **最佳实践**

并不建议手动来构建 `LLMModelConfig`，而是允许用户可以在 UI 上选择自己想使用的模型，在这种情况下可以修改一下工具的参数列表，按照如下配置，添加一个 `model` 参数：

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

请注意在该例子中指定了 `model` 的 `scope` 为 `llm`，那么此时用户就只能选择 `llm` 类型的参数，从而可以将上述用例的代码改成以下代码：

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

### 调用 Summary

你可以请求该接口来总结一段文本，它会使用你当前 workspace 内的系统模型来总结文本。

**入口**

```python
    self.session.model.summary
```

**接口**

* `text` 为需要被总结的文本。
* `instruction` 为你想要额外添加的指令，它可以让你风格化地总结文本。

```python
    def invoke(
        self, text: str, instruction: str,
    ) -> str:
```

### 调用 TextEmbedding

**入口**

```python
    self.session.model.text_embedding
```

**接口**

```python
    def invoke(
        self, model_config: TextEmbeddingResult, texts: list[str]
    ) -> TextEmbeddingResult:
        pass
```

### 调用 Rerank

**入口**

```python
    self.session.model.rerank
```

**接口**

```python
    def invoke(
        self, model_config: RerankModelConfig, docs: list[str], query: str
    ) -> RerankResult:
        pass
```

### 调用 TTS

**入口**

```python
    self.session.model.tts
```

**接口**

```python
    def invoke(
        self, model_config: TTSModelConfig, content_text: str
    ) -> Generator[bytes, None, None]:
        pass
```

请注意 `tts` 接口返回的 `bytes` 流是一个 `mp3` 音频字节流，每一轮迭代返回的都是一个完整的音频。如果你想做更深入的处理任务，请选择合适的库进行。

### 调用 Speech2Text

**入口**

```python
    self.session.model.speech2text
```

**接口**

```python
    def invoke(
        self, model_config: Speech2TextModelConfig, file: IO[bytes]
    ) -> str:
        pass
```

其中 `file` 是一个 `mp3` 格式编码的音频文件。

### 调用 Moderation

**入口**

```python
    self.session.model.moderation
```

**接口**

```python
    def invoke(self, model_config: ModerationModelConfig, text: str) -> bool:
        pass
```

若该接口返回 `true` 则表示 `text` 中包含敏感内容。
