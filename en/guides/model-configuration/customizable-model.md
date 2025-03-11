# Custom Model Integration

### Introduction

After completing vendor integration, the next step is to integrate models under the vendor. To help understand the entire integration process, we will use `Xinference` as an example to gradually complete a full vendor integration.

It is important to note that for custom models, each model integration requires a complete vendor credential.

Unlike predefined models, custom vendor integration will always have the following two parameters, which do not need to be defined in the vendor YAML file.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/model-configuration/30f5d554e9f42670c32b6d877dccdff2.png)

In the previous section, we have learned that vendors do not need to implement `validate_provider_credential`. The Runtime will automatically call the corresponding model layer's `validate_credentials` based on the model type and model name selected by the user for validation.

#### Writing Vendor YAML

First, we need to determine what types of models the vendor supports.

Currently supported model types are as follows:

* `llm` Text Generation Model
* `text_embedding` Text Embedding Model
* `rerank` Rerank Model
* `speech2text` Speech to Text
* `tts` Text to Speech
* `moderation` Moderation

`Xinference` supports `LLM`, `Text Embedding`, and `Rerank`, so we will start writing `xinference.yaml`.

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

Next, we need to consider what credentials are required to define a model in Xinference.

* It supports three different types of models, so we need `model_type` to specify the type of the model. It has three types, so we write it as follows:

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
        zh_Hans: 语言模型
    - value: embeddings
      label:
        en_US: Text Embedding
    - value: reranking
      label:
        en_US: Rerank
```

* Each model has its own name `model_name`, so we need to define it here.

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

* Provide the address for the local deployment of Xinference.

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

* Each model has a unique `model_uid`, so we need to define it here.

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

Now, we have completed the basic definition of the vendor.

#### Writing Model Code

Next, we will take the `llm` type as an example and write `xinference.llm.llm.py`.

In `llm.py`, create a Xinference LLM class, which we will name `XinferenceAILargeLanguageModel` (arbitrary name), inheriting from the `__base.large_language_model.LargeLanguageModel` base class. Implement the following methods:

*   LLM Invocation

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

    When implementing, note that you need to use two functions to return data, one for handling synchronous returns and one for streaming returns. This is because Python identifies functions containing the `yield` keyword as generator functions, and the return data type is fixed as `Generator`. Therefore, synchronous and streaming returns need to be implemented separately, as shown below (note that the example uses simplified parameters; the actual implementation should follow the parameter list above):

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
*   Precompute Input Tokens

    If the model does not provide a precompute tokens interface, it can directly return 0.

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

    Sometimes, you may not want to directly return 0, so you can use `self._get_num_tokens_by_gpt2(text: str)` to get precomputed tokens. This method is located in the `AIModel` base class and uses GPT2's Tokenizer for calculation. However, it can only be used as an alternative method and is not completely accurate.
*   Model Credential Validation

    Similar to vendor credential validation, this is for validating individual model credentials.

    ```python
    def validate_credentials(self, model: str, credentials: dict) -> None:
        """
        Validate model credentials

        :param model: model name
        :param credentials: model credentials
        :return:
        """
    ```
*   Model Parameter Schema

    Unlike custom types, since a model's supported parameters are not defined in the YAML file, we need to dynamically generate the model parameter schema.

    For example, Xinference supports the `max_tokens`, `temperature`, and `top_p` parameters.

    However, some vendors support different parameters depending on the model. For instance, the vendor `OpenLLM` supports `top_k`, but not all models provided by this vendor support `top_k`. Here, we illustrate that Model A supports `top_k`, while Model B does not. Therefore, we need to dynamically generate the model parameter schema, as shown below:

    ```python
    def get_customizable_model_schema(self, model: str, credentials: dict) -> AIModelEntity | None:
        """
            Used to define customizable model schema
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
*   Invocation Error Mapping Table

    When a model invocation error occurs, it needs to be mapped to the Runtime-specified `InvokeError` type to facilitate Dify's different subsequent processing for different errors.

    Runtime Errors:

    * `InvokeConnectionError` Invocation connection error
    * `InvokeServerUnavailableError` Invocation server unavailable
    * `InvokeRateLimitError` Invocation rate limit reached
    * `InvokeAuthorizationError` Invocation authorization failed
    * `InvokeBadRequestError` Invocation parameter error

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

For an explanation of interface methods, see: [Interfaces](https://github.com/langgenius/dify/blob/main/api/core/model\_runtime/docs/en\_US/interfaces.md). For specific implementations, refer to: [llm.py](https://github.com/langgenius/dify-runtime/blob/main/lib/model\_providers/anthropic/llm/llm.py).
