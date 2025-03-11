# Integrate Open Source Models from Hugging Face

Dify supports Text-Generation and Embeddings. Below are the corresponding Hugging Face model types:

* Text-Generation：[text-generation](https://huggingface.co/models?pipeline\_tag=text-generation\&sort=trending)，[text2text-generation](https://huggingface.co/models?pipeline\_tag=text2text-generation\&sort=trending)
* Embeddings：[feature-extraction](https://huggingface.co/models?pipeline\_tag=feature-extraction\&sort=trending)

The specific steps are as follows:

1. You need a Hugging Face account ([registered address](https://huggingface.co/join)).
2. Set the API key of Hugging Face ([obtain address](https://huggingface.co/settings/tokens)).
3. Select a model to enter the [Hugging Face model list page](https://huggingface.co/models?pipeline\_tag=text-generation\&sort=trending).

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/af8a771b1e71152837e0f25b87a4471e.png)

Dify supports accessing models on Hugging Face in two ways:

1. Hosted Inference API. This method uses the model officially deployed by Hugging Face. No fee is required. But the downside is that only a small number of models support this approach.
2. Inference Endpoint. This method uses resources such as AWS accessed by the Hugging Face to deploy the model and requires payment.

### Models that access the Hosted Inference API

#### 1 Select a model

Hosted inference API is supported only when there is an area containing Hosted inference API on the right side of the model details page. As shown in the figure below:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/dc5a5584cef16fe76595058d37043546.png)

On the model details page, you can get the name of the model.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/248a80fb0dac520e690cb122dbe91324.png)

#### 2 Using access models in Dify

Select Hosted Inference API for Endpoint Type in `Settings > Model Provider > Hugging Face > Model Type`. As shown below:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/425f762f4b4b88d7ff69f5e3e898e6d0.png)

API Token is the API Key set at the beginning of the article. The model name is the model name obtained in the previous step.

### Method 2: Inference Endpoint

#### 1 Select the model to deploy

Inference Endpoint is only supported for models with the Inference Endpoints option under the Deploy button on the right side of the model details page. As shown below:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/0821340197577ff126440b2558446890.png)

#### 2 Deployment model

Click the Deploy button for the model and select the Inference Endpoint option. If you have not bound a bank card before, you will need to bind the card. Just follow the process. After binding the card, the following interface will appear: modify the configuration according to the requirements, and click Create Endpoint in the lower left corner to create an Inference Endpoint.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/f7582adc0937dc4f038e462b578d9c17.png)

After the model is deployed, you can see the Endpoint URL.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/30c38995813c0d05c35c42dc0f1d467c.png)

#### 3 Using access models in Dify

Select Inference Endpoints for Endpoint Type in `Settings > Model Provider > Hugging face > Model Type`. As shown below:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/736421b38ac731e58585487ca2040c8b.png)

The API Token is the API Key set at the beginning of the article. `The name of the Text-Generation model can be arbitrary, but the name of the Embeddings model needs to be consistent with Hugging Face.` The Endpoint URL is the Endpoint URL obtained after the successful deployment of the model in the previous step.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/6a8908cace5b287070577bf555d69b0c.png)

> Note: The "User name / Organization Name" for Embeddings needs to be filled in according to your deployment method on Hugging Face's [Inference Endpoints](https://huggingface.co/docs/inference-endpoints/guides/access), with either the ''[User name](https://huggingface.co/settings/account)'' or the "[Organization Name](https://ui.endpoints.huggingface.co/)".
