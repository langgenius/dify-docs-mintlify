# LLM

### Definition

Invokes the capabilities of large language models to process information input by users in the "Start" node (natural language, uploaded files, or images) and provide effective response information.

![LLM Node](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/85730fbfa1d441d12d969b89adf2670e.png)

***

### Scenarios

LLM is the core node of Chatflow/Workflow, utilizing the conversational/generative/classification/processing capabilities of large language models to handle a wide range of tasks based on given prompts and can be used in different stages of workflows.

* **Intent Recognition**: In customer service scenarios, identifying and classifying user inquiries to guide downstream processes.
* **Text Generation**: In content creation scenarios, generating relevant text based on themes and keywords.
* **Content Classification**: In email batch processing scenarios, automatically categorizing emails, such as inquiries/complaints/spam.
* **Text Conversion**: In translation scenarios, translating user-provided text into a specified language.
* **Code Generation**: In programming assistance scenarios, generating specific business code or writing test cases based on user requirements.
* **RAG**: In knowledge base Q\&A scenarios, reorganizing retrieved relevant knowledge to respond to user questions.
* **Image Understanding**: Using multimodal models with vision capabilities to understand and answer questions about the information within images.
* **File Analysis**: In file processing scenarios, use LLMs to recognize and analyze the information contained within files.

By selecting the appropriate model and writing prompts, you can build powerful and reliable solutions within Chatflow/Workflow.

***

### How to Configure

![LLM Node Configuration - Model Selection](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/43f81418ea70d4d79e3705505e777b1b.png)

**Configuration Steps:**

1. **Select a Model**: Dify supports major global models, including OpenAI's GPT series, Anthropic's Claude series, and Google's Gemini series. Choosing a model depends on its inference capability, cost, response speed, context window, etc. You need to select a suitable model based on the scenario requirements and task type.
2. **Configure Model Parameters**: Model parameters control the generation results, such as temperature, TopP, maximum tokens, response format, etc. To facilitate selection, the system provides three preset parameter sets: Creative, Balanced, and Precise.
3. **Write Prompts**: The LLM node offers an easy-to-use prompt composition page. Selecting a chat model or completion model will display different prompt composition structures.
4. **Advanced Settings**: You can enable memory, set memory windows, and use the Jinja-2 template language for more complex prompts.

{% hint style="info" %}
If you are using Dify for the first time, you need to complete the [model configuration](../../model-configuration/) in **System Settings-Model Providers** before selecting a model in the LLM node.
{% endhint %}

#### **Writing Prompts**

In the LLM node, you can customize the model input prompts. If you select a chat model, you can customize the System/User/Assistant sections.

**Prompt Generator**

If you're struggling to come up with effective system prompts (System), you can use the Prompt Generator to quickly create prompts suitable for your specific business scenarios, leveraging AI capabilities.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/bec10045f819316f80068c563cf14eb1.png)

In the prompt editor, you can call out the **variable insertion menu** by typing `/` or `{` to insert **special variable blocks** or **upstream node variables** into the prompt as context content.

![Calling Out the Variable Insertion Menu](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d8ed0160a7fba0a14dd823ef97610cc4.png)

***

### Explanation of Special Variables

**Context Variables**

Context variables are a special type of variable defined within the LLM node, used to insert externally retrieved text content into the prompt.

![Context Variables](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/5aefed96962bd994f8f05bac96b11e22.png)

In common knowledge base Q\&A applications, the downstream node of knowledge retrieval is typically the LLM node. The **output variable** `result` of knowledge retrieval needs to be configured in the **context variable** within the LLM node for association and assignment. After association, inserting the **context variable** at the appropriate position in the prompt can incorporate the externally retrieved knowledge into the prompt.

This variable can be used not only as external knowledge introduced into the prompt context for LLM responses but also supports the application's [**citation and attribution**](../../knowledge-base/retrieval-test-and-citation#id-2.-citation-and-attribution) feature due to its data structure containing segment reference information.

{% hint style="info" %}
If the context variable is associated with a common variable from an upstream node, such as a string type variable from the start node, the context variable can still be used as external knowledge, but the **citation and attribution** feature will be disabled.
{% endhint %}

**File Variables**

Some LLMs, such as [Claude 3.5 Sonnet](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support), now support direct processing of file content, enabling the use of file variables in prompts. To prevent potential issues, application developers should verify the supported file types on the LLM's official website before utilizing the file variable.

![](https://assets-docs.dify.ai/2024/11/05b3d4a78038bc7afbb157078e3b2b26.png)

> Refer to [File Upload](https://docs.dify.ai/guides/workflow/file-upload) for guidance on building a Chatflow/Workflow application with file upload functionality.

**Conversation History**

To achieve conversational memory in text completion models (e.g., gpt-3.5-turbo-Instruct), Dify designed the conversation history variable in the original [Prompt Expert Mode (discontinued)](../../../learn-more/extended-reading/prompt-engineering/prompt-engineering-1/). This variable is carried over to the LLM node in Chatflow, used to insert chat history between the AI and the user into the prompt, helping the LLM understand the context of the conversation.

{% hint style="info" %}
The conversation history variable is not widely used and can only be inserted when selecting text completion models in Chatflow.
{% endhint %}

![Inserting Conversation History Variable](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/b8642f8c6e3f562fceeefae83628fd68.png)

**Model Parameters**

The parameters of the model affect the output of the model. Different models have different parameters. The following figure shows the parameter list for `gpt-4`.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/5eaaa3f8082b769544a02ff510b207d8.png)

The main parameter terms are explained as follows:

**Temperature**: Usually a value between 0-1, it controls randomness. The closer the temperature is to 0, the more certain and repetitive the results; the closer it is to 1, the more random the results.

**Top P**: Controls the diversity of the results. The model selects from candidate words based on probability, ensuring that the cumulative probability does not exceed the preset threshold P.

**Presence Penalty**: Used to reduce the repetitive generation of the same entity or information by imposing penalties on content that has already been generated, making the model inclined to generate new or different content. As the parameter value increases, greater penalties are applied in subsequent generations to content that has already been generated, lowering the likelihood of repeating content.

**Frequency Penalty**: Imposes penalties on words or phrases that appear too frequently by reducing their probability of generation. With an increase in parameter value, greater penalties are imposed on frequently occurring words or phrases. Higher parameter values reduce the frequency of these words, thereby increasing the lexical diversity of the text.

If you do not understand what these parameters are, you can choose to load presets and select from the three presets: Creative, Balanced, and Precise.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/b913f9cdf1f9b03e791a49836bc770dd.png)

***

### Advanced Features

**Memory**: When enabled, each input to the intent classifier will include chat history from the conversation to help the LLM understand the context and improve question comprehension in interactive dialogues.

**Memory Window**: When the memory window is closed, the system dynamically filters the amount of chat history passed based on the model's context window; when open, users can precisely control the amount of chat history passed (in terms of numbers).

**Conversation Role Name Settings**: Due to differences in model training stages, different models adhere to role name instructions differently, such as Human/Assistant, Human/AI, Human/Assistant, etc. To adapt to the prompt response effects of multiple models, the system provides conversation role name settings. Modifying the role name will change the role prefix in the conversation history.

**Jinja-2 Templates**: The LLM prompt editor supports Jinja-2 template language, allowing you to leverage this powerful Python template language for lightweight data transformation and logical processing. Refer to the [official documentation](https://jinja.palletsprojects.com/en/3.1.x/templates/).

**Retry on Failure**: For some exceptions that occur in the node, it is usually sufficient to retry the node again. When the error retry function is enabled, the node will automatically retry according to the preset strategy when an error occurs. You can adjust the maximum number of retries and the interval between each retry to set the retry strategy.

- The maximum number of retries is 10
- The maximum retry interval is 5000 ms

![](https://assets-docs.dify.ai/2024/12/dfb43c1cbbf02cdd36f7d20973a5529b.png)

**Error Handling**: Provides diverse node error handling strategies that can throw error messages when the current node fails without interrupting the main process, or continue completing tasks through backup paths. For detailed information, please refer to the [Error Handling](https://docs.dify.ai/guides/workflow/error-handling).

***

#### Use Cases

* **Reading Knowledge Base Content**

To enable workflow applications to read "[Knowledge Base](../../knowledge-base/)" content, such as building an intelligent customer service application, please follow these steps:

1. Add a knowledge base retrieval node upstream of the LLM node;
2. Fill in the **output variable** `result` of the knowledge retrieval node into the **context variable** of the LLM node;
3. Insert the **context variable** into the application prompt to give the LLM the ability to read text within the knowledge base.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/988590f51629f43ac81770396456b372.png)

The `result` variable output by the Knowledge Retrieval Node also includes segmented reference information. You can view the source of information through the **Citation and Attribution** feature.

{% hint style="info" %}
Regular variables from upstream nodes can also be filled into context variables, such as string-type variables from the start node, but the **Citation and Attribution** feature will be ineffective.
{% endhint %}

* **Reading Document Files**

To enable workflow applications to read document contents, such as building a ChatPDF application, you can follow these steps:

* Add a file variable in the "Start" node;
* Add a document extractor node upstream of the LLM node, using the file variable as an input variable;
* Fill in the **output variable** `text` of the document extractor node into the prompt of the LLM node.

For more information, please refer to [File Upload](../file-upload.md).

![input system prompts](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/373ac80deaf7ef9ed77019a94d31bed5.png)

* **Error Handling**

When processing information, LLM nodes may encounter errors such as input text exceeding token limits or missing key parameters. Developers can follow these steps to configure exception branches, enabling contingency plans when node errors occur to avoid interrupting the entire flow:

1. Enable "Error Handling" in the LLM node
2. Select and configure an error handling strategy

![input system prompts](https://assets-docs.dify.ai/2024/12/f7109ce5e87c0e0a81248bb2672c7667.png)

For more information about exception handling methods, please refer to the [Error Handling](https://docs.dify.ai/guides/workflow/error-handling).
