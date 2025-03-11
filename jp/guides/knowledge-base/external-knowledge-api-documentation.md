# 外部ナレッジベースAPI

# 外部知識API

## エンドポイント

```
POST <your-endpoint>/retrieval
```

## ヘッダー

このAPIは、Difyとは独立して開発者が維持管理するナレッジベースに接続するために使用されます。詳細については、[外部ナレッジベースへの接続](https://docs.dify.ai/guides/knowledge-base/connect-external-knowledge-base)を参照してください。`Authorization` HTTPヘッダーで `API-Key` を使用して権限を検証できます。認証ロジックは、以下のように検索APIで定義します：

```
Authorization: Bearer {API_KEY}
```

## リクエストボディ要素

リクエストは以下のJSON形式のデータを受け入れます。

| プロパティ | 必須 | 型 | 説明 | 例値 |
|------------|------|-----|------|------|
| knowledge_id | TRUE | string | ナレッジベースの一意ID | AAA-BBB-CCC |
| query | TRUE | string | ユーザーのクエリ | Difyとは何ですか？ |
| retrieval_setting | TRUE | object | 知識の検索パラメータ | 以下参照 |

`retrieval_setting` プロパティは以下のキーを含むオブジェクトです：

| プロパティ | 必須 | 型 | 説明 | 例値 |
|------------|------|-----|------|------|
| top_k | TRUE | int | 検索結果の最大数 | 5 |
| score_threshold | TRUE | float | クエリに対する結果の関連性スコアの閾値、範囲：0〜1 | 0.5 |

## リクエスト構文

```json
POST <your-endpoint>/retrieval HTTP/1.1
-- ヘッダー
Content-Type: application/json
Authorization: Bearer your-api-key
-- データ
{
    "knowledge_id": "your-knowledge-id",
    "query": "your question",
    "retrieval_setting":{
        "top_k": 2,
        "score_threshold": 0.5
    }
}
```

## レスポンス要素

アクションが成功した場合、サービスはHTTP 200レスポンスを返します。

サービスは以下のデータをJSON形式で返します。

| プロパティ | 必須 | 型 | 説明 | 例値 |
|------------|------|-----|------|------|
| records | TRUE | List[Object] | ナレッジベースのクエリ結果のレコードリスト | 以下参照 |

`records` プロパティは以下のキーを含むリストオブジェクトです：

| プロパティ | 必須 | 型 | 説明 | 例値 |
|------------|------|-----|------|------|
| content | TRUE | string | ナレッジベースのデータソースからのテキストチャンクを含む | Dify：GenAIアプリケーションのイノベーションエンジン |
| score | TRUE | float | クエリに対する結果の関連性スコア、範囲：0〜1 | 0.5 |
| title | TRUE | string | ドキュメントタイトル | Dify紹介 |
| metadata | FALSE | json | データソース内のドキュメントのメタデータ属性とその値を含む | 例参照 |

## レスポンス構文

```json
HTTP/1.1 200
Content-type: application/json
{
    "records": [{
                    "metadata": {
                            "path": "s3://dify/knowledge.txt",
                            "description": "dify知識ドキュメント"
                    },
                    "score": 0.98,
                    "title": "knowledge.txt",
                    "content": "これは外部知識のドキュメントです。"
            },
            {
                    "metadata": {
                            "path": "s3://dify/introduce.txt",
                            "description": "dify紹介"
                    },
                    "score": 0.66,
                    "title": "introduce.txt",
                    "content": "GenAIアプリケーションのイノベーションエンジン"
            }
    ]
}
```

## エラー

アクションが失敗した場合、サービスは以下のエラー情報をJSON形式で返します：

| プロパティ | 必須 | 型 | 説明 | 例値 |
|------------|------|-----|------|------|
| error_code | TRUE | int | エラーコード | 1001 |
| error_msg | TRUE | string | API例外の説明 | 無効な認証ヘッダー形式です。'Bearer <api-key>'形式が期待されます。 |

`error_code` プロパティには以下の種類があります：

| コード | 説明 |
|--------|------|
| 1001 | 無効な認証ヘッダー形式 |
| 1002 | 認証失敗 |
| 2001 | 知識が存在しません |

### HTTPステータスコード

**AccessDeniedException**
アクセス権限がないため、リクエストが拒否されました。権限を確認して再試行してください。
HTTPステータスコード：403

**InternalServerException**
内部サーバーエラーが発生しました。リクエストを再試行してください。
HTTPステータスコード：500
