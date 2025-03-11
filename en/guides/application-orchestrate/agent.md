# Agent

## Definition

An Agent Assistant can leverage the reasoning abilities of large language models (LLMs). It independently sets goals, simplifies complex tasks, operates tools, and refines processes to complete tasks autonomously.

## Usage Instructions

To facilitate quick learning and use, application templates for the Agent Assistant are available in the 'Explore' section. You can integrate these templates into your workspace. The new Dify 'Studio' also allows the creation of a custom Agent Assistant to suit individual requirements. This assistant can assist in analyzing financial reports, composing reports, designing logos, and organizing travel plans.

![Explore-Agent Assistant Application Template](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/83bd71eba743301bc108ea5e9289b00a.png)

The task completion ability of the Agent Assistant depends on the inference capabilities of the model selected. We recommend using a more powerful model series like GPT-4 when employing Agent Assistant to achieve more stable task completion results.

![Selecting the Reasoning Model for Agent Assistant](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/9843518e4e543071dde7f9b7f1ce527c.png)

You can write prompts for the Agent Assistant in 'Instructions'. To achieve optimal results, you can clearly define its task objectives, workflow, resources, and limitations in the instructions.

![Orchestrating Prompts for Agent Assistant](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/c2cf3853cfda01d111df29dffdef8efe.png)

## Adding Tools for the Agent Assistant

In the "Context" section, you can incorporate knowledge base tools that the Agent Assistant can utilize for information retrieval. This will assist in providing it with external background knowledge.

In the "Tools" section, you are able to add tools that are required for use. These tools can enhance the capabilities of LLMs, such as internet searches, scientific computations, or image creation, thereby enriching the LLM's ability to interact with the real world. Dify offers two types of tools: **built-in tools and custom tools.**

You have the option to directly use built-in tools in Dify, or you can easily import custom API tools (currently supporting OpenAPI/Swagger and OpenAI Plugin standards).

![Adding Tools for the Assistant](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/427269890d201edf077280ff21d6ee17.png)

The **Tools** feature allows you to create more powerful AI applications on Dify. For example, you can orchestrate suitable tools for Agent Assistant, enabling it to complete complex tasks through reasoning, step decomposition, and tool invocation.

Additionally, the tool simplifies the integration of your application with other systems or services, enabling interactions with the external environment, such as executing code or accessing proprietary information sources. Simply mention the name of the tool you want to invoke in the chat box, and it will be automatically activated.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/bf067815b692fc617c4f23f02e687dd9.png)

## Agent Settings

On Dify, two inference modes are provided for Agent Assistant: Function Calling and ReAct. Models like GPT-3.5 and GPT-4 that support Function Calling have demonstrated better and more stable performance. For model series that do not support Function Calling, we have implemented the ReAct inference framework to achieve similar effects.

In the Agent settings, you can modify the iteration limit of the Agent.

![Function Calling Mode](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/03d1837e32321ba352e8df2abf9b0671.png)

![ReAct Mode](../../.gitbook/assets/guides/application_orchestrate/agent/sec-7.png)

## Configuring the Conversation Opener

You can set up a conversation opener and initial questions for your Agent Assistant. The configured conversation opener will be displayed at the beginning of each user's first interaction, showcasing the types of tasks the Agent can perform, along with examples of questions that can be asked.

![Configuring the Conversation Opener and Initial Questions](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/67818c83a30cae24eb7048fe9dc96538.png)

### Uploading Documentation File

Some LLMs now natively support file processing, such as [Claude 3.5 Sonnet](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support) and [Gemini 1.5 Pro](https://ai.google.dev/api/files). You can check the LLMs' websites for details on their file upload capabilities.

Select an LLM that supports file reading and enable the "Documentation" feature. This enables the Chatbot to recognize files without complex configurations.

![](https://assets-docs.dify.ai/2024/11/9f0b7a3c67b58c0bd7926501284cbb7d.png)

## Debugging and Preview

After orchestrating your Agent Assistant, you have the option to debug and preview it before publishing it as an application. This allows you to assess the effectiveness of the agent in completing tasks.

![Debugging and Preview](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/6561599c7b57818a45fb2e380b00ba28.png)

## Application Publish

![Publishing the Application as a Webapp](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/7f5513a74e2dbfc8ac0039a143a12f68.png)
