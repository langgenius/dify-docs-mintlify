# Node

Reverse Node Request refers to the plugin's ability to access certain nodes within Dify's Chatflow/Workflow applications.

The `ParameterExtractor` and `QuestionClassifier` nodes in `Workflow` encapsulate complex Prompt and code logic that can accomplish many tasks that are difficult to solve with hard coding through LLM. Plugins can request these two nodes.

### **Request Parameter Extractor Node**

**Entry**:

```python
self.session.workflow_node.parameter_extractor
```

**Endpoint**:

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

Where `parameters` is the list of parameters to extract, `model` follows the `LLMModelConfig` specification, `query` is the source text for parameter extraction, `instruction` contains additional instructions for the LLM, and `NodeResponse` structure can be referenced in the documentation.

#### **Example**

If you want to extract a person's name from a conversation, refer to this code:

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

### **Request Question Classifier Node**

**Entry**:

```python
self.session.workflow_node.question_classifier
```

**Endpoint**:

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

This endpoint's parameters are consistent with `ParameterExtractor`, and the final result is stored in `NodeResponse.outputs['class_name']`.
