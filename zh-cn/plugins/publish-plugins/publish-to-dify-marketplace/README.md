# 发布至 Dify Marketplace

Dify Marketplace 欢迎来自合作伙伴和社区开发者的插件上架申请，您的贡献将进一步丰富 Dify 插件的可能性。本指引将提供清晰的发布流程和最佳实践建议，让您的插件能够顺利发布，并为社区带来价值。

请按照以下步骤，在 [GitHub 代码仓库](https://github.com/langgenius/dify-plugins)提交您的插件 Pull Request（PR）并接受审核，通过后插件将正式上线至 Dify Marketplace。

### 插件的发布流程

将插件发布至 Dify Marketplace 包含以下步骤：

1. 根据[插件开发者准则](plugin-developer-guidelines.md)完成插件的开发和测试；
2. 根据[插件隐私政策准则](plugin-privacy-protection-guidelines.md)撰写该插件隐私政策，并将该隐私政策的文件路径或 URL 写入插件 [Manifest 文件](../../schema-definition/manifest.md)；
3. 完成插件打包；
4. Fork [Dify Plugins](https://github.com/langgenius/dify-plugins) 代码仓库；
5. 创建 Organization 目录，在 Organization 目录下创建插件名目录，将插件的代码和 pkg 文件上传至对应的插件名目录下；
6. 遵循 GitHub 中的 PR Template 内容格式提交 Pull Request (PR) ，等待审核；
7. 审核通过后，插件代码将合并至 Main 分支，插件自动上架至 [Dify Marketplace](https://marketplace.dify.ai/)。

插件提交、审核和上架流程图：

![The process of uploading plugins](https://assets-docs.dify.ai/2025/01/05df333acfaf662e99316432db23ba9f.png)

{% hint style="info" %}
**Note**:

上图中的 Contributor Agreement 指的是[插件开发者准则](plugin-developer-guidelines.md)。
{% endhint %}

***

### Pull Request (PR) 审核期间

积极回应审查人员的提问和反馈：

* **14 天内**未解决的 PR 评论将被标记为过时（可重新开启）。
* **30 天内**未解决的 PR 评论将被关闭（不可重新开启，需要创建新 PR）。

***

### **Pull Request (PR) 审核通过后**

**1. 持续维护**

* 处理用户报告的问题和功能请求。
* 在发生重大 API 变更时迁移插件：
  * Dify 将提前发布变更通知和迁移说明。
  * Dify 工程师可提供迁移支持。

**2. Marketplace 公开 Beta 测试阶段的限制**

* 避免对现有插件引入破坏性更改。

***

### 审核流程

**1. 审核顺序**

* 按照 **先到先审** 的顺序处理 PR。审核将在 1 周内开始。如有延迟，审查人员将通过评论通知 PR 作者。

**2. 审核重点**

* 检查插件名称、描述和设置说明是否清晰且具有指导性。
* 检查插件的 [Manifest 文件](../../schema-definition/manifest.md)是否符合格式规范，并包含有效的作者联系信息。

3. **插件的功能性和相关性**

* 根据[插件开发说明](../../quick-start/develop-plugins/)测试插件。
* 确保插件在 Dify 生态系统中的用途合理。

[Dify.AI](https://dify.ai/) 保留接受或拒绝插件提交的权利。

***

### 常见问题

1. **如何判断插件是否独特？**

示例：一个 Google 搜索插件仅增加了多语言版本，应被视为现有插件的优化。但如果插件实现了显著的功能改进（如优化批量处理或错误处理），则可以作为新插件提交。

2. **如果我的 PR 被标记为过时或关闭怎么办？**

被标记为过时的 PR 可以在解决反馈后重新开启。被关闭的 PR（超过 30 天）需要重新创建一个新 PR。

3. **Beta 测试阶段可以更新插件吗？**

可以，但应避免引入破坏性更改。
