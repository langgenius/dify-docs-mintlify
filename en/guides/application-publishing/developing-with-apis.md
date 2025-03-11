# Developing with APIs

Dify offers a "Backend-as-a-Service" API, providing numerous benefits to AI application developers. This approach enables developers to access the powerful capabilities of large language models (LLMs) directly in frontend applications without the complexities of backend architecture and deployment processes.

### Benefits of using Dify API

* Allow frontend apps to securely access LLM capabilities without backend development
* Design applications visually with real-time updates across all clients
* Well-encapsulated original LLM APIs
* Effortlessly switch between LLM providers and centrally manage API keys
* Operate applications visually, including log analysis, annotation, and user activity observation
* Continuously provide more tools, plugins, and knowledge

### How to use

Choose an application, and find the API Access in the left-side navigation of the Apps section. On this page, you can view the API documentation provided by Dify and manage credentials for accessing the API.

![API document](../../.gitbook/assets/guides\application-publishing\launch-your-webapp-quickly/API Access.png)

You can create multiple access credentials for an application to deliver to different users or developers. This means that API users can use the AI capabilities provided by the application developer, but the underlying Prompt engineering, knowledge, and tool capabilities are encapsulated.

{% hint style="warning" %}
In best practices, API keys should be called through the backend, rather than being directly exposed in plaintext within frontend code or requests. This helps prevent your application from being abused or attacked.
{% endhint %}

For example, if you're a developer in a consulting company, you can offer AI capabilities based on the company's private database to end-users or developers, without exposing your data and AI logic design. This ensures a secure and sustainable service delivery that meets business objectives.

### Text-generation application

These applications are used to generate high-quality text, such as articles, summaries, translations, etc., by calling the completion-messages API and sending user input to obtain generated text results. The model parameters and prompt templates used for generating text depend on the developer's settings in the Dify Prompt Arrangement page.

You can find the API documentation and example requests for this application in **Applications -> Access API**.

For example, here is a sample call an API for text generation:

{% tabs %}
{% tab title="cURL" %}
```
curl --location --request POST 'https://api.dify.ai/v1/completion-messages' \
--header 'Authorization: Bearer ENTER-YOUR-SECRET-KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "response_mode": "streaming",
    "user": "abc-123"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
import requests
import json

url = "https://api.dify.ai/v1/completion-messages"

headers = {
    'Authorization': 'Bearer ENTER-YOUR-SECRET-KEY',
    'Content-Type': 'application/json',
}

data = {
    "inputs": {"text": 'Hello, how are you?'},
    "response_mode": "streaming",
    "user": "abc-123"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)
```
{% endtab %}
{% endtabs %}

### Conversational Applications

Conversational applications facilitate ongoing dialogue with users through a question-and-answer format. To initiate a conversation, you will call the `chat-messages` API. A `conversation_id` is generated for each session and must be included in subsequent API calls to maintain the conversation flow. 

#### Key Considerations for `conversation_id`:

- **Generating the `conversation_id`:** When starting a new conversation, leave the `conversation_id` field empty. The system will generate and return a new `conversation_id`, which you will use in future interactions to continue the dialogue.
- **Handling `conversation_id` in Existing Sessions:** Once a `conversation_id` is generated, future calls to the API should include this `conversation_id` to ensure the conversation continuity with the Dify bot. When a previous `conversation_id` is passed, any new `inputs` will be ignored. Only the `query` is processed for the ongoing conversation.
- **Managing Dynamic Variables:** If there is a need to modify logic or variables during the session, you can use conversation variables (session-specific variables) to adjust the bot's behavior or responses.

You can access the API documentation and example requests for this application in **Applications -> Access API**.

Here is an example of calling the `chat-messages` API:

{% tabs %}
{% tab title="cURL" %}
```
curl --location --request POST 'https://api.dify.ai/v1/chat-messages' \
--header 'Authorization: Bearer ENTER-YOUR-SECRET-KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "query": "eh",
    "response_mode": "streaming",
    "conversation_id": "1c7e55fb-1ba2-4e10-81b5-30addcea2276",
    "user": "abc-123"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
import requests
import json

url = 'https://api.dify.ai/v1/chat-messages'
headers = {
    'Authorization': 'Bearer ENTER-YOUR-SECRET-KEY',
    'Content-Type': 'application/json',
}
data = {
    "inputs": {},
    "query": "eh",
    "response_mode": "streaming",
    "conversation_id": "1c7e55fb-1ba2-4e10-81b5-30addcea2276",
    "user": "abc-123"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text())
```
{% endtab %}
{% endtabs %}
