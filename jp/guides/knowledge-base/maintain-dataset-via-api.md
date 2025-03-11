# APIによるデータセットの維持

> 認証や呼び出し方法はサービスAPIと同様ですが、生成される各ナレッジベースAPIトークンには、現在のアカウントでアクセス可能なすべてのナレッジベースを操作する権限が付与されています。データの安全性には十分ご注意ください。

### ナレッジベースAPIを使用するのメリット

APIを利用してナレッジベースを管理することで、データ処理の効率が大幅に向上します。コマンドラインを使ってデータの同期を簡単に行え、自動化も可能になるため、ユーザーインターフェースでの手間のかかる操作が不要になります。

主なメリットは以下の通りです：

* **自動同期**: データシステムとDifyナレッジベースをシームレスに統合し、効率的なワークフローを実現します。
* **包括的な管理**: ナレッジベースリスト、ドキュメントリスト、詳細クエリなどの機能を提供し、自分だけのデータ管理画面を簡単に作成できます。
* **柔軟なアップロード**: 純粋なテキストやファイルのアップロード方法をサポートし、セグメント（Chunks）コンテンツに対する一括追加や変更が可能です。
* **効率の向上**: 手動処理の時間を短縮し、Difyプラットフォームの利用体験を向上させます。

### 使用方法

ナレッジベースページにアクセスし、左側のナビゲーションで **API** ページに切り替えます。このページでは、Difyが提供するナレッジベースAPIドキュメントを確認し、 **APIキー** でナレッジベースAPIにアクセスするための資格情報を管理できます。

![Knowledge API ドキュメント](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/knowledge-base/2848fc9fc3a7f641f16eee11ed6c6223.png)

### API呼び出しの例

#### テクストを通してドキュメントを作成する

入力例：

```json
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/document/create-by-text' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "text","text": "text","indexing_technique": "high_quality","process_rule": {"mode": "automatic"}}'
```

出力例：

```json
{
  "document": {
    "id": "",
    "position": 1,
    "data_source_type": "upload_file",
    "data_source_info": {
        "upload_file_id": ""
    },
    "dataset_process_rule_id": "",
    "name": "text.txt",
    "created_from": "api",
    "created_by": "",
    "created_at": 1695690280,
    "tokens": 0,
    "indexing_status": "waiting",
    "error": null,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "archived": false,
    "display_status": "queuing",
    "word_count": 0,
    "hit_count": 0,
    "doc_form": "text_model"
  },
  "batch": ""
}
```

#### ファイルを通してドキュメントを作成する

入力例：

```json
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/document/create_by_file' \
--header 'Authorization: Bearer {api_key}' \
--form 'data="{"indexing_technique":"high_quality","process_rule":{"rules":{"pre_processing_rules":[{"id":"remove_extra_spaces","enabled":true},{"id":"remove_urls_emails","enabled":true}],"segmentation":{"separator":"###","max_tokens":500}},"mode":"custom"}}";type=text/plain' \
--form 'file=@"/path/to/file"'
```

出力例：

```json
{
  "document": {
    "id": "",
    "position": 1,
    "data_source_type": "upload_file",
    "data_source_info": {
      "upload_file_id": ""
    },
    "dataset_process_rule_id": "",
    "name": "Dify.txt",
    "created_from": "api",
    "created_by": "",
    "created_at": 1695308667,
    "tokens": 0,
    "indexing_status": "waiting",
    "error": null,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "archived": false,
    "display_status": "queuing",
    "word_count": 0,
    "hit_count": 0,
    "doc_form": "text_model"
  },
  "batch": ""
}

```

#### **空白のナレッジベースを作成する**

{% hint style="warning" %}
空のデータセットを作成するためだけに使用
{% endhint %}

入力例：

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "name", "permission": "only_me"}'
```

出力例：

```json
{
  "id": "",
  "name": "name",
  "description": null,
  "provider": "vendor",
  "permission": "only_me",
  "data_source_type": null,
  "indexing_technique": null,
  "app_count": 0,
  "document_count": 0,
  "word_count": 0,
  "created_by": "",
  "created_at": 1695636173,
  "updated_by": "",
  "updated_at": 1695636173,
  "embedding_model": null,
  "embedding_model_provider": null,
  "embedding_available": null
}
```

#### **ナレッジベースリスト**

入力例：

```bash
curl --location --request GET 'https://api.dify.ai/v1/datasets?page=1&limit=20' \
--header 'Authorization: Bearer {api_key}'
```

出力例：

```json
{
  "data": [
    {
      "id": "",
      "name": "ナレッジベースの名前",
      "description": "情報説明",
      "permission": "only_me",
      "data_source_type": "upload_file",
      "indexing_technique": "",
      "app_count": 2,
      "document_count": 10,
      "word_count": 1200,
      "created_by": "",
      "created_at": "",
      "updated_by": "",
      "updated_at": ""
    },
    ...
  ],
  "has_more": true,
  "limit": 20,
  "total": 50,
  "page": 1
}
```

#### ナレッジベースの削除

入力例：

```json
curl --location --request DELETE 'https://api.dify.ai/v1/datasets/{dataset_id}' \
--header 'Authorization: Bearer {api_key}'
```

出力例：

```json
204 No Content
```

#### テクストを通してドキュメントを更新する

このAPIは存在しているナレッジベースにしか使えます。

入力例：

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/update_by_text' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "name","text": "text"}'
```

出力例：

```json
{
  "document": {
    "id": "",
    "position": 1,
    "data_source_type": "upload_file",
    "data_source_info": {
      "upload_file_id": ""
    },
    "dataset_process_rule_id": "",
    "name": "name.txt",
    "created_from": "api",
    "created_by": "",
    "created_at": 1695308667,
    "tokens": 0,
    "indexing_status": "waiting",
    "error": null,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "archived": false,
    "display_status": "queuing",
    "word_count": 0,
    "hit_count": 0,
    "doc_form": "text_model"
  },
  "batch": ""
}
```

#### ファイルを通してドキュメントを更新する

このAPIは存在しているナレッジベースにしか使えます。

入力例：

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/update_by_file' \
--header 'Authorization: Bearer {api_key}' \
--form 'data="{"name":"Dify","indexing_technique":"high_quality","process_rule":{"rules":{"pre_processing_rules":[{"id":"remove_extra_spaces","enabled":true},{"id":"remove_urls_emails","enabled":true}],"segmentation":{"separator":"###","max_tokens":500}},"mode":"custom"}}";type=text/plain' \
--form 'file=@"/path/to/file"'
```

出力例：

```json
{
  "document": {
    "id": "",
    "position": 1,
    "data_source_type": "upload_file",
    "data_source_info": {
      "upload_file_id": ""
    },
    "dataset_process_rule_id": "",
    "name": "Dify.txt",
    "created_from": "api",
    "created_by": "",
    "created_at": 1695308667,
    "tokens": 0,
    "indexing_status": "waiting",
    "error": null,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "archived": false,
    "display_status": "queuing",
    "word_count": 0,
    "hit_count": 0,
    "doc_form": "text_model"
  },
  "batch": "20230921150427533684"
}
```

#### **ドキュメント埋め込みステータス(進捗状況)の取得**

入力例：

```bash
curl --location --request GET 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{batch}/indexing-status' \
--header 'Authorization: Bearer {api_key}'
```

出力例：

```json
{
  "data":[{
    "id": "",
    "indexing_status": "indexing",
    "processing_started_at": 1681623462.0,
    "parsing_completed_at": 1681623462.0,
    "cleaning_completed_at": 1681623462.0,
    "splitting_completed_at": 1681623462.0,
    "completed_at": null,
    "paused_at": null,
    "error": null,
    "stopped_at": null,
    "completed_segments": 24,
    "total_segments": 100
  }]
}
```

#### **ドキュメントの削除**

入力例：

```bash
curl --location --request DELETE 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}' \
--header 'Authorization: Bearer {api_key}'
```

出力例：

```bash
{
  "result": "success"
}
```

#### **ナレッジベースのドキュメントのリスト**

入力例：

```bash
curl --location --request GET 'https://api.dify.ai/v1/datasets/{dataset_id}/documents' \
--header 'Authorization: Bearer {api_key}'
```

出力例：

```json
{
  "data": [
    {
      "id": "",
      "position": 1,
      "data_source_type": "file_upload",
      "data_source_info": null,
      "dataset_process_rule_id": null,
      "name": "dify",
      "created_from": "",
      "created_by": "",
      "created_at": 1681623639,
      "tokens": 0,
      "indexing_status": "waiting",
      "error": null,
      "enabled": true,
      "disabled_at": null,
      "disabled_by": null,
      "archived": false
    },
  ],
  "has_more": false,
  "limit": 20,
  "total": 9,
  "page": 1
}
```

#### **新しセグメントを増加**

入力例：

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{"segments": [{"content": "1","answer": "1","keywords": ["a"]}]}'
```

出力例：

```json
{
  "data": [{
    "id": "",
    "position": 1,
    "document_id": "",
    "content": "1",
    "answer": "1",
    "word_count": 25,
    "tokens": 0,
    "keywords": [
        "a"
    ],
    "index_node_id": "",
    "index_node_hash": "",
    "hit_count": 0,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "status": "completed",
    "created_by": "",
    "created_at": 1695312007,
    "indexing_at": 1695312007,
    "completed_at": 1695312007,
    "error": null,
    "stopped_at": null
  }],
  "doc_form": "text_model"
}

```

### ドキュメントのセグメントを見つける

入力例：

```bash
curl --location --request GET 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json'
```

出力例：

```bash
{
  "data": [{
    "id": "",
    "position": 1,
    "document_id": "",
    "content": "1",
    "answer": "1",
    "word_count": 25,
    "tokens": 0,
    "keywords": [
        "a"
    ],
    "index_node_id": "",
    "index_node_hash": "",
    "hit_count": 0,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "status": "completed",
    "created_by": "",
    "created_at": 1695312007,
    "indexing_at": 1695312007,
    "completed_at": 1695312007,
    "error": null,
    "stopped_at": null
  }],
  "doc_form": "text_model"
}
```

### ドキュメントのセグメントの削除

入力例：

```bash
curl --location --request DELETE 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json'
```

出力例：

```bash
{
  "result": "success"
}
```

### ドキュメントのセグメントの更新

入力例：

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json'\
--data-raw '{"segment": {"content": "1","answer": "1", "keywords": ["a"], "enabled": false}}'
```

出力例：

```bash
{
  "data": [{
    "id": "",
    "position": 1,
    "document_id": "",
    "content": "1",
    "answer": "1",
    "word_count": 25,
    "tokens": 0,
    "keywords": [
        "a"
    ],
    "index_node_id": "",
    "index_node_hash": "",
    "hit_count": 0,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "status": "completed",
    "created_by": "",
    "created_at": 1695312007,
    "indexing_at": 1695312007,
    "completed_at": 1695312007,
    "error": null,
    "stopped_at": null
  }],
  "doc_form": "text_model"
}
```

### エラーメッセージ

| エラーメッセージ                      | エラーコード | 理由                                                                                                     |
| ----------------------------- | ------ | ------------------------------------------------------------------------------------------------------ |
| no\_file\_uploaded            | 400    | ファイルをアップロードしてください                                                                                      |
| too\_many\_files              | 400    | 1つのファイルのみアップロードできます                                                                                    |
| file\_too\_large              | 413    | ファイルサイズが制限を超えています                                                                                      |
| unsupported\_file\_type       | 415    | サポートされていないファイルタイプです。現在、以下の形式のみをサポートしています：`txt`、 `markdown`、 `md`、 `pdf`、 `html`、 `xlsx`、 `docx`、 `csv` |
| high\_quality\_dataset\_only  | 400    | 現在の操作は「高品質」のナレッジベースのみをサポートしています                                                                        |
| dataset\_not\_initialized     | 400    | ナレッジベースはまだ初期化中またはインデックス中です。お待ちください                                                                     |
| archived\_document\_immutable | 403    | アーカイブされたドキュメントは編集できません                                                                                 |
| dataset\_name\_duplicate      | 409    | ナレッジベース名がすでに存在します。ナレッジベース名を変更してください                                                                    |
| invalid\_action               | 400    | 無効な操作です                                                                                                |
| document\_already\_finished   | 400    | ドキュメントの処理がすでに完了しています。ページを更新するか、ドキュメントの詳細を確認してください                                                      |
| document\_indexing            | 400    | ドキュメントが処理中のため、編集できません                                                                                  |
| invalid\_metadata             | 400    | メタデータの内容が正しくありません。確認して検証してください                                                                         |
