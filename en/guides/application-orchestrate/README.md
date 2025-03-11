# Application Orchestration

In Dify, an "application" refers to a practical scenario application built on large language models like GPT. By creating an application, you can apply intelligent AI technology to specific needs. It encompasses both the engineering paradigm for developing AI applications and the specific deliverables.

In short, an application provides developers with:

* A user-friendly API that can be directly called by backend or frontend applications, authenticated via Token
* A ready-to-use, aesthetically pleasing, and hosted WebApp, which you can further develop using the WebApp template
* An easy-to-use interface that includes prompt engineering, context management, log analysis, and annotation

You can choose **any one** or **all** of these to support your AI application development.

### Application Types <a href="#application_type" id="application_type"></a>

Dify offers five types of applications:

* **Chatbot**: A conversational assistant built on LLM
* **Text Generator**: An assistant for text generation tasks such as writing stories, text classification, translation, etc.
* **Agent**: A conversational intelligent assistant capable of task decomposition, reasoning, and tool invocation
* **Chatflow**: A workflow orchestration for multi-round complex dialogue tasks with memory capabilities
* **Workflow**: A workflow orchestration for single-round tasks like automation and batch processing

The differences between Text Generator and Chatbot are shown in the table below:

<table><thead><tr><th width="180.33333333333331"></th><th>Text Generator</th><th>Chatbot</th></tr></thead><tbody><tr><td>WebApp Interface</td><td>Form + Results</td><td>Chat-based</td></tr><tr><td>WebAPI Endpoint</td><td><code>completion-messages</code></td><td><code>chat-messages</code></td></tr><tr><td>Interaction Mode</td><td>One question, one answer</td><td>Multi-turn conversation</td></tr><tr><td>Streaming Results</td><td>Supported</td><td>Supported</td></tr><tr><td>Context Preservation</td><td>Per session</td><td>Continuous</td></tr><tr><td>User Input Form</td><td>Supported</td><td>Supported</td></tr><tr><td>Datasets and Plugins</td><td>Supported</td><td>Supported</td></tr><tr><td>AI Opening Remarks</td><td>Not supported</td><td>Supported</td></tr><tr><td>Example Scenarios</td><td>Translation, judgment, indexing</td><td>Chatting</td></tr></tbody></table>

###