---
description: 'Author: Allen'
---

# 常见问题

## 安装插件时提示上传失败如何处理？

**错误详情**：出现 `PluginDaemonBadRequestError: plugin_unique_identifier is not valid` 报错提示。

**解决办法**：将插件项目下的 `manifest.yaml` 文件和 `/provider` 路径下的 `.yaml` 文件中的 `author` 字段修改为 GitHub ID。

重新运行插件打包命令并安装新的插件包。

## 安装插件时遇到异常应如何处理？

**问题描述**：安装插件时遇到异常信息：`plugin verification has been enabled, and the plugin you want to install has a bad signature`，应该如何处理？

**解决办法**：在 `/docker/.env` 配置文件的末尾添加 `FORCE_VERIFYING_SIGNATURE=false` 字段，运行以下命令重启 Dify 服务：

```bash
cd docker
docker compose down
docker compose up -d
```

添加该字段后，Dify 平台将允许安装所有未在 Dify Marketplace 上架（审核）的插件，可能存在安全隐患。

建议在测试 / 沙箱环境内安装插件，确认安全后再安装至生产环境。
