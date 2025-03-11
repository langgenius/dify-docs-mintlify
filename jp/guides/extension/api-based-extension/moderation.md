# 敏感内容審査

このモジュールは、アプリケーションにおける端末ユーザーの入力内容とLLM（大規模言語モデル）の出力内容を審査するために使用され、2つの拡張点タイプに分かれています。

### 拡張点 <a href="#usercontent-kuo-zhan-dian" id="usercontent-kuo-zhan-dian"></a>

* `app.moderation.input` 端末ユーザー入力内容の審査拡張点
  * 端末ユーザーが送信した変数の内容や対話型アプリケーションにおける対話の入力内容を審査するために使用されます。
* `app.moderation.output` LLM出力内容の審査拡張点
  * LLMの出力内容を審査するために使用されます。
  * LLMの出力がストリーミング形式の場合、出力内容は100文字ごとに分割され、APIにリクエストされます。これにより、出力内容が長い場合でも審査が遅れないようにします。

### app.moderation.input 拡張点 <a href="#usercontentappmoderationinput-kuo-zhan-dian" id="usercontentappmoderationinput-kuo-zhan-dian"></a>

#### リクエストボディ <a href="#user-content-request-body" id="user-content-request-body"></a>

```
{
    "point": "app.moderation.input", // 拡張点タイプ。ここでは固定で app.moderation.input
    "params": {
        "app_id": string,  // アプリケーションID
        "inputs": {  // 端末ユーザーが送信した変数の値。key は変数名、value は変数の値
            "var_1": "value_1",
            "var_2": "value_2",
            ...
        },
        "query": string | null  // 端末ユーザーの現在の対話入力内容。対話型アプリケーションの固定パラメータ。
    }
}
```

* 例
  * ```
    {
        "point": "app.moderation.input",
        "params": {
            "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
            "inputs": {
                "var_1": "I will kill you.",
                "var_2": "I will fuck you."
            },
            "query": "Happy everydays."
        }
    }
    ```

#### APIレスポンス <a href="#usercontentapi-fan-hui" id="usercontentapi-fan-hui"></a>

```
{
    "flagged": bool,  // 検証ルールに違反しているかどうか
    "action": string, // アクション。direct_output 予設回答の直接出力; overridden 送信された変数値の上書き
    "preset_response": string,  // 予設回答（actionがdirect_outputの場合のみ返される）
    "inputs": {  // 端末ユーザーが送信した変数の値。key は変数名、value は変数の値（actionがoverriddenの場合のみ返される）
        "var_1": "value_1",
        "var_2": "value_2",
        ...
    },
    "query": string | null  // 上書きされた端末ユーザーの現在の対話入力内容。対話型アプリケーションの固定パラメータ。（actionがoverriddenの場合のみ返される）
}
```

* 例
  * `action=direct_output`
    * ```
      {
          "flagged": true,
          "action": "direct_output",
          "preset_response": "Your content violates our usage policy."
      }
      ```
  * `action=overridden`
    * ```
      {
          "flagged": true,
          "action": "overridden",
          "inputs": {
              "var_1": "I will *** you.",
              "var_2": "I will *** you."
          },
          "query": "Happy everydays."
      }
      ```

### app.moderation.output 拡張点 <a href="#usercontentappmoderationoutput-kuo-zhan-dian" id="usercontentappmoderationoutput-kuo-zhan-dian"></a>

#### リクエストボディ <a href="#user-content-request-body-1" id="user-content-request-body-1"></a>

```
{
    "point": "app.moderation.output", // 拡張点タイプ。ここでは固定で app.moderation.output
    "params": {
        "app_id": string,  // アプリケーションID
        "text": string  // LLMの回答内容。LLMの出力がストリーミング形式の場合、ここには100文字ごとの分割された内容が入ります。
    }
}
```

* 例
  * ```
    {
        "point": "app.moderation.output",
        "params": {
            "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
            "text": "I will kill you."
        }
    }
    ```

#### APIレスポンス <a href="#usercontentapi-fan-hui-1" id="usercontentapi-fan-hui-1"></a>

```
{
    "flagged": bool,  // 検証ルールに違反しているかどうか
    "action": string, // アクション。direct_output 予設回答の直接出力; overridden 送信された変数値の上書き
    "preset_response": string,  // 予設回答（actionがdirect_outputの場合のみ返される）
    "text": string  // 上書きされたLLMの回答内容。（actionがoverriddenの場合のみ返される）
}
```

* 例
  * `action=direct_output`
    * ```
      {
          "flagged": true,
          "action": "direct_output",
          "preset_response": "Your content violates our usage policy."
      }
      ```
  * `action=overridden`
    * ```
      {
          "flagged": true,
          "action": "overridden",
          "text": "I will *** you."
      }
      ```