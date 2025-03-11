# モデル設計ルール

* モデルプロバイダーのルールは、[Provider](model-designing-rules.md#provider) エンティティに基づいています。
* モデルルールは、[AIModelEntity](model-designing-rules.md#aimodelentity) エンティティに基づいています。

> 以下のすべてのエンティティは `Pydantic BaseModel` をベースにしており、`entities` モジュール内で対応するエンティティを見つけることができます。

### Provider（プロバイダ）

* `provider` (string) プロバイダー識別子。例：`openai`
* `label` (object) プロバイダーの表示名。多言語対応で、英語（`en_US`）と中国語（`zh_Hans`）の2言語を設定できます。
  * `zh_Hans` (string) \[optional] 中国語のラベル名。`zh_Hans` が設定されていない場合は、デフォルトで `en_US` が使用されます。
  * `en_US` (string) 英語のラベル名
* `description` (object) \[optional] プロバイダーの説明。多言語対応。
  * `zh_Hans` (string) \[optional] 中国語の説明
  * `en_US` (string) 英語の説明
* `icon_small` (string) \[optional] プロバイダーの小さなアイコン。対応するプロバイダーの実装ディレクトリ下の `_assets` ディレクトリに保存されます。英語と中国語の扱い方は `label` と同様です。
  * `zh_Hans` (string) \[optional] 中国語のアイコン
  * `en_US` (string) 英語のアイコン
* `icon_large` (string) \[optional] プロバイダーの大きなアイコン。対応するプロバイダーの実装ディレクトリ下の `_assets` ディレクトリに保存されます。英語と中国語の扱い方は `label` と同様です。
  * `zh_Hans` (string) \[optional] 中国語のアイコン
  * `en_US` (string) 英語のアイコン
* `background` (string) \[optional] 背景色のカラーコード。例：#FFFFFF。値が設定されていない場合は、フロントエンドのデフォルト色が使用されます。
* `help` (object) \[optional] ヘルプ情報
  * `title` (object) ヘルプタイトル。多言語対応。
    * `zh_Hans` (string) \[optional] 中国語のタイトル
    * `en_US` (string) 英語のタイトル
  * `url` (object) ヘルプリンク。多言語対応。
    * `zh_Hans` (string) \[optional] 中国語のリンク
    * `en_US` (string) 英語のリンク
* `supported_model_types` (array\[[ModelType](model-designing-rules.md#modeltype)]) サポートされているモデルタイプ
* `configurate_methods` (array\[[ConfigurateMethod](model-designing-rules.md#configuratemethod)]) 設定方法
* `provider_credential_schema` (\[[ProviderCredentialSchema](model-designing-rules.md#providercredentialschema)]) プロバイダーの認証情報スキーマ（プロバイダーの資格情報仕様）
* `model_credential_schema` (\[[ModelCredentialSchema](model-designing-rules.md#modelcredentialschema)]) モデルの認証情報スキーマ（モデルの資格情報仕様）

### AIModelEntity（AIモデルエンティティ）

* `model` (string) モデル識別子。例：`gpt-3.5-turbo`
* `label` (object) \[optional] モデルの表示名。多言語対応で、英語（`en_US`）と中国語（`zh_Hans`）の2言語を設定できます。
  * `zh_Hans` (string) \[optional] 中国語のラベル名
  * `en_US` (string) 英語のラベル名
* `model_type` (\[ModelType]\(#ModelType)) モデルタイプ
* `features` (array\[\[ModelFeature]\(#ModelFeature)]) \[optional] サポートされている機能リスト
* `model_properties` (object) モデルのプロパティ
  * `mode` (\[LLMMode]\(#LLMMode)) モード（モデルタイプ `llm` で利用可能）
  * `context_size` (int) コンテキストサイズ（モデルタイプ `llm`、`text-embedding` で利用可能）
  * `max_chunks` (int) 最大チャンク数（モデルタイプ `text-embedding`、`moderation` で利用可能）
  * `file_upload_limit` (int) ファイルの最大アップロード制限（単位：MB）。（モデルタイプ `speech2text` で利用可能）
  * `supported_file_extensions` (string) サポートされているファイル拡張子形式。例：mp3、mp4（モデルタイプ `speech2text` の場合）
  * `default_voice` (string) デフォルトのボイス。必須：alloy,echo,fable,onyx,nova,shimmer（モデルタイプ `tts` で利用可能）
  * `voices` (list) 選択可能なボイスリスト。
    * `mode` (string) ボイスモデル。（モデルタイプ `tts` で利用可能）
    * `name` (string) ボイスモデルの表示名。（モデルタイプ `tts` で利用可能）
    * `language` (string) ボイスモデルがサポートする言語。（モデルタイプ `tts` で利用可能）
  * `word_limit` (int) 1回の変換における文字数制限。デフォルトでは段落ごとに区切られます。（モデルタイプ `tts` で利用可能）
  * `audio_type` (string) サポートされているオーディオファイルの拡張子形式。例：mp3、wav（モデルタイプ `tts` で利用可能）
  * `max_workers` (int) テキストからオーディオへの変換をサポートする同時実行タスク数。（モデルタイプ `tts` で利用可能）
  * `max_characters_per_chunk` (int) 1チャンクあたりの最大文字数（モデルタイプ `moderation` で利用可能）
* `parameter_rules` (array\[[ParameterRule](model-designing-rules.md#parameterrule)]) \[optional] モデル呼び出しパラメータのルール
* `pricing` (\[[PriceConfig](model-designing-rules.md#priceconfig)]) \[optional] 価格情報
* `deprecated` (bool) 非推奨かどうか。非推奨の場合、モデルリストには表示されなくなりますが、すでに設定済みのものは引き続き使用できます。デフォルトは `False` です。

### ModelType（モデルタイプ）

* `llm` テキスト生成モデル
* `text-embedding` テキスト埋め込みモデル
* `rerank` Rerank モデル
* `speech2text` 音声テキスト変換
* `tts` テキスト音声変換
* `moderation` 審査

### ConfigurateMethod（構成方法）

* `predefined-model` 既定モデル

ユーザーは、統一されたプロバイダーの認証情報を設定するだけで、プロバイダーの既定モデルを利用できます。

* `customizable-model` カスタムモデル

ユーザーは、各モデルの認証情報設定を個別に追加する必要があります。

* `fetch-from-remote` リモートから取得

`predefined-model` の設定方法と同様に、統一されたプロバイダーの認証情報を設定するだけで済みます。モデルは認証情報を通じてプロバイダーから取得されます。

### ModelFeature（モデル機能）

* `agent-thought` エージェントの推論。通常、70B を超えるモデルには思考連鎖能力があります。
* `vision` ビジョン、つまり画像理解。
* `tool-call` ツール呼び出し
* `multi-tool-call` 複数ツール呼び出し
* `stream-tool-call` ストリームツール呼び出し

### FetchFrom（入手先）

* `predefined-model` 既定モデル
* `fetch-from-remote` リモートモデル

### LLMMode（LLMモード）

* `completion` テキスト補完
* `chat` 対話

### ParameterRule（パラメータールール）

* `name` (string) モデルを呼び出す際の実際のパラメータ名
* `use_template` (string) \[optional] テンプレートを使用

デフォルトでは、5つの変数設定テンプレートが用意されています。

* `temperature`
* `top_p`
* `frequency_penalty`
* `presence_penalty`
* `max_tokens`

`use_template` でテンプレート変数名を直接設定すると、`entities.defaults.PARAMETER_RULE_TEMPLATE` のデフォルト設定が使用され、`name` と `use_template` 以外のすべてのパラメータを設定する必要はありません。追加の設定パラメータを設定した場合、デフォルト設定が上書きされます。`openai/llm/gpt-3.5-turbo.yaml` を参照してください。

* `label` (object) \[optional] ラベル。多言語対応。
  * `zh_Hans` (string) \[optional] 中国語のラベル名
  * `en_US` (string) 英語のラベル名
* `type` (string) \[optional] パラメータのタイプ
  * `int` 整数
  * `float` 浮動小数点数
  * `string` 文字列
  * `boolean` ブール型
* `help` (string) \[optional] ヘルプ情報
  * `zh_Hans` (string) \[optional] 中国語のヘルプ情報
  * `en_US` (string) 英語のヘルプ情報
* `required` (bool) 必須かどうか。デフォルトは `False` です。
* `default` (int/float/string/bool) \[optional] デフォルト値
* `min` (int/float) \[optional] 最小値。数値型のみ適用。
* `max` (int/float) \[optional] 最大値。数値型のみ適用。
* `precision` (int) \[optional] 精度。小数点以下の桁数。数値型のみ適用。
* `options` (array\[string]) \[optional] ドロップダウンの選択肢。`type` が `string` の場合にのみ適用。設定しない、または null の場合は選択肢を制限しません。

### PriceConfig（価格設定）

* `input` (float) 入力単価。つまり、Prompt の単価。
* `output` (float) 出力単価。つまり、返される内容の単価。
* `unit` (float) 価格単位。例：1M トークン単位で価格設定する場合、単価に対応するトークン数は `0.000001` になります。
* `currency` (string) 通貨単位

### ProviderCredentialSchema（プロバイダー資格情報スキーマ）

* `credential_form_schemas` (array\[[CredentialFormSchema](model-designing-rules.md#credentialformschema)]) 資格情報フォームの仕様

### ModelCredentialSchema（モデル認証情報スキーマ）

* `model` (object) モデル識別子。変数名はデフォルトで `model` です。
  * `label` (object) モデルフォーム項目の表示名
    * `en_US` (string) 英語
    * `zh_Hans` (string) \[optional] 中国語
  * `placeholder` (object) モデルのプレースホルダー
    * `en_US` (string) 英語
    * `zh_Hans` (string) \[optional] 中国語
* `credential_form_schemas` (array\[[CredentialFormSchema](model-designing-rules.md#credentialformschema)]) 資格情報フォームの仕様

### CredentialFormSchema（資格情報フォームスキーマ）

* `variable` (string) フォーム項目の変数名
* `label` (object) フォーム項目のラベル名
  * `en_US` (string) 英語
  * `zh_Hans` (string) \[optional] 中国語
* `type` (\[FormType]\(#FormType)) フォーム項目のタイプ
* `required` (bool) 必須かどうか
* `default` (string) デフォルト値
* `options` (array\[[FormOption](model-designing-rules.md#formoption)]) フォーム項目が `select` または `radio` の場合の専用属性。ドロップダウンの内容を定義します。
* `placeholder` (object) フォーム項目が `text-input` の場合の専用属性。フォーム項目のプレースホルダー。
  * `en_US` (string) 英語
  * `zh_Hans` (string) \[optional] 中国語
* `max_length` (int) フォーム項目が `text-input` の場合の専用属性。入力の最大長を定義します。0 は制限なし。
* `show_on` (array\[[FormShowOnObject](model-designing-rules.md#formshowonobject)]) 他のフォーム項目の値が条件を満たす場合に表示します。空の場合は常に表示します。

#### FormType（フォームタイプ）

* `text-input` テキスト入力コンポーネント
* `secret-input` パスワード入力コンポーネント
* `select` 単一選択ドロップダウン
* `radio` ラジオコンポーネント
* `switch` スイッチコンポーネント。`true` と `false` のみをサポート。

#### FormOption（フォームオプション）

* `label` (object) ラベル
  * `en_US` (string) 英語
  * `zh_Hans` (string) \[optional] 中国語
* `value` (string) ドロップダウンの選択肢の値
* `show_on` (array\[[FormShowOnObject](model-designing-rules.md#formshowonobject)]) 他のフォーム項目の値が条件を満たす場合に表示します。空の場合は常に表示します。

#### FormShowOnObject（フォーム表示オブジェクト）

* `variable` (string) 他のフォーム項目の変数名
* `value` (string) 他のフォーム項目の値