# Cloudflare ワーカーを使用して API ツールをデプロイ

## 入門

Dify API Extension は、アクセス可能な公開アドレスを API エンドポイントとして使用する必要があるため、API 拡張を公開アドレスにデプロイする必要があります。ここでは、Cloudflare ワーカーを使用して API 拡張をデプロイします。

まず、[Example GitHub レポジトリ](https://github.com/crazywoola/dify-extension-workers) をクローンします。このレポジトリには、簡単な API 拡張が含まれており、これを基にして修正を行うことができます。

```bash
git clone https://github.com/crazywoola/dify-extension-workers.git
cp wrangler.toml.example wrangler.toml
```

次に、`wrangler.toml` ファイルを開き、`名前` と `互換性の日付` をあなたのアプリ名と互換日付に変更します。

ここで注意が必要な設定は、`vars` 内の `トークン` です。Dify に API 拡張を追加する際に、このトークンを入力する必要があります。セキュリティ上の観点から、ランダムな文字列をトークンとして使用することをお勧めします。トークンをソースコードに直接書き込むのではなく、環境変数を使用してトークンを渡す方法を取るべきです。したがって、wrangler.toml をコードレポジトリにコミットしないでください。

```toml
name = "dify-extension-example"
compatibility_date = "2023-01-01"

[vars]
TOKEN = "bananaiscool"
```

この API 拡張は、ランダムなブレイキング・バッドの名言を返します。`src/index.ts` 内でこの API 拡張のロジックを変更することができます。この例は、サードパーティの API とやり取りする方法を示しています。

```typescript
// ⬇️ Implement your logic here ⬇️
// point === "app.external_data_tool.query"
// https://api.breakingbadquotes.xyz/v1/quotes
const count = params?.inputs?.count ?? 1;
const url = `https://api.breakingbadquotes.xyz/v1/quotes/${count}`;
const result = await fetch(url).then(res => res.text())
// ⬆️ implement your logic here ⬆️
```

このレポジトリは、ビジネスロジック以外のすべての設定を簡素化しています。`npm` コマンドを使用して API 拡張をデプロイすることができます。

```bash
npm run deploy
```

デプロイが成功すると、公開アドレスが得られます。このアドレスを Dify に API エンドポイントとして追加できます。`endpoint` パスを忘れないようにしてください。

![Dify に API エンドポイントを追加する](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/extension/api-based-extension/9433a486a441713ade6270e9dc6c0544.png)

![アプリ編集ページに API ツールを追加する](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/guides/extension/api-based-extension/72c285e58ec136a1a9a66f61b4b41ca1.png)

## その他のロジック TL;DR

### ベアラー認証について

```typescript
import { bearerAuth } from "hono/bearer-auth";

(c, next) => {
    const auth = bearerAuth({ token: c.env.TOKEN });
    return auth(c, next);
},
```

上記のコードでは、ベアラー認証ロジックを示しています。`hono/bearer-auth` パッケージを使用してベアラー認証を実装しています。`src/index.ts` で `c.env.TOKEN` を使用してトークンを取得できます。

### パラメータの検証について

```typescript
import { z } from "zod";
import { zValidator } from "@hono/zod-validator";

const schema = z.object({
  point: z.union([
    z.literal("ping"),
    z.literal("app.external_data_tool.query"),
  ]), // 'point' を2つの特定の値に制限
  params: z
    .object({
      app_id: z.string().optional(),
      tool_variable: z.string().optional(),
      inputs: z.record(z.any()).optional(),
      query: z.any().optional(),  // 文字列または null
    })
    .optional(),
});

```

ここでは、`zod` を使用してパラメータのタイプを定義しています。`src/index.ts` で `zValidator` を使用してパラメータを検証できます。`const { point, params } = c.req.valid("json");` を使用して検証後のパラメータを取得します。`point` は2つの値しか持たないため、`z.union` を使用して定義しています。`params` はオプションのため、`z.optional` を使用して定義しています。この中には `inputs` パラメータがあり、これは `Record<string, any>` 型です。この型はキーが文字列で値が任意のオブジェクトを示します。`src/index.ts` で `params?.inputs?.count` を使用して `count` パラメータを取得できます。

### Cloudflare ワーカーのログを取得する

```bash
wrangler tail
```

## 参考内容

* [Cloudflare Workers](https://workers.cloudflare.com/)
* [Cloudflare Workers CLI](https://developers.cloudflare.com/workers/cli-wrangler/install-update)
* [Example GitHub Repository](https://github.com/crazywoola/dify-extension-workers)