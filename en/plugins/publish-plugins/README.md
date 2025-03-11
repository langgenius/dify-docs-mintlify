# Publish Plugins

### Publish Methods

To accommodate the various publishing needs of developers, Dify provides three plugin publish methods:

#### **1. Marketplace**

**Introduction**: The official Dify plugin marketplace allows users to browse, search, and install a variety of plugins with just one click.

**Features**:

* Plugins become available after passing a review, ensuring they are **trustworthy** and **high-quality**.
* Can be installed directly into an individual or team **Workspaces**.

**Publication Process**:

* Submit the plugin project to the **Dify Marketplace** [code repository](https://github.com/langgenius/dify-plugins).
* After an official review, the plugin will be publicly released in the marketplace for other users to install and use.

For detailed instructions, please refer to:

{% content-ref url="publish-to-dify-marketplace/" %}
[publish-to-dify-marketplace](publish-to-dify-marketplace/)
{% endcontent-ref %}

#### 2. **GitHub Repository**

**Introduction**: Open-source or host the plugin on **GitHub** makes it easy for others to view, download, and install.

**Features**:

* Convenient for **version management** and **open-source sharing**.
* Users can install the plugin directly via a link, bypassing platform review.

**Publication Process**:

* Push the plugin code to a GitHub repository.
* Share the repository link, users can integrate the plugin into their **Dify Workspace** through the link.

For detailed instructions, please refer to:

{% content-ref url="publish-plugin-on-personal-github-repo.md" %}
[publish-plugin-on-personal-github-repo.md](publish-plugin-on-personal-github-repo.md)
{% endcontent-ref %}

#### Plugin File (Local Installation)

**Introduction**: Package the plugin as a local file (e.g., `.difypkg` format) and share it for others to install.

**Features**:

* Does not depend on an online platform, enabling **quick and flexible** sharing of plugins.
* Suitable for **private plugins** or **internal testing**.

**Publication Process**:

* Package the plugin project as a local file.
* Click **Upload Plugin** on the Dify plugin page and select the local file to install the plugin.

You can package the plugin project as a local file and share it with others. After uploading the file on the plugin page, the plugin can be installed into the Dify Workspace.

For detailed instructions, please refer to:

{% content-ref url="package-plugin-file-and-publish.md" %}
[Package as Local File and Share](package-plugin-file-and-publish.md)
{% endcontent-ref %}

### **Publication Recommendations**

* **Looking to promote a plugin** → **Recommended to use the Marketplace**, ensuring plugin quality through official review and increasing exposure.
* **Open-source sharing project** → **Recommended to use GitHub**, convenient for version management and community collaboration.
* **Quick distribution or internal testing** → **Recommended to use plugin file**, allowing for straightforward and efficient installation and sharing.