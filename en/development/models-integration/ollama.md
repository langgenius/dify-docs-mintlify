# Integrate Local Models Deployed by Ollama

![ollama](<../../.gitbook/assets/ollama (1).png>)

[Ollama](https://github.com/jmorganca/ollama) is a cross-platform inference framework client (MacOS, Windows, Linux) designed for seamless deployment of large language models (LLMs) such as Llama 2, Mistral, Llava, and more. With its one-click setup, Ollama enables local execution of LLMs, providing enhanced data privacy and security by keeping your data on your own machine.

## Quick Integration

### Download and Launch Ollama

1.  Download Ollama

    Visit [https://ollama.com/download](https://ollama.com/download) to download the Ollama client for your system.

2.  Run Ollama and Chat with Llama3.2

    ```bash
    ollama run llama3.2
    ```

    After successful launch, Ollama starts an API service on local port 11434, which can be accessed at `http://localhost:11434`.

    For other models, visit [Ollama Models](https://ollama.com/library) for more details.

3.  Integrate Ollama in Dify

    In `Settings > Model Providers > Ollama`, fill in:

    ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/06aa8dca873203e7bd8cc1866fa8f83b.png)

    * Model Name: `llama3.2`
    *   Base URL: `http://<your-ollama-endpoint-domain>:11434`

        Enter the base URL where the Ollama service is accessible. If filling in a public URL still results in an error, please refer to the [FAQ](#faq) and modify environment variables to make Ollama service accessible from all IPs

        If Dify is deployed using Docker, consider using the local network IP address, e.g., `http://192.168.1.100:11434` or `http://host.docker.internal:11434` to access the service.

        For local source code deployment, use `http://localhost:11434`.
    * Model Type: `Chat`
    *   Model Context Length: `4096`

        The maximum context length of the model. If unsure, use the default value of 4096.
    *   Maximum Token Limit: `4096`

        The maximum number of tokens returned by the model. If there are no specific requirements for the model, this can be consistent with the model context length.
    *   Support for Vision: `Yes`

        Check this option if the model supports image understanding (multimodal), like `llava`.

    Click "Save" to use the model in the application after verifying that there are no errors.

    The integration method for Embedding models is similar to LLM, just change the model type to Text Embedding.
1.  Use Ollama Models

    ![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/development/models-integration/f6003949d3fdf670fb4d61fab39d7947.png)

    Enter `Prompt Eng.` page of the App that needs to be configured, select the `llava` model under the Ollama provider, and use it after configuring the model parameters.

## FAQ

### ⚠️ If you are using docker to deploy Dify and Ollama, you may encounter the following error:

```bash
httpconnectionpool(host=127.0.0.1, port=11434): max retries exceeded with url:/cpi/chat (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f8562812c20>: fail to establish a new connection:[Errno 111] Connection refused'))

httpconnectionpool(host=localhost, port=11434): max retries exceeded with url:/cpi/chat (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f8562812c20>: fail to establish a new connection:[Errno 111] Connection refused'))
```

This error occurs because the Ollama service is not accessible from the docker container. `localhost` usually refers to the container itself, not the host machine or other containers. 

You need to expose the Ollama service to the network to resolve this issue.

### Setting environment variables on Mac

If Ollama is run as a macOS application, environment variables should be set using `launchctl`:

1.  For each environment variable, call `launchctl setenv`.

    ```bash
    launchctl setenv OLLAMA_HOST "0.0.0.0"
    ```
2. Restart Ollama application.
3.  If the above steps are ineffective, you can use the following method:

    The issue lies within Docker itself, and to access the Docker host.\
    you should connect to `host.docker.internal`. Therefore, replacing `localhost` with `host.docker.internal` in the service will make it work effectively.

    ```bash
    http://host.docker.internal:11434
    ```

### Setting environment variables on Linux

If Ollama is run as a systemd service, environment variables should be set using `systemctl`:

1. Edit the systemd service by calling `systemctl edit ollama.service`. This will open an editor.
2.  For each environment variable, add a line `Environment` under section `[Service]`:

    ```ini
    [Service]
    Environment="OLLAMA_HOST=0.0.0.0"
    ```
3. Save and exit.
4.  Reload `systemd` and restart Ollama:

    ```bash
    systemctl daemon-reload
    systemctl restart ollama
    ```

### Setting environment variables on Windows

On windows, Ollama inherits your user and system environment variables.

1. First Quit Ollama by clicking on it in the task bar
2. Edit system environment variables from the control panel
3. Edit or create New variable(s) for your user account for `OLLAMA_HOST`, `OLLAMA_MODELS`, etc.
4. Click OK/Apply to save
5. Run `ollama` from a new terminal window

## How can I expose Ollama on my network?

Ollama binds 127.0.0.1 port 11434 by default. Change the bind address with the `OLLAMA_HOST` environment variable.
