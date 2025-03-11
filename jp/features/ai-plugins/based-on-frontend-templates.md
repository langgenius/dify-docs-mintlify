# Webアプリテンプレートに基づく

開発者がゼロから新しい製品を開発する場合、もしくは製品のプロトタイプを設計するの段階、Difyを使用して人工知能サイトを迅速に立ち上げることができます。同時に、Difyは開発者がさまざまな形式のフロントエンドアプリケーションを自由に作成できることを望んでいます。そのため、以下のものを提供しています:

* **SDK** 様々な言語でDify APIを迅速にアクセスするために使用される
* **Webアプリテンプレート** 様々アプリケーションの種類ごとにWebApp開発のフレームワーク構築するために使用される

ウェブアプリテンプレートはMITライセンスの下で公開されているオープンソースソです。difyのすべての機能を実現するために、これらを自由に修正とデプロイできます、もしくは開発者が独自のアプリケーションの参考コードとして利用もできます。

これらのテンプレートはGitHubで見つけることができます:

* [対話型アプリ](https://github.com/langgenius/webapp-conversation)
* [テキスト生成アプリ](https://github.com/langgenius/webapp-text-generator)

ウェブアプリテンプレートを使用する最も迅速な方法は、GitHubの上にある "**Use this template**" をクリックすることです。これにより、新しいリポジトリが派生されます。その後、DifyアプリケーションIDとAPIキーを設定する必要があります。例として:

```javascript
export const APP_ID = ''
export const API_KEY = ''
```

`config/index.ts`の中でさらに設定を行います:

```
export const APP_INFO: AppInfo = {
  "title": 'Chat APP',
  "description": '',
  "copyright": '',
  "privacy_policy": '',
  "default_language": 'zh-Hans'
}

export const isShowPrompt = true
export const promptTemplate = ''
```

各ウェブアプリテンプレートには、デプロイ手順が記載された Readme ファイルが付属しています。通常、ウェブアプリテンプレートには軽量なバックエンドサービスが含まれており、開発者のAPIキーがユーザーに直接公開しないようにします。

これらのウェブアプリテンプレートは、AIアプリケーションのプロトタイプを迅速に構築し、Difyのすべての機能を使用するのに役立ちます。もしこれを基に独自のアプリケーションや新たなテンプレートを開発した場合、ぜひ私たちと共有してください。
