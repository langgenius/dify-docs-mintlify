## ツール

詳細なインターフェースドキュメントを読む前に、[クイックスタート：ツール](../develop-plugins/tool-plugin.md) を参照し、Difyプラグインにおけるツールの利用プロセスについて、概要を把握しておいてください。

### **データ構造**

#### **メッセージの出力**

Difyは、`text`、`links`、`images`、`file BLOBs`、`JSON`といった複数のメッセージタイプをサポートしています。様々なインターフェースを通じて、これらの異なるタイプのメッセージを出力できます。

デフォルトでは、ワークフロー内でツールが出力する際には、`files`、`text`、`json`という3つの固定の変数が用意されています。これらの変数にデータを設定するには、以下のメソッドを使用します。

例えば、`create_image_message`を使用すると、画像を出力できます。また、ツールはワークフロー内で参照しやすいように、カスタムの出力変数もサポートしています。

#### **画像URL**

画像のURLを渡すだけで、Difyが自動的に画像をダウンロードし、ユーザーに送信します。

```python
def create_image_message(self, image: str) -> ToolInvokeMessage:
    pass
```

#### **リンク**

リンクを出力するには、このインターフェースを使用します。

```python
def create_link_message(self, link: str) -> ToolInvokeMessage:
    pass
```

#### **テキスト**

テキストメッセージを出力するには、このインターフェースを使用します。

```python
def create_text_message(self, text: str) -> ToolInvokeMessage:
    pass
```

#### **ファイル**

生のファイルデータ（画像、音声、動画、PPT、Word、Excelなど）を出力するには、このインターフェースを使用します。

*   `blob`: バイト形式の生ファイルデータ
*   `meta`: ファイルのメタデータです。`mime_type`を指定することで、ファイルの種類を明示できます。指定しない場合は、Difyがデフォルトで`octet/stream`を使用します。

```python
def create_blob_message(self, blob: bytes, meta: dict = None) -> ToolInvokeMessage:
    pass
```

#### **JSON**

フォーマットされたJSONを出力するには、このインターフェースを使用します。通常、ワークフロー内のノード間でデータをやり取りする際に使用されます。多くの大規模言語モデルは、エージェントモードでJSON形式のデータを読み取り、理解できます。

```python
def create_json_message(self, json: dict) -> ToolInvokeMessage:
    pass
```

#### **変数**

ストリーミングではない出力変数を設定するには、このインターフェースを使用します。後から設定された値は、以前の設定値を上書きします。

```python
def create_variable_message(self, variable_name: str, variable_value: Any) -> ToolInvokeMessage:
    pass
```

#### **ストリーミング変数**

テキストをタイプライターのように表示するには、ストリーミング変数を使用します。チャットフローアプリケーションの応答ノードでこの変数を参照すると、テキストがタイプライター効果で表示されます。現在、文字列データのみをサポートしています。

```python
def create_stream_variable_message(
    self, variable_name: str, variable_value: str
) -> ToolInvokeMessage:
```

#### **出力変数の定義**

ワークフロー内でツールの出力変数を参照するには、事前に出力される可能性のある変数を定義しておく必要があります。Difyプラグインは、`json_schema`形式での出力変数定義をサポートしています。以下に設定例を示します。

```yaml
identity:
  author: author
  name: tool
  label:
    en_US: label
    zh_Hans: 标签
    ja_JP: レベル
    pt_BR: etiqueta
description:
  human:
    en_US: description
    zh_Hans: 描述
    ja_JP: 説明
    pt_BR: descrição
  llm: description
output_schema:
  type: object
  properties:
    name:
      type: string
```

この例では、ワークフロー内で参照できる `name` フィールドを含む `output_schema` を持つシンプルなツールを定義しています。実際に使用するには、ツールの実装コード内で変数を設定する必要があることに注意してください。そうしないと、`None` が設定されます。