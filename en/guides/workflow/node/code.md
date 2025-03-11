# Code Execution

## Table of Contents

* [Introduction](code.md#introduction)
* [Usage Scenarios](code.md#usage-scenarios)
* [Local Deployment](code.md#local-deployment)
* [Security Policies](code.md#security-policies)

## Introduction

The code node supports running Python/NodeJS code to perform data transformations within a workflow. It can simplify your workflow and is suitable for scenarios such as arithmetic operations, JSON transformations, text processing, and more.

This node significantly enhances the flexibility for developers, allowing them to embed custom Python or JavaScript scripts within the workflow and manipulate variables in ways that preset nodes cannot achieve. Through configuration options, you can specify the required input and output variables and write the corresponding execution code:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/9969aa1bc1912aebe366f5d8f5dde296.png)

## Configuration

If you need to use variables from other nodes in the code node, you must define the variable names in the `input variables` and reference these variables. You can refer to [Variable References](../key-concept.md#variables).

## Usage Scenarios

Using the code node, you can perform the following common operations:

### Structured Data Processing

In workflows, you often have to deal with unstructured data processing, such as parsing, extracting, and transforming JSON strings. A typical example is data processing from an HTTP node. In common API return structures, data may be nested within multiple layers of JSON objects, and you need to extract certain fields. The code node can help you perform these operations. Here is a simple example that extracts the `data.name` field from a JSON string returned by an HTTP node:

```python
def main(http_response: str) -> str:
    import json
    data = json.loads(http_response)
    return {
        # Note to declare 'result' in the output variables
        'result': data['data']['name'] 
    }
```

### Mathematical Calculations

When you need to perform complex mathematical calculations in a workflow, you can also use the code node. For example, calculating a complex mathematical formula or performing some statistical analysis on data. Here is a simple example that calculates the variance of an array:

```python
def main(x: list) -> float:
    return {
        # Note to declare 'result' in the output variables
        'result': sum([(i - sum(x) / len(x)) ** 2 for i in x]) / len(x)
    }
```

### Data Concatenation

Sometimes, you may need to concatenate multiple data sources, such as multiple knowledge retrievals, data searches, API calls, etc. The code node can help you integrate these data sources together. Here is a simple example that merges data from two knowledge bases:

```python
def main(knowledge1: list, knowledge2: list) -> list:
    return {
        # Note to declare 'result' in the output variables
        'result': knowledge1 + knowledge2
    }
```

## Local Deployment

If you are a local deployment user, you need to start a sandbox service to ensure that malicious code is not executed. This service requires the use of Docker. You can find specific information about the sandbox service [here](https://github.com/langgenius/dify/tree/main/docker/docker-compose.middleware.yaml). You can also start the service directly via `docker-compose`:

```bash
docker-compose -f docker-compose.middleware.yaml up -d
```

## Security Policies

Both Python and JavaScript execution environments are strictly isolated (sandboxed) to ensure security. This means that developers cannot use functions that consume large amounts of system resources or may pose security risks, such as direct file system access, making network requests, or executing operating system-level commands. These limitations ensure the safe execution of the code while avoiding excessive consumption of system resources.

### Advanced Features

**Retry on Failure**

For some exceptions that occur in the node, it is usually sufficient to retry the node again. When the error retry function is enabled, the node will automatically retry according to the preset strategy when an error occurs. You can adjust the maximum number of retries and the interval between each retry to set the retry strategy.

- The maximum number of retries is 10
- The maximum retry interval is 5000 ms

![](https://assets-docs.dify.ai/2024/12/9fdd5525a91dc925b79b89272893becf.png)

**Error Handling**

When processing information, code nodes may encounter code execution exceptions. Developers can follow these steps to configure fail branches, enabling contingency plans when nodes encounter exceptions, thus avoiding workflow interruptions.

1. Enable "Error Handling" in the code node
2. Select and configure an error handling strategy

![Code Error handling](https://assets-docs.dify.ai/2024/12/58f392734ce44b22cd8c160faf28cd14.png)

For more information about exception handling approaches, please refer to [Error Handling](https://docs.dify.ai/zh-hans/guides/workflow/error-handling).

### FAQ

**Why can't I save the code it in the code node?**

Please check if the code contains potentially dangerous behaviors. For example:

```python
def main() -> dict:
    return {
        "result": open("/etc/passwd").read(),
    }
```

This code snippet has the following issues:

* **Unauthorized file access:** The code attempts to read the "/etc/passwd" file, which is a critical system file in Unix/Linux systems that stores user account information.
* **Sensitive information disclosure:** The "/etc/passwd" file contains important information about system users, such as usernames, user IDs, group IDs, home directory paths, etc. Direct access could lead to information leakage.

Dangerous code will be automatically blocked by Cloudflare WAF. You can check if it's been blocked by looking at the "Network" tab in your browser's "Web Developer Tools".

![Cloudflare WAF](https://assets-docs.dify.ai/2024/12/ad4dc065c4c567c150ab7fa7bfd123a3.png)

