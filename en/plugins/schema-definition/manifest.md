# Manifest

**Manifest File** A Manifest is a YAML-compliant file that defines the most basic information about a **plugin**, including but not limited to the plugin name, author, included tools, models, and other information.

If this file's format is incorrect, both the plugin parsing and packaging processes will fail.

### **Code Example**

Below is a simple example of a Manifest file. The meaning and function of each data element will be explained below. For reference to other plugin codes, please check the [Github repository](https://github.com/langgenius/dify-plugin-sdks/tree/main/python/examples).

```yaml
version: 0.0.1
type: "plugin"
author: "Yeuoly"
name: "neko"
label:
  en_US: "Neko"
created_at: "2024-07-12T08:03:44.658609186Z"
icon: "icon.svg"
resource:
  memory: 1048576
  permission:
    tool:
      enabled: true
    model:
      enabled: true
      llm: true
    endpoint:
      enabled: true
    app:
      enabled: true
    storage: 
      enabled: true
      size: 1048576
plugins:
  endpoints:
    - "provider/neko.yaml"
meta:
  version: 0.0.1
  arch:
    - "amd64"
    - "arm64"
  runner:
    language: "python"
    version: "3.10"
    entrypoint: "main"
privacy: "./privacy.md"
```

### **Structure**

* `version` (version, required): Plugin version
* `type` (type, required): Plugin type, currently only supports `plugin`, will support `bundle` in the future
* `author` (string, required): Author, defined as organization name in Marketplace
* `label` (label, required): Multi-language names
* `created_at` (RFC3339, required): Creation time, must not be later than current time for Marketplace
* `icon` (asset, required): Icon path
* `resource` (object): Required resources
  * `memory` (int64): Maximum memory usage, mainly related to AWS Lambda resource requests on SaaS, in bytes
  * `permission` (object): Permission requests
    * `tool` (object): Permission for reverse tool calls
      * `enabled` (bool)
    * `model` (object): Permission for reverse model calls
      * `enabled` (bool)
      * `llm` (bool)
      * `text_embedding` (bool)
      * `rerank` (bool)
      * `tts` (bool)
      * `speech2text` (bool)
      * `moderation` (bool)
    * `node` (object): Permission for reverse node calls
      * `enabled` (bool)
    * `endpoint` (object): Permission to register endpoints
      * `enabled` (bool)
    * `app` (object): Permission for reverse app calls
      * `enabled` (bool)
    * `storage` (object): Permission for persistent storage
      * `enabled` (bool)
      * `size` (int64): Maximum allowed persistent memory size in bytes
* `plugins` (object, required): List of YAML files defining specific plugin capabilities, absolute paths within plugin package
  * Format
    * `tools` (list\[string]): Extended [tool](tool.md) providers
    * `models` (list\[string]): Extended [model](model/) providers
    * `endpoints` (list\[string]): Extended [Endpoints](endpoint.md) providers
    * `agent_strategies` (list\[string]): Extended Agent strategy providers
  * Limitations
    * Cannot extend both tools and models simultaneously
    * Must have at least one extension
    * Cannot extend both models and Endpoints simultaneously
    * Currently supports only one provider per extension type
* `meta` (object)
  * `version` (version, required): Manifest format version, initial version `0.0.1`
  * `arch` (list\[string], required): Supported architectures, currently only `amd64` `arm64`
  * `runner` (object, required): Runtime configuration
    * `language` (string): Currently only supports python
    * `version` (string): Language version, currently only supports `3.12`
    * `entrypoint` (string): Program entry point, should be `main` for Python
* `privacy` (string, optional): An optional field specifying the relative path or URL to the plugin’s privacy policy file, such as `"./privacy.md`" or `"https://your-web/privacy"`. If you plan to publish the plugin to the Dify Marketplace, this field is required to provide a clear statement on user data usage and privacy. For more detailed instructions, please refer to the [Plugin Privacy Policy Guidelines](../publish-plugins/publish-to-dify-marketplace/plugin-privacy-protection-guidelines.md#id-1.-list-the-types-of-data-collected).
