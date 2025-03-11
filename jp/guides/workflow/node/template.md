# テンプレート

### 定義

Jinja2のPythonテンプレート言語を使って、データ変換やテキスト処理などを柔軟に行うことができます。

### Jinjaとは？

> Jinjaは、高速で表現力豊かで拡張可能なテンプレートエンジンです。
>
> Jinja は、速く、表現力があり、拡張可能なテンプレートエンジンです。

—— [https://jinja.palletsprojects.com/en/3.1.x/](https://jinja.palletsprojects.com/en/3.1.x/)

### シーン

テンプレートノードを使うことで、強力なPythonテンプレート言語であるJinja2を用いて、ワークフロー内で軽量かつ柔軟なデータ変換が可能になります。これは、テキスト処理やJSON変換などのシナリオに適しています。例えば、前のステップからの変数を柔軟にフォーマットして結合し、単一のテキスト出力を作成することができます。これは、複数のデータソースの情報を特定のフォーマットにまとめ、後続のステップの要件を満たすのに非常に適しています。

**例1：**複数の入力（記事のタイトル、紹介、内容）を一つの完全なテキストに結合する

![テキストの結合](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/workflow/node/7a3c701efd43e3d1729cb3baebe86018.png)

**例2：** ナレッジリトリーバルノードで取得した情報およびその関連メタデータを、構造化されたMarkdown形式にまとめる

```
{% raw %}
{% for item in chunks %}
### Chunk {{ loop.index }}. 
### Similarity: {{ item.metadata.score | default('N/A') }}

#### {{ item.title }}

##### Content
{{ item.content | replace('\n', '\n\n') }}

---
{% endfor %}
{% endraw %}
```

![ナレッジリトリーバルノードの出力をMarkdownに変換](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCdDIVDY6AtAz028MFT4d%2Fuploads%2FOtGkLaz38v0FSzSBNuV2%2Fimage.png?alt=media&token=122965f8-9d70-4e57-b0e2-1fdaf1320275)

Jinjaの[公式ドキュメント](https://jinja.palletsprojects.com/en/3.1.x/templates/)を参考にして、さまざまなタスクを実行するためのより複雑なテンプレートを作成することができます。
