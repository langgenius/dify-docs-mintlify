# Annotation Reply

The annotated replies feature provides customizable high-quality question-and-answer responses through manual editing and annotation.

Applicable scenarios:

* **Customized Responses for Specific Fields:** In customer service or knowledge base scenarios for enterprises, government, etc., service providers may want to ensure that certain specific questions are answered with definitive results. Therefore, it is necessary to customize the output for specific questions. For example, creating "standard answers" for certain questions or marking some questions as "unanswerable."
* **Rapid Tuning for POC or DEMO Products:** When quickly building prototype products, customized responses achieved through annotated replies can efficiently enhance the expected generation of Q\&A results, thereby improving customer satisfaction.

The annotated replies feature essentially provides another set of retrieval-enhanced systems, allowing you to bypass the LLM generation phase and avoid the hallucination issues of RAG.

### Workflow

1. After enabling the annotated replies feature, you can annotate the responses from LLM conversations. You can add high-quality answers from LLM responses directly as annotations or edit a high-quality answer according to your needs. These edited annotations will be saved persistently.
2. When a user asks a similar question again, the system will vectorize the question and search for similar annotated questions.
3. If a match is found, the corresponding answer from the annotation will be returned directly, bypassing the LLM or RAG process.
4. If no match is found, the question will continue through the regular process (passing to LLM or RAG).
5. Once the annotated replies feature is disabled, the system will no longer match responses from annotations.

![Annotated Replies Workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/7bebcf85d52f65d5649956f47ed33d43.png)

### Enabling Annotated Replies in Prompt Orchestration

Enable the annotated replies switch by navigating to **“Orchestrate -> Add Features”**:

![Enabling Annotated Replies in Prompt Orchestration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/b467da1fbaa9beb22cfb2a987f51f653.png)

When enabling, you need to set the parameters for annotated replies, which include: Score Threshold and Embedding Model.

**Score Threshold:** This sets the similarity threshold for matching annotated replies. Only annotations with scores above this threshold will be recalled.

**Embedding Model:** This is used to vectorize the annotated text. Changing the model will regenerate the embeddings.

Click save and enable, and the settings will take effect immediately. The system will generate embeddings for all saved annotations using the embedding model.

![Setting Parameters for Annotated Replies](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/a2c7b82a4f25a96fcdf68c807fb96812.png)

### Adding Annotations in the Conversation Debug Page

You can directly add or edit annotations on the model response information in the debug and preview pages.

![Adding Annotated Replies](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/e064e3dcca3f04e16f5269b169820d2d.png)

Edit the response to the high-quality reply you need and save it.

![Editing Annotated Replies](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/b79aabe6e9b336e26ca409a49526501e.png)

Re-enter the same user question, and the system will use the saved annotation to reply to the user's question directly.

![Replying to User Questions with Saved Annotations](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/810f640d184227f4918ee197ff906203.png)

### Enabling Annotated Replies in Logs and Annotations

Enable the annotated replies switch by navigating to “Logs & Ann. -> Annotations”:

![Enabling Annotated Replies in Logs and Annotations](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/c74951765f078392924da901008eb815.png)

### Setting Parameters for Annotated Replies in the Annotation Backend

The parameters that can be set for annotated replies include: Score Threshold and Embedding Model.

**Score Threshold:** This sets the similarity threshold for matching annotated replies. Only annotations with scores above this threshold will be recalled.

**Embedding Model:** This is used to vectorize the annotated text. Changing the model will regenerate the embeddings.

![Setting Parameters for Annotated Replies](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/5bbd94402452e3f4ecc29eb398591585.png)

### Bulk Import of Annotated Q\&A Pairs

In the bulk import feature, you can download the annotation import template, edit the annotated Q\&A pairs according to the template format, and then import them in bulk.

![Bulk Import of Annotated Q&A Pairs](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/ad6497dbe8c93fe9988cf76775434a7c.png)

### Bulk Export of Annotated Q\&A Pairs

Through the bulk export feature, you can export all saved annotated Q\&A pairs in the system at once.

![Bulk Export of Annotated Q&A Pairs](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/4d80d0a9b8056711a2dcdf664c19e840.png)

### Viewing Annotation Hit History

In the annotation hit history feature, you can view the edit history of all hits on the annotation, the user's hit questions, the response answers, the source of the hits, the matching similarity scores, the hit time, and other information. You can use this information to continuously improve your annotated content.

![Viewing Annotation Hit History](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/annotation/26b6c37dcff225201ea5b4fb712b2d4d.png)
