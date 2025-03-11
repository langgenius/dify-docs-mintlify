# App

Reverse App requesting means plugins can access App data in Dify. This module supports both streaming and non-streaming App calls.

### **Endpoints Type:**

* For `Chatbot/Agent/Chatflow` type applications, they are all chat-type applications, having the same input and output parameters, thus can be uniformly viewed as a **Chat Interface**.
* For Workflow applications, they occupy a separate **Workflow Interface**.
* For Completion (text generation) applications, they occupy a separate **Completion Interface**.

Note: Plugins can only access Apps within the same Workspace as the plugin.

### **Requesting Chat Interface** **Entry Point**

#### Entry

```python
self.session.app.chat
```

#### **Endpoint Specification**

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

When `response_mode` is `streaming`, the interface returns `Generator[dict]`, otherwise returns `dict`. For specific interface fields, refer to `ServiceApi` return results.

#### **Example**

We can request a Chat type App in an `Endpoint` and directly return the results:

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

**Requesting Workflow Endpint** **Entry Point**

#### Entry

```python
self.session.app.workflow
```

#### **Endpoint Specification**

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

### **Requesting Completion Endpoint**

#### Entry

```python
self.session.app.completion
```

**Endpoint Specification**

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
