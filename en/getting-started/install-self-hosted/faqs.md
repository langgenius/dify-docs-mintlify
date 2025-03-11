# FAQs

### 1. Not receiving reset password emails

You need to configure the `Mail` parameters in the `.env` file. For detailed instructions, please refer to ["Environment Variables Explanation: Mail-related configuration"](https://docs.dify.ai/getting-started/install-self-hosted/environments#mail-related-configuration).

After modifying the configuration, run the following commands to restart the service:

```bash
docker compose down
docker compose up -d
```

If you still haven't received the email, please check if the email service is working properly and whether the email has been placed in the trash list.

### 2. How to handle if the workflow is too complex and exceeds the node limit?

In the community edition, you can manually adjust the MAX\_TREE\_DEPTH limit for single branch depth in `web/app/components/workflow/constants.ts.` Our default value is 50, and it's important to note that excessively deep branches may affect performance in self-hosted scenarios.

### 3. How to specify the runtime for each workflow node?

You can modify the `TEXT_GENERATION_TIMEOUT_MS` variable in the `.env` file to adjust the runtime for each node. This helps prevent overall application service unavailability caused by certain processes timing out.

### 4. How to reset the password of the admin account?

If you deployed using Docker Compose, you can reset the password with the following command while your Docker Compose is running:

```
docker exec -it docker-api-1 flask reset-password
```

It will prompt you to enter the email address and the new password. Example:

```
dify@my-pc:~/hello/dify/docker$ docker compose up -d
[+] Running 9/9
 ✔ Container docker-web-1         Started                                                              0.1s 
 ✔ Container docker-sandbox-1     Started                                                              0.1s 
 ✔ Container docker-db-1          Started                                                              0.1s 
 ✔ Container docker-redis-1       Started                                                              0.1s 
 ✔ Container docker-weaviate-1    Started                                                              0.1s 
 ✔ Container docker-ssrf_proxy-1  Started                                                              0.1s 
 ✔ Container docker-api-1         Started                                                              0.1s 
 ✔ Container docker-worker-1      Started                                                              0.1s 
 ✔ Container docker-nginx-1       Started                                                              0.1s 
dify@my-pc:~/hello/dify/docker$ docker exec -it docker-api-1 flask reset-password
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
sagemaker.config INFO - Not applying SDK defaults from location: /etc/xdg/sagemaker/config.yaml
sagemaker.config INFO - Not applying SDK defaults from location: /root/.config/sagemaker/config.yaml
Email: hello@dify.ai
New password: newpassword4567
Password confirm: newpassword4567
Password reset successfully.
```

### 5. How to Change the Port

If you're using Docker Compose, you can customize the access port by modifying the `.env` configuration file.

You need to modify the Nginx configuration:

```json
EXPOSE_NGINX_PORT=80
EXPOSE_NGINX_SSL_PORT=443
```


Other self-host issue please check this document [Self-Host Related](../../learn-more/faq/install-faq.md)。