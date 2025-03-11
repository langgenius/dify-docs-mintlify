---
description: 'Author: Yeuoly，Allen'
---

# Manifest

Manifest 是一个符合 yaml 规范的文件，它定义了**插件**最基础的信息，包括但不限于插件名称、作者、包含的工具、模型等信息。

若该文件的格式错误，插件的解析和打包过程都将会失败。

### 代码示例

下面是一个 Manifest 文件的简单示例，将在下文解释各个数据的含义和作用。

如需参考其它插件的代码，请参考 [GitHub 代码仓库](https://github.com/langgenius/dify-official-plugins/blob/main/tools/google/manifest.yaml)。

```yaml
version: 0.0.1
type: "plugin"
author: "Yeuoly"
name: "neko"
label:
  en_US: "Neko"
created_at: "2024-07-12T08:03:44.658609186Z"
icon: "icon.svg"
resource:
  memory: 1048576
  permission:
    tool:
      enabled: true
    model:
      enabled: true
      llm: true
    endpoint:
      enabled: true
    app:
      enabled: true
    storage: 
      enabled: true
      size: 1048576
plugins:
  endpoints:
    - "provider/neko.yaml"
meta:
  version: 0.0.1
  arch:
    - "amd64"
    - "arm64"
  runner:
    language: "python"
    version: "3.10"
    entrypoint: "main"
privacy: "./privacy.md"
```

### 结构

* `version`(version, required)：插件的版本
* `type`(type, required)：插件类型，目前仅支持 `plugin`，未来支持 `bundle`
* `author`(string, required)：作者，在 Marketplace 中定义为组织名
* `label`(label, required)：多语言名称
* `created_at`(RFC3339, required)：创建时间，Marketplace 上要求创建时间不得大于当前时间
* `icon`(asset, required)：图标路径
* `resource` (object)：需要申请的资源
  * `memory` (int64)：最大内存占用，主要与 SaaS 上的 AWS Lambda 资源申请相关，单位字节
  * `permission`(object)：权限申请
    * `tool`(object)：反向调用工具的权限
      * `enabled` (bool)
    * `model`(object)：反向调用模型的权限
      * `enabled`(bool)
      * `llm`(bool)
      * `text_embedding`(bool)
      * `rerank`(bool)
      * `tts`(bool)
      * `speech2text`(bool)
      * `moderation`(bool)
    * `node`(object)：反向调用节点的权限
      * `enabled`(bool)
    * `endpoint`(object)：允许注册 `endpoint` 的权限
      * `enabled`(bool)
    * `app`(object)：反向调用`app`的权限
      * `enabled`(bool)
    * `storage`(object)：申请持久化存储的权限
      * `enabled`(bool)
      * `size`(int64)：最大允许多大的持久化内存，单位字节
* `plugins`(object, required)：插件扩展的具体能力的`yaml`文件列表，插件包内的绝对路径，如需要扩展模型，则需要定义一个类似于 `openai.yaml`的文件，并将该文件路径填写在此处，且该路径上的文件必须真实存在，否则打包将失败。
  * 格式
    * `tools`(list\[string])：插件扩展的[工具](tool.md)供应商
    * `models`(list\[string])：插件扩展的[模型](model/)供应商
    * `endpoints`(list\[string])：插件扩展的 [Endpoints](endpoint.md) 供应商
    * `agent_strategies` (list\[string])：插件扩展的 Agent 策略供应商
  * 限制
    * 不允许同时扩展工具与模型
    * 不允许没有任意扩展
    * 不允许同时扩展模型与 Endpoint
    * 目前仅支持各类型扩展最多一个供应商
* `meta`(object)
  * `version`(version, required)：`manifest` 格式版本，初始版本 `0.0.1`
  * `arch`(list\[string], required)：支持的架构，目前仅支持 `amd64` `arm64`
  * `runner`(object, required)：运行时配置
    * `language`(string)：目前仅支持 python
    * `version`(string)：语言的版本，目前仅支持 `3.12`
    * `entrypoint`(string)：程序入口，在 python 下应为 `main`
* `privacy` (string, optional)：可选项，指定插件隐私政策文件的相对路径或 URL，例如 `"./privacy.md"` 或 `"https://your-web/privacy"`。如果计划将插件上架至 Dify Marketplace，**该字段为必填项**，用于提供明确的用户数据使用和隐私声明。详细填写指引请参考[插件隐私政策准则](../publish-plugins/publish-to-dify-marketplace/plugin-privacy-protection-guidelines.md)。
