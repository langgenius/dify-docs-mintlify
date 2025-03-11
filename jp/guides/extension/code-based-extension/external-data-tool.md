# 外部データツール

外部データツールは、エンドユーザーがデータを送信した後、外部ツールを使用して追加のデータを取得し、それをプロンプトに組み込むことで、LLMの追加のコンテキスト情報として利用します。Difyはデフォルトで外部API呼び出しツールを提供しており、詳細は[api-based-extension](../api-based-extension/ "mention")を参照してください。

ローカルにDifyをデプロイする開発者向けには、よりカスタマイズされたニーズに対応するため、または追加のAPIサーバーを開発したくない場合、Difyサービスの基盤にカスタムの外部データツールをプラグインとして直接挿入することができます。カスタムツールを拡張した後、ツールタイプのドロップダウンリストにカスタムツールオプションが追加され、チームメンバーはカスタムツールを使用して外部データを取得できるようになります。

## クイックスタート

ここでは、`天気検索`外部データツール拡張を例として、以下の手順を説明します：

1. ディレクトリの初期化
2. フロントエンドフォーム規格の追加
3. 実装クラスの追加
<!-- 4. フロントエンドインターフェースのプレビュー -->
4. 拡張のデバッグ

### 1. **ディレクトリの初期化**

新しいカスタムタイプ`Weather Search`を追加するには、`api/core/external_data_tool`ディレクトリに関連するディレクトリとファイルを新規作成します。

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

### 2. **フロントエンドコンポーネント規格の追加**

* `schema.json`、ここではフロントエンドコンポーネントの規格を定義します。詳細は[.](./ "mention")を参照してください。

```json
{
    "label": {
        "en-US": "Weather Search",
        "zh-Hans": "天気検索"
    },
    "form_schema": [
        {
            "type": "select",
            "label": {
                "en-US": "Temperature Unit",
                "zh-Hans": "温度単位"
            },
            "variable": "temperature_unit",
            "required": true,
            "options": [
                {
                    "label": {
                        "en-US": "Fahrenheit",
                        "zh-Hans": "華氏度"
                    },
                    "value": "fahrenheit"
                },
                {
                    "label": {
                        "en-US": "Centigrade",
                        "zh-Hans": "摂氏度"
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

### 3. 実装クラスの追加

`weather_search.py`のコードテンプレートです。ここに具体的な業務ロジックを実装します。

{% hint style="warning" %}
注意点：クラス変数nameはカスタムタイプ名称であり、ディレクトリとファイル名と一致し、かつ唯一である必要があります。
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

<!-- ### 4. **フロントエンドインターフェースのプレビュー**

上記の手順を実行し、サービスを実行すると、新しいカスタムタイプが表示されます。

Image todo -->

### 4. **拡張のデバッグ**

これで、Difyアプリケーションオーケストレーションインターフェースでカスタム`Weather Search`外部データツール拡張タイプを選択してデバッグできます。

## 実装クラステンプレート

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

### 実装クラスの詳細な説明

### def validate\_config

`schema.json`フォーム検証メソッド、ユーザーが「公開」をクリックして設定を保存するときに呼び出されます。

* `config` フォームパラメータ
  * `{variable}` フォームカスタム変数

### def query

ユーザーがカスタムデータクエリを実装し、返される結果は指定された変数に置き換えられます。

* `inputs` ：エンドユーザーが入力した変数値
* `query` ：エンドユーザーが現在の会話で入力した内容、対話型アプリケーションの固定パラメータ。