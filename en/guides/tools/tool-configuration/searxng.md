# SearXNG

{% hint style="warning" %}
"Tools" has been fully upgraded to the "Plugins". For more details, please refer to [Install and Use Plugins](https://docs.dify.ai/plugins/quick-start/install-plugins). The content below has been archived.
{% endhint %}

SearXNG is a free internet metasearch engine which aggregates results from various search services and databases. Users are neither tracked nor profiled. Now you can use this tool directly in Dify.

Below are the steps for integrating SearXNG into Dify using Docker in the [Community Edition](https://docs.dify.ai/getting-started/install-self-hosted/docker-compose).

> If you want to use SearXNG within the Dify cloud service, please refer to the [SearXNG installation documentation](https://docs.searxng.org/admin/installation.html) to set up your own service, then return to Dify and fill in the service's Base URL in the "Tools > SearXNG > Authenticate" page.

## 1. Modify Dify Configuration File

The configuration file is located at `dify/api/core/tools/provider/builtin/searxng/docker/settings.yml`, and you can refer to the config documentation [here](https://docs.searxng.org/admin/settings/index.html).

## 2. Start the Service

Start the Docker container in the dify root directory.

```bash
cd dify
docker run --rm -d -p 8081:8080 -v "${PWD}/api/core/tools/provider/builtin/searxng/docker:/etc/searxng" searxng/searxng
```

## 3. Use SearXNG

Fill in the access address in "Tools > SearXNG > Authenticate" to establish a connection between the Dify service and the SearXNG service. The Docker internal address for SearXNG is usually `http://host.docker.internal:8081`.
