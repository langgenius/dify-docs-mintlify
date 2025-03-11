# よくある質問

## プラグインのインストール時にアップロードが失敗する場合の対処方法は？

**エラー詳細**：`PluginDaemonBadRequestError: plugin_unique_identifier is not valid` というエラーメッセージが表示されます。

**解決方法**：プラグインプロジェクトの `manifest.yaml` ファイルと `/provider` パス配下の `.yaml` ファイルの `author` フィールドを GitHub ID に変更してください。

プラグインのパッケージングコマンドを再実行し、新しいプラグインパッケージをインストールしてください。

## プラグインインストール時のエラーの対処方法

**問題**: `plugin verification has been enabled, and the plugin you want to install has a bad signature` というエラーメッセージが表示された場合、どのように対処すればよいですか？

**解決方法**: `/docker/.env` 設定ファイルの末尾に以下の行を追加してください：  
`FORCE_VERIFYING_SIGNATURE=false`. 

Dify サービスを再起動するには、以下のコマンドを実行してください：

```bash
cd docker
docker compose down
docker compose up -d
```

このフィールドを追加すると、Dify プラットフォームは Dify Marketplace にリストされていない（つまり、未検証の）すべてのプラグインのインストールを許可します。

ただし、安全性を考慮して、未知のソースから提供されるプラグインは、テスト環境またはサンドボックス環境でまずインストールし、安全性を確認した後、本番環境にデプロイしてください。
