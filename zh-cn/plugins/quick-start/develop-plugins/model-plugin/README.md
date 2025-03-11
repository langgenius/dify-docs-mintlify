# Model 插件

Model 模型插件使 Dify 平台能够调用该模型供应商下的所有 LLM。例如，安装 OpenAI 模型插件后，Dify 平台即可调用 OpenAI 提供的 `GPT-4`、`GPT-4o-2024-05-13` 等模型。

### 模型插件结构

为了便于理解在开发模型插件过程中可能涉及的概念，以下是模型插件内的结构简介：

* **模型供应商**：大模型的开发公司，例如 **OpenAI、Anthropic、Google** 等；
* **模型分类**：根据模型供应商的不同，存在大语言模型（LLM）、文本嵌入模型（Text embedding）、语音转文字（Speech2text）等分类；
* **具体模型**：`claude-3-5-sonnet`、`gpt-4-turbo` 等。

插件项目中的代码层级结构：

```bash
- 模型供应商
    - 模型分类
        - 具体模型
```

以 **Anthropic** 为例，模型插件的示例结构如下：

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

以 OpenAI 为例，因为它支持多种模型类型，所以存在多层模型分类，结构如下：

```bash
├── models
│   ├── llm
│   │   ├── chatgpt-4o-latest
│   │   ├── gpt-3.5-turbo
│   │   ├── gpt-4-0125-preview
│   │   ├── gpt-4-turbo
│   │   ├── gpt-4o
│   │   ├── llm
│   │   ├── o1-preview
│   │   └── text-davinci-003
│   ├── moderation
│   │   ├── moderation
│   │   └── text-moderation-stable
│   ├── speech2text
│   │   ├── speech2text
│   │   └── whisper-1
│   ├── text_embedding
│   │   ├── text-embedding-3-large
│   │   └── text_embedding
│   └── tts
│       ├── tts-1-hd
│       ├── tts-1
│       └── tts
```

### 开始开发模型插件

请参考以下顺序阅读文档，了解如何开发一个模型插件。

1. [创建模型供应商](create-model-providers.md)
2. 接入[预定义](../../../../guides/model-configuration/predefined-model.md) / [自定义](customizable-model.md)模型
3. [调试插件](../../debug-plugins.md)
