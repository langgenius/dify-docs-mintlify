# Model Schema

The endpoint methods and parameter descriptions that need to be implemented by the supplier and each model type are described here.

### Model Providers

Inherit from the `__base.model_provider.ModelProvider` base class, implement the following endpoint:

#### Provider Credentials Validation

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

Credentials (object): Credential information Credential parameters are defined by the provider's YAML configuration file's `provider_credential_schema`, such as passing in `api_key`. If validation fails, throw the `errors.validate.CredentialsValidateFailedError` error.

Note: Predefined models must fully implement this interface, while custom model providers can implement it simply as follows:

```python
class XinferenceProvider(Provider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        pass
```

### Models

Models are divided into 5 different model types, each inheriting from different base classes and requiring implementation of different methods.

#### Common Interfaces

All models must uniformly implement the following 2 methods:

**Model Credential Validation**

Similar to provider credential validation, this is specifically for validating individual models.

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

* `model` (string): Model name
* `credentials` (object): Credential information Credential parameters are defined by the provider's YAML configuration file's `provider_credential_schema` or `model_credential_schema`, such as passing in `api_key`. If validation fails, throw the `errors.validate.CredentialsValidateFailedError` error.

**Invocation Exception Error Mapping**

When a model invocation encounters an exception, it needs to be mapped to the Runtime-specified InvokeError type to help Dify handle different errors accordingly.

Runtime Errors:

* `InvokeConnectionError`: Invocation connection error
* `InvokeServerUnavailableError`: Invocation service unavailable
* `InvokeRateLimitError`: Invocation rate limit reached
* `InvokeAuthorizationError`: Invocation authentication failed
* `InvokeBadRequestError`: Incorrect invocation parameters

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

You can also directly throw corresponding Errors and define them so that in subsequent calls, you can directly throw `InvokeConnectionError` and other exceptions.

### Large Language Model (LLM)

Inherit from `__base.large_language_model.LargeLanguageModel` base class, implement the following interfaces:

#### LLM Invocation

Implement the core method for LLM invocation, supporting both streaming and synchronous returns.

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

Parameters:

* `model` (string): Model name
* `credentials` (object): Credential information Credential parameters are defined by the provider's YAML configuration file's `provider_credential_schema` or `model_credential_schema`, such as passing in `api_key`
* `prompt_messages` (array\[PromptMessage]): Prompt list
  * For Completion-type models, only one UserPromptMessage element needs to be passed
  * For Chat-type models, a list of SystemPromptMessage, UserPromptMessage, AssistantPromptMessage, ToolPromptMessage elements needs to be passed according to message type
* `model_parameters` (object): Model parameters defined by the model's YAML configuration's `parameter_rules`
* `tools` (array\[PromptMessageTool]) \[optional]: Tool list, equivalent to function calling functions
* `stop` (array\[string]) \[optional]: Stop sequences. Model output will stop before the defined string
* `stream` (bool): Whether to stream output, default True. Streaming returns Generator\[LLMResultChunk], non-streaming returns LLMResult
* `user` (string) \[optional]: Unique user identifier to help providers monitor and detect abuse

Return:

* Streaming returns Generator\[LLMResultChunk]
* Non-streaming returns LLMResult

#### Pre-calculate Input Tokens

If the model does not provide a pre-calculate tokens interface, directly return 0.

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

#### Optional: Get Custom Model Rules

```python
def get_customizable_model_schema(self, model: str, credentials: dict) -> Optional[AIModelEntity]:
    """
    Get customizable model schema

    :param model: model name
    :param credentials: model credentials
    :return: model schema
    """
```

When the vendor supports adding custom LLMs, this method can be implemented to make the model rules available to the custom model, returning None by default.

For most of the fine-tuned models under OpenAI vendor, you can get their base model by their fine-tuned model name, such as gpt-3.5-turbo-1106, and then return the predefined parameter rules of the base model, refer to the implementation of [OpenAI](https://github.com/langgenius/dify-official-plugins/tree/main/models/openai).

### Text Embedding

Inherit from `__base.text_embedding_model.TextEmbeddingModel` base class, implement the following interfaces:

#### Embedding Invocation

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

Parameters:

* `model` (string): Model name
* `credentials` (object): Credential information Credential parameters are defined by the provider's YAML configuration file's `provider_credential_schema` or `model_credential_schema`
* `texts` (array\[string]): Text list, can be processed in batch
* `user` (string) \[optional]: Unique user identifier to help providers monitor and detect abuse

Return:

* TextEmbeddingResult entity

#### Pre-calculate Tokens

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

Similar to LargeLanguageModel, this interface needs to select an appropriate tokenizer based on the model. If the model does not provide a tokenizer, it can use the `_get_num_tokens_by_gpt2(text: str)` method in the AIModel base class.

### Rerank

Inherit from `__base.rerank_model.RerankModel` base class, implement the following interfaces:

#### Rerank Invocation

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

Parameters:

* `model` (string): Model name
* `credentials` (object): Credential information
* `query` (string): Search query content
* `docs` (array\[string]): List of segments to be re-ranked
* `score_threshold` (float) \[optional]: Score threshold
* `top_n` (int) \[optional]: Take top n segments
* `user` (string) \[optional]: Unique user identifier to help providers monitor and detect abuse

Return:

* RerankResult entity

### Speech2Text

Inherit from `__base.speech2text_model.Speech2TextModel` base class, implement the following interfaces:

#### Invoke Invocation

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

Parameters:

* `model` (string): Model name
* `credentials` (object): Credential information
* `file` (File): File stream
* `user` (string) \[optional]: Unique user identifier to help providers monitor and detect abuse

Return:

* Converted text string from speech

### Text2Speech

Inherit from `__base.text2speech_model.Text2SpeechModel` base class, implement the following interfaces:

#### Invoke Invocation

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

Parameters:

* `model` (string): Model name
* `credentials` (object): Credential information
* `content_text` (string): Text content to be converted
* `streaming` (bool): Whether to stream output
* `user` (string) \[optional]: Unique user identifier to help providers monitor and detect abuse

Return:

* Audio stream converted from text

### Moderation

Inherit from `__base.moderation_model.ModerationModel` base class, implement the following interfaces:

#### Invoke Invocation

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

Parameters:

* `model` (string): Model name
* `credentials` (object): Credential information
* `text` (string): Text content
* `user` (string) \[optional]: Unique user identifier to help providers monitor and detect abuse

Return:

* False indicates the input text is safe, True indicates otherwise
