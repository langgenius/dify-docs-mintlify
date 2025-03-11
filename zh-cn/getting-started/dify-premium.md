# Dify Premium

Dify Premium 是一款 [AWS AMI](https://docs.aws.amazon.com/zh\_cn/AWSEC2/latest/UserGuide/ec2-instances-and-amis.html) 产品，允许自定义品牌，并可作为 EC2 一键部署到你的 AWS VPC 上。前往 [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-t22mebxzwjhu6) 进行订阅并使用，它适合以下场景：

* 在中小型企业内，需在服务器上创建一个或多应用程序，并且关心数据私有化。
* 你对 [Dify Cloud](https://docs.dify.ai/v/zh-hans/getting-started/cloud)订阅计划感兴趣，但所需的用例资源超出了[计划](https://dify.ai/pricing)内所提供的资源。
* 你希望在组织内采用 Dify Enterprise 之前进行 POC 验证。

## 设置

如果这是你第一次访问 Dify，请输入管理员初始化密码（设置为你的 EC2 实例 ID）以开始设置过程。

部署 AMI 后，通过 EC2 控制台中找到的实例公有 IP 访问 Dify（默认使用 HTTP 端口 80）。

## 升级

在 EC2 实例中，运行以下命令：

```bash
git clone https://github.com/langgenius/dify.git /tmp/dify
mv -f /tmp/dify/docker/* /dify/
rm -rf /tmp/dify
docker-compose down
docker-compose pull
docker-compose -f docker-compose.yaml -f docker-compose.override.yaml up -d
```

<details>

<summary>将版本升级至 v1.0.0</summary>

> 版本 v1.0.0 包含插件功能，详细介绍请参考[此处](https://github.com/langgenius/dify/releases/tag/1.0.0)。

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
git checkout 1.0.0 # 切换至 1.0.0 分支
cd docker
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

</details>

## 定制化

就像自托管部署一样，你可以根据需要修改 EC2 实例中 `.env` 下的环境变量。然后使用以下命令重新启动 Dify：

```
docker-compose down
docker-compose -f docker-compose.yaml -f docker-compose.override.yaml up -d
```
