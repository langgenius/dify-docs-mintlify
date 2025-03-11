# Package the Plugin File and Publish it

After completing plugin development, you can package your plugin project as a local file and share it with others. Once the plugin file is obtained, it can be installed into a Dify Workspace. This guide will show you how to package a plugin project as a local file and how to install plugins using local files.

### **Prerequisites**

You'll need the Dify plugin development scaffolding tool for packaging plugins. Visit the Github project page to select and download the version for your operating system.

Using **macOS with M-series chips** as an example, download the `dify-plugin-darwin-arm64` file, then navigate to the file's location in terminal and grant execution permissions:

```bash
chmod +x dify-plugin-darwin-arm64
```

For global use of the scaffolding tool, it's recommended to rename the binary file to `dify` and copy it to the `/usr/local/bin` system path.

After configuration, enter the `dify version` command in terminal to verify version number output.

### **Packaging Plugins**

After completing plugin project development, ensure remote connection testing is done. To package plugins, navigate to the parent directory of your plugin project and run the following packaging command:

```bash
cd ../
dify plugin package ./your_plugin_project
```

After running the command, a file with `.difypkg` extension will be generated in the current path.

![](https://assets-docs.dify.ai/2024/12/98e09c04273eace8fe6e5ac976443cca.png)

### **Installing Plugins**

Visit the Dify plugin management page, click **Install Plugin** → **Install via Local File** in the top right corner, or drag and drop the plugin file to a blank area of the page to install.

![](https://assets-docs.dify.ai/2024/12/8c31c4025a070f23455799f942b91a57.png)

### **Publishing Plugins**

You can share the plugin file with others or upload it to the internet for download.
