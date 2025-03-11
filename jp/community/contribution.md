# 貢献者になる

Difyに貢献したいと思っていることには素晴らしいと思います。私たちはあなたの貢献を心待ちにしております。スタッフも資金も限られた新興企業として、私たちはLLMアプリケーションの構築と管理のための最も直感的なワークフローを設計するという野心的な目標を持っています。そのため、コミュニティからのあらゆるサポートは貴重です。

我々の現状を考えると、柔軟かつ迅速に更新する必要がありますが、貢献者がスムーズに貢献できるようにしたいとも考えています。そのために、この貢献ガイドを作成しました。このガイドは、あなたがコードベースに慣れ、貢献者としての活動を迅速に開始できるようにすることを目的としています。

このガイドは、Dify自体と同様に、常に改善されています。時折プロジェクトの実態よりも遅れることがあるかもしれませんが、ご理解と改善のためのフィードバックを心から歓迎します。

ライセンスに関しては、時間を取って短い[ライセンスと貢献者協定](https://github.com/langgenius/dify/blob/main/LICENSE)を読んでください。また、コミュニティは[行動規範](https://github.com/langgenius/.github/blob/main/CODE_OF_CONDUCT.md)にも従います。

## 始める前に

[既存のイシューを探す](https://github.com/langgenius/dify/issues?q=is:issue+is:closed)か、新しいイシューを[作成する](https://github.com/langgenius/dify/issues/new/choose)ことができます。イシューは次の2つのカテゴリに分かれます：

### 機能リクエスト：

* 新しい機能リクエストを行う場合は、提案する機能の目的を説明し、できるだけ詳細なコンテキストを提供してください。[@perzeusss](https://github.com/perzeuss)が作成した優れた[機能リクエスト助手](https://udify.app/chat/MK2kVSnw1gakVwMX)を使ってドラフトを作成することもできます。ぜひ試してみてください。

* 既存のイシューから選びたい場合は、その下にコメントを残して意思を示してください。

関連するチームメンバーが関与します。うまくいけば、彼らがコーディングを開始することを承認します。それまでは、変更が提案される可能性があるため、作業を開始しないでください。

提案された機能が属する領域に応じて、異なるチームメンバーと連携する必要があります。以下は、各チームメンバーが現在取り組んでいる分野の概要です：

  | Member                                                       | Scope                                                |
  | ------------------------------------------------------------ | ---------------------------------------------------- |
  | [@yeuoly](https://github.com/Yeuoly)                         | Architecting Agents                                  |
  | [@jyong](https://github.com/JohnJyong)                       | RAG pipeline design                                  |
  | [@GarfieldDai](https://github.com/GarfieldDai)               | Building workflow orchestrations                     |
  | [@iamjoel](https://github.com/iamjoel) & [@zxhlyh](https://github.com/zxhlyh) | Making our frontend a breeze to use                  |
  | [@guchenhe](https://github.com/guchenhe) & [@crazywoola](https://github.com/crazywoola) | Developer experience, points of contact for anything |
  | [@takatost](https://github.com/takatost)                     | Overall product direction and architecture           |

  優先順位の判定ルール：

| Feature Type                                                 | Priority        |
| ------------------------------------------------------------ | --------------- |
| High-Priority Features as being labeled by a team member     | High Priority   |
| Popular feature requests from our [community feedback board](https://github.com/langgenius/dify/discussions/categories/ideas) | Medium Priority |
| Non-core features and minor enhancements                     | Low Priority    |
| Valuable but not immediate                                   | Future-Feature  |

### その他（例えばバグ報告、パフォーマンス向上、タイポ修正）：
* すぐにコーディングを開始してください。

  優先順位の判定ルール：

  | Issue Type                                                   | Priority        |
  | ------------------------------------------------------------ | --------------- |
  | Bugs in core functions (cannot login, applications not working, security loopholes) | Critical        |
  | Non-critical bugs, performance boosts                        | Medium Priority |
  | Minor fixes (typos, confusing but working UI)                | Low Priority    |


## インストール

以下はDifyを開発用に設定する手順です：

### 1. リポジトリをフォークする

### 2. リポジトリをクローンする

ターミナルからフォークしたリポジトリをクローンします：

```
git clone git@github.com:<github_username>/dify.git
```

### 3. 依存関係を確認する

Difyは以下のツールとライブラリに依存しています：

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Node.js v18.x (LTS)](http://nodejs.org)
- [npm](https://www.npmjs.com/) バージョン 8.x.x もしくは [Yarn](https://yarnpkg.com/)
- [Python](https://www.python.org/) バージョン 3.10.x

### 4. インストール

Difyはバックエンドとフロントエンドで構成されています。`cd api/`を使ってバックエンドディレクトリに移動し、次は[バックエンドREADME](https://github.com/langgenius/dify/blob/main/api/README.md)に従ってインストールして下さい。別のターミナルで`cd web/`を使ってフロントエンドディレクトリに移動し、そして[フロントエンドREADME](https://github.com/langgenius/dify/blob/main/web/README.md)に従ってインストールして下さい。

一般的な問題とトラブルシューティングの手順については[インストールFAQ](https://docs.dify.ai/v/ja-jp/learn-more/faq/install-faq)を参照してください。

### 5. ブラウザでDifyにアクセスする

設定を確認するため、ブラウザを開き[http://localhost:3000](http://localhost:3000)（デフォルトまたはカスタムURLとポート）にアクセスします。これでDifyが動作しているはずです。

## 開発

モデルを追加提供する場合は、[このガイド](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/README.md)を参照してください。

エージェントやワークフローにツールを追加提供する場合は、[このガイド](https://github.com/langgenius/dify/blob/main/api/core/tools/README.md)を参照してください。

> 注意点：新しいツールを提供したい場合は、必ずツールの YAML 説明ページに連絡先を残し、ドキュメント[Dify-docs](https://github.com/langgenius/dify-docs/tree/main/en/guides/tools/tool-configuration) のコードリポジトリに対応するPRを提出してください。

貢献する部分を迅速に理解できるように、以下にDifyのバックエンドとフロントエンドの簡単な注釈付きアウトラインを示します：

### バックエンド

DifyのバックエンドはPythonで書かれており、[Flask](https://flask.palletsprojects.com/en/3.0.x/)フレームワークを使用しています。[SQLAlchemy](https://www.sqlalchemy.org/)をORMとして使用し、[Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)をタスクキューとして使用しています。認証ロジックはFlask-loginで処理されます。

```
[api/]
├── constants             // コードベース全体で使用される定数設定。
├── controllers           // APIルート定義とリクエスト処理ロジック。           
├── core                  // コアアプリケーションオーケストレーション、モデル統合、ツール。
├── docker                // Dockerおよびコンテナ化関連の設定。
├── events                // イベント処理と処理
├── extensions            // サードパーティフレームワーク/プラットフォームとの拡張機能。
├── fields                // シリアライズ/マーシャリングのためのフィールド定義。
├── libs                  // 再利用可能なライブラリとヘルパー。
├── migrations            // データベース移行のためのスクリプト。
├── models                // データベースモデルとスキーマ定義。
├── services              // ビジネスロジックを指定。
├── storage               // 秘密鍵保管。      
├── tasks                 // 非同期タスクとバックグラウンドジョブの処理。
└── tests
```

### フロントエンド

このWebサイトは[Next.js](https://nextjs.org/)テンプレートを使用しており、スタイリングには[Tailwind CSS](https://tailwindcss.com/)を使用しています。[React-i18next](https://react.i18next.com/)を国際化に使用しています。

```
[web/]
├── app                   // レイアウト、ページ、およびコンポーネント
│   ├── (commonLayout)    // アプリ全体で使用される共通レイアウト
│   ├── (shareLayout)     // トークン固有のセッション間で共有されるレイアウト 
│   ├── activate          // アクティベートページ
│   ├── components        // ページとレイアウトで共有されるコンポーネント
│   ├── install           // インストールページ
│   ├── signin            // サインインページ
│   └── styles            // グローバルに共有されるスタイル
├── assets                // 静的アセット
├── bin                   // ビルドステップで実行されるスクリプト
├── config                // 調整可能な設定とオプション 
├── context               // アプリの異なる部分で使用される共有コンテキスト
├── dictionaries          // 言語固有の翻訳ファイル 
├── docker                // コンテナ設定
├── hooks                 // 再利用可能なフック
├── i18n                  // 国際化設定
├── models                // データモデルとAPIレスポンスの形状を記述
├── public                // ファビコンなどのメタアセット
├── service               // APIアクションの形状を指定
├── test                  
├── types                 // 関数パラメータと戻り値の記述
└── utils                 // 共有ユーティリティ関数
```

## PRを提出する

最後に、私たちのリポジトリにプルリクエスト（PR）を提出する時が来ました。重要な機能の場合、最初に `deploy/dev` ブランチにマージしてテストを行い、その後 `main` ブランチにマージします。マージコンフリクトが発生した場合や、プルリクエストの提出方法が分からない場合は、[GitHubのプルリクエストチュートリアル](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)を参照してください。

これで完了です！あなたのPRがマージされると、あなたは私たちの[README](https://github.com/langgenius/dify/blob/main/README_JA.md)に貢献者として掲載されます。

## ヘルプを求める

貢献の過程で困難に直面したり質問がある場合は、関連するGitHubのイシューで質問を提出するか、私たちの[Discord](https://discord.com/invite/8Tpq4AcN9c)に参加して迅速なコミュニケーションを行ってください。
