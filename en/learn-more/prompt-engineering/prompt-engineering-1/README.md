# Expert Mode for Prompt Engineering (Discontinued)

When creating an app on Dify, the default orchestration mode is **Simple Mode**, which is ideal for non-technical users who want to quickly create applications like a company knowledge base chatbot or an article summarizer. Using **Simple Mode**, you can orchestrate pre-prompt phrases, add variables, and context with simple steps to publish a complete application (refer to 👉[conversation-application.md](../../../../guides/application\_orchestrate/conversation-application.md "mention")).

However, if you are a technical user proficient in using **OpenAI's** **Playground** and want to create a learning tutor application that requires embedding different contexts and variables into the prompts for various teaching modules, you can choose **Expert Mode**. In this mode, you can freely write complete prompts, including modifying built-in prompts, adjusting the position of context and chat history within the prompts, and setting necessary parameters. If you are familiar with both Chat and Complete models, **Expert Mode** allows you to quickly switch between these models to meet your needs, and both are suitable for conversational and text generation applications.

Before you start experimenting with the new mode, you need to know the essential elements of **Expert Mode**:

* **Text Completion Model** ![](../../../../.gitbook/assets/screenshot-20231017-092613.png)

  When selecting a model, the name with COMPLETE on the right is a text completion model. This model accepts a free-form text string called a "prompt" and generates a text completion that tries to match any context or pattern you give it. For example, if your prompt is: "As Descartes said, I think therefore," it will likely return "I am" as the completion.
* **Chat Model** <img src="../../../../.gitbook/assets/screenshot-20231017-092957.png" alt="" data-size="line">

  When selecting a model, the name with CHAT on the right is a chat model. This model takes a list of messages as input and returns a generated message as output. Although the chat format is designed to simplify multi-turn conversations, it is also useful for single-turn tasks without any conversation. Chat models use chat messages as input and output, including three types of messages: SYSTEM, USER, and ASSISTANT:

  * `SYSTEM`
    * System messages help set the behavior of the AI assistant. For example, you can modify the AI assistant's personality or provide specific instructions on how it should behave throughout the conversation. System messages are optional, and the model's behavior without system messages may be similar to using a generic message like "You are a helpful assistant."
  * `USER`
    * User messages provide requests or comments for the AI assistant to respond to.
  * `ASSISTANT`
    * Assistant messages store previous assistant responses but can also be written by you to provide examples of the desired behavior.
* **Stop Sequences**

  These are specific words, phrases, or characters used to signal the LLM to stop generating text.
* **Content Blocks in Expert Mode Prompts**
  *   <img src="../../../../.gitbook/assets/3.png" alt="" data-size="line">

      In an app configured with a dataset, the user inputs a query, and the app uses this query as a retrieval condition for the dataset. The retrieved results are organized and replace the `context` variable, allowing the LLM to reference the context content to provide an answer.
  *   <img src="../../../../.gitbook/assets/4.png" alt="" data-size="line">

      The query content is only available in text completion models for conversational applications. The content input by the user in the conversation will replace this variable, triggering a new round of dialogue.
  *   <img src="../../../../.gitbook/assets/5.png" alt="" data-size="line">

      Conversation history is only available in text completion models for conversational applications. During multiple conversations in a conversational application, Dify assembles and concatenates the historical conversation records according to built-in rules and replaces the `conversation history` variable. The Human and Assistant prefixes can be modified by clicking the `...` after `conversation history`.
* **Initial Template**

  In **Expert Mode**, before formal orchestration, the prompt box provides an initial template that you can directly modify to make more customized requests to the LLM. Note: There are differences based on the type of application and mode.

  For details, please refer to 👉[prompt-engineering-template.md](prompt-engineering-template.md "mention")

## Comparison of Two Modes

| Comparison Dimension | Simple Mode | Expert Mode |
|----------------------|-------------|-------------|
| Built-in Prompt Visibility | Encapsulated and Invisible | Open and Visible |
| Automatic Orchestration | Available | Unavailable |
| Difference in Text Completion and Chat Model Selection | None | Different orchestration after selecting text completion and chat models |
| Variable Insertion | Available | Available |
| Content Block Validation | None | Available |
| SYSTEM / USER / ASSISTANT Message Type Orchestration | None | Available |
| Context Parameter Settings | Configurable | Configurable |
| View PROMPT LOG | View full prompt log | View full prompt log |
| Stop Sequences Parameter Settings | None | Configurable |

## Operating Instructions

### 1. How to Enter Expert Mode

After creating an application, you can switch to **Expert Mode** on the prompt orchestration page, where you can edit the complete application prompts.

![Expert Mode Entry](../../../../.gitbook/assets/专家模式.png)

{% hint style="warning" %}
After modifying prompts and publishing the application in **Expert Mode**, you cannot return to **Simple Mode**.
{% endhint %}

### 2. Modify Inserted Context Parameters

In both **Simple Mode** and **Expert Mode**, you can modify the parameters for the inserted context, including **TopK** and **Score Threshold**.

{% hint style="warning" %}
Note that the built-in prompt containing \{{#context#\}} will only be displayed in **Expert Mode** after uploading the context.
{% endhint %}

![Context Parameter Settings](../../../../.gitbook/assets/参数设置.png)

**TopK: Value range is an integer from 1 to 10**

Used to filter text fragments with the highest similarity to the user's question. The system will dynamically adjust the number of fragments based on the context window size of the selected model. The default value is 2. It is recommended to set this value between 2 and 5, as we expect to get answers that better match the embedded context.

**Score Threshold: Value range is a floating-point number with two decimal places from 0 to 1**

Used to set the similarity threshold for filtering text fragments, i.e., only recalling text fragments that exceed the set score (you can view the hit score of each fragment in the "Hit Test"). The system defaults to this setting being off, meaning it will not filter the recalled text fragments by similarity value. When turned on, the default value is 0.7. It is recommended to keep this setting off by default, but if you require more precise responses, you can set a higher value (the maximum value is 1, but it is not recommended to set it too high).

### 3. Set **Stop Sequences**

We do not want the LLM to generate unnecessary content, so specific words, phrases, or characters (default setting is `Human:`) need to be set to inform the LLM to stop generating text.

For example, if you write a _Few-Shot_ prompt:

```
Human1: What color is the sky?
Assistant1: The sky is blue.
Human1: What color is fire?
Assistant1: Fire is red.
Human1: What color is soil?
Assistant1: 
```

Then in the model parameters' `Stop Sequences`, input `Human1:`, and press the "Tab" key.

This way, the LLM will only respond with one sentence:

```
Assistant1: Soil is yellow.
```

And will not generate additional dialogue (i.e., the LLM will stop generating content before reaching the next "Human1:").

### 4. Quick Insert Variables and Content Blocks

In **Expert Mode**, you can type "`/`" in the text editor to quickly bring up content blocks to insert into the prompt. Content blocks include: `context`, `variable`, `conversation history`, `query content`. You can also type "`{`" to quickly insert a list of previously created variables.

![Shortcut Key “/”](../../../../.gitbook/assets/快捷键.png)

{% hint style="warning" %}
Content blocks other than "variables" cannot be inserted repeatedly. The available content blocks may vary based on the prompt template structure in different applications and models. `Conversation history` and `query content` are only available in text completion models for conversational applications.
{% endhint %}

### 5. Input Pre-prompt

The initial template of the system's prompt provides necessary parameters and LLM response requirements. For details, see 👉[prompt-engineering-template.md](prompt-engineering-template.md "mention").

The core of early orchestration by developers is the pre-prompt, which needs to be edited and inserted into the built-in prompt. The suggested insertion position is as follows (taking the creation of an "iPhone Consultation Customer Service" as an example):

```
When answering the user:
- If you don't know, just say that you don't know.
- If you don't know or are not sure, ask for clarification.
Avoid mentioning that you obtained the information from the context.
And answer according to the language of the user's question.

You are a customer service assistant for Apple Inc., and you can provide consultation services for iPhones.
When you answer, you need to list detailed iPhone parameters, and you must output this information as a vertical MARKDOWN table. If the list is too long, transpose it.
You are allowed to think for a long time to generate a more reasonable output.
Note: You currently only have information on some iPhone models, not all of them.
```

Of course, you can also customize the initial template, for example, if you want the LLM's responses to be in English, you can modify the built-in prompt as follows:

```
When answering the user:
- If you don't know, just say that you don't know.
- If you don't know or are not sure, ask for clarification.
Avoid mentioning that you obtained the information from the context.
And answer according to the language English.
```

### 6. Debug Logs

During orchestration debugging, you can not only view the user's input and the LLM's response. In **Expert Mode**, click the icon at the top left of the send message button to see the complete prompt, making it easier for developers to confirm whether the input variable content, context, chat history, and query content meet expectations. For a detailed explanation of the log list, please refer to the log documentation 👉: [logs.md](../../../../guides/biao-zhu/logs.md "mention")

#### 6.1 **View Debug Logs**

In the debug preview interface, after a conversation between the user and the AI, move the mouse pointer to any user session, and you will see the "Log" icon button at the top left. Click it to view the prompt log.

![Debug Log Entry](../../../../.gitbook/assets/日志.png)

In the log, you can clearly see:

* The complete built-in prompt
* Relevant text fragments referenced in the current session
* Historical conversation records

![View Prompt Log in Debug Preview Interface](../../../../.gitbook/assets/11.png)

From the log, you can see the complete prompt sent to the LLM after system assembly and continuously improve the prompt input based on the debugging results.

#### **6.2 Trace Debug History**

On the main interface for initial app construction, you can see "Logs and Annotations" in the left navigation bar. Click it to view the complete logs. On the main interface of Logs and Annotations, click any conversation log entry, and in the pop-up right dialog box, move the mouse pointer to the conversation to click the "Log" button to view the prompt log.

![View Prompt Log in Logs and Annotations Interface](../../../../.gitbook/assets/12.png)