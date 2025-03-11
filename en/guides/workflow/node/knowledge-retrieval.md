# Knowledge Retrieval

The Knowledge Base Retrieval Node is designed to query text content related to user questions from the Dify Knowledge Base, which can then be used as context for subsequent answers by the Large Language Model (LLM).

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d90961c6d794d425a8e11df177315188.png)

Configuring the Knowledge Base Retrieval Node involves three main steps:

1. **Selecting the Query Variable**
2. **Choosing the Knowledge Base for Query**
3. **Configuring the Retrieval Strategy**

**Selecting the Query Variable**

In knowledge base retrieval scenarios, the query variable typically represents the user's input question. In the "Start" node of conversational applications, the system pre-sets "sys.query" as the user input variable. This variable can be used to query the knowledge base for text chunks most closely related to the user's question. The maximum query content sent to the knowledge base is 200 characters.

**Choosing the Knowledge Base for Query**

Within the knowledge base retrieval node, you can add an existing knowledge base from Dify. For instructions on creating a knowledge base within Dify, please refer to the knowledge base [help documentation](https://docs.dify.ai/guides/knowledge-base/create-knowledge-and-upload-documents).

**Configuring the Retrieval Strategy**

It's possible to modify the indexing strategy and retrieval mode for an individual knowledge base within the node. For a detailed explanation of these settings, refer to the knowledge base [help documentation](https://docs.dify.ai/guides/knowledge-base/retrieval-test-and-citation).

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/2e2c3316619ed31514a665226ce6ed08.png)

Dify offers two recall strategies for different knowledge base retrieval scenarios: "N-to-1 Recall" and "Multi-way Recall". In the N-to-1 mode, knowledge base queries are executed through function calling, requiring the selection of a system reasoning model. In the multi-way recall mode, a Rerank model needs to be configured for result re-ranking. For a detailed explanation of these two recall strategies, refer to the retrieval mode explanation in the [help documentation](https://docs.dify.ai/guides/knowledge-base/create-knowledge-and-upload-documents#id-5-indexing-methods).

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/4a3007cda9dfa50ddac3711693725dce.png)
