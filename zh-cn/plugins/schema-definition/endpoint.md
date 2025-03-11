---
description: 'Author: Yeuoly，Allen'
---

# Endpoint

本文将以[彩虹猫](../quick-start/develop-plugins/extension-plugin.md)项目为例，说明插件内的 Endpoint 的结构。完整的插件代码请参考 [Github 仓库](https://github.com/langgenius/dify-plugin-sdks/tree/main/python/examples/neko)。

### 组定义

一个 `Endpoint` 组是多个 `Endpoint` 的集合，在 `Dify` 插件内新建 `Endpoint` 时可能需要填写如下配置。

![](https://assets-docs.dify.ai/2024/11/763dbf86e4319591415dc5a1b6948ccb.png)

除了 `Endpoint Name` 外，你可以通过编写组的配置信息来添加新的表单项，点击保存后，你可以看到其中包含的多个接口，它们将使用相同的配置信息。

![](https://assets-docs.dify.ai/2024/11/b778b7093b7df0dc80a476c65ddcbe58.png)

#### **结构**

* `settings`(map\[string] [ProviderConfig](general-specifications.md#providerconfig) )：Endpoint 配置定义
* `endpoints`(list\[string], required)：指向具体的 `endpoint` 接口定义

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

### 接口定义

* `path`(string)：遵循 werkzeug 接口标准
* `method`(string)：接口方法，仅支持`HEAD` `GET` `POST` `PUT` `DELETE` `OPTIONS`
* `extra`(object)：除基础信息外的配置信息
  * `python`(object)
    * `source`(string)：实现该接口的源代码

```yaml
path: "/duck/<app_id>"
method: "GET"
extra:
  python:
    source: "endpoints/duck.py"
```

### 接口实现

需要实现一个继承自 `dify_plugin.Endpoint` 子类，并实现 `_invoke` 方法。

* **输入参数**
  * `r`(Request)：`werkzeug` 中的 `Request` 对象
  * `values`(Mapping)：从 path 中解析到的路径参数
  * `settings`(Mapping)：该 `Endpoint` 的配置信息
* **返回**
  * `werkzeug` 中的 `Response` 对象，支持流式返回
  * 不支持直接返回字符串

示例代码：

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

