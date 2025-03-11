# App

反向调用 App 指的是插件能够访问 Dify 中的 App 数据。该模块同时支持流式与非流式的 App 调用。

**接口类型：**

* 对于 `Chatbot/Agent/Chatflow`  类型应用而言，它们都属于聊天类型的应用，因此拥有相同类型的输入参数和输出参数，因此可被统一视为**聊天接口。**
* 对于 Workflow 应用而言，它单独占据一个 **Workflow 接口。**
* 对于 Completion（文本生成应用）应用而言，它单独占据一个 **Completion 接口**。

请注意，插件仅允许访问插件所在的 Workspace 中的 App。

### 调用聊天接口

#### **入口**

```python
    self.session.app.chat
```

#### **接口规范**

```python
    def invoke(
        self,
        app_id: str,
        inputs: dict,
        response_mode: Literal["streaming", "blocking"],
        conversation_id: str,
        files: list,
    ) -> Generator[dict, None, None] | dict:
        pass
```

当 `response_mode` 为 `streaming` 时，该接口将直接返回 `Generator[dict]`，否则直接返回 `dict`，具体的接口字段请参考 `ServiceApi` 的返回结果。

#### **用例**

我们可以在一个 `Endpoint` 中调用 Chat 类型的 App，并将结果直接返回。

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
            response = self.session.app.workflow.invoke(
                app_id=app_id, inputs={}, response_mode="streaming", files=[]
            )

            for data in response:
                yield f"{json.dumps(data)} <br>"

        return Response(generator(), status=200, content_type="text/html")
```

### 调用 Workflow 接口

#### **入口**

```python
    self.session.app.workflow
```

#### **接口规范**

```python
    def invoke(
        self,
        app_id: str,
        inputs: dict,
        response_mode: Literal["streaming", "blocking"],
        files: list,
    ) -> Generator[dict, None, None] | dict:
        pass
```

### 调用 Completion 接口

#### **入口**

```python
    self.session.app.completion
```

**接口规范**

```python
    def invoke(
        self,
        app_id: str,
        inputs: dict,
        response_mode: Literal["streaming", "blocking"],
        files: list,
    ) -> Generator[dict, None, None] | dict:
        pass
```

\
