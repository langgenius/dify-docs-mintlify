# 一般的な標準仕様

本文では、プラグイン開発における共通構造について簡単に説明します。

### **パス仕様**

マニフェストまたは任意のyamlファイルでファイルパスを指定する場合、ファイルタイプに基づいて以下の2つのルールに従ってください：

* 画像や動画などのマルチメディアファイル（例：プラグインの`icon`）の場合、プラグインのルートディレクトリの下の`_assets`フォルダに配置します。
* `.py`や`.yaml`などの通常のテキストファイルの場合、プラグインプロジェクト内の絶対パスを使用します。

### **共通構造**

プラグインを定義する際、ツール、モデル、インターフェース間で共有できるデータ構造があります。以下がこれらの共有構造です。

#### **I18nObject**

`I18nObject`は、IETF BCP 47標準に準拠した国際化構造で、現在4つの言語をサポートしています：

* en\_US
* zh\_Hans
* ja\_Jp
* pt\_BR

#### **ProviderConfig**

`ProviderConfig`は、`Tool`と`Endpoint`の両方に適用可能な共通プロバイダーフォーム構造です。

* `name` (string): フォーム項目名
* `label` (I18nObject, 必須): IETF BCP 47に準拠
* `type` (provider\_config\_type, 必須): フォームタイプ
* `scope` (provider\_config\_scope): オプション範囲、`type`により異なる
* `required` (bool): 空にできない
* `default` (any): デフォルト値、基本タイプ`float` `int` `string`のみサポート
* `options` (list\[provider\_config\_option]): オプション、typeが`select`の場合のみ使用
* `helper` (object): ヘルプドキュメントリンクラベル、IETF BCP 47に準拠
* `url` (string): ヘルプドキュメントリンク
* `placeholder` (object): IETF BCP 47に準拠

#### ProviderConfigOption(object)

* `value`(string, 必須)：値
* `label`(object, 必須)：[IETF BCP 47](https://tools.ietf.org/html/bcp47)に準拠

#### ProviderConfigType(string)

* `secret-input` (string)：設定情報が暗号化される
* `text-input`(string)：プレーンテキスト
* `select`(string)：ドロップダウンボックス
* `boolean`(bool)：スイッチ
* `model-selector`(object)：プロバイダー名、モデル名、モデルパラメータなどを含むモデル設定情報
* `app-selector`(object)：アプリID
* `tool-selector`(object)：ツールプロバイダー、名前、パラメータなどを含むツール設定情報
* `dataset-selector`(string)：TBD

#### ProviderConfigScope(string)

* `type`が`model-selector`の場合
  * `all`
  * `llm`
  * `text-embedding`
  * `rerank`
  * `tts`
  * `speech2text`
  * `moderation`
  * `vision`
* `type`が`app-selector`の場合
  * `all`
  * `chat`
  * `workflow`
  * `completion`
* `type`が`tool-selector`の場合
  * `all`
  * `plugin`
  * `api`
  * `workflow`

#### ModelConfig

* `provider` (string): プラグインIDを含むプロバイダー名、形式は`langgenius/openai/openai`
* `model` (string): 具体的なモデル名
* `model_type` (enum): モデルタイプの列挙、このドキュメントを参照

#### NodeResponse

* `inputs` (dict): ノードに最終的に入力される変数
* `outputs` (dict): ノード出力結果
* `process_data` (dict): ノード実行中に生成されたデータ

#### ToolSelector

* `provider_id` (string): ツールプロバイダー名
* `tool_name` (string): ツール名
* `tool_description` (string): ツールの説明
* `tool_configuration` (dict\[str, Any]): ツール設定情報
* `tool_parameters` (dict\[str, dict]): LLM推論が必要なパラメータ
  * `name` (string): パラメータ名
  * `type` (string): パラメータタイプ
  * `required` (bool): 必須かどうか
  * `description` (string): パラメータの説明
  * `default` (any): デフォルト値
  * `options` (list\[string]): 利用可能なオプション
