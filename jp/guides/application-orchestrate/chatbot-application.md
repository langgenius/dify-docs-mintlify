# チャットボット

チャットボットは、ユーザーとの継続的な対話を一問一答形式で行います。

### 適用シーン

チャットボットは、カスタマーサービス、オンライン教育、医療、金融サービスなどの分野で利用されることがあります。これらのアプリは、組織の業務の効率を向上させたり、人件費を削減したり、ユーザーエクスペリエンスを高めるのに寄与します。

### 編成方法

チャットボットの作成には、プロンプト、変数、コンテキスト、オープニングダイアログ、次の質問の提案などが含まれています。

ここでは、**面接官**用のアプリを例に使って、チャットボットの編成方法を紹介します。

#### アプリの作成

ホームページで「最初から作成」をクリックしてアプリを作成します。アプリ名を入力し、アプリタイプは**チャットボット**を選択します。

![チャットボットの作成](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/24a6f30145d5005413fa75693996377c.png)

#### アプリの編成

アプリを作成すると、自動的にアプリの概要ページに移動します。左側のメニューから編成をクリックしてアプリを編成します。

![アプリの編成](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/4332c94f126ae1ce72e1881e91d81729.png)

**プロンプトの記入**

プロンプトは、AIが専門的な回答を行う範囲を制限し、回答をより正確にします。組み込みのプロンプトジェネレータを使用して、適切なプロンプトを作成することができます。プロンプト内には、たとえば `{{input}}` のようなフォーム変数を挿入することができます。変数内の値は、ユーザーが入力した値に置き換えられます。

例：

1. インタビューシナリオの指示を入力します。
2. プロンプトが自動的に右側の内容欄に生成されます。
3. カスタム変数をプロンプトに挿入することで、特定の要望や詳細に応じてカスタマイズが可能です。

ユーザーエクスペリエンスを向上させるために、オープニングダイアログを追加することができます：`こんにちは、{{name}}さん。私はあなたの面接官、Bobです。準備はできていますか？`。ページ下部の「機能の追加」ボタンをクリックして、「オープニングダイアログ」機能を開きます

オープニングダイアログを追加する方法は、底の「機能を追加」ボタンをクリックして、「会話の開始」機能を開きます：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/8ee49c47ed4b197e77d88e95b5bf4b2a.png)

オープニングステートメントを編集する際に、いくつかのオープニング質問を追加することもできます：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/4bbcbecba6f3d826b9f7d0bf1d5e2079.png)

#### コンテキストの追加

AIの対話範囲を[ナレッジベース](../knowledge-base/)内に制限したい場合、企業内のカスタマーサービス用語規準などを「コンテキスト」で参照することができます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/dd33b25175c48bf0776ad32e10ad9f33.png)

### ファイルのアップロード

[Claude 3.5 Sonnet](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support) や [Gemini 1.5 Pro](https://ai.google.dev/api/files) など、一部のLLMはファイル処理に標準対応しています。各LLMのウェブサイトで、ファイルのアップロード機能について詳しくご確認ください。

ファイルの読み込みに対応したLLMを選択し、「Document」を有効にしてください。これにより、チャットボットは複雑な設定なしでファイルの内容を理解し、利用できるようになります。

![](https://assets-docs.dify.ai/2024/11/823399d85e8ced5068dc9da4f693170e.png)

#### デバッグ

右側にユーザー入力項目を入力し、内容を入力してデバッグします。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/58a59cfd677990426d6059008510b7ce.png)

回答結果が望ましくない場合は、プロンプトやモデルを調整することができます。また、複数のモデルを同期してデバッグすることもでき、適切な構成を組み合わせることができます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/96c97bea71df343ddc8dc013602e8a32.jpeg)

単一モデルでのデバッグが効率的ではない場合、[**「複数のモデルでのデバッグ」**](./multiple-llms-debugging.md)機能を使用して、複数のモデルの回答効果を一括確認することもできます。

#### アプリの公開

アプリのデバッグが完了したら、右上の**公開**ボタンをクリックして独立したAIアプリを生成します。公開URLを使用してアプリを体験するだけでなく、APIベースの開発やWebサイトへの組み込みなども行うことができます。詳細については[公開](../application-publishing/README.md)を参照してください。

公開されたアプリをカスタマイズしたい場合は、当社のオープンソースの[WebAppテンプレート](https://github.com/langgenius/webapp-conversation)をForkしてください。テンプレートをベースに、シチュエーションやスタイルに合わせたアプリを作成できます。

### よくある質問

**チャットボット内にサードパーティツールを追加するにはどうすればよいですか？**

チャットボットアプリは、サードパーティツールの追加をサポートしていません。[エージェント](../application-orchestrate/agent.md) 内でサードパーティツールを追加できます。
