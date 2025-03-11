# 高度接続ツール

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい開発手順については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/develop-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

高度接続を始める前に、[クイック接続](https://docs.dify.ai/v/ja-jp/guides/tools/quick-tool-integration)を読んで、Difyのツール接続プロセスについて基本的な理解を持っていることを確認してください。

### ツールインターフェース

`Tool`クラスには、開発者がより複雑なツールを迅速に構築できるようにするための一連のショートカットメソッドが定義されています。

#### メッセージ応答

Difyは`テキスト`、`リンク`、`画像`、`ファイルBLOB`などのさまざまなメッセージタイプをサポートしており、以下のインターフェースを使用して、LLMやユーザーに異なるタイプのメッセージを返すことができます。

注意点：以下のインターフェースの一部のパラメータは、後の章で紹介します。

**画像URL**

画像のURLを渡すだけで、Difyは自動的に画像をダウンロードしてユーザーに返します。

```python
    def create_image_message(self, image: str, save_as: str = '') -> ToolInvokeMessage:
        """
            画像メッセージを作成

            :param image: 画像のURL
            :return: 画像メッセージ
        """
```

**リンク**

リンクを返す必要がある場合は、以下のインターフェースを使用できます。

```python
    def create_link_message(self, link: str, save_as: str = '') -> ToolInvokeMessage:
        """
            リンクメッセージを作成

            :param link: リンクのURL
            :return: リンクメッセージ
        """
```

**テキスト**

テキストメッセージを返す必要がある場合は、以下のインターフェースを使用できます。

```python
    def create_text_message(self, text: str, save_as: str = '') -> ToolInvokeMessage:
        """
            テキストメッセージを作成

            :param text: メッセージのテキスト
            :return: テキストメッセージ
        """
```

**ファイルBLOB**

画像、音声、動画、PPT、Word、Excelなどのファイルの生データを返す必要がある場合は、以下のインターフェースを使用できます。

* `blob` ファイルの生データ、bytesタイプ
* `meta` ファイルのメタデータ、ファイルタイプが分かる場合は`mime_type`を渡すことが推奨されます。そうでない場合、Difyはデフォルトで`octet/stream`を使用します。

```python
    def create_blob_message(self, blob: bytes, meta: dict = None, save_as: str = '') -> ToolInvokeMessage:
        """
            BLOBメッセージを作成

            :param blob: BLOBデータ
            :return: BLOBメッセージ
        """
```

#### クイックツール

大規模モデル応用において、以下の2つの一般的なニーズがあります：

* 長文を事前に要約し、その要約内容をLLMに渡すことで、原文が長すぎてLLMが処理できない問題を防ぐ
* ツールが取得した内容がリンクである場合、ウェブページ情報をスクレイピングしてからLLMに返す

これらのニーズを迅速に実現するために、以下の2つのクイックツールを提供しています。

**テキスト要約ツール**

このツールはuser\_idと要約する必要があるテキストを入力し、要約されたテキストを返します。Difyは現在のワークスペースのデフォルトモデルを使用して長文を要約します。

```python
    def summary(self, user_id: str, content: str) -> str:
        """
            コンテンツを要約

            :param user_id: ユーザーID
            :param content: コンテンツ
            :return: 要約
        """
```

**ウェブスクレイピングツール**

このツールはスクレイピングするウェブページのリンクとユーザーエージェント（任意）を入力し、そのウェブページ情報を含む文字列を返します。`user_agent`はオプションのパラメータで、ツールを識別するために使用されます。入力しない場合、Difyはデフォルトの`user_agent`を使用します。

```python
    def get_url(self, url: str, user_agent: str = None) -> str:
        """
            URLを取得
        """ スクレイピング結果
```

#### 変数プール

`Tool`では、ツールの実行中に生成される変数やファイルなどを保存するための変数プールを導入しています。これらの変数は、ツールの実行中に他のツールによって使用されることがあります。

以下に、`DallE3`と`Vectorizer.AI`を例に、変数プールの使用方法を紹介します。

* `DallE3`はテキストに基づいて画像を生成するツールで、ここでは`DallE3`がカフェのロゴを生成します。
* `Vectorizer.AI`は画像をベクター画像に変換するツールで、生成された画像を無限に拡大しても劣化しないようにし、ここでは`DallE3`が生成したPNGアイコンをベクター画像に変換し、デザイナーが実際に使用できるようにします。

**DallE3**

まず、DallE3を使用して画像を生成し、生成された画像を変数プールに保存します。コードは以下の通りです。

```python
from typing import Any, Dict, List, Union
from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

from base64 import b64decode

from openai import OpenAI

class DallE3Tool(BuiltinTool):
    def _invoke(self, 
                user_id: str, 
               tool_Parameters: Dict[str, Any], 
        ) -> Union[ToolInvokeMessage, List[ToolInvokeMessage]]:
        """
            invoke tools
        """
        client = OpenAI(
            api_key=self.runtime.credentials['openai_api_key'],
        )

        # プロンプト
        prompt = tool_Parameters.get('prompt', '')
        if not prompt:
            return self.create_text_message('プロンプトを入力してください')

        # openapi dalle3を呼び出す
        response = client.images.generate(
            prompt=prompt, model='dall-e-3',
            size='1024x1024', n=1, style='vivid', quality='standard',
            response_format='b64_json'
        )

        result = []
        for image in response.data:
            # すべての画像をsave_asパラメータを介して変数プールに保存し、変数名をself.VARIABLE_KEY.IMAGE.valueに設定します。後続の新しい画像が生成される場合、前の画像が上書きされます。
            result.append(self.create_blob_message(blob=b64decode(image.b64_json), 
                                                   meta={ 'mime_type': 'image/png' },
                                                    save_as=self.VARIABLE_KEY.IMAGE.value))

        return result
```

ここで、`self.VARIABLE_KEY.IMAGE.value`を画像の変数名として使用していることに注意してください。開発者のツールが相互に連携できるように、この`KEY`を定義しました。自由に使用してもよいし、カスタムの`KEY`を渡しても構いません。

**Vectorizer.AI**

次に、Vectorizer.AIを使用して、DallE3が生成したPNGアイコンをベクター画像に変換します。ここで定義した関数を確認します。コードは以下の通りです。

```python
from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage, ToolParameter
from core.tools.errors import ToolProviderCredentialValidationError

from typing import Any, Dict, List, Union
from httpx import post
from base64 import b64decode

class VectorizerTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_Parameters: Dict[str, Any]) \
        -> Union[ToolInvokeMessage, List[ToolInvokeMessage]]:
        """
        ツールを呼び出す。画像変数名はここで渡す必要があるため、変数プールから画像を取得できます。
        """
        
    
    def get_runtime_parameters(self) -> List[ToolParameter]:
        """
        ツールパラメータリストをオーバーライドします。ここでは、変数プールの実際の状況に基づいてパラメータリストを動的に生成し、それに基づいてLLMがフォームを生成できます。
        """
        
    
    def is_tool_available(self) -> bool:
        """
        現在のツールが使用可能かどうかを確認します。変数プールに画像がない場合、LLMがこのツールを表示する必要はありません。ここでFalseを返します。
        """     
```

次に、これらの3つの関数を実装します。

```python
from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage, ToolParameter
from core.tools.errors import ToolProviderCredentialValidationError

from typing import Any, Dict, List, Union
from httpx import post
from base64 import b64decode

class VectorizerTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_Parameters: Dict[str, Any]) \
        -> Union[ToolInvokeMessage, List[ToolInvokeMessage]]:
        """
            ツールを呼び出す
        """
        api_key_name = self.runtime.credentials.get('api_key_name', None)
        api_key_value = self.runtime.credentials.get('api_key_value', None)

        if not api_key_name or not api_key_value:
            raise ToolProviderCredentialValidationError('APIキー名と値を入力してください')

        # 画像IDを取得、画像IDの定義はget_runtime_parametersで確認できます。
        image_id = tool_Parameters.get('image_id', '')
        if not image_id:
            return self.create_text_message('画像IDを入力してください')

        # 変数プールから以前のDallEが生成した画像を取得
        image_binary = self.get_variable_file(self.VARIABLE_KEY.IMAGE)
        if not image_binary:
            return self.create_text_message('画像が見つかりません。まずユーザーに画像を生成するよう依頼してください。')

        # ベクター画像を生成
        response = post(
            'https://vectorizer.ai/api/v1/vectorize',
            files={ 'image': image_binary },
            data={ 'mode': 'test' },
            auth=(api_key_name, api_key_value), 
            timeout=30
        )

        if response.status_code != 200:
            raise Exception(response.text)
        
        return [
            self.create_text_message('ベクター化されたSVGが画像として保存されました。'),
            self.create_blob_message(blob=response.content,
                                    meta={'mime_type': 'image/svg+xml'})
        ]
    
    def get_runtime_parameters(self) -> List[ToolParameter]:
        """
        実行時パラメータをオーバーライド
        """
        # ここでは、ツールパラメータリストをオーバーライドし、image_idを定義し、そのオプションリストを現在の変数プール内のすべての画像に設定しました。ここでの設定はyamlの設定と一致しています。
        return [
            ToolParameter.get_simple_instance(
                name='image_id',
                llm_description=f'ベクター化する画像ID。画像IDは{[i.name for i in self.list_default_image_variables()]}の中から指定してください。',
                type=ToolParameter.ToolParameterType.SELECT,
                required=True,
                options=[i.name for i in self.list_default_image_variables()]
            )
        ]
    
    def is_tool_available(self) -> bool:
        # 変数プールに画像がある場合のみ、LLMがこのツールを使用する必要があります。
        return len(self.list_default_image_variables()) > 0
```

ここで注意すべきは、実際には`image_id`を使用していないことです。このツールを呼び出すときに、デフォルトの変数プールに必ず画像があると仮定しているため、直接`image_binary = self.get_variable_file(self.VARIABLE`を使用しています。 `mage_id`、私たちはこのツールを呼び出す際には必ず変数プールに画像が存在すると仮定しましたので、`画像バイナリ = self.get_variable_file(self.変数キー.画像)`を直接使用して画像を取得しました。モデルの能力が弱い場合、開発者の皆さんもこの方法を用いることをお勧めします。これにより、モデルが誤ったパラメータを渡すことを防ぎ、エラー許容率を効果的に向上させることができます。