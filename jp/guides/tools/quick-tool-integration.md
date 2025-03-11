# ツールを迅速に接続

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい開発手順については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/develop-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

ここでは、GoogleSearchを例にとって、ツールを迅速に接続する方法をご紹介します。

### 1. ツールプロバイダーのyamlを準備

#### イントロダクション

このyamlには、プロバイダーの名前、アイコン、著者などの詳細情報が含まれており、前端で柔軟に表示できるようにします。

#### サンプル

`core/tools/provider/builtin`フォルダーに`google`モジュール（フォルダー）を作成し、その中に`google.yaml`を作成します。名前はモジュール名と一致する必要があります。

以降、このツールに関するすべての操作はこのモジュール内で行います。

```yaml
identity: # ツールプロバイダーの基本情報
  author: Dify # 著者
  name: google # 名前、唯一無二で、他のプロバイダーと重複してはいけません
  label: # ラベル、前端表示用
    en_US: Google # 英語ラベル
    zh_Hans: Google # 中国語ラベル
    ja_JP: : Google # 日本語ラベル
    pt_BR: : : Google # プルトガル語ラベル
  description: # 説明、前端表示用
    en_US: Google # 英語説明
    zh_Hans: Google # 中国語説明
    ja_JP: : Google # 日本語説明
    pt_BR: : Google # プルトガル語説明
  icon: icon.svg # アイコン、現在のモジュールの_assetsフォルダーに配置する必要があります

```

* `identity` フィールドは必須です。著者、名前、ラベル、説明、アイコンなどの基本情報が含まれています。
  * アイコンは現在のモジュールの`_assets`フォルダーに配置する必要があります。参考例：api/core/tools/provider/builtin/google/_assets/icon.svg

      ```xml
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="25" viewBox="0 0 24 25" fill="none">
        <path d="M22.501 12.7332C22.501 11.8699 22.4296 11.2399 22.2748 10.5865H12.2153V14.4832H18.12C18.001 15.4515 17.3582 16.9099 15.9296 17.8898L15.9096 18.0203L19.0902 20.435L19.3106 20.4565C21.3343 18.6249 22.501 15.9298 22.501 12.7332Z" fill="#4285F4"/>
        <path d="M12.214 23C15.1068 23 17.5353 22.0666 19.3092 20.4567L15.9282 17.8899C15.0235 18.5083 13.8092 18.9399 12.214 18.9399C9.38069 18.9399 6.97596 17.1083 6.11874 14.5766L5.99309 14.5871L2.68583 17.0954L2.64258 17.2132C4.40446 20.6433 8.0235 23 12.214 23Z" fill="#34A853"/>
        <path d="M6.12046 14.5766C5.89428 13.9233 5.76337 13.2233 5.76337 12.5C5.76337 11.7766 5.89428 11.0766 6.10856 10.4233L6.10257 10.2841L2.75386 7.7355L2.64429 7.78658C1.91814 9.20993 1.50146 10.8083 1.50146 12.5C1.50146 14.1916 1.91814 15.7899 2.64429 17.2132L6.12046 14.5766Z" fill="#FBBC05"/>
        <path d="M12.2141 6.05997C14.2259 6.05997 15.583 6.91163 16.3569 7.62335L19.3807 4.73C17.5236 3.03834 15.1069 2 12.2141 2C8.02353 2 4.40447 4.35665 2.64258 7.78662L6.10686 10.4233C6.97598 7.89166 9.38073 6.05997 12.2141 6.05997Z" fill="#EB4335"/>
      </svg>
      ```

### 2. プロバイダーの認証情報を準備

GoogleはSerpApiが提供するAPIを使用しているため、SerpApiのAPIキーが必要です。一方で、`wikipedia`のようなツールでは認証情報フィールドを記入する必要はありません。参考例：api/core/tools/provider/builtin/wikipedia/wikipedia.yaml

```yaml
identity:
  author: Dify
  name: wikipedia
  label:
    en_US: Wikipedia
    zh_Hans: 维基百科
    ja_JP: Wikipedia
    pt_BR: Wikipedia
  description:
    en_US: Wikipedia is a free online encyclopedia, created and edited by volunteers around the world.
    zh_Hans: 维基百科是一个由全世界的志愿者创建和编辑的免费在线百科全书。
    ja_JP: Wikipediaは、世界中のボランティアによって作成、編集されている無料のオンライン百科事典です。
    pt_BR: A Wikipédia é uma enciclopédia online gratuita, criada e editada por voluntários ao redor do mundo.
  icon: icon.svg
credentials_for_provider:
```

認証情報フィールドを設定すると以下のようになります：

```yaml
identity:
  author: Dify
  name: google
  label:
    en_US: Google
    zh_Hans: Google
    ja_JP: Google
    pt_BR: Google
  description:
    en_US: Google
    zh_Hans: Google
    ja_JP: Google
    pt_BR: Google
  icon: icon.svg
credentials_for_provider: # 認証情報フィールド
  serpapi_api_key: # 認証情報フィールド名
    type: secret-input # 認証情報フィールドタイプ
    required: true # 必須かどうか
    label: # 認証情報フィールドラベル
      en_US: SerpApi API key # 英語ラベル
      zh_Hans: SerpApi API key # 中国語ラベル
      ja_JP: SerpApi API key # 日本語ラベル
      pt_BR: chave de API SerpApi # プルトガル語ラベル
    placeholder: # 認証情報フィールドプレースホルダー
      en_US: Please input your SerpApi API key # 英語プレースホルダー
      zh_Hans: 请输入你的 SerpApi API key # 中国語プレースホルダー
      ja_JP: SerpApi API keyを入力してください # 日本語プレースホルダー
      pt_BR: Por favor, insira sua chave de API SerpApi # プルトガル語プレースホルダー
    help: # 認証情報フィールドヘルプテキスト
      en_US: Get your SerpApi API key from SerpApi # 英語ヘルプテキスト
      zh_Hans: 从 SerpApi 获取你的 SerpApi API key # 中国語ヘルプテキスト
      ja_JP: SerpApiからSerpApi APIキーを取得する # 日本語ヘルプテキスト
      pt_BR: Obtenha sua chave de API SerpApi da SerpApi # プルトガル語ヘルプテキスト
    url: https://serpapi.com/manage-api-key # 認証情報フィールドヘルプリンク

```

* `type`：認証情報フィールドタイプ、現在は`secret-input`、`text-input`、`select`の3種類をサポートしており、それぞれパスワード入力、テキスト入力、選択ボックスに対応します。`secret-input`の場合、前端で入力内容が非表示となり、後端で入力内容が暗号化されます。

### 3. ツールのyamlを準備

一つのプロバイダーには複数のツールがあり、それぞれのツールには基本情報、パラメーター、出力などを記述したyamlファイルが必要です。

GoogleSearchを例にとって、`google`モジュール内に`tools`モジュールを作成し、その中に`tools/google_search.yaml`を作成します。内容は以下の通りです。

```yaml
identity: # ツールの基本情報
  name: google_search # ツール名、唯一無二で、他のツールと重複してはいけません
  author: Dify # 著者
  label: # ラベル、前端表示用
    en_US: GoogleSearch # 英語ラベル
    zh_Hans: 谷歌搜索 # 中国語ラベル
    ja_JP: Google検索 # 日本語ラベル
    pt_BR: Pesquisa Google # プルトガル語ラベル
description: # 説明、前端表示用
  human: # 前端表示用の紹介文、複数言語対応
    en_US: A tool for performing a Google SERP search and extracting snippets and webpages.Input should be a search query.
    zh_Hans: 一个用于执行 Google SERP 搜索并提取片段和网页的工具。输入应该是一个搜索查询。
    ja_JP: Google SERP 検索を実行し、スニペットと Web ページを抽出するためのツール。入力は検索クエリである必要があります。
    pt_BR: Uma ferramenta para realizar pesquisas no Google SERP e extrair snippets e páginas da web. A entrada deve ser uma consulta de pesquisa.
  llm: A tool for performing a Google SERP search and extracting snippets and webpages.Input should be a search query. # LLMに渡す紹介文。LLMがこのツールをよりよく理解して使用できるように、ここにはできるだけ詳細な情報を書いておくことをお勧めします。
parameters: # パラメーターリスト
  - name: query # パラメーター名
    type: string # パラメータータイプ
    required: true # 必須かどうか
    label: # パラメーターラベル
      en_US: Query string # 英語ラベル
      zh_Hans: 查询语句 # 中国語ラベル
      ja_JP: クエリステートメント # 日本語ラベル
      pt_BR: Declaração de consulta # プルトガル語ラベル
    human_description: # 前端表示用の紹介文、複数言語対応
      en_US: used for searching
      zh_Hans: 用于搜索网页内容
      ja_JP: ネットの検索に使用する
      pt_BR: usado para pesquisar
    llm_description: key words for searching # LLMに渡す紹介文。同上、LLMがこのパラメーターをよりよく理解できるように、できるだけ詳細な情報を書いておくことをお勧めします。
    form: llm # フォームタイプ。llmはこのパラメーターがエージェントによって推論されるべきであることを示します。前端はこのパラメーターを表示しません。
  - name: result_type
    type: select # パラメータータイプ
    required: true
    options: # 選択ボックスオプション
      - value: text
        label:
          en_US: text
          zh_Hans: 文本
          ja_JP: テキスト
          pt_BR: texto
      - value: link
        label:
          en_US: link
          zh_Hans: 链接
          ja_JP: リンク
          pt_BR: link
    default: link
    label:
      en_US: Result type
      zh_Hans: 结果类型
      ja_JP: 結果タイプ
      pt_BR: tipo de resultado
    human_description:
      en_US: used for selecting the result type, text or link
      zh_Hans: 用于选择结果类型，使用文本还是链接进行展示
      ja_JP: 結果の種類、テキスト、リンクを選択するために使用されます
      pt_BR: usado para selecionar o tipo de resultado, texto ou link
    form: form # フォームタイプ。formはこのパラメーターが対話開始前にユーザーによって前端で入力されるべきであることを示します。

```

* `identity` フィールドは必須です。名前、著者、ラベル、説明などの基本情報が含まれています。
* `parameters` パラメーターリスト
  * `name` パラメーター名、唯一無二で、他のパラメーターと重複してはいけません。
  * `type` パラメータータイプ。現在は`string`、`number`、`boolean`、`select`の4種類をサポートしており、文字列、数値、ブール値、選択ボックスに対応します。
  * `required` 必須かどうか
    * `llm`モードでは、パラメーターが必須の場合、エージェントは必ずこのパラメーターを推論する必要があります。
    * `form`モードでは、パラメーターが必須の場合、ユーザーは対話開始前に前端でこのパラメーターを入力する必要があります。
  * `options` パラメーターオプション
    * `llm`モードでは、DifyはすべてのオプションをLLMに渡し、LLMはこれらのオプションを基に推論します。
    * `form`モードでは、`type`が`select`の場合、前端にこれらのオプションが表示されます。
  * `default` デフォルト値
  * `label` パラメーターラベル、前端表示用
  * `human_description` 前端表示用の紹介文、複数言語対応
  * `llm_description` LLMに渡す紹介文。LLMがこのパラメーターをよりよく理解できるように、できるだけ詳細な情報を書いておくことをお勧めします。
  * `form` フォームタイプ。現在は`llm`、`form`の2種類をサポートしており、それぞれエージェントによる推論と前端入力に対応します。

### 4. ツールコードを準備

ツールの設定が完了したら、次にツールのロジックを実装するためのコードを作成します。

`google/tools`モジュール内に`google_search.py`を作成し、以下の内容を記述します。

```python
from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage

from typing import Any, Dict, List, Union

class GoogleSearchTool(BuiltinTool):
    def _invoke(self, 
                user_id: str,
               tool_Parameters: Dict[str, Any], 
        ) -> Union[ToolInvokeMessage, List[ToolInvokeMessage]]:
        """
            invoke tools
        """
        query = tool_Parameters['query']
        result_type = tool_Parameters['result_type']
        api_key = self.runtime.credentials['serpapi_api_key']
        # TODO: search with serpapi
        result = SerpAPI(api_key).run(query, result_type=result_type)

        if result_type == 'text':
            return self.create_text_message(text=result)
        return self.create_link_message(link=result)
```

#### パラメーター

ツールの全体のロジックは`_invoke`メソッド内にあります。このメソッドは`user_id`と`tool_Parameters`の2つのパラメーターを受け取ります。これらはそれぞれユーザーIDとツールパラメーターを表します。

#### 返却データ

ツールの返却時に、1つまたは複数のメッセージを返すことができます。ここでは、1つのメッセージを返す例を示しており、`create_text_message`と`create_link_message`を使用してテキストメッセージまたはリンクメッセージを作成しています。

### 5. プロバイダーコードを準備

最後に、プロバイダーモジュール内にプロバイダークラスを作成し、認証情報の検証ロジックを実装します。認証情報の検証に失敗した場合、`ToolProviderCredentialValidationError`例外が投げられます。

`google`モジュール内に`google.py`を作成し、以下の内容を記述します。

```python
from core.tools.entities.tool_entities import ToolInvokeMessage, ToolProviderType
from core.tools.tool.tool import Tool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController
from core.tools.errors import ToolProviderCredentialValidationError

from core.tools.provider.builtin.google.tools.google_search import GoogleSearchTool

from typing import Any, Dict

class GoogleProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: Dict[str, Any]) -> None:
        try:
            # 1. この場所でGoogleSearchTool()をインスタンス化し、GoogleSearchToolのyaml設定を自動的に読み込みますが、この時点では認証情報が内部にありません。
            # 2. その後、fork_tool_runtimeメソッドを使用して、現在の認証情報をGoogleSearchToolに渡します。
            # 3. 最後にinvokeします。パラメーターはGoogleSearchToolのyamlに記載されたパラメーター規則に従って渡します。
            GoogleSearchTool().fork_tool_runtime(
                meta={
                    "credentials": credentials,
                }
            ).invoke(
                user_id='',
                tool_parameters={
                    "query": "test",
                    "result_type": "link"
                },
            )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
```

### 完成

上記のステップが完了すると、このツールがフロントエンドに表示され、エージェントでこのツールを使用することができます。

もちろん、google検索は資格情報を必要とするため、使用前にフロントエンドで資格情報を設定する必要があります。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/tools/c99fed3e1bbe5d724810fd6118012071.png)
