# Debug Plugin



Once plugin development is complete, the next step is to test whether the plugin runs correctly. Dify provides remote debugging method.

Go to ["Plugin"](https://cloud.dify.ai/plugins) page to get the debugging key and remote URL.

![](https://assets-docs.dify.ai/2024/11/1cf15bc59ea10eb67513c8bdca557111.png)

Go back to the plugin project, copy the `.env.example` file and rename it to `.env`. Fill it with the remote server address and debug key.

`.env` file

```bash
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=remote-url
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=****-****-****-****-****
```

Run the `python -m main` command to start the plugin. You can see on the plugin page that the plugin has been installed into Workspace. Other team members can also access the plugin.

![](https://assets-docs.dify.ai/2024/12/e11acb42ccb23c824f400b7e19fb2952.png)

You can initialize this model provider by entering the API Key in **Settings → Model Provider**.

![](https://assets-docs.dify.ai/2024/12/662de537d70a3607c240a05294a9f3e1.png)
