# Chatbot Application

Chatbot applications use a one-question-one-answer mode to have a continuous conversation with the user.

### Applicable scenarios

Chatbot applications can be used in fields such as customer service, online education, healthcare, financial services, etc. These applications can help organizations improve work efficiency, reduce labor costs, and provide a better user experience.

### How to compose

Chatbot applications supports: prompts, variables, context, opening remarks, and suggestions for the next question.

Here, we use a interviewer application as an example to introduce the way to compose a Chatbot applications.

#### Step 1 Create an application

Click the "Create Application" button on the homepage to create an application. Fill in the application name, and select **"Chatbot"**.

![](https://assets-docs.dify.ai/2024/12/8012e6ed06bfb10b239a4b999b1a0787.png)

#### Step 2: Compose the Application

After the application is successfully created, it will automatically redirect to the application overview page. Click on the button on the left menu: **"Orchestrate"** to compose the application.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/6e45b9cecf2280814de20375ca0a3734.png)

**2.1 Fill in Prompts**

Prompt phrases are used to guide AI in providing professional responses, making the replies more precise. You can utilize the built-in prompt generator to craft suitable prompts. Prompts support the insertion of form variables, such as `{{input}}`. The values in the prompt variables will be replaced with the values filled in by the user.

Example:

1. Enter the interview scenario command.
2. The prompt will automatically generate on the right side content box.
3. You can insert custom variables within the prompt to tailor it to specific needs or details.

For a better experience, we will add an opening dialogue: `"Hello, {{name}}. I'm your interviewer, Bob. Are you ready?"`

To add the opening dialogue, click the "Add Feature" button in the upper left corner, and enable the "Conversation remarkers" feature:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/86ff7c2f2c29bc4a31e3b4a255ecbb84.png)

And then edit the opening remarks:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/30f248ed143042b06d46b95c4f062fe1.png)

**2.2 Adding Context**

If an application wants to generate content based on private contextual conversations, it can use our [knowledge](../knowledge-base/) feature. Click the "Add" button in the context to add a knowledge base.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/dcdcfbe0d7b44792c53d1d026aeebe29.png)

**2.3 Uploading Documentation File**

Some LLMs now natively support file processing, such as [Claude 3.5 Sonnet](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support) and [Gemini 1.5 Pro](https://ai.google.dev/api/files). You can check the LLMs' websites for details on their file upload capabilities.

Select an LLM that supports file reading and enable the "Documentation" feature. This enables the Chatbot to recognize files without complex configurations.

![](https://assets-docs.dify.ai/2024/11/823399d85e8ced5068dc9da4f693170e.png)

**2.4 Debugging**

Enter user inputs on the right side and check the respond content.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/1509ff763400980eba81dac1f01d996f.png)

If the results are not satisfactory, you can adjust the prompts and model parameters. Click on the model name in the upper right corner to set the parameters of the model:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/07a8c40ba969e849f083e27dee6992b0.png)

**Multiple Model Debugging:**

If the LLM’s response is unsatisfactory, you can refine the prompt or switch to different underlying models for comparison. To simultaneously observe how multiple models respond to the same question, see [Multiple Model Debugging](./multiple-llms-debugging.md).


**2.4 Publish App**

After debugging your application, click the **"Publish"** button in the top right corner to create a standalone AI application. In addition to experiencing the application via a public URL, you can also perform secondary development based on APIs, embed it into websites, and more. For details, please refer to [Publishing](https://docs.dify.ai/guides/application-publishing).

If you want to customize the application that you share, you can Fork our open source [WebApp template](https://github.com/langgenius/webapp-conversation). Based on the template, you can modify the application to meet your specific needs and style requirements.

### FAQ

**How ​​to add a third-party tool within the chatbot?**

The chatbot app does not support adding third-party tools. You can add third-party tools within your [agent](../application-orchestrate/agent.md).
