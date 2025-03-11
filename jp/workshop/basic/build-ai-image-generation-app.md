# ゼロからAI画像生成アプリの構築方法

> 著者：Steven Lynn. Difyのテクニカルライター

画像生成技術の発展に伴い、Dall-e、Flux、Stable Diffusionなどの優れた画像生成ツールが多数登場しています。

本記事では、Difyを使用してAI画像生成アプリを開発する方法について学びます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/05ff829cf382e82c9ece2676032d2383.png)

## 今回の学ぶポイント

- Difyを使用してエイジェントの作り方
- エイジェントの基本的なコンセプト
- プロンプトエンジニアリングの基本
- ツールの使用方法
- 大規模モデルの幻覚の概念

## 1. Stablility API キーの設定

[こちら](https://platform.stability.ai/account/keys) をクリックして、ステイビリティAPIキー管理ページに移動します。

まだ登録していない場合は、API管理ページに入る前に登録を求められます。

管理ページに入ったら、キーをコピーするために`コピー`をクリックします。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/f73d82756bdf93c8863ac0b1f55fa5af.png)

次に、[Dify - ツール - Stability](https://cloud.dify.ai/tools) にキーを入力する必要があります。以下の手順に従ってください：

- Difyにログインする
- ツールに入る
- ステイビリティを選択する
- 承認をクリック
![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/bcc961ffc8a341c8ba3137e475072f99.png)
- キーを入力して保存

## 2. モデルプロバイダの設定

インタラクションを最適化するために、ユーザーの指示を具体化するための大規模言語モデル（LLM）が必要です。つまり、画像生成のためのプロンプトを記述します。次に、Difyでモデルプロバイダを設定します。

Difyの無料版では、200回の無料のOpenAIメッセージクレジットが提供されます。

メッセージクレジットが不足している場合は、以下の手順に従って他のモデルプロバイダをカスタマイズできます：

**あなたのアバター - 設定 - モデルプロバイダ**の順にクリックします。
![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/4b4102f9027e2bda3fc520eaa8ea2354.png)

適切なモデルプロバイダが見つからない場合は、groqプラットフォームがLlamaなどのLLM用に無料のコールクレジットを提供しています。

[groq API管理ページ](https://console.groq.com/keys)にログインします。

**API Keyの作成**をクリックし、希望の名前を設定してAPIキーをコピーします。

**Dify - モデルプロバイダ**に戻り、**groqcloud**を選択し、**設定**をクリックします。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/0fda6e81dc23974576ddc21bda96e26d.png)

API Keyを貼り付けて保存します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/b250952afad12b39613aa27da5335fa3.png)

## 3. エイジェントを作る

**Dify - スタジオ**に戻り、**最初から作成**を選択します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/67e8927a4b0dbfbfc81bcf0e5822bef2.png)

この実験では、エージェントの基本的な使用方法を理解するだけで十分です。

{% hint style="info" %}
**エージェントとは？**

エージェントは、人間の行動と能力をシミュレートするAIシステムです。自然言語処理を通じて環境とやり取りし、入力情報を理解し、対応する出力を生成します。エージェントはまた「知覚」能力を持ち、さまざまな形式のデータを処理し・分析し、さまざまな外部ツールやAPIを呼び出して使用してタスクを完了することができます。この設計により、エージェントはより柔軟に複雑な状況を処理し、ある程度人間の思考や行動パターンをシミュレートできるようになります。
{% endhint %}

**エージェント**を選択し、名前を入力します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/139ac0d2f4a10e2ec0e191457f4687a1.png)

以下のようにエージェントのオーケストレーションインターフェースに入ります。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/9045dbab8600e9c9d9632add787f26a6.png)

LLMを選択します。このチュートリアルでは、groqが提供するLlama-3.1-70Bを例にします：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/47edc14c1d3c68eeb4ee4807b35df185.png)

**ツール**でステイビリティを選択します：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/6e1c3dd63925fd9ba60568deb2602044.png)

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/539060be4e014126f9c5fc96c53dc5a4.png)

### プロンプトの書き方

プロンプトはエージェントの核心であり、出力結果に直接的な影響を与えます。一般的に、プロンプトが具体的であればあるほど、出力も向上しますが、過度に長いプロンプトは逆効果になることもあります。

プロンプトを調整する技術は「プロンプトエンジニアリング」と呼ばれています。

この実験では、プロンプトエンジニアリングを完全に習得していなくても心配する必要はありません。後で段階的に学ぶことができます。

まずは、最もシンプルなプロンプトから始めましょう：

```
ユーザーのプロンプトに従って、指定された内容を stability_text2image を使用して描画してください。
```

ユーザーがコマンドを入力するたびに、エージェントはこのシステムレベルの指示を理解し、ユーザーの描画タスクを実行する際には、stabilityというツールを呼び出すことを認識します。

例：女の子が開いた本を持っているのを描く。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/05ff829cf382e82c9ece2676032d2383.png)

### プロンプトを書くのかしなくても可能ですか？もちろん可能です！

プロンプトの上部にある**自動**をクリックしてください。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/92fcf94a052db4ec2a4e1f659c55ae46.png)

**指示**に要件を入力し、**自動**をクリックします。右側に生成されたプロンプトがAIによって作成されます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/a4ef4938ec2ca77d529fa55752c734e0.png)

ただし、プロンプトについての理解を深めるためには、初期段階ではこの機能に頼るべきではありません。

## 発表

右上の公開ボタンをクリックし、公開後に**Run**を選択して、オンラインで実行されるエージェント用のWebページを取得します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/86ecde526fb91c40c790a34fdfaee5e4.png)

このWebページのURLをコピーして、友人と共有することができます。

## 質問1：生成された画像のスタイルを指定する方法は？

ユーザーの入力コマンドにスタイル指示を追加することができます。例えば：「アニメスタイルで、女の子が開いた本を描いてください。」

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/d2d883d887272786ee19d97894cbb307.png)

ただし、デフォルトのスタイルをアニメスタイルに設定したい場合は、システムプロンプトにその旨を追加することができます。なぜなら、システムプロンプトはユーザーコマンドが実行されるたびに認識され、優先されるからです。

```
ユーザーのプロンプトに従って、指定された内容をstability_text2imageを使用して描画してください。画像はアニメスタイルです。
```

## 質問2：特定のユーザーからのリクエストを拒否する方法は？

多くのビジネスシナリオでは、いくつかの不適切なコンテンツの出力を避ける必要がありますが、LLMはしばしば「無知」であり、出力コンテンツが間違っていてもユーザーの指示に従います。このように、モデルが間違ったコンテンツを作り出してユーザーに答えようとする現象を「モデルの幻覚」と呼びます。したがって、必要に応じてモデルがユーザーのリクエストを拒否できることが重要です。

さらに、ユーザーがビジネスに関係のないコンテンツを要求することもあり、エージェントがそのようなリクエストを拒否する必要があります。

異なるプロンプトをカテゴリ別に整理するために、マークダウン形式を使用して、エージェントに不適切なコンテンツを拒否する方法を教えるプロンプトを「制約」のセクションに記述します。もちろん、このフォーマットは標準化のためのものであり、独自のフォーマットを持つこともできます。

```
## タスク
ユーザーのプロンプトに従って、指定された内容をstability_text2imageを使用して描画してください。画像はアニメスタイルです。

## 制約
もしユーザーが描画に関係のないコンテンツを要求した場合、「申し訳ありませんが、その内容は理解できません。」と返答してください。
```

例えば、今夜の夕食は何ですか？と聞いてみましょう。
![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/06dcf569989d797919fbe49ab8d5cadc.png)

よりフォーマルなビジネスシナリオでは、感情的な単語ライブラリを使用してユーザーのリクエストを拒否することができます。

**Add Feature - Content Moderation**にキーワード「dinner」を追加します。ユーザーがそのキーワードを入力すると、エージェントアプリは「申し訳ありませんが、その内容は理解できません。」と出力します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/workshop/basic/828b27d1a873ff7b4b44f76d93229225.png)
