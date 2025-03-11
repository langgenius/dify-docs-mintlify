# SearchApi

> ツールの作者：@SearchApi。

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

SearchApiは、Google検索、Google Jobs、YouTube、Googleニュースなどの検索エンジンから構造化データを提供する強力なリアルタイムのSERP APIです。以下示されましたの手順フォローし、SearchApiツールを設定する。

## 1. SearchのAPIキーを申請する

[SearchApi](https://www.searchapi.io/)のWebサイトでAPIキーを申請してください。

## 2. Dify内での設定

Difyのナビゲーションページから `ツール > SearchApi > 認証する`の順にクリックし、API キーを入力してください。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/b00563dd5a7ea62696bd435e082861e5.png)

## 3. ツールの使用方法

以下のアプリケーションタイプでSearchApiツールを使用できます。

* **チャットフロー / ワークフロー アプリ**

チャットフローとワークフローアプリでは、`SearchApi`のツールノードを追加することで、Google Jobs API、Google News API、Google Search API、YouTube Data APIの4つの異なるツールを使用可能にします。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/174ac4e16e4dc60d67aa0ddaa94b1d36.png)

* **エージェントアプリ**

エージェントアプリ内では、使用したい`SearchApi`ツールを選択し、続いてそのツールを呼び出すためのコマンドを入力してください。
