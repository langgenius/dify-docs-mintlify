# FAQ

### 1. How to reset the password if the local deployment initialization fails with an incorrect password?

If deployed using docker compose, you can execute the following command to reset the password: `docker exec -it docker-api-1 flask reset-password` Enter the account email and twice new passwords, and it will be reset.

### 2. How to resolve File not found error in the log when deploying locally?

```
ERROR:root:Unknown Error in completion
Traceback (most recent call last):
  File "/www/wwwroot/dify/dify/api/libs/rsa.py", line 45, in decrypt
    private_key = storage.load(filepath)
  File "/www/wwwroot/dify/dify/api/extensions/ext_storage.py", line 65, in load
    raise FileNotFoundError("File not found")
FileNotFoundError: File not found
```

This error may be caused by switching deployment methods, or deleting the `api/storage/privkeys` file, which is used to encrypt large model keys and can not be reversed if lost. You can reset the encryption public and private keys with the following command:

* Docker compose deployment

```
docker exec -it docker-api-1 flask reset-encrypt-key-pair
```

* Source code startup

Enter the api directory

```
flask reset-encrypt-key-pair
```

Follow the prompts to reset.

### 3. Unable to log in when installing later, and then login is successful but subsequent interfaces prompt 401?

This may be due to switching the domain name/website, causing cross-domain between front-end and server-side. Cross-domain and identity involve two configuration items:

**CORS cross-domain configuration**

`CONSOLE_CORS_ALLOW_ORIGINS` Console CORS cross-domain policy, default to `*`, which allows access from all domain names. `WEB_API_CORS_ALLOW_ORIGINS` WebAPP CORS cross-domain strategy, default to `*`, which allows access from all domain names.

### 4. After starting, the page keeps loading and checking the request prompts CORS error?

This may be because the domain name/URL has been switched, resulting in cross-domain between the front end and the back end. Please change all the following configuration items in `docker-compose.yml` to the new domain name: `CONSOLE_API_URL:` The backend URL of the console API. `CONSOLE_WEB_URL:` The front-end URL of the console web. `SERVICE_API_URL:` Service API Url `APP_API_URL:` WebApp API backend Url. `APP_WEB_URL:` WebApp Url.

For more information, please check out: [Environments](environments.md)

### 5. How to upgrade version after deployment?

If you start up through images, please pull the latest images to complete the upgrade. If you start up through source code, please pull the latest code and then start up to complete the upgrade.

When deploying and updating local source code, you need to enter the API directory and execute the following command to migrate the database structure to the latest version:

`flask db upgrade`

### 6.How to configure the environment variables when use Notion import

**Q: What is the Notion's Integration configuration address?**

A: [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)

**Q: Which environment variables need to be configured？**

A: Please set below configuration when doing the privatized deployment

1. **`NOTION_INTEGRATION_TYPE`** : The value should configrate as (**public/internal**). Since the Redirect address of Notion’s Oauth only supports https, if it is deployed locally, please use Notion’s internal integration
2. **`NOTION_CLIENT_SECRET`** : Notion OAuth client secret (userd for public integration type)
3. **`NOTION_CLIENT_ID`** : OAuth client ID (userd for public integration type)
4. **`NOTION_INTERNAL_SECRET`** : Notion Internal Integration Secret, If the value of `NOTION_INTEGRATION_TYPE` is **internal** ,you need to configure this variable.

### 7. How to change the name of the space in the local deployment version?

Modify in the `tenants` table in the database.

### 8. Where can I modify the domain name for accessing the application?

Find the configuration domain name APP\_WEB\_URL in `docker_compose.yaml`.

### 9. If database migration is required, what things need to be backed up?

The database, configured storage, and vector database data need to be backed up. If deployed in Docker Compose mode, all data content in the `dify/docker/volumes` directory can be directly backed up.

### 10. Why is Docker deploying Dify and starting OpenLLM locally using 127.0.0.1, but unable to access the local port?

`127.0.0.1` is the internal address of the container, and the server address configured by Dify requires the host LAN IP address.

### 11. How to solve the size and quantity limitations for uploading knowledge documents in the local deployment version？

You can refer to the official website environment variable description document to configure:

[Environments](environments.md)

### 12. How does the local deployment edition invite members through email?

Local deployment edition, members can be invited through email. After entering the email invitation, the page displays the invitation link, copies the invitation link, and forwards it to users. Your team members can open the link and log in to your space by setting a password through email login.

### 13. How to solve listen tcp4 0.0.0.0:80: bind: address already in use?

This is because the port is occupied. You can use the `netstat -tunlp | grep 80` command to view the process that occupies the port, and then kill the process. For example, the apache and nginx processes occupy the port, you can use the `service apache2 stop` and `service nginx stop` commands to stop the process.

### 14. What to do if this error occurs in text-to-speech?

```
[openai] Error: ffmpeg is not installed
```

Since OpenAI TTS has implemented audio stream segmentation, ffmpeg needs to be installed for normal use when deploying the source code. Here are the detailed steps:

**Windows:**

1. Visit the [FFmpeg official website](https://ffmpeg.org/download.html) and download the precompiled Windows shared library.
2. Download and unzip the FFmpeg folder, which will generate a folder similar to "ffmpeg-20200715-51db0a4-win64-static".
3. Move the unzipped folder to a location of your choice, for example, C:\Program Files.
4. Add the absolute path of the FFmpeg bin directory to the system environment variables.
5. Open the command prompt and enter "ffmpeg -version" to see if the FFmpeg version information is displayed, indicating successful installation.

**Ubuntu:**

1. Open the terminal.
2. Enter the following commands to install FFmpeg: `sudo apt-get update`, then enter `sudo apt-get install ffmpeg`.
3. Enter "ffmpeg -version" to check if it has been successfully installed.

**CentOS:**

1. First, you need to enable the EPEL repository. In the terminal, enter: `sudo yum install epel-release`
2. Then, enter: `sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm`
3. Update the yum package, enter: `sudo yum update`
4. Finally, install FFmpeg, enter: `sudo yum install ffmpeg ffmpeg-devel`
5. Enter "ffmpeg -version" to check if it has been successfully installed.

**Mac OS X:**

1. Open the terminal.
2. If you haven't installed Homebrew yet, you can install it by entering the following command in the terminal: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
3. Install FFmpeg with Homebrew, enter: `brew install ffmpeg`
4. Enter "ffmpeg -version" to check if it has been successfully installed.

### 15. Migrate Vector Database to Another Vector Database

If you want to migrate the vector database from weaviate to another vector database, you need to migrate the data in the vector database. The following is the migration method:

Step:

1. If you are starting from local source code, modify the environment variable in the `.env` file to the vector database you want to migrate to. etc: `VECTOR_STORE=qdrant`
2. If you are starting from docker-compose, modify the environment variable in the `docker-compose.yaml` file to the vector database you want to migrate to, both api and worker are all needed. etc:

```
# The type of vector store to use. Supported values are `weaviate`, `qdrant`, `milvus`, `analyticdb`.
VECTOR_STORE: weaviate
```

3. run the below command in your terminal or docker container

```
flask vdb-migrate # or docker exec -it docker-api-1 flask vdb-migrate
```

**Tested target database:**

- qdrant
- milvus
- analyticdb

### 16. Why is SSRF_PROXY Needed?

You may have noticed the `SSRF_PROXY` environment variable in the `docker-compose.yaml` file. This is crucial because the local deployment of Dify uses `SSRF_PROXY` to prevent Server-Side Request Forgery (SSRF) attacks. For more details on SSRF attacks, refer to [this resource](https://portswigger.net/web-security/ssrf).

To reduce potential risks, we have set up a proxy for all services that could be vulnerable to SSRF attacks. This proxy ensures that services like Sandbox can only access external networks through it, thereby protecting your data and services. By default, this proxy does not intercept any local requests. However, you can customize the proxy's behavior by modifying the `squid` configuration file.

#### How to Customize the Proxy Behavior?

In the `docker/volumes/ssrf_proxy/squid.conf` file, you will find the configuration settings for the proxy. For example, if you want to allow the `192.168.101.0/24` network to be accessed by the proxy, but restrict access to an IP address `192.168.101.19` that contains sensitive data, you can add the following rules to `squid.conf`:

```plaintext
acl restricted_ip dst 192.168.101.19
acl localnet src 192.168.101.0/24

http_access deny restricted_ip
http_access allow localnet
http_access deny all
```

This is a basic example, and you can customize the rules to fit your specific needs. For more information about configuring `squid`, refer to the [official documentation](http://www.squid-cache.org/Doc/config/).

