# Build a Notion AI Assistant

### Intro

Notion is a powerful tool for managing knowledge. Its flexibility and extensibility make it an excellent personal knowledge library and shared workspace. Many people use it to store their knowledge and work in collaboration with others, facilitating the exchange of ideas and the creation of new knowledge.

However, this knowledge remains static, as users must search for the information they need and read through it to find the answers they're seeking. This process is neither particularly efficient nor intelligent.

Have you ever dreamed of having an AI assistant based on your Notion library? This assistant would not only assist you in reviewing your knowledge base, but also engage in the communication like a seasoned butler, even answering other people's questions as if you were the master of your personal Notion library.

### How to Make Your Notion AI Assistant Come True?

Now, you can make this dream come true through [Dify](https://dify.ai/). Dify is an open-source LLMOps (Large Language Models Ops) platform.

Large Language Models like ChatGPT and Claude, have been using their impressive abilities to reshape the world. Their powerful learning aptitude primarily attributable to robust training data. Luckily, they've evolved to be sufficiently intelligent to learn from the content you provide, thus making the process of ideating from your personal Notion library, a reality.

Without Dify, you might need to acquaint yourself with langchain, an abstraction that streamlines the process of assembling these pieces.

### How to Use Dify to Build Your Personal Notion AI Assistant?

The process to train a Notion AI assistant is relatively straightforward. Just follow these steps:

1. Login to Dify.
2. Create a new datasets.
3. Connect with Notion and your datasets.
4. Start training.
5. Create your own AI application.

#### 1. Login to dify

Click [here](https://dify.ai/) to login to Dify. You can conveniently log in using your GitHub or Google account.

> If you are using GitHub account to login, how about getting this [project](https://github.com/langgenius/dify) a star? It really help us a lot!

#### 2. Create new knowledge base

Click the `Knowledge` button on the top side bar, followed by the `Create Knowledge` button.

![login-2](../../.gitbook/assets/login-2.png)

#### 3. Connect with Notion and Your Knowledge[​](https://wsyfin.com/notion-dify#3-connect-with-notion-and-datasets)

Select "Sync from Notion" and then click the "Connect" button..

![connect-with-notion-1](../../.gitbook/assets/connect-with-notion-1.png)

Afterward, you'll be redirected to the Notion login page. Log in with your Notion account.

![](../../.gitbook/assets/connect-with-notion-2.png)

Check the permissions needed by Dify, and then click the "Select pages" button.

![](../../.gitbook/assets/connect-with-notion-3.png)

Select the pages you want to synchronize with Dify, and press the "Allow access" button.

![](../../.gitbook/assets/connect-with-notion-4.png)

#### 4. Start training[​](https://wsyfin.com/notion-dify#4-start-training) <a href="#id-4-start-training" id="id-4-start-training"></a>

Specifying the pages for AI need to study, enabling it to comprehend the content within this section of Notion. Then click the "next" button.

![train-1](../../.gitbook/assets/train-1.png)

We suggest selecting the "Automatic" and "High Quality" options to train your AI assistant. Then click the "Save & Process" button.

![train-2](../../.gitbook/assets/train-2.png)

Enjoy your coffee while waiting for the training process to complete.

![train-3](../../.gitbook/assets/train-3.png)

#### 5. Create Your AI application[​](https://wsyfin.com/notion-dify#5-create-your-ai-application) <a href="#id-5-create-your-own-ai-application" id="id-5-create-your-own-ai-application"></a>

You must create an AI application and link it with the knowledge you've recently created.

Return to the dashboard, and click the "Create new APP" button. It's recommended to use the Chat App directly.

![create-app-1](../../.gitbook/assets/create-app-1.png)

Select the "Prompt Eng." and link your notion datasets in the "context".

![create-app-2](../../.gitbook/assets/create-app-2.png)

I recommend adding a 'Pre Prompt' to your AI application. Just like spells are essential to Harry Potter, similarly, certain tools or features can greatly enhance the ability of AI application.

For example, if your Notion notes focus on problem-solving in software development, could write in one of the prompts:

_I want you to act as an IT Expert in my Notion workspace, using your knowledge of computer science, network infrastructure, Notion notes, and IT security to solve the problems_.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/f5a5e95e1120906669b3c1ad4e186dea.png)

It's recommended to initially enable the AI to actively furnish the users with a starter sentence, providing a clue as to what they can ask. Furthermore, activating the 'Speech to Text' feature can allow users to interact with your AI assistant using their voice.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/ffa36d0313dba8ac4255424c4f880191.png)

Finally, Click the "Publish" button on the top right of the page. Now you can click the public URL in the "Monitoring" section to converse with your personalized AI assistant!

![create-app-4](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/1f8c6f7d7f3d61a1928d25ab85f7b1ff.png)

### Utilizing API to Integrate With Your Project <a href="#utilizing-api-to-integrate-with-your-project" id="utilizing-api-to-integrate-with-your-project"></a>

Each AI application baked by Dify can be accessed via its API. This method allows developers to tap directly into the robust characteristics of large language models (LLMs) within frontend applications, delivering a true "Backend-as-a-Service" (BaaS) experience.

With effortless API integration, you can conveniently invoke your Notion AI application without the need for intricate configurations.

Click the "API Reference" button on the page of Overview page. You can refer to it as your App's API document.

![using-api-1](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/4062ac40525d573f14a8059a6605688a.png)

#### 1. Generate API Secret Key[​](https://wsyfin.com/notion-dify#1-generate-api-secret-key) <a href="#id-1-generate-api-secret-key" id="id-1-generate-api-secret-key"></a>

For security reasons, it's recommended to create a new API secret key to access your AI application.

![using-api-2](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/b2546aa50caff4316798edc0b950661d.png)

#### 2. Retrieve Conversation ID[​](https://wsyfin.com/notion-dify#2-retrieve-conversation-id) <a href="#id-2-retrieve-conversation-id" id="id-2-retrieve-conversation-id"></a>

After chatting with your AI application, you can retrieve the session ID from the "Logs & Ann." pages.

![using-api-3](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/6feec1081814299c574b5fb4af3f2bb8.png)

#### 3. Invoke API[​](https://wsyfin.com/notion-dify#3-invoke-api) <a href="#id-3-invoke-api" id="id-3-invoke-api"></a>

You can run the example request code on the API document to invoke your AI application in terminal.

Remember to replace `YOUR SECRET KEY` and `conversation_id` on your code.

> You can input empty `conversation_id` at the first time, and replace it after you receive response contained `conversation_id`.

```
curl --location --request POST 'https://api.dify.ai/v1/chat-messages' \
--header 'Authorization: Bearer ENTER-YOUR-SECRET-KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "query": "eh",
    "response_mode": "streaming",
    "conversation_id": "",
    "user": "abc-123"
}'
```

Sending request in terminal and you will get a successful response.

![using-api-4](../../.gitbook/assets/using-api-4.png)

If you want to continue this chat, go to replace the `conversation_id` of the request code to the `conversation_id` you get from the response.

And you can check all the conversation history on the "Logs & Ann." page.

![using-api-5](../../.gitbook/assets/using-api-5.png)

### Sync with notion periodically[​](https://wsyfin.com/notion-dify#sync-with-notion-periodically) <a href="#sync-with-notion-periodically" id="sync-with-notion-periodically"></a>

If your Notion's pages have updated, you can sync with Dify periodically to keep your AI assistant up-to-date. Your AI assistant will learn from the new content.

![create-app-5](../../.gitbook/assets/create-app-5.png)

### Summary[​](https://wsyfin.com/notion-dify#summary) <a href="#summary" id="summary"></a>

In this tutorial, we have learned not only how to import Your Notion data into Dify, but also know how to use the API to integrate it with your project.

[Dify](https://dify.ai/) is a user-friendly LLMOps platform targeted to empower more individuals to create sustainable, AI-native applications. With visual orchestration designed for various application types, Dify offers ready-to-use applications that can assist you in utilizing data to craft your distinctive AI assistant. Do not hesitate to contact us if you have any inquiries.
