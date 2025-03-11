# Tool

当遇到以下需求时：

* 某个工具类型插件已经实现好了一个功能，但效果未达预期，需要对数据进行二次加工。
* 某个任务需要使用到爬虫，希望能够自由选择爬虫服务。
* 需要集合多个工具的返回结果，但是通过 Workflow 应用不好处理。

此时需要在插件中调用其他已经实现好的工具，该工具可能是市场中的某个工具插件，可能是自主构建的 Workflow as a Tool，亦或是自定义工具。

上述需求可以通过调用插件的 `self.session.tool` 字段来实现。

### 调用已安装的工具

允许插件调用已安装在当前 Workspace 内的各个工具，其中也包含其它工具类型的插件。

**入口**

```python
    self.session.tool
```

**接口**

```python
    def invoke_builtin_tool(
        self, provider: str, tool_name: str, parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        pass
```

其中 provider 为 plugin 的 ID 加上工具供应商名称，格式形如 `langgenius/google/google`，tool\_name 为具体的工具名称，`parameters` 为最后传递给该工具的参数。

### 调用 Workflow as Tool

如需了解关于 Workflow as Tool 的更多说明，请参考[此文档](tool.md#diao-yong-workflow-as-tool)。

**入口**

```python
    self.session.tool
```

**接口**

```python
    def invoke_workflow_tool(
        self, provider: str, tool_name: str, parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        pass
```

此时的 provider 为该 tool 的 ID，tool\_name 在创建该 tool 的时候会要求填写。

### 调用 Custom Tool

**入口**

```python
    self.session.tool
```

**接口**

```python
    def invoke_api_tool(
        self, provider: str, tool_name: str, parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        pass
```

此时的 `provider` 为该 tool 的 ID，`tool_name` 为 OpenAPI 中的 `operation_id`，若不存在，即为 Dify 自动生成的 `tool_name`，可以在工具管理页中看到具体的名称。\
