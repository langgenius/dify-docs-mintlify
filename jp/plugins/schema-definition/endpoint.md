## Endpoint（エンドポイント）

この記事では、プラグイン内のエンドポイントの構造を説明するために、[クイックスタート：レインボーキャットプロジェクト](../develop-plugins/extension-plugin.md)を例として取り上げます。完全なプラグインコードは、[Github](https://github.com/langgenius/dify-plugin-sdks/tree/main/python/examples/neko)で確認できます。

### **グループの定義**

`Endpoint`グループは、複数の`Endpoint`をまとめたものです。`Dify`プラグインで新しい`Endpoint`を作成する際には、以下の設定項目を入力する必要があります。

![](https://assets-docs.dify.ai/2024/11/763dbf86e4319591415dc5a1b6948ccb.png)

「Endpoint Name」の他に、グループ構成情報を記述することで、新しいフォーム項目を追加できます。保存すると、同じ構成情報を使用する複数のインターフェースが表示されるようになります。

![](https://assets-docs.dify.ai/2024/11/b778b7093b7df0dc80a476c65ddcbe58.png)

#### **構造**

*   `settings` (map\[string] [ProviderConfig](general-specifications.md#providerconfig)): エンドポイントの設定定義
*   `endpoints` (list\[string], required): 特定の`endpoint`インターフェース定義を指定します。

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

### **インターフェース定義**

*   `path` (string): werkzeugのインターフェース標準に従います。
*   `method` (string): インターフェースのメソッド。`HEAD` `GET` `POST` `PUT` `DELETE` `OPTIONS`のみをサポートします。
*   `extra` (object): 基本情報以外の設定情報
    *   `python` (object)
        *   `source` (string): このインターフェースを実装するソースコード

```yaml
path: "/duck/<app_id>"
method: "GET"
extra:
  python:
    source: "endpoints/duck.py"
```

### エンドポイントの実装

`dify_plugin.Endpoint`を継承したサブクラスを実装し、`_invoke`メソッドを実装する必要があります。

* **入力パラメータ**
  *   `r` (Request): werkzeugからのリクエストオブジェクト
  *   `values` (Mapping): パスから解析されたパスパラメータ
  *   `settings` (Mapping): このエンドポイントの設定情報
* **戻り値**
  *   werkzeugからのレスポンスオブジェクト。ストリーミングでの応答をサポートします。
  *   直接的な文字列の戻り値はサポートしません。

**コード例:**

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