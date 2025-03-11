# Serper

> ツール作者 @zhuhao 

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

Serperは、Google検索エンジンから取得した構造化データを提供する強力なリアルタイム検索エンジンAPIです。以下示されましたの手順フォローし、Serperツールを設定する。

## 1. SerperのAPIキーを申請する

[Serperプラットフォーム](https://serper.dev/signup)にてAPIキーを申請してください。

## 2. Dify内での設定

Difyのナビゲーションページから `ツール > Serper > 認証する` をタップし、APIキーを入力してください。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/f2e06162b25b3fa295b7fd392cc3534e.png)

## 3. ツールの使用方法

Serperツールは以下のアプリケーションタイプで利用できます。

* **チャットフロー / ワークフロー アプリ**

チャットフローとワークフロー アプリに、`Serper`ツールノードを追加することができます。

* **エージェントアプリ**

エージェントアプリ内で使用する`Serper`ツールを選択し、指示を入力してツールを呼び出すことが可能です。
