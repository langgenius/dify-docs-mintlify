# Plugin Privacy Protection Guidelines

When you are submitting your Plugin to Dify Marketplace, you are required to be transparent in how you handle user data. The following guidelines focus on how to address privacy-related questions and user data processing for your plugin.

Center your privacy policy around the following points:

**Does your plugin collect and use any user personal data?**  If it does, please list the types of data collected.

> “Personal data” refers to any information that can identify a specific individual—either on its own or when combined with other data—such as information used to locate, contact, or otherwise target a unique person.

#### 1. List the types of data collected

**Type A:** **Direct Identifiers**

* Name (e.g., full name, first name, last name)
* Email address
* Phone number
* Home address or other physical address
* Government-issued identification numbers (e.g., Social Security number, passport number, driver's license number)

**Type B**: **Indirect Identifiers**

* Device identifiers (e.g., IMEI, MAC address, device ID)
* IP address
* Location data (e.g., GPS coordinates, city, region)
* Online identifiers (e.g., cookies, advertising IDs)
* Usernames
* Profile pictures
* Biometric data (e.g., fingerprints, facial recognition data)
* Web browsing history
* Purchase history
* Health information
* Financial information

**Type C: Data that can be combined with other data to identify an individual:**

* Age
* Gender
* Occupation
* Interests

While your plugin may not collect any personal information, you also need to make sure the use of third-party services within your plugin may involve data collection or processing. As the plugin developer, you are responsible for disclosing all data collection activities associated within your plugin, including those performed by third-party services. Thus, make sure to read through the privacy policy of the third-party service and verify any data collected by your plugin is claimed in your submission.

For example, if the plugin you are developing involves Slack services, make sure to reference [Slack’s privacy policy](https://slack.com/trust/privacy/privacy-policy) in your plugin’s privacy policy statement and clearly disclose the data collection practices.

#### **2. Submit the most up to date Privacy Policy of your Plugin**

**The Privacy Policy** should contain:

* What types of data are collected.
* How the collected data is used.
* Whether any data is shared with third parties, and if so, identify those third parties and provide links to their privacy policies.
* If you have no clue of how to write a privacy policy, you can also check the privacy policy of Plugins issued by Dify Team.

#### 3. Introducing a privacy policy statement within the plugin Manifest file

For detailed instructions on filling out specific fields, please refer to the [Manifest](https://docs.dify.ai/plugins/schema-definition/manifest) documentation.

**FAQ**

1. **What does "collect and use" mean regarding user personal data? Are there any common examples of how personal data is collected and used in any Plugin?**

"Collect and use" user data generally refers to the collection, transmission, use, or sharing of user data. Common examples of how products may handle personal or sensitive user data include:

* Using forms that gather any kind of personally identifiable information.
* Implementing login features, even when using third-party authentication services.
* Collecting information about input or resources that may contain personally identifiable information.
* Implementing analytics to track user behavior, interactions, and usage patterns.
* Storing communication data like messages, chat logs, or email addresses.
* Accessing user profiles or data from connected social media accounts.
* Collecting health and fitness data such as activity levels, heart rate, or medical information.
* Storing search queries or tracking browsing behavior.
* Processing financial information including bank details, credit scores, or transaction history.
