# Difyで大規模言語モデルの「競技場」を体験する方法：DeepSeek R1 VS o1 を例に

## 概要

Difyのチャットアシスタントタイプのアプリケーションにプリインストールされている[複数モデルのデバッグ](../../guides/application-orchestrate/multiple-llms-debugging.md)機能を使うと、同じ質問に対する異なるLLMの回答効果を同時に比較できます。この記事では、DeepSeek R1とo1を例に、Dify内でさまざまな大規模言語モデルの回答品質を直感的に比較する方法をご紹介します。

![](https://assets-docs.dify.ai/2025/02/dd2a54e05cf5bfa252ac980ec478e3d5.png)

## 事前準備

- Dify.AI クラウド版 / コミュニティ版
- DeepSeek R1 API
- OpenAI o1 API

## クイックスタート

### 1. LLM APIキーの設定

テストを開始する前に、**「右上」→[「新しいプロバイダーを追加」](../../guides/model-configuration/README.md)** をクリックし、表示される指示に従って、複数のモデルのAPIキーを手動で追加してください。

### 2. アプリケーションの作成

チャットボットタイプのアプリケーションを作成し、アプリケーション名と説明を入力して作成を完了させます。

![](https://assets-docs.dify.ai/2025/02/7246807cbd0776564b76e1ef37dcbd4d.png)

### 3. 大規模言語モデルの選択

アプリケーション右上の大規模言語モデル選択ページで、`o1`モデルを選択した後、**「複数のモデルでデバッグ」** をタップし、`deepseek-reasoner`モデルを追加します。

![](https://assets-docs.dify.ai/2025/02/61d8ba00a8a89052ac7a5a9d8fb54f58.png)

### 4. 効果の比較

ダイアログボックスに質問を入力すると、入力した質問に対する各モデルの応答を同時に確認できます。

![](https://assets-docs.dify.ai/2025/02/03ac1c1da6705d76b01f5867a1e24e32.gif)

詳細や利用に関するご質問は、[複数モデルのデバッグ](../../guides/application-orchestrate/multiple-llms-debugging.md)をご覧ください。
