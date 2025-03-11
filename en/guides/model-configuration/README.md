---
description: Learn about the Different Models Supported by Dify.
---

# Model

Dify is a development platform for AI application based on LLM Apps, when you are using Dify for the first time, you need to go to **Settings --> Model Providers** to add and configure the LLM you are going to use.

![Settings - Model Provider](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/model-configuration/941524058c800a06d39290c48d14673b.png)

Dify supports major model providers like OpenAI's GPT series and Anthropic's Claude series. Each model's capabilities and parameters differ, so select a model provider that suits your application's needs. **Obtain the API key from the model provider's official website before using it in Dify.**

## Model Types in Dify

Dify classifies models into 4 types, each for different uses:

1.  **System Inference Models:** Used in applications for tasks like chat, name generation, and suggesting follow-up questions.

    > Providers include [OpenAI](https://platform.openai.com/account/api-keys)、[Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)、[Anthropic](https://console.anthropic.com/account/keys)、Hugging Face Hub、Replicate、Xinference、OpenLLM、[iFLYTEK SPARK](https://www.xfyun.cn/solutions/xinghuoAPI)、[WENXINYIYAN](https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application)、[TONGYI](https://dashscope.console.aliyun.com/api-key\_management?spm=a2c4g.11186623.0.0.3bbc424dxZms9k)、[Minimax](https://api.minimax.chat/user-center/basic-information/interface-key)、ZHIPU(ChatGLM)、[Ollama](https://docs.dify.ai/tutorials/model-configuration/ollama)、[LocalAI](https://github.com/mudler/LocalAI)、[GPUStack](https://github.com/gpustack/gpustack).
2.  **Embedding Models:** Employed for embedding segmented documents in knowledge and processing user queries in applications.

    > Providers include OpenAI, ZHIPU (ChatGLM), Jina AI([Jina Embeddings](https://jina.ai/embeddings/)).
3.  [**Rerank Models**](https://docs.dify.ai/advanced/retrieval-augment/rerank)**:** Enhance search capabilities in LLMs.

    > Providers include Cohere, Jina AI([Jina Reranker](https://jina.ai/reranker)).
4.  **Speech-to-Text Models:** Convert spoken words to text in conversational applications.

    > Provider: OpenAI.

Dify plans to add more LLM providers as technology and user needs evolve.

## Hosted Model Trial Service

Dify offers trial quotas for cloud service users to experiment with different models. Set up your model provider before the trial ends to ensure uninterrupted application use.

* OpenAI Hosted Model Trial: Includes 200 invocations for models like GPT3.5-turbo, GPT3.5-turbo-16k, text-davinci-003 models.

## Setting the Default Model

Dify automatically selects the default model based on usage. Configure this in `Settings > Model Provider`.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/model-configuration/c5ac5f32deb020a8aae46045d3ee9c8d.png)

## Model Integration Settings

Choose your model in Dify's `Settings > Model Provider`.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/model-configuration/b55cb7d0dcff7ef14cdf6e6aca207790.png)

Model providers fall into two categories:

1. Proprietary Models: Developed by providers such as OpenAI and Anthropic.
2. Hosted Models: Offer third-party models, like Hugging Face and Replicate.

Integration methods differ between these categories.

**Proprietary Model Providers:** Dify connects to all models from an integrated provider. Set the provider's API key in Dify to integrate.

{% hint style="info" %}
Dify uses [PKCS1\_OAEP](https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html) encryption to protect your API keys. Each user (tenant) has a unique key pair for encryption, ensuring your API keys remain confidential.
{% endhint %}

**Hosted Model Providers:** Integrate third-party models individually.

Specific integration methods are not detailed here.

* [Hugging Face](../../development/models-integration/hugging-face.md)
* [Replicate](../../development/models-integration/replicate.md)
* [Xinference](../../development/models-integration/xinference.md)
* [OpenLLM](../../development/models-integration/openllm.md)

## Using Models

Once configured, these models are ready for application use.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/model-configuration/6e74424124cfcfe224d3c083f90b54d2.png)
