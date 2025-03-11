# Re-ranking

### Why is Re-ranking Needed?

Hybrid search can leverage the strengths of different retrieval technologies to achieve better recall results. However, the query results from different retrieval modes need to be merged and normalized (converting data to a uniform standard range or distribution for better comparison, analysis, and processing) before being provided to the large model together. This is where a scoring system comes in: the Re-rank Model.

**The re-rank model calculates the semantic match between the list of candidate documents and the user query, reordering them based on semantic match to improve the results of semantic sorting.** The principle is to compute a relevance score between the user query and each candidate document and return a list of documents sorted by relevance from high to low. Common re-rank models include Cohere rerank, bge-reranker, etc.

![Hybrid Search + Re-ranking](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/extended-reading/retrieval-augment/292a7f8e50b9b6be6ababd6b84ac322f.png)

In most cases, there is a preliminary retrieval before re-ranking because calculating the relevance score between a query and millions of documents would be highly inefficient. Therefore, **re-ranking is typically placed at the final stage of the search process and is ideal for merging and sorting results from different retrieval systems.**

However, re-ranking is not only applicable for merging results from different retrieval systems. Even in a single retrieval mode, introducing a re-ranking step can effectively improve document recall. For example, semantic re-ranking can be added after keyword retrieval.

In practical applications, besides normalizing multiple query results, we generally limit the number of segments passed to the large model (i.e., TopK, which can be set in the re-rank model parameters) before handing over the relevant text segments to the large model. This is because the input window of the large model has size limitations (typically 4K, 8K, 16K, 128K tokens). You need to choose an appropriate segmentation strategy and TopK value based on the input window size of the selected model.

It is important to note that even if the model's context window is large enough, recalling too many segments may introduce less relevant content, reducing the quality of the response. Therefore, the TopK parameter for re-ranking is not necessarily the larger, the better.

Re-ranking is not a replacement for search technology but an auxiliary tool to enhance existing retrieval systems. **Its greatest advantage is that it provides a simple and low-complexity method to improve search results, allowing users to incorporate semantic relevance into existing search systems without significant infrastructure modifications.**

For example, with Cohere Rerank, you only need to register an account and apply for an API. Integration requires just two lines of code. Additionally, they offer multilingual models, meaning you can sort query results in different languages simultaneously.

### How to Configure the Re-rank Model?

Dify currently supports the Cohere Rerank model. You can enter the "Model Providers -> Cohere" page and fill in the API key for the Re-rank model:

![Configure Cohere Rerank Model in Model Providers](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/extended-reading/retrieval-augment/cf0cd2766490583758d06cafbfb01a40.png)

### How to Obtain the Cohere Rerank Model?

Visit: [https://cohere.com/rerank](https://cohere.com/rerank), register on the page, and apply for the Rerank model usage qualification to obtain the API key.

### Setting the Re-rank Model in Dataset Retrieval Mode

Enter the "Dataset -> Create Dataset -> Retrieval Settings" page to add the Re-rank settings. Besides setting the Re-rank model when creating a dataset, you can also change the Re-rank configuration in the settings of an existing dataset and in the dataset recall mode settings in application orchestration.

![Setting the Re-rank Model in Dataset Retrieval Mode](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/extended-reading/retrieval-augment/ad3bc13e53749ce69de5db196443676f.png)

**TopK:** Used to set the number of relevant documents returned after re-ranking.

**Score Threshold:** Used to set the minimum score for relevant documents returned after re-ranking. When the Re-rank model is set, the TopK and Score Threshold settings only take effect in the re-rank step.

### Setting the Re-rank Model in Multi-Path Recall Mode for Datasets

Enter the "Prompt Arrangement -> Context -> Settings" page to enable the Re-rank model when setting to multi-path recall mode.

Explanation about multi-path recall mode: 🔗Please check the section [Multi-path Retrieval](https://docs.dify.ai/guides/knowledge-base/integrate-knowledge-within-application#multi-path-retrieval-recommended)

![Setting the Re-rank Model in Multi-Path Recall Mode for Datasets](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/extended-reading/retrieval-augment/f9cde54ca59bfdc5ad94afb00551d5d0.png)
