# 開発ツールのセットアップガイド

Difyプラグインを開発する前に、次の準備を整えましょう。

* Difyプラグイン用のスキャフォールディングツール
* バージョン3.12以上のPython環境

### **1. Difyプラグインスキャフォールディングツールのインストール方法**

> Dify プラグイン開発スキャフォールディングツール、別名 `dify-plugin-daemon` は、プラグイン開発 SDK として見なすことができます。

[DifyプラグインのGitHubページ](https://github.com/langgenius/dify-plugin-daemon/releases) へアクセスし、ご利用のオペレーティングシステムに適したバージョンをダウンロードしてください。

**Mシリーズチップ搭載のmacOS**向けのダウンロード例：プロジェクトページから`dify-plugin-darwin-arm64`をダウンロードし、ターミナルを開いてファイルのあるディレクトリに移動した後、以下のコマンドで実行権限を付与します：

```
chmod +x dify-plugin-darwin-arm64
```

インストールが成功したかどうかを確認するには、次のコマンドを実行します。

```
./dify-plugin-darwin-arm64 version
```

> システムが「Appleによって検証されていません」と警告を出す場合は、**設定 → セキュリティとプライバシー → セキュリティ**ボタンを開き、「とにかく開く」を選択してください。

コマンドを実行し、`v0.0.1-beta.15`などのバージョン情報が表示されれば、インストール完了です。

{% hint style="info" %}
**Tips:**

`dify`コマンドをシステム全体で利用したい場合は、ダウンロードしたバイナリファイルの名前を`dify`に変更し、`/usr/local/bin`にコピーすることをお勧めします。

この設定を行うと、ターミナルから`dify version`と入力するだけで、インストールされたバージョンを確認できます。

<img src="https://assets-docs.dify.ai/2025/01/74e57a57c1ae1cc70f4a45084cbbb37e.png" alt="" data-size="original">
{% endhint %}

### **2. Initialize Python Environment**

For detailed instructions, please refer to the [Python installation](https://pythontest.com/python/installing-python-3-11/) tutorial, or ask the LLM for complete installation instructions.

### **2. Python環境の設定**

Pythonのインストール方法については、[Pythonインストール](https://pythontest.com/python/installing-python-3-11/)チュートリアルを参照するか、LLMに詳細な手順を尋ねてみてください。

### **3. プラグインの開発について**

さまざまなタイプのプラグイン開発の具体例については、以下のリンクをご参照ください。

{% content-ref url="tool-plugin.md" %}
[tool-plugin.md](tool-plugin.md)
{% endcontent-ref %}

{% content-ref url="model-plugin/" %}
[model-plugin](model-plugin/)
{% endcontent-ref %}

{% content-ref url="agent-strategy-plugin.md" %}
[agent-strategy-plugin.md](agent-strategy-plugin.md)
{% endcontent-ref %}

{% content-ref url="extension-plugin.md" %}
[extension.md](extension-plugin.md)
{% endcontent-ref %}

{% content-ref url="bundle.md" %}
[bundle.md](bundle.md)
{% endcontent-ref %}