# Model Designing Rules

* Model provider rules are based on the [Provider](model-designing-rules.md#provider) entity.
* Model rules are based on the [AIModelEntity](model-designing-rules.md#provider) entity.

> All entities below are based on Pydantic BaseModel and can be found in the entities module.

### **Provider**

* `provider` (string): Provider identifier, e.g., openai
* `label` (object): Provider display name, i18n, supports en\_US (English) and zh\_Hans (Chinese)
  * `zh_Hans` (string) \[optional]: Chinese label, defaults to en\_US if not set
  * `en_US` (string): English label
* `description` (object) \[optional]: Provider description, i18n
  * `zh_Hans` (string) \[optional]: Chinese description
  * `en_US` (string): English description
* `icon_small` (string) \[optional]: Provider small icon, stored in \_assets directory
  * `zh_Hans` (string) \[optional]: Chinese icon
  * `en_US` (string): English icon
* `icon_large` (string) \[optional]: Provider large icon, stored in \_assets directory
  * `zh_Hans` (string) \[optional]: Chinese icon
  * `en_US` (string): English icon
* `background` (string) \[optional]: Background color value, e.g., #FFFFFF, uses frontend default if empty
* `help` (object) \[optional]: Help information
  * `title` (object): Help title, i18n
    * `zh_Hans` (string) \[optional]: Chinese title
    * `en_US` (string): English title
  * `url` (object): Help link, i18n
    * `zh_Hans` (string) \[optional]: Chinese link
    * `en_US` (string): English link
* `supported_model_types` (array\[ModelType]): Supported model types
* `configurate_methods` (array\[ConfigurateMethod]): Configuration methods
* `provider_credential_schema` (\[ProviderCredentialSchema]): Provider credential specifications
* `model_credential_schema` (\[ModelCredentialSchema]): Model credential specifications

### **AIModelEntity**

* `model` (string): Model identifier, e.g., gpt-3.5-turbo
* `label` (object) \[optional]: Model display name, i18n
  * `zh_Hans` (string) \[optional]: Chinese label
  * `en_US` (string): English label
* `model_type` (\[ModelType]): Model type
* `features` (array\[\[ModelFeature]]) \[optional]: List of supported features
* `model_properties` (object): Model properties
  * `mode` (\[LLMMode]): Mode (available for llm model type)
  * `context_size` (int): Context size (available for llm and text-embedding types)
  * `max_chunks` (int): Maximum number of chunks (available for text-embedding and moderation types)
  * `file_upload_limit` (int): Maximum file upload limit in MB (available for speech2text type)
  * `supported_file_extensions` (string): Supported file extensions, e.g., mp3,mp4 (available for speech2text type)
  * `default_voice` (string): Default voice, must be one of: alloy,echo,fable,onyx,nova,shimmer (available for tts type)
  * `voices` (list): Available voice list
  * `mode` (string): Voice model (available for tts type)
  * `name` (string): Voice model display name (available for tts type)
  * `language` (string): Voice model supported languages (available for tts type)
  * `word_limit` (int): Single conversion word limit, defaults to paragraph division (available for tts type)
  * `audio_type` (string): Supported audio file extensions, e.g., mp3,wav (available for tts type)
  * `max_workers` (int): Maximum concurrent tasks for text-to-audio conversion (available for tts type)
  * `max_characters_per_chunk` (int): Maximum characters per chunk (available for moderation type)
* `parameter_rules` (array\[ParameterRule]) \[optional]: Model call parameter rules
* `pricing` (\[PriceConfig]) \[optional]: Pricing information
* `deprecated` (bool): Whether deprecated. If true, model won't show in list but configured ones can still be used. Default: False

### **ModelType**

* `llm`: Text generation model
* `text-embedding`: Text embedding model
* `rerank`: Rerank model
* `speech2text`: Speech to text
* `tts`: Text to speech
* `moderation`: Moderation

### **ConfigurateMethod**

* `predefined-model`: Predefined models Users only need to configure unified provider credentials to use predefined models under the provider.
* `customizable-model`: Custom models Users need to add credential configurations for each model.
* `fetch-from-remote`: Fetch from remote Similar to predefined-model configuration, only requires unified provider credentials, models are fetched from provider using credential information.

### **ModelFeature**

* `agent-thought`: Agent reasoning, generally models over 70B have chain-of-thought capability
* `vision`: Visual capability, i.e., image understanding
* `tool-call`: Tool calling
* `multi-tool-call`: Multiple tool calling
* `stream-tool-call`: Streaming tool calling

### **FetchFrom**

* `predefined-model`: Predefined models
* `fetch-from-remote`: Remote models

### **LLMMode**

* `completion`: Text completion
* `chat`: Conversation

### **ParameterRule**

* `name` (string): Actual parameter name for model calls
* `use_template` (string) \[optional]: Template usage Five preset variable content configuration templates:
  * temperature
  * top\_p
  * frequency\_penalty
  * presence\_penalty
  * max\_tokens Can directly set template variable name in use\_template, will use default config from entities.defaults.PARAMETER\_RULE\_TEMPLATE
* `label` (object) \[optional]: Labels, i18n
  * `zh_Hans` (string) \[optional]: Chinese label
  * `en_US` (string): English label
* `type` (string) \[optional]: Parameter type
  * `int`: Integer
  * `float`: Float
  * `string`: String
  * `boolean`: Boolean
* `help` (string) \[optional]: Help information
  * `zh_Hans` (string) \[optional]: Chinese help info
  * `en_US` (string): English help info
* `required` (bool): Whether required, default False
* `default` (int/float/string/bool) \[optional]: Default value
* `min` (int/float) \[optional]: Minimum value, only for numeric types
* `max` (int/float) \[optional]: Maximum value, only for numeric types
* `precision` (int) \[optional]: Precision, decimal places, only for numeric types
* `options` (array\[string]) \[optional]: Dropdown options, only for string type

### **PriceConfig**

* `input` (float): Input price, i.e., Prompt price
* `output` (float): Output price, i.e., Return content price
* `unit` (float): Price unit, e.g., if priced per 1M tokens, unit token number is 0.000001
* `currency` (string): Currency unit

### **ProviderCredentialSchema**

* `credential_form_schemas` (array\[CredentialFormSchema]): Credential form specifications

### **ModelCredentialSchema**

* `model` (object): Model identifier, default variable name is 'model'
* `label` (object): Model form item display name
  * `en_US` (string): English
  * `zh_Hans` (string) \[optional]: Chinese
* `placeholder` (object): Model prompt content
  * `en_US` (string): English
  * `zh_Hans` (string) \[optional]: Chinese
* `credential_form_schemas` (array\[CredentialFormSchema]): Credential form specifications

### **CredentialFormSchema**

* `variable` (string): Form item variable name
* `label` (object): Form item label
  * `en_US` (string): English
  * `zh_Hans` (string) \[optional]: Chinese
* `type` (\[FormType]): Form item type
* `required` (bool): Whether required
* `default` (string): Default value
* `options` (array\[FormOption]): Form item options for select or radio types
* `placeholder` (object): Form item placeholder for text-input type
  * `en_US` (string): English
  * `zh_Hans` (string) \[optional]: Chinese
* `max_length` (int): Maximum input length for text-input type, 0 means no limit
* `show_on` (array\[FormShowOnObject]): Show when other form items meet conditions, always show if empty

#### **FormType**

* `text-input`: Text input component
* `secret-input`: Password input component
* `select`: Single-select dropdown
* `radio`: Radio component
* `switch`: Switch component, only supports true and false

#### **FormOption**

* `label` (object): Label
  * `en_US` (string): English
  * `zh_Hans` (string) \[optional]: Chinese
* `value` (string): Dropdown option value
* `show_on` (array\[FormShowOnObject]): Show when other form items meet conditions, always show if empty

#### **FormShowOnObject**

* `variable` (string): Other form item variable name
* `value` (string): Other form item variable value

