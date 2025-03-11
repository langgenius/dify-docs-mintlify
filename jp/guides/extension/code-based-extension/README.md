# コード拡張

開発者がDifyをローカルでデプロイする際、APIサービスを再構築せずに拡張機能を実装したい場合は、コード拡張を使用できます。これにより、元のDifyのコードロジックを乱すことなく、コード形式（つまり、プラグイン機能）で機能を拡張または強化することが可能です。特定のインターフェースや仕様に従うことで、メインプログラムとの互換性とプラグアンドプレイ機能を実現できます。現在、Difyは2種類のコード拡張を提供しています：

* 新しいタイプの外部データツールの追加 [external-data-tool.md](external-data-tool.md "mention")
* センシティブコンテンツモデレーション戦略の拡張 [moderation.md](moderation.md "mention")

上記の機能に基づき、コードレベルのインターフェース仕様に従うことで水平拡張を実現できます。もしあなたが自分の拡張機能を私たちに提供したい場合、Difyにプルリクエストを提出することを心より歓迎します。

## フロントエンドコンポーネント仕様定義

コード拡張のフロントエンドスタイルは `schema.json` を通じて定義されます：

* label: カスタムタイプ名、システム言語切り替えに対応
* form\_schema: フォーム内容のリスト
  * type: コンポーネントタイプ
    * select: ドロップダウンオプション
    * text-input: テキスト入力
    * paragraph: 段落
  * label: コンポーネント名、システム言語切り替えに対応
  * variable: 変数名
  * required: 必須かどうか
  * default: デフォルト値
  * placeholder: コンポーネントのヒント内容
  * options: "select" コンポーネント専用プロパティ、ドロップダウン内容を定義
    * label: ドロップダウン名、システム言語切り替えに対応
    * value: ドロップダウンオプション値
  * max\_length: "text-input" コンポーネント専用プロパティ、最大長

### テンプレート例

```json
{
    "label": {
        "en-US": "Cloud Service",
        "zh-Hans": "云服务"
    },
    "form_schema": [
        {
            "type": "select",
            "label": {
                "en-US": "Cloud Provider",
                "zh-Hans": "云厂商"
            },
            "variable": "cloud_provider",
            "required": true,
            "options": [
                {
                    "label": {
                        "en-US": "AWS",
                        "zh-Hans": "亚马逊"
                    },
                    "value": "AWS"
                },
                {
                    "label": {
                        "en-US": "Google Cloud",
                        "zh-Hans": "谷歌云"
                    },
                    "value": "GoogleCloud"
                },
                {
                    "label": {
                        "en-US": "Azure Cloud",
                        "zh-Hans": "微软云"
                    },
                    "value": "Azure"
                }
            ],
            "default": "GoogleCloud",
            "placeholder": ""
        },
        {
            "type": "text-input",
            "label": {
                "en-US": "API Endpoint",
                "zh-Hans": "API Endpoint"
            },
            "variable": "api_endpoint",
            "required": true,
            "max_length": 100,
            "default": "",
            "placeholder": "https://api.example.com"
        },
        {
            "type": "paragraph",
            "label": {
                "en-US": "API Key",
                "zh-Hans": "API Key"
            },
            "variable": "api_keys",
            "required": true,
            "default": "",
            "placeholder": "Paste your API key here"
        }
    ]
}
```
