# LangSmithの統合

### 1 LangSmithとは

LangSmithはLLMアプリケーションの開発、コラボレーション、テスト、デプロイ、監視などのツールを提供するプラットフォームです。

{% hint style="info" %}
LangSmithの公式サイト：[https://www.langchain.com/langsmith](https://www.langchain.com/langsmith)
{% endhint %}

***

### 2 LangSmithの使い方

#### 1. LangSmithの[公式サイト](https://www.langchain.com/langsmith)から登録し、ログインする。

#### 2. LangSmithからプロジェクトを作成します

ログイン後、ホームページの **New Project** をクリックし、新たな**プロジェクト**を作成します。このプロジェクトは、Dify内の**アプリ**と連動したデータモニタリングに使用されます。

![新たなプロジェクトを作成します。](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/58e20105fcc0771ca2431e8e5dcc42d3.png)

作成する後、プロジェクトの中にチェクできます。

![LangSmithの中にプロジェクトをチェクします。](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/642c0ff7edfdfe77fba43aa22cc3fa71.png)

#### 3. プロジェクト認証情報の作成

左のサイドバーでプロジェクト **設定** を見つける。

![プロジェクトを設定し](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/c49a1fc769215193928ff0d880422f89.png)

**Create API Key**をクリックし，新たな認証情報を作ります。

![プロジェクトのAPI Keyを作ります。](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/7082286b0d12af4bc0c84d9a3acf8b1b.png)

**Personal Access Token** を選び，のちほとのAPI身分証明の時使えます。

![Personal Access Tokenを選択します](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/75a69bd4dd02f0ffc0313589ae12fb36.png)

新たなAPI keyをコピーし、保存します。

![新たなAPI keyをコピーします](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/723e96a13e8f722d6df714b11ffd0bb1.png)

#### 4. Dify アプリの中に LangSmith を設定します

監視用のアプリのサイトメニューの**監視**ボタンをクリックし，**設定**をクリックします。

![LangSmithを設定します](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/b6c7e5d4c2ca2092d59465cca27bc69c.png)

それから，LangSmith から作った **API Key** と**プロジェクト名**を**設定**の中に貼り付け、保存します。

![ LangSmithを設定します。](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/93dfabcadb7b2ff597f54beb5e642124.png)

{% hint style="info" %}
設定したプロジェクト名は LangSmith のいるプロジェクト名と必ず一致します。一致しない場合、データの同期時に LangSmith は自動的に新しいプロジェクトを作成します。
{% endhint %}

保存に成功すると、現在のページで監視状態を見ることができます。

![監視状態を見る](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/43369dc4de8f606c166fae2efab97d73.png)

### LangSmithでのモニタリングデータの表示

Dify内のアプリケーションからデバッグや製品データを設定することで、LangSmithにてそのデータをモニタリングすることができます。

![Difyにおけるアプリケーションのデバッグ](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/a1370fdbb79257cba31a565ac6764802.png)

LangSmithに切り替えると、ダッシュボード上でDifyアプリケーションの詳細な操作ログを見ることができます。

![LangSmithでのアプリケーションデータの表示](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/2833b2ffa20927b5328e9624b065beea.png)

LangSmithを通じて得られる詳細な大規模言語モデル（LLM）の操作ログは、Difyアプリケーションのパフォーマンスを最適化するために役立ちます。

![LangSmithでのアプリケーションデータの表示](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/monitoring/integrate-external-ops-tools/beeb4ee50c80de8db7400c1f65727c8c.png)

### モニタリングデータリスト

#### ワークフロー/チャットフローのトレース情報

ワークフローやチャットフローを追跡するために使用されます。

| ワークフロー                               | LangSmith Chain               |
| ---------------------------------------- | ---------------------------   |
| workflow\_app\_log\_id/workflow\_run\_id | ID                            |
| user\_session\_id                        | - メタデータに配置               |
| workflow\_{id}                           | 名前                           |
| start\_time                              | 開始時間                        |
| end\_time                                | 終了時間                        |
| inputs                                   | 入力                           |
| outputs                                  | 出力                           |
| モデルトークン消費                          | 使用メタデータ                  |
| metadata                                 | 追加情報                       |
| エラー                                    | エラー                         |
| \[workflow]                              | タグ                           |
| "conversation\_id/none for workflow"     | メタデータ内のconversation\_id   |
| conversion\_id                           | 親実行ID                       |

**ワークフロートレース情報**

- workflow\_id：ワークフローの固有識別子
- conversation\_id：会話ID
- workflow\_run\_id：現在の実行ID
- tenant\_id：テナントID
- elapsed\_time：現在の実行にかかった時間
- status：実行ステータス
- version：ワークフローのバージョン
- total\_tokens：現在の実行で使用されるトークンの合計数
- file\_list：処理されたファイルのリスト
- triggered\_from：現在の実行を引き起こしたソース
- workflow\_run\_inputs：現在の実行の入力データ
- workflow\_run\_outputs：現在の実行の出力データ
- error：現在の実行中に発生したエラー
- query：実行中に使用されたクエリ
- workflow\_app\_log\_id：ワークフローアプリケーションログID
- message\_id：関連メッセージID
- start\_time：実行の開始時間
- end\_time：実行の終了時間
- workflow node executions：ワークフローノード実行に関する情報
- メタデータ
  - workflow\_id：ワークフローの固有識別子
  - conversation\_id：会話ID
  - workflow\_run\_id：現在の実行ID
  - tenant\_id：テナントID
  - elapsed\_time：現在の実行にかかった時間
  - status：実行ステータス
  - version：ワークフローのバージョン
  - total\_tokens：現在の実行で使用されるトークンの合計数
  - file\_list：処理されたファイルのリスト
  - triggered\_from：現在の実行を引き起こしたソース

#### メッセージトレース情報

大規模言語モデル（LLM）関連の会話を追跡するために使用されます。

| チャット                             | LangSmith LLM                |
| -------------------------------- | ---------------------------- |
| message\_id                      | ID                           |
| user\_session\_id                | - メタデータに配置         |
| “message\_{id}"                  | 名前                         |
| start\_time                      | 開始時間                     |
| end\_time                        | 終了時間                     |
| inputs                           | 入力                         |
| outputs                          | 出力                         |
| モデルトークン消費          | 使用メタデータ              |
| metadata                         | 追加情報                    |
| エラー                            | エラー                       |
| \["message", conversation\_mode] | タグ                         |
| conversation\_id                 | メタデータ内のconversation\_id |
| conversion\_id                   | 親実行ID                    |

**メッセージトレース情報**

- message\_id：メッセージID
- message\_data：メッセージデータ
- user\_session\_id：ユーザーセッションID
- conversation\_model：会話モード
- message\_tokens：メッセージ中のトークン数
- answer\_tokens：回答のトークン数
- total\_tokens：メッセージと回答の合計トークン数
- error：エラー情報
- inputs：入力データ
- outputs：出力データ
- file\_list：処理されたファイルのリスト
- start\_time：開始時間
- end\_time：終了時間
- message\_file\_data：メッセージに関連付けられたファイルデータ
- conversation\_mode：会話モード
- メタデータ
  - conversation\_id：会話ID
  - ls\_provider：モデルプロバイダ
  - ls\_model\_name：モデルID
  - status：メッセージステータス
  - from\_end\_user\_id：送信ユーザーのID
  - from\_account\_id：送信アカウントのID
  - agent\_based：メッセージがエージェントベースかどうか
  - workflow\_run\_id：ワークフロー実行ID
  - from\_source：メッセージのソース

#### モデレーショントレース情報

会話のモデレーションを追跡するために使用されます。

| モデレーション    | LangSmith Tool       |
| ------------- | -------------------- |
| user\_id      | - メタデータに配置 |
| “moderation"  | 名前                 |
| start\_time   | 開始時間             |
| end\_time     | 終了時間             |
| inputs        | 入力                 |
| outputs       | 出力                 |
| metadata      | 追加情報            |
| \[moderation] | タグ                 |
| message\_id   | 親実行ID            |

**モデレーショントレース情報**

- message\_id：メッセージID
- user\_id：ユーザーID
- workflow\_app\_log\_id：ワークフローアプリケーションログID
- inputs：モデレーションの入力データ
- message\_data：メッセージデータ
- flagged：コンテンツに注意が必要かどうか
- action：実行された具体的なアクション
- preset\_response：プリセット応答
- start\_time：モデレーション開始時間
- end\_time：モデレーション終了時間
- メタデータ
  - message\_id：メッセージID
  - action：実行された具体的なアクション
  - preset\_response：プリセット応答

#### 提案された質問トレース情報

提案された質問を追跡するために使用されます。