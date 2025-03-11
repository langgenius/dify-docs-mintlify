# Predefined Model Integration

After completing the supplier integration, the next step is to integrate the models under the supplier.

First, we need to determine the type of model to be integrated and create the corresponding model type `module` in the directory of the respective supplier.

The currently supported model types are as follows:

* `llm` Text Generation Model
* `text_embedding` Text Embedding Model
* `rerank` Rerank Model
* `speech2text` Speech to Text
* `tts` Text to Speech
* `moderation` Moderation

Taking `Anthropic` as an example, `Anthropic` only supports LLM, so we create a `module` named `llm` in `model_providers.anthropic`.

For predefined models, we first need to create a YAML file named after the model under the `llm` `module`, such as: `claude-2.1.yaml`.

#### Preparing the Model YAML

```yaml
model: claude-2.1  # Model identifier
# Model display name, can be set in en_US English and zh_Hans Chinese. If zh_Hans is not set, it will default to en_US.
# You can also not set a label, in which case the model identifier will be used.
label:
  en_US: claude-2.1
model_type: llm  # Model type, claude-2.1 is an LLM
features:  # Supported features, agent-thought supports Agent reasoning, vision supports image understanding
- agent-thought
model_properties:  # Model properties
  mode: chat  # LLM mode, complete for text completion model, chat for dialogue model
  context_size: 200000  # Maximum context size supported
parameter_rules:  # Model invocation parameter rules, only LLM needs to provide
- name: temperature  # Invocation parameter variable name
  # There are 5 preset variable content configuration templates: temperature/top_p/max_tokens/presence_penalty/frequency_penalty
  # You can set the template variable name directly in use_template, and it will use the default configuration in entities.defaults.PARAMETER_RULE_TEMPLATE
  # If additional configuration parameters are set, they will override the default configuration
  use_template: temperature
- name: top_p
  use_template: top_p
- name: top_k
  label:  # Invocation parameter display name
    zh_Hans: 取样数量
    en_US: Top k
  type: int  # Parameter type, supports float/int/string/boolean
  help:  # Help information, describes the parameter's function
    zh_Hans: 仅从每个后续标记的前 K 个选项中采样。
    en_US: Only sample from the top K options for each subsequent token.
  required: false  # Whether it is required, can be omitted
- name: max_tokens_to_sample
  use_template: max_tokens
  default: 4096  # Default parameter value
  min: 1  # Minimum parameter value, only applicable to float/int
  max: 4096  # Maximum parameter value, only applicable to float/int
pricing:  # Pricing information
  input: '8.00'  # Input unit price, i.e., Prompt unit price
  output: '24.00'  # Output unit price, i.e., return content unit price
  unit: '0.000001'  # Price unit, the above price is per 100K
  currency: USD  # Price currency
```

It is recommended to prepare all model configurations before starting the implementation of the model code.

Similarly, you can refer to the YAML configuration information in the directories of other suppliers under the `model_providers` directory. The complete YAML rules can be found in: Schema[^1].

#### Implementing Model Invocation Code

Next, create a Python file with the same name `llm.py` under the `llm` `module` to write the implementation code.

Create an Anthropic LLM class in `llm.py`, which we will name `AnthropicLargeLanguageModel` (name can be arbitrary), inheriting from the `__base.large_language_model.LargeLanguageModel` base class, and implement the following methods:

*   LLM Invocation

    Implement the core method for LLM invocation, supporting both streaming and synchronous responses.

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

    When implementing, note to use two functions to return data, one for handling synchronous responses and one for streaming responses. Since Python recognizes functions containing the `yield` keyword as generator functions, returning a fixed data type of `Generator`, synchronous and streaming responses need to be implemented separately, like this (note the example below uses simplified parameters, actual implementation should follow the parameter list above):

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

    If the model does not provide a precompute tokens interface, return 0 directly.

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
*   Model Credentials Validation

    Similar to supplier credentials validation, this validates the credentials for a single model.

    ```python
    def validate_credentials(self, model: str, credentials: dict) -> None:
        """
        Validate model credentials

        :param model: model name
        :param credentials: model credentials
        :return:
        """
    ```
*   Invocation Error Mapping Table

    When a model invocation error occurs, it needs to be mapped to the `InvokeError` type specified by Runtime, facilitating Dify to handle different errors differently.

    Runtime Errors:

    * `InvokeConnectionError` Invocation connection error
    * `InvokeServerUnavailableError` Invocation service unavailable
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

For interface method descriptions, see: [Interfaces](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/docs/en_US/interfaces.md), and for specific implementation, refer to: [llm.py](https://github.com/langgenius/dify-runtime/blob/main/lib/model_providers/anthropic/llm/llm.py).

[^1]: #### Provider

    * `provider` (string) Supplier identifier, e.g., `openai`
    * `label` (object) Supplier display name, i18n, can be set in `en_US` English and `zh_Hans` Chinese
      * `zh_Hans` (string) [optional] Chinese label name, if `zh_Hans` is not set, it will default to `en_US`.
      * `en_US` (string) English label name
    * `description` (object) [optional] Supplier description, i18n
      * `zh_Hans` (string) [optional] Chinese description
      * `en_US` (string) English description
    * `icon_small` (string) [optional] Supplier small icon, stored in the `_assets` directory under the respective supplier implementation directory, follows the same language strategy as `label`
      * `zh_Hans` (string) [optional] Chinese icon
      * `en_US` (string) English icon
    * `icon_large` (string) [optional] Supplier large icon, stored in the `_assets` directory under the respective supplier implementation directory, follows the same language strategy as `label`
      * `zh_Hans` (string) [optional] Chinese icon
      * `en_US` (string) English icon
    * `background` (string) [optional] Background color value, e.g., #FFFFFF, if empty, the default color value will be displayed on the front end.
    * `help` (object) [optional] Help information
      * `title` (object) Help title, i18n
        * `zh_Hans` (string) [optional] Chinese title
        * `en_US` (string) English title
      * `url` (object) Help link, i18n
        * `zh_Hans` (string) [optional] Chinese link
        * `en_US` (string) English link
    * `supported_model_types` (array[ModelType]) Supported model types
    * `configurate_methods` (array[ConfigurateMethod]) Configuration methods
    * `provider_credential_schema` (ProviderCredentialSchema) Supplier credential schema
    * `model_credential_schema` (ModelCredentialSchema) Model credential schema