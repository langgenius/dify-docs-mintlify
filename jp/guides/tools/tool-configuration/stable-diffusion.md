# Stable Diffusion

> 工具作者 @Dify。

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

Stable Diffusionは、テキストプロンプトを基に画像を生成するツールです。DifyではStable DiffusionWebUI APIへのアクセスを実現しているため、Dify内で直接利用することができます。以下にDifyにStable Diffusionを統合する手順を説明します。

## 1. ローカル環境の初期化
Stable Diffusionは、GPUを搭載したマシンを用いることで最適に画像を生成できます。しかし、必須ではなく、CPUのみでも画像を生成することは可能ですが、速度が非常に遅くなるかもしれません。

## 2. インストールし、Stable DiffusionWebUIを起動する
ローカルマシンまたはサーバー上でStable DiffusionWebUIを起動します。

1. [公式リポジトリ](https://github.com/AUTOMATIC1111/stable-diffusion-webui)からStable DiffusionWebUIリポジトリをクローンします。

```bash
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
```

2. コマンドを実行してStable Diffusion WebUIを起動する
リポジトリをクローンした後、クローンしたリポジトリのディレクトリに移動し、以下のコマンドを実行してStable DiffusionWebUIを起動します。

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

3. モデルの準備

ターミナルに表示されたアドレスをブラウザでアクセスすることでStable DiffusionWebUIにアクセスできますが、モデルはまだ利用できません。HuggingFaceまたは他のソースからモデルをダウンロードし、Stable DiffusionWebUIの`models`ディレクトリに配置する必要があります。

例えば、[pastel-mix](https://huggingface.co/JamesFlare/pastel-mix)をモデルとして使用する場合、`git lfs`を使ってモデルをダウンロードし、`stable-diffusion-webui`の`models`ディレクトリに配置します。

```bash
git clone https://huggingface.co/JamesFlare/pastel-mix
```

4 モデル名の取得
モデルリストに`pastel-mix`が表示されますが、モデル名を取得する必要があります。`http://your_id:port/sdapi/v1/sd-models`にアクセスすると、以下のようなモデル名が表示されます。

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

`model_name`が必要です。この例では`pastel-mix_pastelmix-better-vae-fp32`です。

## 3. DifyにStable Diffusionを統合する
`ツール > Stable Diffusion > 認証へ`で認証とモデル設定を行い、前のステップで取得した情報を使用します。

## 4. 完了

- **チャットフロー/ワークフローアプリ**

チャットフローとワークフロー アプリは、`Stable Diffusion`ノードの追加をサポートしています。追加後、ノード内の「変数の入力→プロンプトワード」に[変数](https://docs.dify.ai/v/ja-jp/guides/workflow/variables)を入力して引用する必要があります。ユーザーが入力したプロンプトの単語、または前のノードによって生成されたコンテンツ。最後に、「end」ノード内の変数を使用して、`Stable Diffusion`によって出力された画像を参照します。

- **エージェントアプリ**

エージェント アプリケーションに`Stable Diffusion`ツールを追加し、ダイアログ ボックスで画像の説明を送信し、ツールを呼び出して AI 画像を生成します。