---
cover: ../../.gitbook/assets/%E7%94%BB%E6%9D%BF_1.png
coverY: 0
---

# Generating analysis of Twitter account using Chatflow Agent

## Introduction

In Dify, you can use some crawler tools, such as Jina, which can convert web pages into markdown format that LLMs can read.

Recently, [wordware.ai](https://www.wordware.ai/) has brought to our attention that we can use crawlers to scrape social media for LLM analysis, creating more interesting applications.

However, knowing that X (formerly Twitter) stopped providing free API access on February 2, 2023, and has since upgraded its anti-crawling measures. Tools like Jina are unable to access X's content directly.

> Starting February 9, we will no longer support free access to the Twitter API, both v2 and v1.1. A paid basic tier will be available instead 🧵
>
> — Developers (@XDevelopers) [February 2, 2023](https://twitter.com/XDevelopers/status/1621026986784337922?ref\_src=twsrc%5Etfw)

Fortunately, Dify also has an HTTP tool, which allows us to call external crawling tools by sending HTTP requests. Let's get started!

## **Prerequisites**

### Register Crawlbase

Crawlbase is an all-in-one data crawling and scraping platform designed for businesses and developers.

Moreover, using Crawlbase Scraper allows you to scrape data from social platforms like X, Facebook and Instagram.

Click to register: [crawlbase.com](https://crawlbase.com)

### Deploy Dify locally

Dify is an open-source LLM app development platform. You can choose cloud service or deploy it locally using docker compose.

In this article, If you don’t want to deploy it locally, register a free Dify Cloud sandbox account here: [https://cloud.dify.ai/signin](https://cloud.dify.ai/signin).

{% hint style="info" %}
Dify Cloud Sandbox users get 200 free credits, equivalent to 200 GPT-3.5 messages or 20 GPT-4 messages. 
{% endhint %}

The following are brief tutorials on how to deploy Dify:

#### Clone Dify

```bash
git clone https://github.com/langgenius/dify.git
```

#### **Start Dify**

```bash
cd dify/docker
cp .env.example .env
docker compose up -d
```

### Configure LLM Providers

Configure Model Provider in account setting:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/4b4102f9027e2bda3fc520eaa8ea2354.png)

## Create a chatflow

Now, let's get started on the chatflow.

Click on `Create from Blank` to start:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/b2955735f5c122d8a2fc08ef13654239.png)

The initialized chatflow should be like:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/baee341b771d1cd77780fd4845b467b2.png)

## Add nodes to chatflow

![The final chatflow looks like this](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/bad3185d9f2c92994c24de65a5414182.png)

### Start node

In start node, we can add some system variables at the beginning of a chat. In this article, we need a Twitter user’s ID as a string variable. Let’s name it `id` .

Click on Start node and add a new variable:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/a041be2230364d7e729527f3f7af34d8.png)

### Code node

According to [Crawlbase docs](https://crawlbase.com/docs/crawling-api/scrapers/#twitter-profile), the variable `url` (this will be used in the following node) should be `https://twitter.com/` + `user id` , such as `https://twitter.com/elonmusk` for Elon Musk.

To convert the user ID into a complete URL, we can use the following Python code to integrate the prefix `https://twitter.com/` with the user ID:

```python
def main(id: str) -> dict:
    return {
        "url": "https://twitter.com/"+id,
    }
```

Add a code node and select python, and set input and output variable names:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/e5523ba1f801f4009b74e7cf03e2ef2f.png)

### HTTP request node

Based on the [Crawlbase docs](https://crawlbase.com/docs/crawling-api/scrapers/#twitter-profile), to scrape a Twitter user’s profile in http format, we need to complete HTTP request node in the following format:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/13899d88abeb3b3be20c44d40565a5f9.png)

Importantly, it is best not to directly enter the token value as plain text for security reasons, as this is not a good practice. Actually, in the latest version of Dify, we can set token values in **`Environment Variables`**. Click `env` - `Add Variable` to set the token value, so plain text will not appear in the node.

Check [https://crawlbase.com/dashboard/account/docs](https://crawlbase.com/dashboard/account/docs) for your crawlbase API Key.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/c99b66ac8d30289615a8869bae5a6455.png)

By typing `/` , you can easily insert the API Key as a variable.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/51f9350677acb396bad5841fa80c903c.png)

Tap the start button of this node to check whether it works correctly:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/094b96e513169a47f1749e46e1357893.png)

### LLM node

Now, we can use LLM to analyze the result scraped by crawlbase and execute our command.

The value `context` should be `body` from HTTP Request node.

The following is a sample system prompt.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/46f4e15ac1e9d3ca3f47dc5bb921ff01.png)

## Test run

Click `Preview` to start a test run and input twitter user id in `id`

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/a25b122dfa14f0c65fcd3498ccf1898e.png)

For example, I want to analyze Elon Musk's tweets and write a tweet about global warming in his tone.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/835a01082e74723138d9f97bee0c6c4b.png)

Does this sound like Elon? lol

Click `Publish` in the upper right corner and add it in your website.

Have fun!

## Lastly…

### Other X(Twitter) Crawlers

In this article, I’ve introduced crawlbase. It should be the cheapest Twitter crawler service available, but sometimes it cannot correctly scrape the content of user tweets.

The Twitter crawler service used by [wordware.ai](http://wordware.ai) mentioned earlier is **Tweet Scraper V2**, but the subscription for the hosted platform **apify** is $49 per month.

## Links

* [X@dify\_ai](https://x.com/dify\_ai)
* Dify’s repo on GitHub:[https://github.com/langgenius/dify](https://github.com/langgenius/dify)
