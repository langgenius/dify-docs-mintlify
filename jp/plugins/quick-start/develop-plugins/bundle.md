# バンドル

バンドルプラグインパッケージは、複数のプラグインをまとめたものです。複数のプラグインを一つのパッケージにまとめることで、プラグインの一括インストールを可能にし、より高度な機能を提供します。

Dify CLIツールを使用すると、複数のプラグインをバンドルとしてパッケージ化できます。バンドルプラグインパッケージには、以下の3つのタイプがあります。

*   `Marketplace` タイプ：プラグインのIDとバージョン情報を保持します。インポート時には、Dify Marketplaceから該当するプラグインパッケージをダウンロードします。
*   `GitHub` タイプ：GitHubリポジトリのアドレス、リリースバージョン番号、アセットファイル名を保持します。インポート時に、Difyは該当するGitHubリポジトリにアクセスしてプラグインパッケージをダウンロードします。
*   `Package` タイプ：プラグインパッケージをバンドル内に直接格納します。参照元は保持されませんが、バンドルパッケージのサイズが大きくなる可能性があります。

### 事前準備

*   Difyプラグインのひな形ツール
*   Python環境（バージョン3.10以上）

プラグイン開発のひな形ツールを準備する方法の詳細については、「[開発ツールの初期化](initialize-development-tools.md)」を参照してください。

### バンドルプロジェクトの作成

現在のディレクトリで、ひな形コマンドラインツールを実行し、新しいプラグインパッケージプロジェクトを作成します。

```bash
./dify-plugin-darwin-arm64 bundle init
```

このバイナリファイルを `dify` にリネームし、`/usr/local/bin` ディレクトリにコピーした場合、次のコマンドを実行して新しいプラグインプロジェクトを作成できます。

```bash
dify bundle init
```

#### 1. プラグイン情報の入力

プロンプトに従って、プラグイン名、作成者情報、プラグインの説明を設定します。チームで共同作業している場合は、作成者に組織名を記入することもできます。

> 名前は1〜128文字で、文字、数字、ダッシュ、アンダースコアのみを使用できます。

![バンドルの基本情報](https://assets-docs.dify.ai/2024/12/03a1c4cdc72213f09523eb1b40832279.png)

情報を入力してEnterキーを押すと、バンドルプラグインプロジェクトのディレクトリが自動的に作成されます。

![](https://assets-docs.dify.ai/2024/12/356d1a8201fac3759bf01ee64e79a52b.png)

#### 2. 依存関係の追加

*   **マーケットプレイス(Marketplace)**

次のコマンドを実行します。

```bash
dify-plugin bundle append marketplace . --marketplace_pattern=langgenius/openai:0.0.1
```

ここで、`marketplace_pattern` は、Marketplaceでのプラグインの参照であり、形式は `組織名/プラグイン名:バージョン番号` です。

*   **Github**

次のコマンドを実行します。

```bash
dify-plugin bundle append github . --repo_pattern=langgenius/openai:0.0.1/openai.difypkg
```

ここで、`repo_pattern` は、GitHubでのプラグインの参照であり、形式は `組織名/リポジトリ名:リリース/添付ファイル名` です。

*   **パッケージ(package)**

次のコマンドを実行します。

```bash
dify-plugin bundle append package . --package_path=./openai.difypkg
```

ここで、`package_path` は、プラグインパッケージのディレクトリです。

### バンドルプロジェクトのパッケージ化

次のコマンドを実行して、バンドルプラグインをパッケージ化します。

```bash
dify-plugin bundle package ./bundle
```

コマンドを実行すると、現在のディレクトリに `bundle.difybndl` ファイルが自動的に作成されます。このファイルが最終的なパッケージ結果です。