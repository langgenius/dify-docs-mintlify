# Youtube

> 工具作者 @Dify

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

[Youtube](https://www.youtube.com/) は、最大のオンライン動画共有プラットフォームです。現在、Dify.ai には関連する2つのツール「Video Statistics」と「Free YouTube Transcript API」があり、URLまたはキーワードを入力することで動画情報を分析することができます。

## 1. Google Cloud サービスの使用を許可する

> アカウントをお持ちでない場合は、[Google 認証サイト](https://console.cloud.google.com/apis/credentials)にアクセスし、指示に従ってアカウントを作成してください。

アカウントをお持ちの場合は、API とサービスのページに移動し、`認証情報を作成 -> API キー`をクリックして API キーを作成します。

手順に従って操作を行い、`有効な API とサービス -> YouTube Data API v3` をクリックして YouTube Data API を有効にしてください。

![](/img/en-google-api.jpg)

## 2. Dify ツールページで YouTube API を設定する

[Dify ツールページ](https://cloud.dify.ai/tools)に戻り、YouTube API カードを開いて、ステップ1で取得した API を入力して認証を取得します。

![](/img/en-google-api.jpg)

## 3. ツールを使用する

このツールは以下のアプリケーションタイプで使用できます。

* **Chatflow / Workflow アプリケーション**

Chatflow および Workflow アプリケーションでは、`Video Statistics` ノードを追加することができます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/abaa685d6ffa5fbb8c295869eecfd721.jpeg)

* **Agent アプリケーション**

Agent アプリケーションに `Free YouTube Transcript API` ツールを追加し、関連するコマンドを入力してこのツールを呼び出します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/a5dc28b46d00cb523268bf51399476b6.png)