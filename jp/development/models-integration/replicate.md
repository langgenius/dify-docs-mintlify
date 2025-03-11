# Replicateのオープンソースモデルを統合

DifyはReplicate上の[言語モデル](https://replicate.com/collections/language-models)と[埋め込みモデル](https://replicate.com/collections/embedding-models)に接続することができます。言語モデルはDifyの推論モデルに対応し、埋め込みモデルはDifyの埋め込みモデルに対応します。

具体的な手順は以下の通りです：

1. Replicateのアカウントが必要です（[登録ページ](https://replicate.com/signin?next=/docs)）。
2. APIキーを取得します（[取得ページ](https://replicate.com/account/api-tokens)）。
3. モデルを選択します。[言語モデル](https://replicate.com/collections/language-models)と[埋め込みモデル](https://replicate.com/collections/embedding-models)からモデルを選びます。
4. Difyの`設定 > モデルプロバイダ > Replicate`にてモデルを追加します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/12445212e76936e28dddf328c6372750.png)

APIキーは第2ステップで設定したAPIキーです。モデル名とモデルバージョンはモデルの詳細ページで見つけることができます：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/95e2ad371c82ef7ef641192f2bf1a1f8.png)
