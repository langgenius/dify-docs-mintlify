# 拡張機能型プラグイン

このドキュメントでは、Extensionタイプのプラグインを迅速に開発し、プラグイン開発の基本的な流れを理解するのに役立つように解説します。

### 事前準備

*   Difyプラグインの足場ツール
*   Python環境、バージョン番号 ≥ 3.12

プラグイン開発の足場ツールの準備方法については、[開発ツールの初期化](initialize-development-tools.md)を参照してください。

### 新規プロジェクトの作成 <a href="#chuang-jian-xin-xiang-mu" id="chuang-jian-xin-xiang-mu"></a>

現在のパスで、足場コマンドラインツールを実行し、新しいDifyプラグインプロジェクトを作成します。

```
./dify-plugin-darwin-arm64 plugin init
```

このバイナリファイルを`dify`にリネームし、`/usr/local/bin`パスにコピーした場合、以下のコマンドを実行して新しいプラグインプロジェクトを作成できます。

```bash
dify plugin init
```

### **プラグイン情報の入力**

表示される指示に従って、プラグイン名、作者情報、プラグインの説明を設定してください。チームで共同作業する場合は、作者を組織名にすることも可能です。

> プラグイン名の長さは1〜128文字で、文字、数字、ダッシュ、アンダースコアのみを使用できます。

![Plugins details](https://assets-docs.dify.ai/2024/12/75cfccb11fe31c56c16429b3998f2eb0.png)

入力が完了したら、プラグイン開発言語の選択でPythonを選択してください。

![Plugins development: Python](https://assets-docs.dify.ai/2024/11/1129101623ac4c091a3f6f75f4103848.png)

### 3. プラグインタイプの選択とプロジェクトテンプレートの初期化

足場ツール内のすべてのテンプレートには、完全なコードプロジェクトが用意されています。このドキュメントでは、例として`Extension`タイプのプラグインテンプレートを使用します。プラグインに精通している開発者であれば、テンプレートを使用せずに、[APIドキュメント](../../schema-definition/)を参照して様々なタイプのプラグイン開発を進めることができます。

![拡張機能](https://assets-docs.dify.ai/2024/11/ff08f77b928494e10197b456fc4e2d5b.png)

#### プラグイン権限の設定

プラグインがDifyメインプラットフォームに正常に接続するためには、Difyメインプラットフォームの権限を読み取る必要があります。このサンプルプラグインには、以下の権限を付与してください。

*   ツール
*   LLM
*   アプリ
*   永続ストレージを有効にし、デフォルトサイズのストレージを割り当てる
*   エンドポイントの登録を許可する

> ターミナル内で方向キーを使って権限を選択し、「Tab」キーで権限を付与します。

すべての権限項目をチェックした後、Enterキーを押してプラグインの作成を完了します。システムが自動的にプラグインのプロジェクトコードを生成します。

![プラグインの権限](https://assets-docs.dify.ai/2024/11/5518ca1e425a7135f18f499e55d16bdd.png)

プラグインの基本ファイル構造は以下の通りです。

```
.
├── GUIDE.md
├── README.md
├── _assets
│   └── icon.svg
├── endpoints
│   ├── your-project.py
│   └── your-project.yaml
├── group
│   └── your-project.yaml
├── main.py
├── manifest.yaml
└── requirements.txt
```

*   `GUIDE.md`: プラグインの作成プロセスを説明する簡単なチュートリアルです。
*   `README.md`: 現在のプラグインに関する情報です。このプラグインの概要や使用方法をこのファイルに記述する必要があります。
*   `_assets`: 現在のプラグインに関連するすべてのマルチメディアファイルを保存します。
*   `endpoints`: CLIのガイドに従って作成される`Extension`タイプのプラグインテンプレートです。このディレクトリには、すべてのエンドポイントの機能実装コードが格納されています。
*   `group`: 秘密鍵のタイプ、多言語設定、API定義ファイルのパスを指定します。
*   `main.py`: プロジェクト全体のエントリポイントとなるファイルです。
*  `manifest.yaml`: プラグインの基本設定ファイルです。このプラグインに必要な権限、拡張機能の種類などの設定情報が含まれています。
*   `requirements.txt`: Python環境の依存関係を記述します。

### プラグインの開発

#### 1. プラグインのリクエストエンドポイントの定義

`endpoints/test_plugin.yaml`を編集し、以下のコードを参考に変更してください。

```yaml
path: "/neko"
method: "GET"
extra:
  python:
    source: "endpoints/test_plugin.py"
```

このコードは、プラグインのエントリパスを`/neko`、リクエストメソッドをGETタイプとして定義するものです。プラグインの機能実装コードは、`endpoints/test_plugin.py`ファイルに記述します。

#### 2. プラグイン機能の作成

プラグインの機能：プラグインサービスをリクエストし、猫の情報を出力します。

プラグインの機能実装コードを`endpoints/test_plugin.py`ファイルに記述します。以下のサンプルコードを参考にしてください。

```python
from typing import Mapping
from werkzeug import Request, Response
from flask import Flask, render_template_string
from dify_plugin import Endpoint

app = Flask(__name__)

class NekoEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        ascii_art = '''
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛⬛️⬜️⬜️⬜️⬜️⬜⬜️⬜️️
🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧⬛️⬜️⬜️⬜️⬜️⬜⬜️️
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️🥧🥧🥧💟💟💟💟💟💟💟💟💟💟💟💟💟🥧🥧🥧⬛️⬜️⬜️⬜️⬜⬜️️
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️🥧🥧💟💟💟💟💟💟🍓💟💟🍓💟💟💟💟💟🥧🥧⬛️⬜️⬜️⬜️⬜️⬜️️
🟧🟧🟥🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟧🟥🟥🟥🟥🟥🟥🟥⬛🥧💟💟🍓💟💟💟💟💟💟💟💟💟💟💟💟💟💟🥧⬛️⬜️⬜️⬜️⬜⬜️️
🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛️🥧💟💟💟💟💟💟💟💟💟💟⬛️⬛️💟💟🍓💟💟🥧⬛️⬜️⬛️️⬛️️⬜⬜️️
🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛️🥧💟💟💟💟💟💟💟💟💟⬛️🌫🌫⬛💟💟💟💟🥧⬛️⬛️🌫🌫⬛⬜️️
🟨🟨🟧🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟨🟧⬛️⬛️⬛️⬛️🟧🟧⬛️🥧💟💟💟💟💟💟🍓💟💟⬛️🌫🌫🌫⬛💟💟💟🥧⬛️🌫🌫🌫⬛⬜️️
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛️🌫🌫⬛️⬛️🟧⬛️🥧💟💟💟💟💟💟💟💟💟⬛️🌫🌫🌫🌫⬛️⬛️⬛️⬛️🌫🌫🌫🌫⬛⬜️️
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛️⬛️🌫🌫⬛️⬛️⬛️🥧💟💟💟🍓💟💟💟💟💟⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛⬜️️
🟩🟩🟨🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩🟩🟨🟨⬛⬛️🌫🌫⬛️⬛️🥧💟💟💟💟💟💟💟🍓⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛️
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛️⬛️🌫🌫⬛️🥧💟🍓💟💟💟💟💟💟⬛️🌫🌫🌫⬜️⬛️🌫🌫🌫🌫🌫⬜️⬛️🌫🌫⬛️
️🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛️⬛️⬛️⬛️🥧💟💟💟💟💟💟💟💟⬛️🌫🌫🌫⬛️⬛️🌫🌫🌫⬛️🌫⬛️⬛️🌫🌫⬛️
🟦🟦🟩🟩🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦🟦🟩🟩🟩🟩🟩🟩⬛️⬛️🥧💟💟💟💟💟🍓💟💟⬛🌫🟥🟥🌫🌫🌫🌫🌫🌫🌫🌫🌫🟥🟥⬛️
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛️🥧🥧💟🍓💟💟💟💟💟⬛️🌫🟥🟥🌫⬛️🌫🌫⬛️🌫🌫⬛️🌫🟥🟥⬛️
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛️🥧🥧🥧💟💟💟💟💟💟💟⬛️🌫🌫🌫⬛️⬛️⬛️⬛️⬛️⬛️⬛️🌫🌫⬛️⬜️
🟪🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪🟪🟪🟪🟪🟪🟪🟪🟦🟦🟦🟦🟦🟦⬛️⬛️⬛️🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛️⬜️⬜️
🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛️🌫🌫🌫⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️
🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛️🌫🌫⬛️⬛️⬜️⬛️🌫🌫⬛️⬜️⬜️⬜️⬜️⬜️⬛️🌫🌫⬛️⬜️⬛️🌫🌫⬛️⬜️⬜️⬜️⬜️
⬜️⬜️🟪🟪🟪🟪🟪🟪🟪🟪⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟪🟪🟪🟪🟪⬛️⬛️⬛️⬛⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬜️️
        '''
        ascii_art_lines = ascii_art.strip().split('\n')
        with app.app_context():
            return Response(render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: black;
                color: white;
                overflow: hidden;
                margin: 0;
                padding: 0;
            }
            #ascii-art {
                font-family: monospace;
                white-space: pre;
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                display: inline-block;
                font-size: 16px;
                line-height: 1;
            }
        </style>
    </head>
    <body>
        <div id="ascii-art"></div>
        <script>
            var asciiArtLines = {{ ascii_art_lines | tojson }};
            var asciiArtDiv = document.getElementById("ascii-art");
            var index = 0;
            function displayNextLine() {
                if (index < asciiArtLines.length) {
                    var line = asciiArtLines[index];
                    var lineElement = document.createElement("div");
                    lineElement.innerHTML = line;
                    asciiArtDiv.appendChild(lineElement);
                    index++;
                    setTimeout(displayNextLine, 100);
                } else {
                    animateCat();
                }
            }
            function animateCat() {
                var pos = 0;
                var screenWidth = window.innerWidth;
                var catWidth = asciiArtDiv.offsetWidth;
                function move() {
                    asciiArtDiv.style.left = pos + "px";
                    pos += 2;
                    if (pos > screenWidth) {
                        pos = -catWidth;
                    }
                    requestAnimationFrame(move);
                }
                move();
            }
            displayNextLine();
        </script>
    </body>
    </html>
        ''', ascii_art_lines=ascii_art_lines), status=200, content_type="text/html")
```

このコードを実行する前に、まず以下のPythonの依存パッケージをインストールする必要があります。

```python
pip install werkzeug
pip install flask
pip install dify-plugin
```

### プラグインのデバッグ

次に、プラグインが正常に動作するかどうかをテストします。Difyはリモートデバッグ機能を提供しており、「プラグイン管理」ページでデバッグキーとリモートサーバーのアドレスを取得できます。

![](https://assets-docs.dify.ai/2024/11/1cf15bc59ea10eb67513c8bdca557111.png)

プラグインのプロジェクトに戻り、`.env.example`ファイルをコピーして`.env`にリネームします。そして、取得したリモートサーバーのアドレスやデバッグキーなどの情報を`.env`ファイルに記入してください。

`.env`ファイルの内容：

```bash
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=remote-url
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=****-****-****-****-****
```

`python -m main`コマンドを実行してプラグインを起動します。プラグインページで、このプラグインがワークスペースにインストールされたことを確認できます。他のチームメンバーもこのプラグインにアクセス可能です。

![](https://assets-docs.dify.ai/2024/11/0fe19a8386b1234755395018bc2e0e35.png)

プラグイン内に新しいエンドポイントを追加し、名前や`api_key`などの情報を任意で入力します。自動生成されたURLにアクセスすると、プラグインが提供するウェブサービスが表示されます。

![](https://assets-docs.dify.ai/2024/11/c76375b8df2449d0d8c31a7c2a337579.png)

### プラグインのパッケージ化

プラグインが正常に動作することを確認したら、以下のコマンドラインツールを使用してプラグインをパッケージ化し、名前を付けることができます。実行後、現在のフォルダに`neko.difypkg`というファイルが生成されます。このファイルが最終的なプラグインパッケージです。

```bash
dify-plugin package ./neko
```

おめでとうございます！これで、プラグインの開発、テスト、パッケージ化の全工程が完了しました。

### プラグインの公開

作成したプラグインは、[Dify Plugins コードリポジトリ](https://github.com/langgenius/dify-plugins)にアップロードして公開できます。アップロードする前に、プラグインが[プラグイン公開仕様](../publish-plugins/publish-to-dify-marketplace)に準拠していることを確認してください。審査に合格すると、コードはメインブランチにマージされ、[Dify Marketplace](https://marketplace.dify.ai/)に自動的に公開されます。

### さらに詳しく

**クイックスタート：**

*   [バンドルタイププラグイン：複数のプラグインをまとめる](bundle.md)
*   [ツールタイププラグイン：Google検索](tool-type-plugin.md)
*   [モデルタイププラグイン](model/)

**プラグインインターフェースドキュメント：**

*   [マニフェスト](../../schema-definition/manifest.md)構造
*   [エンドポイント](../../schema-definition/endpoint.md)詳細定義
*   [Dify機能の逆呼び出し](../../schema-definition/reverse-invocation-of-the-dify-service/)
*   [ツール](../../schema-definition/tool.md)
*   [モデル](../../schema-definition/model/)
*   [拡張エージェント戦略](../../schema-definition/agent.md)

**ベストプラクティス：**

[Slack Botプラグインの開発](../../best-practice/develop-a-slack-bot-plugin.md)