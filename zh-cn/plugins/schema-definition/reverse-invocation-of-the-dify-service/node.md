# Node

反向调用 Node 指的是插件能够访问 Dify 中 Chatflow/Workflow 应用内部分节点的能力。

`Workflow` 中的 `ParameterExtractor（参数提取器）`与 `QuestionClassifier（问题分类）`节点封装了较为复杂的 Prompt 与代码逻辑，可以通过 LLM 来完成许多硬编码难以解决的任务。插件能够调用这两个节点。

### 调用参数提取器节点;

#### **入口**

```python
    self.session.workflow_node.parameter_extractor
```

#### **接口**

```python
    def invoke(
        self,
        parameters: list[ParameterConfig],
        model: ModelConfig,
        query: str,
        instruction: str = "",
    ) -> NodeResponse
        pass
```

其中 `parameters` 是需要提取出的参数的列表，`model` 符合 `LLMModelConfig` 规范，`query` 为提取参数的源文本，`instruction` 为一些可能额外需要给到 LLM 的指令，`NodeResponse` 的结构请参考该[文档](../general-specifications.md#noderesponse)。

#### **用例**

如果想要提取对话中的某个人名，可以参考以下代码：

```python
from collections.abc import Generator
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin import Tool
from dify_plugin.entities.workflow_node import ModelConfig, ParameterConfig

class ParameterExtractorTool(Tool):
    def _invoke(
        self, tool_parameters: dict
    ) -> Generator[ToolInvokeMessage, None, None]:
        response = self.session.workflow_node.parameter_extractor.invoke(
            parameters=[
                ParameterConfig(
                    name="name",
                    description="name of the person",
                    required=True,
                    type="string",
                )
            ],
            model=ModelConfig(
                provider="langgenius/openai/openai",
                name="gpt-4o-mini",
                completion_params={},
            ),
            query="My name is John Doe",
            instruction="Extract the name of the person",
        )

        yield self.create_text_message(response.outputs["name"])
```

### 调用问题分类节点

#### **入口**

```python
    self.session.workflow_node.question_classifier
```

#### **接口**

```python
    def invoke(
        self,
        classes: list[ClassConfig],
        model: ModelConfig,
        query: str,
        instruction: str = "",
    ) -> NodeResponse:
        pass
```

该接口参数与 `ParameterExtractor` 一致，最终的返回结果储存在 `NodeResponse.outputs['class_name']` 中。\
