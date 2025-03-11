# LLM Configuration and Usage

### 1. How to access OpenAI via a proxy server in China?

Dify supports custom API domain names for OpenAI and any large model API server compatible with OpenAI. In the community edition, you can fill in the target server address through **Settings --> Model Providers --> OpenAI --> Edit API**.

### 2. How to choose a base model?

* **gpt-3.5-turbo**: gpt-3.5-turbo is an upgraded version of the gpt-3 model series. It is more powerful than gpt-3 and can handle more complex tasks. It has significant improvements in understanding long texts and cross-document reasoning. gpt-3.5-turbo can generate more coherent and persuasive text. It has also greatly improved in summarization, translation, and creative writing. Specializes in: **Long text understanding, cross-document reasoning, summarization, translation, creative writing.**
* **gpt-4**: gpt-4 is the latest and most powerful Transformer language model. It has approximately 20 billion pre-trained parameters, making it top-notch in all language tasks, especially those requiring deep understanding and generation of long, complex responses. gpt-4 can handle all aspects of human language, including understanding abstract concepts and cross-page reasoning. gpt-4 is the first truly universal language understanding system capable of handling any natural language processing task within the AI domain. Specializes in: **All NLP tasks, language understanding, long text generation, cross-document reasoning, abstract concept understanding.** For more details, refer to the [documentation](https://platform.openai.com/docs/models/overview).

### 3. Why is it recommended to set max_tokens smaller?

In natural language processing, longer text outputs usually require more computation time and resources. Therefore, limiting the length of the output text can reduce computational cost and time to some extent. For example, setting max_tokens=500 means only considering the first 500 tokens of the output text, and any part beyond this length will be discarded. This ensures that the output text length does not exceed the LLM's acceptable range and optimizes computational resources, improving model efficiency. Additionally, setting a smaller max_tokens allows for a longer prompt. For instance, gpt-3.5-turbo has a limit of 4097 tokens; if max_tokens=4000, only 97 tokens are left for the prompt, and exceeding this will cause an error.

### 4. How to reasonably split long texts in datasets?

In some natural language processing applications, texts are typically split by paragraphs or sentences to better handle and understand the semantic and structural information in the text. The smallest splitting unit depends on the specific task and technical implementation. For example:

* For text classification tasks, texts are usually split by sentences or paragraphs.
* For machine translation tasks, entire sentences or paragraphs are used as splitting units.

Finally, experiments and evaluations are needed to determine the most suitable embedding technique and splitting unit. You can compare the performance of different techniques and splitting units on the test set and choose the optimal solution.

### 5. What distance function do we use for dataset segmentation?

We use [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity). The choice of distance function is generally not critical. OpenAI embeddings are normalized to a length of 1, which means:

Using dot product can slightly speed up the calculation of cosine similarity

Cosine similarity and Euclidean distance will result in the same ranking

* If normalized embedding vectors are used to calculate cosine similarity or Euclidean distance and vectors are ranked based on these similarity measures, the ranking results will be the same. This is because, after normalization, the length of the vectors no longer affects their relative relationships; only directional information is retained. Therefore, when using normalized vectors for similarity measurement, different measurement methods will yield the same ranking results. After normalization, all vectors are scaled to a length of 1, meaning they all lie on the unit length. Unit vectors describe only direction without magnitude, as their length is always 1. _For specific principles, you can ask ChatGPT._

When embedding vectors are normalized to a length of 1, calculating the cosine similarity between two vectors can be simplified to their dot product. Since the normalized vector lengths are all 1, the dot product result is equivalent to the cosine similarity result. Given that dot product operations are faster than other similarity measures (like Euclidean distance), using normalized vectors for dot product calculations can slightly improve computational efficiency.

### 6. How to get free trial quotas for Zhipu·AI, iFlytek Spark, and MiniMax models?

We collaborate with major model providers to offer a certain amount of free token trial quotas to Chinese users. Through Dify **Settings --> Model Providers --> Show more model providers**, click "Get Free" on the Zhipu·AI, iFlytek Spark, or MiniMax icons. If you can't see the entrance in the English interface, switch the product language to Chinese:

* **Zhipu·AI: Get 10 million tokens for free.** Click "Get Free", enter your phone number and verification code to receive the quota, regardless of whether you have registered with Zhipu·AI before.
* **iFlytek Spark (V1.5 model, V2.0 model): Get 6 million tokens for free, 3 million tokens for each model, quotas are not interchangeable**. Enter through Dify, complete the registration on iFlytek Spark's open platform (only for phone numbers not previously registered with iFlytek Spark), return to Dify, wait for 5 minutes, and refresh the page to see the available quota.
* **MiniMax: Get 1 million tokens for free.** Click "Get Free" to receive the quota without manual registration, regardless of whether you have registered with MiniMax before.

Once the trial quota is credited, select the model you need to use in **Prompt Arrangement --> Model and Parameters --> Language Model**.

### 7. When filling in the OpenAI key, the validation failed with the error: "Validation failed: You exceeded your current quota, please check your plan and billing details." What is the reason?

This indicates that your OpenAI key's account has run out of funds. Please go to OpenAI to recharge.

### 8. When using OpenAI's key for conversation in the application, I encountered the following errors. What is the reason?

Error one:

```JSON
The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application
```

Error two:

```JSON
Rate limit reached for default-gpt-3.5-turbo in organization org-wDrZCxxxxxxxxxissoZb on requests per min. Limit: 3 / min. Please try again in 20s. Contact us through our help center at help.openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method.
```

Please check if you have reached the official API call rate limit. Refer to the [OpenAI official documentation](https://platform.openai.com/docs/guides/rate-limits) for details.

### 9. After user self-deployment, Zhichat is not available, and the error is as follows: "Unrecognized request argument supplied: functions." How to resolve this?

First, check if the front-end and back-end versions are the latest and consistent. Second, this error may occur because you are using an Azure OpenAI key but have not successfully deployed the model. Check if the model is deployed in your Azure OpenAI. The gpt-3.5-turbo model version must be 0613 or above (as versions before 0613 do not support the function call capability used by Zhichat, making it unusable).

### 10. When setting the OpenAI key, the error is as follows. What is the reason?

```JSON
Error communicating with OpenAI: HTTPSConnectionPool(host='api.openai.com', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by NewConnectionError(<urllib3.connection.HTTPSConnection object at 0x7f0462ed7af0>; Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
```

Usually, this is due to your environment setting a proxy. Please check if a proxy is set.

### 11. When switching models in the application, I encountered the following error. How to resolve this?

```JSON
Anthropic: Error code: 400 - 'error': 'type': "invalid request error, 'message': 'temperature: range: -1 or 0..1)
```

Each model has different parameter values. Set the parameter values according to the current model's range.

### 12. I encountered the following error. How to resolve this?

```JSON
Query or prefix prompt is too long, you can reduce the prefix prompt, or shrink the max token, or switch to a llm with a larger token limit size
```

In the parameter settings on the orchestration page, reduce the value of "max token."

### 13. What is the default model in Dify, and can open-source models be used?

The default model can be configured in **Settings - Model Providers**. Currently, it supports text generation models from providers like OpenAI / Azure OpenAI / Anthropic, and also supports integration of open-source models hosted on Hugging Face / Replicate / xinference.

### 14. In the community edition, why does the dataset's **Q&A Segmentation Mode** keep showing "queued"?

Check if the API key for the Embedding model you are using has reached the rate limit.

### 15. When users encounter the error "Invalid token" while using the application, how to resolve it?

If you encounter the error "Invalid token," try the following solutions:

* Clear the browser cache (Cookies, Session Storage, and Local Storage). If using a mobile app, clear the corresponding app's cache and re-access it.
* Generate a new App URL and re-enter the URL.

### 16. What are the size limits for uploading dataset documents?

Currently, the maximum size for a single document upload is 15MB, with a total document limit of 100. If you need to adjust these limits for a locally deployed version, refer to [documentation](https://docs.dify.ai/v/zh-hans/getting-started/faq/install-faq#11.-ben-di-bu-shu-ban-ru-he-jie-jue-shu-ju-ji-wen-dang-shang-chuan-de-da-xiao-xian-zhi-he-shu-liang).

### 17. Why does choosing the Claude model still consume OpenAI's quota?

Because Claude does not support the Embedding model, the Embedding process and other dialogue generation by default use OpenAI's key, thus consuming OpenAI's quota. You can also set other default inference models and Embedding models in **Settings - Model Providers**.

### 18. How can I control the use of more contextual data rather than the model's own generation capabilities?

Whether to use the dataset depends on the dataset's description. Make the dataset description as clear as possible. For specific writing techniques, refer to [this documentation](https://docs.dify.ai/v/zh-hans/advanced/datasets).

### 19. When uploading dataset documents in Excel, how to better segment them?

Set the header in the first row, and display content in each subsequent row without additional header settings or complex table formats.

For example, in the table below, only retain the second row's header. The first row (Table 1) is an extra header and should be removed.

### 20. Why can't I use GPT-4 in Dify even though I bought ChatGPT Plus?

OpenAI's GPT-4 model API and ChatGPT Plus are two separate products with separate charges. The model API has its own pricing. Refer to [OpenAI pricing documentation](https://openai.com/pricing). To apply for paid access, you must first bind a card. Binding a card grants GPT-3.5 access but not GPT-4 access. GPT-4 access requires a paid bill. Refer to [OpenAI official documentation](https://platform.openai.com/account/billing/overview) for details.

### 21. How to add other Embedding Models?

Dify supports the following for use as Embedding models. Simply select the `Embeddings` type in the configuration box.

* Azure
* LocalAI
* MiniMax
* OpenAI
* Replicate
* XInference
* GPUStack

### 22. How to set an application I created as an application template?

This feature provides application templates for cloud version users to reference, and currently does not support setting your created applications as templates. If you use the cloud version, you can **Add to Workspace** or **Customize** it to become your own application. If you use the community version and need to create more application templates for your team, you can contact our commercialization team for paid technical support: `business@dify.ai`.
