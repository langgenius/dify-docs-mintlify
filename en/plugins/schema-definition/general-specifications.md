# General Specifications

This article will briefly introduce common structures in plugin development.

### **Path Specifications**

When specifying file paths in Manifest or any yaml files, follow these two rules based on file types:

* For multimedia files like images or videos (e.g., plugin `icon`), place them in the `_assets` folder under the plugin root directory.
* For regular text files like `.py` or `.yaml`, use the absolute path within the plugin project.

### **Common Structures**

When defining plugins, some data structures can be shared among tools, models, and Endpoints. Here are these shared structures.

#### **I18nObject**

`I18nObject` is an internationalization structure compliant with IETF BCP 47 standard, currently supporting four languages:

* en\_US
* zh\_Hans
* ja\_Jp
* pt\_BR

#### **ProviderConfig**

`ProviderConfig` is a common provider form structure, applicable to both `Tool` and `Endpoint`

* `name` (string): Form item name
* `label` (I18nObject, required): Follows IETF BCP 47
* `type` (provider\_config\_type, required): Form type
* `scope` (provider\_config\_scope): Option range, varies with `type`
* `required` (bool): Cannot be empty
* `default` (any): Default value, only supports basic types `float` `int` `string`
* `options` (list\[provider\_config\_option]): Options, only used when type is `select`
* `helper` (object): Help documentation link label, follows IETF BCP 47
* `url` (string): Help documentation link
* `placeholder` (object): Follows IETF BCP 47

#### ProviderConfigOption(object)

* `value`(string, required)：values
* `label`(object, required)：comply with [IETF BCP 47](https://tools.ietf.org/html/bcp47)

#### ProviderConfigType(string)

* `secret-input` (string)：Configuration information will be encrypted
* `text-input`(string)：Plain text
* `select`(string)：drop-down box
* `boolean`(bool)：switchgear
* `model-selector`(object)：Model configuration information, including vendor name, model name, model parameters, etc.
* `app-selector`(object)：app id
* `tool-selector`(object)：Tool configuration information, including tool vendor, name, parameters, etc.
* `dataset-selector`(string)：TBD

#### ProviderConfigScope(string)

* When `type` is `model-selector`
  * `all`
  * `llm`
  * `text-embedding`
  * `rerank`
  * `tts`
  * `speech2text`
  * `moderation`
  * `vision`
* When `type` is `app-selector`
  * `all`
  * `chat`
  * `workflow`
  * `completion`
* When `type` is `tool-selector`
  * `all`
  * `plugin`
  * `api`
  * `workflow`

#### **ModelConfig**

* `provider` (string): Model provider name including plugin\_id, in the format of `langgenius/openai/openai`
* `model` (string): Specific model name
* `model_type` (enum): Model type enumeration, refer to this document

#### **NodeResponse**

* `inputs` (dict): Variables finally input to the node
* `outputs` (dict): Node output results
* `process_data` (dict): Data generated during node execution

#### **ToolSelector**

* `provider_id` (string): Tool provider name
* `tool_name` (string): Tool name
* `tool_description` (string): Tool description
* `tool_configuration` (dict\[str, Any]): Tool configuration information
* `tool_parameters` (dict\[str, dict]): Parameters requiring LLM inference
  * `name` (string): Parameter name
  * `type` (string): Parameter type
  * `required` (bool): Whether required
  * `description` (string): Parameter description
  * `default` (any): Default value
  * `options` (list\[string]): Available options
