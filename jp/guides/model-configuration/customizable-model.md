# カスタムモデルの追加

### イントロダクション

ベンダー統合が完了した後、次にベンダーの下でモデルのインテグレーションを行います。ここでは、全体のプロセスを理解するために、例として`Xinference`を使用して、段階的にベンダーのインテグレーションを完了します。

注意が必要なのは、カスタムモデルの場合、各モデルのインテグレーションには完全なベンダークレデンシャルの記入が必要です。

事前定義モデルとは異なり、カスタムベンダーのインテグレーション時には常に以下の2つのパラメータが存在し、ベンダー yaml に定義する必要はありません。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/model-configuration/244cf2b0a126ed360f9588fbf1050e03.png)

前述したように、ベンダーは`validate_provider_credential`を実装する必要はなく、Runtimeがユーザーが選択したモデルタイプとモデル名に基づいて、対応するモデル層の`validate_credentials`を呼び出して検証を行います。

#### ベンダー yaml の作成

まず、インテグレーションを行うベンダーがどのタイプのモデルをサポートしているかを確認します。

現在サポートされているモデルタイプは以下の通りです：

* `llm` テキスト生成モデル
* `text_embedding` テキスト Embedding モデル
* `rerank` Rerank モデル
* `speech2text` 音声からテキスト変換
* `tts` テキストから音声変換
* `moderation` モデレーション

`Xinference`は`LLM`、`Text Embedding`、`Rerank`をサポートしているため、`xinference.yaml`を作成します。

```yaml
provider: xinference # Specify vendor identifier
label: # Vendor display name, can be set in en_US (English) and zh_Hans (Simplified Chinese). If zh_Hans is not set, en_US will be used by default.
  en_US: Xorbits Inference
icon_small: # Small icon, refer to other vendors' icons, stored in the _assets directory under the corresponding vendor implementation directory. Language strategy is the same as label.
  en_US: icon_s_en.svg
icon_large: # Large icon
  en_US: icon_l_en.svg
help: # Help
  title:
    en_US: How to deploy Xinference
    zh_Hans: 如何部署 Xinference
  url:
    en_US: https://github.com/xorbitsai/inference
supported_model_types: # Supported model types. Xinference supports LLM/Text Embedding/Rerank
- llm
- text-embedding
- rerank
configurate_methods: # Since Xinference is a locally deployed vendor and does not have predefined models, you need to deploy the required models according to Xinference's documentation. Therefore, only custom models are supported here.
- customizable-model
provider_credential_schema:
  credential_form_schemas:
```

その後、Xinferenceでモデルを定義するために必要なクレデンシャルを考えます。

* 3つの異なるモデルをサポートするため、`model_type`を使用してこのモデルのタイプを指定する必要があります。3つのタイプがあるので、次のように記述します。

```yaml
provider_credential_schema:
  credential_form_schemas:
  - variable: model_type
    type: select
    label:
      en_US: Model type
      zh_Hans: 模型类型
    required: true
    options:
    - value: text-generation
      label:
        en_US: Language Model
        zh_Hans: 言語モデル
    - value: embeddings
      label:
        en_US: Text Embedding
    - value: reranking
      label:
        en_US: Rerank
```

* 各モデルには独自の名称`model_name`があるため、ここで定義する必要があります。

```yaml
  - variable: model_name
    type: text-input
    label:
      en_US: Model name
      zh_Hans: 模型名称
    required: true
    placeholder:
      zh_Hans: 填写模型名称
      en_US: Input model name
```

* Xinferenceのローカルデプロイのアドレスを記入します。

```yaml
  - variable: server_url
    label:
      zh_Hans: 服务器URL
      en_US: Server url
    type: text-input
    required: true
    placeholder:
      zh_Hans: 在此输入Xinference的服务器地址，如 https://example.com/xxx
      en_US: Enter the url of your Xinference, for example https://example.com/xxx
```

* 各モデルには一意の model\_uid があるため、ここで定義する必要があります。

```yaml
  - variable: model_uid
    label:
      zh_Hans: 模型 UID
      en_US: Model uid
    type: text-input
    required: true
    placeholder:
      zh_Hans: 在此输入你的 Model UID
      en_US: Enter the model uid
```

これで、ベンダーの基本定義が完了しました。

#### モデルコードの作成

次に、`llm`タイプを例にとって、`xinference.llm.llm.py`を作成します。

`llm.py`内で、Xinference LLM クラスを作成し、`XinferenceAILargeLanguageModel`（任意の名前）と名付けて、`__base.large_language_model.LargeLanguageModel`基底クラスを継承し、以下のメソッドを実装します：

*   LLM 呼び出し

    LLM 呼び出しのコアメソッドを実装し、ストリームレスポンスと同期レスポンスの両方をサポートします。

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

    実装時には、同期レスポンスとストリームレスポンスを処理するために2つの関数を使用してデータを返す必要があります。Pythonは`yield`キーワードを含む関数をジェネレータ関数として認識し、返されるデータ型は固定でジェネレーターになります。そのため、同期レスポンスとストリームレスポンスは別々に実装する必要があります。以下のように実装します（例では簡略化されたパラメータを使用していますが、実際の実装では上記のパラメータリストに従って実装してください）：

    ```python
    def _invoke(self, stream: bool, **kwargs) \
            -> Union[LLMResult, Generator]:
        if stream:
              return self._handle_stream_response(**kwargs)
        return self._handle_sync_response(**kwargs)

    def _handle_stream_response(self, **kwargs) -> Generator:
        for chunk in response:
              yield chunk
    def _handle_sync_response(self, **kwargs) -> LLMResult:
        return LLMResult(**response)
    ```
*   予測トークン数の計算

    モデルが予測トークン数の計算インターフェースを提供していない場合、直接0を返すことができます。

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

    時には、直接0を返す必要がない場合もあります。その場合は`self._get_num_tokens_by_gpt2(text: str)`を使用して予測トークン数を取得することができます。このメソッドは`AIModel`基底クラスにあり、GPT2のTokenizerを使用して計算を行いますが、代替方法として使用されるものであり、完全に正確ではありません。
*   モデルクレデンシャル検証

    ベンダークレデンシャル検証と同様に、ここでは個々のモデルについて検証を行います。

    ```python
    def validate_credentials(self, model: str, credentials: dict) -> None:
        """
        Validate model credentials

        :param model: model name
        :param credentials: model credentials
        :return:
        """
    ```
*   モデルパラメータスキーマ

    カスタムタイプとは異なり、yamlファイルでモデルがサポートするパラメータを定義していないため、動的にモデルパラメータのスキーマを生成する必要があります。

    例えば、Xinferenceは`max_tokens`、`temperature`、`top_p`の3つのモデルパラメータをサポートしています。

    しかし、ベンダーによっては異なるモデルに対して異なるパラメータをサポートしている場合があります。例えば、ベンダー`OpenLLM`は`top_k`をサポートしていますが、全てのモデルが`top_k`をサポートしているわけではありません。ここでは、例としてAモデルが`top_k`をサポートし、Bモデルが`top_k`をサポートしていない場合、以下のように動的にモデルパラメータのスキーマを生成します：

    ```python
    def get_customizable_model_schema(self, model: str, credentials: dict) -> AIModelEntity | None:
        """
            used to define customizable model schema
        """
        rules = [
            ParameterRule(
                name='temperature', type=ParameterType.FLOAT,
                use_template='temperature',
                label=I18nObject(
                    zh_Hans='温度', en_US='Temperature'
                )
            ),
            ParameterRule(
                name='top_p', type=ParameterType.FLOAT,
                use_template='top_p',
                label=I18nObject(
                    zh_Hans='Top P', en_US='Top P'
                )
            ),
            ParameterRule(
                name='max_tokens', type=ParameterType.INT,
                use_template='max_tokens',
                min=1,
                default=512,
                label=I18nObject(
                    zh_Hans='最大生成长度', en_US='Max Tokens'
                )
            )
        ]

        # if model is A, add top_k to rules
        if model == 'A':
            rules.append(
                ParameterRule(
                    name='top_k', type=ParameterType.INT,
                    use_template='top_k',
                    min=1,
                    default=50,
                    label=I18nObject(
                        zh_Hans='Top K', en_US='Top K'
                    )
                )
            )

        """
            some NOT IMPORTANT code here
        """

        entity = AIModelEntity(
            model=model,
            label=I18nObject(
                en_US=model
            ),
            fetch_from=FetchFrom.CUSTOMIZABLE_MODEL,
            model_type=model_type,
            model_properties={ 
                ModelPropertyKey.MODE:  ModelType.LLM,
            },
            parameter_rules=rules
        )

        return entity
    ```
*   呼び出しエラーマッピングテーブル

    モデル呼び出し時にエラーが発生した場合、Runtimeが指定する`InvokeError`タイプにマッピングする必要があります。これにより、Difyは異なるエラーに対して異なる後続処理を行うことができます。

    Runtime Errors：

    * `InvokeConnectionError` 呼び出し接続エラー
    * `InvokeServerUnavailableError` 呼び出しサービスが利用不可
    * `InvokeRateLimitError` 呼び出し回数制限に達した
    * `InvokeAuthorizationError` 認証エラー
    * `InvokeBadRequestError` 不正なリクエストパラメータ

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

インターフェース方法の詳細については：[インターフェース](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/docs/en_US/interfaces.md)をご覧ください。具体的な実装例については、[llm.py](https://github.com/langgenius/dify-runtime/blob/main/lib/model_providers/anthropic/llm/llm.py)を参照してください。
```
