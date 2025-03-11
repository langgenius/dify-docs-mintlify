# Opikの統合

## Opikの概要

Opikは、大規模言語モデル（LLM）アプリケーションを評価、テスト、および監視するためのオープンソースプラットフォームです。LLMベースのアプリケーション開発において、直感的な評価・テスト・監視機能を提供し、開発効率の向上を支援します。

{% hint style="info" %}
詳細については、[Opik](https://www.comet.com/site/products/opik/)をご参照ください。
{% endhint %}

---

## Opikの導入ガイド

### 1. [Opik](https://www.comet.com/signup?from=llm) に登録/ログイン

### 2. Opik APIキーの取得

右上のユーザーメニューから**API Key**を選択し、APIキーを取得・コピーしてください。

![Opik APIキー](https://assets-docs.dify.ai/2025/01/a66603f01e4ffaa593a8b78fcf3f8204.png)

### 3. OpikとDifyを統合

DifyアプリケーションでOpikを設定します。監視するアプリケーションを開き、サイドメニューで**監視**を選択し、ページ上の**アプリケーションパフォーマンスを追跡**をクリックします。

![アプリケーションパフォーマンスを追跡](https://assets-docs.dify.ai/2025/01/9d52a244e3b6cef1874ee838cd976111.png)

設定後、Opikで作成した**API Key**と**プロジェクト名**を設定ページに貼り付けて保存します。

![Opikの設定](https://assets-docs.dify.ai/2025/01/7f4c436e2dc9fe94a3ed49219bb3360c.png)

保存に成功すると、現在のページで監視ステータスを確認できます。

## 監視データの確認

設定が完了すると、Difyアプリケーションを通常通りデバッグまたは使用できます。すべての使用履歴はOpikで監視可能です。

![Opikでアプリデータを確認](https://assets-docs.dify.ai/2025/01/a1c5aa80325e6d0223d48a178393baec.png)

Opikに切り替えると、ダッシュボードでDifyアプリケーションの詳細な操作ログを確認できます。

![Opikでアプリデータを確認](https://assets-docs.dify.ai/2025/01/09601d45eaf8ed90a4dfb07c34de36ff.png)

Opikの詳細なLLM操作ログにより、Difyアプリケーションのパフォーマンスを最適化できます。

![Opikでアプリデータを確認](https://assets-docs.dify.ai/2025/01/708533b4fc616f852b5601fe602e3ef5.png)

## モニタリングデータリスト

### **ワークフロー/会話フロートラッキング情報**

**ワークフローと会話フローの追跡に使用**

| ワークフロー                           | Opikトラッキング             |
| ------------------------------------ | --------------------------- |
| workflow_app_log_id/workflow_run_id | id                          |
| user_session_id                     | - メタデータに配置            |
| workflow\_{id}                      | name                        |
| start_time                          | start_time                  |
| end_time                            | end_time                    |
| inputs                              | inputs                      |
| outputs                             | outputs                     |
| モデルトークン消費                     | usage_metadata              |
| metadata                            | metadata                    |
| error                               | error                       |
| \[workflow]                         | tags                        |
| "conversation_id/none for workflow" | conversation_id in metadata |

**ワークフロートラッキング情報**

- workflow_id - ワークフローの一意識別子
- conversation_id - 会話ID
- workflow_run_id - 現在の実行ID
- tenant_id - テナントID
- elapsed_time - 現在の実行にかかった時間
- status - 実行ステータス
- version - ワークフローバージョン
- total_tokens - 現在の実行で使用されたトークン総数
- file_list - 処理されたファイルのリスト
- triggered_from - 実行をトリガーしたソース
- workflow_run_inputs - 現在の実行の入力データ
- workflow_run_outputs - 現在の実行の出力データ
- error - 実行中に発生したエラー
- query - 実行中に使用されたクエリ
- workflow_app_log_id - ワークフローアプリケーションログID
- message_id - 関連するメッセージID
- start_time - 実行開始時間
- end_time - 実行終了時間
- workflow node executions - ワークフローノードの実行情報
- メタデータ
  - workflow_id - ワークフローの一意識別子
  - conversation_id - 会話ID
  - workflow_run_id - 現在の実行ID
  - tenant_id - テナントID
  - elapsed_time - 現在の実行にかかった時間
  - status - 実行ステータス
  - version - ワークフローバージョン
  - total_tokens - 現在の実行で使用されたトークン総数
  - file_list - 処理されたファイルのリスト
  - triggered_from - 実行をトリガーしたソース

---

### **メッセージトラッキング情報**

**LLM関連の会話を追跡するために使用**

| チャット                           | Opik LLM                   |
| -------------------------------- | -------------------------- |
| message_id                       | id                         |
| user_session_id                  | - メタデータに配置           |
| "llm"                            | name                       |
| start_time                       | start_time                 |
| end_time                         | end_time                   |
| inputs                           | inputs                     |
| outputs                          | outputs                    |
| モデルトークン消費                 | usage_metadata             |
| metadata                         | metadata                   |
| \["message", conversation_mode]  | tags                       |
| conversation_id                  | conversation_id in metadata |

**メッセージトラッキング情報**

- message_id - メッセージID
- message_data - メッセージデータ
- user_session_id - ユーザーセッションID
- conversation_model - 会話モード
- message_tokens - メッセージ内のトークン数
- answer_tokens - 回答内のトークン数
- total_tokens - メッセージと回答のトークン総数
- error - エラー情報
- inputs - 入力データ
- outputs - 出力データ
- file_list - 処理されたファイルリスト
- start_time - 開始時間
- end_time - 終了時間
- message_file_data - メッセージ関連のファイルデータ
- conversation_mode - 会話モード
- メタデータ
  - conversation_id - 会話ID
  - ls_provider - モデルプロバイダー
  - ls_model_name - モデルID
  - status - メッセージステータス
  - from_end_user_id - 送信ユーザーID
  - from_account_id - 送信アカウントID
  - agent_based - エージェントベースかどうか
  - workflow_run_id - ワークフロー実行ID
  - from_source - メッセージソース

### **レビュー追跡情報**

**会話のレビューを追跡するために使用**

| レビュー         | Opik Tool        |
| ---------------- | ---------------- |
| user_id          | - メタデータに配置 |
| "moderation"     | name             |
| start_time       | start_time       |
| end_time         | end_time         |
| inputs           | inputs           |
| outputs          | outputs          |
| metadata         | metadata         |
| \["moderation"]  | tags             |

**レビュー追跡情報**

- message_id - メッセージID
- user_id - ユーザーID
- workflow_app_log_id - ワークフローアプリケーションログID
- inputs - レビュー入力データ
- message_data - メッセージデータ
- flagged - 注意が必要とマークされたかどうか
- action - 実施された具体的なアクション
- preset_response - プリセットレスポンス
- start_time - レビュー開始時間
- end_time - レビュー終了時間
- メタデータ
  - message_id - メッセージID
  - action - 実施されたアクション
  - preset_response - プリセットレスポンス

---

### **提案質問追跡情報**

**提案質問を追跡するために使用**

| 提案質問               | Opik LLM         |
| --------------------- | ---------------- |
| user_id               | - メタデータに配置 |
| "suggested_question"  | name             |
| start_time            | start_time       |
| end_time              | end_time         |
| inputs                | inputs           |
| outputs               | outputs          |
| metadata              | metadata         |
| \["suggested_question"] | tags            |

**提案質問追跡情報**

- message_id - メッセージID
- message_data - メッセージデータ
- inputs - 入力データ
- outputs - 出力データ
- start_time - 開始時間
- end_time - 終了時間
- total_tokens - トークン総数
- status - メッセージステータス
- error - エラー情報
- from_account_id - 送信アカウントID
- agent_based - エージェントベースかどうか
- from_source - メッセージの送信元
- model_provider - モデルプロバイダー
- model_id - モデルID
- suggested_question - 提案された質問
- level - ステータスレベル
- status_message - ステータスメッセージ
- メタデータ
  - message_id - メッセージID
  - ls_provider - モデルプロバイダー
  - ls_model_name - モデルID
  - status - メッセージステータス
  - from_end_user_id - 送信ユーザーID
  - from_account_id - 送信アカウントID
  - workflow_run_id - ワークフロー実行ID
  - from_source - メッセージの送信元

---

### **データセット検索追跡情報**

**ナレッジベース検索を追跡するために使用**

| データセット検索      | Opik Retriever    |
| ------------------- | ----------------- |
| user_id             | - メタデータに配置 |
| "dataset_retrieval" | name              |
| start_time          | start_time        |
| end_time            | end_time          |
| inputs              | inputs            |
| outputs             | outputs           |
| metadata            | metadata          |
| \["dataset_retrieval"] | tags            |
| message_id          | parent_run_id     |

**データセット検索追跡情報**

- message_id - メッセージID
- inputs - 入力データ
- documents - ドキュメントデータ
- start_time - 開始時間
- end_time - 終了時間
- message_data - メッセージデータ
- メタデータ
  - message_id - メッセージID
  - ls_provider - モデルプロバイダー
  - ls_model_name - モデルID
  - status - メッセージステータス
  - from_end_user_id - 送信ユーザーID
  - from_account_id - 送信アカウントID
  - agent_based - エージェントベースかどうか
  - workflow_run_id - ワークフロー実行ID
  - from_source - メッセージの送信元

---

### **ツール追跡情報**

**ツールの呼び出しを追跡するために使用**

| ツール               | Opik Tool        |
| ------------------- | ---------------- |
| user_id            | - メタデータに配置 |
| tool_name          | name             |
| start_time         | start_time       |
| end_time           | end_time         |
| inputs             | inputs           |
| outputs            | outputs          |
| metadata           | metadata         |
| \["tool", tool_name] | tags            |

**ツール追跡情報**

- message_id - メッセージID
- tool_name - ツール名
- start_time - 開始時間
- end_time - 終了時間
- tool_inputs - ツール入力
- tool_outputs - ツール出力
- message_data - メッセージデータ
- error - エラー情報（該当する場合）
- inputs - メッセージの入力
- outputs - メッセージの出力
- tool_config - ツール設定
- time_cost - 時間コスト
- tool_parameters - ツールパラメーター
- file_url - 関連するファイルのURL
- メタデータ
  - message_id - メッセージID
  - tool_name - ツール名
  - tool_inputs - ツール入力
  - tool_outputs - ツール出力
  - tool_config - ツール設定
  - time_cost - 時間コスト
  - error - エラー情報（該当する場合）
  - tool_parameters - ツールパラメーター
  - message_file_id - メッセージファイルID
  - created_by_role - 作成者の役割
  - created_user_id - 作成者ユーザーID
