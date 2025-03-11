# Building a Smart Customer Service Bot Using a Knowledge Base

> Author: Steven Lynn, Dify Technical Writer

In the last experiment, we learned the basic usage of file uploads. However, when the text we need to read exceeds the LLM's context window, we need to use a knowledge base.

> **What is context?**
>
> The context window refers to the range of text that the LLM can "see" and "remember" when processing text. It determines how much previous text information the model can refer to when generating responses or continuing text. The larger the window, the more contextual information the model can utilize, and the generated content is usually more accurate and coherent.

Previously, we learned about the concept of LLM hallucinations. In many cases, an LLM knowledge base allows the Agent to locate accurate information, thus accurately answering questions. It has applications in specific fields such as customer service and search tools.

Traditional customer service bots are often based on keyword retrieval. When users input questions outside of the keywords, the bot cannot solve the problem. The knowledge base is designed to solve this problem, enabling semantic-level retrieval and reducing the burden on human agents.

Before starting the experiment, remember that the core of the knowledge base is retrieval, not the LLM. The LLM enhances the output process, but the real need is still to generate answers.

### What You Will Learn in This Experiment

* Basic usage of Chatflow
* Usage of knowledge bases and external knowledge bases
* The concept of embeddings

### Prerequisites

#### Create an Application

In Dify, select **Create from Blank - Chatflow.**

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/0147e0d6fa1412dcf38ff0b12d30e5fe.png)

#### Add a Model Provider

This experiment involves using embedding models. Currently, supported embedding model providers include OpenAI and Cohere. In Dify's model providers, those with the `TEXT EMBEDDING` label are supported. Ensure you have added at least one and have sufficient balance.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/ebfb40e8b80adb8d7e1096ee5da16fad.png)

> **What is embedding?**
>
> "Embedding" is a technique that converts discrete variables (such as words, sentences, or entire documents) into continuous vector representations.
>
> Simply put, when we process natural language into data, we convert text into vectors. This process is called embedding. Vectors of semantically similar texts will be close together, while vectors of semantically opposite texts will be far apart. LLMs use this data for training, predicting subsequent vectors, and thus generating text.

### Create a Knowledge Base

Log in to Dify -> Knowledge -> Create Knowledge

{% @arcade/embed flowId="AWhXMYEPd4mYWnupP88B" url="https://app.arcade.software/share/AWhXMYEPd4mYWnupP88B" %}



Dify supports three data sources: documents, Notion, and web pages.

For local text files, note the file type and size limitations; syncing Notion content requires binding a Notion account; syncing a website requires using the **Jina** or **Firecrawl API**.

We will start with a uploading local document as an example.

#### Chunk Settings

After uploading the document, you will enter the following page:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/0dab2d0a607d9486ae973d897b0c08bd.png)

You can see a segmentation preview on the right. The default selection is automatic segmentation and cleaning. Dify will automatically divide the article into many paragraphs based on the content. You can also set other segmentation rules in the custom settings.

#### Index Method

Normally we prefer to select **High Quality**, but this will consume extra tokens. Selecting **Economic** will not consume any tokens.

The community edition of Dify uses a Q\&A segmentation mode. Selecting the corresponding language can organize the text content into a Q\&A format, which requires additional token consumption.

#### Embedding Model

Please refer to the model provider's documentation and pricing information before use.

Different embedding models are suitable for different scenarios. For example, Cohere's `embed-english` is suitable for English documents, and `embed-multilingual` is suitable for multilingual documents.

#### Retrieval Settings

Dify provides three retrieval functions: vector retrieval, full-text retrieval, and hybrid retrieval. Hybrid retrieval is the most commonly used.

In hybrid retrieval, you can set weights or use a reranking model. When setting weights, you can set whether the retrieval should focus more on semantics or keywords. For example, in the image below, semantics account for 70% of the weight, and keywords account for 30%.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/6a1f2b4a6e1b63febdaee3e01c1d39a4.png)

Clicking **Save and Process** will process the document. After processing, the document can be used in the application.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/fdc20eb804ec39a308726324f6b33f45.png)

#### Syncing from a Website

In many cases, we need to build a smart customer service bot based on help documentation. Taking Dify as an example, we can convert the [Dify help documentation](https://docs.dify.ai) into a knowledge base.

Currently, Dify supports processing up to 50 pages. Please pay attention to the quantity limit. If exceeded, you can create a new knowledge base.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/8936a4f7952c7aefe5f9d58ee730883c.png)

#### Adjusting Knowledge Base Content

After the knowledge base has processed all documents, it is best to check the coherence of the segmentation in the knowledge base. Incoherence will affect the retrieval effect and needs to be manually adjusted.

Click on the document content to browse the segmented content. If there is irrelevant content, you can disable or delete it.

{% @arcade/embed flowId="4JUDJQf4ijK85yanuxaI" url="https://app.arcade.software/share/4JUDJQf4ijK85yanuxaI" %}



If content is segmented into another paragraph, it also needs to be adjusted back.

#### Recall Test

In the document page of the knowledge base, click Recall Test in the left sidebar to input keywords to test the accuracy of the retrieval results.

### Add Nodes

Enter the created APP, and let's start building the smart customer service bot.

#### Question Classification Node

You need to use a question classification node to separate different user needs. In some cases, users may even chat about irrelevant topics, so you need to set a classification for this as well.

To make the classification more accurate, you need to choose a better LLM, and the classification needs to be specific enough with sufficient distinction.

Here is a reference classification:

* User asks irrelevant questions
* User asks Dify-related questions
* User requests explanation of technical terms
* User asks about joining the community

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/627566df2b28b58ab84e53d3737c6927.png)

#### Direct Reply Node

In the question classification, "User asks irrelevant questions" and "User asks about joining the community" do not need LLM processing to reply. Therefore, you can directly connect a direct reply node after these two questions.

"User asks irrelevant questions":

You can guide the user to the help documentation, allowing them to try to solve the problem themselves, for example:

```
I'm sorry, I can't answer your question. If you need more help, please check the [help documentation](https://docs.dify.ai).
```

Dify supports Markdown formatted text output. You can use Markdown to enrich the text format in the output. You can even insert images in the text using Markdown.

#### Knowledge Retrieval Node

Add a knowledge retrieval node after "User asks Dify-related questions" and check the knowledge base to be used.

{% @arcade/embed flowId="lFy1LfZ4cFyu1GlmJk8c" url="https://app.arcade.software/share/lFy1LfZ4cFyu1GlmJk8c" %}



#### LLM Node

In the next node after the knowledge retrieval node, you need to select an LLM node to organize the content retrieved from the knowledge base.

The LLM needs to adjust the reply based on the user's question to make the reply more appropriate.

Context: You need to use the output of the knowledge retrieval node as the context of the LLM node.

System prompt: Based on \{{context\}}, answer \{{user question\}}

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/0052ebf236d55dc0c143c5dbfe5f1e76.png)

You can use `/` or `{` to reference variables in the prompt writing area. In variables, variables starting with `sys.` are system variables. Please refer to the help documentation for details.

In addition, you can enable LLM memory to make the user's conversation experience more coherent.

### Question 1: How to Connect External Knowledge Bases

In the knowledge base function, you can connect external knowledge bases through external knowledge base APIs, such as the AWS Bedrock knowledge base.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/7bcfb95e806966a868885814f0d7dc35.png)

For best practices on AWS Bedrock knowledge bases, please read: [how-to-connect-aws-bedrock.md](../../learn-more/use-cases/how-to-connect-aws-bedrock.md "mention")

### Question 2: How to Manage Knowledge Bases Through APIs

In both the community edition and SaaS version of Dify, you can add, delete, and query the status of knowledge bases through the knowledge base API.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/cda4458ccb9be9e1c3ec9821fb5c5f99.png)

In the instance with the knowledge base deployed, go to **Knowledge Base -> API** and create an API key. Please keep the API key safe.

### Question 3: How to Embed the Customer Service Bot into a Webpage

After application deployment, select embed webpage, choose a suitable embedding method, and paste the code into the appropriate location on the webpage.

{% @arcade/embed flowId="5Bc0DqWslBfE99uWQH77" url="https://app.arcade.software/share/5Bc0DqWslBfE99uWQH77" %}

