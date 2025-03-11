# Ollamaでデプロイしたローカルモデルを統合

![ollama](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/4b23476f2be72e5c1acb9a3e5714b191.png)

[Ollama](https://github.com/jmorganca/ollama)は、Llama 2、Mistral、LlavaといったLLMを簡単にデプロイできるように設計された、クロスプラットフォーム対応の推論フレームワーククライアントです（MacOS、Windows、Linuxに対応）。ワンクリックでセットアップできるOllamaを利用すれば、LLMをローカル環境で実行でき、データを手元のマシンに保持することで、データプライバシーとセキュリティを強化できます。

## 簡単な統合

### Ollamaのダウンロードと起動

1.  Ollamaをダウンロード

    [https://ollama.com/download](https://ollama.com/download)にアクセスし、お使いのシステムに対応したOllamaクライアントをダウンロードしてください。

2.  Ollamaを実行し、Llama3.2とチャット

    ```bash
    ollama run llama3.2
    ```
    
    起動が成功すると、Ollamaはローカルポート11434でAPIサービスを開始します。このサービスには、`http://localhost:11434`からアクセスできます。

    他のモデルについては、[Ollama Models](https://ollama.com/library)で詳細をご確認ください。

3.  DifyへのOllama統合

    Difyの設定画面で、「モデルプロバイダー」>「Ollama」を選択し、以下の情報を入力します。

    ![](../../.gitbook/assets/ollama-config-en.png)

    *   モデル名: `llama3.2`
    *   ベースURL: `http://<your-ollama-endpoint-domain>:11434`

        OllamaサービスにアクセスできるベースURLを入力してください。パブリックURLを入力してもエラーが発生する場合は、[FAQ](#faq)を参照し、すべてのIPアドレスからOllamaサービスにアクセスできるよう環境変数を変更してください。

        DifyをDockerでデプロイしている場合は、ローカルネットワークのIPアドレス（例：`http://192.168.1.100:11434` や `http://host.docker.internal:11434`）を使用してサービスにアクセスすることを推奨します。

        ローカルでソースコードをデプロイしている場合は、`http://localhost:11434` を使用してください。

    *   モデルタイプ: `Chat`
    *   モデルコンテキスト長: `4096`

        モデルが一度に処理できる最大コンテキスト長です。不明な場合は、デフォルト値の4096を使用してください。
    *   最大トークン制限: `4096`

        モデルが返す最大トークン数です。モデルに特別な要件がない場合は、モデルのコンテキスト長と同じ値に設定できます。
    *   Visionのサポート: `はい`

        `llava`のように、画像認識（マルチモーダル）をサポートするモデルを使用する場合は、このオプションをオンにしてください。

    エラーがないことを確認したら、「保存」をクリックして、アプリでモデルを使用します。

    Embeddingモデルの統合もLLMと同様の手順で行いますが、モデルタイプを「Text Embedding」に変更するだけです。

4.  Ollamaモデルの使用

    ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/aa3207efbcc2121ae5e03b233c90167a.png)

    設定が必要なアプリの「プロンプトエンジニアリング」ページを開き、Ollamaプロバイダーの中から`llava`モデルを選択し、モデルパラメーターを設定して使用します。

## FAQ

### ⚠️ DifyとOllamaをDockerでデプロイしている場合、以下のエラーが発生することがあります。

```bash
httpconnectionpool(host=127.0.0.1, port=11434): max retries exceeded with url:/cpi/chat (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f8562812c20>: fail to establish a new connection:[Errno 111] Connection refused'))

httpconnectionpool(host=localhost, port=11434): max retries exceeded with url:/cpi/chat (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f8562812c20>: fail to establish a new connection:[Errno 111] Connection refused'))
```

このエラーは、OllamaサービスがDockerコンテナからアクセスできない場合に発生します。`localhost` は通常、ホストマシンや他のコンテナではなく、コンテナ自体を指します。

この問題を解決するには、Ollamaサービスをネットワークに公開する必要があります。

### Macでの環境変数の設定

OllamaをmacOSアプリとして実行している場合は、環境変数を `launchctl` を使用して設定する必要があります。

1.  各環境変数に対して、`launchctl setenv` を実行します。

    ```bash
    launchctl setenv OLLAMA_HOST "0.0.0.0"
    ```

2. Ollamaアプリを再起動します。

3. 上記の手順で解決しない場合は、以下の方法を試してください。

    問題はDocker自体にあり、Dockerホストにアクセスするには、`host.docker.internal` に接続する必要があります。したがって、サービス内で `localhost` を `host.docker.internal` に置き換えることで、正常に動作するようになります。

    ```bash
    http://host.docker.internal:11434
    ```

### Linuxでの環境変数の設定

Ollamaをsystemdサービスとして実行している場合は、環境変数を `systemctl` を使用して設定する必要があります。

1. `systemctl edit ollama.service` を実行してsystemdサービスを編集します。これにより、エディターが開きます。
2. 各環境変数に対して、`[Service]` セクションの下に `Environment` 行を追加します。

    ```ini
    [Service]
    Environment="OLLAMA_HOST=0.0.0.0"
    ```
3.  保存してエディターを閉じます。
4.  `systemd` をリロードし、Ollamaを再起動します。

    ```bash
    systemctl daemon-reload
    systemctl restart ollama
    ```

### Windowsでの環境変数の設定

Windowsでは、Ollamaはユーザーとシステムの環境変数を継承します。

1.  まず、タスクバーにあるOllamaのアイコンをクリックしてOllamaを終了します。
2.  コントロールパネルからシステム環境変数を編集します。
3.  `OLLAMA_HOST` や `OLLAMA_MODELS` など、ユーザーアカウントの新しい環境変数を作成または編集します。
4.  [OK/適用] をクリックして保存します。
5.  新しいターミナルウィンドウから `ollama` を実行します。

## ネットワーク上でOllamaを公開するにはどうすればよいですか？

Ollamaはデフォルトで127.0.0.1のポート11434にバインドされています。`OLLAMA_HOST` 環境変数を使用して、バインドするアドレスを変更してください。

## 詳細情報

Ollamaの詳細については、以下を参照してください。

* [Ollama](https://github.com/jmorganca/ollama)
* [Ollama FAQ](https://github.com/ollama/ollama/blob/main/docs/faq.md)