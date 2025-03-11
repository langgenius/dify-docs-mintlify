# ノード

リバースノードリクエストとは、プラグインがDifyのChatflow/Workflowアプリケーション内の特定のノードにアクセスする能力を指します。

`Workflow`の`ParameterExtractor`と`QuestionClassifier`ノードは、複雑なPromptとコードロジックをカプセル化しており、LLMを通じたハードコーディングでは解決が困難な多くのタスクを実行できます。プラグインはこれら2つのノードをリクエストすることができます。

### **パラメータ抽出ノードのリクエスト**

#### **エントリー**

```python
self.session.workflow_node.parameter_extractor
```

#### **エンドポイント**

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

ここで、`parameters`は抽出するパラメータのリスト、`model`は`LLMModelConfig`仕様に従い、`query`はパラメータ抽出のソーステキスト、`instruction`はLLMへの追加指示を含み、`NodeResponse`構造はドキュメントで参照できます。

#### **例**

会話から人の名前を抽出したい場合は、以下のコードを参照してください：

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

### **質問分類ノードのリクエスト**

#### **エントリー**

```python
self.session.workflow_node.question_classifier
```

#### **エンドポイント**

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

このエンドポイントのパラメータは`ParameterExtractor`と一致しており、最終結果は`NodeResponse.outputs['class_name']`に格納されます。
