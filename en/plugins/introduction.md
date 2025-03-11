# Introduction

> To access the plugin’s functionality in the Community Edition, please update the version to v1.0.0.

## **What is the Plugin?**

Plugin is a more developer-friendly and highly extensible third-party service extension module. While the Dify platform already includes numerous tools maintained by the Dify team and community contributors, the existing tools may not fully meet the demands of various niche scenarios. Additionally, developing and integrating new tools into the Dify platform often requires a lengthy process.

To enable more agile development, we have opened up the ecosystem and provided a comprehensive plugin development SDK. This empowers every developer to easily **build their own tools and seamlessly integrate third-party models and tools**, enhancing application capabilities significantly.

## What is the Advantage of Plugin?

The new plugin system goes beyond the limitations of the previous framework, offering richer and more powerful extension capabilities. It contains five distinct plugin types, each designed to solve well-defined scenarios, giving developers limitless freedom to customize and enhance Dify applications.

Additionally, the plugin system is designed to be easily shared. You can distribute your plugins via the [Dify Marketplace](https://marketplace.dify.ai/), [GitHub](publish-plugins/publish-plugin-on-personal-github-repo/), or as a [Local file package](publish-plugins/package-and-publish-plugin-file/). Other developers can quickly install these plugins and benefit from them.

> Dify Marketplace is an open ecosystem designed for developers, offering a broad range of resources—models, tools, AI Agents, Extensions, and plugin bundles. You can seamlessly integrate third-party services into your existing Dify applications through the Marketplace, enhancing their capabilities and advancing the overall Dify community.

Whether you’re looking to integrate a new model or add a specialized tool to expand Dify’s existing features, the robust plugin marketplace has the resources you need. **We encourage more developers to join and help shape the Dify ecosystem, benefiting everyone involved.**

![](https://assets-docs.dify.ai/2025/01/83f9566063db7ae4886f6a139f3f81ff.png)

## **What Are the Types of Plugin?**

*   **Models**

    These plugins integrate various AI models (including mainstream LLM providers and custom model) to handle configuration and requests for LLM APIs. For more on creating a model plugin, take refer to [Quick Start: Model Plugin](https://docs.dify.ai/plugins/quick-start/develop-plugins/model-plugin).
*   **Tools**

    Tools refer to third-party services that can be invoked by Chatflow, Workflow, or Agent-type applications. They provide a complete API implementation to enhance the capabilities of Dify applications. For example, developing a Google Search plugin, please refer to [Quick Start: Tool Plugin](quick-start/develop-plugins/tool-plugin.md).
*   **Agent Strategy**

    The Agent Strategy plugin defines the reasoning and decision-making logic within an Agent node, including tool selection, invocation, and result processing.
* Agent strategy plugins define the internal reasoning and decision-making logic within agent nodes. They encompass the logic for tool selection, invocation, and handling of returned results by the LLM. For further development guidance, please refer to the [Quick Start: Agent Strategy Plugin](quick-start/develop-plugins/agent-strategy-plugin.md).
*   **Extensions**

    Lightweight plugins that only provide endpoint capabilities for simpler scenarios, enabling fast expansions via HTTP services. This approach is ideal for straightforward integrations requiring basic API invoking. For more details, refer to [Quick Start: Extension Plugin](quick-start/develop-plugins/extension-plugin.md).
*   **Bundle**

    A “plugin bundle” is a collection of multiple plugins. Bundles allow you to install a curated set of plugins all at once—no more adding them one by one. For more information on creating plugin bundles, see [Plugin Development: Bundle Plugin](quick-start/develop-plugins/bundle.md).

### **What’s New in Plugins?**

*   **Extend LLM’s Multimodal Capabilities**

    Plugins can boost an LLM’s ability to handle multimedia. Developers can add tasks like image editing, video processing, and more—ranging from cropping and background removal to working with portrait images.
*   **Developer-Friendly Debugging Capabilities**

    The plugin system supports popular IDEs and debugging tools. You just configure a few environment variables to remotely connect to a Dify instance—even one running as a SaaS. Any actions you take on that plugin in Dify are forwarded to your local runtime for debugging.
*   **Persistent Data Storage**

    Designed for more complex use cases, the plugin system now includes data persistence:

    * **Plugin-Level Data Storage**: You can share workspace-level information with plugins, enabling richer custom features.
    * **Built-In Data Management**: Plugins can reliably store and manage data, making it easier to implement complex business logic.
*   **Convenient Reverse Invocation**

    Plugins can now interact bidirectionally with Dify’s core functions, including:&#x20;

    * AI model invokes
    * Tool usage
    * Application access
    * Knowledge base interaction
    * Function node calls (such as question classification, parameter extraction, etc.)

    This two-way mechanism allows plugins to act not only as a way to leverage existing Dify capabilities, but also as a standalone gateway—expanding the usage scenarios for your applications.
*   **Enhanced Endpoint Customization Capabilities**

    Beyond the existing Dify app APIs (like Chatbot or Workflow APIs), you can now create custom APIs within plugins. Developers can wrap their business logic as a plugin, host it on the [Dify Marketplace](https://marketplace.dify.ai/), and automatically get endpoint support for data processing and request handling.

## Learn More

**Quick Start**

To quickly install and use plugins, take refer to:

{% content-ref url="quick-start/install-plugins.md" %}
[install-plugins.md](quick-start/install-plugins.md)
{% endcontent-ref %}

To start developing plugins, take refer to:

{% content-ref url="quick-start/develop-plugins/" %}
[develop-plugins](quick-start/develop-plugins/)
{% endcontent-ref %}

**Publishing Plugins**

To publish your plugin on the [Dify Marketplace](https://marketplace.dify.ai/), fill out the required information and usage documentation. Then submit your plugin code to the [GitHub repository](https://github.com/langgenius/dify-plugins). Once approved, it will be listed in the marketplace:

{% content-ref url="publish-plugins/publish-to-dify-marketplace/" %}
[publish-to-dify-marketplace](publish-plugins/publish-to-dify-marketplace/)
{% endcontent-ref %}

Beyond the official Dify Marketplace, you can also host your plugin on a personal GitHub repository or package it as a file for direct sharing:

{% content-ref url="publish-plugins/publish-to-dify-marketplace/" %}
[publish-to-dify-marketplace](publish-plugins/publish-to-dify-marketplace/)
{% endcontent-ref %}

{% content-ref url="publish-plugins/package-plugin-file-and-publish.md" %}
[package-plugin-file-and-publish.md](publish-plugins/package-plugin-file-and-publish.md)
{% endcontent-ref %}
