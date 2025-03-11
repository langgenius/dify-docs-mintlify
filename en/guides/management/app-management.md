# App Management

### Editing Application Information

After creating an application, if you want to modify the application name or description, you can click "Edit info" in the upper left corner of the application to revise the application's icon, name, or description.

![Edit App Info](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/63a449e9a8ae337b9c067165d1674a45.png)

### Duplicating Application

All applications support copying. Click "Duplicate" in the upper left corner of the application.

### Exporting Application

Applications created in Dify support export in DSL format files, allowing you to import the configuration files into other Dify teams freely. You can export DSL files using either of the following two methods:

* Click "Export DSL" in the application menu button on the "Studio" page
* After entering the application's orchestration page, click "Export DSL" in the upper left corner

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/544c18d770e230db93d6756bba98d8a7.png)

The DSL file does not include authorization information already filled in [Tool](../workflow/node/tools.md) nodes, such as API keys for third-party services.

If the environment variables contain variables of the `Secret` type, a prompt will appear during file export asking whether to allow the export of this sensitive information.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/25ce002ef7f0392fc6b3b6975ae137ec.png)

{% hint style="info" %}
Dify DSL is an AI application engineering file standard defined by Dify.AI in v0.6 and later. The file format is YML. This standard covers the basic description of the application, model parameters, orchestration configuration, and other information.
{% endhint %}

### Importing Application

To import a Dify application, upload the DSL file to the Dify platform. A version check will be conducted during the import process, and a warning will be issued if a lower version of the DSL file is detected.

- For SaaS users, the DSL file exported from the SaaS platform will always be the latest version.
- For Community users, it is recommended to consult [Upgrade Dify](https://docs.dify.ai/getting-started/install-self-hosted/docker-compose#upgrade-dify) to update the Community Edition and export an updated version of the DSL file, thus avoiding potential compatibility issues.

![](https://assets-docs.dify.ai/2024/11/487d2c1cc8b86666feb35ea8a346c053.png)

### Deleting Application

If you want to remove an application, you can click "Delete" in the upper left corner of the application.

{% hint style="info" %}
⚠️ The deletion of an application cannot be undone. All users will be unable to access your application, and all prompts, orchestration configurations, and logs within the application will be deleted.
{% endhint %}
