# SearXNG

> ツール作者 @Junytang。

{% hint style="warning" %}
「ツール」は「プラグイン」エコシステムに完全アップグレードされました。詳しい使用方法については[プラグイン開発](https://docs.dify.ai/ja-jp/plugins/quick-start/install-plugins)をご参照ください。以下の内容はアーカイブされています。
{% endhint %}

SearXNGは、様々な検索サービスの結果を統合する無料のインターネットメタサーチエンジンです。 DifyはSearXNGにアクセスするためのインターフェイスを実装しており、Difyから直接利用することができます。 以下では、Dockerを使用してSearXNGをDifyに統合する手順を説明します。他の方法でSearXNGをインストールしたい場合は、[こちら](https://docs.searxng.org/admin/installation.html)を参照してください。

## 1. Dockerを使用してSearXNGコンテナをインストールする
設定ファイルは `dify/api/core/tools/provider/builtin/searxng/docker/settings.yml` にあり、[こちら](https://docs.searxng.org/admin/installation.html)を参照してください。

## 2. DifyのルートディレクトリでDockerコンテナを起動する
```
cd dify
docker run --rm -d -p 8081:8080 -v "${PWD}/api/core/tools/provider/builtin/searxng/docker:/etc/searxng" searxng/searxng
```

## 3. DifyにSearXNGを統合する
`ツール > SearXNG > 認証へ行く` でアクセスアドレスを入力します。Dockerを使用してDifyを展開する場合、アドレスは一般的に`http://host.docker.internal:8081`となります。