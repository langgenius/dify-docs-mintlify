# シングルページWebアプリとして公開

Difyを使ってAIアプリを作成するメリットの一つは、数分でユーザー向けのWebアプリを公開できることです。このアプリはあなたのプロンプトに基づいて機能します。

* 自己ホストのオープンソース版を使用する場合、そのアプリはあなたのサーバー上で動作します
* クラウドサービスを使用する場合、そのアプリはUdify.appにホストされます

***

### AIサイトの公開

アプリ概要ページで、AIサイト（Webアプリ）に関するカードを見つけることができます。Webアプリのアクセスをオンにするだけで、ユーザーと共有できるリンクが得られます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-publishing/launch-your-webapp-quickly/56093185a61265109cee9f2e00420ff4.png)

以下の2種類のアプリには、きれいなWebアプリのインターフェースを提供しています：

* テキスト生成型（[前往预览](text-generator.md)）
* 対話型（[前往预览](conversation-application.md)）

***

### AIサイトの設定

Webアプリのカード上の**設定**ボタンをクリックすると、AIサイトのオプションをいくつか設定できます。これらは最終ユーザーに表示されます：

* アイコン
* 名前
* アプリの説明
* インターフェース言語
* 著作権情報
* プライバシーポリシーリンク
* カスタム免責事項

{% hint style="info" %}
現在サポートされているインターフェース言語：英語、中国語（簡体字）、中国語（繁体字）、ポルトガル語、ドイツ語、日本語、韓国語、ウクライナ語、ベトナム語。追加の言語が必要な場合は、GitHubでイシューを提出するか、プルリクエストを提出してコードを提供してください。[サポートを求める](../../../community/support.md)。
{% endhint %}

***

### AIサイトの埋め込み

Difyは、あなたのAIアプリをビジネスWebサイトに埋め込むことをサポートしています。この機能を使えば、数分でビジネスデータを持つ公式サイトのAIカスタマーサポートやビジネス知識Q&Aなどのアプリを作成できます。Webアプリのカード上の埋め込みボタンをクリックし、埋め込みコードをコピーして、Webサイトの目標位置に貼り付けます。

*   iframeタグの方法

    iframeコードを、AIアプリを表示するあなたのWebサイトのタグ（例：`<div>`、`<section>`）にコピーします。
*   scriptタグの方法

    scriptコードを、あなたのWebサイトの`<head>`または`<body>`タグにコピーします。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-publishing/launch-your-webapp-quickly/1e2e8c9adc620f9d6b4ea157119e8659.png)

例えば、scriptコードを公式サイトの`<body>`に貼り付けると、公式サイトのAIロボットが得られます：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-publishing/launch-your-webapp-quickly/f5a5e95e1120906669b3c1ad4e186dea.png)