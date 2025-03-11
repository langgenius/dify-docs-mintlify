---
description: 'Author: Allen'
---

# Install and Use Plugins

## Installing Plugins

To install plugins, click **"Plugins"** in the top-right corner of the Dify platform to access the plugin management page. You can install plugins via **Marketplace, GitHub, or Manual Upload**.

![Install Plugins](https://assets-docs.dify.ai/2025/01/a56c40245090d9252557dcc6f4064a14.png)

#### Marketplace

Browse and select a plugin from the Marketplace. Click **"Install"** to add it to your current workspace effortlessly.

![Install via marketplace](https://assets-docs.dify.ai/2025/01/6ae8b661b7fa01b228a954d00ef552f3.png)

#### GitHub

Install plugins directly using GitHub repository links. This method requires plugins to meet code standards and include a `.difypkg` file attached to a Release. For more details, see [Publishing Plugins on GitHub](../publish-plugins/publish-plugin-on-personal-github-repo.md).

![GitHub Installation](https://assets-docs.dify.ai/2025/01/4026a12a915e3fe9bd057d8827acfdce.png)

#### Local Upload

After [packaging your plugin](../publish-plugins/package-plugin-file-and-publish.md), upload the resulting `.difypkg` file. This option is ideal for offline or test environments and allows organizations to maintain internal plugins without exposing sensitive information.

#### Authorizing Plugins

Some plugins require API Keys or other authorization to function properly. After installation, enter the necessary credentials to enable the plugin.

> API Keys are sensitive information and are only valid for the current user. Other team members must manually input their credentials to use the plugin.

![Authorize Plugin](https://assets-docs.dify.ai/2024/11/972de4c9fa00f792a1ab734b080aafdc.png)

***

## Using Plugins

Once installed, plugins can be integrated into your Dify applications. Below are examples of how to use different types of plugins.

### Model Plugins

For example, after installing the `OpenAI` model plugin, click **Profile → Settings → Model Providers** in the top-right corner to configure your API Key and activate the provider.

![Authorize OpenAI API Key](https://assets-docs.dify.ai/2025/01/3bf32d49975931e5924baa749aa7812f.png)

Once authorized, the model can be used in all application types.

![Using Model Plugin](https://assets-docs.dify.ai/2024/12/4a38b1ea534ca68515839c518c250d2f.png)

### Tool Plugins

Tool plugins can be used in **Chatflow**, **Workflow**, and **Agent** applications. Below is an example using the `Google` tool plugin.

> Some tool plugins require API Key authorization before use. Configure these after installation for future convenience.

#### Agent

In an Agent application, locate the **"Tools"** section at the bottom of the application orchestration page. Select your installed tool plugins.

When using the application, input instructions to utilize the tools. For example, entering "today's news" will invoke the Google plugin to retrieve online content.

![Agent Tools](https://assets-docs.dify.ai/2024/12/78f833811cb0c3d5cbbb1a941cffc769.png)

#### Chatflow / Workflow

Chatflow and Workflow applications share the same orchestration canvas, so tool usage is identical.

Click the **"+"** button at the end of a node, select the installed Google plugin, and connect it to the upstream nodes.

![Chatflow / Workflow Tools](https://assets-docs.dify.ai/2024/12/7e7bcf1f9e3acf72c6917ea9de4e4613.png)

In the plugin's input variables, enter the user query or other required information for online retrieval.

![Tools input](https://assets-docs.dify.ai/2024/12/a67c4cffd8fdf33297d462b2e6d01d27.png)

For usage methods of other plugin types, refer to their respective plugin detail pages.

![Using Plugins](https://assets-docs.dify.ai/2025/01/9d826302637638f705a94f73bd653958.png)

***

## Read More

To learn how to get started with plugin development, refer to the following guide:

{% content-ref url="develop-plugins/" %}
[develop-plugins](develop-plugins/)
{% endcontent-ref %}
