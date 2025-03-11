# Start

#### Definition

The **“Start”** node is a critical preset node in the Chatflow / Workflow application. It provides essential initial information, such as user input and [uploaded files](../file-upload.md), to support the normal flow of the application and subsequent workflow nodes.

#### Configuring the Node

On the Start node's settings page, you'll find two sections: **"Input Fields"** and preset **System Variables**.

![Chatflow and Workflow](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/c4a9bb46f636807f0b59710724fddc40.png)

#### Input Field

Input field is configured by application developers to prompt users for additional information.

For example, in a weekly report application, users might be required to provide background information such as name, work date range, and work details in a specific format. This preliminary information helps the LLM generate higher quality responses.

Six types of input variables are supported, all of which can be set as required:

* **Text:** Short text, filled in by the user, with a maximum length of 256 characters.
* **Paragraph:** Long text, allowing users to input longer content.
* **Select:** Fixed options set by the developer; users can only select from preset options and cannot input custom content.
* **Number:** Only allows numerical input.
* **Single File:** Allows users to upload a single file. Supports document types, images, audio, video, and other file types. Users can upload locally or paste a file URL. For detailed usage, refer to File Upload.
* **File List:** Allows users to batch upload files. Supports document types, images, audio, video, and other file types. Users can upload locally or paste file URLs. For detailed usage, refer to File Upload.

{% hint style="info" %}
Dify's built-in document extractor node can only process certain document formats. For processing images, audio, or video files, refer to External Data Tools to set up corresponding file processing nodes.
{% endhint %}

Once configured, users will be guided to provide necessary information to the LLM before using the application. More information will help to improve the LLM's question-answering efficiency.

#### System Variables

System variables are preset system-level parameters in Chatflow / Workflow applications that can be globally accessed by other nodes in the application. They are typically used in advanced development scenarios, such as building multi-turn dialogue applications, collecting application logs and monitoring data, or recording usage behavior across different applications and users.

**Workflow**

Workflow application provides the following system variables:

<table><thead><tr><th width="193">Variable Name</th><th width="116">Data Type</th><th width="278">Description</th><th>Notes</th></tr></thead><tbody><tr><td><code>sys.files</code><br>[LEGACY]</td><td>Array[File]</td><td>File parameter, stores images uploaded by users when initially using the application</td><td>Image upload feature needs to be enabled in the "Features" section at the top right of the application orchestration page</td></tr><tr><td><code>sys.user_id</code></td><td>String</td><td>User ID, a unique identifier automatically assigned to each user when using the workflow application, used to distinguish different conversation users</td><td></td></tr><tr><td><code>sys.app_id</code></td><td>String</td><td>Application ID, a unique identifier assigned to each Workflow application by the system, used to distinguish different applications and record basic information of the current application</td><td>For users with development capabilities, this parameter can be used to differentiate and locate different Workflow applications</td></tr><tr><td><code>sys.workflow_id</code></td><td>String</td><td>Workflow ID, used to record all node information contained in the current Workflow application</td><td>For users with development capabilities, this parameter can be used to track and record node information within the Workflow</td></tr><tr><td><code>sys.workflow_run_id</code></td><td>String</td><td>Workflow application run ID, used to record the running status of the Workflow application</td><td>For users with development capabilities, this parameter can be used to track the application's run history</td></tr></tbody></table>

**Chatflow**

Chatflow application provides the following system variables:

<table><thead><tr><th>Variable Name</th><th width="127">Data Type</th><th width="283">Description</th><th>Notes</th></tr></thead><tbody><tr><td><code>sys.query</code></td><td>String</td><td>The initial content input by the user in the dialogue box</td><td></td></tr><tr><td><code>sys.files</code></td><td>Array[File]</td><td>Images uploaded by the user in the dialogue box</td><td>Image upload feature needs to be enabled in the "Features" section at the top right of the application orchestration page</td></tr><tr><td><code>sys.dialogue_count</code></td><td>Number</td><td>The number of dialogue turns during user interaction with the Chatflow application. Automatically increments by 1 after each turn. Can be used with if-else nodes to create rich branching logic. For example, at the Xth turn of dialogue, review the conversation history and provide analysis</td><td></td></tr><tr><td><code>sys.conversation_id</code></td><td>String</td><td>Unique identifier for the dialogue interaction session, grouping all related messages into the same conversation, ensuring the LLM continues the dialogue on the same topic and context</td><td></td></tr><tr><td><code>sys.user_id</code></td><td>String</td><td>Unique identifier assigned to each application user, used to distinguish different conversation users</td><td></td></tr><tr><td><code>sys.app_id</code></td><td>String</td><td>Application ID, a unique identifier assigned to each Workflow application by the system, used to distinguish different applications and record basic information of the current application</td><td>For users with development capabilities, this parameter can be used to differentiate and locate different Workflow applications</td></tr><tr><td><code>sys.workflow_id</code></td><td>String</td><td>Workflow ID, used to record all node information contained in the current Workflow application</td><td>For users with development capabilities, this parameter can be used to track and record node information within the Workflow</td></tr><tr><td><code>sys.workflow_run_id</code></td><td>String</td><td>Workflow application run ID, used to record the running status of the Workflow application</td><td>For users with development capabilities, this parameter can be used to track the application's run history</td></tr></tbody></table>
