# SearXNG

> 工具作者 @Junytang。

{% hint style="warning" %}
“工具”已全面升级为“插件”生态，详细的使用说明请参考[插件开发](https://docs.dify.ai/zh-hans/plugins/quick-start/install-plugins)。以下内容已归档。
{% endhint %}

SearXNG 是一个免费的互联网元搜索引擎，整合了各种搜索服务的检索结果。用户不会被跟踪，搜索行为也不会被分析。现在你可以直接在 Dify 中使用此工具。

下文将介绍如何在[社区版](https://docs.dify.ai/v/zh-hans/getting-started/install-self-hosted/docker-compose)使用 Docker 将 SearXNG 集成到 Dify。

> 如果你想在 Dify 云服务内使用 SearXNG，请参考[ SearXNG 安装文档](https://docs.searxng.org/admin/installation.html)自建服务，然后回到 Dify，在 "工具 > SearXNG > 去认证" 页填写服务的 Base URL。

## 1. 修改 Dify 配置文件

SearXNG 的配置文件位于 `dify/api/core/tools/provider/builtin/searxng/docker/settings.yml`， 配置文档可参考[这里](https://docs.searxng.org/admin/settings/index.html)。

你可以按需修改配置，也可直接使用默认配置。

## 2. 启动服务

在 Dify 根目录下启动 Docker 容器。

```bash
cd dify
docker run --rm -d -p 8081:8080 -v "${PWD}/api/core/tools/provider/builtin/searxng/docker:/etc/searxng" searxng/searxng
```

## 3. 使用 SearXNG

在 `工具 > SearXNG > 去认证` 中填写访问地址，建立 Dify 服务与 SearXNG 服务的连接。SearXNG 的 Docker 内网地址一般是 `http://host.docker.internal:8081`。
