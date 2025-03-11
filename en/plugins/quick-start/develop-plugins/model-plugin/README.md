# Model Plugin

Model type plugins enable the Dify platform to request models from specific model providers. For example, after installing the OpenAI model plugin, the Dify platform can request models like GPT-4, GPT-4o-2024-05-13, etc., provided by OpenAI.

### **Model Plugin Structure**

To better understand the concepts involved in developing plugin models, here's an example structure within model type plugins:

* Model Provider: Large model development companies, such as OpenAI, Anthropic, Google, etc.
* Model Categories: Depending on the provider, categories include Large Language Models (LLM), Text Embedding models, Speech-to-Text models, etc.
* Specific Models: `claude-3-5-sonnet`, `gpt-4-turbo`, etc.

Code structure in plugin projects:

```bash
- Model Provider
  - Model Category
    - Specific Models
```

Taking Anthropic as an example, the model plugin structure looks like this:

```bash
- Anthropic
  - llm
    claude-3-5-sonnet-20240620
    claude-3-haiku-20240307
    claude-3-opus-20240229
    claude-3-sonnet-20240229
    claude-instant-1.2
    claude-instant-1
```

Taking OpenAI as an example, which supports multiple model types:

```bash
├── models
│ ├── llm
│ │ ├── chatgpt-4o-latest
│ │ ├── gpt-3.5-turbo
│ │ ├── gpt-4-0125-preview
│ │ ├── gpt-4-turbo
│ │ ├── gpt-4o
│ │ ├── llm
│ │ ├── o1-preview
│ │ └── text-davinci-003
│ ├── moderation
│ │ ├── moderation
│ │ └── text-moderation-stable
│ ├── speech2text
│ │ ├── speech2text
│ │ └── whisper-1
│ ├── text_embedding
│ │ ├── text-embedding-3-large
│ │ └── text_embedding
│ └── tts
│ ├── tts-1-hd
│ ├── tts-1
│ └── tts
```

### **Getting Started with Creating Model Plugins**

Please follow these steps to create a model plugin, click the document titles for specific creation guides:

1. [Create Model Provider](create-model-providers.md)
2. Integrate [Predefined](../../../guides/model-configuration/predefined-model.md)/[Custom](../../../guides/model-configuration/customizable-model.md) Models
3. [Debug Plugin](../../debug-plugin.md)
