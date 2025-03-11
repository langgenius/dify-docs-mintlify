# File Upload

Compared to chat text, document files can contain vast amounts of information, such as academic reports and legal contracts. However, Large Language Models (LLMs) are inherently limited to processing only text or images, making it challenging to extract the rich contextual information within these files. As a result, application users often resort to manually copying and pasting large amounts of information to converse with LLMs, significantly increasing unnecessary operational overhead.

The file upload feature addresses this limitation by allowing files to be uploaded, parsed, referenced, and downloaded as File variables within workflow applications. **This empowers developers to easily construct complex workflows capable of understanding and processing various media types, including images, audio, and video.**

## Application Scenarios

1. **Document Analysis**: Upload academic research reports for LLMs to quickly summarize key points and answer related questions based on the file content.
2. **Code Review**: Developers can upload code files to receive optimization suggestions and bug detection.
3. **Learning Assistance**: Students can upload assignments or study materials for personalized explanations and guidance.
4. **Legal Aid**: Upload complete contract texts for LLMs to assist in reviewing clauses and identifying potential risks.

## Difference Between File Upload and Knowledge Base

Both file upload and knowledge base provide additional contextual information for LLMs, but they differ significantly in usage scenarios and functionality:

1. **Information Source**:
   * File Upload: Allows end-users to dynamically upload files during conversations, providing immediate, personalized contextual information.
   * Knowledge Base: Pre-set and managed by application developers, containing a relatively fixed set of information.
2. **Usage Flexibility**:
   * File Upload: More flexible, users can upload different types of files based on specific needs.
   * Knowledge Base: Content is relatively fixed but can be reused across multiple sessions.
3. **Information Processing**:
   * File Upload: Requires document extractors or other tools to convert file content into text that LLMs can understand.
   * Knowledge Base: Usually pre-processed and indexed, ready for direct retrieval.
4. **Application Scenarios**:
   * File Upload: Suitable for scenarios that need to process user-specific documents, such as document analysis, personalized learning assistance, etc.
   * Knowledge Base: Suitable for scenarios that require access to a large amount of preset information, such as customer service, product inquiries, etc.
5. **Data Persistence**:
   * File Upload: Typically for temporary use, not stored long-term in the system.
   * Knowledge Base: Exists as a long-term part of the application, can be continuously updated and maintained.

## Quick Start: Building a Chatflow / Workflow Application with File Upload Feature

Dify supports file uploads in both [ChatFlow](key-concepts.md) and [WorkFlow](key-concepts.md#chatflow-and-workflow) type applications, processing them through variables for LLMs. Application developers can refer to the following methods to enable file upload functionality:

* In Workflow applications:
  * Add file variables in the ["Start Node"](node/start.md)
* In ChatFlow applications:
  * Enable file upload in ["Additional Features"](additional-features.md) to allow direct file uploads in the chat window
  * Add file variables in the "[Start Node"](node/start.md)
  * Note: These two methods can be configured simultaneously and are independent of each other. The file upload settings in additional features (including upload method and quantity limit) do not affect the file variables in the start node. For example, if you only want to create file variables through the start node, you don't need to enable the file upload feature in additional features.

These two methods provide flexible file upload options for applications to meet the needs of different scenarios.

**File Types**

`File` variables and `array[file]` variables support the following file types and formats:

<table data-header-hidden><thead><tr><th width="227"></th><th></th></tr></thead><tbody><tr><td>File Type</td><td>Supported Formats</td></tr><tr><td>Documents</td><td>TXT, MARKDOWN, PDF, HTML, XLSX, XLS, DOCX, CSV, EML, MSG, PPTX, PPT, XML, EPUB.</td></tr><tr><td>Images</td><td>JPG, JPEG, PNG, GIF, WEBP, SVG.</td></tr><tr><td>Audio</td><td>MP3, M4A, WAV, WEBM, AMR.</td></tr><tr><td>Video</td><td>MP4, MOV, MPEG, MPGA.</td></tr><tr><td>Others</td><td>Custom file extension support</td></tr></tbody></table>

#### Method 1: Using an LLM with File Processing Capabilities

Some LLMs, such as [Claude 3.5 Sonnet](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support), now support direct processing and analysis of file content, enabling the use of file variables in the LLM node's prompts.

> To prevent potential issues, application developers should verify the supported file types on the LLM's official website before utilizing the file variable.

1. Click to create a Chatflow or Workflow application.
2. Add an LLM node and select an LLM with file processing capabilities.
3. Add a file variable in the start node.
4. Enter the file variable in the system prompt of the LLM node.
5. Complete the setup.

![](https://assets-docs.dify.ai/2024/11/a7154e8966d979dcba13eac0a172ef89.png)

**Method 2: Enable File Upload in Application Chat Box (Chatflow Only)**

1. Click the **"Features"** button in the upper right corner of the Chatflow application to add more functionality to the application. After enabling this feature, application users can upload and update files at any time during the application dialogue. A maximum of 10 files can be uploaded simultaneously, with a size limit of 15MB per file.

![file upload](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/20784cfa167417654a69c10e42e8271b.png)

Enabling this feature does not grant LLMs the ability to directly read files. A **Document Extractor** is still needed to parse documents into text for LLM comprehension.

* For audio files, models like `gpt-4o-audio-preview` that support multimodal input can process audio directly without additional extractors.
* For video and other file types, there are currently no corresponding extractors. Application developers need to [integrate external tools](../extension/api-based-extension/external-data-tool.md) for processing.

2. Add a Document Extractor node, and select the `sys.files` variable in the input variables.
3. Add an LLM node and select the output variable of the Document Extractor node in the system prompt.
4. Add an "Answer" node at the end, filling in the output variable of the LLM node.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/6802747ef5de4772ce8d05f6c0a23130.png)

Once enabled, users can upload files and engage in conversations in the dialogue box. However, with this method, the LLM application does not have the ability to remember file contents, and files need to be uploaded for each conversation.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/b18af11da3f339c496193d9732906849.png)

If you want the LLM to remember file contents during conversations, please refer to Method 3.

**Method 3: Enable File Upload by Adding File Variables**

**1. Add File Variables in the "Start" Node**

Add input fields in the application's "Start" node, choosing either **"Single File"** or **"File List"** as the field type for the variable.

{% embed url="https://www.motionshot.app/walkthrough/6773d0e0d27e58127b913943/embed?fullscreen=1&hideAsSteps=1&hideCopy=1&hideDownload=1&hideSteps=1" %}



*   **Single File**

    Allows the application user to upload only one file.
*   **File List**

    Allows the application user to batch upload multiple files at once.

> For ease of operation, we will use a single file variable as an example.

**File Parsing**

There are two main ways to use file variables:

1. Using tool nodes to convert file content:
   * For document-type files, you can use the "Document Extractor" node to convert file content into text form.
   * This method is suitable for cases where file content needs to be parsed into a format that the model can understand (such as string, array\[string], etc.).
2. Using file variables directly in LLM nodes:
   * For certain types of files (such as images), you can use file variables directly in LLM nodes.
   * For example, for file variables of image type, you can enable the vision feature in the LLM node and then directly reference the corresponding file variable in the variable selector.

The choice between these methods depends on the file type and your specific requirements. Next, we will detail the specific steps for both methods.

**2. Add Document Extractor Node**

After uploading, files are stored in single file variables, which LLMs cannot directly read. Therefore, a **"Document Extractor"** node needs to be added first to extract content from uploaded document files and send it to the LLM node for information processing.

Use the file variable from the "Start" node as the input variable for the **"Document Extractor"** node.

![<strong>Document Extractor</strong>](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/8e6a3deaaa5eebeb66f9e1d844dc1ec6.png)

Fill in the output variable of the "Document Extractor" node in the system prompt of the LLM node.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/f6ea094b30b240c999a4248d1fc21a1c.png)

After completing these settings, application users can paste file URLs or upload local files in the WebApp, then interact with the LLM about the document content. Users can replace files at any time during the conversation, and the LLM will obtain the latest file content.

**Referencing File Variables in LLM Nodes**

For certain file types (such as images), file variables can be directly used within LLM nodes. This method is particularly suitable for scenarios requiring visual analysis. Here are the specific steps:

1. In the LLM node, enable the vision functionality. This allows the model to process image inputs (the model must support vision capabilities).
2. In the variable selector of the LLM node, directly reference the previously created file variable. If file upload was enabled through additional features, select the `sys.files` variable.
3. In the system prompt, guide the model on how to process the image input. For example, you can instruct the model to describe the image content or answer questions about the image.

Below is an example configuration:

![Using file variables directly in LLM node](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/f8980732757050049a430eea934511cf.png)

It's important to note that when directly using file variables in LLM node, the developers need to ensure that the file variable contains only image files; otherwise, errors may occur. If users might upload different types of files, we need to use list operator node for filtering files.

**File Download**

Placing file variables in answer nodes or end nodes will provide a file download card in the conversation box when the application reaches that node. Clicking the card allows for file download.

![file download](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/bc39be7fd4879b3875e6b77daaff5d37.png)

## Advanced Usage

If you want the application to support uploading multiple types of files, such as allowing users to upload document files, images, and audio/video files simultaneously, you need to add a "File List" variable in the "Start Node" and use the "List Operation" node to process different file types. For detailed instructions, please refer to the List Operation node.
