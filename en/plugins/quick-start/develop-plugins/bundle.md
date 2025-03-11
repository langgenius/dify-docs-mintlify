# Bundle

A Bundle plugin package is a collection of multiple plugins. It can package multiple plugins into one plugin to achieve batch installation effects while providing more powerful services.

You can package multiple plugins into a Bundle using the Dify CLI tool. Bundle plugin packages offer three types:

* `Marketplace` type: Stores plugin IDs and version information. During import, specific plugin packages are downloaded through the Dify Marketplace.
* `GitHub` type: Stores GitHub repository address, release version number, and asset filename. During import, Dify accesses the corresponding GitHub repository to download plugin packages.
* `Package` type: Plugin packages are stored directly in the Bundle. It doesn't store reference sources but may cause large Bundle package sizes.

### **Prerequisites**

* Dify plugin scaffolding tool
* Python environment, version ≥ 3.10;

For detailed instructions on preparing the plugin development scaffolding tool, please refer to [Initializing Development Tools](initialize-development-tools.md).

### **Create Bundle Project**

In the current path, run the scaffolding command-line tool to create a new plugin package project:

```bash
./dify-plugin-darwin-arm64 bundle init
```

#### **1. Enter Plugin Information**

Follow the prompts to configure plugin name, author information, and plugin description. If you're working in a team, you can also enter an organization name as the author.

> The name must be 1-128 characters long and can only contain letters, numbers, hyphens, and underscores.

![Bundle basic informatio](https://assets-docs.dify.ai/2024/12/03a1c4cdc72213f09523eb1b40832279.png)

Fill in the information and hit enter, the Bundle plugin project directory will be created automatically.

![](https://assets-docs.dify.ai/2024/12/356d1a8201fac3759bf01ee64e79a52b.png)

#### **2. Add Dependencies**

* **Marketplace**

Execute the following command:

```bash
dify-plugin bundle append marketplace . --marketplace_pattern=langgenius/openai:0.0.1
```

Where marketplace\_pattern is the plugin reference in the marketplace, format: organization-name/plugin-name:version

* **Github**

Execute the following command:

```bash
dify-plugin bundle append github . --repo_pattern=langgenius/openai:0.0.1/openai.difypkg
```

Where repo\_pattern is the plugin reference in github, format: `organization-name/repository-name:release/attachment-name`

* **Package**

Execute the following command:

```bash
dify-plugin bundle append package . --package_path=./openai.difypkg
```

Where package\_path is the plugin package directory.

### **Package Bundle Project**

Run the following command to package the Bundle plugin:

```bash
dify-plugin bundle package ./bundle
```

After executing the command, a bundle.difybndl file will be automatically created in the current directory, which is the final packaging result.
