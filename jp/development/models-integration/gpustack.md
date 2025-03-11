# GPUStackとの統合によるローカルモデルのデプロイ

[GPUStack](https://github.com/gpustack/gpustack)は、大規模言語モデル（LLM）を実行するために設計されたオープンソースのGPUクラスターマネージャーです。

Difyは、大規模言語モデルの推論、埋め込み、再順位付け機能をローカル環境で展開するために、GPUStackとの統合を実現しています。

## GPUStackの展開方法

GPUStackを展開する際は、公式の[ドキュメント](https://docs.gpustack.ai)を参照するか、以下の手順に従って簡単に統合できます。

### LinuxまたはMacOSでの展開

GPUStackは、systemdやlaunchdベースのシステムにサービスとしてインストールするためのスクリプトを提供しています。この方法でGPUStackをインストールするには、次のコマンドを実行してください：

```bash
curl -sfL https://get.gpustack.ai | sh -s -
```

### Windowsでの展開

管理者としてPowerShellを実行し（PowerShell ISEは使用しないでください）、次のコマンドを実行してGPUStackをインストールします：

```powershell
Invoke-Expression (Invoke-WebRequest -Uri "https://get.gpustack.ai" -UseBasicParsing).Content
```

その後、表示される指示に従ってGPUStackのUIにアクセスできます。

## LLMの展開手順

GPUStackにホストされたLLMを使用する方法の例です：

1. GPUStack UIで「Models」ページに移動し、「Deploy Model」をクリック、次に「Hugging Face」をドロップダウンメニューから選択します。

2. 左上の検索バーを使って、モデル名「Qwen/Qwen2.5-0.5B-Instruct-GGUF」を検索します。

3. モデルを展開するために「Save」をクリックします。

![gpustack-deploy-llm](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/35f535a6bb3023aa69a3fdafbdb0c8f3.png)

## APIキーの作成方法

1. 「API Keys」ページに移動し、「New API Key」をクリックします。

2. 名前を入力し、「Save」をクリックします。

3. APIキーをコピーし、後で使用するために保存しておきます。

## DifyとGPUStackの統合手順

5. `Settings > Model Providers > GPUStack`に移動し、以下の情報を入力します：

   - モデルタイプ：`LLM`

   - モデル名：`qwen2.5-0.5b-instruct`

   - サーバーURL：`http://your-gpustack-server-ip`

   - APIキー：`コピーしたAPIキーを入力`

   モデルをアプリケーションで使用するために、「Save」をクリックしてください。

![add-gpustack-llm](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/8e8851fec5a1515a2284aad68b90ad40.png)

GPUStackに関する詳細情報は、[Github Repo](https://github.com/gpustack/gpustack)を参照してください。