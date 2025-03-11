# Agent

Agent 策略是一个定义了标准输入内容与输出格式的可扩展模板。通过开发具体 Agent 策略接口的功能代码，你可以实现众多不同的 Agent 策略如 CoT（思维链）/ ToT（思维树）/ GoT（思维图）/ BoT（思维骨架），实现一些诸如 [Sementic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/)  的复杂策略。

### 在 Manifest 内添加字段

在插件中添加 Agent 策略需要在 `manifest.yaml` 文件内新增 `plugins.agent_strategies` 字段，并且也需要定义 Agent 供应商，示例代码如下

```yaml
version: 0.0.2
type: plugin
author: "langgenius"
name: "agent"
plugins:
  agent_strategies:
    - "provider/agent.yaml"
```

此处已省去 `manifest` 文件内部分无关的字段。如需了解 Manifest 的详细格式，请参考 [Manifest](/zh_CN/plugins/schema-definition/manifest) 文档。

### 定义 Agent 供应商

随后，你需要新建 `agent.yaml` 文件并填写基础的 Agent 供应商信息。

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

其主要包含一些描述性质的基础内容，并且指明当前供应商包含哪些策略。在上述示例代码中仅指定了一个最基础的 `function_calling.yaml` 策略文件。

### 定义并实现 Agent 策略

#### 定义

接下来需要定义能够实现 Agent 策略的代码。新建一个 `function_calling.yaml` 文件：

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
  zh_Hans: Function Calling 是一个基本的 Agent 策略，模型将使用提供的工具来执行任务。
  pt_BR: Function Calling is a basic strategy for agent, model will use the tools provided to perform the task.
parameters:
  - name: model
    type: model-selector
    scope: tool-call&llm
    required: true
    label:
      en_US: Model
      zh_Hans: 模型
      pt_BR: Model
  - name: tools
    type: array[tools]
    required: true
    label:
      en_US: Tools list
      zh_Hans: 工具列表
      pt_BR: Tools list
  - name: query
    type: string
    required: true
    label:
      en_US: Query
      zh_Hans: 用户提问
      pt_BR: Query
  - name: max_iterations
    type: number
    required: false
    default: 5
    label:
      en_US: Max Iterations
      zh_Hans: 最大迭代次数
      pt_BR: Max Iterations
    max: 50
    min: 1
extra:
  python:
    source: strategies/function_calling.py
```

代码格式类似 [`Tool` 标准格式](tool.md)，定义了 `model` `tools` `query` `max_iterations` 等一共四个参数，以便于实现最基础的 Agent 策略。该代码的含义是可以允许用户选择模型和需要使用的工具，配置最大迭代次数并最终传入一个 query 后开始执行 Agent。

#### 编写功能实现代码

**获取参数**

根据上文定义的四个参数，其中 model 类型参数为`model-selector`，tool 类型参数为特殊的 `array[tools]。`在参数中获取到的形式可以通过 SDK 中内置的 `AgentModelConfig` 和 `list[ToolEntity]`进行转换。

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

**调用模型**

调用指定模型是 Agent 插件中必不可少的能力。通过 SDK 中的 `session.model.invoke()` 函数调用模型。可以从 model 中获取所需的传入参数。

invoke model 的方法签名示例代码：

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

需要传入模型信息 `model_config`，prompt 信息 `prompt_messages` 和工具信息 `tools`。

其中`prompt_messages`参数可以参考以下示例代码调用；而`tool_messages`则需要进行一定的转换。

请参考 invoke model 使用方法的示例代码：

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

**调用工具**

调用工具同样是 Agent 插件必不可少的能力。可以通过`self.session.tool.invoke()`进行调用。invoke tool 的方法签名示例代码：

```python
def invoke(
        self,
        provider_type: ToolProviderType,
        provider: str,
        tool_name: str,
        parameters: dict[str, Any],
    ) -> Generator[ToolInvokeMessage, None, None]
```

必须的参数有 `provider_type`, `provider`, `tool_name`, `parameters`。其中 `tool_name` 和`parameters`在 Function Calling 中往往都由 LLM 生成。使用 invoke tool 的示例代码：

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

`self.session.tool.invoke()`函数的输出是一个 Generator，代表着同样需要进行流式解析。

解析方法请参考以下函数：

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
    return result
```

#### Log

如果你希望看到 Agent 思考的过程，除了通过查看正常返回的消息以外，还可以使用专门的接口实现以树状结构展示整个 Agent 的思考过程。

**创建日志**

* 该接口创建并返回一个 `AgentLogMessage`，该 Message 表示日志中树的一个节点。
* 如果有传入 parent 则表示该节点具备父节点。
* 状态默认为"Success"（成功）。但如果你想要更好地展示任务执行过程，可以先设置状态为"start"来显示"正在执行"的日志，等任务完成后再将该日志的状态更新为"Success"。这样用户就能清楚地看到任务从开始到完成的整个过程。
* label 将用于最终给用户展示日志标题。

```python
    def create_log_message(
        self,
        label: str,
        data: Mapping[str, Any],
        status: AgentInvokeMessage.LogMessage.LogStatus = AgentInvokeMessage.LogMessage.LogStatus.SUCCESS,
        parent: AgentInvokeMessage | None = None,
    ) -> AgentInvokeMessage
```

**完成日志**

如果在前一个步骤选择了 start 状态作为初始状态，可以使用完成日志的接口来更改状态。

```python
    def finish_log_message(
        self,
        log: AgentInvokeMessage,
        status: AgentInvokeMessage.LogMessage.LogStatus = AgentInvokeMessage.LogMessage.LogStatus.SUCCESS,
        error: Optional[str] = None,
    ) -> AgentInvokeMessage
```

**实例**

这个示例展示了一个简单的两步执行过程：首先输出一条"正在思考"的状态日志，然后完成实际的任务处理。

```python
class FunctionCallingAgentStrategy(AgentStrategy):
    def _invoke(self, parameters: dict[str, Any]) -> Generator[AgentInvokeMessage]:
        thinking_log = self.create_log_message(
            data={
                "Query": parameters.get("query"),
            },
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

        thinking_log = self.finish_log_message(
            log=thinking_log,
        )

        yield thinking_log

        yield self.create_text_message(text=llm_response.message.content)
```
