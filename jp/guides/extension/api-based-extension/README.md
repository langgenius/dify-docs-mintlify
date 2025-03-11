# API 拡張

開発者はAPIエクステンションを通じてモジュールの機能を拡張できます。現在、以下のモジュールがサポートされています：

* `モデレーション` 敏感内容の監査
* `外部データツール` 外部データツール

モジュールの機能を拡張する前に、APIと認証用のAPIキー（Difyが自動生成することも可能）を準備する必要があります。

対応するモジュール機能を開発するだけでなく、DifyがAPIを正しく呼び出せるよう、以下の仕様にも従う必要があります。

![APIに基づくエクステンション](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/extension/api-based-extension/ae289aeca0b29222a4e36820f76e3c5c.png)

### API仕様 <a href="#usercontentapi-gui-fan" id="usercontentapi-gui-fan"></a>

Difyは以下の仕様に従ってインターフェースを呼び出します：

```
POST {Your-API-Endpoint}
```

#### ヘッダー <a href="#user-content-header" id="user-content-header"></a>

| Header     | Value           | Desc                                                        |
| ---------- | --------------- | ----------------------------------------------------------- |
| `Content-Type` | application/json   | リクエスト内容はJSON形式です。                                           |
| `Authorization`       | Bearer {api\_key} | APIキーはトークン形式で送信されます。`api_key`を解析し、提供されたAPIキーと一致するか確認してください。 |

#### リクエストボディ <a href="#user-content-request-body" id="user-content-request-body"></a>

```
{
    "point":  string, //  エクステンションポイント、異なるモジュールは複数のエクステンションポイントを含む可能性があります
    "params": {
        ...  // 各モジュールのエクステンションポイントに渡すパラメータ
    }
}
```

#### APIレスポンス <a href="#usercontentapi-fan-hui" id="usercontentapi-fan-hui"></a>

```
{
    ...  // APIレスポンスの内容、異なるエクステンションポイントのレスポンスは各モジュールの仕様に従います
}
```

### 検証 <a href="#usercontent-xiao-yan" id="usercontent-xiao-yan"></a>

DifyがAPIベースのエクステンションを設定する際、DifyはAPIエンドポイントにリクエストを送り、APIの有効性を確認します。

APIエンドポイントが`point=ping`を受信した場合、インターフェースは`result=pong`を返す必要があります。具体的には次の通りです：

#### ヘッダー <a href="#user-content-header-1" id="user-content-header-1"></a>

```
Content-Type: application/json
Authorization: Bearer {api_key}
```

#### リクエストボディ <a href="#user-content-request-body-1" id="user-content-request-body-1"></a>

```
{
    "point": "ping"
}
```

#### API期待レスポンス <a href="#usercontentapi-qi-wang-fan-hui" id="usercontentapi-qi-wang-fan-hui"></a>

```
{
    "result": "pong"
}
```

### 例 <a href="#usercontent-fan-li" id="usercontent-fan-li"></a>

ここでは外部データツールを例にとり、地域に基づいて外部の天気情報を取得するシナリオを示します。

#### API例 <a href="#usercontentapi-fan-li" id="usercontentapi-fan-li"></a>

```
POST https://fake-domain.com/api/dify/receive
```

**ヘッダー**

```
Content-Type: application/json
Authorization: Bearer 123456
```

**リクエストボディ**

```
{
    "point": "app.external_data_tool.query",
    "params": {
        "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
        "tool_variable": "weather_retrieve",
        "inputs": {
            "location": "London"
        },
        "query": "How's the weather today?"
    }
}
```

**APIレスポンス**

```
{
    "result": "City: London\nTemperature: 10°C\nRealFeel®: 8°C\nAir Quality: Poor\nWind Direction: ENE\nWind Speed: 8 km/h\nWind Gusts: 14 km/h\nPrecipitation: Light rain"
}
```

#### コード例 <a href="#usercontent-dai-ma-fan-li" id="usercontent-dai-ma-fan-li"></a>

コードはPython FastAPIフレームワークに基づいています。

1.  依存関係をインストールする

    ```
    pip install fastapi[all] uvicorn
    ```
2.  インターフェース仕様に従ってコードを書く

    ```
    from fastapi import FastAPI, Body, HTTPException, Header
    from pydantic import BaseModel

    app = FastAPI()


    class InputData(BaseModel):
        point: str
        params: dict = {}


    @app.post("/api/dify/receive")
    async def dify_receive(data: InputData = Body(...), authorization: str = Header(None)):
        """
        DifyからのAPIクエリデータを受信します。
        """
        expected_api_key = "123456"  # TODO このAPIのAPIキー
        auth_scheme, _, api_key = authorization.partition(' ')

        if auth_scheme.lower() != "bearer" or api_key != expected_api_key:
            raise HTTPException(status_code=401, detail="Unauthorized")

        point = data.point

        # デバッグ用
        print(f"point: {point}")

        if point == "ping":
            return {
                "result": "pong"
            }
        if point == "app.external_data_tool.query":
            return handle_app_external_data_tool_query(params=data.params)
        # elif point == "{point name}":
            # TODO その他のポイントの実装

        raise HTTPException(status_code=400, detail="Not implemented")


    def handle_app_external_data_tool_query(params: dict):
        app_id = params.get("app_id")
        tool_variable = params.get("tool_variable")
        inputs = params.get("inputs")
        query = params.get("query")

        # デバッグ用
        print(f"app_id: {app_id}")
        print(f"tool_variable: {tool_variable}")
        print(f"inputs: {inputs}")
        print(f"query: {query}")

        # TODO 外部データツールクエリの実装
        # 返り値は"result"キーを持つ辞書でなければならず、その値はクエリの結果でなければならない
        if inputs.get("location") == "London":
            return {
                "result": "City: London\nTemperature: 10°C\nRealFeel®: 8°C\nAir Quality: Poor\nWind Direction: ENE\nWind "
                          "Speed: 8 km/h\nWind Gusts: 14 km/h\nPrecipitation: Light rain"
            }
        else:
            return {"result": "Unknown city"}
    ```
3.  APIサービスを起動する。デフォルトポートは8000で、APIの完全なアドレスは：`http://127.0.0.1:8000/api/dify/receive`、設定されたAPIキーは`123456`です。

    <pre><code><strong>uvicorn main:app --reload --host 0.0.0.0
    </strong></code></pre>
4. DifyにこのAPIを設定します。

![APIの設定](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/extension/api-based-extension/ae289aeca0b29222a4e36820f76e3c5c.png)

5. アプリでこのAPIエクステンションを選択します。

![エクステンションの選択](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/extension/api-based-extension/ae289aeca0b29222a4e36820f76e3c5c.png)

アプリのデバッグ時、Difyは設定されたAPIにリクエストを送り、以下の内容（例）を送信します：

```
{
    "point": "app.external_data_tool.query",
    "params": {
        "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
        "tool_variable": "weather_retrieve",
        "inputs": {
            "location": "London"
        },
        "query": "How's the weather today?"
    }
}
```

APIレスポンスは以下の通りです：

```
{
    "result": "City: London\nTemperature: 10°C\nRealFeel®: 8°C\nAir Quality: Poor\nWind Direction: ENE\nWind Speed: 8 km/h\nWind Gusts: 14 km/h\nPrecipitation: Light rain"
}
```

### ローカルデバッグ

Difyクラウド版は内網APIサービスにアクセスできないため、ローカルでAPIサービスをデバッグするために、[Ngrok](https://ngrok.com)を使用してAPIサービスのエンドポイントをパブリックに公開し、クラウドでローカルコードをデバッグすることができます。操作手順は次の通りです：

1.  [https://ngrok.com](https://ngrok.com)の公式サイトにアクセスし、登録してNgrokファイルをダウンロードします。

    ![ダウンロード](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/extension/api-based-extension/c44d6cc5425508daac8d31bc4af113df.png)
2. ダウンロードが完了したら、ダウンロードディレクトリに移動し、以下の説明に従って圧縮ファイルを解凍し、初期化スクリプトを実行します。
   * ```Shell
     $ unzip /path/to/ngrok.zip
     $ ./ngrok config add-authtoken あなたのトークン
     ```
3. ローカルAPIサービスのポートを確認します：

![ポートの確認](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/extension/api-based-extension/7ac8ee0f0955f36255e0261b36499db7.png)

次に以下のコマンドを実行して開始します：

*   ```Shell
    $ ./ngrok http ポート番号
    ```

    成功例は以下の通りです：

![Ngrokの起動](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/extension/api-based-extension/2b4adbe0bb1ff203da521ea6eea401f8.png)

4. Forwardingで示されるように、上の図では`https://177e-159-223-41-52.ngrok-free.app`（これは例のドメインです。自分のドメインに置き換えてください）がパブリックドメインとなります。

* 上記の例に従って、ローカルで既に起動しているサービスエンドポイントを公開し、コード例のインターフェース：`http://127.0.0.1:8000/api/dify/receive`を`https://177e-159-223-41-52.ngrok-free.app/api/dify/receive`に置き換えます。

これで、このAPIエンドポイントはパブリックアクセス可能となります。これで、DifyでこのAPIエンドポイントを設定してローカルデバッグコードを実行できます。設定手順については、[external-data-tool.md](../../knowledge-base/external-data-tool.md "mention")を参照してください。

### Cloudflare Workersを使用したAPIエクステンションのデプロイ

Cloudflare Workersを使用してAPIエクステンションをデプロイすることをお勧めします。Cloudflare Workersは簡単にパブリックアドレスを提供でき、無料で使用できます。

[cloudflare-workers.md](cloudflare-workers.md "mention")。
