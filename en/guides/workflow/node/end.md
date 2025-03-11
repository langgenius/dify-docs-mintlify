# End

### 1 Definition

Define the final output content of a workflow. Every workflow needs at least one end node after complete execution to output the final result.

The end node is a termination point in the process; no further nodes can be added after it. In a workflow application, results are only output when the end node is reached. If there are conditional branches in the process, multiple end nodes need to be defined.

The end node must declare one or more output variables, which can reference any upstream node's output variables.

{% hint style="info" %}
End nodes are not supported within Chatflow.
{% endhint %}

***

### 2 Scenarios

In the following [long story generation workflow](iteration.md#example-2-long-article-iterative-generation-another-scheduling-method), the variable `Output` declared by the end node is the output of the upstream code node. This means the workflow will end after the Code node completes execution and will output the execution result of Code.

![End Node - Long Story Generation Example](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/a103792790447c1725c1da1176334cae.png)

**Single Path Execution Example:**

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/9e43961344d318e09af8d64464d81774.png)

**Multi-Path Execution Example:**

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/3cb3f5fea376265bede0a4ac5bcc1ddc.png)
