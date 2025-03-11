# ローカルソースコード起動

### 前提条件

> Dify インストール前に, ぜひマシンが最小インストール要件を満たしていることを確認してください：
> - CPU >= 2 Core
> - RAM >= 4 GiB

| 操作系统                       | ソフトウェア                                                         | 説明                                                                                                                                                                                   |
| -------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| macOS 10.14またはそれ以降     | Docker Desktop                                                 | Docker 仮想マシン（VM）を少なくとも2つの仮想CPU（vCPU）と8GBの初期メモリを使用するように設定してください。そうでないと、インストールが失敗する可能性があります。詳細は[MacにDocker Desktopをインストールする](https://docs.docker.com/desktop/mac/install/)を参照してください。                                   |
| Linux プラットフォーム      | <p>Docker 19.03またはそれ以降<br>Docker Compose 1.25.1またはそれ以降</p>| 詳細は[Dockerをインストールする](https://docs.docker.com/engine/install/)および[Docker Composeをインストールする](https://docs.docker.com/compose/install/)を参照してください。                                                      |
| WSL 2が有効なWindows       | Docker Desktop                                                 | ソースコードや他のデータをLinuxコンテナにバインドする際、WindowsファイルシステムではなくLinuxファイルシステムに保存することをお勧めします。詳細は[WSL 2バックエンドを使用してWindowsにDocker Desktopをインストールする](https://docs.docker.com/desktop/windows/install/#wsl-2-backend)を参照してください。 |

> OpenAI TTSを使用する場合、システムにFFmpegをインストールする必要があります。詳細は[リンク](https://docs.dify.ai/v/ja-jp/learn-more/faq/install-faq#id-15-tekisutomigeniopenai-error-ffmpeg-is-not-installedtoiuergashitano)を参照してください。

Dify コードをクローン：

```Bash
git clone https://github.com/langgenius/dify.git
```

ビジネスサービスを有効にする前に、PostgreSQL / Redis / Weaviate（ローカルにない場合）をデプロイする必要があります。以下のコマンドで起動できます：

```Bash
cd docker
docker compose -f docker-compose.middleware.yaml up -d
```

***

### サービスデプロイ

* API インターフェースサービス
* Worker 非同期キュー消費サービス

#### 基本環境インストール

サーバーの起動にはPython 3.12 が必要です。Python環境の迅速なインストールには[pyenv](https://github.com/pyenv/pyenv)を使用することをお勧めします。

追加のPythonバージョンをインストールするには、pyenv installを使用します。

```Bash
pyenv install 3.12
```

"3.12" の Python 環境に切り替えるには、次のコマンドを使用します。

```Bash
pyenv global 3.12
```


#### 起動手順

1.  apiディレクトリに移動

    ```
    cd api
    ```
> macOSの場合：`brew install libmagic`でlibmagicをインストールしてください。

2.  環境変数構成ファイルをコピー

    ```
    cp .env.example .env
    ```
3.  ランダムキーを生成し、`.env`の`SECRET_KEY`の値を置き換え

    ```
    awk -v key="$(openssl rand -base64 42)" '/^SECRET_KEY=/ {sub(/=.*/, "=" key)} 1' .env > temp_env && mv temp_env .env
    ```
4.  依存関係をインストール

    Dify APIサービスは依存関係を管理するために[Poetry](https://python-poetry.org/docs/)を使用します。環境を有効にするには、`poetry shell`を実行できます。

    ```
    poetry env use 3.12
    poetry install
    ```
5.  データベース移行を実行

    データベーススキーマを最新バージョンに更新します。

    ```
    poetry shell
    flask db upgrade
    ```
6.  APIサービスを開始

    ```
    flask run --host 0.0.0.0 --port=5001 --debug
    ```

    正常な出力：

    ```
    * Debug mode: on
    INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on all addresses (0.0.0.0)
     * Running on http://127.0.0.1:5001
    INFO:werkzeug:Press CTRL+C to quit
    INFO:werkzeug: * Restarting with stat
    WARNING:werkzeug: * Debugger is active!
    INFO:werkzeug: * Debugger PIN: 695-801-919
    ```
7.  Workerサービスを開始

    データセットファイルのインポートやデータセットドキュメントの更新などの非同期操作を消費するためのサービスです。Linux / MacOSでの起動：

    ```
    celery -A app.celery worker -P gevent -c 1 -Q dataset,generation,mail,ops_trace --loglevel INFO
    ```

    Windowsシステムでの起動の場合、以下のコマンドを使用してください：

    ```
    celery -A app.celery worker -P solo --without-gossip --without-mingle -Q dataset,generation,mail,ops_trace --loglevel INFO
    ```

    正常な出力：

    ```
     -------------- celery@TAKATOST.lan v5.2.7 (dawn-chorus)
    --- ***** ----- 
    -- ******* ---- macOS-10.16-x86_64-i386-64bit 2023-07-31 12:58:08
    - *** --- * --- 
    - ** ---------- [config]
    - ** ---------- .> app:         app:0x7fb568572a10
    - ** ---------- .> transport:   redis://:**@localhost:6379/1
    - ** ---------- .> results:     postgresql://postgres:**@localhost:5432/dify
    - *** --- * --- .> concurrency: 1 (gevent)
    -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
    --- ***** ----- 
     -------------- [queues]
                    .> dataset          exchange=dataset(direct) key=dataset
                    .> generation       exchange=generation(direct) key=generation
                    .> mail             exchange=mail(direct) key=mail

    [tasks]
      . tasks.add_document_to_index_task.add_document_to_index_task
      . tasks.clean_dataset_task.clean_dataset_task
      . tasks.clean_document_task.clean_document_task
      . tasks.clean_notion_document_task.clean_notion_document_task
      . tasks.create_segment_to_index_task.create_segment_to_index_task
      . tasks.deal_dataset_vector_index_task.deal_dataset_vector_index_task
      . tasks.document_indexing_sync_task.document_indexing_sync_task
      . tasks.document_indexing_task.document_indexing_task
      . tasks.document_indexing_update_task.document_indexing_update_task
      . tasks.enable_segment_to_index_task.enable_segment_to_index_task
      . tasks.generate_conversation_summary_task.generate_conversation_summary_task
      . tasks.mail_invite_member_task.send_invite_member_mail_task
      . tasks.remove_document_from_index_task.remove_document_from_index_task
      . tasks.remove_segment_from_index_task.remove_segment_from_index_task
      . tasks.update_segment_index_task.update_segment_index_task
      . tasks.update_segment_keyword_index_task.update_segment_keyword_index_task

    [2023-07-31 12:58:08,831: INFO/MainProcess] Connected to redis://:**@localhost:6379/1
    [2023-07-31 12:58:08,840: INFO/MainProcess] mingle: searching for neighbors
    [2023-07-31 12:58:09,873: INFO/MainProcess] mingle: all alone
    [2023-07-31 12:58:09,886: INFO/MainProcess] pidbox: Connected to redis://:**@localhost:6379/1.
    [2023-07-31 12:58:09,890: INFO/MainProcess] celery@TAKATOST.lan ready.
    ```

***

### フロントエンドページデプロイ

Web フロントエンドクライアントページサービス

#### 基本環境インストール

Web フロントエンドサービスを起動するには[Node.js v18.x (LTS)](http://nodejs.org)、[NPMバージョン8.x.x](https://www.npmjs.com/)または[Yarn](https://yarnpkg.com/)が必要です。

* NodeJS + NPMをインストール

https://nodejs.org/en/download から対応するOSのv18.x以上のインストーラーをダウンロードしてインストールしてください。stableバージョンをお勧めします。NPMも同梱されています。

#### 起動手順

1.  webディレクトリに移動

    ```
    cd web
    ```
2.  依存関係をインストール

    ```
    npm install
    ```
3.  環境変数を構成。現在のディレクトリに `.env.local` ファイルを作成し、`.env.example` の内容をコピーします。必要に応じてこれらの環境変数の値を変更します。

    ```
    # For production release, change this to PRODUCTION
    NEXT_PUBLIC_DEPLOY_ENV=DEVELOPMENT
    # The deployment edition, SELF_HOSTED
    NEXT_PUBLIC_EDITION=SELF_HOSTED
    # The base URL of console application, refers to the Console base URL of WEB service if console domain is
    # different from api or web app domain.
    # example: http://cloud.dify.ai/console/api
    NEXT_PUBLIC_API_PREFIX=http://localhost:5001/console/api
    # The URL for Web APP, refers to the Web App base URL of WEB service if web app domain is different from
    # console or api domain.
    # example: http://udify.app/api
    NEXT_PUBLIC_PUBLIC_API_PREFIX=http://localhost:5001/api

    # SENTRY
    NEXT_PUBLIC_SENTRY_DSN=
    NEXT_PUBLIC_SENTRY_ORG=
    NEXT_PUBLIC_SENTRY_PROJECT=
    ```
4.  コードをビルド

    ```
    npm run build
    ```
5.  webサービスを開始

    ```
    npm run start
    # または
    yarn start
    # または
    pnpm start
    ```

正常に起動すると、ターミナルに以下の情報が出力されます：

```
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
warn  - You have enabled experimental feature (appDir) in next.config.js.
warn  - Experimental features are not covered by semver, and may cause unexpected or broken application behavior. Use at your own risk.
info  - Thank you for testing `appDir` please leave your feedback at https://nextjs.link/app-feedback
```

### Difyを訪問

最後に、http://127.0.0.1:3000 にアクセスすると、ローカルデプロイメントされたDifyを使用できます。
