# Knowledge

Dify’s Knowledge feature visualizes each stage of the RAG pipeline, providing a friendly UI for application builders to easily manage personal or team knowledge. It also allows for seamless integration into AI applications.

Developers can upload internal company documents, FAQs, and standard working guides, then process them into structured data that large language models (LLMs) can query.

Compared with the static pre-trained datasets built into AI models, the content in a knowledge base can be updated in real time, ensuring LLMs always have access to the latest information and helping avoid problems caused by outdated or missing data.

When an LLM receives a user query, it first uses keywords to search within the knowledge base. Based on those keywords, the knowledge base returns content chunks with high relevance rankings, giving the LLM crucial context to generate more precise answers.

This approach ensures LLMs don’t rely solely on pre-trained knowledge. Instead, they can also draw from real-time documents and databases, enhancing both the accuracy and relevance of responses.

**Key Advantages**

**• Real-Time Updates**: The knowledge base can be updated anytime, ensuring the model always has the latest information.

• **Precision**: By retrieving relevant documents, the LLM can ground its answers in actual information, minimizing hallucinations.

• **Flexibility**: Developers can customize the knowledge base content to match specific needs, defining the scope of knowledge as required.

***

You only need to prepare text content, such as:

* Long text content (TXT, Markdown, DOCX, HTML, JSONL, or even PDF files)
* Structured data (CSV, Excel, etc.)
* Online data source(Web pages, Notion, etc.)

By simply uploading files to the **Knowledge Base**, data processing is handled automatically.

> If your team already has an independent knowledge base, you can use the [“Connect to an External Knowledge Base”](connect-external-knowledge.md) feature to establish its connection with Dify.

![Create a knowledge base](https://assets-docs.dify.ai/2024/12/effc826d2584d5f2983cdcd746099bb6.png)

### **Use Case**

If you want to create an AI customer support assistant based on your existing knowledge base and product documentation, you can simply upload those files to the Knowledge Base in Dify and then set up a conversational application.

Traditionally, going from raw text training to a fully developed AI customer support chatbot could take weeks, plus it’s challenging to maintain and iterate effectively.

In Dify, the entire process takes just three minutes, after which you can immediately begin gathering user feedback.

### Knowledge Base and Documents

In Dify, a Knowledge Base is a collection of Documents, each of which can include multiple Chunks of content. You can integrate an entire knowledge base into an application to serve as a retrieval context, drawing from uploaded files or data synchronized from other sources.

If your team already has an independent, external knowledge that is separate from the Dify platform, you can link it using the [External Knowledge Base](external-knowledge-api-documentation.md) feature. This way, you don’t need to re-upload all your content to Dify. Your AI app can directly access and process information in real time from your team’s existing knowledge.
