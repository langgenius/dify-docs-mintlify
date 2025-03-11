# HTTP Request

### Definition

Allows sending server requests via the HTTP protocol, suitable for scenarios such as retrieving external data, webhooks, generating images, and downloading files. It enables you to send customized HTTP requests to specified web addresses, achieving interconnectivity with various external services.

This node supports common HTTP request methods:

* **GET**: Used to request the server to send a specific resource.
* **POST**: Used to submit data to the server, typically for submitting forms or uploading files.
* **HEAD**: Similar to GET requests, but the server only returns the response headers without the resource body.
* **PATCH**: Used to apply partial modifications to a resource.
* **PUT**: Used to upload resources to the server, typically for updating an existing resource or creating a new one.
* **DELETE**: Used to request the server to delete a specified resource.

You can configure various aspects of the HTTP request, including URL, request headers, query parameters, request body content, and authentication information.

![HTTP Request Configuration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/07c5e952eb4c9d6a32d0b7c2d855d4a5.png)

***

### Scenarios

* **Send Application Interaction Content to a Specific Server**

One practical feature of this node is the ability to dynamically insert variables into different parts of the request based on the scenario. For example, when handling customer feedback requests, you can embed variables such as username or customer ID, feedback content, etc., into the request to customize automated reply messages or fetch specific customer information and send related resources to a designated server.

![Customer Feedback Classification](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/090975269f8998f906c5636dde8d9540.png)

The return values of an HTTP request include the response body, status code, response headers, and files. Notably, if the response contains a file, this node can automatically save the file for use in subsequent steps of the workflow. This design not only improves processing efficiency but also makes handling responses with files straightforward and direct.

* **Send File**

You can use an HTTP PUT request to send files from the application to other API services. In the request body, you can select the file variable within the `binary`. This method is commonly used in scenarios such as file transfer, document storage, or media processing.

Example: Suppose you are developing a document management application and need to send a user-uploaded PDF file to a third-party service. You can use an HTTP request node to pass the file variable.

Here is a configuration example:

![http-node-send-file](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/1f2e33cf7bed33096b5aee145006193d.png)

### Advanced Features

**Retry on Failure**

For some exceptions that occur in the node, it is usually sufficient to retry the node again. When the error retry function is enabled, the node will automatically retry according to the preset strategy when an error occurs. You can adjust the maximum number of retries and the interval between each retry to set the retry strategy.

- The maximum number of retries is 10
- The maximum retry interval is 5000 ms

![](https://assets-docs.dify.ai/2024/12/2e7c6080c0875e31a074c2a9a4543797.png)

**Error Handling**

When processing information, HTTP nodes may encounter exceptional situations such as network request timeouts or request limits. Application developers can follow these steps to configure fail branches, enabling contingency plans when nodes encounter exceptions and avoiding workflow interruptions.

1. Enable "Error Handling" in the HTTP node
2. Select and configure an error handling strategy

For more information about exception handling approaches, please refer to [Error Handling](https://docs.dify.ai/zh-hans/guides/workflow/error-handling).

![](https://assets-docs.dify.ai/2024/12/91daa86d9770390ab2a41d6d0b6ed1e7.png)