# Docker Compose デプロイ

### 前提条件

> Dify インストール前に, マシンが最小インストール要件を満たしていることを確認してください：
>
> * CPU >= 2 Core
> * RAM >= 4 GiB

| オペレーティング·システム      | ソフトウェア                                         | 説明                                                                                                                                                                                                                     |
| ------------------ | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| macOS 10.14またはそれ以降 | Docker Desktop                                 | Docker仮想マシン (VM) を少なくとも2つの仮想CPU (vCPU) と8 GBの初期メモリを使用するように設定してください。そうしないと、インストールが失敗する可能性があります。詳細については[MacにDocker Desktopをインストール](https://docs.docker.com/desktop/mac/install/)を参照してください。                               |
| Linuxプラットフォーム      | <p>Docker 19.03以降<br>Docker Compose 1.28以降</p> | 詳細については[Dockerのインストール](https://docs.docker.com/engine/install/)および[Docker Composeのインストール](https://docs.docker.com/compose/install/)を参照してください。                                                                          |
| WSL 2を有効にしたWindows | <p>Docker Desktop<br></p>                      | ソースコードやその他のデータをLinuxコンテナにバインドする際には、それらをWindowsファイルシステムではなくLinuxファイルシステムに保存することをお勧めします。詳細については[WSL 2バックエンドを使用してWindowsにDocker Desktopをインストール](https://docs.docker.com/desktop/windows/install/#wsl-2-backend)を参照してください。 |

### Difyのクローン

Difyのソースコードをローカルにクローンします

```bash
# 現在の最新バージョンは0.15.3だと仮定すると
git clone https://github.com/langgenius/dify.git --branch 0.15.3
```

### Difyの起動

1.  difyソースコードのdockerディレクトリに移動し、次のコマンドを実行してdifyを起動する：

    ```bash
    cd dify/docker
    ```
2.  環境配置ファイルをコピーする

    ```bash
    cp .env.example .env
    ```
3.  Docker コンテナを起動する

    システムにインストールしたDocker Composeのバージョンをベースに，相応しい命令を使ってコンテナを起動します。 `$ docker compose version`を通してdockerのバージョンをチェックできます，詳しくは [Docker ドキュメント](https://docs.docker.com/compose/#compose-v2-and-the-new-docker-compose-command)を参考してください：

    * Docker Compose V2を使用する場合，以下の命令を入力する：

    ```bash
    docker compose up -d
    ```

    * Docker Compose V1を使用する場合，以下の命令を入力する：

    ```bash
    docker-compose up -d
    ```

上記のコマンドを実行すると、すべてのコンテナの状態とポートマッピングを表示する以下のような出力が表示されるはずです：

```Shell
[+] Running 11/11
 ✔ Network docker_ssrf_proxy_network  Created                                                                 0.1s 
 ✔ Network docker_default             Created                                                                 0.0s 
 ✔ Container docker-redis-1           Started                                                                 2.4s 
 ✔ Container docker-ssrf_proxy-1      Started                                                                 2.8s 
 ✔ Container docker-sandbox-1         Started                                                                 2.7s 
 ✔ Container docker-web-1             Started                                                                 2.7s 
 ✔ Container docker-weaviate-1        Started                                                                 2.4s 
 ✔ Container docker-db-1              Started                                                                 2.7s 
 ✔ Container docker-api-1             Started                                                                 6.5s 
 ✔ Container docker-worker-1          Started                                                                 6.4s 
 ✔ Container docker-nginx-1           Started                                                                 7.1s
```

最後に、すべてのコンテナが正常に稼働しているか確認：

```bash
docker compose ps
```

これは3つのビジネスサービス `api / worker / web` と4つの基礎コンポーネント `weaviate / db / redis / nginx` を含まれます。

```bash
NAME                IMAGE                              COMMAND                  SERVICE             CREATED             STATUS              PORTS
docker-api-1        langgenius/dify-api:0.3.2          "/entrypoint.sh"         api                 4 seconds ago       Up 2 seconds        80/tcp, 5001/tcp
docker-db-1         postgres:15-alpine                 "docker-entrypoint.s…"   db                  4 seconds ago       Up 2 seconds        0.0.0.0:5432->5432/tcp
docker-nginx-1      nginx:latest                       "/docker-entrypoint.…"   nginx               4 seconds ago       Up 2 seconds        0.0.0.0:80->80/tcp
docker-redis-1      redis:6-alpine                     "docker-entrypoint.s…"   redis               4 seconds ago       Up 3 seconds        6379/tcp
docker-weaviate-1   semitechnologies/weaviate:1.18.4   "/bin/weaviate --hos…"   weaviate            4 seconds ago       Up 3 seconds        
docker-web-1        langgenius/dify-web:0.3.2          "/entrypoint.sh"         web                 4 seconds ago       Up 3 seconds        80/tcp, 3000/tcp
docker-worker-1     langgenius/dify-api:0.3.2          "/entrypoint.sh"         worker              4 seconds ago       Up 2 seconds        80/tcp, 5001/tcp
```

これらの手順を通して、Difyをローカルでインストールできます。

### Difyの更新

difyソースコードのdockerディレクトリに入り、以下のコマンドを順に実行：

```bash
cd dify/docker
git pull origin main
docker compose down
docker compose pull
docker compose up -d
```

#### 環境変数設定の同期 (重要！)

* `.env.example` ファイルが更新された場合は、必ずローカルの `.env` ファイルをそれに応じて修正してください。
* `.env` ファイル内のすべての設定項目を確認し、実際の運用環境に合わせて修正してください。`.env.example` から `.env` ファイルに新しい変数を追加したり、変更された値を更新する必要があるかもしれません。

### Difyへのアクセス

管理者初期化ページにアクセスして管理者アカウントを設定する:

```bash
# ローカル環境
http://localhost/install

# サーバー環境
http://your_server_ip/install
```

Dify web interface address:

```bash
# ローカル環境
http://localhost

# サーバー環境
http://your_server_ip
```

### Difyのカスタマイズ化

環境変数は docker/dotenvs にあります。もし変数を変更するには、対応する`.env.example` ファイル名の接尾辞 `.example` を削除し、ファイル中の変数を直接編集してください。その後、以下のコマンドを順に実行：

```
docker compose down
docker compose up -d
```

すべての環境変数は `docker/.env.example` にあります。

### もっと

もし疑問があれば、[よくある質問](faq.md)をご覧ください。
