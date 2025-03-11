# Connecting to OpenLLM Local Deployed Models

With [OpenLLM](https://github.com/bentoml/OpenLLM), you can run inference with any open-source large-language models, deploy to the cloud or on-premises, and build powerful AI apps.
And Dify supports connecting to OpenLLM deployed large language model's inference capabilities locally.

## Deploy OpenLLM Model
### Starting OpenLLM

Each OpenLLM Server can deploy one model, and you can deploy it in the following way:

```bash
docker run --rm -it -p 3333:3000 ghcr.io/bentoml/openllm start facebook/opt-1.3b --backend pt
```

> Note: Using the `facebook/opt-1.3b` model here is only for demonstration, and the effect may not be good. Please choose the appropriate model according to the actual situation. For more models, please refer to: [Supported Model List](https://github.com/bentoml/OpenLLM#-supported-models).

After the model is deployed, use the connected model in Dify.

   Fill in under `Settings > Model Providers > OpenLLM`:

   - Model Name: `facebook/opt-1.3b`
   - Server URL: `http://<Machine_IP>:3333` Replace with your machine IP address

   Click "Save" and the model can be used in the application.

This instruction is only for quick connection as an example. For more features and information on using OpenLLM, please refer to: [OpenLLM](https://github.com/bentoml/OpenLLM)