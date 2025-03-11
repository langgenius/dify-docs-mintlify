# ComfyUI

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

[ComfyUI](https://www.comfy.org/)は、最強のモジュラー型拡散モデルのGUI、API、バックエンドを備えたツールで、グラフやノードインターフェースを提供します。現在、Difyで利用可能で、画像のプロンプトを入力することで生成された画像を取得できます。

## 1. ComfyUIのワークフローが正しく動作しているか確認します。
ComfyUIが正常に動作し、画像が生成されることを確かめるためには、[公式ドキュメント](https://docs.comfy.org/get_started/gettingstarted)を参照してください。

## 2. Prompt 設定

Difyを介してプロンプトを渡す必要がない場合は、この手順をスキップできます。プロンプトノードが ComfyUI の唯一の `KSampler` ノードに接続されている場合は、この手順もスキップできます。
それ以外の場合は、ポジティブなプロンプトの単語の内容を置き換えるには文字列 `{{positive_prompt}}` を使用し、ネガティヴなプロンプトの単語の内容を置き換えるには `{{negative_prompt}}` を使用してください。
![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/4e937df93709ca5a47c5c17e17498f38.png)

## 3. ワークフローのAPIファイルをエクスポートします。
![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/tool-configuration/49794b23612f47245fabaf1eae207526.png)
画像のように、「Save (API Format)」を選択してください。このオプションが表示されない場合は、設定で「Dev Mode」を有効にする必要があります。

## 4. DifyにComfyUIを統合します。
Difyのナビゲーションページで、`ツール > ComfyUI > 認証する`の順にクリックし、API キーを入力してください。DifyのDocker展開を使用している場合、このアドレスは通常 `http://host.docker.internal:8188` です。

## 5. DifyでComfyUIを利用します。
`Workflow`ツールを開き、エクスポートしたAPIファイルの内容を `WORKFLOW JSON` に入力して、通常通りに生成を行ってください。