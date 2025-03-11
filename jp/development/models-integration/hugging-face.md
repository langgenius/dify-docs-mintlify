# Hugging Faceのオープンソースモデルを統合

Difyはテキスト生成（Text-Generation）と埋め込み（Embeddings）をサポートしており、以下はそれに対応するHugging Faceモデルの種類です：

* テキスト生成：[text-generation](https://huggingface.co/models?pipeline\_tag=text-generation\&sort=trending)，[text2text-generation](https://huggingface.co/models?pipeline\_tag=text2text-generation\&sort=trending)
* 埋め込み：[feature-extraction](https://huggingface.co/models?pipeline\_tag=feature-extraction\&sort=trending)

具体的な手順は以下の通りです：

1. Hugging Faceのアカウントが必要です（[登録はこちら](https://huggingface.co/join)）。
2. Hugging FaceのAPIキーを設定します（[取得はこちら](https://huggingface.co/settings/tokens)）。
3. [Hugging Faceのモデル一覧ページ](https://huggingface.co/models)にアクセスし、対応するモデルの種類を選択します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/af8a771b1e71152837e0f25b87a4471e.png)

DifyはHugging Face上のモデルを次の2つの方法で接続できます：

1. Hosted Inference API。この方法はHugging Face公式がデプロイしたモデルを使用します。料金はかかりませんが、サポートされているモデルは少ないです。
2. Inference Endpoint。この方法は、Hugging Faceが接続しているAWSなどのリソースを使用してモデルをデプロイします。料金が発生します。

### Hosted Inference APIのモデルを接続する

#### 1 モデルを選択

モデルの詳細ページの右側にHosted Inference APIのセクションがあるモデルのみがHosted Inference APIをサポートしています。以下の図のように表示されます：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/dc5a5584cef16fe76595058d37043546.png)

モデルの詳細ページで、モデルの名前を取得できます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/248a80fb0dac520e690cb122dbe91324.png)

#### 2 Difyで接続モデルを使用する

`設定 > モデルプロバイダー > Hugging Face > モデルタイプ`のエンドポイントタイプでHosted Inference APIを選択します。以下の図のように設定します：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/39a93c21134d99b3db9cafa8123a35ed.png)

APIトークンは記事の冒頭で設定したAPIキーです。モデル名は前のステップで取得したモデル名を入力します。

### 方法 2: Inference Endpoint

#### 1 デプロイするモデルを選択

モデルの詳細ページの右側にある`Deploy`ボタンの下にInference EndpointsオプションがあるモデルのみがInference Endpointをサポートしています。以下の図のように表示されます：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/0821340197577ff126440b2558446890.png)

#### 2 モデルをデプロイ

モデルのデプロイボタンをクリックし、Inference Endpointオプションを選択します。以前にクレジットカードを登録していない場合は、カードの登録が必要です。手順に従って進めてください。カードを登録した後、以下の画面が表示されます：必要に応じて設定を変更し、左下のCreate EndpointボタンをクリックしてInference Endpointを作成します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/f7582adc0937dc4f038e462b578d9c17.png)

モデルがデプロイされると、エンドポイントURLが表示されます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/30c38995813c0d05c35c42dc0f1d467c.png)

#### 3 Difyで接続モデルを使用する

`設定 > モデルプロバイダー > Hugging Face > モデルタイプ`のエンドポイントタイプでInference Endpointsを選択します。以下の図のように設定します：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/0c747dc499163323bcbd432396e4c3e1.png)

APIトークンは記事の冒頭で設定したAPIキーです。`テキスト生成モデルの名前は任意に設定可能ですが、埋め込みモデルの名前はHugging Faceの名前と一致する必要があります。`エンドポイントURLは前のステップでデプロイしたモデルのエンドポイントURLを入力します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/development/models-integration/6a8908cace5b287070577bf555d69b0c.png)

> 注意点：埋め込みの「ユーザー名 / 組織名」は、Hugging Faceの[Inference Endpoints](https://huggingface.co/docs/inference-endpoints/guides/access)のデプロイ方法に基づいて、「[ユーザー名](https://huggingface.co/settings/account)」または「[組織名](https://ui.endpoints.huggingface.co/)」を入力する必要があります。
