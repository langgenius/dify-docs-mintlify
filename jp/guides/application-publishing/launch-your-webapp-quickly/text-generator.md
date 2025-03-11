# テキスト生成型アプリケーション

テキスト生成型アプリケーションは、ユーザーが提供するプロンプトに基づいて高品質のテキストを自動生成するアプリケーションです。記事の要約や翻訳など、さまざまなタイプのテキストを生成することができます。

テキスト生成型アプリケーションは以下の機能をサポートしています：

1. 一回実行。
2. バッチ実行。
3. 実行結果の保存。
4. より類似した結果の生成。

以下にそれぞれの機能を紹介します。

### 一度実行

クエリ内容を入力し、実行ボタンをクリックすると、右側に結果が生成されます。以下の図のように：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-publishing/launch-your-webapp-quickly/4c5380cf71066d933082f7c30deacb01.png)

生成された結果部分では、「コピー」ボタンをクリックすると内容をクリップボードにコピーできます。「保存」ボタンをクリックすると内容を保存できます。「保存済み」タブで保存した内容を見ることができます。また、生成された内容には「いいね」や「バッド」をつけることもできます。

### バッチ実行

時には、アプリケーションを何度も実行する必要があります。例えば、テーマに基づいて記事を生成するWebアプリケーションがあるとします。今、100種類のテーマに基づいて記事を生成する必要があるとします。この場合、このタスクを100回も行うのは非常に面倒です。また、1つのタスクが完了するのを待たなければ次のタスクを開始できません。

上記のシナリオでは、バッチ実行機能を使うと操作が便利になり（テーマを `csv` ファイルに入力し、一度だけ実行する）、生成時間も節約できます（複数のタスクが同時に実行される）。使用方法は以下の通りです：

#### 第1歩 バッチ実行ページに入る

「バッチ実行」タブをクリックすると、バッチ実行ページに入ります。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-publishing/launch-your-webapp-quickly/c8381ab7fad14a54c86835dc4b1b6b5d.png)

#### 第2歩 テンプレートをダウンロードして内容を入力する

「テンプレートダウンロード」ボタンをクリックし、テンプレートをダウンロードします。テンプレートを編集し、内容を入力して `.csv` 形式のファイルとして保存します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-publishing/launch-your-webapp-quickly/bae4859c5cb7404ce901b7979237bb93.png)

#### 第3歩 ファイルをアップロードして実行

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-publishing/launch-your-webapp-quickly/fc84f62f41c12e14ff85b29e6bf43d27.png)

生成された内容をエクスポートする必要がある場合は、右上の「ダウンロードボタン」をクリックして `csv` ファイルとしてエクスポートできます。

**注意:** アップロードする `csv` ファイルのエンコードは `ユニコード` でなければなりません。そうでないと、実行結果が失敗する可能性があります。解決策：ExcelやWPSなどで `csv` ファイルをエクスポートする際に、エンコードを `ユニコード` に選択します。

### 保存結果

生成結果の下にある「保存」ボタンをクリックすると、実行結果を保存できます。「保存済み」タブで、すべての保存された内容を見ることができます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-publishing/launch-your-webapp-quickly/3cdd15e87aa1f1aae9f6abadb0f16d1f.png)

### より多くの類似結果の生成

アプリケーションのオーケストレーションで「より類似した」機能を有効にしている場合、Webアプリケーションで「より類似した」ボタンをクリックすると、現在の結果と似た内容を生成できます。以下の図の通りです：

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/application-publishing/launch-your-webapp-quickly/65fb111d8e89a8f7b761859265e42f0a.png)