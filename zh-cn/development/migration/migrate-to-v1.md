# 将社区版升级至 v1.0.0

> 本文主要介绍如何将旧社区版本升级为 [v1.0.0](https://github.com/langgenius/dify/releases/tag/1.0.0)。如果你未曾安装过 Dify 社区版，可以直接克隆 [Dify 项目](https://github.com/langgenius/dify)，并切换至 `1.0.0` 分支。参考[文档](https://docs.dify.ai/zh-hans/getting-started/install-self-hosted/docker-compose)执行安装命令。

如需在社区版中体验插件功能，需要将版本号升级为 `v1.0.0`。本文将为你介绍如何从旧版本升级至 `v1.0.0` 以体验插件生态功能。

## 开始升级

升级分为以下步骤：

1. 备份数据
2. 插件迁移
3. 主项目升级

### 1. 备份数据

1.1 运行 `cd` 命令至你的 Dify 项目路径，新建备份分支。

1.2 运行以下命令，备份你的 docker-compose YAML 文件（可选）。

```bash
cd docker
cp docker-compose.yaml docker-compose.yaml.$(date +%s).bak
```

1.3 运行命令停止服务，在 Docker 目录中执行备份数据命令。

```bash
docker compose down
tar -cvf volumes-$(date +%s).tgz volumes
```

### 2. 升级版本

`v1.0.0` 支持通过 Docker Compose 部署。运行 `cd` 命令至你的 Dify 项目路径，运行以下命令升级 Dify 版本：

```bash
git fetch origin
git checkout 1.0.0 # 切换至 1.0.0 分支
cd docker
nano .env # 修改环境配置文件同步 .env.example 文件
docker compose -f docker-compose.yaml up -d
```

### 3. 工具迁移为插件
 
该步骤的目的：将此前社区版本所使用的工具及模型供应商，自动进行数据迁移并安装至新版本的插件环境中。

1. 运行 docker ps 命令，查看 docker-api 容器 id 号。

示例：

```bash
docker ps
CONTAINER ID   IMAGE                                       COMMAND                  CREATED       STATUS                 PORTS                                                                                                                             NAMES
417241cd****   nginx:latest                                "sh -c 'cp /docker-e…"   3 hours ago   Up 3 hours             0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp                                                          docker-nginx-1
f84aa773****   langgenius/dify-api:1.0.0                   "/bin/bash /entrypoi…"   3 hours ago   Up 3 hours             5001/tcp                                                                                                                          docker-worker-1
a3cb19c2****   langgenius/dify-api:1.0.0                   "/bin/bash /entrypoi…"   3 hours ago   Up 3 hours             5001/tcp                                                                                                                          docker-api-1
```

运行命令 `docker exec -it a3cb19c2**** bash` 进入容器终端，在容器内运行：

```bash
poetry run flask extract-plugins --workers=20
```

> 如果提示报错，建议参考前置准备，先在服务器内安装 `poetry` 环境；运行命令后，若终端出现待输入项，点击 **“回车”** 跳过输入。

此命令将提取当前环境中使用的所有模型和工具。workers 参数将决定提取过程中的所使用的并行进程数，可根据需要进行调整。命令运行完成后将生成 `plugins.jsonl` 文件保存结果，该文件包含了当前 Dify 实例中所有工作区的插件信息。

确保你的网络正常访问公网，并支持访问：`https://marketplace.dify.ai`。在 `docker-api-1` 容器内继续运行以下命令：

```bash
poetry run flask install-plugins --workers=2
```

此命令将下载并安装所有必要的插件到最新的社区版本中。当终端出现 `Install plugins completed.` 标识时，迁移完成。

## 验证结果

访问 Dify 平台，轻点右上角 **“插件”** 查看此前所使用的工具是否被正确安装。随机使用某个插件，验证是否能够正常运行。如果无误，说明你已完成版本升级和数据迁移。

![](https://assets-docs.dify.ai/2025/02/6467b3578d3d3e96510f50a09442d5a5.png)
