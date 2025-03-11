# Difyスケジューラーの構築

> 著者: [Leo\_chen](https://github.com/leochen-g), [Difyワークフロースケジューラー](https://github.com/leochen-g/dify-schedule) および [Smart WeChat Assistant](https://github.com/leochen-g/wechat-assistant-pro) の開発者

## 概要

Difyワークフローを手動で実行するのにうんざりしていませんか？ スケジュールされたタスク機能が欲しいと思ったことはありませんか？ **Difyスケジュールアシスタント** を使えば、Difyワークフローに簡単にスケジュール機能を追加できます。 GitHub Actions を利用して、リアルタイム通知付きの自動タスク実行を設定し、ワークフローの効率を最大限に高めましょう。

> 注: このツールはDifyワークフローアプリケーション**のみ**をサポートしています。

## 🌟 主な機能

* 🔄 複数のワークフローを**同時**実行
* ⏰ 柔軟なスケジューリング (デフォルト: UTC+8 06:30)
* 📱 マルチチャネル通知
  * 企業向け: WeCom, DingTalk, Feishu
  * 個人向け: WeChat, Email, Server Chan, Pushplus
* 🔒 GitHub Actionsによる**セキュア**な実行
* 🐲 QingLongパネルへのデプロイをサポート

## 🚀 クイックスタート

以下の2つのデプロイオプションがあります。

1. **オンライン (GitHub Actions)**
2. **ローカル (QingLongパネル)**

### オプション1: GitHub Actions

1. **リポジトリをフォーク** [Difyスケジュールのリポジトリ](https://github.com/leochen-g/dify-schedule) にアクセスしてフォークしてください。
2. **シークレットの設定** **Settings -> Secrets -> New repository secret** に進み、以下を設定します。

    | シークレット名     | 内容                                                                     | 必須 |
    | --------------- | ------------------------------------------------------------------------ | -------- |
    | `DIFY_BASE_URL` | Dify API URL (デフォルト: https://api.dify.ai/v1)                         | いいえ   |
    | `DIFY_TOKENS`   | DifyワークフローのAPIキー (`;` で区切って複数指定可能)                     | はい     |
    | `DIFY_INPUTS`   | ワークフローの変数 (JSON形式)                                           | いいえ   |

    **通知設定 (オプション)**

    | シークレット名              | 内容                                                                                             | 目的       |
    | ------------------------ | -------------------------------------------------------------------------------------------------- | ------------ |
    | `EMAIL_USER`             | 送信元のメールアドレス (SMTP有効)                                                                  | Email        |
    | `EMAIL_PASS`             | SMTPパスワード                                                                                   | Email        |
    | `EMAIL_TO`               | 受信者のメールアドレス (`,` で区切って複数指定可能)                                                     | Email        |
    | `PUSHPLUS_TOKEN`         | [Pushplus](http://www.pushplus.plus/) のトークン                                                      | WeChat       |
    | `SERVERPUSHKEY`          | [Server Chan](https://sct.ftqq.com/) のキー                                                           | WeChat       |
    | `DINGDING_WEBHOOK`       | DingTalkボットのWebhook URL                                                                       | DingTalk     |
    | `WEIXIN_WEBHOOK`         | WeComボットのWebhook URL                                                                          | WeCom        |
    | `FEISHU_WEBHOOK`         | FeishuボットのWebhook URL                                                                         | Feishu       |
    | `AIBOTK_KEY`             | [Smart WeChat Assistant](https://wechat.aibotk.com/?r=dBL0Bn\&f=difySchedule) のAPIキー               | WeChat       |
    | `AIBOTK_ROOM_RECIVER`    | WeChatグループ名                                                                                   | グループチャット |
    | `AIBOTK_CONTACT_RECIVER` | WeChatコンタクトのニックネーム                                                                        | プライベートチャット |
3. **ワークフローを有効化** **Actions** タブを開き、ワークフローを有効にしてください。

### オプション2: ローカル環境へのデプロイ

> QingLongパネルは、オープンソースのタスクスケジューラーです。[プロジェクトリンク](https://github.com/whyour/qinglong)

1. **QingLongパネルのインストール** [プロジェクトページ](https://github.com/whyour/qinglong) の手順に従ってインストールしてください。
2. **サブスクリプションの追加** 次のコマンドを実行します：

    ```bash
    ql repo https://github.com/leochen-g/dify-schedule.git "ql_" "utils" "sdk"
    ```
3. **依存関係のインストール**
   * 【Dependencies】->【NodeJS】に移動
   * `axios` をインストール
4. **環境変数の設定**
   * `DIFY_TOKENS`: ワークフローのAPIキー (必須)
   * `DIFY_BASE_URL`: API URL (オプション)
   * 複数のAPIキーは`;` で区切ってください。
5. **通知**
   * QingLongに組み込まれている通知システムを使用します。

## 📸 通知のプレビュー

|                             WeChat通知の例                             |                             Email通知の例                             |
| :---------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------: |
| ![WeChat](https://assets-docs.dify.ai/2025/01/48d250d297950452a2c1a95babc06638.png) | ![Email](https://assets-docs.dify.ai/2025/01/192e3ec292686129198a45562fad26cf.png) |

## ❓ トラブルシューティングガイド

### APIキーの取得方法

1. Difyコンソールにログインします
2. 対象のワークフローにアクセスします
3. APIリファレンスページを開きます
4. APIキーを取得します

![](https://assets-docs.dify.ai/2025/01/f7239b198b4aeac98d209bfcebae153d.png)

## **よくある質問**

1. **接続に関する問題**
   * プライベートDifyインスタンスがインターネットにアクセスできることを確認してください
   * ネットワークとファイアウォールの設定を確認してください
2. **実行エラー**
   * アプリケーションタイプがワークフローであることを確認してください
   * `DIFY_INPUTS` のJSON形式が正しいことを確認してください
   * ログを確認して、不足している変数がないか確認してください

その他の問題については、GitHubでご報告ください (機密情報は削除してください)。

## 🤝 貢献

コミュニティからの貢献をお待ちしています！

* 機能の提案
* バグの修正
* ドキュメントの改善
* 新機能

プルリクエストまたはIssueを通じてご参加ください。