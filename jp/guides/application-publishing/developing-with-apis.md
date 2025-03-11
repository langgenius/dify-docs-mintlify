# API 基づく開発

Difyは、「**後端即サービス(Backend as a Service)**」の理念に基づいて、すべてのアプリケーションにAPIを提供し、AIアプリケーション開発者に多くの利便性をもたらしています。この理念を通じて、開発者は複雑なバックエンドアーキテクチャやデプロイプロセスを気にすることなく、フロントエンドアプリケーションで大型言語モデル（LLM）の強力な能力を直接利用できます。

### Dify API を使用する利点

* フロントエンドアプリケーションが直接安全にLLMの能力を呼び出すことができ、バックエンドサービスの開発プロセスを省略
* 視覚的なインターフェースでアプリケーションを設計し、すべてのクライアントにリアルタイムで反映
* LLMプロバイダーの基本能力を良好にパッケージ化
* LLMプロバイダーをいつでも切り替え、LLMのAPIキーを集中管理
* 視覚的なインターフェースでアプリケーションを運営、例えばログの分析、ラベリング、ユーザーの活性度の観察
* アプリケーションに対して継続的により多くのツール能力、プラグイン能力、データセットを提供

### 利用方法

アプリケーションを選択し、アプリケーション（Apps）の左側ナビゲーションで**APIアクセス（API Access）**を見つけます。このページでDifyが提供するAPIドキュメントを確認し、APIにアクセスするための認証情報を管理できます。

![APIアクセス](../../../en/.gitbook/assets/guides\application-publishing\launch-your-webapp-quickly/API Access.png)

例えば、あなたがコンサルティング会社の開発部門であれば、会社のプライベートデータベースに基づいてAI能力をエンドユーザーや開発者に提供できますが、開発者はあなたのデータやAIロジック設計を把握することはできません。これにより、サービスは安全かつ持続可能に提供され、商業目的を満たすことができます。

{% hint style="warning" %}
ベストプラクティスとして、APIキーはバックエンドで呼び出されるべきで、フロントエンドコードやリクエストに平文で直接露出しないようにしてください。これにより、アプリケーションの悪用や攻撃を防ぐことができます。
{% endhint %}

アプリケーションに対して**複数のアクセス認証情報**を作成し、異なるユーザーや開発者に提供することができます。これにより、APIの使用者はアプリケーション開発者が提供するAI能力を使用できますが、その背後のプロンプトエンジニアリング、データセット、ツール能力はパッケージ化されています。

### テキスト生成型アプリケーション

高品質なテキスト生成に使用できるアプリケーション、例えば記事生成、要約、翻訳などが含まれます。completion-messagesエンドポイントを呼び出し、ユーザー入力を送信して生成されたテキスト結果を取得します。テキスト生成に使用されるモデルパラメータとプロンプトテンプレートは、Difyのプロンプト編成ページで開発者が設定したものに依存します。

**アプリケーション -> APIアクセス**でそのアプリケーションのAPIドキュメントとサンプルリクエストを見つけることができます。

例えば、テキスト補完情報のAPIの呼び出し例：

{% tabs %}
{% tab title="cURL" %}
```
curl --location --request POST 'https://api.dify.ai/v1/completion-messages' \
--header 'Authorization: Bearer ENTER-YOUR-SECRET-KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "response_mode": "streaming",
    "user": "abc-123"
}'
```
{% endtab %}

{% tab title="Python" %}
```python
import requests
import json

url = "https://api.dify.ai/v1/completion-messages"

headers = {
    'Authorization': 'Bearer ENTER-YOUR-SECRET-KEY',
    'Content-Type': 'application/json',
}

data = {
    "inputs": {"text": 'Hello, how are you?'},
    "response_mode": "streaming",
    "user": "abc-123"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)
```
{% endtab %}
{% endtabs %}

### 会話型アプリケーション

大部分のシーンで使用できる会話型アプリケーションは、一問一答形式でユーザーと継続的に会話します。会話を開始するにはchat-messagesエンドポイントを呼び出し、返されたconversation\_idを引き続き提供することで会話を継続することができます。

#### `conversation_id` に関する重要事項:

- **`conversation_id` の生成:** 新しい会話を開始するときは、`conversation_id` フィールドを空のままにしておきます。システムは新しい `conversation_id` を生成して返します。この新しい `conversation_id` は、今後のやり取りで使用して会話を続行します。
- **既存のセッションでの `conversation_id` の処理:** `conversation_id` が生成されると、Dify ボットとの会話の継続性を確保するために、今後の API 呼び出しにこの `conversation_id` を含める必要があります。以前の `conversation_id` が渡されると、新しい `inputs` は無視されます。進行中の会話では `query` のみが処理されます。
- **動的変数の管理:** セッション中にロジックまたは変数を変更する必要がある場合は、会話変数 (セッション固有の変数) を使用してボットの動作または応答を調整できます。

**アプリケーション -> APIアクセス**でそのアプリケーションのAPIドキュメントとサンプルリクエストを見つけることができます。

以下は`chat-messages`のAPIの呼び出し例：

{% tabs %}
{% tab title="cURL" %}
```
curl --location --request POST 'https://api.dify.ai/v1/chat-messages' \
--header 'Authorization: Bearer ENTER-YOUR-SECRET-KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "query": "eh",
    "response_mode": "streaming",
    "conversation_id": "1c7e55fb-1ba2-4e10-81b5-30addcea2276",
    "user": "abc-123"
}'

```
{% endtab %}

{% tab title="Python" %}
```python
import requests
import json

url = 'https://api.dify.ai/v1/chat-messages'
headers = {
    'Authorization': 'Bearer ENTER-YOUR-SECRET-KEY',
    'Content-Type': 'application/json',
}
data = {
    "inputs": {},
    "query": "eh",
    "response_mode": "streaming",
    "conversation_id": "1c7e55fb-1ba2-4e10-81b5-30addcea2276",
    "user": "abc-123"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text())
```
{% endtab %}
{% endtabs %}