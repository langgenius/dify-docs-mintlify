# Tools

The workflow provides a rich selection of tools, categorized into three types:

* **Built-in Tools**: Tools provided by Dify.
* **Custom Tools**: Tools imported or configured via the OpenAPI/Swagger standard format.
* **Workflows**: Workflows that have been published as tools.

## Add and Use the Tool Node

Before using built-in tools, you may need to **authorize** the tools.

If built-in tools do not meet your needs, you can create custom tools in the **Dify menu navigation -- Tools** section.

You can also orchestrate a more complex workflow and publish it as a tool.

![Tool Selection](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/0f0255764a3f459f0b3c708db1cb32c9.png)

![Configuring Google Search Tool to Retrieve External Knowledge](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/c7b52209e7ad4e15ce42b882cf646d1b.png)

Configuring a tool node generally involves two steps:

1. Authorizing the tool/creating a custom tool/publishing a workflow as a tool.
2. Configuring the tool's input and parameters.

For more information on how to create custom tools and configure them, please refer to the [Tool Configuration Guide](https://docs.dify.ai/guides/tools).

### Advanced Features

**Retry on Failure**

For some exceptions that occur in the node, it is usually sufficient to retry the node again. When the error retry function is enabled, the node will automatically retry according to the preset strategy when an error occurs. You can adjust the maximum number of retries and the interval between each retry to set the retry strategy.

- The maximum number of retries is 10
- The maximum retry interval is 5000 ms

![](https://assets-docs.dify.ai/2024/12/34867b2d910d74d2671cd40287200480.png)

**Error Handling**

Tool nodes may encounter errors during information processing that could interrupt the workflow. Developers can follow these steps to configure fail branches, enabling contingency plans when nodes encounter exceptions, avoiding workflow interruptions.

1. Enable "Error Handling" in the tool node
2. Select and configure an error-handling strategy

![](https://assets-docs.dify.ai/2024/12/39dc3b5881d9a5fe35b877971f70d3a6.png)

For more information about exception handling approaches, please refer to [Error Handling](https://docs.dify.ai/guides/workflow/error-handling).

## Publishing Workflow Applications as Tools

Workflow applications can be published as tools and used by nodes in other workflows. For information about creating custom tools and tool configuration, please refer to the [Tool Configuration Guide](https://docs.dify.ai/guides/tools).
