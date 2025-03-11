# Sensitive Content Moderation

In addition to the system's built-in content moderation types, Dify also supports user-defined content moderation rules. This method is suitable for developers customizing their own private deployments. For instance, in an enterprise internal customer service setup, it may be required that users, while querying or customer service agents while responding, not only avoid entering words related to violence, sex, and illegal activities but also avoid specific terms forbidden by the enterprise or violating internally established moderation logic. Developers can extend custom content moderation rules at the code level in a private deployment of Dify.

## Quick Start

Here is an example of extending a `Cloud Service` content moderation type, with the steps as follows:

1. Initialize the directory
2. Add the frontend component definition file
3. Add the implementation class
4. Preview the frontend interface
5. Debug the extension

### 1. Initialize the Directory

To add a custom type `Cloud Service`, create the relevant directories and files under the `api/core/moderation` directory.

```Plain
.
└── api
    └── core
        └── moderation
            └── cloud_service
                ├── __init__.py
                ├── cloud_service.py
                └── schema.json
```

### 2. Add Frontend Component Specifications

* `schema.json`: This file defines the frontend component specifications. For details, see [.](./ "mention").

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

### 3. Add Implementation Class

`cloud_service.py` code template where you can implement specific business logic.

{% hint style="warning" %}
Note: The class variable name must be the same as the custom type name, matching the directory and file names, and must be unique.
{% endhint %}

```python
from core.moderation.base import Moderation, ModerationAction, ModerationInputsResult, ModerationOutputsResult

class CloudServiceModeration(Moderation):
    """
    The name of custom type must be unique, keep the same with directory and file name.
    """
    name: str = "cloud_service"

    @classmethod
    def validate_config(cls, tenant_id: str, config: dict) -> None:
        """
        schema.json validation. It will be called when user saves the config.

        Example:
            .. code-block:: python
                config = {
                    "cloud_provider": "GoogleCloud",
                    "api_endpoint": "https://api.example.com",
                    "api_keys": "123456",
                    "inputs_config": {
                        "enabled": True,
                        "preset_response": "Your content violates our usage policy. Please revise and try again."
                    },
                    "outputs_config": {
                        "enabled": True,
                        "preset_response": "Your content violates our usage policy. Please revise and try again."
                    }
                }

        :param tenant_id: the id of workspace
        :param config: the variables of form config
        :return:
        """

        cls._validate_inputs_and_outputs_config(config, True)

        if not config.get("cloud_provider"):
            raise ValueError("cloud_provider is required")

        if not config.get("api_endpoint"):
            raise ValueError("api_endpoint is required")

        if not config.get("api_keys"):
            raise ValueError("api_keys is required")

    def moderation_for_inputs(self, inputs: dict, query: str = "") -> ModerationInputsResult:
        """
        Moderation for inputs.

        :param inputs: user inputs
        :param query: the query of chat app, there is empty if is completion app
        :return: the moderation result
        """
        flagged = False
        preset_response = ""

        if self.config['inputs_config']['enabled']:
            preset_response = self.config['inputs_config']['preset_response']

            if query:
                inputs['query__'] = query
            flagged = self._is_violated(inputs)

        # return ModerationInputsResult(flagged=flagged, action=ModerationAction.overridden, inputs=inputs, query=query)
        return ModerationInputsResult(flagged=flagged, action=ModerationAction.DIRECT_OUTPUT, preset_response=preset_response)

    def moderation_for_outputs(self, text: str) -> ModerationOutputsResult:
        """
        Moderation for outputs.

        :param text: the text of LLM response
        :return: the moderation result
        """
        flagged = False
        preset_response = ""

        if self.config['outputs_config']['enabled']:
            preset_response = self.config['outputs_config']['preset_response']

            flagged = self._is_violated({'text': text})

        # return ModerationOutputsResult(flagged=flagged, action=ModerationAction.overridden, text=text)
        return ModerationOutputsResult(flagged=flagged, action=ModerationAction.DIRECT_OUTPUT, preset_response=preset_response)

    def _is_violated(self, inputs: dict):
        """
        The main logic of moderation.

        :param inputs:
        :return: the moderation result
        """
        return False
```

<!-- ### 4. Preview Frontend Interface

Following the above steps, run the service to see the newly added custom type. -->

<!-- ![](todo) -->

### 4. Debug the Extension

At this point, you can select the custom `Cloud Service` content moderation extension type for debugging in the Dify application orchestration interface.

## Implementation Class Template

```python
from core.moderation.base import Moderation, ModerationAction, ModerationInputsResult, ModerationOutputsResult

class CloudServiceModeration(Moderation):
    """
    The name of custom type must be unique, keep the same with directory and file name.
    """
    name: str = "cloud_service"

    @classmethod
    def validate_config(cls, tenant_id: str, config: dict) -> None:
        """
        schema.json validation. It will be called when user saves the config.
        
        :param tenant_id: the id of workspace
        :param config: the variables of form config
        :return:
        """
        cls._validate_inputs_and_outputs_config(config, True)
        
        # implement your own logic here

    def moderation_for_inputs(self, inputs: dict, query: str = "") -> ModerationInputsResult:
        """
        Moderation for inputs.

        :param inputs: user inputs
        :param query: the query of chat app, there is empty if is completion app
        :return: the moderation result
        """
        flagged = False
        preset_response = ""
        
        # implement your own logic here
        
        # return ModerationInputsResult(flagged=flagged, action=ModerationAction.overridden, inputs=inputs, query=query)
        return ModerationInputsResult(flagged=flagged, action=ModerationAction.DIRECT_OUTPUT, preset_response=preset_response)

    def moderation_for_outputs(self, text: str) -> ModerationOutputsResult:
        """
        Moderation for outputs.

        :param text: the text of LLM response
        :return: the moderation result
        """
        flagged = False
        preset_response = ""
        
        # implement your own logic here

        # return ModerationOutputsResult(flagged=flagged, action=ModerationAction.overridden, text=text)
        return ModerationOutputsResult(flagged=flagged, action=ModerationAction.DIRECT_OUTPUT, preset_response=preset_response)
```

## Detailed Introduction to Implementation Class Development

### def validate\_config

The `schema.json` form validation method is called when the user clicks "Publish" to save the configuration.

* `config` form parameters
  * `{{variable}}` custom variable of the form
  * `inputs_config` input moderation preset response
    * `enabled` whether it is enabled
    * `preset_response` input preset response
  * `outputs_config` output moderation preset response
    * `enabled` whether it is enabled
    * `preset_response` output preset response

### def moderation\_for\_inputs

Input validation function

* `inputs`: values passed by the end user
* `query`: the current input content of the end user in a conversation, a fixed parameter for conversational applications.
* `ModerationInputsResult`
  * `flagged`: whether it violates the moderation rules
  * `action`: action to be taken
    * `direct_output`: directly output the preset response
    * `overridden`: override the passed variable values
  * `preset_response`: preset response (returned only when action=direct_output)
  * `inputs`: values passed by the end user, with key as the variable name and value as the variable value (returned only when action=overridden)
  * `query`: overridden current input content of the end user in a conversation, a fixed parameter for conversational applications (returned only when action=overridden)

### def moderation\_for\_outputs

Output validation function

* `text`: content output by the model
* `moderation_for_outputs`: output validation function
  * `text`: content of the LLM response. When the LLM output is streamed, this is the content in segments of 100 characters.
  * `ModerationOutputsResult`
    * `flagged`: whether it violates the moderation rules
    * `action`: action to be taken
      * `direct_output`: directly output the preset response
      * `overridden`: override the passed variable values
    * `preset_response`: preset response (returned only when action=direct_output)
    * `text`: overridden content of the LLM response (returned only when action=overridden).