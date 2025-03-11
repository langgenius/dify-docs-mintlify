# リトリーバルモード

ユーザーがナレッジベースのQ\&A用AIアプリケーションを構築する際に、Difyはアプリケーション内で複数のデータセットが関連付けられている場合に、検索時に2つの検索モードをサポートします：N-of-1検索モードとMulti-Path検索モードです。

![検索モード設定](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/extended-reading/retrieval-augment/36277c7971c542aad7ff208f555cfc67.png)

### 検索設定

ユーザーの意図に基づいてすべてのデータセットを照合し、複数のデータセットから同時に関連するテキストフラグメントを同時に検索します。Rerankを経た後、ユーザーのクエリに最も適合する結果がマルチパス検索の結果から選ばれます。このプロセスには、設定されたRerankモデルのAPIが必要です。マルチパス検索モードでは、検査が関連するすべてのデータセットからユーザーのクエリに関連するテキストコンテンツを検索し、得られた結果を統合した後、Rerankモデルを用いてドキュメントを意味的に再ランク付けします。

マルチパス検索モードでは、Rerankモデルを設定するがお勧めします。Rerankモデルの構成方法については、こちらをご覧ください：🔗[Rerank](https://docs.dify.ai/v/ja-jp/learn-more/extended-reading/retrieval-augment/rerank)

以下は、マルチパス検索モードの技術フローチャートです：

![マルチパス検索](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/extended-reading/retrieval-augment/64007d543f1c5c3f2e87d606d79d04d3.png)

マルチパス検索モードは、モデルの推論能力やデータセットの説明に依存しないため、複数のデータセットを跨いで高品質な検索結果を得ることができます。さらに、Rerankを組み込むことで文書の検索効果を効果的に向上させることができます。したがって、複数のデータセットに関連付けられたナレッジベースのQ\&Aアプリを作成する際には、検索モードをマルチパス検索に設定することをお勧めします。
