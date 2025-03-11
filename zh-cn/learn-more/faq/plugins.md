# 插件

> 以下常见问题与解决办法仅适用于 `1.0.0` 社区版本。

### 安装插件时遇到异常应如何处理？

问题描述：安装插件时遇到异常信息：`plugin verification has been enabled, and the plugin you want to install has a bad signature`，应该如何处理？

解决办法：在 `.env` 配置文件的末尾添加 `FORCE_VERIFYING_SIGNATURE=false` 字段即可解决该问题。添加该字段后，Dify 平台将允许安装所有未在 Dify Marketplace 上架（审核）的插件，可能存在安全隐患。

建议在测试 / 沙箱环境内安装插件，确认安全后再安装至生产环境。
