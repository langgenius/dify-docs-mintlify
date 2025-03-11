# 外部データツール

AIアプリを作成する際、開発者はAPI拡張を通じて外部ツールを利用し、追加データを取得してPromptに組み込むことができます。具体的な手順については[external-data-tool.md](../../knowledge-base/external-data-tool.md "mention")を参照してください。

### 前提条件

まずは[.](./ "mention")を読み、APIサービスの基本的な機能の開発と接続を完了してください。

### 拡張ポイント

`app.external_data_tool.query`は、外部データツールのクエリ拡張ポイントです。

この拡張ポイントは、エンドユーザーが入力したアプリ変数の内容と対話入力内容（対話型アプリの固定パラメータ）をパラメータとしてAPIに渡します。

開発者は対応するツールのクエリロジックを実装し、文字列型のクエリ結果を返す必要があります。

#### リクエストボディ <a href="#user-content-request-body" id="user-content-request-body"></a>

```
{
    "point": "app.external_data_tool.query", // 拡張ポイントの種類。ここではapp.external_data_tool.queryに固定
    "params": {
        "app_id": string,  // アプリID
        "tool_variable": string,  // 外部データツール変数名。対応する変数ツールの呼び出し元を示す
        "inputs": {  // エンドユーザーが入力した変数値。キーが変数名、値が変数値
            "var_1": "value_1",
            "var_2": "value_2",
            ...
        },
        "query": string | null  // エンドユーザーの現在の対話入力内容。対話型アプリの固定パラメータ
    }
}
```

* 例
  * ```
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

#### API応答 <a href="#usercontentapi-fan-hui" id="usercontentapi-fan-hui"></a>

```
{
    "result": string
}
```

* 例
  * ```
    {
        "result": "City: London\nTemperature: 10°C\nRealFeel®: 8°C\nAir Quality: Poor\nWind Direction: ENE\nWind Speed: 8 km/h\nWind Gusts: 14 km/h\nPrecipitation: Light rain"
    }
    ```