# モデルプラグインについて

モデルタイププラグインを導入することで、Difyプラットフォームは特定のモデルプロバイダーが提供するモデルを利用できるようになります。例えば、OpenAIモデルプラグインをインストールすると、DifyプラットフォームからOpenAIのGPT-4やGPT-4o-2024-05-13といったモデルをリクエストできるようになります。

### **モデルプラグインの構造**

プラグインモデルの開発に関する理解を深めるために、モデルタイププラグインの構造例を以下に示します。

*   モデルプロバイダー：OpenAI、Anthropic、Googleなどの大規模モデル開発企業です。
*   モデルカテゴリ：プロバイダーに応じて、大規模言語モデル（LLM）、テキスト埋め込みモデル、音声テキスト変換モデルなどがあります。
*   具体的なモデル：`claude-3-5-sonnet`、`gpt-4-turbo`など。

プラグインプロジェクトのコード構造：

```bash
- モデルプロバイダー
  - モデルカテゴリ
    - 具体的なモデル
```

Anthropicを例にとると、モデルプラグインの構造は次のようになります。

```bash
- Anthropic
  - llm
    claude-3-5-sonnet-20240620
    claude-3-haiku-20240307
    claude-3-opus-20240229
    claude-3-sonnet-20240229
    claude-instant-1.2
    claude-instant-1
```

OpenAIを例にとると、複数のモデルタイプをサポートしています。

```bash
├── models
│ ├── llm
│ │ ├── chatgpt-4o-latest
│ │ ├── gpt-3.5-turbo
│ │ ├── gpt-4-0125-preview
│ │ ├── gpt-4-turbo
│ │ ├── gpt-4o
│ │ ├── llm
│ │ ├── o1-preview
│ │ └── text-davinci-003
│ ├── moderation
│ │ ├── moderation
│ │ └── text-moderation-stable
│ ├── speech2text
│ │ ├── speech2text
│ │ └── whisper-1
│ ├── text_embedding
│ │ ├── text-embedding-3-large
│ │ └── text_embedding
│ └── tts
│ ├── tts-1-hd
│ ├── tts-1
│ └── tts
```

### **モデルプラグイン作成の準備**

モデルプラグインを作成するには、以下の手順に従ってください。具体的な作成ガイドは、各ドキュメントのタイトルをクリックして参照してください。

1.  [モデルプロバイダーの作成](create-model-providers.md)
2.  [事前定義済み](../../../guides/model-configuration/predefined-model.md)モデル、または[カスタム](../../../guides/model-configuration/customizable-model.md)モデルの統合
3.  [モデルプラグインのデバッグ](../../debug-plugin.md)