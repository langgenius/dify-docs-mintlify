# DifyでJSONスキーマ出力を使用する方法

JSON Schemaは、JSONデータ構造を記述するための仕様です。開発者は、LLMの出力が定義されたデータやコンテンツに厳密に適合するように、JSON Schema構造を定義することができます。これにより、明確で分かりやすいドキュメントやコード構造を生成することが可能となります。

## JSON Schema機能をサポートするモデル

* `gpt-4o-mini-2024-07-18` 及びそれ以降
* `gpt-4o-2024-08-06` 及びそれ以降

> OpenAIシリーズモデルの構造化された出力機能について詳しくは、[Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs/introduction)をご覧ください。

## DifyでのJSON Schemaの有効化

アプリケーション内のLLMを、上記で言及したJSON Schema出力をサポートするモデルのいずれかに切り替えます。次に、設定フォームで`JSON Schema`を有効にし、JSON Schemaテンプレートを入力します。同時に、`response_format`列を有効にし、`json_schema`形式に切り替えます。

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/extended-reading/899b0a46e438e50bef731fa45d3e7837.png)

LLMによって生成されたコンテンツは、次の形式で出力をサポートします：

* **テキスト：** テキスト形式で出力

## JSON Schemaテンプレートの定義

以下のJSON Schema形式を参考にして、テンプレートコンテンツを定義できます：

```json
{
    "name": "template_schema",
    "description": "JSON Schemaの汎用テンプレート",
    "strict": true,
    "schema": {
        "type": "object",
        "properties": {
            "field1": {
                "type": "string",
                "description": "field1の説明"
            },
            "field2": {
                "type": "number",
                "description": "field2の説明"
            },
            "field3": {
                "type": "array",
                "description": "field3の説明",
                "items": {
                    "type": "string"
                }
            },
            "field4": {
                "type": "object",
                "description": "field4の説明",
                "properties": {
                    "subfield1": {
                        "type": "string",
                        "description": "subfield1の説明"
                    }
                },
                "required": ["subfield1"],
                "additionalProperties": false
            }
        },
        "required": ["field1", "field2", "field3", "field4"],
        "additionalProperties": false
    }
}
```

段階的な指導：

1. 基本情報の説明：
   * `name`を設定：スキーマの記述に適した名前を選びます。
   * `description`を追加：スキーマの目的を簡潔に説明します。
   * `strict`をtrueに設定して厳密モードを確保します。
2. `schema`オブジェクトを作成：
   * `type: "object"`を設定して、ルートレベルをオブジェクト型として指定します。
   * すべてのフィールドを定義するために`properties`オブジェクトを追加します。
3. フィールドを定義：
   * 各フィールドに対して`type`と`description`を含むオブジェクトを作成します。
   * 一般的なタイプ：`string`、`number`、`boolean`、`array`、`object`。
   * 配列の場合は`items`を使用して要素のタイプを定義します。
   * オブジェクトの場合は、`properties`を再帰的に定義します。
4. 制約を設定：
   * 各レベルで`required`配列を追加し、すべての必須フィールドをリストアップします。
   * 各オブジェクトレベルで`additionalProperties: false`を設定します。
5. 特殊なフィールドの取り扱い：
   * オプションの値を制限するために`enum`を使用します。
   * 再帰構造を実装するために`$ref`を使用します。

## 例

### 1. 思考の連鎖（Chain-of-Thought）

**JSON Schemaの例**

```json
{
    "name": "math_reasoning",
    "description": "数学的推論の手順と最終回答を記録します",
    "strict": true,
    "schema": {
        "type": "object",
        "properties": {
            "steps": {
                "type": "array",
                "description": "推論ステップの配列",
                "items": {
                    "type": "object",
                    "properties": {
                        "explanation": {
                            "type": "string",
                            "description": "推論ステップの説明"
                        },
                        "output": {
                            "type": "string",
                            "description": "推論ステップの出力"
                        }
                    },
                    "required": ["explanation", "output"],
                    "additionalProperties": false
                }
            },
            "final_answer": {
                "type": "string",
                "description": "数学問題の最終回答"
            }
        },
        "additionalProperties": false,
        "required": ["steps", "final_answer"]
    }
}
```

**Prompt**

```
あなたは数学の助教です。数学問題が提示された際に、ステップバイステップの解法と最終回答を出力することが目標です。各ステップでは、出力欄に方程式を記入し、説明欄には推論の詳細を記述してください。
```

### UI生成（ルート再帰モード）

**JSON Schemaの例**

```json
{
    "name": "ui",
    "description": "動的に生成されたUI",
    "strict": true,
    "schema": {
        "type": "object",
        "properties": {
            "type": {
                "type": "string",
                "description": "UIコンポーネントのタイプ",
                "enum": ["div", "button", "header", "section", "field", "form"]
            },
            "label": {
                "type": "string",
                "description": "UIコンポーネントのラベル、ボタンやフォームフィールドに使用"
            },
            "children": {
                "type": "array",
                "description": "入れ子のUIコンポーネント",
                "items": {
                    "$ref": "#"
                }
            },
            "attributes": {
                "type": "array",
                "description": "UIコンポーネントのための任意の属性、任意の要素に適しています",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "属性の名前、例えばonClickやclassName"
                        },
                        "value": {
                            "type": "string",
                            "description": "属性の値"
                        }
                    },
                    "additionalProperties": false,
                    "required": ["name", "value"]
                }
            }
        },
        "required": ["type", "label", "children", "attributes"],
        "additionalProperties": false
    }
}
```

**Prompt**

```
あなたはUIジェネレータAIです。ユーザー入力をUIに変換してください。
```

**例の出力：**

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/jp/learn-more/extended-reading/03c1132f714cbd5920f5b0f80287a07d.png)

## ヒント

* アプリのプロンプトに、ユーザー入力が有効な応答を生成しない状況の処理方法に関する指示が含まれていることを確認してください。
* モデルは常に指定されたパターンに従おうとするため、入力が指定されたパターンとまったく無関係である場合、LLM が幻覚を引き起こす可能性があります。
* LLM が入力がタスクと互換性がないことを検出した場合、プロンプトに言語を含めて、空のパラメーターまたは特定の文が返されるように指定できます。
* すべてのフィールドは`required`である必要があります。詳細については、[こちら](https://platform.openai.com/docs/guides/structural-outputs/supported-schemas) を参照してください。
* [AdditionalProperties: false](https://platform.openai.com/docs/guides/structurd-outputs/Additionalproperties-false-must-always-be-set-in-objects) は常にオブジェクトに設定する必要があります
* スキーマのルートレベルのオブジェクトはオブジェクトである必要があります

## 参考資料

* [Introduction to Structured Outputs](https://cookbook.openai.com/examples/structured\_outputs\_intro)
* [Structured Output](https://platform.openai.com/docs/guides/structured-outputs/json-mode?context=without\_parse)
