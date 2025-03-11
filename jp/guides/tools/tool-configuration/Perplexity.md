# Perplexity検索ツール

> ツールの作者：@Dify

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

Perplexityは、複雑なクエリを理解し、正確で関連性の高いリアルタイムの回答を提供できるAIベースの検索エンジンです。以下は、DifyでPerplexity検索ツールを設定し、使用するための手順です。

## 1. PerplexityのAPIキーを申請する

[こちら](https://www.perplexity.ai/settings/api)からAPIキーを申請し、アカウントに十分なクレジットがあることを確認してください。

## 2. Dify内で設定する

Difyのナビゲーションページで、`ツール > Perplexity > 認証する`の順にクリックし、APIキーを入力してください。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/4a67338a66101cc29205d631771bd0d6.png)

## 3. ツールの使用方法

以下のアプリケーションタイプでPerplexity検索ツールを使用できます。

- **チャットフロー / ワークフロー アプリ**

チャットフローとワークフローアプリで、Perplexityツールノードの追加がサポートされています。ユーザーの入力コンテンツは変数を介してPerplexityツールノードの「クエリ」ボックスに渡され、必要に応じてPerplexityツールの組み込みパラメータを調整します。最後に、「終了」ノードの応答ボックスでPerplexityツールノードの出力コンテンツを選択します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/4a3ae03baadb7066e6152f2ed883a582.png)

- **エージェントアプリ**

エージェントアプリに`Perplexity検索`ツールを追加し、関連するコマンドを入力してこのツールを呼び出します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/983682ddecfd6c47f04d56d44450c812.png)