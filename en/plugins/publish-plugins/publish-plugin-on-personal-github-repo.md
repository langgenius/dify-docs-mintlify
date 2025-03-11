# Publish to Your Personal GitHub Repository

You can install plugins through GitHub repository links. After developing a plugin, you can choose to publish it to a public GitHub repository for others to download and use. This method offers the following advantages:

• **Personal Management**: Complete control over plugin code and updates

• **Quick Sharing**: Easily share with other users or team members via GitHub links for testing and use

• **Collaboration and Feedback**: Open-sourcing your plugin may attract potential collaborators on GitHub who can help improve it quickly

This guide will show you how to publish plugins to a GitHub repository.

### **Prerequisites**

* GitHub account
* New public GitHub repository
* Git tools installed locally

For basic GitHub knowledge, please refer to [GitHub documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

### **1. Prepare Plugin Project**

Publishing to public GitHub means your plugin will be open source. Ensure you've completed debugging and verification, and have a comprehensive `README.md` file.

Recommended README contents:

* Plugin introduction and feature description
* Installation and configuration steps
* Usage examples
* Contact information or contribution guidelines

### **2. Initialize Local Plugin Repository**

Before publishing to GitHub, ensure debugging and verification are complete. Navigate to the plugin project folder in terminal and run:

```bash
git init
git add .
git commit -m "Initial commit: Add plugin files"
```

If this is your first time using Git, you may also need to configure your Git username and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### **3. Connect Remote Repository**

Use this command to connect local repository to GitHub:

```bash
git remote add origin https://github.com/<your-username>/<repository-name>.git
```

### **4. Upload Plugin Files**

Push project to GitHub repository:

```bash
git branch -M main
git push -u origin main
```

Recommended to add tags for future packaging:

```bash
git tag -a v0.0.1 -m "Release version 0.0.1"
git push origin v0.0.1
```

### **5. Package Plugin Code**

Go to the Releases page of your GitHub repository and create a new release. Upload plugin files when publishing. For detailed instructions on packaging plugins, please read the packaging plugins documentation.

![Packaging Plugins](https://assets-docs.dify.ai/2024/12/5cb4696348cc6903e380287fce8f529d.png)

### **Installing Plugins via GitHub**

Others can install the plugin using the GitHub repository address. Visit the Dify platform's plugin management page, choose to install via GitHub, enter the repository address, select version number and package file to complete installation.

![](https://assets-docs.dify.ai/2024/12/3c2612349c67e6898a1f33a7cc320468.png)

