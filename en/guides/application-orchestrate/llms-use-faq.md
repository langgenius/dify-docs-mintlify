# FAQ

### 1. How to choose a basic model?

**gpt-3.5-turbo** •gpt-3.5-turbo is an upgraded version of the gpt-3 model series. It is more powerful than gpt-3 and can handle more complex tasks. It has significant improvements in understanding long text and cross-document reasoning. Gpt-3.5 turbo can generate more coherent and persuasive text. It also has great improvements in summarization, translation and creative writing. **Good at: Long text understanding, cross-document reasoning, summary, translation, creative writing**

**gpt-4** •gpt-4 is the latest and most powerful Transformer language model. It has nearly 200 billion pre-trained parameters, making it state-of-the-art on all language tasks, especially those requiring deep understanding and generation of long, complex responses. Gpt-4 can handle all aspects of human language, including understanding abstract concepts and cross-page reasoning. Gpt-4 is the first true general language understanding system that can handle any natural language processing task in the field of artificial intelligence. **Good at: \*All NLP tasks, language understanding, long text generation, cross-document reasoning, understanding abstract concepts\***Please refer to: [https://platform.openai.com/docs/models/overview](https://platform.openai.com/docs/models/overview)

### 2. Why is it recommended to set max\_tokens smaller?

Because in natural language processing, longer text outputs usually require longer computation time and more computing resources. Therefore, limiting the length of the output text can reduce the computational cost and time to some extent. For example, set: max\_tokens=500, which means that only the first 500 tokens of the output text are considered, and the part exceeding this length will be discarded. The purpose of doing so is to ensure that the length of the output text does not exceed the acceptable range of the LLM, while making full use of computing resources to improve the efficiency of the model. On the other hand, more often limiting max\_tokens can increase the length of the prompt, such as the limit of gpt-3.5-turbo is 4097 tokens, if you set max\_tokens=4000, then only 97 tokens are left for the prompt, and an error will be reported if exceeded.

### 3. How to split long text data in the knowledge reasonably?

In some natural language processing applications, text is often split into paragraphs or sentences for better processing and understanding of semantic and structural information in the text. The minimum splitting unit depends on the specific task and technical implementation. For example:

• For text classification tasks, text is usually split into sentences or paragraphs.

• For machine translation tasks, entire sentences or paragraphs need to be used as splitting units.

Finally, experiments and evaluations are still needed to determine the most suitable embedding technology and splitting unit. The performance of different technologies and splitting units can be compared on the test set to select the optimal scheme.

### 4. What distance function did we use when getting knowledge segmentation?

We use [cosine similarity](https://en.wikipedia.org/wiki/Cosine\_similarity). The choice of distance function is usually irrelevant. OpenAI embeddings are normalized to length 1, which means:

•Using the dot product to calculate cosine similarity can be slightly faster

•Cosine similarity and Euclidean distance will lead to the same ranking

After the embedding vectors are normalized to length 1, calculating the cosine similarity between two vectors can be simplified to their dot product. Because the normalized vectors have a length of 1, the result of the dot product is equal to the result of the cosine similarity.

Since the dot product calculation is faster than other similarity metrics (such as Euclidean distance), using normalized vectors for dot product calculation can slightly improve computational efficiency.

### 5. **When filling in the OpenAI key, the error "Validation failed: You exceeded your current quota, please check your plan and billing details" occurs. What is causing this error?**

This error indicates that the OpenAI key account balance has been used up. Please top up the OpenAI account at openai.com. Refer to [OpenAI ](https://openai.com/pricing)for details on their plans and billing.

### 6. When using OpenAI's key for dialogue in the application, there is an error prompt as follows. **What is the cause?**

Error 1：

```JSON
The server encountered an internal error and was unable to complete your request。Either the server is overloaded or there is an error in the application
```

Error 1：

```JSON
Rate limit reached for default-gpt-3.5-turboin organization org-wDrZCxxxxxxxxxissoZb on requestsper min。 Limit: 3 / min. Please try again in 20s. Contact us through our help center   at help.openai.com   if you continue to haveissues. Please add a payment method toyour account to increase your rate limit.Visit https://platform.openai.com/account/billingto add a payment method.
```

Please check if the official interface call rate limit has been reached. Please refer to the [official documentation](https://platform.openai.com/docs/guides/rate-limits) for details.

### 6. After local deployment, Explore-Chat returns an error "Unrecognized request argument supplied: functions". How can this be resolved?

First, please check that the frontend and backend versions are up-to-date and consistent with each other. This error can also occur if an Azure OpenAI key is being used without successfully deploying the model. Verify that the Azure OpenAI resource has a deployed model - the gpt-3.5-turbo model version must be 0613 or later, as earlier versions do not support the function calling capabilities required by Explore-Chat.

### 7. When switching models in the app, the following error is encountered:

```JSON
Anthropic: Error code: 400 - f'error': f'type': "invalid request error, 'message': 'temperature: range: -1 or 0..1)
```

This error occurs because each model has different valid ranges for its parameters. Make sure to configure the parameter value according to the allowed range for the current model.

### 8. How to solve the following error prompt?

```JSON
Query or prefix prompt is too long, you can reduce the preix prompt, or shrink the max token, or switch to a llm with a larger token limit size
```

You can lower the value of "Max token" in the parameter settings of the Prompt Eng.

### 9. What are the default models in Dify, and can open-source LLMs be used?

A: The default models can be configured under **Settings - Model Provider.** Currently supported text generation LLMs include OpenAI, Azure OpenAl, Anthropic, etc. At the same time, open-source LLMs hosted on Hugging Face, Replicate, xinference, etc. can also be integrated.

### 10. The knowledge in Community Edition gets stuck in "Queued" when Q\&A segmentation mode is enabled.

Please check if the rate limit has been reached for the Embedding model API key used.

### 11. The error "Invalid token" appears when using the app.

There are two potential solutions if the error "Invalid token" appears:

* Clear the browser cache (cookies, session storage, and local storage) or the app cache on mobile. Then, revisit the app.
* Regenerate the app URL and access the app again with the new URL. This should resolve the "Invalid token" error.

### 12. What are the size limits for uploading knowledge documents?

The maximum size for a single document upload is currently 15MB. There is also a limit of 100 total documents. These limits can be adjusted if you are using a local deployment. Refer to the [documentation](../../getting-started/install-self-hosted/install-faq.md#11.-how-to-solve-the-size-and-quantity-limitations-for-uploading-dataset-documents-in-the-local-depl) for details on changing the limits.

### 13. Why does Claude still consume OpenAI credits when using the Claude model?

The Claude model does not have its own embedding model. Therefore, the embedding process and other dialog generation like next question suggestions default to using OpenAI keys. This means OpenAI credits are still consumed. You can set different default inference and embedding models under **Settings > Model Provider.**

### 14. Is there any way to control the greater use of knowledge data rather than the model's own generation capabilities?

Whether to use a knowledge base is related to the description of the knowledge. Please write the knowledge description clearly as much as possible. Please refer to the [documentation](https://docs.dify.ai/advanced/datasets) for details.

### 15. How to better segment the uploaded knowledge document in Excel?

Set the header in the first row, and display the content in each subsequent row. Do not have any additional header settings or complex formatted table content.

### 16. I have already purchased ChatGPT plus, why can't I still use GPT4 in Dify?

ChatGPT Plus and OpenAI's GPT-4 model API are two separate products with separate pricing. The model APIs have their own pricing structure, see [OpenAI's pricing documentation](https://openai.com/pricing) for details. To get access to the GPT-4 model API, you need to pay for a billing cycle - simply having a payment method on file and access to GPT-3.5 via ChatGPT Plus is not sufficient. Please refer to [OpenAI's official documentation](https://platform.openai.com/account/billing/overview) for complete details on gaining access to GPT-4.

### 17. How to add other embedding models?

Dify supports using the listed providers as an Embedding model provider, simply select the `Embedding` type in the configuration box.

* Azure
* LocalAI
* MiniMax
* OpenAI
* Replicate
* XInference

### 18. How can I set my own created app as an app template?

The ability to set your own created app as a template is currently not supported. The existing templates are provided by Dify officially for cloud version users' reference. If you are using the cloud version, you can add apps to your workspace or customize them to make your own after modifications. If you are using the community version and need to create more app templates for your team, you may consult our business team to obtain paid technical support: [business@dify.ai](mailto:business@dify.ai)


### 19. 502 Bad Gateway

This is caused by Nginx forwarding the service to the wrong location. First, make sure the container is running, then run the following command with root privileges:
```
docker ps -q | xargs -n 1 docker inspect --format '{{ .Name }}: {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
```
Find these two lines in the output:
```
/docker-web-1: 172.19.0.5
/docker-api-1: 172.19.0.7
```
Remember the IP addresses at the end. Then, open the location where you stored the dify source code, open dify/docker/nginx/conf.d, replace http://api:5001 with http://172.19.0.7:5001, and replace http://web:3000 with http://172.19.0.5:3000. Afterward, restart the Nginx container or reload the configuration.  
These IP addresses are ***exemplary***, you must execute the command to obtain your own IP address, do not fill it in directly.  
You may need to reconfigure based on the IP when restarting related containers.
