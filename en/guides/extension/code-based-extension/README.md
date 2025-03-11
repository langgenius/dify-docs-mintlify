# Code Based Extensions

For developers deploying Dify locally, if you want to implement extension capabilities without rewriting an API service, you can use code extensions. This allows you to extend or enhance the functionality of the program in code form (i.e., plugin capability) without disrupting the original code logic of Dify. It follows certain interfaces or specifications to achieve compatibility and plug-and-play capability with the main program. Currently, Dify offers two types of code extensions:

* Adding a new type of external data tool [External Data Tool](https://docs.dify.ai/guides/extension/api-based-extension/external-data-tool)
* Extending sensitive content moderation strategies [Moderation](https://docs.dify.ai/guides/extension/api-based-extension/moderation)

Based on the above functionalities, you can achieve horizontal expansion by following the code-level interface specifications. If you are willing to contribute your extensions to us, we warmly welcome you to submit a PR to Dify.

## Frontend Component Specification Definition

The frontend styles of code extensions are defined through `schema.json`:

* label: Custom type name, supporting system language switching
* form_schema: List of form contents
  * type: Component type
    * select: Dropdown options
    * text-input: Text
    * paragraph: Paragraph
  * label: Component name, supporting system language switching
  * variable: Variable name
  * required: Whether it is required
  * default: Default value
  * placeholder: Component hint content
  * options: Exclusive property for the "select" component, defining the dropdown contents
    * label: Dropdown name, supporting system language switching
    * value: Dropdown option value
  * max_length: Exclusive property for the "text-input" component, maximum length

### Template Example

```json
{
    "label": {
        "en-US": "Cloud Service",
        "zh-Hans": "云服务"
    },
    "form_schema": [
        {
            "type": "select",
            "label": {
                "en-US": "Cloud Provider",
                "zh-Hans": "云厂商"
            },
            "variable": "cloud_provider",
            "required": true,
            "options": [
                {
                    "label": {
                        "en-US": "AWS",
                        "zh-Hans": "亚马逊"
                    },
                    "value": "AWS"
                },
                {
                    "label": {
                        "en-US": "Google Cloud",
                        "zh-Hans": "谷歌云"
                    },
                    "value": "GoogleCloud"
                },
                {
                    "label": {
                        "en-US": "Azure Cloud",
                        "zh-Hans": "微软云"
                    },
                    "value": "Azure"
                }
            ],
            "default": "GoogleCloud",
            "placeholder": ""
        },
        {
            "type": "text-input",
            "label": {
                "en-US": "API Endpoint",
                "zh-Hans": "API Endpoint"
            },
            "variable": "api_endpoint",
            "required": true,
            "max_length": 100,
            "default": "",
            "placeholder": "https://api.example.com"
        },
        {
            "type": "paragraph",
            "label": {
                "en-US": "API Key",
                "zh-Hans": "API Key"
            },
            "variable": "api_keys",
            "required": true,
            "default": "",
            "placeholder": "Paste your API key here"
        }
    ]
}
```