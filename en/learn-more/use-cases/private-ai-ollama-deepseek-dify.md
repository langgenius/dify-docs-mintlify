# Private Deployment of Ollama + DeepSeek + Dify: Build Your Own AI Assistant

## Overview

DeepSeek is an innovative open-source large language model (LLM) that brings a revolutionary experience to AI-powered conversations with its advanced algorithmic architecture and reflective reasoning capabilities. By deploying it privately, you gain full control over data security and system configurations while maintaining flexibility in your deployment strategy.

Dify, an open-source AI application development platform, offers a complete private deployment solution. By seamlessly integrating a locally deployed DeepSeek model into the Dify platform, enterprises can build powerful AI applications within their own infrastructure while ensuring data privacy.

### Advantages of Private Deployment:

* **Superior Performance**: Delivers a conversational experience comparable to commercial models.
* **Isolated Environment**: Runs entirely offline, eliminating data leakage risks.
* **Full Data Control**: Retains complete ownership of data assets, ensuring compliance.

***

## Prerequisites

### **Hardware Requirements:**

* **CPU**: ≥ 2 Cores
* **RAM/GPU Memory**: ≥ 16 GiB (Recommended)

### **Software Requirements:**

* [Docker](https://www.docker.com/)
* Docker Compose
* [Ollama](https://ollama.com/)
* [Dify Community Edition](https://github.com/langgenius/dify)

***

## Deployment Steps

### 1. Install Ollama

[Ollama](https://ollama.com/) is a cross-platform LLM management client (MacOS, Windows, Linux) that enables seamless deployment of large language models like DeepSeek, Llama, and Mistral. Ollama provides a one-click model deployment solution, ensuring that all data remains stored locally for complete security and privacy.

Visit [Ollama's official website](https://ollama.com/) and follow the installation instructions for your platform. After installation, verify it by running the following command:

```bash
➜  ~ ollama -v
ollama version is 0.5.5
```

Select an appropriate DeepSeek model size based on your available hardware. A 7B model is recommended for initial installation.

![](https://assets-docs.dify.ai/2025/01/26978571a8d5f7188a952606f62e6a32.png)

Run the following command to install the DeepSeek R1 model:

```bash
ollama run deepseek-r1:7b
```

![](https://assets-docs.dify.ai/2025/01/9297451d07d7704f73d6db0a83842f5f.png)

### 2. Install Dify Community Edition

Clone the Dify GitHub repository and follow the installation process:

```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
docker compose up -d  # Use `docker-compose up -d` if running Docker Compose V1
```

After running the command, you should see all containers running with proper port mappings. For detailed instructions, refer to [Deploy with Docker Compose](https://docs.dify.ai/getting-started/install-self-hosted/docker-compose).

Dify Community Edition runs on port 80 by default. You can access your private Dify platform at: `http://your_server_ip`

### 3. Integrate DeepSeek with Dify

Go to **Profile → Settings → Model Providers** in the Dify platform. Select **Ollama** and click **Add Model**.

> Note: The “DeepSeek” option in Model Providers refers to the online API service, whereas the Ollama option is used for a locally deployed DeepSeek model.

Configure the Model:&#x20;

• **Model Name**: Enter the deployed model name, e.g., `deepseek-r1:7b`.&#x20;

• **Base URL**: Set the Ollama client’s local service URL, typically `http://your_server_ip:11434`. If you encounter connection issues, please refer to the [FAQ](https://docs.dify.ai/learn-more/use-cases/private-ai-ollama-deepseek-dify#id-1.-connection-errors-when-using-docker).&#x20;

• **Other settings**: Keep default values. According to the [DeepSeek model specifications](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B), the max token length is 32,768.

![](https://assets-docs.dify.ai/2025/01/6f3b53427e46786ba7d1374739344142.png)

## Build AI Applications

### DeepSeek AI Chatbot (Simple Application)

1. On the Dify homepage, click Create Blank App, select Chatbot, and give it a name.

![](https://assets-docs.dify.ai/2025/01/7f56bc3c836c7248043b656fa95e474e.png)

2. Select the `deepseek-r1:7b` model under Ollama in the Model Provider section.

![](https://assets-docs.dify.ai/2025/01/dbd7170abd35f545481ecc0beef85333.png)

3. Enter a message in the chat preview to verify the model’s response. If it replies correctly, the chatbot is online.

![](https://assets-docs.dify.ai/2025/01/619fbbd48e55a1e6a598b4039dd631f5.png)

4. Click the Publish button to obtain a shareable link or embed the chatbot into other websites.

### DeepSeek AI Chatflow / Workflow (Advanced Application)

> Chatflow / Workflow applications enable the creation of more complex AI solutions, such as document recognition, image processing, and speech recognition. For more details, please check the [Workflow Documentation](https://docs.dify.ai/guides/workflow).

1. Click Create Blank App, then select Chatflow or Workflow, and name the application.

![](https://assets-docs.dify.ai/2025/01/cb8637be4dca5a0e684fd9a21df3711f.png)

2. Add an LLM Node, select the `deepseek-r1:7b` model under Ollama, and use the `{{#sys.query#}}` variable into the system prompt to connect to the initial node. If you encounter any API issues, you can handle them via [Load Balancing](https://docs.dify.ai/guides/model-configuration/load-balancing) or the [Error Handling](https://docs.dify.ai/guides/workflow/error-handling) node.
3. Add an LLM node, select the deepseek-r1:7b model under the Ollama framework, and insert the \{{#sys.query#\}} variable into the system prompt to connect to the initial node. If you encounter any API issues, you can handle them via Load Balancing or the Error Handling node.

![](https://assets-docs.dify.ai/2025/01/c21f076398eb09d773d3e543561293e6.png)

4. Add an End Node to complete the configuration. Test the workflow by entering a query. If the response is correct, the setup is complete.

![](https://assets-docs.dify.ai/2025/01/820c37c70cb029cba60ca289e8d6e89a.png)

## FAQ

### 1. Connection Errors When Using Docker

If running Dify and Ollama inside Docker results in the following error:

```bash
httpconnectionpool(host=127.0.0.1, port=11434): max retries exceeded with url:/cpi/chat
(Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f8562812c20>:
fail to establish a new connection:[Errno 111] Connection refused'))
```

**Cause**:

Ollama is not accessible inside the Docker container because localhost refers to the container itself.

**Solution**:

**Setting environment variables on Mac**:

If Ollama is run as a macOS application, environment variables should be set using `launchctl`:

1.  For each environment variable, call `launchctl setenv`.

    ```bash
    launchctl setenv OLLAMA_HOST "0.0.0.0"
    ```
2. Restart Ollama application.
3.  If the above steps are ineffective, you can use the following method:

    The issue lies within Docker itself, and to access the Docker host. You should connect to `host.docker.internal`. Therefore, replacing `localhost` with `host.docker.internal` in the service will make it work effectively.

    ```bash
    http://host.docker.internal:11434
    ```

**Setting environment variables on Linux**:

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

**Setting environment variables on Windows**:

On windows, Ollama inherits your user and system environment variables.

1. First Quit Ollama by clicking on it in the task bar.
2. Edit system environment variables from the control panel.
3. Edit or create New variable(s) for your user account for `OLLAMA_HOST`, `OLLAMA_MODELS`, etc.
4. Click OK/Apply to save.
5. Run `ollama` from a new terminal window.

### 2. How to Modify the Address and Port of Ollama Service?

Ollama binds 127.0.0.1 port 11434 by default. Change the bind address with the `OLLAMA_HOST` environment variable.
