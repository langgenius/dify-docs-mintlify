# External Data Tools

External data tools are used to fetch additional data from external sources after the end user submits data, and then assemble this data into prompts as additional context information for the LLM. Dify provides a default tool for external API calls, check [api-based-extension](../api-based-extension/ "mention") for details.

For developers deploying Dify locally, to meet more customized needs or to avoid developing an additional API Server, you can directly insert custom external data tool logic in the form of a plugin based on the Dify service. After extending custom tools, your custom tool options will be added to the dropdown list of tool types, and team members can use these custom tools to fetch external data.

## Quick Start

Here is an example of extending an external data tool for `Weather Search`, with the following steps:

1. Initialize the directory
2. Add frontend form specifications
3. Add implementation class
4. Preview the frontend interface
5. Debug the extension

### 1. **Initialize the Directory**

To add a custom type `Weather Search`, you need to create the relevant directory and files under `api/core/external_data_tool`.

```python
.
└── api
    └── core
        └── external_data_tool
            └── weather_search
                ├── __init__.py
                ├── weather_search.py
                └── schema.json
```

### 2. **Add Frontend Component Specifications**

* `schema.json`, which defines the frontend component specifications, detailed in [.](./ "mention")

```json
{
    "label": {
        "en-US": "Weather Search",
        "zh-Hans": "天气查询"
    },
    "form_schema": [
        {
            "type": "select",
            "label": {
                "en-US": "Temperature Unit",
                "zh-Hans": "温度单位"
            },
            "variable": "temperature_unit",
            "required": true,
            "options": [
                {
                    "label": {
                        "en-US": "Fahrenheit",
                        "zh-Hans": "华氏度"
                    },
                    "value": "fahrenheit"
                },
                {
                    "label": {
                        "en-US": "Centigrade",
                        "zh-Hans": "摄氏度"
                    },
                    "value": "centigrade"
                }
            ],
            "default": "centigrade",
            "placeholder": "Please select temperature unit"
        }
    ]
}
```

### 3. Add Implementation Class

`weather_search.py` code template, where you can implement the specific business logic.

{% hint style="warning" %}
Note: The class variable `name` must be the custom type name, consistent with the directory and file name, and must be unique.
{% endhint %}

```python
from typing import Optional

from core.external_data_tool.base import ExternalDataTool


class WeatherSearch(ExternalDataTool):
    """
    The name of custom type must be unique, keep the same with directory and file name.
    """
    name: str = "weather_search"

    @classmethod
    def validate_config(cls, tenant_id: str, config: dict) -> None:
        """
        schema.json validation. It will be called when user save the config.

        Example:
            .. code-block:: python
                config = {
                    "temperature_unit": "centigrade"
                }

        :param tenant_id: the id of workspace
        :param config: the variables of form config
        :return:
        """

        if not config.get('temperature_unit'):
            raise ValueError('temperature unit is required')

    def query(self, inputs: dict, query: Optional[str] = None) -> str:
        """
        Query the external data tool.

        :param inputs: user inputs
        :param query: the query of chat app
        :return: the tool query result
        """
        city = inputs.get('city')
        temperature_unit = self.config.get('temperature_unit')

        if temperature_unit == 'fahrenheit':
            return f'Weather in {city} is 32°F'
        else:
            return f'Weather in {city} is 0°C'
```

<!-- ### 4. **Preview the Frontend Interface**

Follow the above steps and run the service to see the newly added custom type. -->

<!-- ![](todo) -->

### 4. **Debug the Extension**

Now, you can select the custom `Weather Search` external data tool extension type in the Dify application orchestration interface for debugging.

## Implementation Class Template

```python
from typing import Optional

from core.external_data_tool.base import ExternalDataTool


class WeatherSearch(ExternalDataTool):
    """
    The name of custom type must be unique, keep the same with directory and file name.
    """
    name: str = "weather_search"

    @classmethod
    def validate_config(cls, tenant_id: str, config: dict) -> None:
        """
        schema.json validation. It will be called when user save the config.

        :param tenant_id: the id of workspace
        :param config: the variables of form config
        :return:
        """

        # implement your own logic here

    def query(self, inputs: dict, query: Optional[str] = None) -> str:
        """
        Query the external data tool.

        :param inputs: user inputs
        :param query: the query of chat app
        :return: the tool query result
        """
       
        # implement your own logic here
        return "your own data."
```

### Detailed Introduction to Implementation Class Development

### def validate_config

`schema.json` form validation method, called when the user clicks "Publish" to save the configuration.

* `config` form parameters
  * `{{variable}}` custom form variables

### def query

User-defined data query implementation, the returned result will be replaced into the specified variable.

* `inputs`: Variables passed by the end user
* `query`: Current conversation input content from the end user, a fixed parameter for conversational applications.