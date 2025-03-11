# Zeabur に Dify をデプロイする

[Zeabur](https://zeabur.com) は、ワンクリックデプロイで Dify をデプロイできるサービスデプロイプラットフォームです。本ガイドは、Zeabur に Dify をデプロイする方法を説明します。

## 前提条件

開始する前に、以下の事項が必要です：

- Zeabur のアカウント。アカウントをお持ちでない場合は、[Zeabur](https://zeabur.com/) で無料のアカウントを登録できます。
- Zeabur のアカウントを開発者プラン（月額 5 ドル）にアップグレードする必要があります。詳細は [Zeabur 定价](https://zeabur.com/pricing) をご覧ください。

## Dify を Zeabur にデプロイする

Zeabur チームはワンクリックデプロイテンプレートを用意しています。以下のボタンをクリックするだけで開始できます：

[![Deploy to Zeabur](https://zeabur.com/button.svg)](https://zeabur.com/1D4DOW)

ボタンをクリックすると、Zeabur 上のテンプレートページに移動し、デプロイの詳細情報と説明を確認できます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/getting-started/install-self-hosted/fc58c921d332857fb644d4c869162bb5.jpeg)

デプロイボタンをクリックした後、生成されたドメイン名を入力し、そのドメイン名を Dify インスタンスにバインドし、他のサービスに環境変数として注入します。
次に、お好みのリージョンを選択し、デプロイボタンをクリックすると、数分以内に Dify インスタンスがデプロイされます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/getting-started/install-self-hosted/43cdd302ca243f2a1d2475a857cc1e66.png)

デプロイが完了すると、Zeabur コンソール上にプロジェクトページが表示されます。以下の図のように、デプロイ中に入力したドメイン名が自動的に NGINX サービスにバインドされ、そのドメイン名を使用して Dify インスタンスにアクセスできます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/getting-started/install-self-hosted/7aa82d91ab9e798245b9df18221637b2.png)

また、NGINX サービスページのネットワーキングタブでドメイン名を変更することもできます。詳細については [Zeabur ドキュメント](https://zeabur.com/docs/deploy/domain-binding) を参照してください。