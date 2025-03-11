# Notion AI アシスタントの構築

_著者：アチョ・Dify ユーザー_

### 概要

Notionは強力な知識管理ツールです。その柔軟性と拡張性を利用し、優秀な個人ナレッジベースや共有なスペースとして利用されています。多くの人々がこれを使って知識や資料を保存し、他者と協力してアイデアの交流や新しい知識の創造を促進しています。

しかし、これらの知識はまだ自動的に現れません、ユーザーは情報を検索し、その内容を読み、有用な答えを見つける必要があります。このプロセスは特に効率的でも賢明でもありません。NotionライブラリをベースにしたAIアシスタントを持つことを想像したことがあるだろうか？このアシスタントは、ナレッジベースをレビューするだけでなく、経験豊富な執事のように交流に参加し、他の人々の質問に答えることができる、まるであなたが自分自身のNotionライブラリの主人であるかのように振る舞います。

### Notion AIアシスタントをどう実現するか？

今、[Dify](https://dify.ai/jp)を使ってこの夢を実現できます。DifyはオープンソースのLLMOps（大規模言語モデル運用）プラットフォームです。ChatGPTやClaudeなどの大規模言語モデルは、その強力な能力で世界を変えてきました。これらの強力な学習能力は、主に豊富なトレーニングデータによるものです。幸いなことに、これらは提供されたコンテンツから学び、個人のNotionライブラリから創造性を生成するのに十分なほど知能が発展しています。Difyがなければ、langchainというこれらの要素を簡略化して組み立てる抽象的な概念を理解する必要があるかもしれません。

### Difyを使って個人のAIアシスタントを作成する方法

Notion AIアシスタントのトレーニングプロセスは非常に簡単です。以下の手順に従ってください：

1. Difyにログインします。
2. データセットを作成します。
3. Notionとデータセットを接続します。
4. トレーニングを開始します。
5. 自分のAIアプリケーションを作成します。

#### 1. Difyにログイン <a href="#1-login-to-dify" id="1-login-to-dify"></a>
こちらをクリックしてDifyにログインします。GitHubまたはGoogleアカウントを使用して簡単にログインできます。

> GitHubアカウントを使用してログインする場合、この[プロジェクト](https://github.com/langgenius/dify)にスターを付けてください。それが私たちにとって大きなサポートになります！

![login-1](https://pan.wsyfin.com/f/ERGcp/login-1.png)

#### 2. 新しいデータセットを作成 <a href="#2-create-a-new-datasets" id="2-create-a-new-datasets"></a>
トップサイドバーの「Knowledge」ボタンをクリックし、「Create Knowledge」ボタンをクリックします。

![login-2](https://pan.wsyfin.com/f/G6ziA/login-2.png)

#### 3. Notionとデータセットを接続 <a href="#3-connect-with-notion-and-datasets" id="3-connect-with-notion-and-datasets"></a>
「Sync from Notion」を選択し、「Connect」ボタンをクリックします。

![connect-with-notion-1](https://pan.wsyfin.com/f/J6WsK/connect-with-notion-1.png)

その後、Notionのログインページにリダイレクトされます。Notionアカウントを使用してログインします。

![connect-with-notion-2](https://pan.wsyfin.com/f/KrEi4/connect-with-notion-2.png)

Difyが必要とする権限を確認し、「選択ページ」ボタンをクリックします。

![connect-with-notion-3](https://pan.wsyfin.com/f/L91iQ/connect-with-notion-3.png)

Difyと同期するページを選択し、「アクセスを許可」ボタンをクリックします。

![connect-with-notion-4](https://pan.wsyfin.com/f/M8Xtz/connect-with-notion-4.png)

#### 4. トレーニングを開始 <a href="#4-start-training" id="4-start-training"></a>
AIがNotion内のこの部分の内容を理解できるように、学習させるページを指定します。次に、「次へ」ボタンをクリックします。

![train-1](https://pan.wsyfin.com/f/Nkjuj/train-1.png)

AIアシスタントをトレーニングするために「自動」および「高品質」オプションを選択することをお勧めします。その後、「保存して処理」ボタンをクリックします。

![train-2](https://pan.wsyfin.com/f/OYoCv/train-2.png)

数秒待ち、埋め込み処理が完了するのを待ちます。

![train-3](https://pan.wsyfin.com/f/PN9F3/train-3.png)

#### 5. 自分のAIアプリケーションを作成 <a href="#5-create-your-own-ai-application" id="5-create-your-own-ai-application"></a>
AIアプリケーションを作成し、先ほど作成したデータセットを接続する必要があります。ダッシュボードに戻り、「新しいアプリを作成」ボタンをクリックします。チャットアプリを直接使用することをお勧めします。

![create-app-1](https://pan.wsyfin.com/f/QWRHo/create-app-1.png)

「Prompt Eng.」を選択し、「context」にNotionデータセットを追加します。

![create-app-2](https://pan.wsyfin.com/f/R6DT5/create-app-2.png)

AIアプリケーションに「プリセットプロンプト」を追加することをお勧めします。ハリー・ポッターにとって呪文が不可欠なように、特定のツールや機能はAIアプリケーションの能力を大いに強化します。

例えば、Notionノートが主にソフトウェア開発における問題解決に焦点を当てている場合、以下のようなプロンプトを一つ追加できます：

> 私のNotionワークスペース内でITの専門家として振る舞い、コンピュータサイエンス、ネットワークインフラ、Notionノート、ITセキュリティに関する知識を活用して問題を解決してほしい。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/27f353c0cc454912205d0acdc1aed51f.png)

初期設定では、AIがユーザーに開始文を提供し、質問の手がかりを与えるようにすることをお勧めします。また、「音声からテキストへの変換」機能を有効にして、ユーザーがAIアシスタントと音声でやり取りできるようにします。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/cf3649fe8bffaa76a86d71daa8ec0afb.png)

今や「概要」で公開URLをクリックして、自分のAIアシスタントとチャットできるようになりました！

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/3830bbae27580f32cc415340984cb4e9.png)

### APIを通じてプロジェクトに統合

Difyで作成されたすべてのAIアプリケーションは、そのAPIを通じてアクセスできます。この方法により、開発者はフロントエンドアプリケーション内で強力な大規模言語モデル（LLM）の特性を直接活用でき、真の「バックエンド as a サービス」（BaaS）体験を提供します。

シームレスなAPI統合を通じて、複雑な設定なしにNotion AIアプリケーションを簡単に呼び出すことができます。

概要ページで「APIリファレンス」ボタンをクリックします。これをアプリケーションのAPIドキュメントとして参照できます。

![using-api-1](https://pan.wsyfin.com/f/wp0Cy/using-api-1.png)

#### 1. APIキーを生成 <a href="#1-generate-api-secret-key" id="1-generate-api-secret-key"></a>
セキュリティのため、AIアプリケーションにアクセスするためのAPIキーを生成することをお勧めします。

![using-api-2](https://pan.wsyfin.com/f/xk2Fx/using-api-2.png)

#### 2. セッションIDを取得 <a href="#2-retrieve-conversation-id" id="2-retrieve-conversation-id"></a>
AIアプリケーションとチャットした後、「ログ＆アナウンス」ページからセッションIDを取得できます。

![using-api-3](https://pan.wsyfin.com/f/yPXHL/using-api-3.png)

#### 3. APIを呼び出し <a href="#3-invoke-api" id="3-invoke-api"></a>
APIドキュメントでサンプルリクエストコードを実行して、ターミナルでAIアプリケーションを呼び出すことができます。

コード中のSECRET KEYとconversation\_idを置き換えることを忘れないでください。

最初は空のconversation\_idを入力し、応答に含まれるconversation\_idを受け取った後にそれを置き換えます。

```
curl --location --request POST 'https://api.dify.ai/v1/chat-messages' \
--header 'Authorization: Bearer ENTER-YOUR-SECRET-KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "query": "eh",
    "response_mode": "streaming",
    "conversation_id": "",
    "user": "abc-123"
}'
```

ターミナルでリクエストを送信すると、成功した応答が得られます。

![using-api-4](https://pan.wsyfin.com/f/zpnI4/using-api-4.png)

このチャットを続けたい場合、リクエストコードの`conversation_id`を応答から得た`conversation_id`に置き換えます。

`"ログ＆アナウンス"`ページで全ての会話記録を確認できます。

![using-api-5](https://pan.wsyfin.com/f/ADQSE/using-api-5.png)

### 周期的にNotionと同期

Notionページが更新された場合、Difyと定期的に同期して、AIアシスタントを最新の状態に保つことができます。AIアシスタントは新しいコンテンツから学び、新しい質問に答えることができます。

![create-app-5](https://pan.wsyfin.com/f/XDBfO/create-app-5.png)

### まとめ

このチュートリアルでは、NotionデータをDifyにインポートする方法だけでなく、APIを使用してプロジェクトに統合する方法も学びました。

Difyは、持続可能なAIネイティブアプリケーションをより多くの人々が作成できるように設計されたユーザーフレンドリーなLLMOpsプラットフォームです。さまざまなアプリケーションタイプに対して設計された可視化オーケストレーションを提供し、データを活用して独自のAIアシスタントを作成するためのアプリケーションを提供しています。質問がある場合は、いつでもご連絡ください。
