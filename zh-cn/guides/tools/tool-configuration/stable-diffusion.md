# Stable Diffusion

> 工具作者 @Dify。

{% hint style="warning" %}
“工具”已全面升级为“插件”生态，详细的使用说明请参考[插件开发](https://docs.dify.ai/zh-hans/plugins/quick-start/install-plugins)。以下内容已归档。
{% endhint %}

StableDiffusion 是一种基于文本提示生成图像的工具，Dify 已经实现了访问 Stable Diffusion WebUI API 的接口，因此你可以直接在 Dify 中使用它。以下是在 Dify 中集成 Stable Diffusion 的步骤。

## 1. 初始化本地环境

推荐使用装有较强 GPU 的机器来安装和驱动 Stable Diffusion，但这并不是必须的，你也可以使用 CPU 来生成图像，但速度可能会很慢。

## 2. 安装并启动 Stable Diffusion WebUI

1. 从[官方仓库](https://github.com/AUTOMATIC1111/stable-diffusion-webui)克隆 Stable Diffusion WebUI 仓库
    
```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
```

2. 运行命令启动 Stable Diffusion WebUI。

克隆仓库后，切换到仓库目录。根据系统的不同，可能需要使用不同的命令来启动 WebUI。

#### Windows

```bash
cd stable-diffusion-webui
./webui.bat --api --listen
```

#### Linux
```bash
cd stable-diffusion-webui
./webui.sh --api --listen
```

3. 准备模型

现在你可以根据终端中显示的地址在浏览器中访问 Stable Diffusion WebUI，但模型还不可用。你需要从 HuggingFace 或其他来源下载模型，并将其放在 Stable Diffusion WebUI 的 `models` 目录中。

例如，我们使用 [pastel-mix](https://huggingface.co/JamesFlare/pastel-mix) 作为模型，使用 `git lfs` 下载模型并将其放在 `stable-diffusion-webui` 的 `models` 目录中。

```bash
git clone https://huggingface.co/JamesFlare/pastel-mix
```

4. 获取模型名称

现在你可以在模型列表中看到 `pastel-mix`，但我们仍然需要获取模型名称，访问 `http://your_id:port/sdapi/v1/sd-models`，你将看到如下的模型名称。

```json
[
    {
        "title": "pastel-mix/pastelmix-better-vae-fp32.ckpt [943a810f75]",
        "model_name": "pastel-mix_pastelmix-better-vae-fp32",
        "hash": "943a810f75",
        "sha256": "943a810f7538b32f9d81dc5adea3792c07219964c8a8734565931fcec90d762d",
        "filename": "/home/takatost/stable-diffusion-webui/models/Stable-diffusion/pastel-mix/pastelmix-better-vae-fp32.ckpt",
        "config": null
    },
]
```

`model_name` 就是我们需要的，这个例子中是 `pastel-mix_pastelmix-better-vae-fp32`。

## 3. 在 Dify 集成 Stable Diffusion

在 `工具 > StableDiffusion > 去认证` 中填写你在之前步骤中获取的认证信息和模型配置。

## 4. 完成

- **Chatflow / Workflow 应用**

Chatflow 和 Workflow 应用均支持添加 `Stable Diffusion` 工具节点。添加后，需要在节点内的 “输入变量 → 提示词” 内填写[变量](https://docs.dify.ai/v/zh-hans/guides/workflow/variables)引用用户输入的提示词，或者是上一节点生成的内容。最后在 “结束” 节点内使用变量引用 `Stable Diffusion` 输出的图像。

- **Agent 应用**

在 Agent 应用内添加 `Stable Diffusion` 工具，然后在对话框内发送图片描述，调用工具生成 AI 图像。
