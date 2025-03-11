# LocalAIでデプロイしたローカルモデルを統合

[LocalAI](https://github.com/go-skynet/LocalAI) は、RESTFul APIを提供するローカル推論フレームワークで、OpenAI API仕様と互換性があります。これにより、消費者向けハードウェア上で、または自社サーバー上で、GPUを使用せずにLLM（大型言語モデル）や他のモデルを実行することが可能です。Difyは、LocalAIでデプロイされた大型言語モデルの推論および埋め込み機能をローカルで接続することをサポートしています。

## LocalAIのデプロイ

### 使用前の注意事項

もしコンテナのIPアドレスを直接使用する必要がある場合、上記の手順がその情報を取得するのに役立ちます。

### デプロイ開始

公式の[入門ガイド](https://localai.io/basics/getting_started/)を参考にデプロイを行うか、以下の手順で迅速に接続を行うことができます：

（以下の手順は[LocalAI Data query example](https://github.com/go-skynet/LocalAI/blob/master/examples/langchain-chroma/README.md)から引用しています）

1. まず、LocalAIのコードリポジトリをクローンし、指定のディレクトリに移動します

    ```bash
    $ git clone https://github.com/go-skynet/LocalAI
    $ cd LocalAI/examples/langchain-chroma
    ```

2. サンプルのLLMと埋め込みモデルをダウンロードします

    ```bash
    $ wget https://huggingface.co/skeskinen/ggml/resolve/main/all-MiniLM-L6-v2/ggml-model-q4_0.bin -O models/bert
    $ wget https://gpt4all.io/models/ggml-gpt4all-j.bin -O models/ggml-gpt4all-j
    ```

    ここでは、小型で全プラットフォーム対応の2つのモデルを選んでいます。`ggml-gpt4all-j`がデフォルトのLLMモデルとして、`all-MiniLM-L6-v2`がデフォルトの埋め込みモデルとして使用され、ローカルで迅速にデプロイすることができます。

3. .envファイルを設定します

   ```shell
   $ mv .env.example .env
   ```

   注意点：`.env`内のTHREADS変数の値が、あなたのマシンのCPUコア数を超えないことを確認してください。

4. LocalAIを起動します

   ```shell
   # docker-composeを使用して起動
   $ docker-compose up -d --build
   
   # ログを追跡し、ビルドが完了するまで待つ
   $ docker logs -f langchain-chroma-api-1
   7:16AM INF Starting LocalAI using 4 threads, with models path: /models
   7:16AM INF LocalAI version: v1.24.1 (9cc8d9086580bd2a96f5c96a6b873242879c70bc)
   
    ┌───────────────────────────────────────────────────┐ 
    │                   Fiber v2.48.0                   │ 
    │               http://127.0.0.1:8080               │ 
    │       (bound on host 0.0.0.0 and port 8080)       │ 
    │                                                   │ 
    │ Handlers ............ 55  Processes ........... 1 │ 
    │ Prefork ....... Disabled  PID ................ 14 │ 
    └───────────────────────────────────────────────────┘ 
   ```

   ローカルの`http://127.0.0.1:8080`がLocalAIのAPIリクエストのエンドポイントとして開放されます。

   そして、以下の2つのモデルが提供されます：

   - LLMモデル：`ggml-gpt4all-j`

     外部アクセス名：`gpt-3.5-turbo`（この名前は`models/gpt-3.5-turbo.yaml`でカスタマイズ可能です）

   - 埋め込みモデル：`all-MiniLM-L6-v2`

     外部アクセス名：`text-embedding-ada-002`（この名前は`models/embeddings.yaml`でカスタマイズ可能です）

    > DifyをDockerでデプロイする場合、ネットワーク設定に注意し、DifyコンテナがXinferenceのエンドポイントにアクセスできることを確認してください。Difyコンテナ内からはlocalhostにアクセスできないため、ホストのIPアドレスを使用する必要があります。

5. LocalAI APIサービスがデプロイ完了したら、Difyでモデルを使用します

   `設定 > モデル供給者 > LocalAI`に以下を入力します：

   モデル1：`ggml-gpt4all-j`

   - モデルタイプ：テキスト生成

   - モデル名：`gpt-3.5-turbo`

   - サーバーURL：http://127.0.0.1:8080

     Difyがdockerデプロイの場合、ホストのドメイン名：http://<your-LocalAI-endpoint-domain>:8080を入力してください。例えば、局域網のIPアドレス：http://192.168.1.100:8080

   "保存"後、アプリケーション内でこのモデルを使用できます。

   モデル2：`all-MiniLM-L6-v2`

   - モデルタイプ：埋め込み

   - モデル名：`text-embedding-ada-002`

   - サーバーURL：http://127.0.0.1:8080

     > Difyがdockerデプロイの場合、ホストのドメイン名：http://<your-LocalAI-endpoint-domain>:8080を入力してください。例えば、局域網のIPアドレス：http://192.168.1.100:8080

   "保存"後、アプリケーション内でこのモデルを使用できます。

LocalAIに関する詳しい情報については、https://github.com/go-skynet/LocalAI を参照してください。