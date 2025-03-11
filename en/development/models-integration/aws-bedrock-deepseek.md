# Integrate Models from AWS Bedrock

## Overview

The [AWS Bedrock Marketplace](https://aws.amazon.com/bedrock/marketplace/) is a comprehensive platform for deploying large language models (LLMs). It allows developers to discover, test, and deploy over 100 emerging foundation models (FMs) seamlessly. 

This guide will take the deployment of DeepSeek models as an example to demonstrate how to deploy model on the Bedrock Marketplace platform and integrate it into the Dify platform, helping you quickly build AI applications based on DeepSeek models.

## Prerequisites

- An AWS account with access to [Bedrock](https://aws.amazon.com/bedrock/).
- A [Dify.AI account](https://cloud.dify.ai/).

## Deployment Procedure

### 1. Deploy the DeepSeek Model

#### 1.1 Searching and Selecting the Model

1. Navigate to the **Bedrock Marketplace** and search for **DeepSeek**.
2. Choose a **DeepSeek** model based on your requirements.

![](https://assets-docs.dify.ai/2025/02/9c6e17fc0cf262b2005013bf122251d1.png)

#### 1.2 Initiating Deployment

1. Go to the **Model detail** page and click **Deploy**.
2. Follow the instructions to configure the deployment settings.

> **Note:** Model versions require different compute configurations, affecting costs.

![](https://assets-docs.dify.ai/2025/02/613497e3473d9b6eaa7cb5611decee0c.png)

#### 1.3 Retrieving the Endpoint

Once deployment is complete, navigate to the **Marketplace Deployments** page to find the auto-generated **Endpoint**. This endpoint is equivalent to a **SageMaker endpoint** and will be used for connecting to the Dify platform.

![View Endpoint](https://assets-docs.dify.ai/2025/02/82a1d6406662b83386b86ec511ab20be.png)

### 2. Connecting DeepSeek to the Dify Platform

#### 2.1 Accessing Configuration Settings

1. Log in to the Dify management panel and go to the **Settings** page.

2. On the **Model Provider** page, select **Amazon SageMaker**.

![Add Model](https://assets-docs.dify.ai/2025/02/864fc8476c47b460b67f14152cbbf360.png)

#### 2.2 Configuring SageMaker Settings

Click **Add Model** and fill in the following information:
   
   * **Model Type:** Select **LLM** as the model type
   * **Model Name:** Provide a custom name for your model
   * **SageMaker Endpoint:** Enter the endpoint retrieved from the Bedrock Marketplace

![](https://assets-docs.dify.ai/2025/02/1feaa8d5054933f42da25a8f655b5a9e.png)

### 3. Testing the Model

1. Open Dify and select Create a Blank App.
2. Select either Chatflow or Workflow.
3. Add an LLM node.
4. Verify model responses (see screenshot below for expected responses).

![Model Running](https://assets-docs.dify.ai/2025/02/e7fb06888101662ecb970401fdba63b5.png)

> **Note:** You can also create a **Chatbot** application for additional testing.

## FAQ

### 1. **Endpoint Parameter Not Visible After Deployment**

Ensure that the compute instance is configured correctly and that AWS permissions are properly set. If the issue persists, consider redeploying the model or contacting AWS customer support.
