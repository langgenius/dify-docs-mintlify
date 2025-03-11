# AlphaVantage 株式分析ツール

> ツール作者 [@zhuhao](https://github.com/hwzhuhao)。

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

AlphaVantageは、金融市場のデータとAPIを提供する包括的なオンラインプラットフォームであり、個人投資家や開発者が株価、テクニカル指標、そして詳細な株式分析に簡単にアクセスできるようにします。DifyはAlphaVantageツールを統合しており、以下示されましたの手順フォローし、AlphaVantageツールを設定する。

## 1. AlphaVantageのAPIキーを申請する

[AlphaVantage](https://www.alphavantage.co/support/#api-key)から API キーを申請してください。

## 2. Dify内で設定する

Difyのダッシュボードで、`ツール > AlphaVantage > 認証する`の順にクリックし、API キーを入力してください。

## 3. ツールの使用方法

- **チャットフロー / ワークフロー アプリ**

チャットフローとワークフローアプリには、`AlphaVantage`ノードの統合がサポートされています。ノードを追加後、[変数](https://docs.dify.ai/v/ja-jp/guides/workflow/variables)を利用して、`入力変数 → 株式コード`フィールドにおけるユーザーの入力クエリを参照します。"終了" ノードでは、変数を使用して`AlphaVantage`ノードの出力を参照します。

- **エージェントアプリ**

`AlphaVantage`ツールをエージェントアプリに統合します。ユーザーはチャットインターフェースで株式コードや一般的な株式の説明を入力し、このツールをトリガーして正確な財務データを取得します。