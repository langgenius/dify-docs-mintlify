# Adding a New Provider

### Provider Configuration Methods

Providers support three configuration models:

**Predefined Model**

This indicates that users only need to configure unified provider credentials to use the predefined models under the provider.

**Customizable Model**

Users need to add credentials configuration for each model. For example, Xinference supports both LLM and Text Embedding, but each model has a unique **model_uid**. If you want to connect both, you need to configure a **model_uid** for each model.

**Fetch from Remote**

Similar to the `predefined-model` configuration method, users only need to configure unified provider credentials, and the models are fetched from the provider using the credential information.

For instance, with OpenAI, we can fine-tune multiple models based on gpt-turbo-3.5, all under the same **api_key**. When configured as `fetch-from-remote`, developers only need to configure a unified **api_key** to allow Dify Runtime to fetch all the developer's fine-tuned models and connect to Dify.

These three configuration methods **can coexist**, meaning a provider can support `predefined-model` + `customizable-model` or `predefined-model` + `fetch-from-remote`, etc. This allows using predefined models and models fetched from remote with unified provider credentials, and additional custom models can be used if added.

### Configuration Instructions

**Terminology**

* `module`: A `module` is a Python Package, or more colloquially, a folder containing an `__init__.py` file and other `.py` files.

**Steps**

Adding a new provider mainly involves several steps. Here is a brief outline to give you an overall understanding. Detailed steps will be introduced below.

* Create a provider YAML file and write it according to the [Provider Schema](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/docs/en_US/schema.md).
* Create provider code and implement a `class`.
* Create corresponding model type `modules` under the provider `module`, such as `llm` or `text_embedding`.
* Create same-named code files under the corresponding model `module`, such as `llm.py`, and implement a `class`.
* If there are predefined models, create same-named YAML files under the model `module`, such as `claude-2.1.yaml`, and write them according to the [AI Model Entity](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/docs/en_US/schema.md#aimodelentity).
* Write test code to ensure functionality is available.

#### Let's Get Started

To add a new provider, first determine the provider's English identifier, such as `anthropic`, and create a `module` named after it in `model_providers`.

Under this `module`, we need to prepare the provider's YAML configuration first.

**Preparing Provider YAML**

Taking `Anthropic` as an example, preset the basic information of the provider, supported model types, configuration methods, and credential rules.

```YAML
provider: anthropic  # Provider identifier
label:  # Provider display name, can be set in en_US English and zh_Hans Chinese. If zh_Hans is not set, en_US will be used by default.
  en_US: Anthropic
icon_small:  # Small icon of the provider, stored in the _assets directory under the corresponding provider implementation directory, same language strategy as label
  en_US: icon_s_en.png
icon_large:  # Large icon of the provider, stored in the _assets directory under the corresponding provider implementation directory, same language strategy as label
  en_US: icon_l_en.png
supported_model_types:  # Supported model types, Anthropic only supports LLM
- llm
configurate_methods:  # Supported configuration methods, Anthropic only supports predefined models
- predefined-model
provider_credential_schema:  # Provider credential rules, since Anthropic only supports predefined models, unified provider credential rules need to be defined
  credential_form_schemas:  # Credential form item list
  - variable: anthropic_api_key  # Credential parameter variable name
    label:  # Display name
      en_US: API Key
    type: secret-input  # Form type, secret-input here represents an encrypted information input box, only displaying masked information when editing.
    required: true  # Whether it is required
    placeholder:  # PlaceHolder information
      zh_Hans: 在此输入你的 API Key
      en_US: Enter your API Key
  - variable: anthropic_api_url
    label:
      en_US: API URL
    type: text-input  # Form type, text-input here represents a text input box
    required: false
    placeholder:
      zh_Hans: 在此输入你的 API URL
      en_US: Enter your API URL
```

If the connected provider offers customizable models, such as `OpenAI` which provides fine-tuned models, we need to add [`model_credential_schema`](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/docs/en_US/schema.md). Taking `OpenAI` as an example:

```yaml
model_credential_schema:
  model: # Fine-tuned model name
    label:
      en_US: Model Name
      zh_Hans: 模型名称
    placeholder:
      en_US: Enter your model name
      zh_Hans: 输入模型名称
  credential_form_schemas:
  - variable: openai_api_key
    label:
      en_US: API Key
    type: secret-input
    required: true
    placeholder:
      zh_Hans: 在此输入你的 API Key
      en_US: Enter your API Key
  - variable: openai_organization
    label:
        zh_Hans: 组织 ID
        en_US: Organization
    type: text-input
    required: false
    placeholder:
      zh_Hans: 在此输入你的组织 ID
      en_US: Enter your Organization ID
  - variable: openai_api_base
    label:
      zh_Hans: API Base
      en_US: API Base
    type: text-input
    required: false
    placeholder:
      zh_Hans: 在此输入你的 API Base
      en_US: Enter your API Base
```

You can also refer to the [YAML configuration information](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/docs/en_US/schema.md) in the directories of other providers under the `model_providers` directory.

**Implement Provider Code**

We need to create a Python file with the same name under `model_providers`, such as `anthropic.py`, and implement a `class` that inherits from the `__base.provider.Provider` base class, such as `AnthropicProvider`.

**Custom Model Providers**

For providers like Xinference that offer custom models, this step can be skipped. Just create an empty `XinferenceProvider` class and implement an empty `validate_provider_credentials` method. This method will not actually be used and is only to avoid abstract class instantiation errors.

```python
class XinferenceProvider(Provider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        pass
```

**Predefined Model Providers**

Providers need to inherit from the `__base.model_provider.ModelProvider` base class and implement the `validate_provider_credentials` method to validate the provider's unified credentials. You can refer to [AnthropicProvider](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/model_providers/anthropic/anthropic.py).

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

You can also reserve the `validate_provider_credentials` implementation first and directly reuse it after implementing the model credential validation method.

**Adding Models**

[**Adding Predefined Models**](https://docs.dify.ai/v/zh-hans/guides/model-configuration/predefined-model)**👈🏻**

For predefined models, we can connect them by simply defining a YAML file and implementing the calling code.

[**Adding Custom Models**](https://docs.dify.ai/v/zh-hans/guides/model-configuration/customizable-model) **👈🏻**

For custom models, we only need to implement the calling code to connect them, but the parameters they handle may be more complex.

***

#### Testing

To ensure the availability of the connected provider/model, each method written needs to have corresponding integration test code written in the `tests` directory.

Taking `Anthropic` as an example.

Before writing test code, you need to add the credential environment variables required for testing the provider in `.env.example`, such as: `ANTHROPIC_API_KEY`.

Before executing, copy `.env.example` to `.env` and then execute.

**Writing Test Code**

Create a `module` with the same name as the provider under the `tests` directory: `anthropic`, and continue to create `test_provider.py` and corresponding model type test py files in this module, as shown below:

```shell
.
├── __init__.py
├── anthropic
│   ├── __init__.py
│   ├── test_llm.py       # LLM Test
│   └── test_provider.py  # Provider Test
```

Write test code for various situations of the implemented code above, and after passing the tests, submit the code.
