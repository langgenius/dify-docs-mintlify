# 新しいプロバイダーの追加

### モデル設定方法

プロバイダーは三つのモデル設定方法に対応しています：

**事前定義モデル（predefined-model）**

ユーザーは統一されたプロバイダーのクレデンシャルを設定するだけで、プロバイダーの事前定義モデルを使用できます。

**カスタマイズ可能モデル（customizable-model）**

ユーザーは各モデルのクレデンシャル設定を追加する必要があります。例えば、XinferenceはLLMとテキスト埋め込みの両方に対応していますが、各モデルには一意の**モデルUID**があり、両方を同時に接続したい場合は、それぞれのモデルに対して**モデルUID**を設定する必要があります。

**リモートから取得（fetch-from-remote）**

`predefined-model`の設定方法と一致しており、統一されたプロバイダーのクレデンシャルを設定するだけで、モデルはクレデンシャル情報を通じてプロバイダーから取得されます。

例えばOpenAIの場合、gpt-turbo-3.5を基に複数のモデルを微調整することができ、それらはすべて同じ**APIキー**の下にあります。`fetch-from-remote`として設定すると、開発者は統一された**APIキー**を設定するだけで、Difyランタイムが開発者のすべての微調整モデルを取得してDifyに接続できます。

これら三つの設定方法は**共存可能**であり、例えばプロバイダーが`predefined-model`と`customizable-model`、または`predefined-model`と`fetch-from-remote`をサポートする場合があります。統一されたプロバイダーのクレデンシャルを設定することで、事前定義モデルとリモートから取得したモデルを使用でき、新しいモデルを追加することでカスタマイズ可能なモデルも使用できます。

### 設定説明

**名詞解説**

* `モジュール`: 一つの`モジュール`は一つのPythonパッケージ、または簡単に言えば一つのフォルダーであり、その中に`__init__.py`ファイルと他の`.py`ファイルが含まれます。

**手順**

新しいプロバイダーを追加するには主にいくつかのステップがあります。ここでは簡単に列挙し、具体的な手順は以下で詳しく説明します。

* プロバイダーのYAMLファイルを作成し、[プロバイダースキーマ](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/docs/en_US/schema.md)に基づいて記述します。
* プロバイダーのコードを作成し、`class`を実装します。
* モデルタイプに応じて、プロバイダーの`モジュール`内に対応するモデルタイプの`モジュール`を作成します。例えば`llm`や`text_embedding`。
* モデルタイプに応じて、対応するモデル`モジュール`内に同名のコードファイルを作成し、例えば`llm.py`、`class`を実装します。
* 事前定義モデルがある場合、モデル名と同名のyamlファイルをモデル`モジュール`内に作成し、[AIモデルエンティティ](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/docs/en_US/schema.md#aimodelentity)に基づいて記述します。
* テストコードを記述し、機能の有用性を確認します。

#### 始めましょう

新しいプロバイダーを追加するには、まずプロバイダーの英語識別子を決めます。例えば`anthropic`、この識別子を使って`model_providers`内に同名の`モジュール`を作成します。

この`モジュール`内で、まずプロバイダーのYAML設定を準備する必要があります。

**プロバイダーYAMLの準備**

ここでは`Anthropic`を例に、プロバイダーの基本情報、対応するモデルタイプ、設定方法、クレデンシャルルールを設定します。

```YAML
provider: anthropic  # プロバイダーの識別子
label:  # プロバイダーの表示名、en_US英語、zh_Hans中国語の二言語を設定できます。zh_Hansが設定されていない場合、en_USがデフォルトで使用されます。
  en_US: Anthropic
icon_small:  # プロバイダーの小アイコン、対応するプロバイダーの実装ディレクトリ内の_assetsディレクトリに保存されます。labelと同じく二言語の設定が可能です。
  en_US: icon_s_en.png
icon_large:  # プロバイダーの大アイコン、対応するプロバイダーの実装ディレクトリ内の_assetsディレクトリに保存されます。labelと同じく二言語の設定が可能です。
  en_US: icon_l_en.png
supported_model_types:  # 対応するモデルタイプ、AnthropicはLLMのみ対応
- llm
configurate_methods:  # 対応する設定方法、Anthropicは事前定義モデルのみ対応
- predefined-model
provider_credential_schema:  # プロバイダーのクレデンシャルルール、Anthropicは事前定義モデルのみ対応するため、統一されたプロバイダーのクレデンシャルルールを定義する必要があります
  credential_form_schemas:  # クレデンシャルフォーム項目リスト
  - variable: anthropic_api_key  # クレデンシャルパラメーターの変数名
    label:  # 表示名
      en_US: API Key
    type: secret-input  # フォームタイプ、ここではsecret-inputは暗号化された情報入力フィールドを意味し、編集時にはマスクされた情報のみが表示されます。
    required: true  # 必須かどうか
    placeholder:  # プレースホルダー情報
      zh_Hans: 在此输入你的 API Key
      en_US: Enter your API Key
  - variable: anthropic_api_url
    label:
      en_US: API URL
    type: text-input  # フォームタイプ、ここではtext-inputはテキスト入力フィールドを意味します
    required: false
    placeholder:
      zh_Hans: 在此输入你的 API URL
      en_US: Enter your API URL
```

カスタマイズ可能なモデルを提供するプロバイダー、例えば`OpenAI`が微調整モデルを提供する場合、[`モデルクレデンシャルスキーマ`](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/docs/en_US/schema.md)を追加する必要があります。以下は`OpenAI`を例にしたものです：

```yaml
model_credential_schema:
  model: # 微調整モデルの名称
    label:
      en_US: Model Name
      zh_Hans: 模型名称
    placeholder:
      en_US: Enter your model name
      zh_Hans: 输入模型名称
  credential_form_schemas:
  - variable: openai_api_key
    label:
      en_US: API Key
    type: secret-input
    required: true
    placeholder:
      zh_Hans: 在此输入你的 API Key
      en_US: Enter your API Key
  - variable: openai_organization
    label:
        zh_Hans: 组织 ID
        en_US: Organization
    type: text-input
    required: false
    placeholder:
      zh_Hans: 在此输入你的组织 ID
      en_US: Enter your Organization ID
  - variable: openai_api_base
    label:
      zh_Hans: API Base
      en_US: API Base
    type: text-input
    required: false
    placeholder:
      zh_Hans: 在此输入你的 API Base
      en_US: Enter your API Base
```

`model_providers`ディレクトリ内の他のプロバイダーディレクトリの[YAML設定情報](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/docs/en_US/schema.md)も参考にできます。

**プロバイダーコードの実装**

`model_providers`内に同名のPythonファイルを作成します。例えば`anthropic.py`を作成し、`class`を実装、`__base.provider.Provider`基クラスを継承します。例えば`AnthropicProvider`。

**カスタマイズ可能モデルプロバイダー**

プロバイダーがXinferenceなどのカスタマイズ可能モデルプロバイダーの場合、このステップをスキップし、空の`XinferenceProvider`クラスを作成し、空の`validate_provider_credentials`メソッドを実装するだけで済みます。このメソッドは実際には使用されず、抽象クラスのインスタンス化を避けるためにのみ存在します。

```python
class XinferenceProvider(Provider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        pass
```

**事前定義モデルプロバイダー**

プロバイダーは`__base.model_provider.ModelProvider`基クラスを継承し、`validate_provider_credentials`プロバイダーの統一クレデンシャル検証メソッドを実装するだけで済みます。[AnthropicProvider](https://github.com/langgenius/dify/blob/main/api/core/model_runtime/model_providers/anthropic/anthropic.py)を参考にできます。

```python
def validate_provider_credentials(self, credentials: dict) -> None:
    """
    Validate provider credentials
    You can choose any validate_credentials method of model type or implement validate method by yourself,
    such as: get model list api

    if validate failed, raise exception

    :param credentials: provider credentials, credentials form defined in `provider_credential_schema`.
    """
```

もちろん、`validate_provider_credentials`の実装を先に予約し、モデルクレデンシャル検証メソッドの実装後に直接再利用することもできます。

**モデルの追加**

[**事前定義モデルの追加**](https://docs.dify.ai/v/ja-jp/guides/model-configuration/predefined-model)**👈🏻**

事前定義モデルの場合、単純にyamlを定義し、呼び出しコードを実装することで接続できます。

[**カスタマイズ可能モデルの追加**](https://docs.dify.ai/v/ja-jp/guides/model-configuration/customizable-model) **👈🏻**

カスタマイズ可能モデルの場合、呼び出しコードを実装するだけで接続できますが、処理するパラメーターはさらに複雑になる可能性があります。

***

#### テスト

プロバイダー/モデルの有用性を確保するため、実装した各メソッドには`tests`ディレクトリ内で対応する統合テストコードを記述する必要があります。

再び`Anthropic`を例にします。

テストコードを記述する前に、`.env.example`にテストプロバイダーが必要とするクレデンシャル環境変数を追加します。例えば：`ANTHROPIC_API_KEY`。

実行前に`.env.example`をコピーして`.env`にし、実行します。

**テストコードの記述**

`tests`ディレクトリ内にプロバイダーと同名の`モジュール`を作成します：`anthropic`。このモジュール内に`test_provider.py`および対応するモデルタイプのテストpyファイルを作成します。以下のようになります：

```shell
.
├── __init__.py
├── anthropic
│   ├── __init__.py
│   ├── test_llm.py       # LLMテスト
│   └── test_provider.py  # プロバイダーテスト
```

上記で実装したコードの様々な状況に対してテストコードを記述し、テストを通過した後にコードを提出します。
