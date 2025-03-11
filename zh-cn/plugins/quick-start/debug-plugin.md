# 插件调试

插件开发完成后，接下来需要测试插件是否可以正常运行。Dify 提供便捷地远程调试方式，帮助你快速在测试环境中验证插件功能。

前往[“插件管理”](https://cloud.dify.ai/plugins)页获取远程服务器地址和调试 Key。

![](https://assets-docs.dify.ai/2024/12/053415ef127f1f4d6dd85dd3ae79626a.png)

回到插件项目，拷贝 `.env.example` 文件并重命名为 `.env`，将获取的远程服务器地址和调试 Key 等信息填入其中。

`.env` 文件：

```bash
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=localhost
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=****-****-****-****-****
```

运行 `python -m main` 命令启动插件。在插件页即可看到该插件已被安装至 Workspace 内，团队中的其他成员也可以访问该插件。

![](https://assets-docs.dify.ai/2024/12/ec26e5afc57bbfeb807719638f603807.png)
