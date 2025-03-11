# Additional Features

Both Workflow and Chatflow applications support enabling additional features to enhance the user interaction experience. For example, adding a file upload entry, giving the LLM application a self-introduction, or using a welcome message can provide users with a richer interactive experience.

Click the **"Features"** button in the upper right corner of the application to add more functionality.

{% embed url="https://www.motionshot.app/walkthrough/6773d34ad27e58127b913945/embed?fullscreen=1&hideAsSteps=1&hideCopy=1&hideDownload=1&hideSteps=1" %}

#### Workflow

> Note: This method of adding file uploads to Workflow applications is deprecated. We recommend adding custom file variables on the start node instead.

Workflow type applications only support the **"Image Upload"** feature. When enabled, an image upload entry will appear on the usage page of the Workflow application.

{% embed url="https://www.motionshot.app/walkthrough/6773d3d86a0c3ed534f24da9/embed?fullscreen=1&hideAsSteps=1&hideCopy=1&hideDownload=1&hideSteps=1" %}



**Usage:**

**For application users:** Applications with image upload enabled will display an upload button on the usage page. Click the button or paste a file link to complete the image upload. You will receive the LLM's response to the image.

**For application developers:** After enabling the image upload feature, the uploaded image files will be stored in the `sys.files` variable. Next, add an LLM node, select a large model with vision capabilities, and enable the VISION feature within it. Choose the `sys.files` variable to allow the LLM to read the image file.

Finally, select the output variable of the LLM node in the END node to complete the setup.

#### Chatflow

Chatflow type applications support the following features:

*   **Conversation Opener**

    Allow AI to proactively send a message, which can be a welcome message or AI self-introduction, to bring it closer to the user.
*   **Follow-up**

    Automatically add suggestions for the next question after the conversation is complete, to increase the depth and frequency of dialogue topics.
*   **Text-to-Speech**

    Add an audio playback button in the Q\&A text box, using a TTS service (needs to be set up in Model Providers) to read out the text.
*   **File Upload**

    Supports the following file types: documents, images, audio, video, and other file types. After enabling this feature, application users can upload and update files at any time during the application dialogue. A maximum of 10 files can be uploaded simultaneously, with a size limit of 15MB per file.
*   **Citation and Attribution**

    Commonly used in conjunction with the "Knowledge Retrieval" node to display the reference source documents and attribution parts of the LLM's responses.
*   **Content Moderation**

    Supports using moderation APIs to maintain a sensitive word library, ensuring that the LLM can respond and output safe content. For detailed instructions, please refer to Sensitive Content Moderation.

**Usage:**

Except for the **File Upload** feature, the usage of other features in Chatflow applications is relatively simple. Once enabled, they can be intuitively used on the application interaction page.

This section will mainly introduce the specific usage of the **File Upload** feature:

**For application users:** Chatflow applications with file upload enabled will display a "paperclip" icon on the right side of the dialogue box. Click it to upload files and interact with the LLM.

![Upload file](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/b18af11da3f339c496193d9732906849.png)

**For application developers:**

After enabling the file upload feature, the files users send will be uploaded in the `sys.files` variable. It will be updated after the user sends a new message in the same conversation turn.

Different types of files correspond to different application orchestration methods based on the uploaded file differences.

* **Document Files**

LLMs do not have the ability to directly read document files, so a Document Extractor node is needed to preprocess the files in the `sys.files` variable. The orchestration steps are as follows:

1. Enable the Features function and only check "Documents" in the file types.
2. Select the `sys.files` variable in the input variables of the Document Extractor node.
3. Add an LLM node and select the output variable of the document extractor node in the system prompt.
4. Add a "Direct Reply" node at the end, filling in the output variable of the LLM node.

Chatflow applications built using this method cannot remember the content of uploaded files. Application users need to upload document files in the chat box for each conversation. If you want the application to remember uploaded files, please refer to File Upload: Adding Variables in the Start Node.

* **Image Files**

Some LLMs support directly obtaining information from images, so no additional nodes are needed to process images.

The orchestration steps are as follows:

1. Enable the Features function and only check "Images" in the file types.
2. Add an LLM node, enable the VISION feature, and select the `sys.files` variable.
3. Add a "Answer" node at the end, filling in the output variable of the LLM node.

![Enable vision](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/3a3582bd9bc8ea94bbdbfeefe6a78571.png)

* **Mixed File Types**

If you want the application to have the ability to process both document files and image files simultaneously, you need to use the List Operation node to preprocess the files in the `sys.files` variable, extract more refined variables, and send them to the corresponding processing nodes. The orchestration steps are as follows:

1. Enable the Features function and check both "Images" and "Document Files" types.
2. Add two list operation nodes, extracting image and document variables in the "Filter" condition.
3. Extract document file variables and pass them to the "Document Extractor" node; extract image file variables and pass them to the "LLM" node.
4. Add a "Direct Reply" node at the end, filling in the output variable of the LLM node.

After the application user uploads both document files and images, document files are automatically diverted to the document extractor node, and image files are automatically diverted to the LLM node to achieve joint processing of files.

![<strong>Mixed File Types</strong>](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/66471e8e67b2ede0c94bfa1cffeab834.png)

* **Audio and Video Files**

LLMs do not yet support direct reading of audio and video files, and the Dify platform has not yet built-in related file processing tools. Application developers can refer to [External Data Tools](../extension/api-based-extension/external-data-tool.md) to integrate tools for processing file information themselves.
