# プラグイン開発ガイド

### はじめに

このガイドでは、ツール型プラグインやモデルプラグインなど、様々な種類の**プラグインの開発方法を例**を挙げて説明します。これにより、プラグイン開発における様々な機能の組み合わせを迅速に理解し、活用できるようになります。開発を始める前には、まず開発環境を用意し、必要なフレームワークをインストールして初期設定を行ってください。詳細は以下を参照してください：

{% content-ref url="initialize-development-tools.md" %}
[initialize-development-tools.md](initialize-development-tools.md)
{% endcontent-ref %}

**GoogleSearch**ツールを例に、ツール型プラグインの開発方法を紹介します。具体的な手順は以下をご覧ください：

{% content-ref url="tool-plugin.md" %}
[tool-plugin.md](tool-plugin.md)
{% endcontent-ref %}

**Anthropic**や**Xinference**モデルを例に、事前にトレーニングされたモデルプラグインとカスタムモデルプラグインの開発方法について説明します。

* 事前にトレーニングされたモデルは、GPTやClaudeなどの商用モデルを指し、追加の訓練や設定なしで利用できます。
* カスタムモデルプラグインは、開発者が独自に訓練または設定したモデルを統合し、特定のニーズに合わせた機能を提供します。

具体的な開発例は以下を参照してください：

{% content-ref url="model-plugin/" %}
[model](model-plugin/)
{% endcontent-ref %}

Extensionプラグインにより、開発者はビジネスロジックをプラグインとしてパッケージ化し、Difyプラットフォーム上でAPIサービスとして公開できます。詳細は以下をご覧ください：

{% content-ref url="extension-plugin.md" %}
[extension-plugin.md](extension-plugin.md)
{% endcontent-ref %}

### インターフェースドキュメント

プラグインの詳細なインターフェース仕様が必要な場合は、以下の標準仕様書を参照してください：

1. [一般的な構造の標準定義](../../schema-definition/general-specifications.md)
2. [マニフェストの標準定義](../../schema-definition/manifest.md)
3. [ツールとの接続の標準定義](../../schema-definition/tool.md)
4. [モデルとの接続の標準定義](../../schema-definition/model/)
5. [エンドポイントの標準定義](../../schema-definition/endpoint.md)
6. [拡張エージェント策略](../../schema-definition/agent.md)
7. Difyサービスの逆呼び出し機能
   1. [アプリ](../../schema-definition/reverse-invocation-of-the-dify-service/app.md "mention")の逆呼び出し
   2. [モデル](../../schema-definition/reverse-invocation-of-the-dify-service/model.md "mention")の逆呼び出し
   3. [ノード](../../schema-definition/reverse-invocation-of-the-dify-service/node.md "mention")の逆呼び出し
   4. [ツール](../../schema-definition/reverse-invocation-of-the-dify-service/tool.md "mention")の逆呼び出し
8. [プラグインの永続化されたストレージ機能](../../schema-definition/persistent-storage.md)

### 貢献ガイド

Difyプラグインにコードや機能を提供し、公式プラグインに貢献したいとお考えですか？開発者がプラグインの開発と貢献のプロセスをスムーズに理解し、参加できるように、詳細なガイドを用意しています：

*   [マーケットプレイスの公開ガイド](../../publish-plugins/publish-to-dify-marketplace.md)

    あなたのプラグインを Dify Marketplace に公開し、多くの開発者と成果を共有する方法についてご案内します。

*   [GitHub での公開ガイド](../../publish-plugins/publish-plugin-on-personal-github-repo.md)

    GitHub でプラグインを公開・管理する方法を学び、プラグインの継続的な最適化とコミュニティとの協力を促進します。

貢献者の参加を歓迎し、世界中の開発者とともにDifyエコシステムを充実させていきましょう！
