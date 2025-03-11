# Upgrading Community Edition to v1.0.0

> This document primarily explains how to upgrade from an older Community Edition version to [v1.0.0](https://github.com/langgenius/dify/releases/tag/1.0.0). If you have not installed the Dify Community Edition yet, you can directly clone the [Dify project](https://github.com/langgenius/dify) and switch to the `1.0.0` branch. For installation commands, refer to the [documentation](https://docs.dify.ai/zh-hans/getting-started/install-self-hosted/docker-compose).

To experience the plugin functionality in the Community Edition, you need to upgrade to version`v1.0.0`. This document will guide you through the steps of upgrading from older versions to `v1.0.0` to access the plugin ecosystem features.

## Start the Upgrade

The upgrade process involves the following steps:

1. Backup your data
2. Migrate plugins
3. Upgrade the main dify project

### 1. Backup Data

1.1 Execute the `cd` command to navigate to your Dify project directory and create a backup branch.

1.2 Run the following command to back up your docker-compose YAML file (optional).

```bash
cd docker
cp docker-compose.yaml docker-compose.yaml.$(date +%s).bak
```

1.3 Run the command to stop docker services, then execute the backup data command in the Docker directory.

```bash
docker compose down
tar -cvf volumes-$(date +%s).tgz volumes
```

### 2. Upgrade the Version

`v1.0.0` supports deployment via Docker Compose. Navigate to your Dify project path and run the following commands to upgrade to the Dify version:

```bash
git fetch origin
git checkout 1.0.0 # Switch to the 1.0.0 branch
cd docker
nano .env # Modify the environment configuration file to synchronizing .env.example file
docker compose -f docker-compose.yaml up -d
```

### 3. Migrate Tools to Plugins

The purpose of this step is to automatically migrate the tools and model vendors previously used in the Community Edition and install them into the new plugin environment.

1.	Run the docker ps command to check the docker-api container ID.

Example:

```bash
docker ps
CONTAINER ID   IMAGE                                       COMMAND                  CREATED       STATUS                 PORTS                                                                                                                             NAMES
417241cd****   nginx:latest                                "sh -c 'cp /docker-e…"   3 hours ago   Up 3 hours             0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp                                                          docker-nginx-1
f84aa773****   langgenius/dify-api:1.0.0                   "/bin/bash /entrypoi…"   3 hours ago   Up 3 hours             5001/tcp                                                                                                                          docker-worker-1
a3cb19c2****   langgenius/dify-api:1.0.0                   "/bin/bash /entrypoi…"   3 hours ago   Up 3 hours             5001/tcp                                                                                                                          docker-api-1
```

Run the command `docker exec -it a3cb19c2**** bash` to enter the container terminal, and then run:

```bash
poetry run flask extract-plugins --workers=20
```

> If an error occurs, it is recommended to first install the `poetry` environment on the server as per the prerequisites. If the terminal asks for input after running the command, press **“Enter”** to skip the input.

This command will extract all models and tools currently in use in the environment. The workers parameter controls the number of parallel processes used during extraction and can be adjusted as needed. After the command runs, it will generate a `plugins.jsonl` file containing plugin information for all workspaces in the current Dify instance.

Ensure your network can access the public internet and support access to: `https://marketplace.dify.ai`. Continue running the following command in the `docker-api-1` container:

```bash
poetry run flask install-plugins --workers=2
```

This command will download and install all necessary plugins into the latest Community Edition. When the terminal shows `Install plugins completed.`, the migration is complete.

## Verify the Migration

Access the Dify platform and click the **“Plugins”** button in the upper-right corner to check if the previously used tools have been correctly installed. Randomly use one of the plugins to verify if it works properly. If the plugins work well, the version upgrade and data migration have been successfully completed.
