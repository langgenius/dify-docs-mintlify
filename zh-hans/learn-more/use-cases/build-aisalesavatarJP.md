# AIセールスアバターの探求

—— Dify × TEN × Trulience × Azure × Agora × OpenAI 統合実践ガイド ——

本ガイドは、世界中の 🌍 企業開発者および個人の探究者の方々を対象に、  
できるだけシンプルでわかりやすい方法で、  
「聞く・話す・考える・演じる」ことができるAIデジタルセールスアシスタントの構築手順を一歩ずつご紹介します。  

今回のユースケースは、**高級車のAIデジタル販売員**。彼女の名前は **Vendy** です。

---

構築を始める前に、**Dify、TEN、Agora、Azure** 各チームの皆様より  
多大なるご指導とご支援をいただきましたこと、心より御礼申し上げます。

本プロジェクトは、グローバルなオープンソースコミュニティが持つ  
**「探求・共創・賦能」** の精神によって支えられており、  
ゼロから始めた私のようなAI共創の探索者にも、  
この構想をエンドツーエンドで実現する機会が与えられました。

---

このドキュメントが、世界中のAI探究者にとって：

**実用的かつ再利用可能な道しるべ** となり、 ハンズオンのハードルを下げ、  
AX（AIトランスフォーメーション）を個人 × 企業 × 社会のレベルで真に実装・活用する後押しになれば幸いです。

もし改善点やお気づきの点がありましたら、ぜひご連絡ください。

---

💡 **私は信じています：**

> **AIは人により生まれ、人に育まれ、そして人の尊厳と自由を守るために存在する。**  
>  
> テクノロジーの進化は、人の価値観と共鳴してこそ、真に一人ひとりの力となる。

---

**著者**：Alec Lee｜AXグローバルストラテジスト & フルスタック・エクスプローラー  
　 文化やシステムを越え、「一騎当千」と「一人不遺」（＝誰一人も取り残さない）のAX新時代へ。

**日付**：2025年5月11日  
**Eメール**：[alec.lee1005@gmail.com](mailto:alec.lee1005@gmail.com)


## 一、「聞く・話す・考える・演じる」AIデジタルアシスタントは、どの6つのプラットフォームから構成されているのか？

本プロジェクトは、**TENプラットフォームを中枢**とし、  
以下の6つの主要プラットフォームを統合することで、  
高級車の販売を想定したAIセールスアバター（AI Sales Avatar）— **Vendy** を構築します。

---

Vendyは、以下の4つの能力を備えています：

- 👂「聞く」：ユーザーの質問を音声で受け取る  
- 🤔「考える」：質問に基づき思考・回答を生成する  
- 🗣️「話す」：自然な音声で応答を返す  
- 👤「演じる」：デジタルヒューマンとして画面上に現れ、表情を伴って表現する

👇 以下は、システム全体の統合アーキテクチャ図です：

![AI Sales Avatar](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/001AIsalesAvatar.jpg)

## 🧩 各プラットフォームにおける役割分担

👇 下図は、システム内で各プラットフォームが担うモジュールおよび  
統合されたワークフローの概要を示しています：

![Trulience 工作模块图](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/002Trulience.jpg)

## 📌 各プラットフォームの機能概要：

- **Dify + OpenAI**：  
  インテリジェントエージェントを構築し、社内データおよびOpenAI APIを活用。  
  TENプラットフォームに対し、統一された対話APIインターフェースを提供します。

- **Trulience**：  
  デジタルヒューマンの演出機能を提供。  
  TENに対し、アバターIDとアクセストークンを渡し、仮想キャラクターの表示を可能にします。

- **Agora**：  
  音声通信・ビデオ通話機能を提供。  
  TENに対して、App IDおよびCertificate（証明書）を提供します。

- **Azure Speech**：  
  音声認識（STT）および音声合成（TTS）サービスを提供。  
  TENには以下のパラメーターを渡します：  
  `AZURE_STT_KEY`、`AZURE_STT_REGION`、`AZURE_TTS_KEY`、`AZURE_TTS_REGION`

- **TEN（中枢プラットフォーム）**：  
  システムのオーケストレーションハブとして、上記すべてのAPI、キー、トークンを統合・管理。  
  AIセールスアバター **Vendy** によるインテリジェントな会話とリアルタイム対話機能を実現します。

---

📌 **補足**：  
上記プラットフォームは、ユースケースに応じて他のOSSやSaaSに置き換えることも可能です。  
本プロジェクトの構成は、学習および再利用を目的としたリファレンス例です。

---

## 二、構築を開始しよう（まるでLEGOを組み立てるように）

まずは Dify 上で3つのステップを行い、  
社内データに基づいた AI Sales Avatar の「本体」を構築します。  

今回のデモシナリオは：  
**高級車販売のデジタルアシスタント**、彼女の名前は **Vendy** です。

---

### 🧩 Step 1：Difyアカウントの登録とモデルAPIの設定

👉 Difyの公式サイトへアクセス： [https://dify.ai/](https://dify.ai/)  
右上の「Get Started」ボタンをクリックし、登録を開始します。

![Dify AI](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/003DifyAIsales.jpg)

アカウントの登録・ログインには、以下の方法が利用できます： **GitHub**、**Gmail**、または **Hotmail**

![Dify Email](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/004DifyEmail.jpg)

Difyにログインした後、左側メニューから **「Settings > Model Provider（モデルプロバイダー）」** をクリックします。  
ページ内の **OpenAI** モジュールを見つけて、**「Install」** をクリックし、インストールを行います。

![Dify Models](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/005DifyModels.jpg)

**OpenAI** モジュール内で、青色のリンク **「Get your API Key from OpenAI」** をクリックすると、  
OpenAI の公式プラットフォームへ：[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)。

![Dify OpenAI](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/006DifyOpenAI.jpg)

OpenAI の画面で **「+ Create new secret key」** をクリックし、新しい APIキー を生成します。  
生成されたキーをコピーし、Dify に戻って OpenAI モジュール内の以下のフィールドに貼り付けます：

![Dify OpenAI Key](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/007DifyOpenAIKey.jpg)

モデルの設定が完了すると、Dify上での実行環境の準備が整います。  
これで、AI Sales Avatar の「知識ベース（ナレッジ本体）」の構築を始めることができます。

---

### 🧩 Step 2：AI Sales Avatar に必要な内部資料（ナレッジドキュメント）をアップロードする

Dify のコンソール上部メニューから **「Knowledge」** をクリックし、  
続いて **「Create Knowledge」** を選択して、新しいナレッジデータセットを作成します。

![Dify Data](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/008Difydatasets.jpg)

次の画面で、ナレッジのアップロード方法を選択します。  
おすすめは、**「Import from file（ファイルからインポート）」** を選ぶ方法です。

👇 以下のような画面になります：

![DifyUpload](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/009DifydataImport.jpg)

あらかじめ用意しておいた社内資料（製品紹介、営業マニュアル、FAQドキュメントなど）をアップロードしてください。  
もし資料がまだ準備できていない場合は、ChatGPTを使ってコンテンツを生成することも可能です。

👇 例えば、私たちは ChatGPT を活用して、Lexus・Audi・BMW などの高級車ブランド紹介をまとめた Word ドキュメントを作成しました：

![ChatGPTUpload](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/010DifydataChatGPT.jpg)

ドキュメントをダウンロードしたら、Difyのアップロード画面に戻り、  
**「Import from file」** を選択して該当ファイルをアップロードします。  

アップロードが完了したら、画面右下の **「Next」** をクリックして、次の設定ステップへ進みます。

![Dify Next](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/011DifyImportNext.jpg)

デフォルトの設定はほとんどのケースに適しているため、基本的にはそのままで問題ありません。  
そのまま **「Save & Process」** をクリックして進めてください。
（エージェントの理解精度をさらに高めたい場合は、後からパラメーターを調整することも可能です。）

![Dify Dataset1](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/012DifyEmbedding.jpg)

✅ 以下の画面が表示された場合、ドキュメントのアップロードが正常に完了し、Difyシステムによって正しく解析されたことを意味します。

![DifydataSet](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/013DifyDataUploadSucess.jpg)

これで、AIエージェントのナレッジベース構築が完了しました。  
次のステップでは、このナレッジを活用するためのエージェントアプリを作成し、接続していきます！

---

### 🧩 Step 3：エージェントアプリを作成し、ナレッジベースに接続する

Dify のコンソール画面にて、上部メニューから **「Studio」** をクリックし、  
右上の **「Create」** ボタンを押して、新しいアプリを作成します。

ポップアップウィンドウで、以下の内容を入力します：

- **App Name & Icon**：如 `AI Sales Avatar`
- **Description**：
Your name is Vendy, the AI Clerk of Luxury Cars.
Your task is to provide information about luxury cars to the customers based on the knowledge.

👇 設定画面は以下のようになります：

![DifyAvatar](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/014DifySalesAvatarSetting.jpg)

点击 **Create** 后，会进入 App 的 **Orchestrate** 编辑界面。

在 **INSTRUCTION** 栏中填写与刚才 **Description** 一致的内容：

**Create** をクリックすると、アプリの **Orchestrate（オーケストレート）** 編集画面に移動します。  

ここで、**INSTRUCTION** 欄に、先ほど入力した **Description（説明文）** と同じ内容を入力してください。

続いて、画面下部の **Knowledge** セクションにて、  
先ほどアップロードしたナレッジドキュメントを参照資料として選択します。

👇 設定画面の例は以下の通りです：

![Dify AvatarData](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/015DifyAvatarData.jpg)

設定が完了したら、右側の入力フィールドでテストを行い、  
ナレッジベースの内容が正しく参照できるかを確認します。  

アップロードしたドキュメントに基づいた回答が返ってくる場合、  
エージェントがナレッジと正常に接続されていることを意味します。

問題がなければ、画面右上の **「Publish」** をクリックして、AIアプリを公開しましょう。

![Dify AvatarTest](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/016DifyAvataRunTest.jpg)

アプリを公開した後、左側メニューの **「API Access」** をクリックします。  
画面右上の **「Create Secret Key」** をクリックすると、APIキーが生成されます。

この APIキー は、後ほど TEN プラットフォームに接続する際に必須となるため、  
**必ずコピーして安全な場所に保存しておいてください。**

👇 APIキーの生成画面は以下の通りです：

![Dify API Key](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/018DifyAPI2.jpg)

🎉 おめでとうございます！  
これで、AI Sales Avatar の「知能本体」部分の構築が完了し、  
TENプラットフォームで使用するための APIキー も無事に取得できました。

---

続いては、**Trulience プラットフォーム** に進み、  
AI Sales Avatar に「外見と演出能力（＝デジタルヒューマンの可視化）」を与えます。

つまり、彼女が「聞く・話す・考える」だけでなく、  
画面上に現れ、人と自然にインタラクションできるようになります！

---

📚 Dify の詳細については、以下の公式ドキュメントも参考にしてください：  
👉 [https://docs.dify.ai/en/introduction](https://docs.dify.ai/en/introduction)

---

### 🧩 Step 4：Trulienceアカウントの登録と、アバターID・アクセストークンの取得

次は、AI Sales Avatar に「可視化されたデジタルヒューマンの姿」を与えます。  
Trulience プラットフォームを使用してアバターを生成し、  
後ほど接続に必要となる **Avatar ID** と **アクセストークン（Token）** を取得します。

✅ 操作の流れは以下の通りです：

1️⃣ Trulienceの公式サイトにアクセス： [https://trulience.com](https://trulience.com)  
トップページの **「Start For Free」** ボタンをクリックして、アカウント登録を開始します。

👇 ページの画面例は以下の通りです：

![Trulience](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/019Trulience.jpg)

2️⃣ 登録が完了すると、管理画面（ダッシュボード）に移動します。  
左側メニューの **「IMAGE AVATARS」** をクリックし、  
女性キャラクターの中から1人を選び、**Vendy** の外見として設定します。  

その後、緑色の **「Create Avatar」** ボタンをクリックして、アバターを生成します。

👇 選択および作成画面の例は以下の通りです：

![Trulience Avatar](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/020TrulienceAvatar.jpg)

---

3️⃣ 画面に **「Avatar created」** のメッセージが表示されたら、  
デジタルヒューマンの作成が正常に完了したことを意味します。

👇 作成成功時の画面例は以下の通りです：

![TrulienceAvatar2](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/021TrulieceAvatarCreation.jpg)

3️⃣ 左側に表示されているデフォルトの名前（例：**Amanda**）を **Vendy** に変更します。  
名前を変更すると、画面下部にこのアバター専用の **Avatar ID** が表示されます。

👇 以下のように確認できます：

![Trulience Vendy Avatar ID](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/022TrulienceAvatarName.jpg)

---

4️⃣ 次に、画面下部の **「Connect」** ボタンをクリックすると、  
ブラウザが新しいページにリダイレクトされます。  

そのとき、URLの中にある `token=` 以降の文字列をコピーしてください。  
これが **アクセストークン（Token）** になります。

この **Avatar ID** と **Token** は、後ほど TEN プラットフォームに接続する際に必要となるため、  
忘れずに一緒に控えておくことをおすすめします。

---

🎉 おめでとうございます！  
これで、AI Sales Avatar の「**外見構築**」が完了し、  
アバターの **Avatar ID** および **アクセストークン（Token）** を無事に取得できました。

---

次はいよいよ最終ステップです：  
Difyで構築したインテリジェントエージェントと、  
Trulienceで生成したデジタルヒューマンを、  
**TEN プラットフォーム** に統合し、  
「聞く・話す・考える・演じる」を一体化したリアルタイム音声AIエージェントを実現します！

---

📚 Trulience の詳細については、以下の公式ドキュメントをご参照ください：  
👉 [https://www.trulience.com/docs#/](https://www.trulience.com/docs#/)

---

## 🧩 Step 5：TEN Agent プラットフォームをローカルで構築する前に必要な3つの準備

Dify のインテリジェントエージェントと Trulience のデジタルヒューマンを  
TEN プラットフォームに接続する前に、  
音声通信および音声認識・音声合成に必要なアカウントと認証情報を事前に用意しておく必要があります。

主に準備が必要なのは、以下の3項目です：

---

### ✅ 1. Agora のリアルタイム音声通信パラメーター

TEN は **Agora** を使用して、音声通話機能（＝「彼女が話す」）を実現しています。  
そのため、以下のパラメーターを準備する必要があります：

- `AGORA_APP_ID=`（App ID）  
- `AGORA_CERTIFICATE=`（Certificate）

👉 取得方法：  
Agora の管理コンソールにログインします： [https://console.agora.io](https://console.agora.io)  
新しいプロジェクトを作成すると、上記の情報（App ID など）を取得できます。

👇 コンソール画面の例は以下の通りです：

![Agora Project](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/023Agora.jpg)

アカウントにログインした後、左側メニューの **「Projects」** をクリックし、  
右上の **「Create New」** ボタンをクリックして、新しいプロジェクトを作成します。

👇 プロジェクト作成画面の例は以下の通りです：

![AgoraNew](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/024AgoraCreate.jpg)

---

### 📝 入力項目の説明：

- **Project Name**：`AISalesAvatar` と入力します  
- **Use Case**：`Enterprise Collaboration` など、適切な用途を選択します  
- **Authentication Mode**：**Secure Mode: APP ID + Token（推奨）** を選択します

すべて入力したら、**「Submit」** をクリックしてプロジェクト作成を完了します。

👇 プロジェクトが作成されると、App ID および Certificate（証明書）を取得できます：

![Agora APP ID](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/025AgoraAPPID.jpg)

プロジェクトが正常に作成されると、自動的にプロジェクト管理ページに移動します。  
プロジェクト一覧の中から、**App ID** の右側にあるコピーアイコンをクリックすると、  
**App ID** をコピーできます。

👇 以下はその画面例です：

![AgoraApp IDGet](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/026AgoraAPPID2.jpg)

---

App ID を取得した後は、プロジェクト右側の ✏️ **鉛筆アイコン（編集ボタン）** をクリックし、  
プロジェクトの詳細ページに入ります。

ページ下部の **Primary Certificate** セクションにあるコピーアイコンをクリックすると、  
該当プロジェクトの **Certificate（証明書）** をコピーできます。

👇 以下はその画面の例です：

![Agora Certificate](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/027AgoraCertificate.jpg)

これで、**Agora の App ID および Primary Certificate（証明書）** の取得が完了しました。  
TEN プラットフォームで音声通信機能を有効化するための準備が整いました。

---

📚 詳細については、Agora の公式ドキュメントをご参照ください：  
👉 [https://docs.agora.io/en/video-calling/get-started/manage-agora-account?platform=web#create-an-agora-project](https://docs.agora.io/en/video-calling/get-started/manage-agora-account?platform=web#create-an-agora-project)

---

### ✅ 2. Azure Speech のパラメーター（音声認識 + 音声合成）

**Azure** は、ユーザーの音声を文字に変換する「STT（Speech to Text）」と、  
AI の返答を音声に変換する「TTS（Text to Speech）」の機能を担います。  

以下の4つの環境変数を準備する必要があります：

- `AZURE_STT_KEY`  
- `AZURE_STT_REGION`  
- `AZURE_TTS_KEY`  
- `AZURE_TTS_REGION`

👉 取得方法は以下の通りです：

Azure の公式ポータルにアクセスし、ログインします：  
🔗 [https://portal.azure.com](https://portal.azure.com)

Azure ポータルのホーム画面で、左上の **「Create a resource（リソースの作成）」** をクリックします。  
検索バーに **Azure OpenAI** と入力し、表示された項目をクリックして作成画面へ進みます。

👇 作成画面の例は以下の通りです：

![Azure Resource](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/028Azure.jpg)

---

以下の内容を参考にして、**「Basics」** セクションの基本情報を入力してください：

![Azure OpenAI List](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/029AzureOpenAI.jpg)

---

通常は、デフォルトの **「パブリックアクセス（公共アクセス）」** を選択すれば問題ありません。  
これにより、サービスはインターネット経由でアクセス可能になります。

![Azure OpenAI Public](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/030AzureCreateAzureOpenAI.jpg)

🧩 オプションステップ：  
リソースに `project=ai-agent` のようなタグを追加することで、  
後からの分類や管理がしやすくなります。

👇 タグとネットワーク設定の画面は以下の通りです：

![Azure resourceset](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/031AzureNetwork.jpg)

---

📝 入力内容に誤りがないことを確認したら、  
**「Create（作成）」** ボタンをクリックして、Azure OpenAI サービスのデプロイを開始します。

👇 デプロイ確認画面の例は以下の通りです：

![Azure createconfirm](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/032AzureReview.jpg)

👇 リソースのデプロイ中の画面は以下の通りです：

![Azure deploy](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/033AzureDeployment.jpg)

---

デプロイが完了したら、**Azure AI Foundry** にアクセスします。  
すると、以下のようなウェルカム画面が表示され、  
プロジェクトの作成やモデルの選択をすばやく行うことができます。

👇 ウェルカム画面の例は以下の通りです：

![Azure AI Foundry](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/034AzureAIFoundry.jpg)

---

**「Model Catalog（モデルカタログ）」** ページに移動し、  
一覧の中から **Azure AI Speech** を選択します。

![Azure Speech model](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/035AzureModels.jpg)

**Azure-AI-Speech** モデルをクリックすると、詳細ページに移動します。  
そのページ上部にある **「Use Service」** ボタンをクリックすると、  
**Speech Playground** ページに遷移します。

![Azure Speech entry](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/036AzureUseService.jpg)

**Speech Playground** にアクセスしたら、画面上で自分の音声サービスリソースを選択します（以下の図を参照）。  
選択すると、対応する **API Key** と **Region** が表示されます。

![Azure STT KeyRegion](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/037AzureSTTKey.jpg)

---

**「Text to Speech」** タブをクリックすると、**Voice Gallery（ボイスギャラリー）** に移動します。  
ここでは、さまざまな音声スタイルを試聴でき、  
AIアバターに最も適した音声タイプを選ぶことができます。

![Azure TTS](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/038AzureTTSmodels.jpg)

---

**「View Code」** ボタンをクリックすると、  
現在の音声サービスに対応する **API Key** と **Region** をコピーすることができます。

![AzureAPI KeyRegion](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/039AzureTTSKey.jpg)

---

🎉 **おめでとうございます！**  
これで、**TEN プラットフォームの実行に必要なすべてのパラメーター準備が完了しました。**

---

### 🧱 次のステップでは、いよいよローカル環境で TEN Agent プラットフォームを起動し、  
これまでに構築してきたすべてのモジュールを連携させます：

- 🧠 インテリジェントエージェント（Dify）  
- 🔊 音声機能（Azure Speech + Agora）  
- 👩‍💻 バーチャルアバター（Trulience）

**これらを完全に統合し、「聞く・話す・考える・演じる」を兼ね備えたリアルタイムAIセールスアシスタントを完成させましょう！**

---

📚 Azure Speech および OpenAI サービスの導入についてさらに詳しく知りたい場合は、 以下の公式ドキュメントをご参照ください：
👉 [https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)

## 🧩 Step 6：Mac 上で TEN Agent の開発環境をローカルに構築する

AI Sales Avatar の音声インタラクションシステムを実行・デバッグするためには、  
ローカル環境に **TEN Agent の開発環境** を準備する必要があります。

---

### 🔧 必要なツールとインストール方法一覧：

| ツール      | 役割・機能説明                      | インストール方法                             |
|-------------|----------------------------------|-------------------------------------------|
| Docker      | TEN のコンテナ環境を実行する         | 公式サイトから Docker Desktop をダウンロード   |
| Git         | TEN のコードリポジトリをクローン・管理 | `brew install git`                        |
| Node.js     | フロントエンド（Playground）を実行   | `brew install node`                       |


---

### ✅ ① 安装 Docker

### ✅ ① Docker のインストール

💡 Docker は TEN プラットフォームの中核となる実行環境であり、  
すべてのモジュールはコンテナとしてデプロイされます。

- 公式サイトにアクセス：👉 [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)  
- macOS 用の `.dmg` インストーラーをダウンロードしてインストールします。  
- インストール後、アプリ一覧から Docker アイコンをクリックして起動します。  
- 上部メニューバーの 🐳 アイコンが緑色になれば、起動成功です。  
- Terminal を開き、以下のコマンドを入力してインストール確認を行います：docker -v.

### ✅ ② Git のインストール

💡 Git は、TEN フレームワークのコードをクローンおよび管理するためのバージョン管理ツールです。

インストールコマンド：brew install git
インストール確認：git -v

### ✅ ③ Node.js のインストール

💡 Node.js は、TEN のフロントエンドインターフェース（Playground）を実行するために必要な環境です。

インストールコマンド：brew install node
インストール確認：node -v

### ✅ ④ TEN Agent フレームワークのクローン

Docker、Git、Node.js のインストールが完了したら、  
次は TEN Agent のソースコードをクローンし、`.env` 環境変数ファイルを設定します。

🚀 1. TEN Agent のコードリポジトリをクローンする

Terminal（ターミナル）で以下のコマンドを実行します：git clone https://github.com/TEN-Framework/TEN-Agent.git

実行後、ローカル環境に TEN-Agent というフォルダが作成され、
必要なすべてのコードと設定ファイルが格納されます。

👇 フォルダ構成の例は以下の通りです：

![TEN Clone](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/040TEN.jpg)

📦 2. プロジェクトディレクトリに移動し、環境変数テンプレートをコピーする

まず、`ai_agents` サブディレクトリに移動し、以下のコマンドを実行します：

cd TEN-Agent/ai_agents
cp .env.example .env

.env ファイルは、TEN Agent の実行に必要な環境変数を設定するための構成ファイルです。
このファイルをテキストエディタで開き、Dify、Trulience、Azure、Agora から取得した各種キーやトークンを入力してください。

👇 編集画面の例は以下の通りです：

![TEN Agent .env](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/041TEN.jpg)

✍ 3. `.env` ファイルを編集し、以下の変数を設定する

`.env` ファイルを、**Cursor** や **VS Code** などのテキストエディタで開いてください。  
ファイルの末尾に、以下の内容を追加し、各自の環境に合わせたキーとリージョン情報を入力します：

Agora App ID と Certificate
AGORA_APP_ID=your_agora_app_id
AGORA_APP_CERTIFICATE=your_agora_certificate

Azure STT　パラメーター
AZURE_STT_KEY=your_stt_key
AZURE_STT_REGION=your_stt_region

Azure TTS パラメーター
AZURE_TTS_KEY=your_tts_key
AZURE_TTS_REGION=your_tts_region

👇 `.env` ファイルの編集画面の例は以下の通りです：

![TEN .env](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/042TENCursor.jpg)

## ✅ Step ⑤：TEN Agent のコンテナを起動し、サーバーをビルド・実行する

`.env` 環境変数の設定が完了したら、  
次は **TEN Agent のコンテナ環境** を本格的に起動していきます。

---

### 🐳 ① コンテナの起動

`ai_agents` ディレクトリに移動し、Docker コンテナサービスを起動します：

cd ai_agents
docker compose up -d

このコマンドにより、以下のコンテナサービスが起動されます：

- `ten_agent_dev`：エージェントの開発および実行用  
- `ten_agent_demo`：サンプルエージェント  
- `ten_agent_playground`：フロントエンドのインタラクション画面

👇 プロジェクト構成の例は以下の通りです：

![TEN Agent ai_agents 目录结构](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/043TENaiagents.jpg)

🔧 ② コンテナに入って Agent サーバーをビルドする

以下のコマンドを実行して、開発用コンテナに入ります：docker exec -it ten_agent_dev bash

コンテナ内に入ったら、初期化用のタスクスクリプトを実行して、エージェントを登録します：task use

👇 プロジェクト構成の例は以下の通りです：

![task use](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/044TENtaskuse.jpg)

このコマンドを実行すると、`manifest.json` や `property.json` などのエージェント設定ファイルが自動的に読み込まれ、  
必要な依存パッケージも自動でインストールされます。

👇 実行プロセスの画面例は以下の通りです：

![TEN task run](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/045TENTaskRun.jpg)

✅ `task run` コマンドの実行が完了したら、  
以下のアドレスをブラウザで開くことで、フロントエンドの画面にアクセスできます：

👉 [https://localhost:49483]

正常に起動していれば、以下のような画面が表示されます：

画面上部の **「Graph」** タブをクリックします。

ドロップダウンメニューから、以下のグラフを選択します：
➡️ **`voice_assistant_intergrated_stt (Auto Start)`**，  
その後、画面右下の **「Save」** ボタンをクリックして、設定を保存します。

👇 ページ画面の例は以下の通りです：

![TEN Agent Playground](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/046TEN494483.jpg)

✅ 音声合成（TTS）モジュールを **Azure エンジン** に置き換える

1. フロー図の中から、**TTS モジュール**（例：`tts_default`）を見つけます  
2. そのモジュールを右クリックし、**「Replace Node with」** を選択します  
3. 表示されるリストの中から **`azure_tts`** を選びます

これで、音声合成モジュールの Azure への切り替えが完了します。

👇 Azure TTS モジュールの置き換え画面は以下の通りです：

![TEN Agent Azure TTS Change](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/047TENAzuretts.jpg)

🎙️ デジタルヒューマンの音声設定（TTS）

デジタルヒューマンの外見に合わせて、彼女の音声もカスタマイズすることができます。  
Microsoft の音声サービスページでは、サポートされている音声の名前が一覧で表示されています。

👉 こちらのリンクからアクセスできます：  
[https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#multilingual-voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#multilingual-voices)

---

この例では、英語の女性の音声を選択します：  
🗣️ **`en-US-AshleyNeural`**

Azure TTS モジュール内では、以下のフィールドに次の内容を入力してください：  
`Azure_synthesis_voice_name=en-US-AshleyNeural`

👇 Azure TTS 音声設定画面の例は以下の通りです：

![TEN Azure_synthesis_voice_name](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/048TENAzureVoice.jpg)

🔁 LLM モジュールを Dify インターフェースに置き換えて、Dify エージェントを接続する

1. **`llm` モジュール** を右クリックし、**「Replace Node with」** を選択します  
2. 表示されたリストから **`dify_python`** を選択します

これで、TEN Agent の大規模言語モデル（LLM）モジュールが、Dify が提供するインテリジェントエージェントインターフェースに接続されます。

👇 操作画面の例は以下の通りです：

![TEN Agent Dify](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/049TENDifyAPI.jpg)

2️⃣ 置き換えが完了したら、新しく生成された **`dify_python`** モジュールを再度右クリックし、  
**「Update Properties」** をクリックして、プロパティ設定ページに移動します。

- **API Key** フィールドに、Dify プラットフォームで作成した API Key を入力します。  
- **Greeting** フィールドでは、必要に応じて歓迎のメッセージ（音声での挨拶など）をカスタマイズできます。

👇 設定画面の例は以下の通りです：

![TEN AgentDify API KeyGreeting](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/050TENDifyAPI2.jpg)

✅ TEN Agent を起動し、Trulience のデジタルヒューマンと接続する

---

### 🚀 フロントエンドページを起動

設定が完了したら、ブラウザを開き、以下のアドレスにアクセスして、TEN Agent の起動画面に入ります：

👉 [http://localhost:3000](http://localhost:3000)

👇 ページの画面例は以下の通りです：

![TEN Agent](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/051TEN3000.jpg)

🧠 インテリジェントエージェントのフローチャート（Graph）を選択

1. 画面右上の **「Select Graph」** をクリックし、ドロップダウンメニューから  
   ➤ `voice_assistant_integrated_stt` を選択します

2. **「Enable Trulience Avatar」** にチェックを入れ、以下のフィールドを入力します：

   - **Avatar ID**（Trulience でデジタルヒューマンを作成した際に得られる ID）
   - **Avatar Token**（Connect をクリック後、ブラウザのアドレスバーからコピーしたトークン）

3. 入力が完了したら、**「Save changes」** をクリックして設定を保存します。

👇 設定画面の例は以下の通りです：

![TEN AgentTrulience](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/052TENTrulienceGrah.jpg)

🗣️ 音声インタラクションを起動し、デジタルヒューマンが正常に接続されているかテストする

✅ 画面右上の **「Connect」** ボタンをクリックして、最終テストを実施します。

すべての設定が正しく行われていれば、以下のシナリオが表示されます：

- 🧍 デジタルヒューマンの姿が自動的にロードされて表示される  
- 🗣️ 彼女は自然な音声で挨拶し、質問を投げかけてきます。例えば：  
  _「どの高級車を紹介できますか？」_

- 🤖 彼女の回答を基に、Dify ナレッジベースの内容が正しく読み取られ、理解されているかを検証できます。

👇 実行画面の例は以下の通りです：

![TEN AgentTalk](https://raw.githubusercontent.com/aleclee1005/AISalesAvatar/img/img/053TrulienceDifyFinal.jpg)

🎯 おめでとうございます！これで、あなたは完全な **AI Sales Avatar** を手に入れました！

---

✅ **OpenAI / Dify** のチャットボット  
✅ **Azure** の自然な音声合成機能（女性の声）  
✅ **Trulience** によるデジタルヒューマンの外見  
✅ **TEN プラットフォーム** に基づいた音声インタラクション能力  

---

🌟 これが AI エージェントの最も重要な完全なフローです：  
**「聞く → 考える → 話す → 演じる → 接続」**

📚  詳細については、TEN の公式技術ドキュメントをご参照ください：
👉 [https://theten.ai/docs/ten_agent/architecture_flow](https://theten.ai/docs/ten_agent/architecture_flow)

## 🛠️ 次のステップの拡張提案（AX アーキテクチャに基づく）

現在構築された「AI Sales Avatar」をベースに、  
**AX アーキテクチャ** のパスに沿って、実際のビジネスシーンにおける能力をさらに拡張し、  
次のステップとして、以下のフローを順次実現します：  
**データ → モデル → エージェント → ユーザーインターフェース → 全業務ライフサイクル管理** の閉ループを構築する。

---

### 🧑‍💼 ウェブサイトのホームページに埋め込み、会社のバーチャルキャラクターとして活用

**Trulience** の D-Human および Avatar 機能を活用し、  
現在のデジタルヒューマンを会社のホームページや Web アプリに展開します。  
自然言語での音声質問応答を通じて訪問者をガイドし、意図を収集することができます。  
ユーザー中心のエントランスを構築し、以下の内容を担当します：

- `マーケティング情報（Marketing Info）`  
- `顧客ライフサイクル（Customer Lifecycle）`

---

### 📦 データベースおよび注文管理システムの統合、進化した「AIセールスレプレゼンタティブ」

アバターを会社の内部システムと統合します。例えば：

- CRM、ERP、OA、注文管理システム（例：Salesforce、SAP、Notion DB など）

これにより、以下のタスクが実現されます：
- セールスリードの管理  
- 在庫の確認  
- 契約書の生成などの閉ループタスク

サービス対象：
- `契約ライフサイクル（Contract Lifecycle）`  
- `資産ライフサイクル（Asset Lifecycle）`
---

### 🔗 企業のコアプラットフォームへの統合：個別アプリケーションから組織レベルの協働へ

Agent PF（プラットフォーム）の機能をさらにモジュール化し、  
異なる事業部（BU）の Data Lake とワークフロー管理プラットフォームに統合します。  
これにより、以下のような多様なビジネスシーンの融合を実現します：

- AI + 財務（Finance）  
- AI + 人事（HR）  
- AI + 研究開発（R&D）  
- AI + SNS（協働）

最終的には、企業全体の AI トランスフォーメーション（AI転換）を推進し、  
進化を加速させます。

## ✨ 最後に：一言感想

私はAIは単なる冷たくて強力なツールではなく、  
それは人間の温かいパートナーであり、個々の能力を拡張し、強化する存在であると信じています。

未来、世界中でますます多くの「**Vendy**」のようなデジタルパートナーが生まれていくことでしょう——  
彼女たちは**聞き、考え、反応し、表現**し、テクノロジーの力で人間の尊厳と創造力を守ってくれます。

---

📣 あなたもこの共創の旅に参加したいと思われるなら、  
一緒に探求し、共有し、すべての個人がAIと共に成長できる機会を掴んで、
共に **「一騎当千」と「一人不遺」**（＝誰一人も取り残さない）のAX新時代を切り開きませんか。

---

この文書を小さな試みと記録として書き記します。  
それが小さな種となり、  
人とAIが調和して共生する未来で、**静かに根付き、ゆっくりと芽を出しますように**。
