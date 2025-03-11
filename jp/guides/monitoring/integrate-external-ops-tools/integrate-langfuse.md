# LangFuseとの統合

### Langfuseとは

LangfuseはLLMアプリケーションの開発者がデバッグ、分析、イテレーション等を使用してアプリケーションのパフォーマンスを向上させるためのツールです。

{% hint style="info" %}
Langfuseの公式サイト：[https://langfuse.com/](https://langfuse.com/)
{% endhint %}

***

### Langfuseの使い方

1. Langfuseの[公式サイト](https://langfuse.com/)から登録し、ログインする。
2. Langfuseからプロジェクトを作成します
ログイン後、ホームページの **New** をクリックし、新たな**プロジェクト**を作成します。このプロジェクトは、Dify内の**アプリ**と連動したデータモニタリングに使用されます。

![新たなプロジェクトを作成します。](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/75bed34765ed7d0e933a0069ecb094dd.png)

プロジェクトの名前を付けます。

![プロジェクトの名前を付けます。](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/26cfbb94e312a100c39e217fdd0b4406.png)

3. プロジェクト認証情報の作成のために、左のサイドバーでプロジェクト **設定** をクリックする。

![左のサイドバーをクリックします](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/2ed72a6761f2977201c29e67e5bc634c.png)

**Create API Key**をクリックし，新たな認証情報を作ります。

![プロジェクトのAPI Keyを作ります。](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/3c3fbd5392d37fbccf1f9ef76c54f0bc.png)

**Secret Key** と **Public Key，Host** をコピーし、保存します。

![APIキーの設定を取得する](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/a2ff67951ce300082d875eae8458c8c7.png)

4. Dify アプリの中に Langfuse を設定します。監視用のアプリのサイトメニューの**監視**ボタンをクリックし，**設定**をクリックします。

![Langfuseを設定します](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/ebc84b328ad37c0f6dbca6101e1f90ab.png)

それから，Langfuse から作った **Secret Key, Public Key** と **Host** を**設定**の中に貼り付け、保存します。

![Langfuseを設定します](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/5bfa409e7a073f133f21146535401512.png)

保存に成功すると、現在のページで監視状態を見ることができます。

![監視状態を見る](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/de3b4e21db7fd39b4fa4cb4d54d1079e.png)

***

### Langfuse ページで監視データをチェックします

設定した後， Difyのアプリや生産データは Langfuse の中にチェクをできます。

![Dify 内でのアプリの調整](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/a1370fdbb79257cba31a565ac6764802.png)

![Langfuseでアプリデータを見る](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/b4fc3474336d5f60dc049c9153454496.png)

***

### 監視データのリスト

#### ワークフローとチャットフローの情報を追跡

**ワークフローとチャットフローの追跡**

| Workflow                                 | LangFuse Trace          |
| ---------------------------------------- | ----------------------- |
| workflow\_app\_log\_id/workflow\_run\_id | id                      |
| user\_session\_id                        | user\_id                |
| workflow\_{id}                           | name                    |
| start\_time                              | start\_time             |
| end\_time                                | end\_time               |
| inputs                                   | input                   |
| outputs                                  | output                  |
| Model token consumption                  | usage                   |
| metadata                                 | metadata                |
| error                                    | level                   |
| error                                    | status\_message         |
| \[workflow]                              | tags                    |
| \["message", conversation\_mode]         | session\_id             |
| conversion\_id                           | parent\_observation\_id |

**Workflow Trace Info**

- workflow\_id - ワークフローのユニークID
- conversation\_id - 会話ID
- workflow\_run\_id - このランタイムのワークフローID
- tenant\_id - テナントID
- elapsed\_time - このランタイムの経過時間
- status - ランタイムのステータス
- version - ワークフローのバージョン
- total\_tokens - このランタイムで使用されたトークンの合計
- file\_list - 処理されたファイルのリスト
- triggered\_from - このランタイムをトリガしたソース
- workflow\_run\_inputs - このワークフローの入力
- workflow\_run\_outputs - このワークフローの出力
- error - エラーメッセージ
- query - ランタイムで使用されるクエリ
- workflow\_app\_log\_id - ワークフローアプリケーションログID
- message\_id - 関連するメッセージID
- start\_time - このランタイムの開始時刻
- end\_time - このランタイムの終了時刻
- workflow node executions - ワークフローノードのランタイム情報
- Metadata
  - workflow\_id - ワークフローのユニークID
  - conversation\_id - 会話ID
  - workflow\_run\_id - このランタイムのワークフローID
  - tenant\_id - テナントID
  - elapsed\_time - このランタイムの経過時間
  - status - 運用状態
  - version - ワークフローのバージョン
  - total\_tokens - このランタイムで使用されたトークンの合計
  - file\_list - 処理されたファイルのリスト
  - triggered\_from - このランタイムをトリガしたソース

#### Message Trace 情報

**LLM会話を追跡するため**

| Message                          | LangFuse Generation/Trace |
| -------------------------------- | ------------------------- |
| message\_id                      | id                        |
| user\_session\_id                | user\_id                  |
| message\_{id}                    | name                      |
| start\_time                      | start\_time               |
| end\_time                        | end\_time                 |
| inputs                           | input                     |
| outputs                          | output                    |
| Model token consumption          | usage                     |
| metadata                         | metadata                  |
| error                            | level                     |
| error                            | status\_message           |
| \["message", conversation\_mode] | tags                      |
| conversation\_id                 | session\_id               |
| conversion\_id                   | parent\_observation\_id   |

**Message Trace Info**

- message\_id - メッセージID
- message\_data - メッセージデータ
- user\_session\_id - ユーザーのセッションID
- conversation\_model - 会話モデル
- message\_tokens - メッセージトークン
- answer\_tokens - 回答トークン
- total\_tokens - メッセージと回答のトータルトークン
- error - エラーメッセージ
- inputs - 入力データ
- outputs - 出力データ
- file\_list - 処理されたファイルのリスト
- start\_time - 開始時刻
- end\_time - 終了時刻
- message\_file\_data - 関連ファイルデータのメッセージ
- conversation\_mode - 会話モード
- Metadata
  - conversation\_id - 会話ID
  - ls\_provider - モデルプロバイダ
  - ls\_model\_name - モデルID
  - status - メッセージステータス
  - from\_end\_user\_id - 送信ユーザーID
  - from\_account\_id - 送信アカウントID
  - agent\_based - エージェントベースか
  - workflow\_run\_id - このランタイムのワークフローID
  - from\_source - メッセージのソース
  - message\_id - メッセージID

#### Moderation Trace 情報

**会話モデレーションを追跡するため**

| Moderation    | LangFuse Generation/Trace |
| ------------- | ------------------------- |
| user\_id      | user\_id                  |
| moderation    | name                      |
| start\_time   | start\_time               |
| end\_time     | end\_time                 |
| inputs        | input                     |
| outputs       | output                    |
| metadata      | metadata                  |
| \[moderation] | tags                      |
| message\_id   | parent\_observation\_id   |

**Message Trace Info**

- message\_id - メッセージID
- user\_id - ユーザーID
- workflow\_app\_log\_id - ワークフローアプリケーションログID
- inputs - レビュー用の入力データ
- message\_data - メッセージデータ
- flagged - 注目対象としてフラグが立てられているか
- action - 実行すべき具体的なアクション
- preset\_response - 事前設定の応答
- start\_time - レビューの開始時刻
- end\_time - レビューの終了時刻
- Metadata
  - message\_id - メッセージID
  - action - 実行すべき具体的なアクション
  - preset\_response - 事前設定の応答

#### 提案された質問トレース情報

**提案された質問を追跡するため**

| Suggested Question     | LangFuse Generation/Trace |
| ---------------------- | ------------------------- |
| user\_id               | user\_id                  |
| suggested\_question    | name                      |
| start\_time            | start\_time               |
| end\_time              | end\_time                 |
| inputs                 | input                     |
| outputs                | output                    |
| metadata               | metadata                  |
| \[suggested\_question] | tags                      |
| message\_id            | parent\_observation\_id   |

**Message Trace Info**

* message\_id - メッセージID
* message\_data - メッセージデータ
* inputs - 入力データ
* outputs - 出力データ
* start\_time - 開始時刻
* end\_time - 終了時刻
* total\_tokens - トータルトークン
* status - メッセージの状態
* error - エラーメッセージ
* from_account_id - 送信元アカウントのID
* agent_based - エージェントベースであるかどうか
* from_source - メッセージの発信元
* model_provider - モデルの提供者
* model_id - モデルのID
* suggested_question - 提案された質問
* level - ステータスのレベル
* status_message - ステータスメッセージ
* Metadata
  * message_id - メッセージのID
  * ls_provider - モデルの提供者
  * ls_model_name - モデルの名前
  * status - メッセージの状態
  * from_end_user_id - 送信元ユーザーのID
  * from_account_id - 送信元アカウントのID
  * workflow_run_id - このランタイムにおけるワークフローのID
  * from_source - メッセージの発信元

#### Dataset Retrieval Trace 情報

**ナレッジベースの取得を追跡するために使用**

| データセットの取得 | LangFuse生成/トレース |
| ----------------- | ------------------- |
| user_id           | user_id             |
| dataset_retrieval | name                |
| start_time        | start_time          |
| end_time          | end_time            |
| inputs            | input               |
| outputs           | output              |
| metadata          | metadata            |
| \[dataset_retrieval] | tags              |
| message_id        | parent_observation_id |

**Dataset Retrieval Trace Info**

* message_id - メッセージのID
* inputs - 入力メッセージ
* documents - ドキュメントデータ
* start_time - 開始時間
* end_time - 終了時間
* message_data - 消息数据
* Metadata
  * message_id - メッセージのID
  * ls_provider - モデルの提供者
  * ls_model_name - モデルの名前
  * status - モデルの状態
  * from_end_user_id - 送信元ユーザーのID
  * from_account_id - 送信元アカウントのID
  * agent_based - エージェントベースであるかどうか
  * workflow_run_id - このランタイムにおけるワークフローのID
  * from_source - メッセージの発信元

#### Tool Trace 情報

**ツールの呼び出しを追跡するために使用**

| ツール               | LangFuse生成/トレース |
| ------------------- | ------------------- |
| user_id             | user_id             |
| tool_name           | name                |
| start_time          | start_time          |
| end_time            | end_time            |
| inputs              | input               |
| outputs             | output              |
| metadata            | metadata            |
| \["tool", tool_name] | tags              |
| message_id          | parent_observation_id |

**Tool Trace Info**

* message_id - メッセージのID
* tool_name - ツール名
* start_time - 開始時間
* end_time - 終了時間
* tool_inputs - ツールの入力
* tool_outputs - ツールの出力
* error - エラーメッセージ（存在する場合）
* inputs - メッセージの入力
* outputs - メッセージの出力
* tool_config - ツールの構成
* tool_parameters - ツールのパラメータ
* file_url - 関連ファイルのURL
* Metadata
  * message_id - メッセージのID
  * tool_name - ツール名
  * tool_inputs - ツールの入力
  * tool_outputs - ツールの出力
  * tool_config - ツールの構成
  * error - エラーメッセージ
  * tool_parameters - ツールのパラメータ
  * message_file_id - メッセージファイルのID
  * created_by_role - 作成者の役割
  * created_user_id - 作成ユーザーのID

#### Generate Name Trace 情報

**会話タイトル生成の追跡に使用**

| Generate Name     | LangFuse Generation/Trace |
| ----------------- | ------------------- |
| user_id           | user_id             |
| generate_name     | name                |
| start_time        | start_time          |
| end_time          | end_time            |
| inputs            | input               |
| outputs           | output              |
| metadata          | metadata            |
| \[generate_name]   | tags                |

**Generate Name Trace Info**

* conversation_id - 会話のID
* inputs - 入力データ
* outputs - 生成されたセッション名
* start_time - 開始時間
* end_time - 終了時間
* tenant\_id - テナントID
* Metadata
  * conversation_id - 会話のID
  * tenant\_id - テナントID
