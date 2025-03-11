# Initial Prompt Template References

To meet the more customized requirements of LLMs for developers, Dify fully opens up the complete prompts in **Expert Mode** and provides initial templates in the orchestration interface. Here are references for four initial templates:

### 1. Template for Building Conversational Applications Using Chat Models

* **SYSTEM**

```
Use the following context as your learned knowledge, inside <context></context> XML tags.

<context>
{{#context#}}
</context>

When answering the user:
- If you don't know, just say that you don't know.
- If you are not sure, ask for clarification.
Avoid mentioning that you obtained the information from the context.
And answer according to the language of the user's question.
{{pre_prompt}}
```

* **USER**

```
{{Query}} // Input the query variable here
```

* **ASSISTANT**

```Python
"" 
```

#### **Template Structure:**

* Context (`Context`)
* Pre-prompt (`Pre-prompt`)
* Query Variable (`Query`)

### 2. Template for Building Text Generation Applications Using Chat Models

* **SYSTEM**

```
Use the following context as your learned knowledge, inside <context></context> XML tags.

<context>
{{#context#}}
</context>

When answering the user:
- If you don't know, just say that you don't know.
- If you are not sure, ask for clarification.
Avoid mentioning that you obtained the information from the context.
And answer according to the language of the user's question.
{{pre_prompt}}
```

* **USER**

```
{{Query}} // Input the query variable here, commonly in the form of a paragraph
```

* **ASSISTANT**

```Python
"" 
```

#### **Template Structure:**

* Context (`Context`)
* Pre-prompt (`Pre-prompt`)
* Query Variable (`Query`)

### 3. Template for Building Conversational Applications Using Text Completion Models

```Python
Use the following context as your learned knowledge, inside <context></context> XML tags.

<context>
{{#context#}}
</context>

When answering the user:
- If you don't know, just say that you don't know.
- If you are not sure, ask for clarification.
Avoid mentioning that you obtained the information from the context.
And answer according to the language of the user's question.

{{pre_prompt}}

Here are the chat histories between human and assistant, inside <histories></histories> XML tags.

<histories>
{{#histories#}}
</histories>

Human: {{#query#}}

Assistant: 
```

**Template Structure:**

* Context (`Context`)
* Pre-prompt (`Pre-prompt`)
* Conversation History (`History`)
* Query Variable (`Query`)

### 4. Template for Building Text Generation Applications Using Text Completion Models

```Python
Use the following context as your learned knowledge, inside <context></context> XML tags.

<context>
{{#context#}}
</context>

When answering the user:
- If you don't know, just say that you don't know.
- If you are not sure, ask for clarification.
Avoid mentioning that you obtained the information from the context.
And answer according to the language of the user's question.

{{pre_prompt}}
{{query}}
```

**Template Structure:**

* Context (`Context`)
* Pre-prompt (`Pre-prompt`)
* Query Variable (`Query`)

{% hint style="warning" %}
Dify and some model vendors have jointly optimized the system prompts deeply. Therefore, the initial templates under some models may differ from the examples above.
{% endhint %}

### Parameter Descriptions

* Context (`Context`): Used to insert relevant text from the dataset as the context of the complete prompt.
* Pre-prompt (`Pre-prompt`): In **Easy Mode**, the pre-prompt orchestrated will be inserted into the complete prompt.
* Conversation History (`History`): When building chat applications using text generation models, the system will insert the user's conversation history as context into the complete prompt. Since some models respond differently to role prefixes, you can also modify the role prefix in the conversation history settings, e.g., changing "Assistant" to "AI".
* Query (`Query`): The query content is the variable value used to insert the user's question in the chat.