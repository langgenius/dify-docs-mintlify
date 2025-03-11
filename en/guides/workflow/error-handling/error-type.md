# Error Type

This article summarizes the potential exceptions and corresponding error types that may occur in different types of nodes.

### General Error

*   **System error**

    Typically caused by system issues such as a disabled sandbox service or network connection problems.
*   **Operational Error**

    Occurs when developers are unable to configure or run the node correctly.

### Code Node

[Code](../node/code.md) nodes support running Python and JavaScript code for data transformation in workflows or chat flows. Here are 4 common runtime errors:

1.  **Code Node Error (CodeNodeError)**

    This error occurs due to exceptions in developer-written code, such as: missing variables, calculation logic errors, or treating string array inputs as string variables. You can locate the issue using the error message and exact line number.

![Code Error](https://assets-docs.dify.ai/2024/12/c86b11af7f92368180ea1bac38d77083.png)

2.  **Sandbox Network Issues (System Error)**

    This error commonly occurs when there are network traffic or connection issues, such as when the sandbox service isn't running or proxy services have interrupted the network. You can resolve this through the following steps:

    1. Check network service quality
    2. Start the sandbox service
    3. Verify proxy settings

![Sandbox network issues](https://assets-docs.dify.ai/2024/12/d95007adf67c4f232e46ec455c348e2c.PNG)

3.  **Depth Limit Error (DepthLimitError)**

    The current node's default configuration only supports up to 5 levels of nested structures. An error will occur if it exceeds 5 levels.

![<strong>OutputValidationError</strong>](https://assets-docs.dify.ai/2024/12/5649d52a6e80ddd4180b336266701f7b.png)

4.  **Output Validation Error (OutputValidationError)**

    An error occurs when the actual output variable type doesn't match the selected output variable type. Developers need to change the selected output variable type to avoid this issue.

![](https://assets-docs.dify.ai/2024/12/ab8cae01a590b037017dfe9ea4dbbb8b.png)

### LLM Node

The [LLM](../node/llm.md) node is a core component of Chatflow and Workflow, utilizing LLM' capabilities in dialogue, generation, classification, and processing to complete various tasks based on user input instructions.

Here are 6 common runtime errors:

1.  **Variable Not Found Error (VariableNotFoundError)**

    This error occurs when the LLM cannot find system prompts or variables set in the context. Application developers can resolve this by replacing the problematic variables.

![](https://assets-docs.dify.ai/2024/12/f20c5fbde345144de6183374ab277662.png)

2.  **Invalid Context Structure Error (InvalidContextStructureError)**

    An error occurs when the context within the LLM node receives an invalid data structure (such as `array[object]`).

    > Context only supports string (String) data structures.

![<strong>InvalidContextStructureError</strong>](https://assets-docs.dify.ai/2024/12/f20c5fbde345144de6183374ab277662.png)

3.  **Invalid Variable Type Error (InvalidVariableTypeError)**

    This error appears when the system prompt type is not in the standard Prompt text format or Jinja syntax format.
4.  **Model Not Exist Error (ModelNotExistError)**

    Each LLM node requires a configured model. This error occurs when no model is selected.
5.  **LLM Authorization Required Error (LLMModeRequiredError)**

    The model selected in the LLM node has no configured API Key. You can refer to the documentation for model authorization.
6.  **No Prompt Found Error (NoPromptFoundError)**

    An error occurs when the LLM node's prompt is empty, as prompts cannot be blank.

![](https://assets-docs.dify.ai/2024/12/9882f7a5ee544508ba11b51fb469a911.png)

### HTTP

[HTTP](../node/http-request.md) nodes allow seamless integration with external services through customizable requests for data retrieval, webhook triggering, image generation, or file downloads via HTTP requests. Here are 5 common errors for this node:

1.  **Authorization Configuration Error (AuthorizationConfigError)**

    This error occurs when authentication information (Auth) is not configured.
2. **File Fetch Error (FileFetchError)** This error appears when file variables cannot be retrieved.
3.  **Invalid HTTP Method Error (InvalidHttpMethodError)**

    An error occurs when the request header method is not one of the following: GET, HEAD, POST, PUT, PATCH, or DELETE.
4.  **Response Size Error (ResponseSizeError)**

    HTTP response size is limited to 10MB. An error occurs if the response exceeds this limit.
5. **HTTP Response Code Error (HTTPResponseCodeError)** An error occurs when the request response returns a code that doesn't start with 2 (such as 200, 201). If exception handling is enabled, errors will occur for status codes 400, 404, and 500; otherwise, these won't trigger errors.

### Tool

The following 3 errors commonly occur during runtime:

1.  **Tool Execution Error (ToolNodeError)**

    An error that occurs during tool execution itself, such as when reaching the target API's request limit.



    ![](https://assets-docs.dify.ai/2024/12/84af0831b7cb23e64159dfbba80e9b28.jpg)
2.  **Tool Parameter Error (ToolParameterError)**

    An error occurs when the configured tool node parameters are invalid, such as passing parameters that don't match the tool node's defined parameters.
3.  **Tool File Processing Error (ToolFileError)**

    An error occurs when the tool node cannot find the required files.





