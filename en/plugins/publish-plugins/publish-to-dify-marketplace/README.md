# Publish to Dify Marketplace

**Dify Marketplace** welcomes plugin submission requests from both partners and community developers. Your contributions will broaden the scope of possibilities for Dify plugins. This guide provides clear publishing procedures and best-practice recommendations to help you successfully release your plugin and create value for the community.

Follow these steps to submit your plugin as a Pull Request (PR) in the [GitHub repository](https://github.com/langgenius/dify-plugins) for review. Once approved, your plugin will officially launch on the Dify Marketplace.

### Submitting a Pull Request (PR) for Review

To publish your plugin on the Dify Marketplace, follow these steps:

1. Develop and test your plugin according to the [Plugin Developer Guidelines](plugin-developer-guidelines.md).
2. Write a [Plugin Privacy Policy](plugin-privacy-protection-guidelines.md) for your plugin in line with Dify’s privacy policy requirements. In your plugin’s [Manifest](../../schema-definition/manifest.md) file, include the file path or URL for this privacy policy.
3. Package your plugin for distribution.
4. Fork the [Dify Plugins](https://github.com/langgenius/dify-plugins) repository on GitHub.
5. Create an organization directory under the repository’s main structure, then create a subdirectory named after your plugin. Place your plugin’s source code and the packaged `.pkg` file in that subdirectory.
6. Submit a Pull Request (PR) following the required PR template format, then wait for the review;
7. Once approved, your plugin code will merge into the main branch, and the plugin will be automatically listed on the [Dify Marketplace](https://marketplace.dify.ai/).

Here is the general plugin review process:

![The process of uploading plugins](https://assets-docs.dify.ai/2025/01/05df333acfaf662e99316432db23ba9f.png)

{% hint style="info" %}
**Note**:

The Contributor Agreement mentioned above refers to [Plugin Developer Guidelines](plugin-developer-guidelines.md).
{% endhint %}

***

### **During Pull Request (PR) Review**

Respond proactively to reviewer questions and feedback.

* PR comments unresolved within **14 days** will be marked as stale (they can be reopened).
* PR comments unresolved within **30 days** will be closed (they cannot be reopened, and a new PR must be created).

***

### **After Pull Request (PR) Approval**

**1. Ongoing Maintenance**

* Address user-reported issues and feature requests
* Migrate plugins when major API changes occur:
  * Dify will provide advance notice of changes and migration instructions.
  * Dify engineers can provide migration support.

**2. Marketplace Public Beta Testing Restrictions**

* Avoid introducing breaking changes to existing plugins.

***

### **Review Process**

**1. Review Order**

* Pull Requests (PRs) are handled on a **first-come, first-served** basis.
* Review will generally begin within one week. If there’s a delay, the reviewer will comment on the PR to inform the author.

**2. Review Focus**

* Verify plugin name, description, and setup instructions are clear and instructive.
* Check if the plugin’s [Manifest](https://docs.dify.ai/plugins/schema-definition/manifest) file follows format specifications and includes valid author contact information.

**3. Plugin Functionality and Relevance**

* Test plugins according to [Plugin Development Guidelines](plugin-developer-guidelines.md).
* Ensure the plugin's purpose is reasonable within the Dify ecosystem.

[Dify.AI](https://dify.ai/) reserves the right to accept or reject plugin submissions.

***

### **Frequently Asked Questions**

1. **How do I know if my plugin is unique?**

Example: A Google search plugin that only adds language parameters should probably be submitted as an extension to an existing plugin. However, if the plugin implements significant functional improvements (like optimized batch processing or error handling), it can be submitted as a new plugin.

2. **What if my PR is marked as stale or closed?**

* A stale PR can be reopened once you’ve addressed the requested changes.
* A closed PR (over 30 days old) requires opening a new PR.

3. **Can I update my plugin during the beta test phase?**

Yes, but breaking changes should be avoided.
