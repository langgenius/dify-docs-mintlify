# APIによるデータセットの維持

> 認証、メソッド呼び出し、アプリケーションサービスAPIは一貫性を保ちます。ナレッジAPIトークンの違いは、すべてのナレッジベースで操作できることです。

### ナレッジAPIを使用する利点
* Difyデータセットを使ってデータシステムを同期化し、強力なワークフローを作成します。
* データセットリスト、ドキュメントリスト、詳細クエリを提供し、独自のデータ管理ページを生成しやすくします。
* プレーンテキストとファイルのアップロード、ドキュメントの更新。セグメントレベルでの一括追加・変更に対応し、同期プロセスをします。
* Difyソフトウェアおよびサービスの可視性を向上させ、手動でのドキュメント処理や同期の時間を短縮します。

### 使用方法

ナレッジページに移動し、左側のナビゲーションでAPIページに切り替えます。このページでは、difyが提供するAPIドキュメントを表示し、ナレッジAPIにアクセスするための認証情報を管理できます。

![ナレッジAPIドキュメント](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/features/datasets/9c9f592c965ab8cf57ae6160361099bf.png)

## **空のナレッジを作成する**

**`POST /datasets`**

{% hint style="warning" %}
空のデータセットを作成するためだけに使用します
{% endhint %}

```
curl --location --request POST 'https://api.dify.ai/v1/datasets' \
--header 'Authorization: Bearer {api_key}' \
--header 'コンテンツタイプ: application/json' \
--data-raw '{"name": "name"}'
```

#### **ナレッジリスト**

```
curl --location --request GET 'https://api.dify.ai/v1/datasets?page=1&limit=20' \
--header 'Authorization: Bearer {api_key}'
```

#### **テキストでドキュメントを作成**

```
curl --location --request POST '<https://api.dify.ai/v1/datasets/<uuid:データセットID>/document/create_by_text>' \\
--header 'Authorization: Bearer {api_key}' \\
--header 'コンテンツタイプ: application/json' \\
--data-raw '{
    "name": "Dify",
    "text": "Dify means Do it for you...",
    "indexing_technique": "高品質",
    "process_rule": {
        "rules": {
                "pre_processing_rules": [{
                        "id": "余分なスペースを削除",
                        "enabled": true
                }, {
                        "id": "URLとメールを削除",
                        "enabled": true
                }],
                "segmentation": {
                        "separator": "###",
                        "max_tokens": 500
                }
        },
        "mode": "カスタム"
    }
}'
```

#### **ファイルでドキュメントを作成**

```
curl --location POST 'https://api.dify.ai/v1/datasets/{データセットID}/document/create_by_file' \
--header 'Authorization: Bearer {api_key}' \
--form 'data="{
	"name": "Dify",
	"indexing_technique": "高品質",
	"process_rule": {
		"rules": {
			"pre_processing_rules": [{
				"id": "余分なスペースを削除",
				"enabled": true
			}, {
				"id": "URLとメールを削除",
				"enabled": true
			}],
			"segmentation": {
				"separator": "###",
				"max_tokens": 500
			}
		},
		"mode": "カスタム"
	}
    }";
    タイプ=テキスト/プレーン' \
--form 'file=@"/パス/ファイル"'
```

#### **ドキュメントのインデックスステータスを取得**

```
curl --location --request GET 'https://api.dify.ai/v1/datasets/{データセットID}/documents/{batch}/indexing-status' \
--header 'Authorization: Bearer {api_key}'
```

#### **ドキュメントを削除**

```
curl --location --request GET 'https://api.dify.ai/v1/datasets/{データセットID}/documents' \
--header 'Authorization: Bearer {api_key}'
```

#### **新しいセグメントを追加**

```
curl --location 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data '{"segments": [{"content": "1","answer": "1","keywords": ["a"]}]}'
```

#### 文書セグメントの削除

```
curl --location --request DELETE 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json'
```

### エラーメッセージ

- `document_indexing`、ドキュメントがインデックス化中であることを示します
- `provider_not_initialize`、埋め込みモデルが設定されていないことを示します
- `not_found`、ドキュメントが見つからないことを示します
- `dataset_name_duplicate`、重複した名前が付けられていることを示します
- `provider_quota_exceeded`、プロバイダーのクォータが最大制限を超えたことを示します
- `dataset_not_initialized`、データセットが初期化されていないことを示します
- `unsupported_file_type`、サポートされていないファイルタイプであることを示します
    - 現在サポートされているファイルタイプは次のとおりです：txt、markdown、md、pdf、html、htm、xlsx、docx、csv
- `too_many_files`、ファイルの数が多すぎることを示します。現在は単一ファイルのアップロードのみサポートします
- `file_too_large`、ファイルが大きすぎることを示します。15M以下のファイルのみサポートします