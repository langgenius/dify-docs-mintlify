# モデル

Difyは大規模言語モデルに基づいたAIアプリケーション開発プラットフォームです。初めて使用する際には、Difyの**設定 -- モデルプロバイダー**ページで必要なモデルを追加および設定してください。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/model-configuration/458a37f10d6f0d08c3701aa86c447983.png)

Difyは現在、OpenAIのGPTシリーズやAnthropicのClaudeシリーズなど、主流のモデルプロバイダーをサポートしています。異なるモデルの能力やパラメータの種類が異なるため、アプリケーションのニーズに応じて適切なモデルプロバイダーを選択できます。**Difyで以下のモデル能力を使用する前に、各モデルプロバイダーの公式サイトでAPIキーを取得する必要があります。**

### モデルタイプ

Difyでは、モデルの使用シーンに応じて以下の4つのタイプに分類しています：

1.  **システム推論モデル**。アプリケーション内で使用されるのはこのタイプのモデルです。チャット、会話名生成、次の質問の提案でもこの推論モデルが使用されます。

    > サポートされているシステム推論モデルプロバイダー：[OpenAI](https://platform.openai.com/account/api-keys)、[Azure OpenAIサービス](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)、[Anthropic](https://console.anthropic.com/account/keys)、Hugging Faceハブ、Replicate、Xinference、OpenLLM、[讯飞星火](https://www.xfyun.cn/solutions/xinghuoAPI)、[文心一言](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application)、[通义千问](https://dashscope.console.aliyun.com/api-key\_management?spm=a2c4g.11186623.0.0.3bbc424dxZms9k)、[Minimax](https://api.minimax.chat/user-center/basic-information/interface-key)、ZHIPU(ChatGLM)
2.  **埋め込みモデル**。データセット内の分割された文書の埋め込みに使用されるのはこのタイプのモデルです。データセットを使用するアプリケーションでは、ユーザーの質問を埋め込み処理する際にもこのタイプのモデルが使用されます。

    > サポートされている埋め込みモデルプロバイダー：OpenAI、ZHIPU(ChatGLM)、Jina AI([Jina Embeddings](https://jina.ai/embeddings/))
3.  [**Rerankモデル**](https://docs.dify.ai/v/ja-jp/learn-more/extended-reading/retrieval-augment/rerank)。**Rerankモデルは検索能力を強化し、LLMの検索結果を改善するために使用されます。**

    > サポートされているRerankモデルプロバイダー：Cohere、Jina AI([Jina Reranker](https://jina.ai/reranker))
4.  **音声からテキストへのモデル**。対話型アプリケーションで音声をテキストに変換する際に使用されるのはこのタイプのモデルです。

    > サポートされている音声からテキストへのモデルプロバイダー：OpenAI

技術の進化とユーザーのニーズに応じて、今後もさらに多くのLLMプロバイダーをサポートしていきます。

### ホストモデル試用サービス

Difyクラウドサービスのユーザーには、異なるモデルの試用枠を提供しています。この枠が尽きる前に自分のモデルプロバイダーを設定してください。さもないと、アプリケーションの正常な使用に影響を及ぼす可能性があります。

* **OpenAIホストモデル試用：** GPT3.5-turbo、GPT3.5-turbo-16k、text-davinci-003モデルの試用として200回の呼び出し回数を提供します。

### デフォルトモデルの設定

Difyは使用シーンに応じて設定されたデフォルトモデルを選択します。`設定 > モデルプロバイダー`でデフォルトモデルを設定します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/model-configuration/22d9f76bae0f0b0a492ce465d3cb0f38.png)

システム推論モデル：アプリケーションの作成に使用されるデフォルトの推論モデルを設定し、対話名の生成や次のステップの質問に関する提案などの機能も含まれます。

### モデルの接続設定

Difyの`設定 > モデルプロバイダー`で接続するモデルを設定します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/model-configuration/a5ec4a8508382ff895a375aa19b84e53.png)

モデルプロバイダーは2種類に分かれます：

1. 自社モデル。このタイプのモデルプロバイダーは自社で開発したモデルを提供します。例としてOpenAI、Anthropicなどがあります。
2. ホストモデル。このタイプのモデルプロバイダーは第三者のモデルを提供します。例としてHugging Face、Replicateなどがあります。

Difyで異なるタイプのモデルプロバイダーを接続する方法は若干異なります。

**自社モデルのモデルプロバイダーの接続**

自社モデルのプロバイダーを接続すると、Difyはそのプロバイダーのすべてのモデルに自動的に接続します。

Difyで対応するモデルプロバイダーのAPIキーを設定するだけで、そのモデルプロバイダーに接続できます。

{% hint style="info" %}
Difyは[PKCS1\_OAEP](https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html)を使用してユーザーが管理するAPIキーを暗号化して保存しています。各テナントは独立した鍵ペアを使用して暗号化しており、APIキーの漏洩を防止します。
{% endhint %}

**ホストモデルのモデルプロバイダーの接続**

ホストタイプのプロバイダーには多くの第三者モデルがあります。モデルの接続には個別に追加が必要です。具体的な接続方法は以下の通りです：

* [Hugging Face](hugging-face.md)
* [Replicate](replicate.md)
* [Xinference](xinference.md)
* [OpenLLM](openllm.md)

### モデルの使用

モデルの設定が完了したら、アプリケーションでこれらのモデルを使用できます：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/model-configuration/961fa0a4c3b9e11615170b9851e6a583.png)
