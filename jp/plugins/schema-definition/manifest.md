# マニフェスト

**マニフェストファイル** マニフェストファイルとは、**プラグイン**に関する最も基本的な情報を定義するYAML形式のファイルです。プラグイン名、作成者、含まれるツールやモデルなどの情報が含まれます。

このファイルの形式が正しくないと、プラグインの解析とパッケージング処理は失敗します。

### **コード例**

以下は、マニフェストファイルの簡単な例です。各データ要素の意味と機能については、以下で説明します。他のプラグインコードについては、[Githubリポジトリ](https://github.com/langgenius/dify-plugin-sdks/tree/main/python/examples) を参照してください。

```yaml
version: 0.0.1
type: "plugin"
author: "Yeuoly"
name: "neko"
label:
  en_US: "Neko"
created_at: "2024-07-12T08:03:44.658609186Z"
icon: "icon.svg"
resource:
  memory: 1048576
  permission:
    tool:
      enabled: true
    model:
      enabled: true
      llm: true
    endpoint:
      enabled: true
    app:
      enabled: true
    storage: 
      enabled: true
      size: 1048576
plugins:
  endpoints:
    - "provider/neko.yaml"
meta:
  version: 0.0.1
  arch:
    - "amd64"
    - "arm64"
  runner:
    language: "python"
    version: "3.10"
    entrypoint: "main"
```

### 構造

* `version` (version、required): プラグインのバージョン
* `type` (type、required): プラグインの種類。現在は`plugin`のみをサポートしており、将来的には`bundle`をサポート予定
* `author` (string、required): 作成者。マーケットプレイスでは組織名として扱われます
* `label` (label、required): 多言語対応の名前
* `created_at` (RFC3339、required): 作成時間。マーケットプレイスでは現在時刻より後の日時であってはなりません
* `icon` (アセット、required): アイコンのパス
* `resource` (object): 必要なリソース設定
  * `memory` (int64): 最大メモリ使用量。主にSaaS上のAWS Lambdaリソースリクエストに関連し、単位はバイト
  * `permission` (object): 権限設定
    * `tool` (object): ツール呼び出しの権限
      * `enabled` (bool)
    * `model` (object): モデル呼び出しの権限
      * `enabled` (bool)
      * `llm` (bool)
      * `text_embedding` (bool)
      * `rerank` (bool)
      * `tts` (bool)
      * `speech2text` (bool)
      * `moderation` (bool)
    * `node` (object): ノード呼び出しの権限
      * `enabled` (bool)
    * `endpoint` (object): エンドポイント登録の権限
      * `enabled` (bool)
    * `app` (object): アプリ呼び出しの権限
      * `enabled` (bool)
    * `storage` (object): 永続ストレージの権限
      * `enabled` (bool)
      * `size` (int64): 最大許容永続メモリサイズ（バイト単位）
* `plugins` (object、required): プラグインの機能を定義するYAMLファイルのリスト。プラグインパッケージ内の絶対パスで指定
  * 形式：
    * `tools` (list\[string]): 拡張された[ツール](tool.md)プロバイダ
    * `models` (list\[string]): 拡張された[モデル](model/)プロバイダ
    * `endpoints` (list\[string]): 拡張された[エンドポイント](endpoint.md)プロバイダ
    * `agent_strategies` (list\[string]): 拡張されたエージェント戦略プロバイダ
  * 制限：
    * ツールとモデルの両方を同時に拡張することはできません。
    * 少なくとも1つの拡張が必要です。
    * モデルとエンドポイントの両方を同時に拡張することはできません。
    * 現在、拡張タイプごとに1つのプロバイダのみをサポートしています。
* `meta` (object): メタ情報
  * `version` (version、required): マニフェスト形式のバージョン。初期バージョンは`0.0.1`
  * `arch` (list\[string]、required): サポートされるアーキテクチャ。現在は`amd64`と`arm64`のみ
  * `runner` (object、required): ランタイム設定
    * `language` (string): 現在はPythonのみをサポート
    * `version` (string): 言語バージョン。現在は`3.12`のみをサポート
    * `entrypoint` (string): プログラムのエントリポイント。Pythonの場合は`main`である必要があります。