# 回答

### 定義

チャットフローのプロセス内で返信内容を定義します。

テキストエディタを使用して返信フォーマットを自由に定義できます。固定のテキスト内容をカスタマイズしたり、前のステップで出力された変数を返信内容として使用したり、カスタマイズしたテキストと変数を組み合わせて返信することができます。

ノードを随時追加して内容をストリーミング形式で会話に返信し、所見即所得の設定モードをサポートし、テキストと画像の混在も可能です。例えば：

1. LLMノードの返信内容を出力
2. 生成された画像を出力
3. 純テキストを出力

**例1：** 純テキストを出力

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/workflow/node/6491003f25630e300ebd70d1deb7034e.png)

**例2：** 画像+LLMの返信を出力

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/workflow/node/aee5e83eafa2222473da745da1f8ee22.png)

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/workflow/node/19b19eddfb50fdbe880da598e43c24c9.png)

{% hint style="info" %}
回答ノードは最終的な出力ノードとして使用しないこともでき、プロセスの中間ステップで結果をストリーミング形式で出力することができます。
{% endhint %}
