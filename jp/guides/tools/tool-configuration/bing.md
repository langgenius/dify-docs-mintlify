# Bing

> ツールの作者：@Dify。 

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

Bing検索ツールは、LLM（大規模言語モデル）アプリを使用する際に、インターネット検索結果を取得するのに役立ちます。以下示されましたの手順フォローし、Bing検索ツールを設定する。

## 1. BingのAPIキーを申請する

まず、[Microsoft Azure ポータル](https://platform.openai.com/)からAPIキーを取得してください。このAPIキーは、Bing検索機能にアクセスするために必要です。

## 2. Dify内で設定する

Difyのナビゲーションページで、`ツール > Bing > 認証する`の順にクリックし、API キーを入力してください。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/e460fd7a41a47061b6a4b3f0dd0f3cc6.png)

## 3. ツールの使用方法

Bing検索ツールは、以下のアプリケーションタイプで使用できます。

* **チャットフロー / ワークフロー アプリ**

チャットフローとワークフローアプリに、`Bing`ツールノードを追加することができます。

* **エージェントアプリ**

エージェントアプリに`Bing`ツールを追加し、オンライン検索の指示を入力してこのツールを呼び出すことが可能です。
