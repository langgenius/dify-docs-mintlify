# インターフェース方法

ここでは、サプライヤーと各モデルタイプが実装する必要があるインターフェース方法とそのパラメータについて説明します。

## サプライヤー

`__base.model_provider.ModelProvider`基本クラスを継承し、以下のインターフェースを実装する必要があります：

```python
def validate_provider_credentials(self, credentials: dict) -> None:
    """
    Validate provider credentials
    You can choose any validate_credentials method of model type or implement validate method by yourself,
    such as: get model list api

    if validate failed, raise exception

    :param credentials: provider credentials, credentials form defined in `provider_credential_schema`.
    """
```

- `credentials` (object) 資格情報

  資格情報のパラメータは、サプライヤーのYAML構成ファイルの `provider_credential_schema` で定義され、`api_key`などが渡されます。

検証に失敗した場合は、`errors.validate.CredentialsValidateFailedError`エラーをスローします。

**注：事前定義されたモデルはこのインターフェースを完全に実装する必要がありますが、カスタムモデルサプライヤーは以下の簡単な実装のみが必要です**

```python
class XinferenceProvider(Provider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        pass
```

## モデル

モデルには5つの異なるモデルタイプがあり、異なる基底クラスを継承し、実装する必要があるメソッドも異なります。

### 一般インターフェース

すべてのモデルには以下の2つのメソッドを実装する必要があります：

- モデルの資格情報を検証する

  サプライヤーの資格情報検証と同様に、ここでは個々のモデルに対して検証を行います。

  ```python
  def validate_credentials(self, model: str, credentials: dict) -> None:
      """
      Validate model credentials
  
      :param model: model name
      :param credentials: model credentials
      :return:
      """
  ```

  パラメータ：

  - `model` (string) モデル名

  - `credentials` (object) 資格情報

    資格情報のパラメータは、供給業者の YAML 構成ファイルの provider_credential_schema または model_credential_schema で定義されており、api_key などの詳細が含まれます。
  
  検証に失敗した場合は、`errors.validate.CredentialsValidateFailedError` エラーをスローします。

- 例外エラーマッピングの呼び出し

  モデルの呼び出しが例外をスローした場合、Runtimeが指定する `InvokeError` タイプにマッピングする必要があり、異なるエラーに対して異なる後続処理を行うためのDifyにとって便利です。

  Runtime Errors:

  - `InvokeConnectionError` コール接続エラー
  - `InvokeServerUnavailableError ` コールサービスが利用できない
  - `InvokeRateLimitError ` コールが制限に達した
  - `InvokeAuthorizationError`  コール認証エラー
  - `InvokeBadRequestError ` コールパラメータが誤っています

  ```python
  @property
  def _invoke_error_mapping(self) -> dict[type[InvokeError], list[type[Exception]]]:
      """
      Map model invoke error to unified error
      The key is the error type thrown to the caller
      The value is the error type thrown by the model,
      which needs to be converted into a unified error type for the caller.
  
      :return: Invoke error mapping
      """
  ```

  または、対応するエラーを直接スローし、以下のように定義することもできます。これにより、後続の呼び出しで `InvokeConnectionError` などの例外を直接スローできます。
  
    ```python
    @property
    def _invoke_error_mapping(self) -> dict[type[InvokeError], list[type[Exception]]]:
        return {
            InvokeConnectionError: [
              InvokeConnectionError
            ],
            InvokeServerUnavailableError: [
              InvokeServerUnavailableError
            ],
            InvokeRateLimitError: [
              InvokeRateLimitError
            ],
            InvokeAuthorizationError: [
              InvokeAuthorizationError
            ],
            InvokeBadRequestError: [
              InvokeBadRequestError
            ],
        }
    ```

​	OpenAIの `_invoke_error_mapping` をご参照ください。 

### LLM

`__base.large_language_model.LargeLanguageModel` 基本クラスを継承し、以下のインターフェースを実装します：

- LLMの呼び出し

  LLM呼び出しの核心メソッドを実装し、ストリーミングと同期応答の両方をサポートします。

  ```python
  def _invoke(self, model: str, credentials: dict,
              prompt_messages: list[PromptMessage], model_parameters: dict,
              tools: Optional[list[PromptMessageTool]] = None, stop: Optional[list[str]] = None,
              stream: bool = True, user: Optional[str] = None) \
          -> Union[LLMResult, Generator]:
      """
      Invoke large language model
  
      :param model: model name
      :param credentials: model credentials
      :param prompt_messages: prompt messages
      :param model_parameters: model parameters
      :param tools: tools for tool calling
      :param stop: stop words
      :param stream: is stream response
      :param user: unique user id
      :return: full response or stream response chunk generator result
      """
  ```

  - パラメータ：

    - `model` (string) モデル名

    - `credentials` (object) 資格情報
    
      資格情報のパラメータは、供給業者の YAML 構成ファイルの provider_credential_schema または model_credential_schema で定義されており、api_key などの詳細が含まれます。

    - `prompt_messages` (array[[PromptMessage](#PromptMessage)]) Prompt リスト
    
      モデルのタイプが `Completion` の場合、リストには1つの[UserPromptMessage](#UserPromptMessage) 要素のみを渡す必要があります；
    
      モデルのタイプが `Chat` の場合、[SystemPromptMessage](#SystemPromptMessage), [UserPromptMessage](#UserPromptMessage), [AssistantPromptMessage](#AssistantPromptMessage), [ToolPromptMessage](#ToolPromptMessage) 要素のリストをメッセージに応じて渡す必要があります。

    - `model_parameters` (object) モデルのパラメータ
    
      モデルのパラメータは、モデルのYAML設定における`parameter_rules`で定義されています。

    - `tools` (array[[PromptMessageTool](#PromptMessageTool)]) [optional] ツールのリスト，`function calling` 内の `function` に相当します。
    
      つまり、tool calling のためのツールリストを指定します。

    - `stop` (array[string]) [optional] ストップシーケンス
    
      モデルが出力を返す際に、定義された文字列の前で出力を停止します。

    - `stream` (bool) ストリーム出力の有無、デフォルトはTrue
    
      ストリーム出力の場合は Generator[[LLMResultChunk](#LLMResultChunk)]，出力ではないの場合は [LLMResult](#LLMResult)。

    - `user` (string) [optional] ユーザーの一意の識別子
    
      供給業者が不正行為を監視および検出するのに役立ちます。

  - 返り値

    ストリーム出力の場合は Generator[[LLMResultChunk](#LLMResultChunk)]，出力ではないの場合は [LLMResult](#LLMResult)。

- 入力tokenの事前計算

  モデルがtokenの事前計算インターフェースを提供していない場合、直接0を返すことができます。

  ```python
  def get_num_tokens(self, model: str, credentials: dict, prompt_messages: list[PromptMessage],
                     tools: Optional[list[PromptMessageTool]] = None) -> int:
      """
      Get number of tokens for given prompt messages

      :param model: model name
      :param credentials: model credentials
      :param prompt_messages: prompt messages
      :param tools: tools for tool calling
      :return:
      """
  ```

  パラメータの説明は上記の `LLMの呼び出し` を参照してください。

  このインターフェースは、対応する`model`に基づいて適切な`tokenizer`を選択して計算する必要があります。対応するモデルが`tokenizer`を提供していない場合は、`AIModel`ベースクラスの`_get_num_tokens_by_gpt2(text: str)`メソッドを使用して計算できます。

- カスタムモデルスキーマの取得 [オプション]

  ```python
  def get_customizable_model_schema(self, model: str, credentials: dict) -> Optional[AIModelEntity]:
      """
      Get customizable model schema

      :param model: model name
      :param credentials: model credentials
      :return: model schema
      """
  ```

供給業者がカスタムLLMを追加することをサポートしている場合、このメソッドを実装してカスタムモデルがモデル規則を取得できるようにすることができます。デフォルトではNoneを返します。

ほとんどの微調整モデルは`OpenAI`供給業者の下で、微調整モデル名を使用してベースモデルを取得できます。例えば、`gpt-3.5-turbo-1106`のような微調整モデル名を使用して、基本モデルの事前定義されたパラメータルールを取得できます。具体的な実装については、[openai](https://github.com/langgenius/dify-runtime/blob/main/lib/model_providers/anthropic/llm/llm.py)を参照してください。

### TextEmbedding

`__base.text_embedding_model.TextEmbeddingModel`ベースクラスを継承し、次のインターフェースを実装します：

- Embeddingの呼び出し

  ```python
  def _invoke(self, model: str, credentials: dict,
              texts: list[str], user: Optional[str] = None) \
          -> TextEmbeddingResult:
      """
      Invoke large language model
  
      :param model: model name
      :param credentials: model credentials
      :param texts: texts to embed
      :param user: unique user id
      :return: embeddings result
      """
  ```

  - パラメータ：

    - `model` (string) モデル名

    - `credentials` (object) 資格情報
    
      資格情報のパラメータは、供給業者の YAML 構成ファイルの provider_credential_schema または model_credential_schema で定義されており、api_key などの詳細が含まれます。

    - `texts` (array[string]) テキストリスト，バッチで処理できる

    - `user` (string) [optional] ユーザーの一意の識別子

      供給業者が不正行為を監視および検出するのに役立ちます。

  - 返り値：

    [TextEmbeddingResult](#TextEmbeddingResult) エンティティ。

- tokensの事前計算

  ```python
  def get_num_tokens(self, model: str, credentials: dict, texts: list[str]) -> int:
      """
      Get number of tokens for given prompt messages

      :param model: model name
      :param credentials: model credentials
      :param texts: texts to embed
      :return:
      """
  ```

  パラメータの説明は上記の `Embeddingの呼び出し` を参照してください。

  上記の`LargeLanguageModel`と同様に、このインターフェースは、対応する`model`に基づいて適切な`tokenizer`を選択して計算する必要があります。対応するモデルが`tokenizer`を提供していない場合は、`AIModel`ベースクラスの`_get_num_tokens_by_gpt2(text: str)`メソッドを使用して計算できます。

### Rerank

`__base.rerank_model.RerankModelベースクラスを継承し、次のインターフェースを実装します：

- rerankの呼び出し

  ```python
  def _invoke(self, model: str, credentials: dict,
              query: str, docs: list[str], score_threshold: Optional[float] = None, top_n: Optional[int] = None,
              user: Optional[str] = None) \
          -> RerankResult:
      """
      Invoke rerank model
  
      :param model: model name
      :param credentials: model credentials
      :param query: search query
      :param docs: docs for reranking
      :param score_threshold: score threshold
      :param top_n: top n
      :param user: unique user id
      :return: rerank result
      """
  ```

  - パラメータ：

    - `model` (string) モデル名

    - `credentials` (object) 資格情報
    
      資格情報のパラメータは、供給業者の YAML 構成ファイルの provider_credential_schema または model_credential_schema で定義されており、api_key などの詳細が含まれます。

    - `query` (string) リクエスト内容をチェックする

    - `docs` (array[string]) 並べ替えが必要なセクションリスト

    - `score_threshold` (float) [optional] Scoreの閾値

    - `top_n` (int) [optional] トップのnセクションを取得します

    - `user` (string) [optional] ユーザーの一意の識別子

      供給業者が不正行為を監視および検出するのに役立ちます。

  - 返り値：

    [RerankResult](#RerankResult) エンティティ。

### Speech2text

`__base.speech2text_model.Speech2TextModel`基底クラスを継承し、以下のインターフェースを実装します：

- Invokeの呼び出し

  ```python
  def _invoke(self, model: str, credentials: dict,
              file: IO[bytes], user: Optional[str] = None) \
          -> str:
      """
      Invoke large language model
  
      :param model: model name
      :param credentials: model credentials
      :param file: audio file
      :param user: unique user id
      :return: text for given audio file
      """	
  ```

  - パラメータ：

    - `model` (string) モデル名

    - `credentials` (object) 資格情報

      資格情報のパラメータは、供給業者の YAML 構成ファイルの provider_credential_schema または model_credential_schema で定義されており、api_key などの詳細が含まれます。

    - `file` (File) ファイルストリーム

    - `user` (string) [optional] ユーザーの一意の識別子

      供給業者が不正行為を監視および検出するのに役立ちます。

  - 返り値：

    音声をテキストに変換した結果を返します。

### Text2speech

`__base.text2speech_model.Text2SpeechModel`基底クラスを継承し、以下のインターフェースを実装します：

- Invokeの呼び出し

  ```python
  def _invoke(self, model: str, credentials: dict, content_text: str, streaming: bool, user: Optional[str] = None):
      """
      Invoke large language model
  
      :param model: model name
      :param credentials: model credentials
      :param content_text: text content to be translated
      :param streaming: output is streaming
      :param user: unique user id
      :return: translated audio file
      """	
  ```

  - パラメータ：

    - `model` (string) モデル名

    - `credentials` (object) 資格情報

      資格情報のパラメータは、供給業者の YAML 構成ファイルの provider_credential_schema または model_credential_schema で定義されており、api_key などの詳細が含まれます。

    - `content_text` (string) 変換すべきテキストコンテンツ

    - `streaming` (bool) ストリーミング出力かどうか

    - `user` (string) [optional] ユーザーの一意の識別子

      供給業者が不正行為を監視および検出するのに役立ちます。

  - 返り値：

    テキストを音声に変換した結果を返します。

### Moderation

`__base.moderation_model.ModerationModel`基底クラスを継承し、以下のインターフェースを実装します：

- Invokeの呼び出し

  ```python
  def _invoke(self, model: str, credentials: dict,
              text: str, user: Optional[str] = None) \
          -> bool:
      """
      Invoke large language model
  
      :param model: model name
      :param credentials: model credentials
      :param text: text to moderate
      :param user: unique user id
      :return: false if text is safe, true otherwise
      """
  ```

  - パラメータ：

    - `model` (string) モデル名

    - `credentials` (object) 資格情報

      資格情報のパラメータは、供給業者の YAML 構成ファイルの provider_credential_schema または model_credential_schema で定義されており、api_key などの詳細が含まれます。

    - `text` (string) テキスト内容

    - `user` (string) [optional] ユーザーの一意の識別子

      供給業者が不正行為を監視および検出するのに役立ちます。

  - 返り値：

    False の場合は入力したテキストは安全であり、True の場合はその逆。



## エンティティ

### PromptMessageRole 

メッセージロールを定義する列挙型。

```python
class PromptMessageRole(Enum):
    """
    Enum class for prompt message.
    """
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"
```

### PromptMessageContentType

メッセージコンテンツのタイプを定義し、テキストと画像の2種類がある。

```python
class PromptMessageContentType(Enum):
    """
    Enum class for prompt message content type.
    """
    TEXT = 'text'
    IMAGE = 'image'
```

### PromptMessageContent

メッセージコンテンツの基底クラスであり、パラメータのみを宣言するため初期化は行えない。

```python
class PromptMessageContent(BaseModel):
    """
    Model class for prompt message content.
    """
    type: PromptMessageContentType
    data: str  # コンテンツデータ
```
現在、テキストと画像の2つのタイプがサポートされており、テキストと複数の画像を同時に渡すことができる。

テキストと画像を同時に渡す場合は、`TextPromptMessageContent` と `ImagePromptMessageContent` をそれぞれ初期化する必要がある。

### TextPromptMessageContent

```python
class TextPromptMessageContent(PromptMessageContent):
    """
    Model class for text prompt message content.
    """
    type: PromptMessageContentType = PromptMessageContentType.TEXT
```

画像とテキストを一緒に渡す場合、テキストは `content` リストの一部としてこのエンティティを構築する必要がある。

### ImagePromptMessageContent

```python
class ImagePromptMessageContent(PromptMessageContent):
    """
    Model class for image prompt message content.
    """
    class DETAIL(Enum):
        LOW = 'low'
        HIGH = 'high'

    type: PromptMessageContentType = PromptMessageContentType.IMAGE
    detail: DETAIL = DETAIL.LOW  # 解像度
```

画像とテキストを一緒に渡す場合、画像は `content` リストの一部としてこのエンティティを構築する必要がある。

`data` には `url` または画像の `base64` でエンコードされた文字列を指定することができる。

### PromptMessage

すべてのロールメッセージの基底クラスであり、パラメータのみを宣言するため初期化はできません。

```python
class PromptMessage(ABC, BaseModel):
    """
    Model class for prompt message.
    """
    role: PromptMessageRole  # メッセージロール
    content: Optional[str | list[PromptMessageContent]] = None  # 2つのタイプ、文字列とコンテンツリストをサポート。コンテンツリストはマルチモーダルのニーズを満たすために使用されます。PromptMessageContentの説明を参照してください。
    name: Optional[str] = None  # 名前、オプション
```

### UserPromptMessage

UserMessage ユーザーメッセージを表すクラス。

```python
class UserPromptMessage(PromptMessage):
    """
    Model class for user prompt message.
    """
    role: PromptMessageRole = PromptMessageRole.USER
```

### AssistantPromptMessage

モデルの返信メッセージを表し、通常は `few-shots` やチャット履歴が入力として使用されます。

```python
class AssistantPromptMessage(PromptMessage):
    """
    Model class for assistant prompt message.
    """
    class ToolCall(BaseModel):
        """
        Model class for assistant prompt message tool call.
        """
        class ToolCallFunction(BaseModel):
            """
            Model class for assistant prompt message tool call function.
            """
            name: str  # ツール名
            arguments: str  # ツールパラメータ

        id: str  # ツールID。OpenAI tool callの場合のみ有効で、ツール呼び出しのユニークIDです。同じツールを複数回呼び出すことができます。
        type: str  # デフォルト function
        function: ToolCallFunction  # ツール呼び出し情報

    role: PromptMessageRole = PromptMessageRole.ASSISTANT
    tool_calls: list[ToolCall] = []  # モデルの返信としてのツール呼び出し結果（`tools`を渡した場合のみ、モデルがツール呼び出しが必要と判断した場合に返されます）
```

`tool_calls` は、モデルに `tools` を渡した後、モデルが返す `tool call` のリストです。

### SystemPromptMessage

システムメッセージを表し、通常はモデルに与えられるシステム命令に使用されます。

```python
class SystemPromptMessage(PromptMessage):
    """
    Model class for system prompt message.
    """
    role: PromptMessageRole = PromptMessageRole.SYSTEM
```

### ToolPromptMessage

ツールメッセージを表し、ツールの実行結果をモデルに渡して次のステップの計画を行います。

```python
class ToolPromptMessage(PromptMessage):
    """
    Model class for tool prompt message.
    """
    role: PromptMessageRole = PromptMessageRole.TOOL
    tool_call_id: str  # ツール呼び出しID。OpenAI tool callをサポートしない場合、ツール名を渡すこともできます。
```

基类的 `content` 传入工具执行结果。

### PromptMessageTool

```python
class PromptMessageTool(BaseModel):
    """
    Model class for prompt message tool.
    """
    name: str  # ツール名
    description: str  # ツールの説明
    parameters: dict  # ツールパラメータ dict
```

---

### LLMResult

```python
class LLMResult(BaseModel):
    """
    Model class for llm result.
    """
    model: str  # 使用された実際のモデル
    prompt_messages: list[PromptMessage]  # プロンプトメッセージのリスト
    message: AssistantPromptMessage  # 返信メッセージ
    usage: LLMUsage  # 使用したtokenとコスト情報
    system_fingerprint: Optional[str] = None  # リクエスト指紋。OpenAIのこのパラメータの定義を参照。
```

### LLMResultChunkDelta

ストリーム化された各イテレーション内の `delta` エンティティ。

```python
class LLMResultChunkDelta(BaseModel):
    """
    Model class for llm result chunk delta.
    """
    index: int  # インデックス
    message: AssistantPromptMessage  # 返信メッセージ
    usage: Optional[LLMUsage] = None  # 使用したトークンとコスト情報（最後の1つのみ）
    finish_reason: Optional[str] = None  # 終了理由（最後の1つのみ）
```

### LLMResultChunk

ストリーム化された各イテレーションのエンティティ。

```python
class LLMResultChunk(BaseModel):
    """
    Model class for llm result chunk.
    """
    model: str  # 実際に使用したモデル
    prompt_messages: list[PromptMessage]  # プロンプトメッセージのリスト
    system_fingerprint: Optional[str] = None  # リクエスト指紋。OpenAIのこのパラメータの定義を参照。
    delta: LLMResultChunkDelta  # 各イテレーションの変更が存在する内容
```

### LLMUsage

```python
class LLMUsage(ModelUsage):
    """
    Model class for llm usage.
    """
    prompt_tokens: int  # プロンプトで使用したトークン数
    prompt_unit_price: Decimal  # プロンプトの単価
    prompt_price_unit: Decimal  # プロンプト料金の単位（単価が基づいているトークンの量）
    prompt_price: Decimal  # プロンプトの料金
    completion_tokens: int  # 返答で使用したトークン数
    completion_unit_price: Decimal  # 返答の単価
    completion_price_unit: Decimal  # 返答料金の単位（単価が基づいているトークンの量）
    completion_price: Decimal  # 返答の料金
    total_tokens: int  # 総使用トークン数
    total_price: Decimal  # 総料金
    currency: str  # 通貨単位
    latency: float  # リクエスト処理時間（秒）
```

---

### TextEmbeddingResult

```python
class TextEmbeddingResult(BaseModel):
    """
    Model class for text embedding result.
    """
    model: str  # 実際に使用したモデル
    embeddings: list[list[float]]  # テキストリストに対応するembeddingベクトルのリスト
    usage: EmbeddingUsage  # 使用した情報
```

### EmbeddingUsage

```python
class EmbeddingUsage(ModelUsage):
    """
    Model class for embedding usage.
    """
    tokens: int  # 使用した token 数
    total_tokens: int  # 総使用 token 数
    unit_price: Decimal  # 単価
    price_unit: Decimal  # 価格の単位（単価が基づいているトークンの量）
    total_price: Decimal  # 総料金
    currency: str  # 通貨単位
    latency: float  # リクエスト処理時間(s)
```

---

### RerankResult

```python
class RerankResult(BaseModel):
    """
    Model class for rerank result.
    """
    model: str  # 実際に使用したモデル
    docs: list[RerankDocument]  # Rerankされたセグメントリスト
```

### RerankDocument

```python
class RerankDocument(BaseModel):
    """
    Model class for rerank document.
    """
    index: int  # 元の文書の順番
    text: str  # 文書のテキスト内容
    score: float  # スコア
```
 interfaces:

```python
def validate_provider_credentials(self, credentials: dict) -> None:
    """
    Validate provider credentials
    You can choose any validate_credentials method of model type or implement validate method by yourself,
    such as: get model list api

    if validate failed, raise exception

    :param credentials: provider credentials, credentials form defined in `provider_credential_schema`.
    """
```

- `credentials` (object) Credential information

  The parameters of credential information are defined by the `provider_credential_schema` in the provider's YAML configuration file. Inputs such as `api_key` are included.

If verification fails, throw the `errors.validate.CredentialsValidateFailedError` error.

## Model

Models are divided into 5 different types, each inheriting from different base classes and requiring the implementation of different methods.

All models need to uniformly implement the following 2 methods:

- Model Credential Verification

  Similar to provider credential verification, this step involves verification for an individual model.


  ```python
  def validate_credentials(self, model: str, credentials: dict) -> None:
      """
      Validate model credentials
  
      :param model: model name
      :param credentials: model credentials
      :return:
      """
  ```

  Parameters:

  - `model` (string) Model name

  - `credentials` (object) Credential information

    The parameters of credential information are defined by either the `provider_credential_schema` or `model_credential_schema` in the provider's YAML configuration file. Inputs such as `api_key` are included.

  If verification fails, throw the `errors.validate.CredentialsValidateFailedError` error.

- Invocation Error Mapping Table

  When there is an exception in model invocation, it needs to be mapped to the `InvokeError` type specified by Runtime. This facilitates Dify's ability to handle different errors with appropriate follow-up actions.

  Runtime Errors:

  - `InvokeConnectionError` Invocation connection error
  - `InvokeServerUnavailableError` Invocation service provider unavailable
  - `InvokeRateLimitError` Invocation reached rate limit
  - `InvokeAuthorizationError` Invocation authorization failure
  - `InvokeBadRequestError` Invocation parameter error

  ```python
  @property
  def _invoke_error_mapping(self) -> dict[type[InvokeError], list[type[Exception]]]:
      """
      Map model invoke error to unified error
      The key is the error type thrown to the caller
      The value is the error type thrown by the model,
      which needs to be converted into a unified error type for the caller.
  
      :return: Invoke error mapping
      """
  ```

​	You can refer to OpenAI's `_invoke_error_mapping` for an example.

### LLM

Inherit the `__base.large_language_model.LargeLanguageModel` base class and implement the following interfaces:

- LLM Invocation

  Implement the core method for LLM invocation, which can support both streaming and synchronous returns.


  ```python
  def _invoke(self, model: str, credentials: dict,
              prompt_messages: list[PromptMessage], model_parameters: dict,
              tools: Optional[list[PromptMessageTool]] = None, stop: Optional[List[str]] = None,
              stream: bool = True, user: Optional[str] = None) \
          -> Union[LLMResult, Generator]:
      """
      Invoke large language model
  
      :param model: model name
      :param credentials: model credentials
      :param prompt_messages: prompt messages
      :param model_parameters: model parameters
      :param tools: tools for tool calling
      :param stop: stop words
      :param stream: is stream response
      :param user: unique user id
      :return: full response or stream response chunk generator result
      """
  ```

  - Parameters:

    - `model` (string) Model name

    - `credentials` (object) Credential information

      The parameters of credential information are defined by either the `provider_credential_schema` or `model_credential_schema` in the provider's YAML configuration file. Inputs such as `api_key` are included.

    - `prompt_messages` (array[[PromptMessage](#PromptMessage)]) List of prompts

      If the model is of the `Completion` type, the list only needs to include one [UserPromptMessage](#UserPromptMessage) element;

      If the model is of the `Chat` type, it requires a list of elements such as [SystemPromptMessage](#SystemPromptMessage), [UserPromptMessage](#UserPromptMessage), [AssistantPromptMessage](#AssistantPromptMessage), [ToolPromptMessage](#ToolPromptMessage) depending on the message.

    - `model_parameters` (object) Model parameters

      The model parameters are defined by the `parameter_rules` in the model's YAML configuration.

    - `tools` (array[[PromptMessageTool](#PromptMessageTool)]) [optional] List of tools, equivalent to the `function` in `function calling`.

      That is, the tool list for tool calling.

    - `stop` (array[string]) [optional] Stop sequences

      The model output will stop before the string defined by the stop sequence.

    - `stream` (bool) Whether to output in a streaming manner, default is True

      Streaming output returns Generator[[LLMResultChunk](#LLMResultChunk)], non-streaming output returns [LLMResult](#LLMResult).

    - `user` (string) [optional] Unique identifier of the user

      This can help the provider monitor and detect abusive behavior.

  - Returns

    Streaming output returns Generator[[LLMResultChunk](#LLMResultChunk)], non-streaming output returns [LLMResult](#LLMResult).

- Pre-calculating Input Tokens

  If the model does not provide a pre-calculated tokens interface, you can directly return 0.

  ```python
  def get_num_tokens(self, model: str, credentials: dict, prompt_messages: list[PromptMessage],
                     tools: Optional[list[PromptMessageTool]] = None) -> int:
      """
      Get number of tokens for given prompt messages

      :param model: model name
      :param credentials: model credentials
      :param prompt_messages: prompt messages
      :param tools: tools for tool calling
      :return:
      """
  ```

  For parameter explanations, refer to the above section on `LLM Invocation`.

- Fetch Custom Model Schema [Optional]

  ```python
  def get_customizable_model_schema(self, model: str, credentials: dict) -> Optional[AIModelEntity]:
      """
      Get customizable model schema

      :param model: model name
      :param credentials: model credentials
      :return: model schema
      """
  ```

  When the provider supports adding custom LLMs, this method can be implemented to allow custom models to fetch model schema. The default return null.


### TextEmbedding

Inherit the `__base.text_embedding_model.TextEmbeddingModel` base class and implement the following interfaces:

- Embedding Invocation

  ```python
  def _invoke(self, model: str, credentials: dict,
              texts: list[str], user: Optional[str] = None) \
          -> TextEmbeddingResult:
      """
      Invoke large language model
  
      :param model: model name
      :param credentials: model credentials
      :param texts: texts to embed
      :param user: unique user id
      :return: embeddings result
      """
  ```

  - Parameters:

    - `model` (string) Model name

    - `credentials` (object) Credential information

      The parameters of credential information are defined by either the `provider_credential_schema` or `model_credential_schema` in the provider's YAML configuration file. Inputs such as `api_key` are included.

    - `texts` (array[string]) List of texts, capable of batch processing

    - `user` (string) [optional] Unique identifier of the user

      This can help the provider monitor and detect abusive behavior.

  - Returns:

    [TextEmbeddingResult](#TextEmbeddingResult) entity.

- Pre-calculating Tokens

  ```python
  def get_num_tokens(self, model: str, credentials: dict, texts: list[str]) -> int:
      """
      Get number of tokens for given prompt messages

      :param model: model name
      :param credentials: model credentials
      :param texts: texts to embed
      :return:
      """
  ```

  For parameter explanations, refer to the above section on `Embedding Invocation`.

### Rerank

Inherit the `__base.rerank_model.RerankModel` base class and implement the following interfaces:

- Rerank Invocation

  ```python
  def _invoke(self, model: str, credentials: dict,
              query: str, docs: list[str], score_threshold: Optional[float] = None, top_n: Optional[int] = None,
              user: Optional[str] = None) \
          -> RerankResult:
      """
      Invoke rerank model
  
      :param model: model name
      :param credentials: model credentials
      :param query: search query
      :param docs: docs for reranking
      :param score_threshold: score threshold
      :param top_n: top n
      :param user: unique user id
      :return: rerank result
      """
  ```

  - Parameters:

    - `model` (string) Model name

    - `credentials` (object) Credential information

      The parameters of credential information are defined by either the `provider_credential_schema` or `model_credential_schema` in the provider's YAML configuration file. Inputs such as `api_key` are included.

    - `query` (string) Query request content

    - `docs` (array[string]) List of segments to be reranked

    - `score_threshold` (float) [optional] Score threshold

    - `top_n` (int) [optional] Select the top n segments

    - `user` (string) [optional] Unique identifier of the user

      This can help the provider monitor and detect abusive behavior.

  - Returns:

    [RerankResult](#RerankResult) entity.

### Speech2text

Inherit the `__base.speech2text_model.Speech2TextModel` base class and implement the following interfaces:

- Invoke Invocation

  ```python
  def _invoke(self, model: str, credentials: dict, file: IO[bytes], user: Optional[str] = None) -> str:
      """
      Invoke large language model
  
      :param model: model name
      :param credentials: model credentials
      :param file: audio file
      :param user: unique user id
      :return: text for given audio file
      """	
  ```

  - Parameters:

    - `model` (string) Model name

    - `credentials` (object) Credential information

      The parameters of credential information are defined by either the `provider_credential_schema` or `model_credential_schema` in the provider's YAML configuration file. Inputs such as `api_key` are included.

    - `file` (File) File stream

    - `user` (string) [optional] Unique identifier of the user

      This can help the provider monitor and detect abusive behavior.

  - Returns:

    The string after speech-to-text conversion.

### Text2speech

Inherit the `__base.text2speech_model.Text2SpeechModel` base class and implement the following interfaces:

- Invoke Invocation

  ```python
  def _invoke(self, model: str, credentials: dict, content_text: str, streaming: bool, user: Optional[str] = None):
      """
      Invoke large language model
  
      :param model: model name
      :param credentials: model credentials
      :param content_text: text content to be translated
      :param streaming: output is streaming
      :param user: unique user id
      :return: translated audio file
      """	
  ```

  - Parameters：

    - `model` (string) Model name

    - `credentials` (object) Credential information

      The parameters of credential information are defined by either the `provider_credential_schema` or `model_credential_schema` in the provider's YAML configuration file. Inputs such as `api_key` are included.

    - `content_text` (string) The text content that needs to be converted

    - `streaming` (bool) Whether to stream output

    - `user` (string) [optional] Unique identifier of the user

      This can help the provider monitor and detect abusive behavior.

  - Returns：

    Text converted speech stream。

### Moderation

Inherit the `__base.moderation_model.ModerationModel` base class and implement the following interfaces:

- Invoke Invocation

  ```python
  def _invoke(self, model: str, credentials: dict,
              text: str, user: Optional[str] = None) \
          -> bool:
      """
      Invoke large language model
  
      :param model: model name
      :param credentials: model credentials
      :param text: text to moderate
      :param user: unique user id
      :return: false if text is safe, true otherwise
      """
  ```

  - Parameters:

    - `model` (string) Model name

    - `credentials` (object) Credential information

      The parameters of credential information are defined by either the `provider_credential_schema` or `model_credential_schema` in the provider's YAML configuration file. Inputs such as `api_key` are included.

    - `text` (string) Text content

    - `user` (string) [optional] Unique identifier of the user

      This can help the provider monitor and detect abusive behavior.

  - Returns:

    False indicates that the input text is safe, True indicates otherwise.



## Entities

### PromptMessageRole 

Message role

```python
class PromptMessageRole(Enum):
    """
    Enum class for prompt message.
    """
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"
```

### PromptMessageContentType

Message content types, divided into text and image.

```python
class PromptMessageContentType(Enum):
    """
    Enum class for prompt message content type.
    """
    TEXT = 'text'
    IMAGE = 'image'
```

### PromptMessageContent

Message content base class, used only for parameter declaration and cannot be initialized.

```python
class PromptMessageContent(BaseModel):
    """
    Model class for prompt message content.
    """
    type: PromptMessageContentType
    data: str
```

Currently, two types are supported: text and image. It's possible to simultaneously input text and multiple images.

You need to initialize `TextPromptMessageContent` and `ImagePromptMessageContent` separately for input.

### TextPromptMessageContent

```python
class TextPromptMessageContent(PromptMessageContent):
    """
    Model class for text prompt message content.
    """
    type: PromptMessageContentType = PromptMessageContentType.TEXT
```

If inputting a combination of text and images, the text needs to be constructed into this entity as part of the `content` list.

### ImagePromptMessageContent

```python
class ImagePromptMessageContent(PromptMessageContent):
    """
    Model class for image prompt message content.
    """
    class DETAIL(Enum):
        LOW = 'low'
        HIGH = 'high'

    type: PromptMessageContentType = PromptMessageContentType.IMAGE
    detail: DETAIL = DETAIL.LOW  # Resolution
```

If inputting a combination of text and images, the images need to be constructed into this entity as part of the `content` list.

`data` can be either a `url` or a `base64` encoded string of the image.

### PromptMessage

The base class for all Role message bodies, used only for parameter declaration and cannot be initialized.

```python
class PromptMessage(ABC, BaseModel):
    """
    Model class for prompt message.
    """
    role: PromptMessageRole
    content: Optional[str | list[PromptMessageContent]] = None  # Supports two types: string and content list. The content list is designed to meet the needs of multimodal inputs. For more details, see the PromptMessageContent explanation.
    name: Optional[str] = None
```

### UserPromptMessage

UserMessage message body, representing a user's message.

```python
class UserPromptMessage(PromptMessage):
    """
    Model class for user prompt message.
    """
    role: PromptMessageRole = PromptMessageRole.USER
```

### AssistantPromptMessage

Represents a message returned by the model, typically used for `few-shots` or inputting chat history.

```python
class AssistantPromptMessage(PromptMessage):
    """
    Model class for assistant prompt message.
    """
    class ToolCall(BaseModel):
        """
        Model class for assistant prompt message tool call.
        """
        class ToolCallFunction(BaseModel):
            """
            Model class for assistant prompt message tool call function.
            """
            name: str  # tool name
            arguments: str  # tool arguments

        id: str  # Tool ID, effective only in OpenAI tool calls. It's the unique ID for tool invocation and the same tool can be called multiple times.
        type: str  # default: function
        function: ToolCallFunction  # tool call information

    role: PromptMessageRole = PromptMessageRole.ASSISTANT
    tool_calls: list[ToolCall] = []  # The result of tool invocation in response from the model (returned only when tools are input and the model deems it necessary to invoke a tool).
```

Where `tool_calls` are the list of `tool calls` returned by the model after invoking the model with the `tools` input.

### SystemPromptMessage

Represents system messages, usually used for setting system commands given to the model.

```python
class SystemPromptMessage(PromptMessage):
    """
    Model class for system prompt message.
    """
    role: PromptMessageRole = PromptMessageRole.SYSTEM
```

### ToolPromptMessage

Represents tool messages, used for conveying the results of a tool execution to the model for the next step of processing.

```python
class ToolPromptMessage(PromptMessage):
    """
    Model class for tool prompt message.
    """
    role: PromptMessageRole = PromptMessageRole.TOOL
    tool_call_id: str  # Tool invocation ID. If OpenAI tool call is not supported, the name of the tool can also be inputted.
```

The base class's `content` takes in the results of tool execution.

### PromptMessageTool

```python
class PromptMessageTool(BaseModel):
    """
    Model class for prompt message tool.
    """
    name: str
    description: str
    parameters: dict
```

---

### LLMResult

```python
class LLMResult(BaseModel):
    """
    Model class for llm result.
    """
    model: str  # Actual used modele
    prompt_messages: list[PromptMessage]  # prompt messages
    message: AssistantPromptMessage  # response message
    usage: LLMUsage  # usage info
    system_fingerprint: Optional[str] = None  # request fingerprint, refer to OpenAI definition
```

### LLMResultChunkDelta

In streaming returns, each iteration contains the `delta` entity.

```python
class LLMResultChunkDelta(BaseModel):
    """
    Model class for llm result chunk delta.
    """
    index: int
    message: AssistantPromptMessage  # response message
    usage: Optional[LLMUsage] = None  # usage info
    finish_reason: Optional[str] = None  # finish reason, only the last one returns
```

### LLMResultChunk

Each iteration entity in streaming returns.

```python
class LLMResultChunk(BaseModel):
    """
    Model class for llm result chunk.
    """
    model: str  # Actual used modele
    prompt_messages: list[PromptMessage]  # prompt messages
    system_fingerprint: Optional[str] = None  # request fingerprint, refer to OpenAI definition
    delta: LLMResultChunkDelta
```

### LLMUsage

```python
class LLMUsage(ModelUsage):
    """
    Model class for LLM usage.
    """
    prompt_tokens: int  # Tokens used for prompt
    prompt_unit_price: Decimal  # Unit price for prompt
    prompt_price_unit: Decimal  # Price unit for prompt, i.e., the unit price based on how many tokens
    prompt_price: Decimal  # Cost for prompt
    completion_tokens: int  # Tokens used for response
    completion_unit_price: Decimal  # Unit price for response
    completion_price_unit: Decimal  # Price unit for response, i.e., the unit price based on how many tokens
    completion_price: Decimal  # Cost for response
    total_tokens: int  # Total number of tokens used
    total_price: Decimal  # Total cost
    currency: str  # Currency unit
    latency: float  # Request latency (s)
```

---

### TextEmbeddingResult

```python
class TextEmbeddingResult(BaseModel):
    """
    Model class for text embedding result.
    """
    model: str  # Actual model used
    embeddings: list[list[float]]  # List of embedding vectors, corresponding to the input texts list
    usage: EmbeddingUsage  # Usage information
```

### EmbeddingUsage

```python
class EmbeddingUsage(ModelUsage):
    """
    Model class for embedding usage.
    """
    tokens: int  # Number of tokens used
    total_tokens: int  # Total number of tokens used
    unit_price: Decimal  # Unit price
    price_unit: Decimal  # Price unit, i.e., the unit price based on how many tokens
    total_price: Decimal  # Total cost
    currency: str  # Currency unit
    latency: float  # Request latency (s)
```

---

### RerankResult

```python
class RerankResult(BaseModel):
    """
    Model class for rerank result.
    """
    model: str  # Actual model used
    docs: list[RerankDocument]  # Reranked document list	
```

### RerankDocument

```python
class RerankDocument(BaseModel):
    """
    Model class for rerank document.
    """
    index: int  # original index
    text: str
    score: float
```
