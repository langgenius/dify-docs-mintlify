# Plugin Developer Guidelines

### Before Submitting a Pull Request (PR)

1. **Check Plugin's Functionality and Complete Documentation**

* Verify that the plugin works as intended.
* Provide a comprehensive **README file** including:
  * Setup and usage instructions
  * Required codes, APIs, credentials, or other information needed to connect the plugin to services
* Ensure collected user information is only used for service connectivity and plugin improvements.
* Prepare the plugin's privacy policy file or URL according to the [Plugin Privacy Protection Guidelines](plugin-developer-guidelines.md).

2. **Validate Plugin Value Proposition**

* Ensure your plugin provides unique value to Dify users.
* The plugin should introduce features or services not currently available in Dify or other plugins.
* Follow community standards:
  * Non-violent content that respects the global user base
  * Compliance with integrated service policies
* **How to Check for Similar Plugins?**
  * Avoid submitting functionality that duplicates existing plugins or PRs unless your plugin:
    * Introduces new features
    * Provides performance improvements
  * **Determining Plugin Uniqueness:**
    * If the plugin makes minor adjustments to existing functionality (like adding language parameters), consider extending the existing plugin.
    * If the plugin implements significant functional changes (like optimized batch processing or improved error handling), submit it as a new plugin.
    * Not sure? Include a brief explanation in your PR describing why a new plugin is needed.

**Example:**

Consider a Google Search plugin that takes a single input query and outputs Google search results using the Google Search API.

If you're offering a new Google Search plugin with similar underlying implementation but minor input adjustments (e.g., adding new language parameters), we recommend extending the existing plugin.

However, if you've implemented the plugin differently with optimized batch search capabilities and error handling, it may be reviewed as a separate plugin.


3. **Ensure Compliance with Privacy Data Standards**

**Information Disclosure Requirements:**

* Developers **must** declare whether they collect any type of user personal data when submitting applications/tools.
* If collecting data, **briefly list** the types of data collected (e.g., username, email, device ID, location information, etc.) - detailed explanations are not necessary.
* Developers **must** provide a privacy policy link that states what information is collected, how it's used, what information is shared with third parties, and links to third-party privacy policies.

**Review Focus:**

* **Format Review:** Check if data collection has been declared as required.
* **High-Risk Data Screening:** Focus on whether sensitive data is collected (e.g., health information, financial information, children's personal information). **Additional review** of usage purpose and security measures is required if sensitive data is collected.
* **Malicious Behavior Screening:** Check for obvious malicious behavior, such as collecting data without user consent or uploading user data to unknown servers.