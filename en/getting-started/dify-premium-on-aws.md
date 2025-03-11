# Dify Premium on AWS

Dify Premium is our AWS AMI offering that allows custom branding and is one-click deployable to your AWS VPC as an EC2. Head to [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-t22mebxzwjhu6) to subscribe. It's useful in a couple of scenarios:

* You're looking to create one or a few applications as a small/medium business and you care about data residency.
* You are interested in [Dify Cloud](cloud.md), but your use case require more resource than supported by the [plans](https://dify.ai/pricing).
* You'd like to run a POC before adopting Dify Enterprise within your organization.

## Setup

If this is your first time accessing Dify, enter the Admin initialization password (set to your EC2's instance ID) to start the set up process.

After the AMI is deployed, access Dify via the instance's public IP found in th EC2 console (HTTP port 80 is used by default).

## Upgrading

In the EC2 instance, run the following commands:

```
git clone https://github.com/langgenius/dify.git /tmp/dify
mv -f /tmp/dify/docker/* /dify/
rm -rf /tmp/dify
docker-compose down
docker-compose pull
docker-compose -f docker-compose.yaml -f docker-compose.override.yaml up -d
```

> To upgrade to version v1.0.0, please refer to [Migrating Community Edition to v1.0.0](https://docs.dify.ai/development/migration/migrate-to-v1).

<details>

<summary>Upgrading Community Edition to v1.0.0</summary>

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
git checkout 1.0.0 # Switch to the 1.0.0 branch
cd docker
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
</details>

## Customizing

Just like self-hosted deploy, you may modify the environment variables under `.env` in your EC2 instance as you see fit. Then, restart Dify with:

```
docker-compose down
docker-compose -f docker-compose.yaml -f docker-compose.override.yaml up -d
```
