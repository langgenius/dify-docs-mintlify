# コミュニティ版を v1.0.0 にアップグレードする

> この記事では、旧コミュニティ版を [v1.0.0](https://github.com/langgenius/dify/releases/tag/1.0.0) にアップグレードする方法を説明します。もし Dify コミュニティ版をまだインストールしていない場合は、[Dify プロジェクト](https://github.com/langgenius/dify)をクローンし、`1.0.0` ブランチに切り替えてください。[ドキュメント](../../getting-started/install-self-hosted/docker-compose)を参照してインストールコマンドを実行してください。

コミュニティ版でプラグイン機能を体験するには、バージョンを v1.0.0 にアップグレードする必要があります。この記事では、旧バージョンから `v1.0.0` にアップグレードしてプラグインエコシステム機能を体験する方法を説明します。

## アップグレード開始

アップグレードは以下の手順で行います：

1. データのバックアップ
2. プラグインの移行
3. メインプロジェクトのアップグレード

### 1. データのバックアップ

1.1 `cd` コマンドで Dify プロジェクトのパスに移動し、バックアップ用のブランチを作成します。

1.2 次のコマンドを実行して、docker-compose YAML ファイルをバックアップします（オプション）。

```bash
cd docker
cp docker-compose.yaml docker-compose.yaml.$(date +%s).bak
```

1.3 サービスを停止するために以下のコマンドを実行し、Docker ディレクトリでデータバックアップを作成します。

```bash
docker compose down
tar -cvf volumes-$(date +%s).tgz volumes
```

### 2. バージョンアップ

`v1.0.0` は Docker Compose を使用してデプロイできます。`cd` コマンドで Dify プロジェクトのパスに移動し、以下のコマンドで Dify のバージョンをアップグレードします：

```bash
git fetch origin
git checkout 1.0.0 # 1.0.0 ブランチに切り替える
cd docker
nano .env # .env.example ファイルと同期するように環境構成ファイルを変更する
docker compose -f docker-compose.yaml up -d
```

### 3. ツールの移行をプラグインに変換

このステップでは、以前のコミュニティ版で使用していたツールやモデルプロバイダを自動的にデータ移行し、新しいバージョンのプラグイン環境にインストールします。

1. `docker ps` コマンドを実行して、docker-api コンテナの ID を確認します。

例：

```bash
docker ps
CONTAINER ID   IMAGE                                       COMMAND                  CREATED       STATUS                 PORTS                                                                                                                             NAMES
417241cd****   nginx:latest                                "sh -c 'cp /docker-e…"   3 hours ago   Up 3 hours             0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp                                                          docker-nginx-1
f84aa773****   langgenius/dify-api:1.0.0                   "/bin/bash /entrypoi…"   3 hours ago   Up 3 hours             5001/tcp                                                                                                                          docker-worker-1
a3cb19c2****   langgenius/dify-api:1.0.0                   "/bin/bash /entrypoi…"   3 hours ago   Up 3 hours             5001/tcp                                                                                                                          docker-api-1
```

`docker exec -it a3cb19c2**** bash` コマンドを実行してコンテナのターミナルにアクセスし、以下を実行します：

```bash
poetry run flask extract-plugins --workers=20
```

> エラーが発生した場合は、サーバーに `poetry` 環境をインストールしてから実行してください。コマンド実行後、端末に入力待機のプロンプトが表示された場合は「Enter」を押して入力をスキップします。

このコマンドは、現在の環境で使用しているすべてのモデルとツールを抽出します。workers パラメータは並行プロセス数を決定し、必要に応じて調整できます。コマンドが終了すると、結果が保存される `plugins.jsonl` ファイルが生成されます。このファイルには、現在の Dify インスタンス内のすべてのワークスペースのプラグイン情報が含まれます。

インターネット接続が正常で、`https://marketplace.dify.ai` にアクセスできることを確認してください。`docker-api-1` コンテナ内で以下のコマンドを実行します：

```bash
poetry run flask install-plugins --workers=2
```

このコマンドは、最新のコミュニティ版に必要なすべてのプラグインをダウンロードしてインストールします。ターミナルに `Install plugins completed.` と表示されたら、移行は完了です。

## 移行結果の検証

Dify プラットフォームにアクセスし、右上の「プラグイン」ボタンをクリックして、以前使用していたツールが正しくインストールされているか確認します。ランダムにプラグインを使用して、正常に動作するかを検証します。問題がなければ、バージョンアップとデータ移行が完了したことを示しています。

![](https://assets-docs.dify.ai/2025/02/6467b3578d3d3e96510f50a09442d5a5.png)
