# Notionデータをインポート

DifyデータセットはNotionからのインポートをサポートし、**同期**を設定することで、Notionのデータが更新されると自動的にDifyに同期されます。

### 認証確認

1. データセットを作成し、データソースを選択する際に、**Notion内容から同期-- バインドへ進み、指示に従って認証確認を完了してください。**
2. または、**設定 -- データソース -- データソースを追加**に進み、Notionソースで**バインド**をクリックして認証確認を完了することもできます。

![Notionをバインド](https://assets-docs.dify.ai/2024/12/f1d5bcdcfbd57407e0bce1597df4daad.png)

### Notionデータのインポート

認証確認が完了したら、データセット作成ページに進み、**Notion内容から同期**をクリックし、必要な認証ページを選択してインポートします。

![Notionをインポートする](https://assets-docs.dify.ai/2024/12/863f1cd15318b146a556c34e93c5df2c.png)

### 分割とクリーニングの実施

次に、**分割設定**と**インデックス方式**を選択し、**保存して処理**をクリックします。Difyがこれらのデータを処理するのを待ちます。このステップでは、大規模言語モデル（LLM）サプライヤーでトークンが消費される場合があります。Difyは通常のページデータのインポートをサポートするだけでなく、データベースタイプのページ属性もまとめて保存します。

_**注意点：画像やファイルのインポートは現在サポートされていません。表データはテキストとして表示されます。**_

![Notionのコンテンツをチャンク化する](https://assets-docs.dify.ai/2024/12/ab1b1aa690adad153cac0a321b6b7585.png)

### Notionデータの同期

Notionの内容に変更があった場合、Difyデータセットの**文書リストページ**で**同期**をクリックするだけで、データを一括で同期できます。このステップでもトークンが消費されます。

![Notion内容を同期](https://assets-docs.dify.ai/2024/12/af7cabd98c3aac392819d9041cc408de.png)

### コミュニティ版Notionの統合設定方法

Notionの統合は、**インターナル統合**（internal integration）と**パブリック統合**（public integration）の2種類があります。Difyで必要に応じて設定できます。2つの統合方法の具体的な違いについては[Notion公式ドキュメント](https://developers.notion.com/docs/authorization)を参照してください。

### 1、**インターナル統合方式の利用**

まず、統合設定ページで[統合を作成](https://www.notion.so/my-integrations)します。デフォルトでは、すべての統合はインターナル統合として開始されます。インターナル統合は選択したワークスペースと関連付けられるため、ワークスペースの所有者である必要があります。

具体的な操作手順：

**New integration**ボタンをクリックし、タイプはデフォルトで**インターナル**（変更不可）です。関連付けるスペースを選択し、統合名を入力しロゴをアップロードした後、**Submit**をクリックして統合を作成します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/knowledge-base/create-knowledge-and-upload-documents/import-online-datasource/87e612b70469281ed2ec2c45038daf1e.png)

統合を作成したら、必要に応じてCapabilitiesタブで設定を更新し、Secretsタブで**Show**ボタンをクリックしてSecretsをコピーします。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/knowledge-base/create-knowledge-and-upload-documents/import-online-datasource/a2e0a30fb3903d8cce6556ed9ecd3951.png)

コピーした後、Difyのソースコードに戻り、**.env**ファイルに関連する環境変数を設定します。環境変数は以下の通りです：

**NOTION\_INTEGRATION\_TYPE** = インターナル または **NOTION\_INTEGRATION\_TYPE** = パブリック

**NOTION\_INTERNAL\_SECRET**=you-internal-secret

### 2、**パブリック統合方式の利用**

**インターナル統合をパブリック統合にアップグレードする必要があります**。統合の配布ページに移動し、スイッチを切り替えて統合を公開します。スイッチをパブリック設定に切り替えるには、以下の組織情報フォームに会社名、Webサイト、リダイレクトURLなどの情報を入力し、**Submit**ボタンをクリックします。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/knowledge-base/create-knowledge-and-upload-documents/import-online-datasource/3e7a700f41464d88057e63050c6f2093.png)

統合の設定ページで公開に成功すると、密鍵タブで統合の密鍵にアクセスできるようになります：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/knowledge-base/create-knowledge-and-upload-documents/import-online-datasource/554557566ef3f56076be1e8542c4cddb.png)

Difyのソースコードに戻り、**.env**ファイルに関連する環境変数を設定します。環境変数は以下の通りです：

**NOTION\_INTEGRATION\_TYPE**=パブリック

**NOTION\_CLIENT\_SECRET**=you-client-secret

**NOTION\_CLIENT\_ID**=you-client-id

設定が完了したら、データセットでNotionのデータインポートおよび同期機能を操作できます。
