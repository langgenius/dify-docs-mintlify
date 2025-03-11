# Integrate Local Models Deployed by Xinference

[Xorbits inference](https://github.com/xorbitsai/inference) is a powerful and versatile library designed to serve language, speech recognition, and multimodal models, and can even be used on laptops. It supports various models compatible with GGML, such as chatglm, baichuan, whisper, vicuna, orca, etc. And Dify supports connecting to Xinference deployed large language model inference and embedding capabilities locally.

## Deploy Xinference

Please note that you usually do not need to manually find the IP address of the Docker container to access the service, because Docker offers a port mapping feature. This allows you to map the container ports to local machine ports, enabling access via your local address. For example, if you used the `-p 80:80` parameter when running the container, you can access the service inside the container by visiting `http://localhost:80` or `http://127.0.0.1:80`.

If you do need to use the container's IP address directly, the steps above will assist you in obtaining this information.

### Starting Xinference

There are two ways to deploy Xinference, namely [local deployment](https://github.com/xorbitsai/inference/blob/main/README.md#local) and [distributed deployment](https://github.com/xorbitsai/inference/blob/main/README.md#distributed), here we take local deployment as an example.

1.  First, install Xinference via PyPI:

    ```bash
    $ pip install "xinference[all]"
    ```
2.  Start Xinference locally:

    ```bash
    $ xinference-local
    2023-08-20 19:21:05,265 xinference   10148 INFO     Xinference successfully started. Endpoint: http://127.0.0.1:9997
    2023-08-20 19:21:05,266 xinference.core.supervisor 10148 INFO     Worker 127.0.0.1:37822 has been added successfully
    2023-08-20 19:21:05,267 xinference.deploy.worker 10148 INFO     Xinference worker successfully started.
    ```

    Xinference will start a worker locally by default, with the endpoint: `http://127.0.0.1:9997`, and the default port is `9997`. By default, access is limited to the local machine only, but it can be configured with `-H 0.0.0.0` to allow access from any non-local client. To modify the host or port, you can refer to xinference's help information: `xinference-local --help`.

    > If you use the Dify Docker deployment method, you need to pay attention to the network configuration to ensure that the Dify container can access the endpoint of Xinference. The Dify container cannot access localhost inside, and you need to use the host IP address.
3.  Create and deploy the model

    Visit `http://127.0.0.1:9997`, select the model and specification you need to deploy, as shown below:

    ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/6945f8e7a0ae88d1f67f988d53d420bd.png)

    As different models have different compatibility on different hardware platforms, please refer to [Xinference built-in models](https://inference.readthedocs.io/en/latest/models/builtin/index.html) to ensure the created model supports the current hardware platform.
4.  Obtain the model UID

    Copy model ID from `Running Models` page, such as: `2c886330-8849-11ee-9518-43b0b8f40bea`
5.  After the model is deployed, connect the deployed model in Dify.

    In `Settings > Model Providers > Xinference`, enter:

    * Model name: `vicuna-v1.3`
    * Server URL: `http://<Machine_IP>:9997` **Replace with your machine IP address**
    * Model UID: `2c886330-8849-11ee-9518-43b0b8f40bea`

    Click "Save" to use the model in the dify application.

Dify also supports using [Xinference builtin models](https://github.com/xorbitsai/inference/blob/main/README.md#builtin-models) as Embedding models, just select the Embeddings type in the configuration box.

For more information about Xinference, please refer to: [Xorbits Inference](https://github.com/xorbitsai/inference)
