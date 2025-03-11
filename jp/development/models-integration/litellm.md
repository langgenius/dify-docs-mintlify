# LiteLLM Proxyを使用してモデルを統合する

[LiteLLM Proxy](https://github.com/BerriAI/litellm)は、以下の機能を提供するプロキシサーバーとなります：

- OpenAI形式の100以上のLLM（OpenAI、Azure、Vertex、Bedrock）への呼び出し
- 予算やレート制限の設定、利用状況の追跡には仮想キーを使用します

Difyは、LiteLLM Proxyで利用可能なLLMおよびテキスト埋め込み機能モデルを統合するサポートを提供します。

## クイック統合

### ステップ1. LiteLLM Proxyサーバーを起動する

LiteLLMには、すべてのモデルが定義された構成が必要です。このファイルを `litellm_config.yaml` と呼びます。

[LiteLLM構成の設定方法のドキュメント - こちら](https://docs.litellm.ai/docs/proxy/configs)

```yaml
model_list:
  - model_name: gpt-4
    litellm_params:
      model: azure/chatgpt-v-2
      api_base: https://openai-gpt-4-test-v-1.openai.azure.com/
      api_version: "2023-05-15"
      api_key: 
  - model_name: gpt-4
    litellm_params:
      model: azure/gpt-4
      api_key: 
      api_base: https://openai-gpt-4-test-v-2.openai.azure.com/
  - model_name: gpt-4
    litellm_params:
      model: azure/gpt-4
      api_key: 
      api_base: https://openai-gpt-4-test-v-2.openai.azure.com/
```

### ステップ2. LiteLLM Proxyを起動する

```shell
docker run \
    -v $(pwd)/litellm_config.yaml:/app/config.yaml \
    -p 4000:4000 \
    ghcr.io/berriai/litellm:main-latest \
    --config /app/config.yaml --detailed_debug
```

成功すると、プロキシは `http://localhost:4000` で実行されます。

### ステップ3. DifyでLiteLLM Proxyを統合する

`設定 > モデルプロバイダー > OpenAI-API互換` で、以下を入力してください：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/c02feef6b054be16639ecd23ce10b605.png)

- モデル名: `gpt-4`
- ベースURL: `http://localhost:4000`

    LiteLLMサービスにアクセス可能なベースURLを入力します。
- モデルタイプ: `Chat`
- モデルコンテキスト長: `4096`

    モデルの最大コンテキスト長。不明な場合は、デフォルト値の4096を使用してください。
- トークンの最大制限: `4096`

    モデルによって返されるトークンの最大数。モデルに特定の要件がない場合は、モデルコンテキスト長と一致させることができます。
- ビジョンのサポート: `Yes`

    `gpt4-o`のように画像理解（マルチモーダル）をサポートする場合は、このオプションをチェックしてください。

エラーがないことを確認したら、「保存」をクリックしてアプリケーションでモデルを使用してください。

埋め込みモデルの統合方法はLLMと同様で、モデルタイプをテキスト埋め込みに変更するだけです。

## 詳細情報

LiteLLMに関する詳細情報は、以下を参照してください：

- [LiteLLM](https://github.com/BerriAI/litellm)
- [LiteLLM Proxyサーバー](https://docs.litellm.ai/docs/simple_proxy)