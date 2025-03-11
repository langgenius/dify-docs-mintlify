# セルフホスト / ローカル展開に関するよくある質問（FAQ）

### 1. ローカル展開の初期化後、パスワードが間違っている場合のリセット方法は？

Docker Composeで展開した場合、次のコマンドを使用してパスワードをリセットできます：

```
docker exec -it docker-api-1 flask reset-password
```

メールアドレスと新しいパスワードを2回入力してください。

### 2. ローカル展開ログで「ファイルが見つかりません」というエラーを修正する方法は？

```
ERROR:root:Unknown Error in completion
Traceback (most recent call last):
  File "/www/wwwroot/dify/dify/api/libs/rsa.py", line 45, in decrypt
    private_key = storage.load(filepath)
  File "/www/wwwroot/dify/dify/api/extensions/ext_storage.py", line 65, in load
    raise FileNotFoundError("File not found")
FileNotFoundError: File not found
```

このエラーは、展開方法の変更や `api/storage/privkeys` ディレクトリの削除によって発生する可能性があります。このファイルは大規模モデルキーの暗号化に使用されるため、損失は不可逆です。次のコマンドを使用して暗号化キーペアをリセットできます：

* Docker Compose デプロイ

    ```
    docker exec -it docker-api-1 flask reset-encrypt-key-pair
    ```
* ソースコードの起動

    apiディレクトリに移動し、次のコマンドを実行します：

    ```
    flask reset-encrypt-key-pair
    ```

    プロンプトに従ってリセットしてください。

### **3. インストール後にログインできない、またはログインした後に401エラーが表示される場合は？**

これは、ドメイン/URLを変更したため、フロントエンドとバックエンドの間でクロスドメインの問題が発生している可能性があります。クロスドメインとアイデンティティの問題には、次の構成が関係しています：

1. CORS クロスドメイン構成
   1. `CONSOLE_CORS_ALLOW_ORIGINS`

   コンソールCORSポリシー。デフォルトは*で、すべてのドメインがアクセス可能です。
   2. `WEB_API_CORS_ALLOW_ORIGINS`

   WebAPP CORSポリシー。デフォルトは*で、すべてのドメインがアクセス可能です。

### **4. 起動後にページが読み込まれ続け、CORSエラーが表示される場合は？**

これは、ドメイン/URLを変更したため、フロントエンドとバックエンドの間でクロスドメインの問題が発生している可能性があります。`docker-compose.yml`内の次の構成項目を新しいドメインに更新してください：

`CONSOLE_API_URL`: コンソールAPIのバックエンドURL
`CONSOLE_WEB_URL`: コンソールWebのフロントエンドURL
`SERVICE_API_URL`: サービスAPIのURL
`APP_API_URL`: WebApp APIのバックエンドURL
`APP_WEB_URL`: WebAppのURL

詳細については、[環境変数](../../getting-started/install-self-hosted/environments)を参照してください。

### 5. 展開後のバージョンアップ方法は？

イメージから開始した場合は、最新のイメージを取得し、アップグレードを完了させてください。ソースコードから開始した場合は、最新のコードを取得してから始め、アップグレードを完了させます。

ソースコードの更新については、apiディレクトリに移動し、次のコマンドを実行してデータベース構造を最新バージョンにマイグレートします：

`flask db upgrade`

### 6. Notionを使用してインポート時に環境変数を設定する方法は？

[**Notion 統合構成アドレス**](https://www.notion.so/my-integrations)**。**プライベート展開を行う場合は、次の構成を設定してください：

1. **`NOTION_INTEGRATION_TYPE`** ：この値は（**public/internal**）に設定する必要があります。Notion の OAuth リダイレクトアドレスは https のみをサポートするため、ローカル展開には Notion の内部統合を使用してください。
2. **`NOTION_CLIENT_SECRET`** ： Notion OAuth クライアントシークレット（パブリック統合タイプ用）。
3. **`NOTION_CLIENT_ID`** ： OAuth クライアントID（パブリック統合タイプ用）。
4. **`NOTION_INTERNAL_SECRET`** ： Notion内部統合シークレット。`NOTION_INTEGRATION_TYPE`が **internal**の場合、この変数を設定してください。

### 7. ローカル展開バージョンでスペースの名前を変更する方法は？

データベースの`tenants`テーブルを直接修正してください。

### 8. アプリケーションへのアクセスドメインを変更するには？

`docker_compose.yaml`内の`APP_WEB_URL`構成項目を見つけて、新しいドメインに変更してください。

### 9. データベースのマイグレーションが発生した場合にバックアップすべき内容は？

データベース、構成されたストレージ、ベクトルデータベースのデータをバックアップしてください。Docker Composeを使用して展開した場合は、`dify/docker/volumes`ディレクトリ内のすべてのデータを直接バックアップします。

### 10. OpenLLMをローカルで起動する際にDocker展開のDifyが127.0.0.1を使用してローカルポートにアクセスできない理由は？

127.0.0.1はコンテナ内のアドレスです。Difyの構成されたサーバーアドレスは、ホストのローカルネットワークIPアドレスである必要があります。

### 11. ローカル展開バージョンのデータセットでドキュメントをアップロードする際のサイズと数量制限を解決する方法は？

公式Webサイトの[環境変数](../../getting-started/install-self-hosted/environments)を参照してください。

### 12. ローカル展開バージョンでメール経由でメンバーを招待する方法は？

ローカル展開バージョンでは、メールを通じてメンバーを招待できます。メールアドレスを入力し、招待を送信すると、ページに招待リンクが表示されます。招待リンクをコピーしてユーザーに転送してください。ユーザーはそのリンクを開き、メール経由でログインし、パスワードを設定してスペースにアクセスできます。

### 13. ローカル展開バージョンで「Can't load tokenizer for 'gpt2」というエラーが発生した場合はどうすればよいですか？

```
Can't load tokenizer for 'gpt2'. If you were trying to load it from 'https://huggingface.co/models', make sure you don't have a local directory with the same name. Otherwise, make sure 'gpt2' is the correct path to a directory containing all relevant files for a GPT2TokenizerFast tokenizer.
```

設定に関しては、公式Webサイトの[環境変数](../../getting-started/install-self-hosted/environments)や関連する[Issue](https://github.com/langgenius/dify/issues/1261)を参照してください。

### 14. ローカル展開バージョンでポート80の競合を解消する方法

ポート80が使用中の場合、ポート80を占有しているサービスを停止するか、docker-compose.yamlでポートマッピングを変更し、ポート80を別のポートにマッピングしてください。通常、ApacheやNginxがこのポートを占有しているため、これらのサービスを停止することで解決できます。

### 15. テキスト読み上げ中に「[openai] Error: ffmpeg is not installed」というエラーが発生した場合の対処方法

```
[openai] Error: ffmpeg is not installed
```

OpenAI TTSはオーディオストリームの分割を実装しているため、ソースコード展開にはffmpegのインストールが必要です。詳細な手順は以下の通りです：

**Windows:**

1. [FFmpeg公式Webサイト](https://ffmpeg.org/download.html)を訪れ、事前にコンパイルされたWindows用の共有ライブラリをダウンロードします。
2. FFmpegフォルダをダウンロードして展開し、"ffmpeg-20200715-51db0a4-win64-static"のようなフォルダが生成されます。
3. 展開したフォルダを任意の場所に移動します。例：C:\Program Files\。
4. FFmpegのbinディレクトリの絶対パスをシステムの環境変数に追加します。
5. コマンドプロンプトを開き、"ffmpeg -version"と入力します。FFmpegのバージョン情報が表示されれば、インストールが成功しています。

**Ubuntu:**

1. ターミナルを開きます。
2. 次のコマンドを入力してFFmpegをインストールします：`sudo apt-get update`、次に`sudo apt-get install ffmpeg`を入力します。
3. インストールが成功したかどうかを確認するために、"ffmpeg -version"と入力します。

**CentOS:**

1. まず、EPELリポジトリを有効にします。ターミナルで次を入力します：`sudo yum install epel-release`
2. 次に、次のコマンドを入力します：`sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm`
3. yumパッケージを更新します。入力：`sudo yum update`
4. 最後に、FFmpegをインストールします。入力：`sudo yum install ffmpeg ffmpeg-devel`
5. インストールが成功したかどうかを確認するために、"ffmpeg -version"と入力します。

**Mac OS X:**

1. ターミナルを開きます。
2. Homebrewをまだインストールしていない場合は、次のコマンドを入力してインストールできます：`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. Homebrew を使用して FFmpeg をインストールします。入力：`brew install ffmpeg`
4. インストールが成功したかどうかを確認するために、"ffmpeg -version"と入力します。

### 16. ローカル展開中のNginx設定ファイルのマウントエラーを解消する方法

```
Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error mounting "/run/desktop/mnt/host/d/Documents/docker/nginx/nginx.conf" to rootfs at "/etc/nginx/nginx.conf": mount /run/desktop/mnt/host/d/Documents/docker/nginx/nginx.conf:/etc/nginx/nginx.conf (via /proc/self/fd/9), flags: 0x5000: not a directory: unknown: Are you trying to mount a directory onto a file (or vice-versa)? Check if the specified host path exists and is the expected type
```

完全なプロジェクトをダウンロードし、dockerに移動し、`docker-compose up -d`を実行してください。

```
git clone https://github.com/langgenius/dify.git
cd dify/docker
docker compose up -d
```

### 17. ベクトルデータベースを他のベクトルデータベースに移行する方法

Weaviate から他のベクトルデータベースにベクトルデータベースを移行する場合、データを移行する必要があります。以下はその手順です：

1. ローカルソースコードから始める場合は、.envファイル内の環境変数を移行したいベクトルデータベースに変更してください。例：`VECTOR_STORE=qdrant`
2. docker-composeから始める場合は、`docker-compose.yaml`ファイル内の環境変数を移行したいベクトルデータベースに変更し、apiとworkerの両方を修正する必要があります。例：

```
# The type of vector store to use. Supported values are `weaviate`, `qdrant`, `milvus`, `analyticdb``.
VECTOR_STORE: weaviate
```

3. 以下のコマンドを実行してください

```
flask vdb-migrate # or docker exec -it docker-api-1 flask vdb-migrate
```

**テスト済みのターゲット データベース:**

- qdrant
- milvus
- analyticdb

### 18. SSRF_PROXYが必要な理由とは？

コミュニティエディションの `docker-compose.yaml` では、一部のサービスに `SSRF_PROXY` と `HTTP_PROXY` 環境変数が設定されています。これらは全て、`ssrf_proxy` コンテナを指しており、SSRF攻撃を防ぐために利用されています。SSRF攻撃について詳しく学びたい方は、[こちらの記事](https://portswigger.net/web-security/ssrf)をご覧ください。

不必要なリスクを避けるために、SSRF攻撃の可能性があるすべてのサービスにプロキシを設定し、Sandboxのようなサービスがプロキシを通じてのみ外部ネットワークにアクセスできるようにしています。これにより、データとサービスのセキュリティが強化されます。デフォルトでは、このプロキシはローカルリクエストをインターセプトしませんが、`squid` 構成ファイルを変更することで、プロキシの動作をカスタマイズできます。

#### プロキシの動作をカスタマイズする方法は？

プロキシの動作は `docker/volumes/ssrf_proxy/squid.conf` にある `squid` 構成ファイルを編集することでカスタマイズできます。例えば、ローカルネットワークが `192.168.101.0/24` セグメントにアクセスできる場合でも、`192.168.101.19` にある機密データには、ローカル展開のDifyユーザーがアクセスしてほしくない場合、以下のように `squid.conf` にルールを追加できます。

```
acl restricted_ip dst 192.168.101.19
acl localnet src 192.168.101.0/24

http_access deny restricted_ip
http_access allow localnet
http_access deny all
```

これは一例に過ぎません。必要に応じてプロキシの動作を自由にカスタマイズできます。アップストリームプロキシやキャッシュの設定が必要な場合は、詳細については [squid構成ドキュメント](http://www.squid-cache.org/Doc/config/) をご覧ください。

### 19. 作成したアプリをテンプレートとして設定する方法は？

現時点では、作成したアプリをテンプレートとして設定する機能はサポートされていません。既存のテンプレートは、Difyの公式がクラウドバージョンユーザー向けに提供しているもので、参考用となっています。クラウドバージョンをご利用の場合は、アプリをワークスペースに追加したり、変更後にカスタマイズして独自のアプリを作成できます。コミュニティバージョンを使用していて、チーム向けにさらに多くのアプリテンプレートが必要な場合は、有料の技術サポートを受けるために弊社ビジネスチームにお問い合わせください：[business@dify.ai](mailto:business@dify.ai)

### 20. 502 Bad Gateway

このエラーは、Nginxがサービスを誤った場所に転送しているために発生します。まず、対象のコンテナが実行中であることを確認し、以下のコマンドを管理者権限で実行してください：

```
docker ps -q | xargs -n 1 docker inspect --format '{{ .Name }}: {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
```

出力の中から以下の2行を見つけてください：

```
/docker-web-1: 172.19.0.5
/docker-api-1: 172.19.0.7
```

これらのIPアドレスをメモしておきます。次に、Difyソースコードを保存しているディレクトリに移動し、`dify/docker/nginx/conf.d` を開いて、`http://api:5001` を `http://172.19.0.7:5001` に、`http://web:3000` を `http://172.19.0.5:3000` に置き換え、Nginxコンテナを再起動するか、構成を再読み込みします。

なお、これらのIPアドレスは _**例**_ ですので、独自のIPアドレスを取得するためにコマンドを実行する必要があります。また、関連するコンテナを再起動する際には、IPアドレスの再設定が必要になることがあります。

### 21. コンテンツ セキュリティ ポリシーを有効にするにはどうすればよいですか?

`.env`構成ファイルで`CSP_WHITELIST`パラメータを見つけて、製品の使用に関連するすべての URL や API リクエスト アドレスなど、許可できるドメイン名を入力します。
この動きは、潜在的な XSS 攻撃を減らすのに役立ちます。 CSP に関する推奨事項の詳細については、[コンテンツ セキュリティ ポリシー](https://developer.mozilla.org/ja/docs/Web/HTTP/CSP) を参照してください。

### 22. APIサービスのポート番号を変更する方法

API サービスのポートは、Dify プラットフォームで使用されるポートと一致します。`docker-compose.yaml` ファイルの `nginx` 設定を変更することで、実行中のポートを再指定することができます。

### 23. ファイルをローカルストレージからクラウドストレージに移行する方法

ファイルをローカルストレージからクラウドストレージ（例：Alibaba Cloud OSS）に移行するには、'upload_files'と'privkeys'ディレクトリからデータを移行する必要があります。以下の手順に従って操作してください：

1. ストレージ設定を構成する

   ローカルソースコードデプロイメントの方法：
   - `.env`ファイルでストレージ設定を更新します
   - `STORAGE_TYPE=aliyun-oss`を設定します
   - Alibaba Cloud OSSの認証情報を設定します

   Docker Composeデプロイメントの方法：
   - `docker-compose.yaml`ファイルでストレージ設定を更新します
   - `STORAGE_TYPE: aliyun-oss`を設定します
   - Alibaba Cloud OSSの認証情報を設定します

2. 移行コマンドを実行する

   ローカルソースコードの場合：
   ```bash
   flask upload-private-key-file-to-cloud-storage
   flask upload-local-files-to-cloud-storage
   ```

   Docker Composeの場合：
   ```bash
   docker exec -it docker-api-1 flask upload-private-key-file-to-cloud-storage
   docker exec -it docker-api-1 flask upload-local-files-to-cloud-storage
   ```