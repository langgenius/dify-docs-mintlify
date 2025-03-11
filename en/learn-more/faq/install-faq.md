# Self Host / Local Deployment

### 1. How to reset the password if it is incorrect after local deployment initialization?

If you deployed using Docker Compose, you can reset the password with the following command:

```
docker exec -it docker-api-1 flask reset-password
```

Enter the account email and the new password twice.

### 2. How to fix the "File not found" error in local deployment logs?

```
ERROR:root:Unknown Error in completion
Traceback (most recent call last):
  File "/www/wwwroot/dify/dify/api/libs/rsa.py", line 45, in decrypt
    private_key = storage.load(filepath)
  File "/www/wwwroot/dify/dify/api/extensions/ext_storage.py", line 65, in load
    raise FileNotFoundError("File not found")
FileNotFoundError: File not found
```

This error might be due to changing the deployment method or deleting the `api/storage/privkeys` directory. This file is used to encrypt the large model keys, so its loss is irreversible. You can reset the encryption key pair with the following commands:

* Docker Compose deployment

    ```
    docker exec -it docker-api-1 flask reset-encrypt-key-pair
    ```
* Source code startup

    Navigate to the `api` directory

    ```
    flask reset-encrypt-key-pair
    ```

    Follow the prompts to reset.

### 3. Unable to log in after installation, or receiving a 401 error on subsequent interfaces after a successful login?

This might be due to switching the domain/URL, causing cross-domain issues between the frontend and backend. Cross-domain and identity issues involve the following configurations:

1. CORS Cross-Domain Configuration
   1. `CONSOLE_CORS_ALLOW_ORIGINS`

       Console CORS policy, default is `*`, meaning all domains can access.
   2. `WEB_API_CORS_ALLOW_ORIGINS`

       WebAPP CORS policy, default is `*`, meaning all domains can access.

### 4. The page keeps loading after startup, and requests show CORS errors?

This might be due to switching the domain/URL, causing cross-domain issues between the frontend and backend. Update the following configuration items in `docker-compose.yml` to the new domain:

`CONSOLE_API_URL:` Backend URL for the console API.
`CONSOLE_WEB_URL:` Frontend URL for the console web.
`SERVICE_API_URL:` URL for the service API.
`APP_API_URL:` Backend URL for the WebApp API.
`APP_WEB_URL:` URL for the WebApp.

For more information, please refer to: [Environment Variables](../../getting-started/install-self-hosted/environments.md)

### 5. How to upgrade the version after deployment?

If you started with an image, pull the latest image to complete the upgrade. If you started with source code, pull the latest code and then start it to complete the upgrade.

For source code deployment updates, navigate to the `api` directory and run the following command to migrate the database structure to the latest version:

`flask db upgrade`

### 6. How to configure environment variables when importing using Notion?

[**Notion Integration Configuration Address**](https://www.notion.so/my-integrations). When performing a private deployment, set the following configurations:

1. **`NOTION_INTEGRATION_TYPE`**: This value should be configured as **public/internal**. Since Notion's OAuth redirect address only supports https, use Notion's internal integration for local deployment.
2. **`NOTION_CLIENT_SECRET`**: Notion OAuth client secret (for public integration type).
3. **`NOTION_CLIENT_ID`**: OAuth client ID (for public integration type).
4. **`NOTION_INTERNAL_SECRET`**: Notion internal integration secret. If the value of `NOTION_INTEGRATION_TYPE` is **internal**, configure this variable.

### 7. How to change the name of the space in the local deployment version?

Modify it in the `tenants` table of the database.

### 8. Where to modify the domain for accessing the application?

Find the `APP_WEB_URL` configuration domain in `docker_compose.yaml`.

### 9. What to back up if a database migration occurs?

Back up the database, configured storage, and vector database data. If deployed using Docker Compose, directly back up all data in the `dify/docker/volumes` directory.

### 10. Why can't Docker deployment Dify access the local port using 127.0.0.1 when starting OpenLLM locally?

127.0.0.1 is the internal address of the container. Dify's configured server address needs to be the host's local network IP address.

### 11. How to resolve the size and quantity limit of document uploads in the dataset for the local deployment version?

Refer to the official website [Environment Variables Documentation](https://docs.dify.ai/v/zh-hans/getting-started/install-self-hosted/environments) for configuration.

### 12. How to invite members via email in the local deployment version?

In the local deployment version, invite members via email. After entering the email and sending the invitation, the page will display an invitation link. Copy the invitation link and forward it to the user. The user can open the link, log in via email, set a password, and log in to your space.

### 13. What to do if you encounter the error "Can't load tokenizer for 'gpt2'" in the local deployment version?

```
Can't load tokenizer for 'gpt2'. If you were trying to load it from 'https://huggingface.co/models', make sure you don't have a local directory with the same name. Otherwise, make sure 'gpt2' is the correct path to a directory containing all relevant files for a GPT2TokenizerFast tokenizer.
```

Refer to the official website [Environment Variables Documentation](https://docs.dify.ai/v/zh-hans/getting-started/install-self-hosted/environments) for configuration, and the related [Issue](https://github.com/langgenius/dify/issues/1261).

### 14. How to resolve a port 80 conflict in the local deployment version?

If port 80 is occupied, stop the service occupying port 80 or modify the port mapping in `docker-compose.yaml` to map port 80 to another port. Typically, Apache and Nginx occupy this port, which can be resolved by stopping these two services.

### 15. What to do if you encounter the error "[openai] Error: ffmpeg is not installed" during text-to-speech?

```
[openai] Error: ffmpeg is not installed
```

Since OpenAI TTS implements audio stream segmentation, ffmpeg needs to be installed for source code deployment to work properly. Detailed steps:

**Windows:**

1. Visit [FFmpeg Official Website](https://ffmpeg.org/download.html) and download the precompiled Windows shared library.
2. Download and extract the FFmpeg folder, which will generate a folder like "ffmpeg-20200715-51db0a4-win64-static".
3. Move the extracted folder to your desired location, e.g., C:\Program Files\.
4. Add the absolute path of the FFmpeg bin directory to the system environment variables.
5. Open Command Prompt and enter "ffmpeg -version". If you see the FFmpeg version information, the installation is successful.

**Ubuntu:**

1. Open Terminal.
2. Enter the following commands to install FFmpeg: `sudo apt-get update`, then `sudo apt-get install ffmpeg`.
3. Enter "ffmpeg -version" to check if the installation is successful.

**CentOS:**

1. First, enable the EPEL repository. Enter in Terminal: `sudo yum install epel-release`
2. Then, enter: `sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm`
3. Update yum packages, enter: `sudo yum update`
4. Finally, install FFmpeg, enter: `sudo yum install ffmpeg ffmpeg-devel`
5. Enter "ffmpeg -version" to check if the installation is successful.

**Mac OS X:**

1. Open Terminal.
2. If you haven't installed Homebrew, you can install it by entering the following command in Terminal: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. Use Homebrew to install FFmpeg, enter: `brew install ffmpeg`
4. Enter "ffmpeg -version" to check if the installation is successful.

### 16. How to resolve an Nginx configuration file mount failure during local deployment?

```
Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error mounting "/run/desktop/mnt/host/d/Documents/docker/nginx/nginx.conf" to rootfs at "/etc/nginx/nginx.conf": mount /run/desktop/mnt/host/d/Documents/docker/nginx/nginx.conf:/etc/nginx/nginx.conf (via /proc/self/fd/9), flags: 0x5000: not a directory: unknown: Are you trying to mount a directory onto a file (or vice-versa)? Check if the specified host path exists and is the expected type
```

Download the complete project, navigate to the docker directory, and execute `docker-compose up -d`.

```
git clone https://github.com/langgenius/dify.git
cd dify/docker
docker compose up -d
```

### 17. Migrate weaviate to another vector database

To migrate from Weaviate to another vector database, follow these steps:

1. For local source code deployment:
   - Update the vector database setting in the `.env` file
   - Example: Set `VECTOR_STORE=qdrant` to migrate to Qdrant

2. For Docker Compose deployment:
   - Update the vector database settings in `docker-compose.yaml`
   - Make sure to modify both API and worker service configurations

```
# The type of vector store to use. Supported values are `weaviate`, `qdrant`, `milvus`, `analyticdb`.
VECTOR_STORE: weaviate
```

3. Execute the below command in your terminal or docker container

```
flask vdb-migrate # or docker exec -it docker-api-1 flask vdb-migrate
```

**Tested target database:**

- qdrant
- milvus
- analyticdb

### 18. Why is SSRF_PROXY needed?

In the community edition's `docker-compose.yaml`, you might notice some services configured with `SSRF_PROXY` and `HTTP_PROXY` environment variables, all pointing to an `ssrf_proxy` container. This is to prevent SSRF attacks. For more information on SSRF attacks, you can read [this article](https://portswigger.net/web-security/ssrf).

To avoid unnecessary risks, we configure a proxy for all services that might cause SSRF attacks and force services like Sandbox to only access external networks through the proxy, ensuring your data and service security. By default, this proxy does not intercept any local requests, but you can customize the proxy behavior by modifying the `squid` configuration file.

#### How to customize the proxy behavior?

In `docker/volumes/ssrf_proxy/squid.conf`, you can find the `squid` configuration file. You can customize the proxy behavior here, such as adding ACL rules to restrict proxy access or adding `http_access` rules to restrict proxy access. For example, your local network can access the `192.168.101.0/24` segment, but `192.168.101.19` has sensitive data that you don't want local deployment Dify users to access, but other IPs can. You can add the following rules in `squid.conf`:

```
acl restricted_ip dst 192.168.101.19
acl localnet src 192.168.101.0/24

http_access deny restricted_ip
http_access allow localnet
http_access deny all
```

This is just a simple example. You can customize the proxy behavior according to your needs. If your business is more complex, such as needing to configure an upstream proxy or cache, you can refer to the [squid configuration documentation](http://www.squid-cache.org/Doc/config/) for more information.

### 19. How to set your created application as a template?

Currently, it is not supported to set your created application as a template. The existing templates are provided by Dify official for cloud version users to refer to. If you are using the cloud version, you can add applications to your workspace or customize them after modification to create your own applications. If you are using the community version and need to create more application templates for your team, you can contact our business team for paid technical support: [business@dify.ai](mailto:business@dify.ai)

### 20. 502 Bad Gateway

This is because Nginx is forwarding the service to the wrong location. First, ensure the container is running, then run the following command with root privileges:

```
docker ps -q | xargs -n 1 docker inspect --format '{{ .Name }}: {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
```

Find these two lines in the output:

```
/docker-web-1: 172.19.0.5
/docker-api-1: 172.19.0.7
```

Remember the IP addresses. Then open the directory where you store the Dify source code, open `dify/docker/nginx/conf.d`, replace `http://api:5001` with `http://172.19.0.7:5001`, and replace `http://web:3000` with `http://172.19.0.5:3000`, then restart the Nginx container or reload the configuration.

These IP addresses are _**examples**_, you must execute the command to get your own IP addresses, do not fill them in directly. You might need to reconfigure the IP addresses when restarting the relevant containers.

### 21. How to modify the API service port number?

The API service port is consistent with the one used by the Dify platform. You can reassign the running port by modifying the `nginx` configuration in the `docker-compose.yaml` file.

### 22. How to Migrate from Local to Cloud Storage?

To migrate files from local storage to cloud storage (e.g., Alibaba Cloud OSS), you'll need to transfer data from the 'upload_files' and 'privkeys' folders. Follow these steps:

1. Configure Storage Settings

   For local source code deployment:
   - Update storage settings in `.env` file
   - Set `STORAGE_TYPE=aliyun-oss`
   - Configure Alibaba Cloud OSS credentials

   For Docker Compose deployment:
   - Update storage settings in `docker-compose.yaml`
   - Set `STORAGE_TYPE: aliyun-oss`
   - Configure Alibaba Cloud OSS credentials

2. Execute Migration Commands

   For local source code:
   ```bash
   flask upload-private-key-file-to-cloud-storage
   flask upload-local-files-to-cloud-storage
   ```

   For Docker Compose:
   ```bash
   docker exec -it docker-api-1 flask upload-private-key-file-to-cloud-storage
   docker exec -it docker-api-1 flask upload-local-files-to-cloud-storage
   ```
