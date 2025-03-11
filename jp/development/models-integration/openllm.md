# OpenLLMでデプロイしたローカルモデルを統合

[OpenLLM](https://github.com/bentoml/OpenLLM)を使用すると、任意のオープンソース大規模言語モデルに対して推論を行い、クラウドまたはローカルにデプロイし、強力なAIアプリケーションを構築することができます。
DifyはローカルデプロイされたOpenLLMモデルの推論能力をサポートしています。

## OpenLLM モデルのデプロイ
### デプロイの開始

以下の方法でデプロイを開始できます：

```bash
docker run --rm -it -p 3333:3000 ghcr.io/bentoml/openllm start facebook/opt-1.3b --backend pt
```
> 注意点：ここで使用されている facebook/opt-1.3b モデルはあくまで例示であり、効果が不十分な場合があります。実際の状況に応じて適切なモデルを選択してください。詳細なモデルについては、[サポートされているモデル一覧](https://github.com/bentoml/OpenLLM#-supported-models)を参照してください。

モデルのデプロイが完了したら、Difyでモデルを接続して使用することができます。

`設定 > モデルプロバイダー > OpenLLM` の中で以下を入力します：

- モデル名：`facebook/opt-1.3b`
- サーバー URL：`http://<Machine_IP>:3333` ここで `<Machine_IP>` をあなたのマシンの IP アドレスに置き換えてください。
 "保存" を押せば、アプリケーション内でこのモデルを使用することができます。

この説明はあくまで迅速な接続のための例として提供されています。OpenLLMのその他の特性や情報については、[OpenLLM](https://github.com/bentoml/OpenLLM) を参照してください。