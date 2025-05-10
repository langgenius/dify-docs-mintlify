# AI Sales Avatar 的探索

—— Dify × TEN × Trulience × Azure × Agora × OpenAI 集成实践 ——

本指南面向全球 🌍 企业开发者和个人探索者，我们将用最简单易懂的方式，  
一步步搭建一个会 “听、说、想、演” 的 AI 数字销售助理。  
本次选择的应用场景是：**名品车 AI 数字导购**，她的名字叫 **Vendy**。

---

在正式开始搭建之前，我衷心感谢 Dify、TEN、Agora 和 Azure 团队给予的指导与鼓励。  
正是全球开源社区所秉持的**探索、共创与赋能**精神，  
让像我这样的从零起步的 AI 共建探索者也有机会将设想落地，  
实现这一端到端的集成方案。

---

我希望这份文档能为全球更多 AI 探索者提供：

**一条实用、可复用的路径**，  
降低动手门槛，推动 AX（AI Transformation）在个体 × 企业 × 社会层面的真正落地与赋能。

若您发现文中存在不足或改进空间，欢迎随时联系我。

---

💡 **我坚信：**

> **AI 源于人、发展于人，其根本目的，是为守护人的尊严与自由。**  
>  
> 技术的进步，唯有与人的价值共振，才能真正成为每一个人的力量。

---

**作者**：Alec Lee｜AX 全球战略师 & 全栈探索者  
 跨越文化与系统，共创 **“以一当千，不落一人”** 的AX新时代。

**日期**：2025 年 5 月 11 日  
**E-Mail**：alec.lee1005@gmail.com

## 一、“会听说想演”的 AI 数字人助理由哪六大平台构成？

本项目以 **TEN 平台为中枢**，集成以下六大平台，  
构建一个具备完整对话能力的名品车 AI 销售数字人（AI Sales Avatar）——**Vendy**。

她能“**听、说、想、演**”——  
也就是：**聆听用户提问、思考应答、语音回复，并以数字人形象呈现**。

👇 下图展示了系统整体集成架构图：

![AI Sales Avatar](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/001AIsalesAvatar.jpg)

## 🧩 各平台在系统中的角色分工：

👇 下图展示了系统中各平台的集成模块与工作流程：

![Trulience 工作模块图](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/002Trulience.jpg)

## 📌 各平台功能说明：

- **Dify + OpenAI**：搭建智能体，支持调用企业内部数据与 OpenAI API，并向 TEN 提供统一的对话接口（API）。

- **Trulience**：提供数字人演绎能力，向 TEN 提供数字人 ID 与访问 Token，用于虚拟形象呈现。

- **Agora**：实现语音通信与视频通话，向 TEN 提供 App ID 与 Certificate（证书）。

- **Azure Speech**：提供语音识别（STT）与语音合成（TTS）服务，向 TEN 提供以下参数：  
  `AZURE_STT_KEY`、`AZURE_STT_REGION`、`AZURE_TTS_KEY`、`AZURE_TTS_REGION`

- **TEN（平台中枢）**：作为系统的中枢平台，统一集成并调度上述所有平台的 API、密钥与 Token，  
  实现 AI Sales Avatar —— **Vendy** 的整体智能对话流程与实时互动能力。

---

📌 **小提示**：上述平台均可根据实际需求，替换为其他开源或 SaaS 方案。  
本项目所用组合为参考示例，便于学习与复用。

---

## 二、开始搭建（每一步都像玩乐高）

我们首先将在 Dify 上完成三步操作，搭建出一个基于内部数据的 AI Sales Avatar “本体”。  
演示场景是：**名品车导购数字人**，她的名字叫 **Vendy**。

---

### 🧩 Step 1：注册 Dify 账号并配置模型 API

👉 打开 Dify 官网： [https://dify.ai/](https://dify.ai/)，点击右上角 “Get Started”，开始注册流程。

![Dify AI](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/003DifyAIsales.jpg)

你可以使用以下方式登录或注册账号：**GitHub**、**Gmail**，或 **Hotmail**。

![Dify Email](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/004DifyEmail.jpg)

登录 Dify 后，在左侧菜单点击 **「Settings > Model Provider」（模型提供商）**。  
在页面中找到 **OpenAI** 模块，点击 **Install** 进行安装。

![Dify Models](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/005DifyModels.jpg)

在 **OpenAI** 模块中，点击蓝色链接 **「Get your API Key from OpenAI」**，  
系统会自动跳转到 OpenAI 官方平台：[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)。

![Dify OpenAI](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/006DifyOpenAI.jpg)

在 OpenAI 上点击 **「+ Create new secret key」** 生成新的 API 密钥。  
复制生成的 Key，并返回 Dify，在 OpenAI 模块中粘贴如下字段：

![Dify OpenAI Key](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/007DifyOpenAIKey.jpg)

完成模型配置后，我们已经准备好了运行环境，  
现在可以开始在 Dify 上构建 AI Sales Avatar 的知识本体了。

---

### 🧩 Step 2：上传 AI Sales Avatar 所需的内部资料（知识文档）

在 Dify 控制台顶部菜单，点击 **「Knowledge」**，  
然后点击 **「Create Knowledge」** 创建一个新的知识数据集。

![Dify Data](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/008Difydatasets.jpg)

在接下来的页面中，选择资料上传方式，推荐使用 **「Import from file」** 方式。

👇 如下图所示：

![DifyUpload](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/009DifydataImport.jpg)

请上传你已经准备好的企业内部资料，如产品介绍、销售手册、常见问题文档等。  
若你还没有准备相关资料，也可以用 ChatGPT 辅助生成内容。

👇 例如我们用 ChatGPT 生成了一个名品车品牌介绍的 Word 文档（Lexus、Audi、BMW 等）：

![ChatGPTUpload](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/010DifydataChatGPT.jpg)

下载好文档后，回到 Dify 上传页面，选择 **「Import from file」**，上传该文件。  
上传成功后，点击右下角的 **「Next」**，继续下一步设置。

![Dify Next](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/011DifyImportNext.jpg)

默认设置已经适用于大多数场景，建议保持原样，直接点击 **「Save & Process」** 即可。  
（如需后续提升智能体的理解精度，也可根据实际需求调整相关参数）

![Dify 知识库配置保存与处理](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/012DifyEmbedding.jpg)

✅ 若你看到以下页面，表示你的文档已经成功上传并被 Dify 系统解析完成。

![DifydataSet](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/013DifyDataUploadSucess.jpg)

到这里，我们已经完成了智能体知识库的构建部分，  
下一步，我们将创建一个智能体应用，并接入这个知识库！

---

### 🧩 Step 3：创建智能体 App，并接入知识库

进入 Dify 控制台，点击顶部菜单栏的 **「Studio」**，再点击右上角的 **「Create」** 创建新 App。

在弹出窗口中填写以下内容：

- **App Name & Icon**：如 `AI Sales Avatar`
- **Description**：
Your name is Vendy, the AI Clerk of Luxury Cars.
Your task is to provide information about luxury cars to the customers based on the knowledge.

👇 设置界面如下所示：

![DifyAvatar](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/014DifySalesAvatarSetting.jpg)

点击 **Create** 后，会进入 App 的 **Orchestrate** 编辑界面。

在 **INSTRUCTION** 栏中填写与刚才 **Description** 一致的内容：

Your name is Vendy, the AI Clerk of Luxury Cars.
Your task is to provide information about luxury cars to the customers based on the knowledge.

然后，在下方的 **Knowledge** 区块中，选择我们刚刚上传的知识文档作为参考资料。

👇 配置界面如下所示：

![Dify AvatarData](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/015DifyAvatarData.jpg)

配置完成后，可以在右侧输入框测试是否能正常调用知识库内容。  
如果返回的内容基于上传的文档，就说明智能体连接成功 ✅

测试无误后，点击右上角的 **「Publish」**，发布这个 AI 应用。

![Dify AvatarTest](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/016DifyAvataRunTest.jpg)

应用发布后，点击左侧菜单栏中的 **「API Access」**，进入后点击右上角的 **「Create Secret Key」**。
这个 API Key 是后续在 TEN 平台接入时必须使用的，请务必复制保存好。

👇 接口密钥生成界面如下所示：

![Dify API Key](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/018DifyAPI2.jpg)

🎉 恭喜你！至此，我们已经完成了 AI Sales Avatar 的“智能体本体”搭建，  
并成功获得了用于调用的 API Key。

接下来，我们将进入 **Trulience 平台**，为 AI Sales Avatar 生成她的 “数字人外貌与演绎能力” ——  
也就是构建她的虚拟形象，让她不仅能“听、说、想”，还能真实地出现在用户面前，与人互动！

📚 如需进一步了解 Dify，可参考官方技术文档：  
👉 [https://docs.dify.ai/en/introduction](https://docs.dify.ai/en/introduction)

---

### 🧩 Step 4：注册 Trulience 账号，获取数字人的 ID 和访问 Token

现在，我们将为 AI Sales Avatar 赋予一个可视化的 “数字人形象”！  
我们将使用 Trulience 平台来生成形象，并获取用于后续连接的 **Avatar ID** 与访问 **Token**。

✅ 操作流程如下：

1️⃣ 打开 Trulience 官网： [https://trulience.com](https://trulience.com)  
点击主页上的 **「Start For Free」** 按钮，开始注册账号。

👇 页面示意图如下：

![Trulience](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/019Trulience.jpg)

2️⃣ 注册完成后，进入后台界面。点击左侧菜单的 **「IMAGE AVATARS」**，  
选择一个女性角色作为 **Vendy** 的外貌，点击绿色按钮 **「Create Avatar」** 生成数字人。

👇 选择与创建界面示意图如下：

![Trulience Avatar](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/020TrulienceAvatar.jpg)

---

3️⃣ 当你看到 **“Avatar created”** 的提示时，说明数字人已经成功创建。

👇 创建成功提示界面如下所示：

![TrulienceAvatar2](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/021TrulieceAvatarCreation.jpg)

3️⃣ 我们将左侧的名称从默认的 **Amanda** 修改为 **Vendy**，  
此时你可以在下方看到她专属的 **Avatar ID**。

👇 如下图所示：

![Trulience 修改为 Vendy 并查看 Avatar ID](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/022TrulienceAvatarName.jpg)

---

4️⃣ 接下来，点击底部按钮 **「Connect」**，浏览器会跳转到一个新的页面。  
请从网页地址（URL）中复制 `token=` 后面的那段字符串，  
这就是你的 **访问 Token**。

建议将 **Avatar ID** 与 **Token** 一并复制保存好，稍后将在 TEN 平台中使用。

---

🎉 恭喜你！  
我们已经完成了 AI Sales Avatar 的“**外貌搭建**”，并成功获得了她的 Avatar ID 与访问 Token！

接下来就进入最后一步：  
我们将把 Dify 的智能体 + Trulience 的数字人，  
一并接入 **TEN 平台**，构建真正“听说想演”一体化的实时语音 AI 代理！

📚 如需进一步了解 Trulience，可参考官方技术文档：  
👉 [https://www.trulience.com/docs#/](https://www.trulience.com/docs#/)

---

## 🧩 Step 5：在本地搭建 TEN Agent 平台前，我们需要准备这三项配置

在将 Dify 的智能体、Trulience 的数字人接入 TEN 平台之前，  
我们需要提前准备好语音通信和语音识别/合成所需的账号与密钥，主要包括以下三项：

---

### ✅ 1. Agora 实时语音通信参数

TEN 使用 **Agora** 来实现语音通话能力（“她会说话”），需要准备以下参数：

- `AGORA_APP_ID=`（App ID）  
- `AGORA_CERTIFICATE=`（Certificate）

👉 获取方式：  
登录 Agora 控制台 [https://console.agora.io](https://console.agora.io) 创建一个新项目后，即可获取上述信息。

👇 控制台页面如下：

![Agora Project](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/023Agora.jpg)

登录账号后，点击左侧栏的 **「Projects」**，  
再点击右上角的 **「Create New」** 创建一个新项目。

👇 创建项目入口界面如下：

![AgoraNew](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/024AgoraCreate.jpg)

---

### 📝 输入项说明：

- **Project Name**：填写为 `AISalesAvatar`
- **Use Case**：选择合适的用途，例如 `Enterprise Collaboration`
- **Authentication Mode**：选择 **Secure Mode: APP ID + Token（推荐）**

填写完成后，点击 **「Submit」** 完成项目创建。

👇 创建成功后，即可获取 App ID 和 Certificate：

![Agora APP ID](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/025AgoraAPPID.jpg)

项目创建成功后，将跳转到项目管理页面。  
在项目列表中，点击 **App ID** 后方的复制按钮，即可获取 **App ID**。

👇 如图所示：

![AgoraApp IDGet](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/026AgoraAPPID2.jpg)

---

在获取 App ID 后，继续点击项目右侧的 ✏️ **铅笔图标（编辑按钮）**，进入项目详情页。

在页面底部的 **Primary Certificate** 区域，点击右侧的复制按钮，  
即可复制该项目的 **Certificate**。

👇 如下图所示：

![Agora Certificate](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/027AgoraCertificate.jpg)

至此，我们已经成功获取 **Agora 的 App ID 和 Primary Certificate**，  
为后续在 TEN 平台启用语音通信功能做好了准备。

📚 如需进一步了解，可参考官方技术文档：  
👉 [https://docs.agora.io/en/video-calling/get-started/manage-agora-account?platform=web#create-an-agora-project](https://docs.agora.io/en/video-calling/get-started/manage-agora-account?platform=web#create-an-agora-project)

---

### ✅ 2. Azure Speech 参数（语音识别 + 语音合成）

**Azure** 负责将用户的语音转为文字（STT），并将 AI 回复转成语音（TTS）。  
需要准备以下 4 个环境变量：

AZURE_STT_KEY= ；AZURE_STT_REGION= ；AZURE_TTS_KEY= ；AZURE_TTS_REGION= 。

👉 获取方式如下：

打开 Azure Portal，请登录 Azure 官方门户网站：  
🔗 [https://portal.azure.com](https://portal.azure.com)

在首页点击左上角的 **「Create a resource（创建资源）」**，  
在搜索栏中输入 **Azure OpenAI**，点击进入创建页面。

👇 创建入口界面如下：

![Azure Resource](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/028Azure.jpg)

---

参考以下内容，填写基本信息（**Basics**）：

![Azure OpenAI List](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/029AzureOpenAI.jpg)

---

通常默认选择 **「公共访问」** 即可，允许服务通过互联网访问：

![Azure OpenAI Public](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/030AzureCreateAzureOpenAI.jpg)

🧩 可选步骤：你可以为资源添加如 `project=ai-agent` 等标签，便于后续分类与管理。

👇 标签与网络配置界面如下：

![Azure resourceset](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/031AzureNetwork.jpg)

---

📝 确认填写信息无误后，点击 **「Create（创建）」** 按钮，即可开始部署 Azure OpenAI 服务资源。

👇 创建部署确认界面：

![Azure createconfirm](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/032AzureReview.jpg)

👇 资源部署中画面如下：

![Azure deploy](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/033AzureDeployment.jpg)

---

部署完成后，进入 **Azure AI Foundry**，你将看到如下欢迎界面，  
可用于快速创建项目与选择模型：

![Azure AI Foundry](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/034AzureAIFoundry.jpg)

---

进入 **「Model Catalog（模型目录）」** 页面后，选择 **Azure AI Speech**：

![Azure Speech model](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/035AzureModels.jpg)

点击 **Azure-AI-Speech** 模型后，进入其详细页面，  
点击页面上方的 **「Use Service」** 按钮，即可跳转进入 Speech Playground 页面：

![Azure Speech entry](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/036AzureUseService.jpg)

进入 **Speech Playground**，选择你的语音服务资源（如下图所示），  
即可看到对应的 **API Key** 和 **Region**：

![Azure STT KeyRegion](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/037AzureSTTKey.jpg)

---

点击 **「Text to Speech」** 标签，进入 **Voice Gallery**，  
可试听多种语音风格，选择最适合你 AI Avatar 的声音类型：

![Azure TTS](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/038AzureTTSmodels.jpg)

---

点击 **「View Code」**，即可复制当前语音服务的 **API Key 和 Region**：

![AzureAPI KeyRegion](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/039AzureTTSKey.jpg)

---

🎉 **恭喜你！**  
至此，我们已经完成了 **TEN 平台运行所需的所有参数准备工作 ✅**

---

### 🧱 下一步，我们就可以正式在本地启动 TEN Agent 平台，  
并将前面搭建的所有模块：

- 🧠 智能体（Dify）
- 🔊 语音能力（Azure Speech + Agora）
- 👩‍💻 虚拟形象（Trulience）

**完整串联起来，构建真正“听说想演”的实时 AI 数字销售助理！**

---

📚 如需进一步了解 Azure Speech 与 OpenAI 服务部署，参考官方文档：  
👉 [https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)

## 🧩 Step 6：在 Mac 上本地部署 TEN Agent 的开发环境

为了运行并调试 AI Sales Avatar 的语音交互系统，  
我们需要在本地准备好 **TEN Agent 的开发环境**。

---

### 🔧 所需工具与安装方式一览：

| 工具     | 功能说明                  | 安装方式                         |
|----------|---------------------------|----------------------------------|
| Docker   | 运行 TEN 的容器环境        | 官网下载安装 Docker Desktop     |
| Git      | 克隆并管理 TEN 的代码仓库  | `brew install git`              |
| Node.js  | 运行前端代码（Playground） | `brew install node`             |

---

### ✅ ① 安装 Docker

💡 Docker 是 TEN 平台的核心运行环境，所有模块都将以容器形式部署。

- 打开官网链接：👉 [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)  
- 下载适用于 macOS 的 `.dmg` 安装包，并完成安装。
- 安装后，点击应用列表中的 Docker 图标启动。
- 等待顶部菜单栏的 🐳 图标变为绿色 表示已成功启动。
- 打开 Terminal，输入以下命令验证是否成功安装：
  ```bash
  docker -v

✅ ② 安装 Git
💡 Git 是用来克隆和管理 TEN 框架代码的版本控制工具。

安装命令：brew install git; 验证安装：git -v

✅ ③ 安装 Node.js
💡 Node.js 是运行 TEN 的前端 Playground 所必需的环境。

安装命令：brew install node; 验证安装：node -v

✅ ④ 克隆 TEN Agent 框架代码
完成 Docker、Git、Node 安装后，下一步就是克隆 TEN Agent 的源代码，并配置 .env 环境变量。

🚀 1. 克隆 TEN Agent 代码仓库
在 Terminal 中执行以下命令：git clone https://github.com/TEN-Framework/TEN-Agent.git

执行后，会在本地创建一个 TEN-Agent 文件夹，
其中包含所有运行所需的代码和配置文件。

👇 如下图所示：

![TEN Clone](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/040TEN.jpg)

📦 2. 进入项目目录并复制环境变量模板
进入 ai_agents 子目录，并复制环境变量文件：

cd TEN-Agent/ai_agents
cp .env.example .env

.env 是 TEN Agent 运行所需的环境变量配置文件，
接下来你需要手动编辑它，输入密钥信息（来自 Dify、Trulience、Azure、Agora）。

👇 示例界面如下：

![TEN Agent .env](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/041TEN.jpg)

✍ 3. 编辑 `.env` 文件，填写以下变量：

请使用文本编辑器（推荐使用 **Cursor** 或 **VS Code**）打开并编辑 `.env` 文件，  
在文件末尾添加以下内容（填写你自己的密钥和区域信息）：

Agora App ID 和 Certificate
AGORA_APP_ID=your_agora_app_id
AGORA_APP_CERTIFICATE=your_agora_certificate

Azure 语音识别（STT）参数
AZURE_STT_KEY=your_stt_key
AZURE_STT_REGION=your_stt_region

Azure 语音合成（TTS）参数
AZURE_TTS_KEY=your_tts_key
AZURE_TTS_REGION=your_tts_region

👇 编辑 `.env` 文件示意图如下：

![TEN .env](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/042TENCursor.jpg)

## ✅ Step ⑤：启动 TEN Agent 容器，编译并运行 Server

在 `.env` 环境变量配置完成后，下一步是正式启动 **TEN Agent 的容器环境**。

---

### 🐳 ① 启动容器

进入 `ai_agents` 目录并启动 Docker 容器服务：

cd ai_agents
docker compose up -d

这会启动以下容器服务：

ten_agent_dev：用于开发和运行 Agent

ten_agent_demo：示例 Agent

ten_agent_playground：前端交互页面

👇 项目结构示意图如下：

![TEN Agent ai_agents 目录结构](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/043TENaiagents.jpg)


🔧 ② 进入容器并编译 Agent Server
执行以下命令，进入开发容器：docker exec -it ten_agent_dev bash

进入容器后，执行初始化任务脚本来注册 Agent：task use

👇 项目结构示意图如下：

![task use](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/044TENtaskuse.jpg)

该命令将自动读取并链接 Agent 的配置文件（如 `manifest.json` 和 `property.json`），  
并自动安装所需依赖包。

👇 执行过程示意图如下：

![TEN task run](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/045TENTaskRun.jpg)

✅ 完成 `task run` 后，在浏览器中访问以下地址以打开前端页面：

👉 [https://localhost:49483]

如果运行成功，你将看到如下界面：

点击页面上方的 **「Graph」** 选项卡。

在下拉框中选择：  
➡️ **`voice_assistant_intergrated_stt (Auto Start)`**，  
然后点击右下角的 **「Save」** 保存配置。

👇 页面示意图如下：

![TEN Agent Playground](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/046TEN494483.jpg)

✅ 替换语音合成（TTS）模块为 **Azure 引擎**

1. 找到图中的 **TTS 模块**（如 `tts_default`）  
2. 鼠标右键点击该模块，选择 **「Replace Node with」**  
3. 在弹出的列表中选择 **`azure_tts`**

这样就完成了语音合成模块的替换.

👇 Azure TTS 模块替换示意图如下：

![TEN Agent Azure TTS Change](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/047TENAzuretts.jpg)

🎙️ 关于数字人的声音设置（TTS 语音）

我们可以根据数字人的形象需求，自定义她的声音。  
在 Microsoft 提供的语音服务页面中，列出了所有支持的语音名称。

👉 访问地址如下：  
[https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#multilingual-voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#multilingual-voices)

---

在本例中，我们选择的是一位英文女声：  
🗣️ **`en-US-AshleyNeural`**

在 Azure TTS 模块中，请将以下字段填写为：
Azure_synthesis_voice_name=en-US-AshleyNeural

👇 Azure TTS 语音名称设置示意图如下：

![TEN Azure_synthesis_voice_name](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/048TENAzureVoice.jpg)

🔁 替换 LLM 模块为 Dify 接口，连接 Dify 智能体

1. 右键点击 **`llm` 模块**，选择 **「Replace Node with」**  
2. 在弹出的列表中选择 **`dify_python`**

这样即可将 TEN Agent 的大语言模型（LLM）模块，接入 Dify 提供的智能体接口。

👇 操作示意图如下：

![TEN Agent Dify](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/049TENDifyAPI.jpg)

2️⃣ 完成替换后，再次右键点击新生成的 **`dify_python` 模块**，  
点击 **「Update Properties」**，进入属性设置页面。

- 在 **API Key** 字段中，输入你在 Dify 平台上创建的 API Key  
- 在 **Greeting** 字段中，可以根据需求自定义欢迎语（如欢迎语音问候）

👇 设置界面示意图如下：

![TEN AgentDify API KeyGreeting](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/050TENDifyAPI2.jpg)

✅ 启动 TEN Agent 并连接 Trulience 数字人

---

### 🚀 启动前端页面

配置完成后，打开浏览器，访问以下地址，即可进入 TEN Agent 启动界面：

👉 [http://localhost:3000](http://localhost:3000)

👇 页面示意图如下：

![TEN Agent](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/051TEN3000.jpg)

🧠 选择智能体流程图（Graph）

1. 点击右上角的 **「Select Graph」**，在下拉菜单中选择：  
   ➤ `voice_assistant_integrated_stt`

2. 勾选 **「Enable Trulience Avatar」**，并填写以下字段：

   - **Avatar ID**（在 Trulience 创建数字人时获得）
   - **Avatar Token**（点击 Connect 后，从浏览器地址栏中复制）

3. 填写完成后，点击 **「Save changes」** 保存设置。

👇 配置界面如下图所示：

![TEN AgentTrulience](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/052TENTrulienceGrah.jpg)

🗣️ 启动语音互动，测试数字人是否连通成功

✅ 点击右上角的 **「Connect」** 按钮，完成最后测试。

如果一切配置正确，将出现以下情景：

- 🧍 数字人形象自动加载显示  
- 🗣️ 她会用自然语音向你问候，并提问，例如：  
  _“我能为你介绍哪几款豪华车？”_

- 🤖 你可以根据她的回答，验证她是否成功读取并理解了 Dify 知识库的内容。

👇 运行示意图如下：

![TEN AgentTalk](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/053TrulienceDifyFinal.jpg)

🎯 恭喜你！你现在已经拥有了完整的 **AI Sales Avatar**！

---
✅ 来自 **OpenAI / Dify** 的聊天大脑  
✅ 使用 **Azure** 的自然语音合成能力（女声）  
✅ 拥有 **Trulience** 的数字人形象  
✅ 构建于 **TEN 平台** 的语音交互能力
---
🌟 这就是 AI Agent 最核心的完整链路：  
**“听 → 想 → 说 → 演 → 链接”**
---

📚 如需进一步了解，可参考 TEN 官方技术文档：  
👉 [https://theten.ai/docs/ten_agent/architecture_flow](https://theten.ai/docs/ten_agent/architecture_flow)

## 🛠️ 下一步扩展建议（基于 AX 架构）

在目前已搭建的「AI Sales Avatar」基础上，  
我们可以依照 **AX Architecture** 的路径，进一步扩展它在实际业务场景中的能力，  
逐步打通：  
**数据 → 模型 → 代理 → 用户接口 → 全业务生命周期管理** 的闭环链路。

---

### 🧑‍💼 嵌入网页首页，作为公司虚拟形象代表

结合 **Trulience** 的 D-Human & Avatar 能力，  
将当前数字人部署到公司首页或 Web App，  
通过自然语音问答引导访客、收集意图，构建以用户为中心的入口，承接：

- `Marketing Info`  
- `Customer Lifecycle`

---

### 📦 接入数据库 & 订单管理系统，进阶为“AI 销售代表”

将 Avatar 与公司内部系统对接，例如：

- CRM、ERP、OA、订单系统（如 Salesforce、SAP、Notion DB 等）

实现：
- 销售线索管理  
- 库存查询  
- 合同生成等闭环任务  
服务于：

- `Contract Lifecycle`  
- `Asset Lifecycle`
---

### 🔗 接入企业核心平台：从“个体应用”迈向“组织级协同”

你可以进一步将 Agent PF（平台）能力模块化，  
嵌入不同 BU 的 Data Lake 与工作流管理平台，  
实现以下多业务融合扩展场景：

- AI + Finance  
- AI + HR  
- AI + R&D  
- AI + SNS（协作）

最终推动企业整体的 AI 转型升级。

## ✨ 写在最后：一点感言

我始终相信，AI 不应只是冰冷和强大的工具，  
它更可以是人类温暖的伙伴，是个体能力的延伸与放大器。

未来，也许会有越来越多像 “**Vendy**” 这样的数字伙伴，在世界各地悄然诞生——  
她们**倾听、思考、回应、表达**，用技术的力量，守护人的尊严与创造力。

---

📣 若您也愿意加入这场全球共创的旅程，  
欢迎携手探索与分享，让每一位个体都有机会与 AI 一同成长，  
共同探索 **“一以当千、不落一人”** 的 AX 新时代。

---

谨以此文作为一次小小的尝试与记录，  
愿它化作一颗微小的种子，  
在人与 AI 和谐共生的未来中，**悄然生根、缓缓发芽。**
