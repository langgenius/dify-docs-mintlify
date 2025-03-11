---
description: Last edited by Allen, Dify Technical Writer
---

# Variables

**Workflow** and **Chatflow** Application are composed of independent nodes. Most nodes have input and output items, but the input and output information for each node is not consistent and dynamic.

**How to use a fixed symbol to refer dynamically changing content?** Variables, as dynamic data containers, can store and transmit unfixed content, being referenced mutually within different nodes, providing flexible information mobility between nodes.

### System Variables

System variables refer to pre-set system-level parameters within Chatflow / Workflow App that can be globally read by other nodes. All system-level variables begin with `sys.`

#### Workflow

Workflow type application provides the system variables below:

<table><thead><tr><th>Variables name</th><th>Data Type</th><th width="267">Description</th><th>Remark</th></tr></thead><tbody><tr><td><p><code>sys.files</code></p><p><code>[LEGACY]</code></p></td><td>Array[File]</td><td>File Parameter: Stores images uploaded by users</td><td>The image upload function needs to be enabled in the 'Features' section in the upper right corner of the application orchestration page</td></tr><tr><td><code>sys.user_id</code></td><td>String</td><td>User ID: A unique identifier automatically assigned by the system to each user when they use a workflow application. It is used to distinguish different users</td><td></td></tr><tr><td><code>sys.app_id</code></td><td>String</td><td>App ID: A unique identifier automatically assigned by the system to each App. This parameter is used to record the basic information of the current application. </td><td>This parameter is used to differentiate and locate distinct Workflow applications for users with development capabilities</td></tr><tr><td><code>sys.workflow_id</code></td><td>String</td><td>Workflow ID: This parameter records information about all nodes information in the current Workflow application.</td><td>This parameter can be used by users with development capabilities to track and record information about the nodes contained within a Workflow</td></tr><tr><td><code>sys.workflow_run_id</code></td><td>String</td><td>Workflow Run ID: Used to record the runtime status and execution logs of a Workflow application.</td><td>This parameter can be used by users with development capabilities to track the application's historical execution records</td></tr></tbody></table>

![Workflow App System Variables](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/09d9f977965d41cf056f37a4f8f952db.png)

#### Chatflow

Chatflow type application provides the following system variables:

<table><thead><tr><th>Variables name</th><th>Data Type</th><th width="283">Description</th><th>Remark</th></tr></thead><tbody><tr><td><code>sys.query</code></td><td>String</td><td>Content entered by the user in the chatting box.</td><td></td></tr><tr><td><code>sys.files</code></td><td>Array[File]</td><td>File Parameter: Stores images uploaded by users</td><td>The image upload function needs to be enabled in the 'Features' section in the upper right corner of the application orchestration page</td></tr><tr><td><code>sys.dialogue_count</code></td><td>Number</td><td><p>The number of conversations turns during the user's interaction with a Chatflow application. The count automatically increases by one after each chat round and can be combined with if-else nodes to create rich branching logic.<br></p><p>For example, LLM will review the conversation history at the X conversation turn and automatically provide an analysis.</p></td><td></td></tr><tr><td><code>sys.conversation_id</code></td><td>String</td><td>A unique ID for the chatting box interaction session, grouping all related messages into the same conversation, ensuring that the LLM continues the chatting on the same topic and context.</td><td></td></tr><tr><td><code>sys.user_id</code></td><td>String</td><td>A unique ID is assigned for each application user to distinguish different conversation users.</td><td></td></tr><tr><td><code>sys.workflow_id</code></td><td>String</td><td>Workflow ID: This parameter records information about all nodes information in the current Workflow application.</td><td>This parameter can be used by users with development capabilities to track and record information about the nodes contained within a Workflow</td></tr><tr><td><code>sys.workflow_run_id</code></td><td>String</td><td>Workflow Run ID: Used to record the runtime status and execution logs of a Workflow application.</td><td>This parameter can be used by users with development capabilities to track the application's historical execution records</td></tr></tbody></table>

![Chatflow App System Variables](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/79340d58bf2c202dd6bd4e93fa03272d.png)

### Environment Variables

**Environment variables are used to protect sensitive information involved in workflows**, such as API keys and database passwords used when running workflows. They are stored in the workflow rather than in the code, allowing them to be shared across different environments.

![Environment Variables](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/475c2b9a04b8c9ab16b7d3dba21755f3.png)

Supports the following 3 data types:

* String
* Number
* Secret

Environmental variables have the following characteristics:

* Environment variables can be globally referenced within most nodes;
* Environment variable names cannot be duplicated;
* Output variables of nodes are generally read-only and cannot be written to.

***

### Conversation Variables

> Conversation variables are only applicable to [Chatflow](variables.md#chatflow-and-workflow) App.

**Conversation variables allow application developers to specify particular information that needs to be temporarily stored within the same Chatflow session, ensuring that this information can be referenced across multiple rounds of chatting within the current chatflow**. This can include context, files uploaded to the chatting box(coming soon), user preferences input during the conversation, etc. It's like providing a "memo" for the LLM that can be checked at any time, avoiding information bias caused by LLM memory errors.

For example, you can store the language preference input by the user in the first round of chatting in a conversation variable. The LLM will refer to the information in the conversation variable when answering and use the specified language to reply to the user in subsequent chats.

![Conversation Variable](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/c04285fec92f13a20ccbd3e21361a30d.png)

**Conversation variables** support the following six data types:

* String
* Number
* Object
* Array\[string]
* Array\[number]
* Array\[object]

**Conversation variables** have the following features:

* Conversation variables can be referenced globally within most nodes in the same Chatflow App;
* Writing to conversation variables requires using the [Variable Assigner](https://docs.dify.ai/guides/workflow/node/variable-assignment) node;
* Conversation variables are read-write variables;

About how to use conversation variables with the Variable Assigner node, please refer to the [Variable Assigner](node/variable-assignment.md).

To track changes in conversation variable values during debugging the application, click the conversation variable icon at the top of the Chatflow application preview page.

![](https://assets-docs.dify.ai/2024/11/cc8067fa4c96436f037f8210ebe3f65c.png)

### Notice

* To avoid variable name duplication, node naming must not be repeated
* The output variables of nodes are generally fixed variables and cannot be edited
