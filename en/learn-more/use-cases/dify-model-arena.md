# How to Experience a “Model Arena” in Dify? Example: DeepSeek R1 vs o1

## Overview

Dify’s **[“Multiple Model Debugging”](/en/guides/application-orchestrate/multiple-llms-debugging.md)** feature in Chatbot applications allows you to observe how different large language models respond to the same question. This guide uses the example of **DeepSeek R1 vs o1** to demonstrate how to intuitively compare various models’ responses within Dify.

![](https://assets-docs.dify.ai/2025/02/dd2a54e05cf5bfa252ac980ec478e3d5.png)

## Prerequisites

- Dify.AI (Cloud or Community Edition)
- DeepSeek R1 API
- OpenAI o1 API

## Quick Start

### 1. Configure LLM API Keys

Before testing, click **“Profile → Model Provider”** (top-right corner) and follow the prompts to manually add the API keys for multiple models. For more details, please check [here](https://docs.dify.ai/guides/model-configuration)

### 2. Create an Application

Create a **Chatbot** application, specifying a name and description to complete the setup.

![](https://assets-docs.dify.ai/2025/02/7246807cbd0776564b76e1ef37dcbd4d.png)

### 3. Select the Models

Click the **Model** selection button in the top-right corner of the application screen. Choose the `o1` model, then select **Debug as Multiple Models”** and add the `deepseek-reasoner` model.

![](https://assets-docs.dify.ai/2025/02/61d8ba00a8a89052ac7a5a9d8fb54f58.png)

### 4. Compare Results

Enter a question in the chat window. You can now view the responses from different models side by side for the same prompt.

![](https://assets-docs.dify.ai/2025/02/03ac1c1da6705d76b01f5867a1e24e32.gif)

For more information, or if you encounter any issues, see [Multiple Model Debugging](/en/guides/application-orchestrate/multiple-llms-debugging.md).
