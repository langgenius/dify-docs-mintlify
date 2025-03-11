# Ollama + DeepSeek + Dify のプライベートデプロイ：あなた自身のAIアシスタントの構築方法

## 概要

DeepSeekは、革新的なオープンソースの大規模言語モデル（LLM）であり、高度なアルゴリズムアーキテクチャと内省的な推論能力によって、AIを活用した会話に新たな体験をもたらします。プライベート環境にデプロイすることで、データセキュリティとシステム構成を完全に制御しながら、デプロイ戦略の柔軟性を維持できます。

Difyは、オープンソースのAIアプリケーション開発プラットフォームであり、完全なプライベートデプロイメントソリューションを提供します。ローカルにデプロイしたDeepSeekモデルをDifyプラットフォームにシームレスに統合することで、企業はデータプライバシーを確保しつつ、独自のインフラストラクチャ内で強力なAIアプリケーションを構築できます。

### プライベートデプロイメントの利点：

- **優れたパフォーマンス**: 商用モデルに匹敵する会話体験を提供します。
- **隔離された環境**: 完全にオフラインで動作し、データ漏洩のリスクを排除します。
- **完全なデータ制御**: データ資産の完全な所有権を保持し、コンプライアンスを確保できます。

---

## 前提条件

### **ハードウェア要件：**
- **CPU**: 2コア以上
- **RAM/GPUメモリ**: 16GiB以上（推奨）

### **ソフトウェア要件：**
- [Docker](https://www.docker.com/)
- Docker Compose
- [Ollama](https://ollama.com/)
- [Dify Community Edition](https://github.com/langgenius/dify)

---

## デプロイ手順

### 1. Ollama のインストール

[Ollama](https://ollama.com/)は、DeepSeek、Llama、Mistralなどの大規模言語モデルをシームレスにデプロイできるクロスプラットフォームのLLM管理クライアント（MacOS、Windows、Linux）です。Ollamaは、ワンクリックでモデルをデプロイできるソリューションを提供し、すべてのデータがローカルに保存されるため、セキュリティとプライバシーが完全に保護されます。

[Ollamaの公式サイト](https://ollama.com/)にアクセスし、お使いのプラットフォームのインストール手順に従ってください。インストール後、次のコマンドを実行して検証します。

```bash
➜  ~ ollama -v
ollama version is 0.5.5
```

利用可能なハードウェアに基づいて、適切なDeepSeekモデルサイズを選択してください。最初のインストールには7Bモデルを推奨します。

![](https://assets-docs.dify.ai/2025/01/26978571a8d5f7188a952606f62e6a32.png)

次のコマンドを実行して、DeepSeek R1モデルをインストールします。

```bash
ollama run deepseek-r1:7b
```

![](https://assets-docs.dify.ai/2025/01/9297451d07d7704f73d6db0a83842f5f.png)

### 2. Dify Community Edition のインストール

Dify GitHubリポジトリをクローンし、インストール手順に従います。

```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
docker compose up -d  # Docker Compose V1 を使用している場合は、`docker-compose up -d` を使用してください
```

コマンドを実行すると、すべてのコンテナが適切なポートマッピングで実行されていることを確認できるはずです。詳細な手順については、[Docker Composeでのデプロイ](https://docs.dify.ai/getting-started/install-self-hosted/docker-compose)を参照してください。

Dify Community Editionは、デフォルトでポート80で実行されます。プライベートなDifyプラットフォームには、`http://your_server_ip` でアクセスできます。

### 3. DeepSeek と Dify の統合

Difyプラットフォームの **Profile → Settings → Model Providers** に移動します。**Ollama** を選択し、**Add Model** をクリックします。

> 注：Model Providers の「DeepSeek」オプションはオンラインAPIサービスを指しますが、OllamaオプションはローカルにデプロイされたDeepSeekモデルに使用します。

モデルを構成します。
•	モデル名：デプロイしたモデル名（例：`deepseek-r1:7b`）を入力します。
•	ベースURL：OllamaクライアントのローカルサービスURL（通常は `http://your_server_ip:11434`）を設定します。
接続問題が発生した場合は、[よくある質問](https://docs.dify.ai/ja-jp/learn-more/use-cases/private-ai-ollama-deepseek-dify#id-1-docker-noer)をご参照ください。
•	その他の設定：デフォルト値を保持します。[DeepSeekモデルの仕様](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)によると、最大トークン長は32,768です。

![](https://assets-docs.dify.ai/2025/01/6f3b53427e46786ba7d1374739344142.png)

## AI アプリケーションの構築

### DeepSeek AI チャットボット（シンプルなアプリケーション）

1. Difyホームページで、Create Blank App をクリックし、Chatbot を選択して名前を付けます。

![](https://assets-docs.dify.ai/2025/01/7f56bc3c836c7248043b656fa95e474e.png)

2. Model Provider セクションで、Ollama の下にある `deepseek-r1:7b` モデルを選択します。

![](https://assets-docs.dify.ai/2025/01/dbd7170abd35f545481ecc0beef85333.png)

3. チャットプレビューにメッセージを入力して、モデルの応答を確認します。正しく応答すれば、チャットボットはオンラインになります。

![](https://assets-docs.dify.ai/2025/01/619fbbd48e55a1e6a598b4039dd631f5.png)

4. Publish ボタンをクリックして、共有可能なリンクを取得するか、チャットボットを他のWebサイトに埋め込みます。

### DeepSeek AI チャットフロー/ワークフロー（高度なアプリケーション）

> チャットフロー/ワークフローアプリケーションを使用すると、ドキュメント認識、画像処理、音声認識などのより複雑なAIソリューションを作成できます。詳細については、[ワークフローのドキュメント](https://docs.dify.ai/guides/workflow)をご覧ください。

1.	Create Blank App をクリックし、Chatflow または Workflow を選択して、アプリケーションに名前を付けます。

![](https://assets-docs.dify.ai/2025/01/cb8637be4dca5a0e684fd9a21df3711f.png)

2.	LLMノードを追加し、Ollama の下にある `deepseek-r1:7b` モデルを選択し、`{{#sys.query#}}` 変数をシステムプロンプトに使用して、最初のノードに接続します。APIの問題が発生した場合は、[ロードバランシング](https://docs.dify.ai/guides/model-configuration/load-balancing)または[エラー処理](https://docs.dify.ai/guides/workflow/error-handling)ノードを使用して処理できます。

3.	LLMノードを追加し、Ollamaフレームワークの下にあるdeepseek-r1:7bモデルを選択し、{{#sys.query#}}変数をシステムプロンプトに挿入して、最初のノードに接続します。APIの問題が発生した場合は、ロードバランシングまたはエラー処理ノードを使用して処理できます。

![](https://assets-docs.dify.ai/2025/01/c21f076398eb09d773d3e543561293e6.png)

4.	Endノードを追加して構成を完了します。クエリを入力してワークフローをテストします。応答が正しければ、セットアップは完了です。

![](https://assets-docs.dify.ai/2025/01/820c37c70cb029cba60ca289e8d6e89a.png)

## FAQ

### 1. Docker 使用時の接続エラー

Docker内でDifyとOllamaを実行すると、次のエラーが発生する場合があります。

```bash
httpconnectionpool(host=127.0.0.1, port=11434): max retries exceeded with url:/cpi/chat
(Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f8562812c20>:
fail to establish a new connection:[Errno 111] Connection refused'))
```

**原因**:

`localhost` はコンテナ自体を指すため、Ollama は Docker コンテナ内からアクセスできません。

**解決策**:

**Mac での環境変数の設定**:

Ollama が macOS アプリケーションとして実行されている場合、環境変数は `launchctl` を使用して設定する必要があります。

1.  各環境変数に対して、`launchctl setenv` を呼び出します。

    ```bash
    launchctl setenv OLLAMA_HOST "0.0.0.0"
    ```
2.  Ollama アプリケーションを再起動します。

3.  上記の手順が効果がない場合は、次の方法を試してください。

    問題は Docker 自体にあり、Docker ホストにアクセスする必要があります。`host.docker.internal` に接続する必要があります。したがって、サービス内で `localhost` を `host.docker.internal` に置き換えると、正常に動作します。

    ```bash
    http://host.docker.internal:11434
    ```

**Linuxでの環境変数の設定**:

Ollama が systemd サービスとして実行されている場合、環境変数は `systemctl` を使用して設定する必要があります。

1. `systemctl edit ollama.service` を呼び出して、systemd サービスを編集します。これにより、エディターが開きます。
2.  各環境変数に対して、`[Service]` セクションの下に `Environment` 行を追加します。

    ```ini
    [Service]
    Environment="OLLAMA_HOST=0.0.0.0"
    ```
3. 保存して終了します。
4.  `systemd` をリロードし、Ollama を再起動します。

    ```bash
    systemctl daemon-reload
    systemctl restart ollama
    ```

**Windows での環境変数の設定**:

Windows では、Ollama はユーザーとシステムの環境変数を継承します。

1.  まず、タスクバーで Ollama をクリックして終了します。
2.  コントロールパネルからシステムの環境変数を編集します。
3.  `OLLAMA_HOST`、`OLLAMA_MODELS` などのユーザーアカウントの新しい変数を作成または編集します。
4.  [OK]/[適用] をクリックして保存します。
5.  新しいターミナルウィンドウから `ollama` を実行します。

### 2. Ollama サービスのポートとアドレスを変更する方法

Ollama はデフォルトで 127.0.0.1 のポート 11434 にバインドされています。`OLLAMA_HOST` 環境変数を使用して、バインドアドレスを変更します。