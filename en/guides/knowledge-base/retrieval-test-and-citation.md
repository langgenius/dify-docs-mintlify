# Retrieval Test / Citation and Attributions

### 1. Retrieval Testing

Dify’s knowledge base provides a text retrieval testing feature, allowing you to simulate user queries and retrieve knowledge base content blocks. The retrieval chunks are sorted by score and then sent to the LLM. Generally, the higher the match between the question and the content chunks, the more closely the LLM’s answer will align with the source document, leading to better “training results.”

You can test with different **retrieval methods and parameter configurations** to evaluate the quality and effectiveness of the retrieved text chunks. Different **chunking modes** use different retrieved testing methods.

{% tabs %}
{% tab title="General" %}
**General**

Enter common user questions into the **Source Text field** and click **Test** to see the **Retrieved Chunks** results on the right.

In **General Mode**, each text chunk stands independently. The score shown in the top-right corner of a chunk represents how closely it matches the query keywords. A higher score indicates a stronger alignment between the chunk and the keywords.

![General mode - retrieval text chunks](https://assets-docs.dify.ai/2024/12/806967bb36e74fc744b34887cd3ebe52.png)

Tap a content chunk to see the details of the referenced content. Each chunk shows its source document information at the bottom, letting you verify whether the text  chunk is appropriate.

![Review the details of text chunks](https://assets-docs.dify.ai/2024/12/419ac78ad21ea198b08f89c4f5fde485.png)
{% endtab %}

{% tab title="Parent-child" %}
**Parent-child**

Enter typical user questions into the **Source Text** field and click **Test** to view the **Retrieved Chunks** on the right. In parent-child chunking mode, keywords are matched against child chunks for more precise results, and the score in the upper-right corner indicates how closely a child chunk matches the keyword.

You can click a child chunk to preview its exact content. After the match, the entire parent chunk is recalled to provide more comprehensive information.

![Retrieval test - Parent-child mode](https://assets-docs.dify.ai/2024/12/6f0b99f97b138805bf4665d0c5c16f26.png)

Each chunk displays its source document at the bottom—usually a specific paragraph or sentence. Tap the “Open” button on the right side of the source to view the entire referenced content chunk. Since multiple child chunks can be relevant, this allows you to assess whether the current chunk is appropriate.

![Check the details of retrieval chunks](https://assets-docs.dify.ai/2024/12/22103227f8a25069d147160254f69512.png)
{% endtab %}
{% endtabs %}

In **Records**, you can check the past query records. If the knowledge base is linked to an application, any queries triggered within the application will also appear here.

#### Modify Text Retrieval Setting

Click the icon in the upper-right corner of the Source Text field to change the current knowledge base’s retrieval method and related parameters. These changes only take effect during the current retrieval test session for debugging, you can compare the retrieval performance of different retrieval settings.

If you want to permanently modify the retrieval method for the knowledge base, go to **“Knowledge Base Settings”** > **“Retrieval Settings”** to make changes.

![Retrieval settings](https://assets-docs.dify.ai/2024/12/86b78cb114a843c9dedcba1fe12e3b02.png)

**Suggested Steps for Retrieval Testing:**

1. Design and organize test cases/test question sets covering common user questions.
2. Choose an appropriate retrieval strategy: vector search/full-text search/hybrid search. For the pros and cons of different retrieval methods, please refer to the extended reading [Retrieval-Augmented Generation (RAG)](../../learn-more/extended-reading/retrieval-augment/).
3. Debug the number of retrieval segments (TopK) and the recall score threshold (Score). Choose appropriate parameter combinations based on the application scenario, including the quality of the documents themselves.

**How to Configure TopK Value and Retrieval Threshold (Score)**

* **TopK represents the maximum number of retrieval chunks when sorted in descending order of similarity scores.** A smaller TopK value will recall fewer segments, which may result in incomplete recall of relevant texts; a larger TopK value will recall more segments, which may result in recalling segments with lower semantic relevance, reducing the quality of LLM responses.
* **The retrieval threshold (Score) represents the minimum similarity score allowed for recall segments.** A smaller recall score will retrieval more segments, which may result in recalling less relevant segments; a larger recall score threshold will recall fewer segments, and if too large, may result in missing relevant segments.

***

### 2. Citation and Attribution

When testing the knowledge base effect within the application, you can go to **Workspace -- Add Feature -- Citation and Attribution** to enable the citation attribution feature.

![Enable citation and attribution feature](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/knowledge-base/c50a37d96be8b631c02483144c226cd7.png)

After enabling the feature, when the large language model responds to a question by citing content from the knowledge base, you can view specific citation paragraph information below the response content, including **original segment text, segment number, matching degree**, etc. Clicking **Link to Knowledge** above the cited segment allows quick access to the segment list in the knowledge base, facilitating developers in debugging and editing.

![View citation information in response content](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/knowledge-base/8eed0be0aa90697a4bfbc0ea84a2dcdb.png)

#### View Linked Applications in the Knowledge Base

On the left side of the knowledge base, you can see all linked Apps. Hover over the circular icon to view the list of all linked apps. Click the jump button on the right to quickly browser them.

![Viewing the linked Apps](https://assets-docs.dify.ai/2024/12/28899b9b0eba8996f364fb74e5b94c7f.png)

