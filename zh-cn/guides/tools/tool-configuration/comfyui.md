# ComfyUI

{% hint style="warning" %}
“工具”已全面升级为“插件”生态，详细的使用说明请参考[插件开发](https://docs.dify.ai/zh-hans/plugins/quick-start/install-plugins)。以下内容已归档。
{% endhint %}

[ComfyUI](https://www.comfy.org/) 是一个强大的、模块化的生成图形的平台。现在你可以在 Dify 中使用它， 传入图片的提示词或图片文件， 得到生成的图片。

## 1. 确保已能正常运行 ComfyUI 的工作流
请参考其[官方文档](https://docs.comfy.org/get_started/gettingstarted)，确保 ComfyUI 可以正常运行并生成图片。

## 2. 提示词设置
如果你不需要通过dify传入提示词，可以跳过此步。如果你的提示词节点连接到了 ComfyUI 中唯一的 `KSampler` 节点，那么你可以跳过此步。  
否则，请使用字符串 `{{positive_prompt}}` 替换掉正向提示词内容，`{{negative_prompt}}` 替换掉负向提示词内容。
![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/4e937df93709ca5a47c5c17e17498f38.png)

## 3. 导出工作流的 API 文件
![](https://assets-docs.dify.ai/dify-enterprise-mintlify/zh_CN/guides/tools/tool-configuration/49794b23612f47245fabaf1eae207526.png)
如图所示，在工具栏中选择 `Save(API Format)`，如果没有该选择，则需要在设置中开启 `Dev Mode`。

## 4. 在 Dify 中集成 ComfyUI  
在 `工具 > ComfyUI > 去认证` 中填写访问地址，如果你使用的 docker 部署的 Dify，这个地址一般是 `http://host.docker.internal:8188`。

## 5. 在 Dify 中使用 ComfyUI
打开其 `工作流` 工具，在 `WORKFLOW JSON` 中填入刚刚导出的 API 文件中的内容，就可以正常生成了。

## 6. 图片输入
有的 ComfyUI 工作流需要输入多张图片，在 dify 中会查找到 `WORKFLOW JSON` 中的每一个 `LoadImage` 节点，并按顺序填充用户输入的图片文件。

当你想改变这个顺序时，就可以通过填写 `图片节点ID列表` 来调整。例如你的工作流中35号、69号、87号节点需要传入图片，那么输入`69,35,87`则会向69号节点传入第一张图片。
