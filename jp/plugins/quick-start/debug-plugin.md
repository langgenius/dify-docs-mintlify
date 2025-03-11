## プラグインのデバッグ

プラグインの開発が完了したら、次は正常に動作するかどうかをテストしましょう。Difyはリモートデバッグ機能を提供しており、「プラグイン管理」ページでデバッグキーとリモートサーバーアドレスを取得できます。

![](https://assets-docs.dify.ai/2024/11/1cf15bc59ea10eb67513c8bdca557111.png)

プラグインのプロジェクトに戻り、`.env.example`ファイルをコピーして`.env`にリネームします。そして、取得したリモートサーバーアドレスやデバッグキーなどの情報を入力してください。

`.env`ファイル

```bash
INSTALL_METHOD=remote
REMOTE_INSTALL_HOST=remote-url
REMOTE_INSTALL_PORT=5003
REMOTE_INSTALL_KEY=****-****-****-****-****
```

`python -m main`コマンドを実行してプラグインを起動します。プラグインページで、Workspaceにインストールされたことを確認できます。他のチームメンバーもこのプラグインを利用可能です。

![](https://assets-docs.dify.ai/2024/12/ec26e5afc57bbfeb807719638f603807.png)