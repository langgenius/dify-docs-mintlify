# Moderation Tool

In our interactions with AI applications, we often have stringent requirements in terms of content security, user experience, and legal regulations. At this point, we need the "Sensitive Word Review" feature to create a better interactive environment for end-users. On the orchestration page, click "Add Feature" and locate the "Content Review" toolbox at the bottom:

![Content moderation](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/app-toolkits/63c5c0be18933a0578edf72c2eed1609.png)

## Call the OpenAI Moderation API

OpenAI, along with most companies providing LLMs, includes content moderation features in their models to ensure that outputs do not contain controversial content, such as violence, sexual content, and illegal activities. Additionally, OpenAI has made this content moderation capability available, which you can refer to [OpenAI's Moderation](https://platform.openai.com/docs/guides/moderation/overview).

Now you can also directly call the OpenAI Moderation API on Dify; you can review either input or output content simply by entering the corresponding "preset reply."

![Configuring Load Balancing from Add Model](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/app-toolkits/959415a64f32ee28461441847a96ae64.png)

## Keywords

Developers can customize the sensitive words they need to review, such as using "kill" as a keyword to perform an audit action when users input. The preset reply content should be "The content is violating usage policies." It can be anticipated that when a user inputs a text chuck containing "kill" at the terminal, it will trigger the sensitive word review tool and return the preset reply content.

![Configuring Load Balancing from Add Model](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/app-toolkits/15652f65c3af15d931598a866a7baa17.png)

## Moderation Extension

Different enterprises often have their own mechanisms for sensitive word moderation. When developing their own AI applications, such as an internal knowledge base ChatBot, enterprises need to moderate the query content input by employees for sensitive words. For this purpose, developers can write an API extension based on their enterprise's internal sensitive word moderation mechanisms, which can then be called on Dify to achieve a high degree of customization and privacy protection for sensitive word review.

![Moderation Extension](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-orchestrate/app-toolkits/d101ff5542c53b7ca6f8d57d24193916.png)
