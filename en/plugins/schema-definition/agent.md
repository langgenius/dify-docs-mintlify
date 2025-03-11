# Agent

**Agent Strategy Overview**

An Agent Strategy is an extensible template that defines standard input content and output formats. By developing specific Agent strategy interface functionality, you can implement various Agent strategies such as CoT (Chain of Thought) / ToT (Tree of Thought) / GoT (Graph of Thought) / BoT (Backbone of Thought), and achieve complex strategies like [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/).

### **Adding Fields in Manifest**

To add Agent strategies in a plugin, add the `plugins.agent_strategies` field in the manifest.yaml file and define the Agent provider. Example code:

```yaml
version: 0.0.2
type: plugin
author: "langgenius"
name: "agent"
plugins:
  agent_strategies:
    - "provider/agent.yaml"
```

Some unrelated fields in the manifest file are omitted. For detailed Manifest format, refer to [Manifest](manifest.md).

### **Defining the Agent Provider**

Create an agent.yaml file with basic Agent provider information:

```yaml
identity:
  author: langgenius
  name: agent
  label:
    en_US: Agent
    zh_Hans: Agent
    pt_BR: Agent
  description:
    en_US: Agent
    zh_Hans: Agent
    pt_BR: Agent
  icon: icon.svg
strategies:
  - strategies/function_calling.yaml
```

### **Defining and Implementing Agent Strategy**

#### **Definition**

Create a function\_calling.yaml file to define the Agent strategy code:

```yaml
identity:
  name: function_calling
  author: Dify
  label:
    en_US: FunctionCalling
    zh_Hans: FunctionCalling
    pt_BR: FunctionCalling
description:
  en_US: Function Calling is a basic strategy for agent, model will use the tools provided to perform the task.
parameters:
  - name: model
    type: model-selector
    scope: tool-call&llm
    required: true
    label:
      en_US: Model
  - name: tools
    type: array[tools]
    required: true
    label:
      en_US: Tools list
  - name: query
    type: string
    required: true
    label:
      en_US: Query
  - name: max_iterations
    type: number
    required: false
    default: 5
    label:
      en_US: Max Iterations
    max: 50
    min: 1
extra:
  python:
    source: strategies/function_calling.py
```

The code format is similar to the [Tool](tool.md) standard format and defines four parameters: `model`, `tools`, `query`, and `max_iterations` to implement the most basic Agent strategy. This means that users can:

* Select which model to use
* Choose which tools to utilize
* Configure the maximum number of iterations
* Input a query to start executing the Agent

All these parameters work together to define how the Agent will process tasks and interact with the selected tools and models.

#### Functional Implementation Coding

**Retrieving Parameters**

Based on the four parameters defined earlier, the model type parameter is model-selector, and the tool type parameter is a special array\[tools]. The retrieved parameters can be converted using the SDK’s built-in AgentModelConfig and list\[ToolEntity].

```python
from dify_plugin.interfaces.agent import AgentModelConfig, AgentStrategy, ToolEntity

class FunctionCallingParams(BaseModel):
    query: str
    model: AgentModelConfig
    tools: list[ToolEntity] | None
    maximum_iterations: int = 3
    
 class FunctionCallingAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        """
        Run FunctionCall agent application
        """
        fc_params = FunctionCallingParams(**parameters)
```

**Invoking the Model**

Invoking a specific model is an essential capability of the Agent plugin. Use the session.model.invoke() function from the SDK to call the model. The required input parameters can be obtained from the model.

Example Method Signature for Invoking the Model:

```python
def invoke(
        self,
        model_config: LLMModelConfig,
        prompt_messages: list[PromptMessage],
        tools: list[PromptMessageTool] | None = None,
        stop: list[str] | None = None,
        stream: bool = True,
    ) -> Generator[LLMResultChunk, None, None] | LLMResult:
```

You need to pass the model information (model\_config), prompt information (prompt\_messages), and tool information (tools). The prompt\_messages parameter can be referenced using the example code below, while tool\_messages require certain transformations.

Refer to the example code for using invoke model:

```python
from collections.abc import Generator
from typing import Any

from pydantic import BaseModel

from dify_plugin.entities.agent import AgentInvokeMessage
from dify_plugin.entities.model.llm import LLMModelConfig
from dify_plugin.entities.model.message import (
    PromptMessageTool,
    SystemPromptMessage,
    UserPromptMessage,
)
from dify_plugin.entities.tool import ToolParameter
from dify_plugin.interfaces.agent import AgentModelConfig, AgentStrategy, ToolEntity

class FunctionCallingParams(BaseModel):
    query: str
    instruction: str | None
    model: AgentModelConfig
    tools: list[ToolEntity] | None
    maximum_iterations: int = 3

class FunctionCallingAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        """
        Run FunctionCall agent application
        """
        # init params
        fc_params = FunctionCallingParams(**parameters)
        query = fc_params.query
        model = fc_params.model
        stop = fc_params.model.completion_params.get("stop", []) if fc_params.model.completion_params else []
        prompt_messages = [
            SystemPromptMessage(content="your system prompt message"),
            UserPromptMessage(content=query),
        ]
        tools = fc_params.tools
        prompt_messages_tools = self._init_prompt_tools(tools)

        # invoke llm
        chunks = self.session.model.llm.invoke(
            model_config=LLMModelConfig(**model.model_dump(mode="json")),
            prompt_messages=prompt_messages,
            stream=True,
            stop=stop,
            tools=prompt_messages_tools,
        )

    def _init_prompt_tools(self, tools: list[ToolEntity] | None) -> list[PromptMessageTool]:
        """
        Init tools
        """

        prompt_messages_tools = []
        for tool in tools or []:
            try:
                prompt_tool = self._convert_tool_to_prompt_message_tool(tool)
            except Exception:
                # api tool may be deleted
                continue

            # save prompt tool
            prompt_messages_tools.append(prompt_tool)

        return prompt_messages_tools

    def _convert_tool_to_prompt_message_tool(self, tool: ToolEntity) -> PromptMessageTool:
        """
        convert tool to prompt message tool
        """
        message_tool = PromptMessageTool(
            name=tool.identity.name,
            description=tool.description.llm if tool.description else "",
            parameters={
                "type": "object",
                "properties": {},
                "required": [],
            },
        )

        parameters = tool.parameters
        for parameter in parameters:
            if parameter.form != ToolParameter.ToolParameterForm.LLM:
                continue

            parameter_type = parameter.type
            if parameter.type in {
                ToolParameter.ToolParameterType.FILE,
                ToolParameter.ToolParameterType.FILES,
            }:
                continue
            enum = []
            if parameter.type == ToolParameter.ToolParameterType.SELECT:
                enum = [option.value for option in parameter.options] if parameter.options else []

            message_tool.parameters["properties"][parameter.name] = {
                "type": parameter_type,
                "description": parameter.llm_description or "",
            }

            if len(enum) > 0:
                message_tool.parameters["properties"][parameter.name]["enum"] = enum

            if parameter.required:
                message_tool.parameters["required"].append(parameter.name)

        return message_tool

```

**Invoking Tools**

Invoking tools is also a crucial capability of the Agent plugin. Use self.session.tool.invoke() to call a tool.

Example Method Signature for Invoking a Tool:

```python
def invoke(
        self,
        provider_type: ToolProviderType,
        provider: str,
        tool_name: str,
        parameters: dict[str, Any],
    ) -> Generator[ToolInvokeMessage, None, None]
```

Required parameters include provider\_type, provider, tool\_name, and parameters. Typically, tool\_name and parameters are generated by the LLM during Function Calling.

Example Code for Using invoke tool:

```python
from dify_plugin.entities.tool import ToolProviderType

class FunctionCallingAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        """
        Run FunctionCall agent application
        """
        fc_params = FunctionCallingParams(**parameters)
        
        # tool_call_name and tool_call_args parameter is obtained from the output of LLM
        tool_instances = {tool.identity.name: tool for tool in fc_params.tools} if fc_params.tools else {}
        tool_instance = tool_instances[tool_call_name]
        tool_invoke_responses = self.session.tool.invoke(
            provider_type=ToolProviderType.BUILT_IN,
            provider=tool_instance.identity.provider,
            tool_name=tool_instance.identity.name,
            # add the default value
            parameters={**tool_instance.runtime_parameters, **tool_call_args},
        )
```

The output of the self.session.tool.invoke() function is a Generator, which requires stream parsing.

Refer to the following function for parsing:

```python
import json
from collections.abc import Generator
from typing import cast

from dify_plugin.entities.agent import AgentInvokeMessage
from dify_plugin.entities.tool import ToolInvokeMessage

def parse_invoke_response(tool_invoke_responses: Generator[AgentInvokeMessage]) -> str:
    result = ""
    for response in tool_invoke_responses:
        if response.type == ToolInvokeMessage.MessageType.TEXT:
            result += cast(ToolInvokeMessage.TextMessage, response.message).text
        elif response.type == ToolInvokeMessage.MessageType.LINK:
            result += (
                f"result link: {cast(ToolInvokeMessage.TextMessage, response.message).text}."
                + " please tell user to check it."
            )
        elif response.type in {
            ToolInvokeMessage.MessageType.IMAGE_LINK,
            ToolInvokeMessage.MessageType.IMAGE,
        }:
            result += (
                "image has been created and sent to user already, "
                + "you do not need to create it, just tell the user to check it now."
            )
        elif response.type == ToolInvokeMessage.MessageType.JSON:
            text = json.dumps(cast(ToolInvokeMessage.JsonMessage, response.message).json_object, ensure_ascii=False)
            result += f"tool response: {text}."
        else:
            result += f"tool response: {response.message!r}."
    return result'
```

**Log**

To view the Agent's thinking process, besides normal message returns, you can use specialized interfaces to display the entire Agent thought process in a tree structure.

**Creating Logs**

* This interface creates and returns an `AgentLogMessage`, which represents a node in the log tree.
* If a parent is passed in, it indicates this node has a parent node.
* The default status is "Success". However, if you want to better display the task execution process, you can first set the status to "start" to show a "in progress" log, then update the log status to "Success" after the task is completed. This way, users can clearly see the entire process from start to finish.
* The label will be used as the log title shown to users.

```python
def create_log_message(
    self,
    label: str,
    data: Mapping[str, Any],
    status: AgentInvokeMessage.LogMessage.LogStatus = AgentInvokeMessage.LogMessage.LogStatus.SUCCESS,
    parent: AgentInvokeMessage | None = None,
) -> AgentInvokeMessage
```

**Completing Logs**

You can use the log completion endpoint to change the status if you previously set "start" as the initial status.

```python
def finish_log_message(
    self,
    log: AgentInvokeMessage,
    status: AgentInvokeMessage.LogMessage.LogStatus = AgentInvokeMessage.LogMessage.LogStatus.SUCCESS,
    error: Optional[str] = None,
) -> AgentInvokeMessage
```

**Example Implementation**

This example demonstrates a simple two-step execution process: first outputting a "Thinking" status log, then completing the actual task processing.

```python
class FunctionCallingAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        thinking_log = self.create_log_message(
            data={"Query": parameters.get("query")},
            label="Thinking",
            status=AgentInvokeMessage.LogMessage.LogStatus.START,
        )

        yield thinking_log

        llm_response = self.session.model.llm.invoke(
            model_config=LLMModelConfig(
                provider="openai",
                model="gpt-4o-mini",
                mode="chat",
                completion_params={},
            ),
            prompt_messages=[
                SystemPromptMessage(content="you are a helpful assistant"),
                UserPromptMessage(content=parameters.get("query")),
            ],
            stream=False,
            tools=[],
        )

        thinking_log = self.finish_log_message(log=thinking_log)
        yield thinking_log
        yield self.create_text_message(text=llm_response.message.content)
```
