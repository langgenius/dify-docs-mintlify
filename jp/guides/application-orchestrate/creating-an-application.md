# アプリ作成

Difyスタジオでは、アプリケーションを作成するにあたり以下の3つの方法があります：

* アプリケーションテンプレートを使用（初心者におすすめ）
* 最初からアプリケーションを作成
* DSLファイルをインポートして作成(ローカル・オンライン)

### テンプレートを使ってアプリケーションを作成

Difyを初めて使う場合、アプリケーション制作に不慣れなこともあるでしょう。そのため、Difyチームは様々な用途に対応する高品質なテンプレートを提供しており、これによりDifyで作成可能なアプリケーションの種類を迅速に把握できます。

ナビゲーションメニューより「スタジオ」を選んだ後、「テンプレートから作成」をアプリケーションリストから選択してください。

![テンプレートからアプリケーションを作成](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/448760da7b5f22f9e6bee7fd47e33a90.png)

好みのテンプレートを選択し、**このテンプレートを使用する**ボタンをクリックします。

### 新しいアプリケーションの作成

Difyで最初からアプリケーションを作成する場合、ナビゲーションメニューから「スタジオ」を選び、「最初から作成」をアプリケーションリストで選択します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/9f5d811f6e117d4f9c11c9128e44d3f7.png)

Difyは、チャットボイス、テキストジェネレータ、エージェント、ワークフロー、チャットフローという5つの異なる種類のアプリケーションがあります。

アプリケーションを作成する際には、名前を付け、適切なアイコンを選択し、このアプリケーションの目的を簡潔に説明することで、チーム内での使用を容易にします。

![アプリケーションを最初から作成](https://assets-docs.dify.ai/2024/12/b0598446c2e129047aa7f4f06f2bf74d.png)

### DSLファイルから作成

{% hint style="info" %}
Dify DSLは、Dify.AIが定めるAIアプリケーション開発のための標準ファイルフォーマット(YML)です。この標準には、アプリケーションの基本情報、モデルのパラメータ、オーケストレーションの設定などが含まれます。
{% endhint %}

#### ローカルのDSLファイルをインポート

コミュニティや他者から提供されたDSLファイル（テンプレート）を持っている場合は、「DSLファイルをインポート」をスタジオから選択してください。インポート後、元のアプリケーションの設定が直接読み込まれます。

![DSLファイルをインポートしてアプリケーションを作成](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/188ed099d344761e396510031f991dcc.png)

#### URLを通じてDSLファイルをインポート

以下の形式を使用して、URL経由でDSLファイルをインポートすることができます：

```url
https://example.com/your_dsl.yml
```

![URL経由でDSLファイルをインポート](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-orchestrate/661112195d6fea2437ffa0dfe94436cb.png)

> DSLファイルを取り込む際には、バージョンが自動で確認されます。バージョン間に大きな違いがあると、互換性に問題が生じる恐れがあります。この件につきましては、[アプリケーション管理：インポート](https://docs.dify.ai/guides/management/app-management#importing-application)セクションで詳細をご覧いただけます。
