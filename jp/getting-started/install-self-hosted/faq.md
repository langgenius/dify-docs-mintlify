# よくある質問

### 1. パスワードリセットメールが長時間届かない場合はどうしたらいいですか？

`.env`ファイルに`Mail`パラメータを設定する必要があることをご確認ください。メール設定に関する詳細は、「[環境変数の説明：メール関連の設定](https://docs.dify.ai/v/ja-jp/getting-started/install-self-hosted/environments#mru)」セクションをご参照ください。

設定の変更後は、以下のコマンドを実行して、サービスをリスタートさせてください。

```javascript
docker compose down
docker compose up -d
```

それでもまだメールが届かない場合は、メールサービスが正常に動作しているか、またメールがスパムフィルターに捕まっていないかをご確認ください。

### 2. ワークフローが複雑すぎてノードの上限を超えた場合、どう対処しますか？

コミュニティ版では、`web/app/components/workflow/constants.ts`で手動で `MAX_TREE_DEPTH` の単一ブランチの深さの上限を調整できます。私たちのデフォルト値は50ですが、自分で拡張した場合、あまりにも深いブランチはパフォーマンスに影響を与える可能性があることに注意してください。

### 3. 各ワークフローノードのランタイムを指定するには？

`.env` ファイル内の `TEXT_GENERATION_TIMEOUT_MS` 変数を変更することで、各ノードのランタイムを調整することができます。これにより、特定のプロセスがタイムアウトすることによるアプリケーション全体のサービス停止を防ぐことができます。

### 4. 管理者アカウントのパスワードをリセットする方法

Docker Composeを使ってデプロイしている場合、Docker Composeの実行中に以下のコマンドでパスワードをリセットすることができます：

```
docker exec -it docker-api-1 flask reset-password
```

メールアドレスと新しいパスワードを入力するプロンプトが表示されます。例えば：

```
dify@my-pc:~/hello/dify/docker$ docker compose up -d
[+] Running 9/9
 ✔ Container docker-web-1         Started                                                              0.1s 
 ✔ Container docker-sandbox-1     Started                                                              0.1s 
 ✔ Container docker-db-1          Started                                                              0.1s 
 ✔ Container docker-redis-1       Started                                                              0.1s 
 ✔ Container docker-weaviate-1    Started                                                              0.1s 
 ✔ Container docker-ssrf_proxy-1  Started                                                              0.1s 
 ✔ Container docker-api-1         Started                                                              0.1s 
 ✔ Container docker-worker-1      Started                                                              0.1s 
 ✔ Container docker-nginx-1       Started                                                              0.1s 
dify@my-pc:~/hello/dify/docker$ docker exec -it docker-api-1 flask reset-password
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
sagemaker.config INFO - Not applying SDK defaults from location: /etc/xdg/sagemaker/config.yaml
sagemaker.config INFO - Not applying SDK defaults from location: /root/.config/sagemaker/config.yaml
Email: hello@dify.ai
New password: newpassword4567
Password confirm: newpassword4567
Password reset successfully.
```

### 5. ポートの変更方法

Docker Compose を使用してデプロイする場合、`.env` 設定を変更することで Dify のアクセスポートをカスタマイズできます。

Nginx 関連の設定を変更する必要があります：

```
EXPOSE_NGINX_PORT=80
EXPOSE_NGINX_SSL_PORT=443
```


他のデプロイに関する質問は[ここに](../../learn-more/faq/install-faq.md)います。