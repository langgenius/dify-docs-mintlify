# アプリ

リバース呼び出しとは、プラグインがDify内のAppデータにアクセスできることを意味します。このモジュールは、ストリーミングと非ストリーミングの両方のAppコールをサポートしています。

### **エンドポイントタイプ：**

* `Chatbot/Agent/Chatflow`タイプのアプリケーションは、すべてチャットタイプのアプリケーションであり、同じ入力パラメータと出力パラメータを持つため、統一的に**チャットインターフェース**として扱うことができます。
* Workflowアプリケーションは、独立した**ワークフローインターフェース**を占有します。
* Completion（テキスト生成）アプリケーションは、独立した**Completionエンドポイント**を占有します。

注意：プラグインは、プラグインと同じWorkspace内のAppにのみアクセスできます。

### **チャットインターフェースのリクエスト** **エントリーポイント**

#### エントリーポイント

```python
self.session.app.chat
```

#### **エンドポイント仕様**

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

`response_mode`が`streaming`の場合、インターフェースは`Generator[dict]`を返し、それ以外の場合は`dict`を返します。具体的なインターフェースフィールドについては、`ServiceApi`の戻り値を参照してください。

#### **例**

`Endpoint`内でチャットタイプのAppをリクエストし、結果を直接返すことができます：

```python
import json
from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint

class Duck(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        """
        与えられたリクエストでエンドポイントを呼び出します。
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

**ワークフローエンドポイント** **エントリーポイント**

#### エントリー

```python
self.session.app.workflow
```

#### **エンドポイント仕様**

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

### **Completionエンドポイントのリクエスト**

#### エントリー

```python
self.session.app.completion
```

**エンドポイント仕様**

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
