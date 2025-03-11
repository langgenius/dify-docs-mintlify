# Maintain Documents

## Manage Documentations in the Knowledge Base

### Adding Documentations

A knowledge base is a collection of documents. Documents can be uploaded by developers or operators, or synchronized from other data sources. Each document in the knowledge base corresponds to a file in its data source—for example, a Notion document or an online webpage.

To upload a new document to an existing knowledge base, go to **Knowledge Base** > **Documents** and click **Add File**.

![Uploading the new documentation on Knowledge Base](https://assets-docs.dify.ai/2024/12/424ab491aaebe09b490a36d26c9fa8da.png)

### Disable / Archive / Delete document

**Enable**: Documents that are currently in normal status can be edited and retrieved in the knowledge base. If a document has been disabled, you can re-enable it. For archived documents, you must first unarchive them before re-enabling.

**Disable**: If you don’t want a document to be indexed during use, toggle off the blue switch on the right side of the document to disable it. A disabled document can still be edited or modified.

**Archive**: For older documents that are no longer in use but you don’t want to delete, you can archive them. Archived documents can only be viewed or deleted and cannot be edited. You can archive a document from the Knowledge Base’s **Document List** by clicking the **Archive** button, or within the document’s details page. Archiving can be undone.

**Delete**: ⚠️ Dangerous Option. For incorrect documents or clearly ambiguous content, select Delete from the menu on the right side of the document. Deleted content cannot be restored, so proceed with caution.

> The above options all support batch operations after multiple documents are selected.

![Batch file Operations](https://assets-docs.dify.ai/2024/12/5e0e64859a1ac51602d167ec55ef9350.png)

**Note:**

If there are some documents in your knowledge base that haven’t been updated or retrieved for a while, the system will disable inactive documents to ensure optimal performance.

* For Sandbox users, the "inactive document disable period" is **after 7 days**.
* For Professional and Team users, it is **after 30 days**. You can revert these documents and continue using them at any time by clicking the "Enable" button in the knowledge base.

You can revert these disable documents and continue using them at any time by clicking the "Enable" button in the knowledge base. Paid users are provided with **one-click revert** function.

![O<strong>ne-click revert</strong>](https://assets-docs.dify.ai/2024/12/bf6485b17aec716741eb65e307c2274c.png)

***

## Managing Text Chunks

### Viewing Text Chunks

In the knowledge base, each uploaded document is stored as text chunks. By clicking on the document title, you can view the list of chunks and their specific text content on the details page. Each page displays 10 chunks by default, but you can change the number of chunks shown per page at the bottom of the web.

Only the first two lines of each content chunk are visible in the preview. If you need to see the full text within a chunk, click the “Expand Chunk” button for a complete view.

![Expand text chunks](https://assets-docs.dify.ai/2024/12/86cc80f17fab1eea75aa73ee681e4663.png)

You can quickly view all enabled or disabled documents using the filter.

![Filter text chunks](https://assets-docs.dify.ai/2025/01/47ef07319175a102bfd1692dcc6cac9b.png)

Different [chunking modes](../create-knowledge-and-upload-documents/2.-choose-a-chunk-mode.md) correspond to different text chunking preview methods:

{% tabs %}
{% tab title="General Mode" %}
**General Mode**

Chunks of text in [General mode](../create-knowledge-and-upload-documents.md#general) are independent blocks. If you want to view the complete content of a chunk, click the **full-screen** icon.

![Full screen viewing](https://assets-docs.dify.ai/2024/12/c37a1a247092cda9433a10243543698f.png)

Tap the document title at the top to quickly switch to other documents in the knowledge base.

![General mode - text chunking](https://assets-docs.dify.ai/2024/12/4422286c6d254e13c1ab59b147f0ffbf.png)
{% endtab %}

{% tab title="Parent-child Mode" %}
**Parent-child Mode**

In[ Parent-child](maintain-knowledge-documents.md#parent-child-chunking-mode) mode, content is divided into parent chunks and child chunks.

*   **Parent chunks**

    After selecting a document in the knowledge base, you’ll first see the parent chunk content. Parent chunks can be split by **Paragraph** or **Full Doc**, offering a more comprehensive context. The illustration below shows how the text preview differs between these split modes.

![Difference in preview between paragraph and full doc](https://assets-docs.dify.ai/2024/12/b3961da2536dc922496ef6646315b9f4.png)

*   **Child chunks**

    Child chunks are usually sentences (smaller text blocks) within a paragraph, containing more detailed information. Each chunk displays its character count and the number of times it has been retrieved. Tapping **“Child Chunks”** reveals more details. If you want to see the full content of a chunk, click the full-screen icon in the top-right corner of that chunk to enter full-screen reading mode.

![Parent-child mode - text chunking](https://assets-docs.dify.ai/2024/12/c0776f91e155bb1c961ae255bb98f39e.png)
{% endtab %}

{% tab title="Q&A Mode (Community Edition Only)" %}
**Q\&A Mode**

In Q\&A Mode, a content chunk consists of a question and an answer. Click on any document title to view the text chunks.

![<strong>Q&#x26;A Mode - check content chunk</strong>](https://assets-docs.dify.ai/2024/12/98e2486f6c5e06b4ece1b81d078afa08.png)
{% endtab %}
{% endtabs %}

***

### Checking Chunk Quality

Document chunking significantly influences the Q\&A performance of knowledge-base applications. It’s recommended to perform a manual review of chunking quality before integrating the knowledge base with your application.

Although automated chunk methods based on character length, identifiers, or NLP semantic system can significantly reduce the workload of large-scale text chunk, the quality of chunk is related to the text structure of different document formats and the semantic context. Manual checking and correction can effectively compensate for the shortcomings of machine chunk in semantic recognition.

When checking chunk quality, pay attention to the following situations:

* **Overly short text chunks**, leading to semantic loss;

![Overly short text chunks](https://assets-docs.dify.ai/2024/12/ee081e98c1649aea4a5c2b15b88e11aa.png)

* **Overly long text chunks**, leading to semantic noise affecting matching accuracy;

![Overly long text chunks](https://assets-docs.dify.ai/2024/12/ac47381ae4be183768dd025c37c049fa.png)

* **Obvious semantic truncation**, which occurs when using maximum segment length limits, leading to forced semantic truncation and missing content during recall;

![Obvious semantic truncation](https://assets-docs.dify.ai/2024/12/b8ab7ac84028b0b16c3948f35015e069.png)

***

### Adding Text Chunks

You can add text chunks individually to the knowledge base, and different chunking modes correspond to different ways of adding those chunks.

> Adding text chunks is a paid feature. Please upgrade your account [here](https://dify.ai/pricing) to access this functionality.

{% tabs %}
{% tab title="General Mode" %}
**General Mode**

Click **Add Chunks** in the chunks list page to add one or multiple custom chunks to the document.

![General mode - Add chunks](https://assets-docs.dify.ai/2024/12/552ff4ab9e77130ad09aaef878b19cc9.png)

When manually adding text chunks, you can choose to add both the main content and keywords. After entering the content, select the **“Add another”** checkbox at the bottom to continue adding more text chunks seamlessly.

![General mode - Add another text chunk](https://assets-docs.dify.ai/2024/12/cd769622bc1d85c037277ef6fa5247c9.png)

To add chunks in bulk, you need to download the upload template in CSV format first and edit all the chunk contents in Excel according to the template format, then save the CSV file and upload it.

![General mode - Add customize chunks in bulk](https://assets-docs.dify.ai/2024/12/5e501dd8efba02ff31d2e739417ce864.png)
{% endtab %}

{% tab title="Parent-child Mode" %}
**Parent Child Chunks Mode**

Click Add Chunks in the Chunk list to add one or multiple custom **parent chunks** to the document.

![Parent-child mode - Add chunks](https://assets-docs.dify.ai/2024/12/ed4be3bf178e3a41d53bcc10255ad3b2.png)

After entering the content, select the **“Add another”** checkbox at the bottom to keep adding more text chunks.

![Parent-child mode - Add chunks 2](https://assets-docs.dify.ai/2024/12/ba64232eea364b68f2e38341eb9cf5c1.png)

You can add child chunks individually under a parent chunk. Click “Add” on the right side of the child chunk within the parent chunk to add it.

![Parent-child mode - Add child chunks](https://assets-docs.dify.ai/2024/12/23f68a369eb9c1a2cc9022b99a08341d.png)
{% endtab %}

{% tab title="Q&A Mode (Community Edition Only)" %}
**Q\&A Mode**

Click the “Add Chunk” button at the top of the chunk list to manually add a single or multiple question-answer pairs chunk to the document.
{% endtab %}
{% endtabs %}

***

### Editing Text Chunks

{% tabs %}
{% tab title="General Mode" %}
**General Mode**

You can directly edit or modify the added chunks content, including modifying the **text content or keywords within the chunks.**

To prevent duplicate edits, an “Edited” tag will appear on the content chunk after it has been modified.

![Edit text chunks](https://assets-docs.dify.ai/2024/12/92e7788dad008d38f7c8f532fbcb3636.png)
{% endtab %}

{% tab title="Parent-child Mode" %}
**Parent-child Mode**

A parent chunk contains the content of its child chunks, but they remain independent. You can edit the parent chunk or child chunks separately. Below is a diagram explaining the process of modifying parent and child chunks:

![Diagram of editing parent-child chunks](https://assets-docs.dify.ai/2024/12/aacdb2e95b9b7c0265455caaf0f1f55f.png)

**To edit a parent chunk:**

1\. Click the Edit button on the right side of the parent chunk.

2\. Enter your changes and then click **Save**—this won’t affect the content of the child chunks.

3\. If you want to regenerate the child chunks after editing, click Save and Re-generate Child Chunks.

To prevent duplicate edits, an “Edited” tag will appear on the content chunk after it has been modified.

![Parent-chid chunks mode - Modify parent chunks](https://assets-docs.dify.ai/2024/12/06354a75368f96b3f8f2afaad4f50b0c.png)

**Modify child chunks**: select any child chunks and enter edit mode and save it after modification. The modification will not affect the contents of the parent chunks. Child chunks that have been edited or newly added will be marked with a deep blue label, `C-NUMBER-EDITED`.

You can also treat child chunks as tags for the current parent text block.

![Parent-child mode - modify child chunks](https://assets-docs.dify.ai/2024/12/a59563614d8f4661ebfb20f6b646b4ea.png)
{% endtab %}

{% tab title="Q&A Mode (Community Edition Only)" %}
**Q\&A Mode**

In Q\&A chunking mode, each content chunk consists of a question and an answer. Click on the text chunk you wish to edit to modify the question and answer individually. Additionally, you can edit the keywords for the current chunk.

![<strong>Q&#x26;A Mode - modify text chunks</strong>](https://assets-docs.dify.ai/2024/12/5c69adc0d4ec470d0677e67a4dd894a1.png)
{% endtab %}
{% endtabs %}

### Modify Text Chunks for Uploaded Documents

Knowledge Base supports reconfiguring document segmentation.

**Larger Chunks**

* Retain more context within each chunk, ideal for tasks requiring a broader understanding of the text.
* Reduce the total number of chunks, lowering processing time and storage overhead.

**Smaller Chunks**

* Provide finer granularity, improving accuracy for tasks like extraction or summarization.
* Reduce the risk of exceeding model token limits, making it safer for models with stricter constraints.

Go to **Chunk Settings**, adjust the settings, and click **Save & Process** to save changes and reprocess the document. The chunk list will update automatically once processing is complete—no page refresh needed.

![Chunk Settings](https://assets-docs.dify.ai/2025/01/36cb20be8aae1f368ebf501c0d579051.png)

![Save & Process](https://assets-docs.dify.ai/2025/01/a47b890c575a7693c40303d3d7cb4952.png)

***

### Metadata Management

In addition to capturing metadata (e.g., title, URL, keywords, or a web page description) from various source documents, metadata is also used as structured fields during the chunk retrieval process for filtering or displaying citation sources.

![Metadata management](https://assets-docs.dify.ai/2024/12/f3b1ff4b559ebc40f18b8980b3719fe8.png)

***
