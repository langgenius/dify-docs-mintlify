# Bulletin: Image Upload Replaced by File Upload

The image upload feature has been integrated into the more comprehensive [File Upload](file-upload.md) functionality. To avoid redundant features, we have decided to upgrade and adjust the “[Features](additional-features.md)” for Workflow and Chatflow applications as follows:

* The image upload option in Chatflow’s “Features” has been removed and replaced by the new “File Upload” feature. Within the “File Upload” feature, you can select the image file type. Additionally, the image upload icon in the application dialog has been replaced with a file upload icon.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/edeb9bfe8cafc8c7fa242bf895dfb850.png)

* The image upload option in Workflow’s “Features” and the `sys.files` [variable](variables.md) will be deprecated in the future. Both have been marked as `LEGACY`, and developers are encouraged to use custom file variables to add file upload functionality to Workflow applications.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/df9f74f5362f31672ebe3a166f0a419a.png)

### Why Replace the “Image Upload” Feature?

Previously, Dify only supported image file uploads. In the latest version, a more comprehensive file upload capability has been introduced, supporting documents, images, audio, video, and custom file formats.

**Image uploading is now part of the broader “File Upload” feature.** When adding the file upload feature, developers can simply check the “image” file type to enable image uploads.

To avoid confusion caused by redundant features, we have decided to replace the standalone image upload feature in Chatflow applications with the more comprehensive file upload capability, and no longer recommend enabling image upload for Workflow applications.

### More Comprehensive Functionality: File Upload

To enhance the information processing capabilities of your applications, we have introduced the “File Upload” feature in this update. Unlike chat text, document files can carry a large amount of information, such as academic reports or legal contracts.

* The file upload feature allows files to be uploaded, parsed, referenced, and downloaded as file variables within Workflow applications.
* Developers can now easily build applications capable of understanding and processing complex tasks involving images, audio, and video.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/05bf5ca6ea2f384cc171e3041a6f0751.png)

We no longer recommend using the standalone “Image Upload” feature and instead suggest transitioning to the more comprehensive “File Upload” feature to improve the application experience.

### What You Need to Do?

#### For Dify Cloud Users: 

* **Chatflow Applications**

If you have already created Chatflow applications with the “Image Upload” feature enabled and activated the Vision feature in the LLM node, the system will automatically switch the feature, and it will not affect the application’s image upload capability. If you need to update and republish the application, select the file variable in the Vision variable selection box of the LLM node, clear the item from the checklist, and republish the application.\


![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/bc6e9e3a57844f5f1e50b4716592449d.png)

If you wish to add the “Image Upload” feature to a Chatflow application, enable “File Upload” in the features and select only the “image” file type. Then enable the Vision feature in the LLM node and specify the sys.files variable. The upload entry will appear as a “paperclip” icon. For detailed instructions, refer to [Additional Features](additional-features.md).

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/d8c447886a9bdea1aeeda8991b46742e.png)

* **Workflow Applications**

If you have already created Workflow applications with the “Image Upload” feature enabled and activated the Vision feature in the LLM node, this change will not affect you immediately, but you will need to complete manual migration before the official deprecation.

If you wish to enable the “Image Upload” feature for a Workflow application, add a file variable in the [Start](node/start.md) node. Then, reference this file variable in subsequent nodes instead of using the `sys.files` variable.

#### For Dify Community Edition or Self-hosted Enterprise Users:

After upgrading to version v0.10.0, you will see the “File Upload” feature.

* Chatflow Applications:

Chatflow applications with the “Image Upload” feature enabled will automatically switch to the file upload feature, with no changes required.

If you wish to add the “Image Upload” feature to a Chatflow application, refer to the Additional Features section for detailed instructions.

* Workflow Applications:

Existing Workflow applications will not be affected, but please complete the manual migration before the official deprecation.

If you wish to enable the “Image Upload” feature for a Workflow application, add a file variable in the [Start](node/start.md) node. Then, reference this file variable in subsequent nodes instead of using the `sys.files` variable.\

### FAQs:

#### 1. Will This Update Affect My Existing Applications?

* Existing Chatflow applications will automatically migrate, seamlessly switching image upload capabilities to the file upload feature. The `sys.files` variable will still be used as the default Vision input. The image upload entry in the application interface will be replaced with a file upload entry.
* Existing Workflow applications will not be affected for now. The `sys.files` variable and the image upload feature have been marked as `LEGACY`, but they can still be used. However, these `LEGACY` features will be deprecated in the future, and a manual update will be required at that time.

#### 2. Do I Need to Update My Applications Immediately?

* For Chatflow applications, the system will automatically migrate, and no manual updates are required.
* For Workflow applications, although an immediate update is not necessary, we recommend familiarizing yourself with the new file upload feature to prepare for future migration.

#### 3. How Can I Ensure My Applications Are Compatible with the New File Upload Feature?

For Chatflow applications:

• Check if the file upload option is enabled in the features configuration.

• Ensure you’re using an LLM with Vision capabilities, and turn on the Vision toggle.

• Verify that `sys.files` is correctly selected as the input item in the Vision box.

\
For Workflow applications:

• Create a file-type variable in the “Start” node.

• Reference this file variable in subsequent nodes instead of using the LEGACY `sys.files` variable.

#### 4. How to handle missing image upload icons in previously published Chatflow applications?

It is recommended to republish the application, and the file upload icon will appear in the application's chat box.

#### We Value Your Feedback

As a key member of the Dify community, your experience and feedback are crucial to us. We warmly invite you to:

1. Try the file upload feature and experience its convenience and flexibility.
2.  Share your thoughts and suggestions via the following channels:

    • [GitHub](https://github.com/langgenius/dify)

    • [Discord channel](https://discord.com/invite/FngNHpbcY7)

Your feedback will help us continuously improve the product and provide a better experience for the entire community.
