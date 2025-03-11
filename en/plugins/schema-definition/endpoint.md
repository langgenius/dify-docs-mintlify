# Endpoint

In this article, we will use the [Quick Start: Rainbow Cat project](../develop-plugins/extension-plugin.md) as an example to illustrate the structure of Endpoint within the plugin. For the complete plugin code, please refer to the [Github repository](https://github.com/langgenius/dify-plugin-sdks/tree/main/python/examples/neko).

### **Group Definition**

An `Endpoint` group is a collection of multiple `Endpoints`. When creating a new `Endpoint` in a `Dify` plugin, you may need to fill in the following configurations.

![](https://assets-docs.dify.ai/2024/11/763dbf86e4319591415dc5a1b6948ccb.png)

Besides the `Endpoint Name`, you can add new form items by writing group configuration information. After saving, you'll see multiple interfaces that will use the same configuration information.

![](https://assets-docs.dify.ai/2024/11/b778b7093b7df0dc80a476c65ddcbe58.png)

#### **Structure**

* `settings` (map\[string] [ProviderConfig](general-specifications.md#providerconfig)): Endpoint configuration definitions
* `endpoints` (list\[string], required): Points to specific `endpoint` interface definitions

```yaml
settings:
  api_key:
    type: secret-input
    required: true
    label:
      en_US: API key
      zh_Hans: API key
      ja_Jp: API key
      pt_BR: API key
    placeholder:
      en_US: Please input your API key
      zh_Hans: 请输入你的 API key
      ja_Jp: あなたの API key を入れてください
      pt_BR: Por favor, insira sua chave API
endpoints:
  - endpoints/duck.yaml
  - endpoints/neko.yaml
```

### **Interface Definition**

* `path` (string): Follows werkzeug interface standard
* `method` (string): Interface method, only supports HEAD GET POST PUT DELETE OPTIONS
* `extra` (object): Configuration information beyond basic info
  * `python` (object)
    * `source` (string): Source code implementing this interface

```yaml
path: "/duck/<app_id>"
method: "GET"
extra:
  python:
    source: "endpoints/duck.py"
```

### **Endpoint Implementation**

Must implement a subclass inheriting from `dify_plugin.Endpoint` and implement the `_invoke` method.

* **Input Parameters**
  * `r` (Request): Request object from werkzeug
  * `values` (Mapping): Path parameters parsed from the path
  * `settings` (Mapping): Configuration information for this Endpoint
* **Return**
  * Response object from werkzeug, supports streaming return
  * Does not support direct string return

**Example Code:**

```python
import json
from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint

class Duck(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        Invokes the endpoint with the given request.
        """
        app_id = values["app_id"]
        def generator():
            yield f"{app_id} <br>"
        return Response(generator(), status=200, content_type="text/html")
```
