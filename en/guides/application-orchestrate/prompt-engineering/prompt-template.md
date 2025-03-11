# Prompt Template

In order to meet the more customized requirements of developers for LLM, Dify has fully opened the built-in complete prompts in the **Expert Mode** and provided initial templates in the composition interface. Below are four initial templates for reference:

### 1. Using Chat models to build Conversational apps

* **SYSTEM**

```
Use the following context as your learned knowledge, inside <context></context> XML tags.

<context>
{{#context#}}
</context>

When answer to user:
- If you don't know, just say that you don't know.
- If you don't know when you are not sure, ask for clarification.
Avoid mentioning that you obtained the information from the context.
And answer according to the language of the user's question.
{{pre_prompt}}
```

* **USER**

```
{{Query}} //Enter the Query variables here.
```

* **ASSISTANT**

```
""
```

#### **Prompt Structure：**

* `Context`
* `Pre-prompt`
* `Query`

### 2. Using Chat models to build Text Generator apps

* **SYSTEM**

```
Use the following context as your learned knowledge, inside <context></context> XML tags.

<context>
{{#context#}}
</context>

When answer to user:
- If you don't know, just say that you don't know.
- If you don't know when you are not sure, ask for clarification.
Avoid mentioning that you obtained the information from the context.
And answer according to the language of the user's question.
{{pre_prompt}}
```

* **USER**

```
{{Query}} //Enter the Query variables here.
```

* **ASSISTANT**

```
""
```

#### **Prompt Structure：**

* `Context`
* `Pre-prompt`
* `Query`

### 3. Using Complete models to build Conversational apps

```
Use the following context as your learned knowledge, inside <context></context> XML tags.

<context>
{{#context#}}
</context>

When answer to user:
- If you don't know, just say that you don't know.
- If you don't know when you are not sure, ask for clarification.
Avoid mentioning that you obtained the information from the context.
And answer according to the language of the user's question.

{{pre_prompt}}

Here is the chat histories between human and assistant, inside <histories></histories> XML tags.

<histories>
{{#histories#}}
</histories>


Human: {{#query#}}

Assistant: 
```

**Prompt Structure：**

* `Context`
* `Pre-prompt`
* `History`
* `Query`

### 4. Using Complete models to build Text Generator apps

```
Use the following context as your learned knowledge, inside <context></context> XML tags.

<context>
{{#context#}}
</context>

When answer to user:
- If you don't know, just say that you don't know.
- If you don't know when you are not sure, ask for clarification.
Avoid mentioning that you obtained the information from the context.
And answer according to the language of the user's question.

{{pre_prompt}}
{{query}}
```

#### **Prompt Structure：**

* `Context`
* `Pre-prompt`
* `Query`

{% hint style="warning" %}
Dify has collaborated with some model providers for joint deep optimization of system prompts, and the initial templates for some models may differ from the examples provided above.
{% endhint %}

### **Parameter Definitions**

* **Context**: Used to insert related text from the knowledge as context into the complete prompts.
* **Pre-prompt**: Pre-prompts arranged in the **Basic Mode** are inserted into the complete prompts.
* **History**: When building a chat application using text generation models, the system inserts the user's conversation history as context into the complete prompts. Since some models may respond differently to role prefixes, you can also modify the role prefix name in the conversation history settings, for example, changing the name "Assistant" to "AI".
* **Query**: The query content represents variable values used to insert questions that users input during the chat.
