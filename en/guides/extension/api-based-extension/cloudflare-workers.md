# Deploy API Tools with Cloudflare Workers

## Getting Started

Since the Dify API Extension requires a publicly accessible internet address as an API Endpoint, we need to deploy our API extension to a public internet address. Here, we use Cloudflare Workers for deploying our API extension.

We clone the [Example GitHub Repository](https://github.com/crazywoola/dify-extension-workers), which contains a simple API extension. We can modify this as a base.

```bash
git clone https://github.com/crazywoola/dify-extension-workers.git
cp wrangler.toml.example wrangler.toml
```

Open the `wrangler.toml` file, and modify `name` and `compatibility_date` to your application's name and compatibility date.

An important configuration here is the `TOKEN` in `vars`, which you will need to provide when adding the API extension in Dify. For security reasons, it's recommended to use a random string as the Token. You should not write the Token directly in the source code but pass it via environment variables. Thus, do not commit your wrangler.toml to your code repository.

```toml
name = "dify-extension-example"
compatibility_date = "2023-01-01"

[vars]
TOKEN = "bananaiscool"
```

This API extension returns a random Breaking Bad quote. You can modify the logic of this API extension in `src/index.ts`. This example shows how to interact with a third-party API.

```typescript
// ⬇️ implement your logic here ⬇️
// point === "app.external_data_tool.query"
// https://api.breakingbadquotes.xyz/v1/quotes
const count = params?.inputs?.count ?? 1;
const url = `https://api.breakingbadquotes.xyz/v1/quotes/${count}`;
const result = await fetch(url).then(res => res.text())
// ⬆️ implement your logic here ⬆️
```

This repository simplifies all configurations except for business logic. You can directly use `npm` commands to deploy your API extension.

```bash
npm run deploy
```

After successful deployment, you will get a public internet address, which you can add in Dify as an API Endpoint. Please note not to miss the `endpoint` path.

![Adding API Endpoint in Dify](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/extension/api-based-extension/9433a486a441713ade6270e9dc6c0544.png)

![Adding API Tool in the App edit page](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/extension/api-based-extension/72c285e58ec136a1a9a66f61b4b41ca1.png)

## Other Logic TL;DR

### About Bearer Auth

```typescript
import { bearerAuth } from "hono/bearer-auth";

(c, next) => {
    const auth = bearerAuth({ token: c.env.TOKEN });
    return auth(c, next);
},
```

Our Bearer authentication logic is as shown above. We use the `hono/bearer-auth` package for Bearer authentication. You can use `c.env.TOKEN` in `src/index.ts` to get the Token.

### About Parameter Validation

```typescript
import { z } from "zod";
import { zValidator } from "@hono/zod-validator";

const schema = z.object({
  point: z.union([
    z.literal("ping"),
    z.literal("app.external_data_tool.query"),
  ]), // Restricts 'point' to two specific values
  params: z
    .object({
      app_id: z.string().optional(),
      tool_variable: z.string().optional(),
      inputs: z.record(z.any()).optional(),
      query: z.any().optional(),  // string or null
    })
    .optional(),
});
```

We use `zod` to define the types of parameters. You can use `zValidator` in `src/index.ts` for parameter validation. Get validated parameters through `const { point, params } = c.req.valid("json");`. Our point has only two values, so we use `z.union` for definition. `params` is an optional parameter, defined with `z.optional`. It includes a `inputs` parameter, a `Record<string, any>` type representing an object with string keys and any values. This type can represent any object. You can get the `count` parameter in `src/index.ts` using `params?.inputs?.count`.

### Accessing Logs of Cloudflare Workers

```bash
wrangler tail
```

## Reference Content

* [Cloudflare Workers](https://workers.cloudflare.com/)
* [Cloudflare Workers CLI](https://developers.cloudflare.com/workers/cli-wrangler/install-update)
* [Example GitHub Repository](https://github.com/crazywoola/dify-extension-workers)
