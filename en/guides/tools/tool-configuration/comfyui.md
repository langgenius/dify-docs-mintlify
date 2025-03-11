# ComfyUI

{% hint style="warning" %}
"Tools" has been fully upgraded to the "Plugins". For more details, please refer to [Install and Use Plugins](https://docs.dify.ai/plugins/quick-start/install-plugins). The content below has been archived.
{% endhint %}


[ComfyUI](https://www.comfy.org/): The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. Now you can use it in dify, input the prompt or images, and get the generated image.

## 1. Ensure that the ComfyUI workflow is running normally.  
Please refer to its [official documentation](https://docs.comfy.org/get_started/gettingstarted) to ensure that ComfyUI can run normally and generate images.

## 2. Prompt setting
If you don't need dify to pass in the prompt, you can skip this step. If your prompt node is connected to the only `KSampler` node in ComfyUI, you can skip this step.  
Otherwise, use the string `{{positive_prompt}}` to replace the positive prompt content, and `{{negative_prompt}}` to replace the negative prompt content.
![](/en/.gitbook/assets/guides/tools/comfyui_prompt.png)

## 3. Export the API file of the workflow. 
![](/en/.gitbook/assets/guides/tools/comfyui.png)
As shown in the figure, select `Save(API Format)`, if there is no such selection, you need to enable `Dev Mode` in the settings.

## 4. Integrate ComfyUI in Dify  
Fill in the access address in `Tools > ComfyUI > Go to Authentication`, if you are using a docker deployment of Dify, this address is usually `http://host.docker.internal:8188`.

## 5. Use ComfyUI in Dify
Open its `Workflow` tool, fill in the content in the API file you just exported in `WORKFLOW JSON`, and you can generate normally.

## 6. Image input
Some ComfyUI workflows require multiple images inputs. In dify, it will find every `LoadImage` node in the `WORKFLOW JSON` and fill in the image files input by the user in order. When you want to change this order, you can adjust it by filling in the `Image node ID list`. For example, if your workflow needs to input images into the 35th, 69th, and 87th nodes, then input `69,35,87` will pass the first image to the 69th node.
