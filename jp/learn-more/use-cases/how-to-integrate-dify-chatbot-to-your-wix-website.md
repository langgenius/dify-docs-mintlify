# DifyチャットボットをWixサイトに統合する方法

Wixは人気のWebサイト作成プラットフォームです。ドラッグ・アンド・ドロップを使用して、ユーザーがWebサイトを視覚的にデザインできます。Wixのiframeコード機能を活用することで、DifyチャットボットをWixサイトにシームレスに統合できます。

この機能はチャットボットの統合だけでなく、外部のサーバーや他のソースからのコンテンツをWixページに表示することもできます。例えば、天気ウィジェット、株価ティッカー、カレンダー、またはカスタムウェブ要素などがあります。

このガイドでは、iframeコードを使用してDifyチャットボットをWixWebサイトに埋め込む手順を説明します。この方法は他のWebサイト、ブログ、またはウェブページにDifyアプリケーションを統合する際にも適用できます。

## 1. DifyアプリケーションのiFrameコードスニペットを取得する

すでに[Dify AIアプリケーション](https://docs.dify.ai/v/ja-jp/guides/application-orchestrate/creating-an-application)を作成していると仮定し、以下の手順に従ってiFrameコードスニペットを取得してください：

1. Difyアカウントにログインします。
2. 埋め込みたいDifyアプリケーションを選択します。
3. ページ右上の「公開」ボタンをクリックします。
4.  公開ページで「サイトに埋め込む」のオプションを選択します。

    ![サイトに埋め込む](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/238daf21d6632d7d20cc9a6b882194f9.png)
5.  適切なスタイルを選択し、表示されるiFrameコードをコピーします。例：

    ![iFrameコード例](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/ebab9e1f734d80e793db3675a46099fb.png)

## 2. iFrameコードスニペットをWixサイトに埋め込む

1. WixWebサイトにログインし、編集したいページを開きます。
2. ページの左側にある青い`+`（要素の追加）ボタンをクリックします。
3.  **埋め込みコード**を選択し、**HTMLを埋め込む**をクリックして、ページにHTML iFrame要素を追加します。

    ![HTML iFrameを追加](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/43b79d103da8beb69619e8f122609b89.png)
4. `HTML設定`ボックスで、`コード`オプションを選択します。
5. Difyアプリケーションから取得したiFrameコードスニペットを貼り付けます。
6. **更新**ボタンをクリックして変更内容を保存し、プレビューします。

以下はDifyチャットボットを埋め込むためのiFrameコードスニペットの例です：

```bash
<iframe src="https://udify.app/chatbot/ez1pf83HVV3JgWO4" style="width: 100%; height: 100%; min-height: 700px" frameborder="0" allow="microphone"></iframe>
```

![Dify iFrameコードを挿入](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/fb257be087645aaa5eb2ae01a4a15d8d.png)

> ⚠️ iFrameコード内のアドレスがHTTPSで始まることを確認してください。HTTPアドレスは正しく表示されません。

## 3. Difyチャットボットのカスタマイズ

Difyチャットボットのボタンスタイル、位置、その他の設定を調整することができます。

### 3.1 スタイルのカスタマイズ

iFrameコード内の`style`属性を変更することで、チャットボットボタンの外観をカスタマイズできます。例：

```bash
<iframe src="https://udify.app/chatbot/ez1pf83HVV3JgWO4" style="width: 100%; height: 100%; min-height: 700px" frameborder="0" allow="microphone"></iframe>

# 幅2ピクセルの実線の黒い境界線を追加：border: 2px solid #000

→

<iframe src="https://udify.app/chatbot/ez1pf83HVV3JgWO4" style="width: 80%; height: 80%; min-height: 500px; border: 2px solid #000;" frameborder="0" allow="microphone"></iframe>
```

このコードは、チャットボットインターフェースに幅2ピクセルの実線の黒い境界線を追加します。

### 3.2 位置のカスタマイズ

`style`属性内の`position`値を変更することで、ボタンの位置を調整できます。例：

```bash
<iframe src="https://udify.app/chatbot/ez1pf83HVV3JgWO4" style="width: 100%; height: 100%; min-height: 700px" frameborder="0" allow="microphone"></iframe>

# ページの右下隅にチャットボットを固定し、下端と右端から20ピクセルの位置に配置

→

<iframe src="https://udify.app/chatbot/ez1pf83HVV3JgWO4" style="width: 100%; height: 100%; min-height: 700px; position: fixed; bottom: 20px; right: 20px;" frameborder="0" allow="microphone"></iframe>
```

このコードは、ページの右下隅にチャットボットを固定し、下端と右端から20ピクセルの位置に配置します。

## よくある質問

**1. iFrameのコンテンツが表示されない**

* URLがHTTPSで始まっていることを確認してください。
* `iframe`コードに誤字がないか確認してください。
* 埋め込まれたコンテンツがWixのセキュリティポリシーに準拠しているか確認してください。

**2. iFrameのコンテンツが切り取られて表示される**

`iframe`コード内の`width`と`height`のパーセンテージ値を変更することで、コンテンツの切り取り問題を解決できます。
