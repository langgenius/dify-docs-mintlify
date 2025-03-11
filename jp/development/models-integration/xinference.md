# Xinferenceでデプロイしたローカルモデルを統合

[Xorbits推論](https://github.com/xorbitsai/inference)は、大型言語モデル、音声認識モデル、マルチモーダルモデルにサービスを提供するための強力で汎用的な分散推論フレームワークであり、ノートパソコンでも使用可能です。chatglm、baichuan、whisper、vicuna、orcaなど、GGML互換の多くのモデルをサポートしています。Difyは、ローカルにデプロイされたXinferenceの大型言語モデル推論および埋め込み機能を接続することができます。

## Xinferenceのデプロイ

### デプロイの開始

Xinferenceのデプロイ方法は、[ローカルデプロイ](https://github.com/xorbitsai/inference/blob/main/README_zh_CN.md#%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2)と[分散デプロイ](https://github.com/xorbitsai/inference/blob/main/README_zh_CN.md#%E5%88%86%E5%B8%83%E5%BC%8F%E9%83%A8%E7%BD%B2)の2つがあります。ここではローカルデプロイを例に説明します。

1.  まず、PyPIを使用してXinferenceをインストールします：

    ```bash
    $ pip install "xinference[all]"
    ```
2.  ローカルデプロイ方式でXinferenceを起動します：

    ```bash
    $ xinference-local
    2023-08-20 19:21:05,265 xinference   10148 INFO     Xinference successfully started. Endpoint: http://127.0.0.1:9997
    2023-08-20 19:21:05,266 xinference.core.supervisor 10148 INFO     Worker 127.0.0.1:37822 has been added successfully
    2023-08-20 19:21:05,267 xinference.deploy.worker 10148 INFO     Xinference worker successfully started.
    ```

    Xinferenceはデフォルトでローカルにワーカーを起動し、エンドポイントは`http://127.0.0.1:9997`、ポートはデフォルトで`9997`です。デフォルトではローカルホストからのみアクセス可能ですが、`-H 0.0.0.0`を設定することで、外部クライアントからもアクセス可能になります。ホストやポートのさらに詳細な設定方法については、`xinference-local --help`で確認できます。
    > Dify Dockerデプロイ方式を使用する場合、ネットワーク設定に注意が必要です。DifyコンテナがXinferenceのエンドポイントにアクセスできるように設定してください。Difyコンテナ内部からローカルホストにはアクセスできないため、ホストマシンのIPアドレスを使用する必要があります。

3.  モデルの作成とデプロイ

    `http://127.0.0.1:9997`にアクセスし、デプロイするモデルとその仕様を選択します。以下の図を参照してください：

    ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/6945f8e7a0ae88d1f67f988d53d420bd.png)

    モデルによっては異なるハードウェアプラットフォームでの互換性が異なるため、[Xinference内蔵モデル](https://inference.readthedocs.io/en/latest/models/builtin/index.html)を確認して、作成するモデルが現在のハードウェアプラットフォームでサポートされているかどうかを確認してください。
4.  モデルUIDの取得

    上記ページから対応するモデルのIDを取得します。例：`2c886330-8849-11ee-9518-43b0b8f40bea`
5.  モデルのデプロイ完了後、Difyでのモデル接続

    `設定 > モデルプロバイダー > Xinference`に以下を入力します：

    * モデル名称：`vicuna-v1.3`
    * サーバーURL：`http://<Machine_IP>:9997` **あなたのマシンのIPアドレスに置き換えてください**
    * モデルUID：`2c886330-8849-11ee-9518-43b0b8f40bea`

    "保存"をクリックすると、アプリケーションでそのモデルを使用できます。

Difyはまた、[Xinference埋め込みモデル](https://github.com/xorbitsai/inference/blob/main/README_zh_CN.md#%E5%86%85%E7%BD%AE%E6%A8%A1%E5%9E%8B)をEmbeddingモデルとして使用することもサポートしています。設定ボックスで`Embeddings`タイプを選択するだけで使用可能です。

Xinferenceの詳細については、[Xorbits推論](https://github.com/xorbitsai/inference/blob/main/README_zh_CN.md)を参照してください。