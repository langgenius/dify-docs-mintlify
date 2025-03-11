# How to Build an AI Image Generation App

> Author: Steven Lynn. Dify Technical Writer.

With the rise of image generation, many excellent image generation products have emerged, such as Dall-e, Flux, Stable Diffusion, etc.

In this article, you will learn how to develop an AI image generation app using Dify.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/05ff829cf382e82c9ece2676032d2383.png)

## You Will Learn

* Methods for building an Agent using Dify
* Basic concepts of Agent
* Fundamentals of prompt engineering
* Tool usage
* Concepts of large model hallucinations

## 1. Setting Stablility API Key

[Click here](https://platform.stability.ai/account/keys) to go to the Stability API key management page.

If you haven't registered yet, you will be asked to register before entering the API management page.

After entering the management page, click `copy` to copy the key.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/f73d82756bdf93c8863ac0b1f55fa5af.png)

Next, you need to fill in the key in [Dify - Tools - Stability](https://cloud.dify.ai/tools) by following these steps:

* Log in to Dify
* Enter Tools
* Select Stability
* Click `Authorize`

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/bcc961ffc8a341c8ba3137e475072f99.png)

* Fill in the key and save

## 2. Configure Model Providers

To optimize interaction, we need an LLM to concretize user instructions, i.e., to write prompts for generating images. Next, we will configure model providers in Dify following these steps.

The Free version of Dify provides 200 free OpenAI message credits.

If the message credits are insufficient, you can customize other model providers by following the steps in the image below:

Click **Your Avatar - Settings - Model Provider**

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/4b4102f9027e2bda3fc520eaa8ea2354.png)

If you haven't found a suitable model provider, the groq platform provides free call credits for LLMs like Llama.

Log in to [groq API Management Page](https://console.groq.com/keys)

Click **Create API Key**, set a desired name, and copy the API Key.

Back to **Dify - Model Providers**, select **groqcloud**, and click **Setup**.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/0fda6e81dc23974576ddc21bda96e26d.png)

Paste the API Key and save.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/b250952afad12b39613aa27da5335fa3.png)

## 3. Build an Agent

Back to **Dify - Studio**, select **Create from Blank**.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/3b86940eadfe0ce14d175a9bb80fe5a9.png)

In this experiment, we only need to understand the basic usage of Agent.

{% hint style="info" %}
**What is an Agent**

An Agent is an AI system that simulates human behavior and capabilities. It interacts with the environment through natural language processing, understands input information, and generates corresponding outputs. The Agent also has "perception" capabilities, can process and analyze various forms of data, and can call and use various external tools and APIs to complete tasks, extending its functional scope. This design allows the Agent to handle complex situations more flexibly and simulate human thinking and behavior patterns to some extent.
{% endhint %}

Select **Agent**, fill in the name.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/139ac0d2f4a10e2ec0e191457f4687a1.png)

Next, you will enter the Agent orchestration interface as shown below.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/9045dbab8600e9c9d9632add787f26a6.png)

Select the LLM. Here we use Llama-3.1-70B provided by groq as an example:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/47edc14c1d3c68eeb4ee4807b35df185.png)

Select Stability in **Tools**:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/6e1c3dd63925fd9ba60568deb2602044.png)

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/539060be4e014126f9c5fc96c53dc5a4.png)

### Write Prompts

Prompts are the soul of the Agent and directly affect the output effect. Generally, the more specific the prompts, the better the output, but overly lengthy prompts can also lead to negative effects.

The engineering of adjusting prompts is called Prompt Engineering.

In this experiment, you don't need to worry about not mastering Prompt Engineering; we will learn it step by step later.

Let's start with the simplest prompts:

```
Draw the specified content according to the user's prompt using stability_text2image.
```

Each time the user inputs a command, the Agent will know this system-level instruction, thus understanding that when executing a user's drawing task, it needs to call stability tool.

For example: Draw a girl holding an open book.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/05ff829cf382e82c9ece2676032d2383.png)

### Don't want to write prompts? Of course you can!

Click **Generate** in the upper right corner of Instructions.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/426a416e468b9f495eb13ac2986acdca.png)

Enter your requirements in the **Instructions** and click **Generate**. The generated prompts on the right will show AI-generated prompts.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/d750983264182e7af5014d5df4477e31.png)

However, to develop a good understanding of prompts, we should not rely on this feature in the early stages.

## Publish

Click the publish button in the upper right corner, and after publishing, select **Run App** to get a web page for an online running Agent.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/38a1bf752ca1fc71eccbbfd18046f5bc.png)

Copy the URL of this web page to share with other friends.

## Question 1: How to Specify the Style of Generated Images?

We can add style instructions in the user's input command, for example: Anime style, draw a girl holding an open book.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/d2d883d887272786ee19d97894cbb307.png)

But if we want set the default style to anime style, we can add it to the system prompt because we previously learned that the system prompt is known each time the user command is executed and has a higher priority.

```
Draw the specified content according to the user's prompt using stability_text2image, the picture is in anime style.
```

## Question 2: How to Reject Certain Requests from Some Users?

In many business scenarios, we need to avoid outputting some unreasonable content, but LLMs are often "dumb" and will follow user instructions without question, even if the output content is wrong. This phenomenon of the model trying hard to answer users by fabricating false content is called **model hallucinations**. Therefore, we need the model to refuse user requests when necessary.

Additionally, users may also ask some content unrelated to the business, and we also need the Agent to refuse such requests.

We can use markdown format to categorize different prompts, writing the prompts that teach the Agent to refuse unreasonable content under the "Constraints" title. Of course, this format is just for standardization, and you can have your own format.

```
## Task
Draw the specified content according to the user's prompt using stability_text2image, the picture is in anime style.

## Constraints
If the user requests content unrelated to drawing, reply: "Sorry, I don't understand what you're saying."
```

For example, let's ask: What's for dinner tonight?

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/06dcf569989d797919fbe49ab8d5cadc.png)

In some more formal business scenarios, we can call a sensitive word library to refuse user requests.

Add the keyword "dinner" in **Add Feature - Content Moderation**. When the user inputs the keyword, the Agent app outputs "Sorry, I don't understand what you're saying."

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/basic/828b27d1a873ff7b4b44f76d93229225.png)
