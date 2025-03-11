# Retrieval-Augmented Generation (RAG)

### Explanation of RAG Concept

The RAG architecture, with vector retrieval at its core, has become the mainstream technical framework for enabling large models to access the latest external knowledge while addressing the problem of hallucinations in generated content. This technology has been implemented in a variety of application scenarios.

Developers can use this technology to build AI-powered customer service, enterprise knowledge bases, AI search engines, and more at a low cost. By using natural language input to interact with various forms of knowledge organization, they can create intelligent systems. Let's take a representative RAG application as an example:

In the diagram below, when a user asks, "Who is the President of the United States?", the system does not directly pass the question to the large model for an answer. Instead, it first performs a vector search in a knowledge base (such as Wikipedia shown in the diagram) to find relevant content through semantic similarity matching (e.g., "Joe Biden is the 46th and current president of the United States..."). Then, the system provides the user's question along with the retrieved relevant knowledge to the large model, allowing it to obtain sufficient information to answer the question reliably.

![Basic RAG Architecture](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/extended-reading/retrieval-augment/19b393464a4d0374498144502f024516.png)

**Why is this necessary?**

We can think of a large model as a super expert who is familiar with various fields of human knowledge. However, it has its limitations. For instance, it does not know personal information about you because such information is private and not publicly available on the internet, so it has no prior learning opportunity.

When you want to hire this super expert as your personal financial advisor, you need to allow them to review your investment records, household expenses, and other data before answering your questions. This way, the expert can provide professional advice based on your personal circumstances.

**This is exactly what the RAG system does: it helps the large model temporarily acquire external knowledge it does not possess, allowing it to find answers before responding to questions.**

From the example above, it is easy to see that the most critical part of the RAG system is the retrieval of external knowledge. Whether the expert can provide professional financial advice depends on whether they can accurately find the necessary information. If they find your weight loss plan instead of your investment records, even the most knowledgeable expert would be powerless.
