# Integrate Langfuse

### What is Langfuse

Langfuse is an open-source LLM engineering platform that helps teams collaborate on debugging, analyzing, and iterating their applications.

{% hint style="info" %}
Introduction to Langfuse: [https://langfuse.com/](https://langfuse.com/)
{% endhint %}

***

### How to Configure Langfuse

1. Register and log in to Langfuse on the [official website](https://langfuse.com/)
2. Create a project in Langfuse. After logging in, click **New** on the homepage to create your own project. The **project** will be used to associate with **applications** in Dify for data monitoring.

![Create a project in Langfuse](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/75bed34765ed7d0e933a0069ecb094dd.png)

Edit a name for the project.

![Create a project in Langfuse](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/26cfbb94e312a100c39e217fdd0b4406.png)

3. Create project API credentials. In the left sidebar of the project, click **Settings** to open the settings.

![Create project API credentials](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/2ed72a6761f2977201c29e67e5bc634c.png)

In Settings, click **Create API Keys** to create project API credentials.

![Create project API credentials](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/3c3fbd5392d37fbccf1f9ef76c54f0bc.png)

Copy and save the **Secret Key**, **Public Key**, and **Host**.

![Get API Key configuration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/a2ff67951ce300082d875eae8458c8c7.png)

4. Configure Langfuse in Dify. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

![Configure Langfuse](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/ebc84b328ad37c0f6dbca6101e1f90ab.png)

After clicking configure, paste the **Secret Key, Public Key, Host** created in Langfuse into the configuration and save.

![Configure Langfuse](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/5bfa409e7a073f133f21146535401512.png)

Once successfully saved, you can view the status on the current page. If it shows as started, it is being monitored.

![View configuration status](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/1aa086a1aead0e29948e7d6d5815d5d1.png)

***

### Viewing Monitoring Data in Langfuse

After configuration, debugging or production data of the application in Dify can be viewed in Langfuse.

![Debugging Applications in Dify](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/a1370fdbb79257cba31a565ac6764802.png)

![Viewing application data in Langfuse](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/integrate-external-ops-tools/b4fc3474336d5f60dc049c9153454496.png)

***

### List of monitoring data

#### Trace the information of Workflow and Chatflow

**Tracing workflow and chatflow**

| Workflow                                 | LangFuse Trace          |
| ---------------------------------------- | ----------------------- |
| workflow\_app\_log\_id/workflow\_run\_id | id                      |
| user\_session\_id                        | user\_id                |
| workflow\_{id}                           | name                    |
| start\_time                              | start\_time             |
| end\_time                                | end\_time               |
| inputs                                   | input                   |
| outputs                                  | output                  |
| Model token consumption                  | usage                   |
| metadata                                 | metadata                |
| error                                    | level                   |
| error                                    | status\_message         |
| \[workflow]                              | tags                    |
| \["message", conversation\_mode]         | session\_id             |
| conversion\_id                           | parent\_observation\_id |

**Workflow Trace Info**

* workflow\_id - Unique ID of Workflow
* conversation\_id - Conversation ID
* workflow\_run\_id - Workflow ID of this runtime
* tenant\_id - Tenant ID
* elapsed\_time - Elapsed time at this runtime
* status - Runtime status
* version - Workflow version
* total\_tokens - Total token used at this runtime
* file\_list - List of files processed
* triggered\_from - Source that triggered this runtime
* workflow\_run\_inputs - Input of this workflow
* workflow\_run\_outputs - Output of this workflow
* error - Error Message
* query - Queries used at runtime
* workflow\_app\_log\_id - Workflow Application Log ID
* message\_id - Relevant Message ID
* start\_time - Start time of this runtime
* end\_time - End time of this runtime
* workflow node executions - Workflow node runtime information
* Metadata
  * workflow\_id - Unique ID of Workflow
  * conversation\_id - Conversation ID
  * workflow\_run\_id - Workflow ID of this runtime
  * tenant\_id - Tenant ID
  * elapsed\_time - Elapsed time at this runtime
  * status - Operational state
  * version - Workflow version
  * total\_tokens - Total token used at this runtime
  * file\_list - List of files processed
  * triggered\_from - Source that triggered this runtime

#### Message Trace Info

**For trace llm conversation**

| Message                          | LangFuse Generation/Trace |
| -------------------------------- | ------------------------- |
| message\_id                      | id                        |
| user\_session\_id                | user\_id                  |
| message\_{id}                    | name                      |
| start\_time                      | start\_time               |
| end\_time                        | end\_time                 |
| inputs                           | input                     |
| outputs                          | output                    |
| Model token consumption          | usage                     |
| metadata                         | metadata                  |
| error                            | level                     |
| error                            | status\_message           |
| \["message", conversation\_mode] | tags                      |
| conversation\_id                 | session\_id               |
| conversion\_id                   | parent\_observation\_id   |

**Message Trace Info**

* message\_id - Message ID
* message\_data - Message data
* user\_session\_id - Session ID for user
* conversation\_model - Conversation model
* message\_tokens - Message tokens
* answer\_tokens - Answer Tokens
* total\_tokens - Total Tokens from Message and Answer
* error - Error Message
* inputs - Input data
* outputs - Output data
* file\_list - List of files processed
* start\_time - Start time
* end\_time - End time
* message\_file\_data - Message of relevant file data
* conversation\_mode - Conversation mode
* Metadata
  * conversation\_id - Conversation ID
  * ls\_provider - Model provider
  * ls\_model\_name - Model ID
  * status - Message status
  * from\_end\_user\_id - Sending user's ID
  * from\_account\_id - Sending account's ID
  * agent\_based - Whether agent based
  * workflow\_run\_id - Workflow ID of this runtime
  * from\_source - Message source
  * message\_id - Message ID

#### Moderation Trace Information

**Used to track conversation moderation**

| Moderation    | LangFuse Generation/Trace |
| ------------- | ------------------------- |
| user\_id      | user\_id                  |
| moderation    | name                      |
| start\_time   | start\_time               |
| end\_time     | end\_time                 |
| inputs        | input                     |
| outputs       | output                    |
| metadata      | metadata                  |
| \[moderation] | tags                      |
| message\_id   | parent\_observation\_id   |

**Message Trace Info**

* message\_id - Message ID
* user\_id - user ID
* workflow\_app\_log\_id workflow\_app\_log\_id
* inputs - Input data for review
* message\_data - Message Data
* flagged - Whether it is flagged for attention
* action - Specific actions to implement
* preset\_response - Preset response
* start\_time - Start time of review
* end\_time - End time of review
* Metadata
  * message\_id - Message ID
  * action - Specific actions to implement
  * preset\_response - Preset response

#### Suggested Question Trace Information

**Used to track suggested questions**

| Suggested Question     | LangFuse Generation/Trace |
| ---------------------- | ------------------------- |
| user\_id               | user\_id                  |
| suggested\_question    | name                      |
| start\_time            | start\_time               |
| end\_time              | end\_time                 |
| inputs                 | input                     |
| outputs                | output                    |
| metadata               | metadata                  |
| \[suggested\_question] | tags                      |
| message\_id            | parent\_observation\_id   |

**Message Trace Info**

* message\_id - Message ID
* message\_data - Message data
* inputs - Input data
* outputs - Output data
* start\_time - Start time
* end\_time - End time
* total\_tokens - Total tokens
* status - Message Status
* error - Error Message
* from\_account\_id - Sending account ID
* agent\_based - Whether agent based
* from\_source - Message source
* model\_provider - Model provider
* model\_id - Model ID
* suggested\_question - Suggested question
* level - Status level
* status\_message - Message status
* Metadata
  * message\_id - Message ID
  * ls\_provider - Model Provider
  * ls\_model\_name - Model ID
  * status - Message status
  * from\_end\_user\_id - Sending user's ID
  * from\_account\_id - Sending Account ID
  * workflow\_run\_id - Workflow ID of this runtime
  * from\_source - Message source

#### Dataset Retrieval Trace Information

**Used to track knowledge base retrieval**

| Dataset Retrieval     | LangFuse Generation/Trace |
| --------------------- | ------------------------- |
| user\_id              | user\_id                  |
| dataset\_retrieval    | name                      |
| start\_time           | start\_time               |
| end\_time             | end\_time                 |
| inputs                | input                     |
| outputs               | output                    |
| metadata              | metadata                  |
| \[dataset\_retrieval] | tags                      |
| message\_id           | parent\_observation\_id   |

**Dataset Retrieval Trace Info**

* message\_id - Message ID
* inputs - Input Message
* documents - Document data
* start\_time - Start time
* end\_time - End time
* message\_data - Message data
* Metadata
  * message\_id - Message ID
  * ls\_provider - Model Provider
  * ls\_model\_name - Model ID
  * status - Model status
  * from\_end\_user\_id - Sending user's ID
  * from\_account\_id - Sending account's ID
  * agent\_based - Whether agent based
  * workflow\_run\_id - Workflow ID of this runtime
  * from\_source - Message Source

#### Tool Trace Information

**Used to track tool invocation**

| Tool                  | LangFuse Generation/Trace |
| --------------------- | ------------------------- |
| user\_id              | user\_id                  |
| tool\_name            | name                      |
| start\_time           | start\_time               |
| end\_time             | end\_time                 |
| inputs                | input                     |
| outputs               | output                    |
| metadata              | metadata                  |
| \["tool", tool\_name] | tags                      |
| message\_id           | parent\_observation\_id   |

**Tool Trace Info**

* message\_id - Message ID
* tool\_name - Tool Name
* start\_time - Start time
* end\_time - End time
* tool\_inputs - Tool inputs
* tool\_outputs - Tool outputs
* message\_data - Message data
* error - Error Message，if exist
* inputs - Input of Message
* outputs - Output of Message
* tool\_config - Tool config
* time\_cost - Time cost
* tool\_parameters - Tool Parameters
* file\_url - URL of relevant files
* Metadata
  * message\_id - Message ID
  * tool\_name - Tool Name
  * tool\_inputs - Tool inputs
  * tool\_outputs - Tool outputs
  * tool\_config - Tool config
  * time\_cost - Time. cost
  * error - Error Message
  * tool\_parameters - Tool parameters
  * message\_file\_id - Message file ID
  * created\_by\_role - Created by role
  * created\_user\_id - Created user ID

#### Generate Name Trace

**Used to track conversation title generation**

| Generate Name     | LangFuse Generation/Trace |
| ----------------- | ------------------------- |
| user\_id          | user\_id                  |
| generate\_name    | name                      |
| start\_time       | start\_time               |
| end\_time         | end\_time                 |
| inputs            | input                     |
| outputs           | output                    |
| metadata          | metadata                  |
| \[generate\_name] | tags                      |

**Generate Name Trace Info**

* conversation\_id - Conversation ID
* inputs - Input data
* outputs - Generated session name
* start\_time - Start time
* end\_time - End time
* tenant\_id - Tenant ID
* Metadata
  * conversation\_id - Conversation ID
  * tenant\_id - Tenant ID
