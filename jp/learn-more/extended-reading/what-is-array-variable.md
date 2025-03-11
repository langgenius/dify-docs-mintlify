# 配列変数とは何ですか？

配列変数は特定のデータ型で、通常は複数の要素を持っています。要素はカンマで区切られ、`[`から始まり、`]`で終わります。以下にいくつかの例を示します：

* **数字型：**
  [0, 1, 2, 3, 4, 5]
  
* **文字列型：**
  ["monday", "Tuesday", "Wednesday", "Thursday"]
  
* **JSONオブジェクト：**
  [
      {
          "name": "Alice",
          "age": 30,
          "email": "alice@example.com"
      },
      {
          "name": "Bob",
          "age": 25,
          "email": "bob@example.com"
      },
      {
          "name": "Charlie",
          "age": 35,
          "email": "charlie@example.com"
      }
  ]

### 可能な使用シーン
* [ワークフロー - リスト操作](../../guides/workflow/node/list-operator.md)：リスト操作ノードは、ファイルの形式、ファイル名、サイズなどの属性をフィルタリングおよび抽出し、異なる形式のファイルを対応する処理ノードに渡して、異なるファイル処理フローを正確に制御します。
  
* [ワークフロー - イテレーション](../../guides/workflow/node/iteration.md)：配列内の要素に対して同じ操作ステップを順番に実行し、すべての結果を出力するまで、タスクのバッチ処理機として理解できます。