# Data Analysis

The **Overview -- Data Analysis** section displays metrics such as usage, active users, and LLM (Language Learning Model) invocation costs. This allows you to continuously improve the effectiveness, engagement, and cost-efficiency of your application operations. We will gradually provide more useful visualization capabilities, so please let us know what you need.

![Overview—Data Analysis](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/monitoring/273fbe372440ad8da870e6524854fa97.png)

***

**Total Messages**

Reflects the total number of daily interactions between users and AI. Each time the AI answers a user's question, it counts as one message. Prompt orchestration and debugging sessions are not included.

**Active Users**

The number of unique users who have had effective interactions with the AI, defined as having more than one question-and-answer exchange. Prompt orchestration and debugging sessions are not included.

**Average Session Interactions**

Reflects the number of continuous interactions per session user. For example, if a user has a 10-round Q\&A with the AI, it is counted as 10. This metric reflects user engagement. It is available only for conversational applications.

**Token Output Speed**

The number of tokens output per second, indirectly reflecting the model's generation rate and the application's usage frequency.

**User Satisfaction Rate**

The number of likes per 1,000 messages, reflecting the proportion of users who are very satisfied with the answers.

**Token Usage**

Reflects the daily token expenditure for language model requests by the application, useful for cost control.

**Total Conversations**

Daily AI conversation count; each new conversation session counts as one. A single conversation session may contain multiple message exchanges; messages related to prompt engineering and debugging are not included.
