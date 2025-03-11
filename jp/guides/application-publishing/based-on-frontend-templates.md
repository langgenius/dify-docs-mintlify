# フロントエンドテンプレートに基づいた再開発

もし開発者が新製品をゼロから開発する場合や製品プロトタイプ設計の段階にある場合、Difyを使用して迅速にAIサイトをリリースすることができます。同時に、Difyは開発者がさまざまな形式のフロントエンドアプリを自由に創造できることを望んでおり、そのため以下を提供しています：

* **SDK**：さまざまな言語でDify APIに迅速に接続するためのもの
* **WebAppテンプレート**：各種アプリケーションのためのWebApp開発用スキャフォルディング

WebAppテンプレートはMITライセンスに基づいてオープンソース化されていますので、自由に変更してデプロイすることができ、Difyのすべての機能を実現することができます。また、自分のアプリを実現するための参考コードとしても使用できます。

これらのテンプレートはGitHubで見つけることができます：

* [会話型アプリケーション](https://github.com/langgenius/webapp-conversation)
* [テキスト生成型アプリケーション](https://github.com/langgenius/webapp-text-generator)

WebAppテンプレートを使用する最も簡単な方法は、GitHubで「このテンプレートを使用」をクリックすることです。これにより、新しいリポジトリがフォークされます。その後、DifyのアプリIDとAPIキーを以下のように設定する必要があります：

````javascript
export const APP_ID = ''
export const API_KEY = ''
```

`config/index.ts`での詳細な設定：
```js
export const APP_INFO: AppInfo = {
  "title": 'Chat APP',
  "description": '',
  "copyright": '',
  "privacy_policy": '',
  "default_language": 'zh-Hans'
}

export const isShowPrompt = true
export const promptTemplate = ''
````

> アプリIDはアプリのURLの中から取得できます。URLの長い文字列の部分がユニークなアプリIDです。

各WebAppテンプレートにはREADMEファイルが含まれており、デプロイ方法の説明が記載されています。通常、WebAppテンプレートには軽量バックエンドサービスが含まれており、これは開発者のAPIキーがユーザーに直接露出しないようにするためのものです。

これらのWebAppテンプレートは、AIアプリプロトタイプを迅速に構築し、Difyのすべての機能を使用するのに役立ちます。もしこれらを基に自分のアプリや新しいテンプレートを開発した場合、ぜひ私たちと共有してください。