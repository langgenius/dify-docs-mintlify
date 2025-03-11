# 概念同步

Dify的概念支持从概念导入并设置 **同步** 以便在概念更新后自动同步数据以进行更新.

### 鉴权

1. 当创建知识库时, 选择数据源, 点击 **从概念同步--转到连接**, 并根据提示完成授权验证.
2. 你也可以: 点击 **设置--数据源--添加数据源**, 点击概念来源 **连接** 以完成鉴权.

![概念链接](../../.gitbook/assets/notion-connect.png)

### 导入数据

完成鉴权操作后, 前往构建知识库页面, 点击 **概念同步**, 选择要导入的所需授权页面.

### 分段清洗

接下来, 选择你的 **分段设置** 和 **索引方法**, **保存并处理**. 等待dify数据处理, 通常此步骤需要在LLM提供程序中使用令牌. 不仅支持导入普通页面类型，还可以汇总保存数据库类型下的页面属性.

_**便笺:当前不支持导入图像和文件。表数据将转换为文本.**_

### 同步概念数据

如果你的概念内容已被修改，你可以直接在dify知识文档列表页面上单击[同步]按钮，一键同步数据(请注意，每次单击都会同步当前内容)。此步骤需要使用令牌.

![同步概念数据](../../.gitbook/assets/sync-notion-data.png)

### (社区版) 概念集成配置指南

集成分为两种方式: **内部集成** 和 **公共集成** . 它可以按需在dify中配置.

有关这两种集成方法的具体区别，请参阅 [概念正式说明](https://developers.notion.com/docs/authorization).

#### 1. **使用内部集成**

创建你的集成页面 [集成设置](https://www.notion.so/my-integrations) . 默认状态下, 所有集成都从内部集成开始; 内部集成将与你选择的工作空间相关联, 因此，你需要是工作区所有者才能创建集成.

**具体操作步骤:**

点击 " **New integration** " 按钮, 即默认为内部(不能修改), 选择关联的空间, 输入名称并上传logo, 点击"**提交**" 成功创建集成.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/features/datasets/2b26dc5f5b088304b65190e14f58423a.png)

一旦创建了集成, 你可以根据需要更新其设置。 **性能** 此选项卡，然后再单击 "**显示**" 按钮后 **密钥** 复制你的密钥.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/features/datasets/764276a102e3264747c64f02dafa5f5d.png)

将其复制并返回到dify源代码 , 在 **.env** 文件与配置相关的环境变量中，环境变量如下:

**NOTION\_INTEGRATION\_TYPE** = 内部 或 **NOTION\_INTEGRATION\_TYPE** = 公用

**NOTION\_INTERNAL\_SECRET**= 你的内部密钥

#### 2. **使用公共集成**

**你需要将内部集成升级为公共集成** , 导航到集成分发页面，并切换开关以显示集成.

要将开关切换到公共设置，你需要 **在组织信息中填写其他信息**, 包括你的公司名称, 网址, 和重定向目标路径, 然后点击 "提交" 按钮.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/features/datasets/4618b25f23d05de13f99f635459316ec.png)

在你公共集成成功后， 在你的[集成设置页面](https://www.notion.so/my-integrations), 你将能够在[密钥]选项卡中访问集成的密钥.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/features/datasets/053643a0ec218c4e16a3e1b5753ad6a8.png)

返回到dify源代码,在 **.env** 与文件配置相关的环境变量中, 环境变量如下:

**NOTION\_INTEGRATION\_TYPE**=公共

**NOTION\_CLIENT\_SECRET**=你的客户端密钥

**NOTION\_CLIENT\_ID**=你的客户端id

配置完成后，你将能够使用知识部分中的概念数据导入和同步功能.
