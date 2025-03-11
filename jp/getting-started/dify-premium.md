---
description: プレミアムPremium
---

# Dify Premium

Dify Premiumは[AWS AMI](https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/ec2-instances-and-amis.html)製品であります。これにより、ブランドのカスタマイズが可能で、AWS EC2にワンクリックで展開できます。[AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-t22mebxzwjhu6)から購読し、次のようなシナリオに最適です：

* 中小企業が1つ以上のアプリケーションをサーバーに構築し、データのプライバシーに関心がある場合。
* [Dify Cloud](https://docs.dify.ai/v/ja-jp/getting-started/cloud)のサブスクリプションプランに関心があり、しかし、活用事例が[プラン](https://dify.ai/pricing)で提供されるリソースを超える場合。
* Dify Enterpriseを組織内で導入する前に、POC検証を行いたい場合。

## セットアップ

Difyを初めて使用する際には、管理者初期化パスワード（EC2インスタンスIDとして設定）を入力し、セットアッププロセスを開始してください。

AMIを展開した後は、EC2コンソールで見つかるインスタンスのパブリックIPを使用してDifyにアクセスします（デフォルトではHTTPポート80を使用します）。

## アップグレード

EC2インスタンスで、次のコマンドを実行してください：

```
git clone https://github.com/langgenius/dify.git /tmp/dify
mv -f /tmp/dify/docker/* /dify/
rm -rf /tmp/dify
docker-compose down
docker-compose pull
docker-compose -f docker-compose.yaml -f docker-compose.override.yaml up -d
```

<details>

<summary>コミュニティ版を v1.0.0 にアップグレードする</summary>

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
git checkout 1.0.0 # 1.0.0 ブランチに切り替える
cd docker
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
</details>

## カスタマイズ

セルフホスト展開の場合と同様に、EC2インスタンス内の.envファイルの環境変数を必要に応じて変更することができます。その後、以下のコマンドを使用してDifyを再起動してください：

```
docker-compose down
ocker-compose -f docker-compose.yaml -f docker-compose.override.yaml up -d
```
