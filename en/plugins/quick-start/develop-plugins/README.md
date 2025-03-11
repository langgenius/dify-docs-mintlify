# Develop Plugins

### **Quick Start**

You can quickly understand how to develop different types of plugins and master the functional components involved in plugin development through these development examples:

{% content-ref url="initialize-development-tools.md" %}
[initialize-development-tools.md](initialize-development-tools.md)
{% endcontent-ref %}

Using the **Google Search** tool as an example to demonstrate how to develop tool-type plugins. For more details, please take refer to the following:

{% content-ref url="tool-plugin.md" %}
[tool-plugin.md](tool-plugin.md)
{% endcontent-ref %}

By examining the **Anthropic** and **Xinference** models, we present separate guides on how to develop predefined model plugins and custom model plugins.

* Predefined models are pre-trained and validated, typically commercial models (such as the GPT series and Claude series models). These models can be utilized directly to accomplish specific tasks without additional training or configuration.
* Custom model plugins enable developers to integrate privately trained or specifically configured models tailored to meet local needs.

For development examples, refer to the following content:

{% content-ref url="model-plugin/" %}
[model-plugin](model-plugin/)
{% endcontent-ref %}

Extension plugins enable developers to package business code as plugins and automatically provide an Endpoint request entry, functioning akin to an API service hosted on the Dify platform. For more details please take refer to:

{% content-ref url="extension-plugin.md" %}
[extension-plugin.md](extension-plugin.md)
{% endcontent-ref %}

### **Endpoints Documentation**

If you want to read detailed interface documentation for plugin projects, you can refer to these standard specification documents:

1. [General Specifications](../../schema-definition/general-specifications.md)
2. [Manifest Definitions](../../schema-definition/manifest.md)
3. [Tool Integration Definitions](../../schema-definition/tool.md)
4. [Model Integration Introduction](../../schema-definition/model/)
5. [Endpoint Definitions](../../schema-definition/endpoint.md)
6. [Extended Agent Strategy](../../schema-definition/agent.md)
7. [Reverse Invocation of the Dify](../../schema-definition/reverse-invocation-of-the-dify-service/) Services
   1. [Reverse Invoking Apps](../../schema-definition/reverse-invocation-of-the-dify-service/app.md)
   2. [Reverse Invoking Models](../../schema-definition/reverse-invocation-of-the-dify-service/model.md)
   3. [Reverse Invoking Nodes](../../schema-definition/reverse-invocation-of-the-dify-service/node.md)
   4. [Reverse Invoking Tools](../../schema-definition/reverse-invocation-of-the-dify-service/tool.md)
8. [Plugin Persistence Storage Capabilities](../../schema-definition/persistent-storage.md)

### **Contribution Guidelines**

Want to contribute code and features to Dify Marketplace?&#x20;

We provide detailed development guidelines and contribution guidelines to help you understand our architecture design and contribution process:

*   [Dify Plugin Contribution Guidelines](../../publish-plugins/publish-to-dify-marketplace/)

    Learn how to submit your plugin to the Dify Marketplace to share your work with a broader developer community.
*   [GitHub Publishing Guidelines](../../publish-plugins/publish-plugin-on-personal-github-repo.md)

    Discover how to publish and manage your plugins on GitHub, ensuring ongoing optimization and collaboration with the community.

Welcome to join us and become our contributors, and help to enhance the Dify ecosystem alongside developers worldwide!
