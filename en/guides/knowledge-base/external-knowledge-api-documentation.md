---
description: 'Editor: Allen. Dify Technical Writer'
---

# External Knowledge API

## Endpoint

```
POST <your-endpoint>/retrieval
```

## Header

This API is used to connect to a knowledge base that is independent of the Dify and maintained by developers. For more details, please refer to [Connecting to an External Knowledge Base](https://docs.dify.ai/guides/knowledge-base/connect-external-knowledge-base). You can use `API-Key` in the `Authorization` HTTP Header to verify permissions. The authentication logic is defined by you in the retrieval API, as shown below:

```
Authorization: Bearer {API_KEY}
```

## Request Body Elements

The request accepts the following data in JSON format.

| Property | Required | Type | Description | Example value |
|----------|----------|------|-------------|---------------|
| knowledge_id | TRUE | string | Your knowledge's unique ID | AAA-BBB-CCC |
| query | TRUE | string | User's query | What is Dify? |
| retrieval_setting | TRUE | object | Knowledge's retrieval parameters | See below |

The `retrieval_setting` property is an object containing the following keys:

| Property | Required | Type | Description | Example value |
|----------|----------|------|-------------|---------------|
| top_k | TRUE | int | Maximum number of retrieved results | 5 |
| score_threshold | TRUE | float | The score limit of relevance of the result to the query, scope: 0~1 | 0.5 |

## Request Syntax

```json
POST <your-endpoint>/retrieval HTTP/1.1
-- header
Content-Type: application/json
Authorization: Bearer your-api-key
-- data
{
    "knowledge_id": "your-knowledge-id",
    "query": "your question",
    "retrieval_setting":{
        "top_k": 2,
        "score_threshold": 0.5
    }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

| Property | Required | Type | Description | Example value |
|----------|----------|------|-------------|---------------|
| records | TRUE | List[Object] | A list of records from querying the knowledge base. | See below |

The `records` property is a list object containing the following keys:

| Property | Required | Type | Description | Example value |
|----------|----------|------|-------------|---------------|
| content | TRUE | string | Contains a chunk of text from a data source in the knowledge base. | Dify:The Innovation Engine for GenAI Applications |
| score | TRUE | float | The score of relevance of the result to the query, scope: 0~1 | 0.5 |
| title | TRUE | string | Document title | Dify Introduction |
| metadata | FALSE | json | Contains metadata attributes and their values for the document in the data source. | See example |

## Response Syntax

```json
HTTP/1.1 200
Content-type: application/json
{
    "records": [{
                    "metadata": {
                            "path": "s3://dify/knowledge.txt",
                            "description": "dify knowledge document"
                    },
                    "score": 0.98,
                    "title": "knowledge.txt",
                    "content": "This is the document for external knowledge."
            },
            {
                    "metadata": {
                            "path": "s3://dify/introduce.txt",
                            "description": "dify introduce"
                    },
                    "score": 0.66,
                    "title": "introduce.txt",
                    "content": "The Innovation Engine for GenAI Applications"
            }
    ]
}
```

## Errors

If the action fails, the service sends back the following error information in JSON format:

| Property | Required | Type | Description | Example value |
|----------|----------|------|-------------|---------------|
| error_code | TRUE | int | Error code | 1001 |
| error_msg | TRUE | string | The description of API exception | Invalid Authorization header format. Expected 'Bearer <api-key>' format. |

The `error_code` property has the following types:

| Code | Description |
|------|-------------|
| 1001 | Invalid Authorization header format. |
| 1002 | Authorization failed |
| 2001 | The knowledge does not exist |

### HTTP Status Codes

**AccessDeniedException**
The request is denied because of missing access permissions. Check your permissions and retry your request.
HTTP Status Code: 403

**InternalServerException**
An internal server error occurred. Retry your request.
HTTP Status Code: 500
