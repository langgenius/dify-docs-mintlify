# 集成 Langfuse

### Langfuse 简介

Langfuse 是一个开源的 LLM 工程平台，可以帮助团队协作调试、分析和迭代他们的应用程序。

{% hint style="info" %}
Langfuse 官网介绍：[https://langfuse.com/](https://langfuse.com/)
{% endhint %}

***

### 配置 Langfuse

1. 在[官网注册](https://langfuse.com/)并登录 Langfuse
2. 在 Langfuse 内创建项目，登录后在主页点击 **New** ，创建一个自己的项目，**项目**将用于与 Dify 内的**应用**关联进行数据监测。

![在 Langfuse 内创建项目](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/75bed34765ed7d0e933a0069ecb094dd.png)

为项目编辑一个名称。

![在 Langfuse 内创建项目](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/26cfbb94e312a100c39e217fdd0b4406.png)

3. 创建项目 API 凭据，在项目内左侧边栏中点击 **Settings** 打开设置

![创建一个项目 API 凭据](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/2ed72a6761f2977201c29e67e5bc634c.png)

在 Settings 内点击 **Create API Keys** 创建一个项目 API 凭据。

![创建一个项目 API 凭据](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/3c3fbd5392d37fbccf1f9ef76c54f0bc.png)

复制并保存 **Secret Key** ，**Public Key，Host**

![获取 API Key 配置](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/a2ff67951ce300082d875eae8458c8c7.png)

4. 在 Dify 内配置 Langfuse，打开需要监测的应用，在侧边菜单打开**监测**，在页面中选择**配置。**

![配置 Langfuse](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/0eea1c32267c651ea799cbb6ad1f5052.png)

点击配置后，将在 Langfuse 内创建的 **Secret Key, Public Key, Host** 粘贴到配置内并保存。

![配置 Langfuse](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/fe19c8989b14e80420beb3d704b518db.png)

成功保存后可以在当前页面查看到状态，显示已启动即正在监测。

![查看配置状态](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/9caa62e2a91f1f8470b4fa13a104251c.png)

***

### 在 Langfuse 内查看监测数据

配置完成后， Dify 内应用的调试或生产数据可以在 Langfuse 查看监测数据。

![在 Dify 内调试应用](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/3021f46e89ea94af506b1436891c1a56.png)

![在 Langfuse 内查看应用数据](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/b5b48b5a3a1a917f137171290e1c3b0c.png)

![在 Langfuse 内查看应用数据](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/monitoring/integrate-external-ops-tools/de3b4e21db7fd39b4fa4cb4d54d1079e.png)

### 监测数据清单

#### Workflow /Chatflow Trace信息

**用于追踪workflow以及chatflow**

| Workflow                                 | LangFuse Trace          |
| ---------------------------------------- | ----------------------- |
| workflow\_app\_log\_id/workflow\_run\_id | id                      |
| user\_session\_id                        | user\_id                |
| workflow\_{id}                           | name                    |
| start\_time                              | start\_time             |
| end\_time                                | end\_time               |
| inputs                                   | input                   |
| outputs                                  | output                  |
| 模型token消耗相关                              | usage                   |
| metadata                                 | metadata                |
| error                                    | level                   |
| error                                    | status\_message         |
| \[workflow]                              | tags                    |
| conversation\_id/workflow时无              | session\_id             |
| conversion\_id                           | parent\_observation\_id |

**Workflow Trace Info**

* workflow\_id - Workflow的唯一标识
* conversation\_id - 对话ID
* workflow\_run\_id - 此次运行的ID
* tenant\_id - 租户ID
* elapsed\_time - 此次运行耗时
* status - 运行状态
* version - Workflow版本
* total\_tokens - 此次运行使用的token总数
* file\_list - 处理的文件列表
* triggered\_from - 触发此次运行的来源
* workflow\_run\_inputs - 此次运行的输入数据
* workflow\_run\_outputs - 此次运行的输出数据
* error - 此次运行中发生的错误
* query - 运行时使用的查询
* workflow\_app\_log\_id - Workflow应用日志ID
* message\_id - 关联的消息ID
* start\_time - 运行开始时间
* end\_time - 运行结束时间
* workflow node executions - workflow节点运行信息
* Metadata
  * workflow\_id - Workflow的唯一标识
  * conversation\_id - 对话ID
  * workflow\_run\_id - 此次运行的ID
  * tenant\_id - 租户ID
  * elapsed\_time - 此次运行耗时
  * status - 运行状态
  * version - Workflow版本
  * total\_tokens - 此次运行使用的token总数
  * file\_list - 处理的文件列表
  * triggered\_from - 触发来源

#### Message Trace信息

**用于追踪llm对话相关**

| Message                          | LangFuse Generation/Trace |
| -------------------------------- | ------------------------- |
| message\_id                      | id                        |
| user\_session\_id                | user\_id                  |
| message\_{id}                    | name                      |
| start\_time                      | start\_time               |
| end\_time                        | end\_time                 |
| inputs                           | input                     |
| outputs                          | output                    |
| 模型token消耗相关                      | usage                     |
| metadata                         | metadata                  |
| error                            | level                     |
| error                            | status\_message           |
| \["message", conversation\_mode] | tags                      |
| conversation\_id                 | session\_id               |
| conversion\_id                   | parent\_observation\_id   |

**Message Trace Info**

* message\_id - 消息ID
* message\_data - 消息数据
* user\_session\_id - 用户的session\_id
* conversation\_model - 对话模式
* message\_tokens - 消息中的令牌数
* answer\_tokens - 回答中的令牌数
* total\_tokens - 消息和回答中的总令牌数
* error - 错误信息
* inputs - 输入数据
* outputs - 输出数据
* file\_list - 处理的文件列表
* start\_time - 开始时间
* end\_time - 结束时间
* message\_file\_data - 消息关联的文件数据
* conversation\_mode - 对话模式
* Metadata
  * conversation\_id - 消息所属对话的ID
  * ls\_provider - 模型提供者
  * ls\_model\_name - 模型ID
  * status - 消息状态
  * from\_end\_user\_id - 发送用户的ID
  * from\_account\_id - 发送账户的ID
  * agent\_based - 是否基于代理
  * workflow\_run\_id - 工作流运行ID
  * from\_source - 消息来源
  * message\_id - 消息ID

#### Moderation Trace信息

**用于追踪对话审查**

| Moderation    | LangFuse Generation/Trace |
| ------------- | ------------------------- |
| user\_id      | user\_id                  |
| moderation    | name                      |
| start\_time   | start\_time               |
| end\_time     | end\_time                 |
| inputs        | input                     |
| outputs       | output                    |
| metadata      | metadata                  |
| \[moderation] | tags                      |
| message\_id   | parent\_observation\_id   |

**Message Trace Info**

* message\_id - 消息ID
* user\_id: 用户id
* workflow\_app\_log\_id workflow\_app\_log\_id
* inputs - 审查的输入数据
* message\_data - 消息数据
* flagged - 是否被标记为需要注意的内容
* action - 执行的具体行动
* preset\_response - 预设响应
* start\_time - 审查开始时间
* end\_time - 审查结束时间
* Metadata
  * message\_id - 消息ID
  * action - 执行的具体行动
  * preset\_response - 预设响应

#### Suggested Question Trace信息

**用于追踪建议问题**

| Suggested Question     | LangFuse Generation/Trace |
| ---------------------- | ------------------------- |
| user\_id               | user\_id                  |
| suggested\_question    | name                      |
| start\_time            | start\_time               |
| end\_time              | end\_time                 |
| inputs                 | input                     |
| outputs                | output                    |
| metadata               | metadata                  |
| \[suggested\_question] | tags                      |
| message\_id            | parent\_observation\_id   |

**Message Trace Info**

* message\_id - 消息ID
* message\_data - 消息数据
* inputs - 输入的内容
* outputs - 输出的内容
* start\_time - 开始时间
* end\_time - 结束时间
* total\_tokens - 令牌数量
* status - 消息状态
* error - 错误信息
* from\_account\_id - 发送账户的ID
* agent\_based - 是否基于代理
* from\_source - 消息来源
* model\_provider - 模型提供者
* model\_id - 模型ID
* suggested\_question - 建议的问题
* level - 状态级别
* status\_message - 状态信息
* Metadata
  * message\_id - 消息ID
  * ls\_provider - 模型提供者
  * ls\_model\_name - 模型ID
  * status - 消息状态
  * from\_end\_user\_id - 发送用户的ID
  * from\_account\_id - 发送账户的ID
  * workflow\_run\_id - 工作流运行ID
  * from\_source - 消息来源

#### Dataset Retrieval Trace信息

**用于追踪知识库检索**

| Dataset Retrieval     | LangFuse Generation/Trace |
| --------------------- | ------------------------- |
| user\_id              | user\_id                  |
| dataset\_retrieval    | name                      |
| start\_time           | start\_time               |
| end\_time             | end\_time                 |
| inputs                | input                     |
| outputs               | output                    |
| metadata              | metadata                  |
| \[dataset\_retrieval] | tags                      |
| message\_id           | parent\_observation\_id   |

**Dataset Retrieval Trace Info**

* message\_id - 消息ID
* inputs - 输入内容
* documents - 文档数据
* start\_time - 开始时间
* end\_time - 结束时间
* message\_data - 消息数据
* Metadata
  * message\_id消息ID
  * ls\_provider模型提供者
  * ls\_model\_name模型ID
  * status消息状态
  * from\_end\_user\_id发送用户的ID
  * from\_account\_id发送账户的ID
  * agent\_based是否基于代理
  * workflow\_run\_id工作流运行ID
  * from\_source消息来源

#### Tool Trace信息

**用于追踪工具调用**

| Tool                  | LangFuse Generation/Trace |
| --------------------- | ------------------------- |
| user\_id              | user\_id                  |
| tool\_name            | name                      |
| start\_time           | start\_time               |
| end\_time             | end\_time                 |
| inputs                | input                     |
| outputs               | output                    |
| metadata              | metadata                  |
| \["tool", tool\_name] | tags                      |
| message\_id           | parent\_observation\_id   |

**Tool Trace Info**

* message\_id消息ID
* tool\_name工具名称
* start\_time开始时间
* end\_time结束时间
* tool\_inputs工具输入
* tool\_outputs工具输出
* message\_data消息数据
* error错误信息，如果存在
* inputs消息的输入内容
* outputs消息的回答内容
* tool\_config工具配置
* time\_cost时间成本
* tool\_parameters工具参数
* file\_url关联文件的URL
* Metadata
  * message\_id消息ID
  * tool\_name工具名称
  * tool\_inputs工具输入
  * tool\_outputs工具输出
  * tool\_config工具配置
  * time\_cost时间成本
  * error错误信息
  * tool\_parameters工具参数
  * message\_file\_id消息文件ID
  * created\_by\_role创建者角色
  * created\_user\_id创建者用户ID

#### Generate Name Trace信息

**用于追踪会话标题生成**

| Generate Name     | LangFuse Generation/Trace |
| ----------------- | ------------------------- |
| user\_id          | user\_id                  |
| generate\_name    | name                      |
| start\_time       | start\_time               |
| end\_time         | end\_time                 |
| inputs            | input                     |
| outputs           | output                    |
| metadata          | metadata                  |
| \[generate\_name] | tags                      |

**Generate Name Trace Info**

* conversation\_id对话ID
* inputs输入数据
* outputs生成的会话名称
* start\_time开始时间
* end\_time结束时间
* tenant\_id租户ID
* Metadata
  * conversation\_id对话ID
  * tenant\_id租户ID
