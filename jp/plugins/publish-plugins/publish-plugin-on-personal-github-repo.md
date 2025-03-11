# 個人GitHubリポジトリへの公開

GitHubリポジトリリンクを通じたプラグインのインストールに対応しています。プラグイン開発完了後、公開GitHubリポジトリにプラグインを公開して、他のユーザーがダウンロードして使用できるようにすることができます。この方法には以下の利点があります：

* 個人管理：プラグインのコードとアップデートを完全にコントロール可能
* 迅速な共有：GitHubリンクを通じて他のユーザーやチームメンバーと簡単に共有でき、テストや使用が容易
* コラボレーションとフィードバック：プラグインをオープンソース化することで、GitHubの潜在的な協力者を引き付け、プラグインの迅速な改善が可能

このガイドでは、GitHubリポジトリへのプラグインの公開方法を説明します。

## 準備作業

* GitHubアカウント
* 新規パブリックGitHubリポジトリの作成
* ローカルにGitツールがインストール済み

GitHubの基本知識については、[GitHubドキュメント](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)を参照してください。

## 1. プラグインプロジェクトの完成

パブリックGitHubへのアップロードは、プラグインを公開することを意味します。プラグインのデバッグと検証が完了し、`README.md`ファイルが適切に作成されていることを確認してください。

説明文書には以下の内容を含めることを推奨します：

* プラグインの概要と機能説明
* インストールと設定手順
* 使用例
* 連絡先または貢献ガイドライン

## 2. ローカルリポジトリの初期化
プラグインを公開アップロードする前に、デバッグと検証作業が完了していることを確認してください。ターミナルでプラグインプロジェクトフォルダに移動し、以下のコマンドを実行します：

    git init
    git add .
    git commit -m "Initial commit: Add plugin files"
    
Gitを初めて使用する場合は、Gitのユーザー名とメールアドレスの設定が必要な場合があります：

    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"

## 3. リモートリポジトリの接続

以下のコマンドを使用して、ローカルリポジトリをGitHubリポジトリに接続します：

    git remote add origin https://github.com/<your-username>/<repository-name>.git

## 4. プラグインファイルのアップロード

> プラグインプロジェクトをプッシュする前に、`manifest.yaml`ファイルのauthorフィールドがGitHub IDと一致していることを確認してください。

プラグインプロジェクトをGitHubリポジトリにプッシュします：

    git branch -M main
    git push -u origin main
    
コードのアップロード時には、後のパッケージング用にタグを付けることを推奨します：

    git tag -a v0.0.1 -m "Release version 0.0.1"
    git push origin v0.0.1
    
## 5. プラグインコードのパッケージング

GitHubリポジトリのReleasesページで新しいバージョンリリースを作成します。リリース時にはプラグインファイルをアップロードする必要があります。プラグインファイルのパッケージング方法の詳細については、[プラグインのパッケージング](https://docs.dify.ai/ja-jp/plugins/publish-plugins/package-and-publish-plugin-file)をご覧ください。

![プラグインコードのパッケージング](https://assets-docs.dify.ai/2025/01/de1d01614ade2214dba5f19eea682804.png)

## GitHubからのプラグインインストール

他のユーザーは、GitHubリポジトリアドレスを通じてプラグインをインストールできます。Difyプラットフォームのプラグイン管理ページにアクセスし、GitHubからのインストールを選択し、リポジトリアドレスを入力後、バージョン番号とパッケージファイルを選択してインストールを完了します。

![GitHubからのプラグインインストール](https://assets-docs.dify.ai/2025/01/7db779f2d581f1c55250e45a4f23d6fb.png)
