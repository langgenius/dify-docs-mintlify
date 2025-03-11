# 发布插件

### 发布方式

为了满足不同开发者的发布需求，Dify 提供了以下三种插件发布方式：

#### **1. Marketplace**

**简介**：Dify 官方提供的插件市场，用户可以在此浏览、搜索并一键安装各类插件。

**特点**：

* 插件经审核后上线，**安全可靠**。
* 可直接安装至个人或团队的 **Workspace** 中。

**发布流程**：

* 将插件项目提交至 **Dify Marketplace** [代码仓库](https://github.com/langgenius/dify-plugins)。
* 经过官方审核后，插件将在市场内公开发布，供其他用户安装使用。

详细说明请参考：

{% content-ref url="publish-to-dify-marketplace/" %}
[publish-to-dify-marketplace](publish-to-dify-marketplace/)
{% endcontent-ref %}

#### 2. **GitHub 仓库**

**简介**：将插件开源或托管在 **GitHub** 上，方便他人查看、下载和安装。

**特点**：

* 便于**版本管理**和**开源共享**。
* 用户可通过插件链接直接安装，无需平台审核。

**发布流程**：

* 将插件代码推送至 GitHub 仓库。
* 分享仓库链接，用户可通过链接将插件集成至 **Dify Workspace**。

详细说明请参考：

{% content-ref url="publish-plugin-on-personal-github-repo.md" %}
[publish-plugin-on-personal-github-repo.md](publish-plugin-on-personal-github-repo.md)
{% endcontent-ref %}

#### 3. 插件文件包（本地安装）

**简介**：将插件打包成本地文件（如 `.difypkg` 格式），通过文件分享的方式供他人安装。

**特点**：

* 不依赖在线平台，**快速灵活**地分享插件。
* 适用于**私有插件**或**内部测试**。

**发布流程**：

* 将插件项目打包为本地文件。
* 在 Dify 插件页面点击**上传插件**，选择本地文件安装插件。

你可以将插件项目打包为一个本地文件并分享给他人，在插件页上传文件后即可将插件安装至 Dify Workspace 内。

详细说明请参考：

{% content-ref url="package-plugin-file-and-publish.md" %}
[package-plugin-file-and-publish.md](package-plugin-file-and-publish.md)
{% endcontent-ref %}

### **发布建议**

* **想要推广插件** → **推荐使用 Marketplace**，通过官方审核保障插件质量，提升曝光度。
* **开源共享项目** → **推荐使用 GitHub**，方便版本管理与社区协作。
* **快速分发或内部测试** → **推荐使用插件文件**，简单高效地安装和分享。
