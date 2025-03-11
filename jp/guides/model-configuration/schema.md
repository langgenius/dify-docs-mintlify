---
title: 設定ルール
version: 'v1.0'
---

- 供給業者のルールは [Provider](#Provider) エンティティに基づいています。

- モデルのルールは [AIModelEntity](#AIModelEntity) エンティティに基づいています。

> 以下のすべてのエンティティは `Pydantic BaseModel` に基づいており、対応するエンティティは `entities` モジュールで見つけることができます。

### Provider

- `provider` (string) 供給業者の識別子、例：`openai`
- `label` (object) 供給業者の表示名、i18n、`en_US` 英語、`zh_Hans` 中国語の2種類の言語を設定できます
  - `zh_Hans` (string) [optional] 中国語のラベル名、`zh_Hans` が設定されていない場合はデフォルトで `en_US` が使用されます。
  - `en_US` (string) 英語のラベル名
- `description` (object) [optional] 供給業者の説明、i18n
  - `zh_Hans` (string) [optional] 中国語の説明
  - `en_US` (string) 英語の説明
- `icon_small` (string) [optional] 供給業者の小さなアイコン、対応する供給業者の実装ディレクトリ内の `_assets` ディレクトリに保存されています。中国語と英語の方針は `label` と同じです。
  - `zh_Hans` (string) [optional] 中国語のアイコン
  - `en_US` (string) 英語のアイコン
- `icon_large` (string) [optional] 供給業者の大きなアイコン、対応する供給業者の実装ディレクトリ内の `_assets` ディレクトリに保存されています。中国語と英語の方針は `label` と同じです。
  - `zh_Hans` (string) [optional] 中国語のアイコン
  - `en_US` (string) 英語のアイコン
- `background` (string) [optional] 背景色の値、例：#FFFFFF、空白の場合はフロントエンドのデフォルトの色が表示されます。
- `help` (object) [optional] ヘルプ情報
  - `title` (object) ヘルプのタイトル、i18n
    - `zh_Hans` (string) [optional] 中国語のタイトル
    - `en_US` (string) 英語のタイトル
  - `url` (object) ヘルプリンク、i18n
    - `zh_Hans` (string) [optional] 中国語のリンク
    - `en_US` (string) 英語のリンク
- `supported_model_types` (array[[ModelType](#ModelType)]) サポートされるモデルタイプ
- `configurate_methods` (array[[ConfigurateMethod](#ConfigurateMethod)]) 設定方法
- `provider_credential_schema` ([ProviderCredentialSchema](#ProviderCredentialSchema)) 供給業者の資格情報スキーマ
- `model_credential_schema` ([ModelCredentialSchema](#ModelCredentialSchema)) モデルの資格情報スキーマ

### AIModelEntity

- `model` (string) モデルの識別子、例：`gpt-3.5-turbo`
- `label` (object) [optional] モデルの表示名、i18n、`en_US` 英語、`zh_Hans` 中国語の2種類の言語を設定できます
  - `zh_Hans `(string) [optional] 中国語のラベル名
  - `en_US` (string) 英語のラベル名
- `model_type` ([ModelType](#ModelType)) モデルのタイプ
- `features` (array[[ModelFeature](#ModelFeature)]) [optional] サポートされる機能のリスト
- `model_properties` (object) モデルのプロパティ
  - `mode` ([LLMMode](#LLMMode)) モード (モデルタイプ `llm` で使用可能)
  - `context_size` (int) コンテキストサイズ (モデルタイプ `llm` `text-embedding` で使用可能)
  - `max_chunks` (int) 最大チャンク数 (モデルタイプ `text-embedding` `moderation` で使用可能)
  - `file_upload_limit` (int) ファイルの最大アップロード制限、単位：MB。（モデルタイプ `speech2text` で使用可能）
  - `supported_file_extensions` (string) サポートされるファイルの拡張形式、例：mp3,mp4（モデルタイプ `speech2text` で使用可能）
  - `default_voice` (string) デフォルトの音声、必須：alloy,echo,fable,onyx,nova,shimmer（モデルタイプ `tts` で使用可能）
  - `voices` (list)  選択可能な音声のリスト。
    - `mode` (string)  音声モデル。（モデルタイプ `tts` で使用可能）
    - `name` (string)  音声モデルの表示名。（モデルタイプ `tts` で使用可能）
    - `language` (string)  音声モデルのサポート言語。（モデルタイプ `tts` で使用可能）
  - `word_limit` (int)  一度に変換できる単語数の制限、デフォルトでは段落ごとに分割されます（モデルタイプ `tts` で使用可能）
  - `audio_type` (string)  サポートされるオーディオファイルの拡張形式、例：mp3,wav（モデルタイプ `tts` で使用可能）
  - `max_workers` (int)  テキストオーディオ変換の並行タスク数をサポート（モデルタイプ `tts` で使用可能）
  - `max_characters_per_chunk` (int) チャンクあたりの最大文字数（モデルタイプ `moderation` で使用可能）
- `parameter_rules` (array[[ParameterRule](#ParameterRule)]) [optional] モデル呼び出しパラメータのルール
- `pricing` ([PriceConfig](#PriceConfig)) [optional] 価格情報
- `deprecated` (bool) 廃止されていますか。廃止されると、モデルリストは表示されなくなりますが、すでに設定されているモデルは引き続き使用できます。デフォルトは False です。

### ModelType

- `llm` テキスト生成モデル
- `text-embedding` テキスト埋め込みモデル
- `rerank` Rerank モデル
- `speech2text` 音声からテキストへ
- `tts` テキストから音声へ
- `moderation` モデレーション

### ConfigurateMethod

- `predefined-model` 事前定義モデル

  ユーザーは、供給業者ごとに統一された資格情報を設定するだけで、供給業者の事前定義モデルを使用できます。

- `customizable-model` カスタマイズ可能なモデル

  ユーザーは、各モデルの資格情報を設定することができます。

- `fetch-from-remote` リモートから取得

  `predefined-model` の設定方法と同様に、統一されたベンダーの認証情報を設定すれば、モデルは認証情報を通じてベンダーから取得されます。

### ModelFeature

- `agent-thought` エージェントの思考、一般的に70Bを超えると推論能力があります。
- `vision` 視覚、例えば：画像理解。
- `tool-call` ツールの呼び出し
- `multi-tool-call` 複数ツールの呼び出し
- `stream-tool-call` ストリーミングツール呼び出し

### FetchFrom

- `predefined-model` 予め定義されたモデル
- `fetch-from-remote` リモートモデル

### LLMMode

- `completion` テキスト補完
- `chat` チャット

### ParameterRule

- `name` (string) モデル呼び出しの実際のパラメータ名

- `use_template` (string) [optional] テンプレートを使用
  
  デフォルトで5種類の変数内容設定テンプレートが用意されています：

  - `temperature`
  - `top_p`
  - `frequency_penalty`
  - `presence_penalty`
  - `max_tokens`
  
  `use_template` にテンプレート変数名を直接設定することで、`entities.defaults.PARAMETER_RULE_TEMPLATE` に基づくデフォルト設定が使用されます。
  `name` と `use_template` 以外のすべてのパラメータを設定する必要はありません。追加の設定パラメータを設定した場合、デフォルト設定が上書きされます。
  `openai/llm/gpt-3.5-turbo.yaml`を参照してください。

- `label` (object) [optional] ラベル，i18n

  - `zh_Hans`(string) [optional] 中国語ラベル名
  - `en_US` (string) 英語ラベル名

- `type`(string) [optional] パラメータタイプ

  - `int` 整数
  - `float` 浮動小数点
  - `string` 文字列
  - `boolean` ブール型

- `help` (string) [optional] ヘルプ情報

  - `zh_Hans` (string) [optional] 中国語ヘルプ情報
  - `en_US` (string) 英語ヘルプ情報

- `required` (bool) 必須かどうか、デフォルトは False。

- `default`(int/float/string/bool) [optional] デフォルト値

- `min`(int/float) [optional] 最小値、数値型のみ適用

- `max`(int/float) [optional] 最大値、数値型のみ適用

- `precision`(int) [optional] 精度、小数点以下の桁数を保持、数値型のみ適用

- `options` (array[string]) [optional] ドロップダウン選択肢、`type` が `string` の場合にのみ適用、設定しないか null の場合は選択肢に制限はありません。

### PriceConfig

- `input` (float) 入力単価、すなわちプロンプト単価
- `output` (float) 出力単価、すなわち返却内容単価
- `unit` (float) 価格単位、例えば1Mトークン単位で計算する場合、単価に対応する単位トークン数は `0.000001`
- `currency` (string) 通貨単位

### ProviderCredentialSchema

- `credential_form_schemas` (array[[CredentialFormSchema](#CredentialFormSchema)]) 認証情報フォーム規範

### ModelCredentialSchema

- `model` (object) モデル識別子、変数名はデフォルトで `model`
  - `label` (object) モデルフォーム項目の表示名
    - `en_US` (string) 英語
    - `zh_Hans` (string) [optional] 中国語
  - `placeholder` (object) モデルのヒント内容
    - `en_US` (string) 英語
    - `zh_Hans` (string) [optional] 中国語
- `credential_form_schemas` (array[[CredentialFormSchema](#CredentialFormSchema)]) 認証情報フォーム規範

### CredentialFormSchema

- `variable` (string) フォーム項目の変数名
- `label` (object) フォーム項目のラベル
  - `en_US` (string) 英語のラベル
  - `zh_Hans` (string) [optional] 中国語のラベル
- `type` ([FormType](#FormType)) フォーム項目の種類
- `required` (bool) この項目が必須かどうか
- `default` (string) デフォルト値
- `options` (array[[FormOption](#FormOption)]) フォーム項目が `select` または `radio` の場合に使用するドロップダウンの選択肢を定義
- `placeholder` (object) フォーム項目が `text-input` の場合にのみ使用するプロパティ、入力フィールドに表示されるヒント
  - `en_US` (string) 英語のプレースホルダー
  - `zh_Hans` (string) [optional] 中国語のプレースホルダー
- `max_length` (int) フォーム項目が `text-input` の場合に使用するプロパティ、入力可能な最大文字数を定義。0 は制限なしを意味する。
- `show_on` (array[[FormShowOnObject](#FormShowOnObject)]) 他のフォーム項目の値が条件に一致する場合に表示される。空の場合は常に表示される。

### FormType

- `text-input` テキスト入力コンポーネント
- `secret-input` パスワード入力コンポーネント
- `select` 単一選択ドロップダウン
- `radio` ラジオボタンコンポーネント
- `switch` スイッチコンポーネント、`true` と `false` のみをサポート

### FormOption

- `label` (object) ラベル
  - `en_US` (string) 英語のラベル
  - `zh_Hans` (string) [optional] 中国語のラベル
- `value` (string) ドロップダウンの選択肢の値
- `show_on` (array[[FormShowOnObject](#FormShowOnObject)]) 他のフォーム項目の値が条件に一致する場合に表示される。空の場合は常に表示される。

### FormShowOnObject

- `variable` (string) 他のフォーム項目の変数名
- `value` (string) 他のフォーム項目の変数値