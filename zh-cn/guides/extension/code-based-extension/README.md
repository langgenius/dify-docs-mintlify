# 代码扩展

对于在本地部署 Dify 的开发人员来说，代码扩展可以在不重写 API 服务的情况下实现功能的扩展。你可以在不破坏 Dify 原始代码逻辑的情况下，以代码形式扩展或增强程序的功能（即插件功能）。它遵循一定的接口或规范，以实现与主程序的兼容性和即插即用功能。目前，Dify 提供两种代码扩展：

* [外部数据工具](external-data-tool.md "mention")
* [敏感内容审核](moderation.md "mention")

基于上述功能，你可以按照代码级接口规范实现横向扩展。如果你愿意为我们贡献你的扩展功能，我们非常欢迎你为 Dify 提交 PR。

## 前端组件规范定义

代码扩展的前端样式通过 `schema.json` 进行定义：

* label: 自定义类型名称，支持系统语言切换
* form_schema: 表单内容列表
  * type: 组件类型
    * select: 下拉选项
    * text-input: 文本
    * paragraph: 段落
  * label: 组件名称，支持系统语言切换
  * variable: 变量名
  * required: 是否为必填
  * default：默认值
  * placeholder: 组件提示内容
  * options: 组件的专属属性，定义下拉内容
    * label：下拉菜单名称，支持系统语言切换
    * value：下拉选项值
  * max_length：专属属性

### 模板示例

```json
{
    "label": {
        "en-US": "Cloud Service",
        "zh-Hans": "云服务"
    },
    "form_schema": [
        {
            "type": "select",
            "label": {
                "en-US": "Cloud Provider",
                "zh-Hans": "云厂商"
            },
            "variable": "cloud_provider",
            "required": true,
            "options": [
                {
                    "label": {
                        "en-US": "AWS",
                        "zh-Hans": "亚马逊"
                    },
                    "value": "AWS"
                },
                {
                    "label": {
                        "en-US": "Google Cloud",
                        "zh-Hans": "谷歌云"
                    },
                    "value": "GoogleCloud"
                },
                {
                    "label": {
                        "en-US": "Azure Cloud",
                        "zh-Hans": "微软云"
                    },
                    "value": "Azure"
                }
            ],
            "default": "GoogleCloud",
            "placeholder": ""
        },
        {
            "type": "text-input",
            "label": {
                "en-US": "API Endpoint",
                "zh-Hans": "API Endpoint"
            },
            "variable": "api_endpoint",
            "required": true,
            "max_length": 100,
            "default": "",
            "placeholder": "https://api.example.com"
        },
        {
            "type": "paragraph",
            "label": {
                "en-US": "API Key",
                "zh-Hans": "API Key"
            },
            "variable": "api_keys",
            "required": true,
            "default": "",
            "placeholder": "Paste your API key here"
        }
    ]
}
```