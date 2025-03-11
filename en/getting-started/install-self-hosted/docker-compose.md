# Deploy with Docker Compose

## Prerequisites

> Before installing Dify, make sure your machine meets the following minimum system requirements:
>
> * CPU >= 2 Core
> * RAM >= 4 GiB

| Operating System           | Software                                                     | Explanation                                                                                                                                                                                                                                                                                                                               |
| -------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| macOS 10.14 or later       | Docker Desktop                                               | Set the Docker virtual machine (VM) to use a minimum of 2 virtual CPUs (vCPUs) and 8 GB of initial memory. Otherwise, the installation may fail. For more information, please refer to the [Docker Desktop installation guide for Mac](https://docs.docker.com/desktop/mac/install/).                                                     |
| Linux platforms            | <p>Docker 19.03 or later<br>Docker Compose 1.28 or later</p> | Please refer to the [Docker installation guide](https://docs.docker.com/engine/install/) and [the Docker Compose installation guide](https://docs.docker.com/compose/install/) for more information on how to install Docker and Docker Compose, respectively.                                                                            |
| Windows with WSL 2 enabled | Docker Desktop                                               | We recommend storing the source code and other data that is bound to Linux containers in the Linux file system rather than the Windows file system. For more information, please refer to the [Docker Desktop installation guide for using the WSL 2 backend on Windows.](https://docs.docker.com/desktop/windows/install/#wsl-2-backend) |

> \[!IMPORTANT]
>
> Dify 0.6.12 has introduced significant enhancements to Docker Compose deployment, designed to improve your setup and update experience. For more information, read the [README.md](https://github.com/langgenius/dify/blob/main/docker/README.md).

### Clone Dify

Clone the Dify source code to your local machine:

```bash
# Assuming current latest version is 0.15.3
git clone https://github.com/langgenius/dify.git --branch 0.15.3
```

### Starting Dify

1.  Navigate to the Docker directory in the Dify source code

    ```bash
    cd dify/docker
    ```
2.  Copy the environment configuration file

    ```bash
    cp .env.example .env
    ```
3.  Start the Docker containers

    Choose the appropriate command to start the containers based on the Docker Compose version on your system. You can use the `$ docker compose version` command to check the version, and refer to the [Docker documentation](https://docs.docker.com/compose/install/) for more information:

    * If you have Docker Compose V2, use the following command:

    ```bash
    docker compose up -d
    ```

    * If you have Docker Compose V1, use the following command:

    ```bash
    docker-compose up -d
    ```

After executing the command, you should see output similar to the following, showing the status and port mappings of all containers:

```bash
[+] Running 11/11
 ✔ Network docker_ssrf_proxy_network  Created                                                                 0.1s 
 ✔ Network docker_default             Created                                                                 0.0s 
 ✔ Container docker-redis-1           Started                                                                 2.4s 
 ✔ Container docker-ssrf_proxy-1      Started                                                                 2.8s 
 ✔ Container docker-sandbox-1         Started                                                                 2.7s 
 ✔ Container docker-web-1             Started                                                                 2.7s 
 ✔ Container docker-weaviate-1        Started                                                                 2.4s 
 ✔ Container docker-db-1              Started                                                                 2.7s 
 ✔ Container docker-api-1             Started                                                                 6.5s 
 ✔ Container docker-worker-1          Started                                                                 6.4s 
 ✔ Container docker-nginx-1           Started                                                                 7.1s
```

Finally, check if all containers are running successfully:

```bash
docker compose ps
```

This includes 3 core services: `api / worker / web`, and 6 dependent components: `weaviate / db / redis / nginx / ssrf_proxy / sandbox` .

```bash
NAME                  IMAGE                              COMMAND                   SERVICE      CREATED              STATUS                        PORTS
docker-api-1          langgenius/dify-api:0.6.13         "/bin/bash /entrypoi…"   api          About a minute ago   Up About a minute             5001/tcp
docker-db-1           postgres:15-alpine                 "docker-entrypoint.s…"   db           About a minute ago   Up About a minute (healthy)   5432/tcp
docker-nginx-1        nginx:latest                       "sh -c 'cp /docker-e…"   nginx        About a minute ago   Up About a minute             0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp
docker-redis-1        redis:6-alpine                     "docker-entrypoint.s…"   redis        About a minute ago   Up About a minute (healthy)   6379/tcp
docker-sandbox-1      langgenius/dify-sandbox:0.2.1      "/main"                   sandbox      About a minute ago   Up About a minute             
docker-ssrf_proxy-1   ubuntu/squid:latest                "sh -c 'cp /docker-e…"   ssrf_proxy   About a minute ago   Up About a minute             3128/tcp
docker-weaviate-1     semitechnologies/weaviate:1.19.0   "/bin/weaviate --hos…"   weaviate     About a minute ago   Up About a minute             
docker-web-1          langgenius/dify-web:0.6.13         "/bin/sh ./entrypoin…"   web          About a minute ago   Up About a minute             3000/tcp
docker-worker-1       langgenius/dify-api:0.6.13         "/bin/bash /entrypoi…"   worker       About a minute ago   Up About a minute             5001/tcp
```

With these steps, you should be able to install Dify successfully.

### Upgrade Dify

Enter the docker directory of the dify source code and execute the following commands:

```bash
cd dify/docker
docker compose down
git pull origin main
docker compose pull
docker compose up -d
```

#### Sync Environment Variable Configuration (Important)

* If the `.env.example` file has been updated, be sure to modify your local `.env` file accordingly.
* Check and modify the configuration items in the `.env` file as needed to ensure they match your actual environment. You may need to add any new variables from `.env.example` to your `.env` file, and update any values that have changed.

### Access Dify

Access administrator initialization page to set up the admin account:

```bash
# Local environment
http://localhost/install

# Server environment
http://your_server_ip/install
```

Dify web interface address:

```bash
# Local environment
http://localhost

# Server environment
http://your_server_ip
```

### Customize Dify

Edit the environment variable values in your `.env` file directly. Then, restart Dify with:

```
docker compose down
docker compose up -d
```

The full set of annotated environment variables along can be found under docker/.env.example.

### Read More

If you have any questions, please refer to [FAQs](faqs.md).
