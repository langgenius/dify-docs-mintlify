# Workflow

### Basic Introduction

Workflows reduce system complexity by breaking down complex tasks into smaller steps (nodes), reducing reliance on prompt engineering and model inference capabilities, and enhancing the performance of LLM applications for complex tasks. This also improves the system's interpretability, stability, and fault tolerance.

Dify workflows are divided into two types:

* **Chatflow**: Designed for conversational scenarios, including customer service, semantic search, and other conversational applications that require multi-step logic in response construction.
* **Workflow**: Geared towards automation and batch processing scenarios, suitable for high-quality translation, data analysis, content generation, email automation, and more.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/65e9ed3fb88e03f631b3862acc2479e4.png)

To address the complexity of user intent recognition in natural language input, Chatflow provides question understanding nodes. Compared to Workflow, it adds support for Chatbot features such as conversation history (Memory), annotated replies, and Answer nodes.

To handle complex business logic in automation and batch processing scenarios, Workflow offers a variety of logic nodes, such as code nodes, IF/ELSE nodes, template transformation, iteration nodes, and more. Additionally, it provides capabilities for timed and event-triggered actions, facilitating the construction of automated processes.

### Common Use Cases

* Customer Service

By integrating LLM into your customer service system, you can automate responses to common questions, reducing the workload of your support team. LLM can understand the context and intent of customer queries and generate helpful and accurate answers in real-time.

* Content Generation

Whether you need to create blog posts, product descriptions, or marketing materials, LLM can assist by generating high-quality content. Simply provide an outline or topic, and LLM will use its extensive knowledge base to produce engaging, informative, and well-structured content.

* Task Automation

LLM can be integrated with various task management systems like Trello, Slack, and Lark to automate project and task management. Using natural language processing, LLM can understand and interpret user input, create tasks, update statuses, and assign priorities without manual intervention.

* Data Analysis and Reporting

LLM can analyze large datasets and generate reports or summaries. By providing relevant information to LLM, it can identify trends, patterns, and insights, transforming raw data into actionable intelligence. This is particularly valuable for businesses looking to make data-driven decisions.

* Email Automation

LLM can be used to draft emails, social media updates, and other forms of communication. By providing a brief outline or key points, LLM can generate well-structured, coherent, and contextually relevant messages. This saves significant time and ensures your responses are clear and professional.

### How to Get Started

* Start by building a workflow from scratch or use system templates to help you get started.
* Get familiar with basic operations, including creating nodes on the canvas, connecting and configuring nodes, debugging workflows, and viewing run history.
* Save and publish a workflow.
* Run the published application or call the workflow through an API.
