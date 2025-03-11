# ツール

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

### ツール定義

ツールは、ネット検索、科学計算、画像の描画などの機能を追加し、大規模言語モデル(LLM)の能力を拡張して外部世界と接続する力を与えます。Difyは2種類のツールを提供しています：**ファーストパーティツール**と**カスタムAPIツール**です。

Difyエコシステムが提供するファーストパーティツールを直接使用することができ、また、OpenAPI/SwaggerおよびOpenAIプラグイン規格をサポートするカスタムAPIツールを簡単にインポートできます。

#### ツールの役割：

1. ツールを使用すると、Dify上でより強力なAIアプリケーションを作成できます。たとえば、エージェント型アプリケーションに適切なツールを組み合わせることで、タスク推論、ステップの分解、ツールの呼び出しを通じて複雑なタスクを完了させることができます。
2. あなたのアプリケーションを他のシステムやサービスと連携させ、外部環境と対話できるようにします。たとえば、コードの実行や専用情報源へのアクセスなどです。

### ファーストパーティツールの設定方法

![ファーストパーティツールリスト](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/20cffc5ccef7e59ca3f7e7de6fcec302.png)

Difyは現在、以下のツールをサポートしています：

<table><thead><tr><th width="154">ツール</th><th>ツールの説明</th></tr></thead><tbody><tr><td>Google検索</td><td>Google SERP検索を実行し、スニペットやウェブページを抽出するツール。入力は検索クエリであるべきです。</td></tr><tr><td>ウィキペディア</td><td>ウィキペディア検索を実行し、スニペットやウェブページを抽出するツール。</td></tr><tr><td>DALL-E</td><td>自然言語入力を通じて高品質な画像を生成するツール。</td></tr><tr><td>ウェブスクレイピング</td><td>ウェブページデータをクロールするためのツール。</td></tr><tr><td>WolframAlpha</td><td>質問に基づいた標準化された回答を提供し、強力な数学計算機能を持つ知識エンジン。</td></tr><tr><td>可視化チャート生成</td><td>棒グラフ、折れ線グラフ、円グラフなどの可視化チャートを生成するツール。</td></tr><tr><td>現在時刻</td><td>現在の時刻を問い合わせるツール。</td></tr><tr><td>Yahooファイナンス</td><td>最新のニュース、株価情報などの財務情報を取得して整理するツール。</td></tr><tr><td>Stable Diffusion</td><td>ローカルに展開可能な画像生成ツールで、stable-diffusion-webuiを使用して展開できます。</td></tr><tr><td>ベクトライザー</td><td>PNGおよびJPG画像をSVGベクトル画像に迅速かつ簡単に変換するツール。</td></tr><tr><td>YouTube</td><td>YouTubeチャンネルの動画統計データを取得するためのツール。</td></tr></tbody></table>

{% hint style="info" %}
Difyに自分で開発したツールを貢献することを歓迎します。貢献方法については[Dify開発貢献ドキュメント](https://github.com/langgenius/dify/blob/main/CONTRIBUTING.md)を確認してください。あなたのサポートは私たちにとって非常に貴重です。
{% endhint %}

#### ファーストパーティツールの認証

Difyエコシステムが提供するファーストパーティ・ビルトインツールを直接使用する場合、使用前に適切な認証情報を設定する必要があります。

![ファーストパーティツール認証情報の設定](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/67643e5b416c155a1e3af54d3c5bb136.png)

認証情報の検証が成功すると、ツールは「認証済み」の状態になります。認証情報が設定されると、ワークスペース内のすべてのメンバーがアプリケーションの編成時にこのツールを使用できます。

### カスタムツールの作成方法

「ツール - カスタムツール」内でカスタムAPIツールをインポートできます。現在、OpenAPI / SwaggerおよびChatGPTプラグイン規格をサポートしています。OpenAPIスキーマの内容を直接貼り付けるか、URLからインポートできます。OpenAPI / Swagger規格については[公式ドキュメント](https://swagger.io/specification/)を参照してください。

ツールは現在、2種類の認証方式をサポートしています：無認証とAPIキー。

![カスタムツールの作成](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/308a8b052236aad9531ce723988e8005.png)

スキーマ内容をインポートすると、システムはファイル内のパラメーターを自動的に解析し、ツールの具体的なパラメーター、方法、パスをプレビューできます。ここでツールのパラメーターをテストすることもできます。

![カスタムツールのパラメータテスト](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/7f16a89d118b94e010a71140043a912c.png)

カスタムツールの作成が完了すると、ワークスペース内のすべてのメンバーが「スタジオ」内でアプリケーションを編成する際にこのツールを使用できます。

![カスタムツールが追加されました](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/6422555dbb0735400fc66f629677d796.png)

#### Cloudflare Workers

[dify-tools-worker](https://github.com/crazywoola/dify-tools-worker)を使用してカスタムツールを迅速に展開することもできます。このツールは以下を提供します：

* Difyにインポート可能なルーティング `https://difytoolsworker.yourname.workers.dev/doc`、OpenAPI互換のインターフェイスドキュメントを提供します。
* APIの実装コードを提供し、Cloudflare Workersに直接展開できます。

### アプリ内でツールを使用する方法

現在、「スタジオ」で**エージェント型アプリケーション**を作成する際に、認証情報が設定されたツールを使用できます。

![エージェント型アプリケーション作成時にツールを追加](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/34e5fdc6118a42ffc2923d03c4ef6330.png)

以下の図のように、財務分析アプリケーションにツールを追加すると、エージェントは必要に応じてツールを自動的に呼び出し、ツールから財務報告データを取得し、それを解析してユーザーとの対話を完了します。

![エージェントが対話中にツールを呼び出して質問に回答](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/d3845b811075914c1e0b4ac9f509d7ed.png)