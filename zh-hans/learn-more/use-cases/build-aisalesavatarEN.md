# Exploring the AI Sales Avatar  
**Dify × TEN × Trulience × Azure × Agora × OpenAI Integration Guide**

---

This guide is designed for global 🌍 enterprise developers and individual explorers.  
We’ll walk you through building an AI-powered digital sales assistant capable of:

🧠 **Listening**  
🗣️ **Speaking**  
🤖 **Thinking**  
🎭 **Performing**

All through a real-world use case:  
> **Luxury Car AI Sales Avatar – Vendy**

---

### 🙏 Acknowledgements  
Before we begin, heartfelt thanks to the teams from **Dify**, **TEN**, **Agora**, and **Azure**  
for their guidance and encouragement. This project was made possible by the spirit of:

- ✨ Exploration  
- 🤝 Collaboration  
- 🚀 Empowerment  

It is this spirit that enabled me — a zero-to-one AI co-creator — to bring this idea to life.

> 💬 _“I hope this document provides a practical and reusable pathway for more AI explorers around the world —  
lowering technical barriers and enabling the real-world implementation of **AX (AI Transformation)**.”_

---

### 💡 I firmly believe:

> **AI is created by humans, developed by humans, and ultimately exists to protect human dignity and freedom.**  
Only when technology resonates with human values can it truly become a power for every individual.

---

**👤 Author**: Alec Lee ｜AX Global Strategist & Full-Stack Explorer  
_“Empowering one to stand for a thousand — leaving no one behind across cultures and systems.”_  

📅 **Date**: May 11, 2025  
📧 **Email**: [alec.lee1005@gmail.com](mailto:alec.lee1005@gmail.com)


---

## 1. What are the six platforms that power a “Listen–Think–Speak–Perform” AI Avatar?

This project is centered on the **TEN platform**, integrating six key systems to create **Vendy**, a luxury car AI sales avatar with full conversational capability.  
Vendy can:
- 👂 Listen to questions  
- 🧠 Think and respond  
- 🗣️ Speak answers  
- 🧍 Present herself as a digital human

👇 Below is the **architecture diagram** showing the full system integration:

---

## 🧩 Platform Roles Overview

👇 This diagram outlines the **role of each platform**, their **integration modules**, and the **collaboration workflow**:
<!-- (Insert diagram or list here in next section) -->



![AI Sales Avatar](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/001AIsalesAvatar.jpg)

## 🧩 Roles of Each Platform in the System

👇 The diagram below illustrates how each platform contributes within the system — including their integration modules and collaborative workflow:
<!-- (Insert architecture diagram or detailed list of platform roles below) -->

![Trulience ](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/002Trulience.jpg)

## 📌 Platform Functions Overview

### **Dify + OpenAI**  
Builds the **intelligent agent core**. It connects to both **internal enterprise data** and the **OpenAI API**, providing a **unified conversation API interface** to TEN.

### **Trulience**  
Enables **digital human rendering**. It provides a **digital human ID** and **access token** to TEN for **visual avatar presentation**.

### **Agora**  
Handles **voice and video communication**. It provides **App ID** and **Certificate** to TEN for **real-time interaction**.

### **Azure Speech**  
Offers **speech-to-text (STT)** and **text-to-speech (TTS)** services. It provides the following parameters to TEN:
- `AZURE_STT_KEY`  
- `AZURE_STT_REGION`  
- `AZURE_TTS_KEY`  
- `AZURE_TTS_REGION`

### **TEN (Central Platform)**  
Serves as the **orchestration hub**, integrating and managing APIs, keys, and tokens from all platforms.  
TEN enables **Vendy**, the AI Sales Avatar, to conduct **intelligent conversations** and **real-time interactions**.

> 📌 **Note:** Each of the platforms above can be substituted with alternative open-source or SaaS services depending on your use case.  
> The current combination is a reference setup, designed for **learning** and **reusability**.

---

## 2. Let’s Build! (Think of it like assembling LEGO 🧱)

We’ll start with three simple steps in **Dify** to build the **“core intelligence”** of our AI Sales Avatar — based on **internal company data**.  
Our demo scenario: a **luxury car sales assistant** named **Vendy**.

---

### 🧩 Step 1: Register a Dify Account & Configure Model API

👉 Go to the official Dify website: [https://dify.ai/](https://dify.ai/)  
Click "**Get Started**" in the top right corner to begin the registration process.


![Dify AI](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/003DifyAIsales.jpg)

You can sign up or log in using one of the following methods:：**GitHub**、**Gmail**，or **Hotmail**.

![Dify Email](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/004DifyEmail.jpg)

After logging into **Dify**, follow these steps:
Click **“Settings > Model Provider”** in the left-hand menu.
On the page, locate the **OpenAI** module and click **Install** to set it up.

![Dify Models](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/005DifyModels.jpg)

In the OpenAI module, click the blue link labeled **“Get your API Key from OpenAI”**.
You’ll be redirected to the official OpenAI platform：[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)。

![Dify OpenAI](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/006DifyOpenAI.jpg)

On the OpenAI platform, click **“+ Create new secret key”** to generate a new API key.
Copy the generated key.Return to **Dify**, and paste the key into the **OpenAI module** under the following fields:

![Dify OpenAI Key](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/007DifyOpenAIKey.jpg)

---

### 🧩 Step 2: Upload Internal Documents for the AI Sales Avatar

Once the model configuration is complete, your environment is ready.  
You can now begin building the **knowledge base** for your AI Sales Avatar in Dify.

1. In the **Dify console**, click **“Knowledge”** from the top menu.
2. Then click **“Create Knowledge”** to create a new **knowledge dataset**.

![Dify Data](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/008Difydatasets.jpg)

On the following page, choose your preferred method for uploading content.  
We recommend using the **“Import from file”** option for the most straightforward setup.

👇 As shown in the illustration below:

![DifyUpload](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/009DifydataImport.jpg)

Please upload your prepared internal documents — such as product brochures, sales manuals, FAQ sheets, and more.  
If you haven't prepared relevant materials yet, you can also use **ChatGPT** to help generate content.

👇 For example, we generated a Word document using ChatGPT that introduces several luxury car brands (e.g., **Lexus**, **Audi**, **BMW**, etc.):

![ChatGPTUpload](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/010DifydataChatGPT.jpg)

After downloading the document, return to the **Dify upload page**,  
select **“Import from file”**, and upload the prepared file.

✅ Once the upload is successful, click the **“Next”** button in the bottom-right corner to proceed to the next configuration step.

![Dify Next](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/011DifyImportNext.jpg)

The **default settings** are suitable for most use cases.  
We recommend keeping them as they are and simply clicking **“Save & Process”** to complete the setup.
> ⚙️ *(Optional)* If you later wish to improve the AI assistant’s comprehension accuracy,  
> you can adjust parameters based on your specific business needs.

![Dify Knowledge](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/012DifyEmbedding.jpg)

✅ If you see the following page, it means your document has been successfully uploaded and parsed by the Dify system.

![DifydataSet](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/013DifyDataUploadSucess.jpg)

---

At this point, we’ve completed the **knowledge base setup** —  
your AI Sales Avatar now has its foundational memory in place.

---

### 🧩 Step 3: Create an AI Application and Connect the Knowledge Base

1. In the **Dify console**, click the top menu item **“Studio”**.
2. Then, click the **“Create”** button in the upper-right corner to start building a new App.

In the pop-up window, fill in the following fields:

- **App Name & Icon**：Example: `AI Sales Avatar`
- **Description**：
Your name is Vendy, the AI Clerk of Luxury Cars.
Your task is to provide information about luxury cars to the customers based on the knowledge.

👇 The settings interface looks like this:

![DifyAvatar](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/014DifySalesAvatarSetting.jpg)

After clicking **“Create”**, you’ll be taken to the App’s **Orchestrate** editing interface.

In the **INSTRUCTION** section, enter content consistent with the earlier **Description**, such as:

Your name is Vendy, the AI Clerk of Luxury Cars.
Your task is to provide information about luxury cars to the customers based on the knowledge.

Next, scroll down to the **Knowledge** section.  

Select the **knowledge document** we uploaded earlier as the reference material for the AI application.

![Dify AvatarData](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/015DifyAvatarData.jpg)

Once the configuration is complete, use the **input box on the right side** of the Orchestrate interface to test your AI agent.
If the responses reference the content from your uploaded document, it means the **knowledge base integration is working correctly**.

After confirming everything works as expected, click the **“Publish”** button in the upper-right corner to officially launch your AI application.

![Dify AvatarTest](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/016DifyAvataRunTest.jpg)

After publishing the application, click **“API Access”** from the left-hand sidebar menu.  
Then click the **“Create Secret Key”** button in the upper-right corner.

This **API Key** is essential for integrating your AI application with the **TEN platform** in the next step.  
Please make sure to **copy and store it securely**.

👇 The secret key generation interface looks like this:

![Dify API Key](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/018DifyAPI2.jpg)

🎉 **Congratulations!**  
You’ve now completed the setup of your **AI Sales Avatar’s core intelligence** and successfully obtained the **API Key** required for integration.

Next, we’ll move into the **Trulience platform**, where we will design the **digital appearance and performance capabilities** of your AI Sales Avatar.

In other words — we will give her a **face, expression, and presence**, enabling her to not only “listen, speak, and think,” but also to **appear on screen and interact with users in a human-like manner**!

📚 To learn more about Dify, visit the official documentation:  
👉 [https://docs.dify.ai/en/introduction](https://docs.dify.ai/en/introduction)

---

### 🧩 Step 4: Register a Trulience Account and Get Your Digital Avatar ID & Token

Now it’s time to give your AI Sales Avatar a **visual identity**!  
We’ll use the **Trulience platform** to generate a digital human and retrieve the necessary **Avatar ID** and **Access Token** for integration.

✅ Follow these steps:

1️⃣ Go to the Trulience website: [https://trulience.com](https://trulience.com)  
Click the **“Start For Free”** button on the homepage to begin registration.

👇 Sample interface:

![Trulience](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/019Trulience.jpg)

2️⃣ After registration, you’ll be redirected to the dashboard.  
From the left-hand menu, click **“IMAGE AVATARS”**.

Choose a **female character** to represent **Vendy**’s appearance,  
then click the green **“Create Avatar”** button to generate the digital human.

👇 Sample interface for avatar selection and creation:

![Trulience Avatar](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/020TrulienceAvatar.jpg)

---

3️⃣ When you see the **“Avatar created”** message, it means your digital human has been successfully created.

👇 Confirmation screen after successful creation:

![TrulienceAvatar2](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/021TrulieceAvatarCreation.jpg)

3️⃣ Rename the default avatar name (e.g., **Amanda**) to **Vendy** using the field on the left panel.  
Once renamed, you’ll see her unique **Avatar ID** displayed below.

👇 Example view:
<!-- (Insert screenshot showing renamed avatar and Avatar ID) -->

![Trulience Vendy](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/022TrulienceAvatarName.jpg)

---

4️⃣ Next, click the **“Connect”** button at the bottom of the screen.  
Your browser will redirect to a new page.

From the **URL**, copy the string that comes after `token=` —  
this is your **Access Token**.

---

🎉 **Congratulations!**  
You’ve successfully completed the **visual appearance setup** for your AI Sales Avatar,  
and obtained both the **Avatar ID** and **Access Token**.

---

## 🧩 Step 5: Connect Everything in TEN for Real-Time Voice AI Agent

Now it’s time for the final step:  
We’ll integrate the **intelligent core from Dify** and the **digital human from Trulience**  
into the **TEN platform**, building a truly unified AI agent that can **listen, speak, think, and perform** — all in real time!

> 📚 To learn more about Trulience, visit the official documentation:  
👉 [https://www.trulience.com/docs#/](https://www.trulience.com/docs#/)

---

## 🧩 Step 5: Prepare Three Key Configurations Before Running TEN Agent Locally

Before integrating the **Dify agent** and **Trulience digital human** into the TEN platform,  
we need to set up the accounts and credentials required for voice communication and speech processing.

Specifically, you’ll need to prepare the following three components:

---

### ✅ 1. Agora Real-Time Voice Communication Parameters

TEN uses **Agora** to enable real-time voice interactions (i.e., “she can speak”).  
You’ll need the following parameters:

- `AGORA_APP_ID=`（App ID）  
- `AGORA_CERTIFICATE=`（Certificate）

👉 **How to get it:**  
Log in to the Agora Console: [https://console.agora.io](https://console.agora.io)  
Create a new project, and you’ll be able to access the required parameters.

👇 Sample view of the Agora Console:

![Agora Project](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/023Agora.jpg)

After logging in, click **“Projects”** from the left sidebar.  
Then, click **“Create New”** in the top-right corner to create a new project.

👇 Project creation interface:

![AgoraNew](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/024AgoraCreate.jpg)

---

### 📝 Input Field Guide:

- **Project Name**: Use something like `AISalesAvatar`
- **Use Case**: Select an appropriate option, e.g., `Enterprise Collaboration`
- **Authentication Mode**: Choose **Secure Mode: APP ID + Token (Recommended)**

Once completed, click **“Submit”** to create the project.

👇 After successful creation, you will be able to access your **App ID** and **Certificate**:
<!-- (Insert screenshot showing the generated App ID and Certificate) -->

![Agora APP ID](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/025AgoraAPPID.jpg)

Once the project is created, you’ll be redirected to the project management page.  
In the project list, click the **copy icon** next to **App ID** to copy it.

👇 Example interface:

![AgoraApp IDGet](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/026AgoraAPPID2.jpg)

---

After copying the **App ID**, click the ✏️ **pencil icon** (Edit) on the right side of the project row to enter the **Project Details** page.

Scroll to the bottom of the page to find the **Primary Certificate** section.  
Click the **copy icon** to copy the project's **Certificate**.

👇 Example view:

![Agora Certificate](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/027AgoraCertificate.jpg)

At this point, you’ve successfully obtained the **Agora App ID** and **Primary Certificate**,  
completing the required setup for enabling **real-time voice communication** in the TEN platform.

> 📚 For more information, refer to the official Agora documentation:  
> [https://docs.agora.io](https://docs.agora.io)

📚 For more information, refer to the official Agora documentation:  
👉 [https://docs.agora.io/en/video-calling/get-started/manage-agora-account?platform=web#create-an-agora-project](https://docs.agora.io/en/video-calling/get-started/manage-agora-account?platform=web#create-an-agora-project)

---

### ✅ 2. Azure Speech Parameters (Speech-to-Text + Text-to-Speech)

**Azure** handles two critical voice functions:
- **STT (Speech-to-Text)**: Converts the user's spoken words into text  
- **TTS (Text-to-Speech)**: Converts the AI's text responses into speech

You’ll need to prepare the following four environment variables:

AZURE_STT_KEY= ；AZURE_STT_REGION= ；
AZURE_TTS_KEY= ；AZURE_TTS_REGION=.

![Azure Resource](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/028Azure.jpg)

---

Next, fill in the required fields under the **Basics** tab:
👇 Reference guide for the "Basics" section:

![Azure OpenAI List](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/029AzureOpenAI.jpg)

---

For most cases, selecting the default option **“Public access”** is sufficient,  
which allows the service to be accessed over the internet.

![Azure OpenAI Public](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/030AzureCreateAzureOpenAI.jpg)

🧩 **Optional Step:**  
You can add resource tags — for example, `project=ai-agent` — to help with future organization and management.

👇 Example view of the **Tags** and **Networking** configuration screen:

![Azure resourceset](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/031AzureNetwork.jpg)

---

📝 After reviewing and confirming that all information is correct,  
click the **“Create”** button to start deploying the Azure OpenAI resource.

👇 Deployment confirmation screen:

![Azure createconfirm](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/032AzureReview.jpg)

👇 Resource deployment in progress:

![Azure deploy](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/033AzureDeployment.jpg)

---

After deployment is complete, navigate to **Azure AI Foundry**.  
You’ll see the following welcome screen, which allows you to quickly create a project and select a model:

👇 Azure AI Foundry welcome interface:

![Azure AI Foundry](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/034AzureAIFoundry.jpg)

---

Go to the **“Model Catalog”** page and select **Azure AI Speech**.

👇 Model selection interface:

![Azure Speech model](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/035AzureModels.jpg)

After clicking the **Azure-AI-Speech** model, you’ll be taken to its details page.  
Click the **“Use Service”** button at the top of the page to jump to the **Speech Playground**.

👇 Speech service launch interface:

![Azure Speech entry](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/036AzureUseService.jpg)

Inside the **Speech Playground**, select your speech service resource (as shown below).  
You’ll then be able to view the corresponding **API Key** and **Region**.

👇 Speech service resource selection and key display:

![Azure STT KeyRegion](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/037AzureSTTKey.jpg)

---

Click the **“Text to Speech”** tab to enter the **Voice Gallery**,  
where you can preview various voice styles and select the one that best fits your AI Avatar.

👇 Voice Gallery interface for selecting speech styles:

![Azure TTS](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/038AzureTTSmodels.jpg)

---

Click the **“View Code”** button to copy the current speech service’s **API Key** and **Region**.

👇 Example interface for copying credentials:

![AzureAPI KeyRegion](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/039AzureTTSKey.jpg)

---

🎉 **Congratulations!**  
You’ve now completed all the required parameter preparations.
for running the **TEN platform** and connecting your AI Sales Avatar.

---

---

### 🧱 What’s Next: Launching the TEN Agent Platform Locally

Now we’re ready to **launch the TEN Agent platform on your local machine**,  
and connect all the components we’ve prepared:

- 🧠 **Intelligent Agent** (via Dify)  
- 🔊 **Voice Capabilities** (via Azure Speech + Agora)  
- 👩‍💻 **Digital Avatar** (via Trulience)

Together, these form a truly **real-time, embodied AI Sales Assistant**  
that can **listen, think, speak, and perform** — end to end.

Let’s build it!

---

📚 For more details on deploying Azure Speech and OpenAI services, refer to the official documentation: 
👉 [https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)

### 🧩 Step 6: Set Up the TEN Agent Development Environment on macOS

To run and test the AI Sales Avatar’s real-time voice interaction system,  
we first need to set up the **TEN Agent development environment** on your Mac.

---

### 🔧 Required Tools & Installation Guide

| Tool      | Purpose                                | Installation Method                     |
|-----------|----------------------------------------|-----------------------------------------|
| Docker    | Container environment for running TEN  | Download from the official Docker site  |
| Git       | Clone and manage the TEN codebase      | `brew install git`                      |
| Node.js   | Run the front-end (Playground)         | `brew install node`                     |


---

### ✅ ① Install Docker

💡 Docker is the core runtime environment for the TEN platform — all modules will run in containerized form.

Follow these steps:

- Open the official Docker website: 👉 [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)  
- Download the `.dmg` installer for macOS and complete the installation.
- After installation, launch Docker from your Applications folder.
- Wait until the 🐳 Docker icon in the top menu bar turns **green**, indicating it's running successfully.
- Open your Terminal and run the following command to verify the installation:

  Verify the installation: docker -v. If you see a version number, Docker is installed correctly.

### ✅ ② Install Git

💡 Git is a version control tool used to **clone and manage the TEN framework codebase**.

- Install Git using Homebrew:
  brew install git.
  Verify the installation: git -v. If a version number appears, Git is installed successfully.

### ✅ ③ Install Node.js

💡 Node.js is required to run the **TEN Playground frontend** locally.

- Install Node.js using Homebrew: brew install node
  Verify the installation: node -v. If a version number appears, Node.js has been installed successfully.


### ✅ ④ Clone the TEN Agent Codebase

Once Docker, Git, and Node.js are installed, the next step is to **clone the TEN Agent source code** and prepare the `.env` environment configuration.

🚀 **Step 1: Clone the TEN Agent GitHub repository**

Open your Terminal and run: git clone https://github.com/TEN-Framework/TEN-Agent.git

This will create a local folder named TEN-Agent,
containing all the necessary code and configuration files for the platform.

👇 Directory structure example:

![TEN Clone](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/040TEN.jpg)

📦 **Step 2: Navigate to the project directory and copy the environment variable template**

Change into the `ai_agents` subdirectory and copy the example `.env` file:

cd TEN-Agent/ai_agents
cp .env.example .env

The `.env` file contains the **environment variables required to run the TEN Agent**.

Next, you’ll need to **manually edit** this file and input the necessary credentials, including:

- Azure STT/TTS Keys and Regions  
- Agora App ID & Certificate

👇 Example view of the `.env` configuration file:

![TEN Agent .env](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/041TEN.jpg)

✍ **Step 3: Edit the `.env` File and Fill in the Following Variables**

Use a text editor (we recommend **Cursor** or **VS Code**) to open the `.env` file.  
Scroll to the end of the file and add the following variables — replacing the values with **your own credentials**:

Agora App ID and Certificate
AGORA_APP_ID=your_agora_app_id
AGORA_APP_CERTIFICATE=your_agora_certificate

Azure STT Parameters
AZURE_STT_KEY=your_stt_key
AZURE_STT_REGION=your_stt_region

Azure TTS Parameters
AZURE_TTS_KEY=your_tts_key
AZURE_TTS_REGION=your_tts_region

👇 Example view of the `.env` file being edited:

![TEN .env](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/042TENCursor.jpg)

## ✅ Step ⑤: Start the TEN Agent Container and Run the Server

Once your `.env` file has been properly configured,  the next step is to **launch the TEN Agent container environment**.

---

### 🐳 ① Start the Container

Navigate to the `ai_agents` directory and start the Docker container services:

cd ai_agents
docker compose up -d

This command will launch the following container services:

ten_agent_dev: Main development container for running the Agent

ten_agent_demo: Example agent instance

ten_agent_playground: Frontend interface for interactive testing

👇 Project structure example:

![TEN Agent ai_agents](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/043TENaiagents.jpg)


🔧 ② Enter the Container and Compile the Agent Server

Run the following command to access the development container:docker exec -it ten_agent_dev bash

🔧 ③ Run the Initialization Script to Register the Agent.

Once inside the container, execute the following command to register the Agent:task use

👇 Example of the project structure after initialization:

![task use](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/044TENtaskuse.jpg)

This command will automatically read and link the Agent’s configuration files  
(such as `manifest.json` and `property.json`),  
and install all necessary dependencies.

👇 Example output of the execution process:

![TEN task run](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/045TENTaskRun.jpg)

✅ After completing `task run`, open your browser and go to the following address to launch the frontend:

👉 [https://localhost:49483](https://localhost:49483)

If everything is running correctly, you should see the interface below:

- Click on the **“Graph”** tab at the top of the page.
- From the dropdown menu, select your desired Agent instance.

👇 Example UI view:

➡️ **`voice_assistant_intergrated_stt (Auto Start)`**，  
Then, click the **“Save”** button in the bottom-right corner to save your configuration.

👇 Sample interface view:

![TEN Agent Playground](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/046TEN494483.jpg)

✅ Replace the Text-to-Speech (TTS) Module with **Azure Engine**

1. Locate the **TTS module** in the graph (e.g., `tts_default`)  
2. Right-click on the module and select **“Replace Node with”**  
3. From the dropdown list, choose **`azure_tts`**

This completes the replacement of the TTS module with the Azure-based engine.

👇 Example view of replacing the TTS module with Azure TTS:

![TEN Agent Azure TTS Change](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/047TENAzuretts.jpg)

🎙️ **Customizing the Digital Human’s Voice (TTS Settings)**

You can customize the voice of your digital avatar to match her personality and appearance.  
Microsoft provides a full list of supported voice names in its speech service documentation.

👉 Visit the following link to browse available voices:   
[https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#multilingual-voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#multilingual-voices)

---

In this example, we selected an English female voice:  

🗣️ **`en-US-AshleyNeural`**

In the Azure TTS module, set the following field:

Azure_synthesis_voice_name=en-US-AshleyNeural

![TEN Azure_synthesis_voice_name](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/048TENAzureVoice.jpg)

🔁 **Replace the LLM Module with Dify API to Connect Your Intelligent Agent**

1. Right-click on the **`llm`** module and select **“Replace Node with”**  
2. From the popup list, choose **`dify_python`**

This will replace the default large language model (LLM) in TEN Agent with the Dify-powered intelligent agent interface.

👇 Example view of the replacement process:

![TEN Agent Dify](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/049TENDifyAPI.jpg)

2️⃣ After replacing the module, right-click the newly created **`dify_python`** node again  
and select **“Update Properties”** to open the configuration panel.

- In the **API Key** field, enter the API Key you created on the Dify platform  
- In the **Greeting** field, you can optionally customize a welcome message (e.g., a voice greeting)

👇 Example view of the Dify module property settings:

![TEN AgentDify API KeyGreeting](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/050TENDifyAPI2.jpg)

✅ 启动 TEN Agent 并连接 Trulience 数字人

---

### 🚀 Launch the Frontend Interface

Once configuration is complete, open your browser and navigate to the following address  
to access the TEN Agent launch interface:

👉 [http://localhost:3000](http://localhost:3000)

👇 Example view of the launch interface:

![TEN Agent](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/051TEN3000.jpg)

🧠 **Select the Agent Graph (Workflow)**

1. Click **“Select Graph”** in the upper-right corner, and from the dropdown menu choose:  
   ➤ `voice_assistant_integrated_stt`

2. Check the box for **“Enable Trulience Avatar”** and fill in the following fields:

   - **Avatar ID** (obtained during Trulience avatar creation)
   - **Avatar Token** (copied from the URL after clicking "Connect" in Trulience)

3. After completing the fields, click **“Save changes”** to apply the settings.

👇 Example view of the configuration screen:

![TEN AgentTrulience](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/052TENTrulienceGrah.jpg)

🗣️ **Start Voice Interaction and Verify Digital Human Connectivity**

✅ Click the **“Connect”** button in the upper-right corner to run the final test.

If everything is configured correctly, the following should happen:

- 🧍 The digital human avatar will load and appear on screen  
- 🗣️ She will greet you with natural speech and ask a question, such as:  
  _“Which luxury cars can I introduce to you today?”_

- 🤖 Based on her response, you can verify whether she successfully retrieved and understood content from the Dify knowledge base.

👇 Example view of the running interaction:

![TEN AgentTalk](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/053TrulienceDifyFinal.jpg)

---

🎯 **Congratulations!**  
You now have a fully functional **AI Sales Avatar**!

---

✅ A conversational brain powered by **OpenAI / Dify**  
✅ Natural voice synthesis (female voice) via **Azure**  
✅ A digital human appearance rendered by **Trulience**  
✅ Real-time voice interaction built on the **TEN platform**

---

🌟 This is the complete and essential chain of an AI Agent:  
**Listen → Think → Speak → Perform → Connect**

---

📚 To learn more, refer to the official TEN documentation:  
[https://github.com/TEN-Framework/TEN-Agent](https://github.com/TEN-Framework/TEN-Agent)

👉 [https://theten.ai/docs/ten_agent/architecture_flow](https://theten.ai/docs/ten_agent/architecture_flow)

## 🛠️ Next Step: Expansion Suggestions (Based on AX Architecture)

Building upon your current **AI Sales Avatar**,  
you can follow the **AX Architecture** roadmap to further enhance its capabilities in real-world business scenarios.

The goal is to gradually integrate a full-cycle loop of:

**Data → Model → Agent → User Interface → Full Business Lifecycle Management**

---

### 🧑‍💼 Embed on the Company Homepage as a Virtual Brand Representative

By integrating **Trulience**’s D-Human and Avatar capabilities,  
you can deploy your digital human onto the company homepage or web application.

Through natural voice-based Q&A, the avatar can guide visitors, capture their intent,  
and serve as a user-centric entry point that connects to:

- `Marketing Info`  
- `Customer Lifecycle`

---

### 📦 Integrate with Databases & Order Management Systems to Evolve into an “AI Sales Representative”

Connect the Avatar with internal enterprise systems such as:

- CRM, ERP, OA, and order management tools (e.g., Salesforce, SAP, Notion DB, etc.)

This enables the AI agent to perform end-to-end tasks like:

- Sales lead management  
- Inventory checks  
- Contract generation

Serving business processes such as:

- `Contract Lifecycle`  
- `Asset Lifecycle`

---

### 🔗 Integrate with Core Enterprise Platforms: From “Individual Use” to “Organizational Collaboration”

You can further modularize the Agent PF (platform) capabilities  
and embed them into the Data Lakes and workflow management platforms of various BUs.

This unlocks cross-functional integration scenarios such as:

- AI + Finance  
- AI + HR  
- AI + R&D  
- AI + SNS (Collaboration)

Ultimately, it paves the way for a company-wide AI transformation and upgrade.

---

### ✨ Final Reflections

I’ve always believed that AI should not merely be a cold, powerful tool —  
but also a **warm companion to humanity**,  
an extension and amplifier of our individual potential.

In the near future, we may see more digital companions like **“Vendy”** quietly emerge across the world —  
beings who **listen**, **think**, **respond**, and **express**,  
using the power of technology to uphold **human dignity and creativity**.

---

### 🤝 A Call for Co-Creation

If you, too, wish to join this global journey of co-creation,  
we warmly invite you to **explore, experiment, and share** —  
so that every individual can grow alongside AI,  
and together, we may step into the AX era of:

> **“One Against a Thousand — Leaving No One Behind.”**

---

### 🌱 A Humble Beginning

This document is just a small experiment — a seed of possibility.  
May it quietly take root, and gently begin to sprout  
in a future where **humans and AI coexist in harmony**.
