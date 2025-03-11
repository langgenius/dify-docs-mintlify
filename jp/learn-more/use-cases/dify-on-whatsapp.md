# DifyとTwilioを使用してWhatsAppボットを構築する方法

> 著者：Warren，[Microsoft 最有価値専門家 (MVP)](https://mvp.microsoft.com/en-US/mvp/profile/476f41d3-6bd1-ea11-a812-000d3a8dfe0d)

## 1. 概要

メッセージアプリケーションを通じて世界がますます密接に繋がる中、チャットボットは企業が顧客とより個別化された交流を行うための重要なツールとなっています。

人工知能の台頭に伴い、チャットボットはより賢く、個別化され、直感的になってきました。本記事では、DifyとTwilioを使用してWhatsAppと統合する方法を説明します。

まず、FastAPIを使用してDifyのバックエンドを設定し、その後、TwilioのWhatsAppメッセージAPIを統合し、顧客がWhatsAppチャットボットと対話できるようにします。

Localtunnelを使用して、FastAPIのローカルホストをインターネット上に公開し、Twilio APIとの通信が可能になります。

## 2. 準備作業

- DockerとDocker Composeのインストール
- Twilioアカウント： [こちら](https://www.twilio.com/try-twilio)で無料のTwilioアカウントを作成
- AIチャットボットのテスト用にWhatsAppをインストールしたスマートフォン
- Python 3.6+を使用してAPIを構築するためのフレームワークであるFastAPIの基本的な理解

## 3. Difyの基本的なチャットアシスタントアプリケーションの作成（[DifyをWeChatエコシステムに接続する方法](./dify-on-wechat.md)からの抜粋）

まず、[Dify公式アプリケーションプラットフォーム](https://cloud.dify.ai/signin)にログインします。GithubまたはGoogleのアカウントでログインすることができます。また、Dify公式チュートリアル[Docker Composeによるデプロイ | 日本語 | Dify](https://docs.dify.ai/v/ja-jp/getting-started/install-self-hosted/docker-compose)を参照して、プライベートデプロイを行うことも可能です。Difyはオープンソースプロジェクトであり、プライベートデプロイをサポートしています。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/08ece9f6dd15b6ba3c44eb187ea73bdd.jpeg)

ログイン後、Difyのページに移動し、以下のステップに従って基本的なチャットアシスタントアプリケーションを作成します。

1. ページ上部の「スタジオ」をクリック
2. 空のアプリケーションを作成
3. アプリケーションの種類を「チャットアシスタント」に選択
4. チャットアシスタントの編成方法を「基本編成」に選択
5. アプリケーションのアイコンを選択し、アプリケーションに「基本編成チャットアシスタント」などの名前を付ける
6. 作成をクリック

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/312d1fbcd5c8f58ca41b9f8dc8131286.jpeg)
作成が成功すると、上記のページに移動します。続いてアプリケーションを設定します。

1. モデルの選択（例：gpt-3.5-turbo-0125）
2. モデルパラメータの設定
3. アプリケーションのプロンプトを入力

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/410dc25f76beebf8659294b06c1a4d25.jpeg)

設定が完了したら、右側の対話ボックスでテストを行い、テストが完了したら以下の操作を行います。

1. 発行
2. 更新
3. APIのアクセス

##### （4）基本編成チャットアシスタントのAPIキーの生成
![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/de85ada57a6f1a0029486dbdaea62fcf.jpeg)

「APIのアクセス」をクリックすると、上記のAPI管理ページに移動します。このページで以下の手順に従ってAPIキーを取得します。

1. 右上の「APIキー」をクリック
2. 「キーを作成」をクリック
3. キーをコピーして保存

キーを保存した後、右上のAPIサーバーも確認してください。Dify公式のアプリケーションの場合、APIサーバーのアドレスは「https://api.dify.ai/v1」です。プライベートデプロイの場合は、自分のAPIサーバーアドレスを確認してください。

以上でチャットアシスタントの準備作業が終了です。このセクションでは、**APIキー**と**APIサーバーアドレス**の2つを保存する必要があります。

## 4. Twilioキーの取得

[Twilioコンソール]に移動し、Account SIDとAuth Tokenを取得して保存します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/f1586199a94ffefb18ffc4c8456a58d0.png)

## 5. チャットボットの作成

このセクションでは、FastAPIとTwilioを使用して基本的なチャットボットのコードを作成します。

#### 5.1 コードのダウンロード

```
git clone https://github.com/somethingwentwell/dify-twilio-whatsapp
```

#### 5.2 .envの設定

プロジェクトのルートディレクトリに.envを作成し、以下の内容を記載します。

```
TWILIO_NUMBER=+14155238886
TWILIO_ACCOUNT_SID=<4で取得したTwilio Account SID>
TWILIO_AUTH_TOKEN=<4で取得したTwilio Auth Token>
DIFY_URL=<3で取得したDify APIサーバーアドレス>
DIFY_API_KEY=<3で取得したDify APIキー>
```

#### 5.3 コードの実行

docker compose upを実行します。
```
docker compose up
```

成功すると、以下のメッセージが表示されるはずです。
```
dify-whatsapp-1  | INFO:     Started server process [68]
dify-whatsapp-1  | INFO:     Waiting for application startup.
dify-whatsapp-1  | INFO:     Application startup complete.
```

ブラウザーでhttp://localhost:9000を開きます。JSONレスポンス{"msg": "working"}が表示されるはずです。

#### 5.4 Localtunnelを使用してローカルプロジェクトをパブリックアクセスに公開

Twilioはバックエンドにメッセージを送信する必要があるため、アプリケーションをパブリックサーバーにホスティングする必要があります。Localtunnelを使用すると簡単です。

FastAPIアプリケーションを9000ポートで引き続き実行し、別のターミナルウィンドウで以下のlocaltunnelコマンドを実行します。

```
npx localtunnel --port 9000
```

このコマンドは、ローカルサーバー（9000ポートで実行中）とlocaltunnelが作成するパブリックドメイン間に接続を確立します。localtunnel転送URLを取得すると、クライアントからそのURLへのリクエストはすべて自動的にFastAPIのバックエンドに転送されます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/73f585d06be68fc71c0d37622a5b6f6c.png)

#### 5.5 コードの説明

##### 5.5.1 番号がホワイトリストに登録されているか確認し、未登録のユーザーには「このサービスに登録されていません」と返答

```python
enrolled_numbers = ['+14155238886']
```

対応するコード

```python
    # Check if the number is enrolled
    if whatsapp_number not in enrolled_numbers:
        message = client.messages.create(  
            from_=f"whatsapp:{twilio_number}",  
            body="You are not enrolled in this service.",  
            to=f"whatsapp:{whatsapp_number}"  
        )
        return ""
```

##### 5.5.2 WhatsApp番号をDifyセッションIDとして使用し、ユーザーのセッションを継続的に保持

```python
conversation_ids = {}
```

対応するコード

```python
    url = dify_url
    headers = {  
        'Content-Type': 'application/json',  
        'Authorization': f"Bearer {dify_api_key}",  
    }  
    data = {  
        'inputs': {},  
        'query': Body,  
        'response_mode': 'streaming',  
        'conversation_id': conversation_ids.get(whatsapp_number, ''),  
        'user': whatsapp_number,  
    }  
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)  
    answer = []  
    for line in response.iter_lines():  
        if line:  
            decoded_line = line.decode('utf-8')  
            if decoded_line.startswith('data: '):  
                decoded_line = decoded_line[6:]  
            try:  
                json_line = json.loads(decoded_line) 
                if "conversation_id" in json_line:
                    conversation_ids[whatsapp_number] = json_line["conversation_id"]
                if json_line["event"] == "agent_thought":  
                    answer.append(json_line["thought"])  
            except json.JSONDecodeError: 
                print(json_line)  
                continue  

    merged_answer = ''.join(answer)  
```

## 6. TwilioサンドボックスをWhatsAppで使用するための設定

#### 6.1 WhatsAppサンドボックスを開く

TwilioのメッセージAPIを使用して、チャットボットがWhatsAppユーザーと通信できるようにするために、Twilioサンドボックスを設定する必要があります。以下はその手順です。

[Twilioコンソール](https://console.twilio.com/)に移動し、左側のパネルでメッセージタブを選択します。

「試してみる」セクションで「WhatsAppメッセージを送信」をクリックします。デフォルトでサンドボックスタブに移動し、「+14155238886」という電話番号と、隣に参加コード、右側にQRコードが表示されます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/1f966b36bd5c213e4006a057b1c70c04.png)

Twilioのテスト環境を有効にするには、このコードのテキストをWhatsAppメッセージとして表示された電話番号に送信します。Webバージョンを使用している場合、ハイパーリンクをクリックしてWhatsAppチャットに誘導されることができます。

#### 6.2 WhatsAppサンドボックスの設定

「サンドボックス」タブの隣にある「サンドボックス設定」タブを選択します。

localtunnel URLをコピーし、/messageを追加します。それを「メッセージが届いたとき」の隣のボックスに貼り付けます。

TwilioサンドボックスのWebhook
完全なURLは次のようになります：https://breezy-humans-help.loca.lt/message。

FastAPIアプリケーションで設定したエンドポイントは/messageです。チャットボットのロジックはこのエンドポイントで実行されます。

設定が完了したら、「保存」ボタンを押します。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/6f810feee2a1eb07f718fc3f2be00b4b.png)

## 7. WhatsAppのテスト

6.1のページでQRコードをスキャンしてWhatsAppサンドボックス環境に入り、WhatsAppメッセージを送信してAIチャットボットの応答を待ちます。Difyチャットアシスタントに質問できることをAIチャットボットに試してみてください。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/use-cases/36376da1b4699289e944355282656780.jpeg)

## 8. 後記

これで、あなたのAIチャットボットはWhatsApp上で正常に動作しています。次のステップとして、Twilioサンドボックスではなく自分のWhatsAppビジネスアカウントを使用し、ローカルではなくサーバーでホスティングして、このWhatsAppアシスタントを本番環境で実行することが考えられます。このチュートリアルを楽しんでいただけたら幸いです。次回もお楽しみに。