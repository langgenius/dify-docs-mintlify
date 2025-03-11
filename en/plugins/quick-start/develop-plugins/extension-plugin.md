# Extension Plugin

This guide will help you quickly develop an Extension type plugin and understand the basic plugin development process.

### **Prerequisites**

* Dify plugin scaffolding tool
* Python environment, version ≥ 3.12

For detailed instructions on preparing the plugin development scaffolding tool, please refer to [Initializing Development Tools](initialize-development-tools.md).

### **Create New Project**

In the current path, run the CLI tool to create a new dify plugin project:

```bash
./dify-plugin-darwin-arm64 plugin init
```

If you have renamed the binary file to `dify` and copied it to the `/usr/local/bin` path, you can run the following command to create a new plugin project:

```bash
dify plugin init
```

### **Fill Plugin Information**

Follow the prompts to configure the plugin name, author information, and plugin description. If you're working in a team, you can also enter an organization name as the author.

> The plugin name must be 1-128 characters long and can only contain letters, numbers, hyphens, and underscores.

![Plugins detail](https://assets-docs.dify.ai/2024/12/75cfccb11fe31c56c16429b3998f2eb0.png)

Once filled out, select Python in the Plugin Development Language section.

![Plugins development: Python](https://assets-docs.dify.ai/2024/11/1129101623ac4c091a3f6f75f4103848.png)

### **3. Select Plugin Type and Initialize Project Template**

All templates in the scaffolding tool provide complete code projects. For demonstration purposes, this guide will use the `Extension` type plugin template as an example. For developers already familiar with plugin development, templates are not necessary, and you can refer to the interface documentation to complete different types of plugin development.

![Extension](https://assets-docs.dify.ai/2024/11/ff08f77b928494e10197b456fc4e2d5b.png)

#### **Configure Plugin Permissions**

The plugin needs permissions to access the Dify main platform for proper connection. The following permissions need to be granted for this example plugin:

* Tools
* LLMs
* Apps
* Enable persistent Storage with default size allocation
* Allow Endpoint registration

> Use arrow keys in the terminal to select permissions, and use the "Tab" key to grant permissions.

After checking all permission items, press Enter to complete the plugin creation. The system will automatically generate the plugin project code.

![Plugins permissions](https://assets-docs.dify.ai/2024/11/5518ca1e425a7135f18f499e55d16bdd.png)

The base file structure of the plugin contains the following:

```
.
├── GUIDE.md
├── README.md
├── _assets
│   └── icon.svg
├── endpoints
│   ├── your-project.py
│   └── your-project.yaml
├── group
│   └── your-project.yaml
├── main.py
├── manifest.yaml
└── requirements.txt
```

* `GUIDE.md`: A brief tutorial guide that leads you through the plugin writing process.
* `README.md`: Basic introduction about the current plugin. You need to fill this file with information about the plugin and its usage instructions.
* `_assets`: Stores all multimedia files related to the current plugin.
* `endpoints`: An `Extension` type plugin template created following the CLI guidance, this directory contains all implementation code for Endpoint functionality.
* `group`: Specifies key types, multilingual settings, and API definition file paths.
* `main.py`: The entry file for the entire project.
* `manifest.yaml`: The basic configuration file for the entire plugin, containing information such as required permissions and extension type.
* `requirements.txt`: Contains Python environment dependencies.

### Developing Plugins

#### **1. Define Plugin's Request Endpoint**

Edit `endpoints/test_plugin.yaml`, modifying it according to the following code:

```yaml
path: "/neko"
method: "GET"
extra:
  python:
    source: "endpoints/test_plugin.py"
```

This code defines the plugin's entry path as `/neko`, with a GET request method. The plugin's functionality implementation code is in the `endpoints/test_plugin.py` file.

#### **2. Write Plugin Functionality**

Plugin functionality: Request the plugin service to output a cat.

Write the plugin's implementation code in the `endpoints/test_plugin.py` file, referring to the following example code:

```python
from typing import Mapping
from werkzeug import Request, Response
from flask import Flask, render_template_string
from dify_plugin import Endpoint

app = Flask(__name__)

class NekoEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        ascii_art = '''
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛⬛️⬜️⬜️⬜️⬜️⬜⬜️⬜️️
🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧⬛️⬜️⬜️⬜️⬜️⬜⬜️️
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️🥧🥧🥧💟💟💟💟💟💟💟💟💟💟💟💟💟🥧🥧🥧⬛️⬜️⬜️⬜️⬜⬜️️
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️🥧🥧💟💟💟💟💟💟🍓💟💟🍓💟💟💟💟💟🥧🥧⬛️⬜️⬜️⬜️⬜️⬜️️
🟧🟧🟥🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟧🟥🟥🟥🟥🟥🟥🟥⬛🥧💟💟🍓💟💟💟💟💟💟💟💟💟💟💟💟💟💟🥧⬛️⬜️⬜️⬜️⬜⬜️️
🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛️🥧💟💟💟💟💟💟💟💟💟💟⬛️⬛️💟💟🍓💟💟🥧⬛️⬜️⬛️️⬛️️⬜⬜️️
🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛️🥧💟💟💟💟💟💟💟💟💟⬛️🌫🌫⬛💟💟💟💟🥧⬛️⬛️🌫🌫⬛⬜️️
🟨🟨🟧🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟨🟧⬛️⬛️⬛️⬛️🟧🟧⬛️🥧💟💟💟💟💟💟🍓💟💟⬛️🌫🌫🌫⬛💟💟💟🥧⬛️🌫🌫🌫⬛⬜️️
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛️🌫🌫⬛️⬛️🟧⬛️🥧💟💟💟💟💟💟💟💟💟⬛️🌫🌫🌫🌫⬛️⬛️⬛️⬛️🌫🌫🌫🌫⬛⬜️️
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛️⬛️🌫🌫⬛️⬛️⬛️🥧💟💟💟🍓💟💟💟💟💟⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛⬜️️
🟩🟩🟨🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩🟩🟨🟨⬛⬛️🌫🌫⬛️⬛️🥧💟💟💟💟💟💟💟🍓⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛️
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛️⬛️🌫🌫⬛️🥧💟🍓💟💟💟💟💟💟⬛️🌫🌫🌫⬜️⬛️🌫🌫🌫🌫🌫⬜️⬛️🌫🌫⬛️
️🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛️⬛️⬛️⬛️🥧💟💟💟💟💟💟💟💟⬛️🌫🌫🌫⬛️⬛️🌫🌫🌫⬛️🌫⬛️⬛️🌫🌫⬛️
🟦🟦🟩🟩🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦🟦🟩🟩🟩🟩🟩🟩⬛️⬛️🥧💟💟💟💟💟🍓💟💟⬛🌫🟥🟥🌫🌫🌫🌫🌫🌫🌫🌫🌫🟥🟥⬛️
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛️🥧🥧💟🍓💟💟💟💟💟⬛️🌫🟥🟥🌫⬛️🌫🌫⬛️🌫🌫⬛️🌫🟥🟥⬛️
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛️🥧🥧🥧💟💟💟💟💟💟💟⬛️🌫🌫🌫⬛️⬛️⬛️⬛️⬛️⬛️⬛️🌫🌫⬛️⬜️
🟪🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪🟪🟪🟪🟪🟪🟪🟪🟦🟦🟦🟦🟦🟦⬛️⬛️⬛️🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛️⬜️⬜️
🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛️🌫🌫🌫⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️
🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛️🌫🌫⬛️⬛️⬜️⬛️🌫🌫⬛️⬜️⬜️⬜️⬜️⬜️⬛️🌫🌫⬛️⬜️⬛️🌫🌫⬛️⬜️⬜️⬜️⬜️
⬜️⬜️🟪🟪🟪🟪🟪🟪🟪🟪⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟪🟪🟪🟪🟪⬛️⬛️⬛️⬛⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬜️️
        '''
        ascii_art_lines = ascii_art.strip().split('\n')
        with app.app_context():
            return Response(render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: black;
                color: white;
                overflow: hidden;
                margin: 0;
                padding: 0;
            }
            #ascii-art {
                font-family: monospace;
                white-space: pre;
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                display: inline-block;
                font-size: 16px;
                line-height: 1;
            }
        </style>
    </head>
    <body>
        <div id="ascii-art"></div>
        <script>
            var asciiArtLines = {{ ascii_art_lines | tojson }};
            var asciiArtDiv = document.getElementById("ascii-art");
            var index = 0;
            function displayNextLine() {
                if (index < asciiArtLines.length) {
                    var line = asciiArtLines[index];
                    var lineElement = document.createElement("div");
                    lineElement.innerHTML = line;
                    asciiArtDiv.appendChild(lineElement);
                    index++;
                    setTimeout(displayNextLine, 100);
                } else {
                    animateCat();
                }
            }
            function animateCat() {
                var pos = 0;
                var screenWidth = window.innerWidth;
                var catWidth = asciiArtDiv.offsetWidth;
                function move() {
                    asciiArtDiv.style.left = pos + "px";
                    pos += 2;
                    if (pos > screenWidth) {
                        pos = -catWidth;
                    }
                    requestAnimationFrame(move);
                }
                move();
            }
            displayNextLine();
        </script>
    </body>
    </html>
        ''', ascii_art_lines=ascii_art_lines), status=200, content_type="text/html")
```

The following Python dependencies need to be installed first to run this code:

```python
pip install werkzeug
pip install flask
pip install dify-plugin
```

### Debugging Plugins

Dify provides remote debugging method, go to "Plugin Management" page to get the debugging key and remote server address.

![](https://assets-docs.dify.ai/2024/12/053415ef127f1f4d6dd85dd3ae79626a.png)

Go back to the plugin project, copy the `.env.example` file and rename it to .env. Fill it with the remote server address and debugging key.

The `.env` file:

```bash
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=localhost
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=****-****-****-****-****
```

Run the `python -m main` command to launch the plugin. You can see on the plugin page that the plugin has been installed into Workspace. Other team members can also access the plugin.

![](https://assets-docs.dify.ai/2024/11/0fe19a8386b1234755395018bc2e0e35.png)

### Packing Plugin

After confirming that the plugin works properly, you can package and name the plugin with the following command line tool. After running it you can find the `neko.difypkg` file in the current folder, which is the final plugin package.

```
dify plugin package ./neko
```

Congratulations, you have completed the complete development, debugging and packaging process of a tool type plugin!

### Publishing Plugins

You can now publish your plugin by uploading it to the [Dify Plugins code repository](https://github.com/langgenius/dify-plugins)! Before uploading, make sure your plugin follows the [plugin release guide](../publish-plugins/publish-to-dify-marketplace.md). Once approved, the code will be merged into the master branch and automatically live in the [Dify Marketplace](https://marketplace.dify.ai/).

#### Exploring More

**Quick Start:**

* [Develop Extension Type Plugin](extension-plugin.md)
* [Develop Model Type Plugin](model-plugin/)
* [Bundle Type Plugin: Package Multiple Plugins](bundle.md)

**Plugins Specification Definition Documentaiton:**

* [Minifest](../schema-definition/manifest.md)
* [Endpoint](../schema-definition/endpoint.md)
* [Reverse Invocation of the Dify Service](../schema-definition/reverse-invocation-of-the-dify-service/)
* [Tools](../../guides/tools/)
* [Models](../schema-definition/model/model-schema.md)
* [Extend Agent Strategy](../schema-definition/agent.md)

**Best Practices:**

[Develop a Slack Bot Plugin](../../best-practice/develop-a-slack-bot-plugin.md)
