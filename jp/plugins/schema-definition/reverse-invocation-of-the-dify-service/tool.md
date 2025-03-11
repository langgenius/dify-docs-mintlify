# ツール

以下のようなシナリオに遭遇した場合：

* ツールタイププラグインが機能を実装したが、期待を満たしておらずデータの再処理が必要な場合
* タスクがWebクローリングを必要とし、クローリングサービスの選択に柔軟性が必要な場合
* 複数のツールの戻り値を組み合わせる必要があるが、Workflowアプリケーションでの処理が困難な場合

これらの場合、プラグイン内の他の実装済みツールをリクエストする必要があります。これらのツールは、マーケットプレイスのツールプラグイン、自作のWorkflow as Tool、またはカスタムツールである可能性があります。

上記の要件は、プラグインの`self.session.tool`フィールドを使用することで達成できます。

### **インストール済みツールのリクエスト**

プラグインが現在のWorkspaceにインストールされている様々なツール（他のツールタイププラグインを含む）をリクエストすることができます。

**エントリー**：

```python
self.session.tool
```

**エンドポイント**：

```python
def invoke_builtin_tool(
    self, provider: str, tool_name: str, parameters: dict[str, Any]
) -> Generator[ToolInvokeMessage, None, None]:
    pass
```

ここで、`provider`はプラグインIDとツールプロバイダー名を組み合わせたもので、`langgenius/google/google`のような形式です。`tool_name`は具体的なツール名、`parameters`はそのツールに渡すパラメータです。

### **Workflow as Toolのリクエスト**

Workflow as Toolの詳細については、このドキュメントを参照してください。

**エントリー**：

```python
self.session.tool
```

**エンドポイント**：

```python
def invoke_workflow_tool(
    self, provider: str, tool_name: str, parameters: dict[str, Any]
) -> Generator[ToolInvokeMessage, None, None]:
    pass
```

ここで、`provider`はツールのID、`tool_name`はツール作成時に必要となります。

### **カスタムツールのリクエスト**

**エントリー**：

```python
self.session.tool
```

**エンドポイント**：

```python
def invoke_api_tool(
    self, provider: str, tool_name: str, parameters: dict[str, Any]
) -> Generator[ToolInvokeMessage, None, None]:
    pass
```

ここで、`provider`はツールのID、`tool_name`はOpenAPIの`operation_id`です。存在しない場合は、Difyによって自動生成された`tool_name`で、ツール管理ページで確認できます。
