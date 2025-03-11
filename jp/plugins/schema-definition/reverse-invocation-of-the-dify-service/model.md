# モデル

リバースモデルリクエストとは、プラグインがDify内のLLM機能に対してリバースリクエストを行う能力を指し、TTS、Rerankなど、プラットフォーム上のすべてのモデルタイプと機能が含まれます。

モデルのリクエストには、ModelConfigタイプのパラメータを渡す必要があることに注意してください。その構造は共通仕様定義で参照でき、この構造は異なるタイプのモデルで若干の違いがあります。

例えば、LLMタイプのモデルの場合、`completion_params`と`mode`パラメータを含める必要があります。この構造は手動で構築するか、`model-selector`タイプのパラメータまたは設定を使用することができます。

### **LLMのリクエスト**

#### エントリー

```python
self.session.model.llm
```

#### エンドポイント：

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

注意：リクエストするモデルにtool_call機能がない場合、ここで渡されるツールは効果を持ちません。

#### **例**

ツールでOpenAIのgpt-4o-miniモデルをリクエストする場合は、以下のサンプルコードを参照してください：

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

コードでは`tool_parameters`から`query`パラメータが渡されていることに注意してください。

### **ベストプラクティス**

`LLMModelConfig`を手動で構築することは推奨されません。代わりに、UIでユーザーが希望のモデルを選択できるようにします。この場合、以下の設定に従って`model`パラメータを追加することでツールのパラメータリストを変更できます：

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

この例では、モデルのスコープがllmとして指定されているため、ユーザーは`llm`タイプのパラメータのみを選択できることに注意してください。これにより、上記の例のコードを以下のように変更できます：

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

### **要約のリクエスト**

このエンドポイントを使用してテキストを要約することができます。現在のワークスペースのシステムモデルを使用してテキストを要約します。

**エントリー**：

```python
self.session.model.summary
```

**エンドポイント**：

* `text`: 要約するテキスト
* `instruction`: 追加の指示。要約のスタイルをカスタマイズできます

```python
def invoke(
    self, text: str, instruction: str,
) -> str:
```

**テキスト埋め込みのリクエスト**

**エントリー**

```python
self.session.model.text_embedding
```

**エンドポイント**

```python
def invoke(
    self, model_config: TextEmbeddingResult, texts: list[str]
) -> TextEmbeddingResult:
    pass
```

### **Rerankのリクエスト**

#### エントリー

```python
self.session.model.rerank
```

#### エンドポイント

```python
def invoke(
    self, model_config: RerankModelConfig, docs: list[str], query: str
) -> RerankResult:
    pass
```

### **TTSのリクエスト**

#### エントリー

```python
self.session.model.tts
```

#### エンドポイント

```python
def invoke(
    self, model_config: TTSModelConfig, content_text: str
) -> Generator[bytes, None, None]:
    pass
```

注意：TTSエンドポイントが返すバイトストリームはmp3オーディオバイトストリームで、各イテレーションで完全なオーディオを返します。より高度な処理タスクを実行したい場合は、適切なライブラリを選択してください。

### **音声認識のリクエスト**

**エントリー**：

```python
self.session.model.speech2text
```

**エンドポイント**：

```python
def invoke(
    self, model_config: Speech2TextModelConfig, file: IO[bytes]
) -> str:
    pass
```

ここで、fileはmp3エンコードされたオーディオファイルです。

### **モデレーションのリクエスト**

**エントリー**：

```python
self.session.model.moderation
```

**エンドポイント**：

```python
def invoke(self, model_config: ModerationModelConfig, text: str) -> bool:
    pass
```

このエンドポイントが`true`を返す場合、`text`に機密コンテンツが含まれていることを示します。
