# How to connect with AWS Bedrock Knowledge Base？

This article will briefly introduce how to connect the Dify platform with the AWS Bedrock knowledge base through the [external knowledge base API](https://docs.dify.ai/guides/knowledge-base/external-knowledge-api-documentation), so that AI applications in the Dify platform can directly obtain content stored in the AWS Bedrock knowledge base and expand new information source channels.

### Pre-preparation

* AWS Bedrock Knowledge Base
* Dify SaaS Service / Dify Community Version
* Backend API Development Basics

### 1. Register and Create AWS Bedrock Knowledge Base

Visit [AWS Bedrock](https://aws.amazon.com/bedrock/) and create the Knowledge Base service.

![Create AWS Bedrock Knowledge Base](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/1bf24647a5ffeba4accecd1052011980.png)

### 2. Build the Backend API Service

The Dify platform cannot directly connect to AWS Bedrock Knowledge Base. The developer needs to refer to Dify's [API definition](../../guides/knowledge-base/external-knowledge-api-documentation.md) on external knowledge base connection, manually create the backend API service, and establish a connection with AWS Bedrock. Please refer to the specific architecture diagram:

![Build the backend API service](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/c57ce0a77ee668268f53e91497bd5c2b.png)

You can refer to the following 2 demo code.

`knowledge.py`

```python
from flask import request
from flask_restful import Resource, reqparse

from bedrock.knowledge_service import ExternalDatasetService


class BedrockRetrievalApi(Resource):
    # url : <your-endpoint>/retrieval
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("retrieval_setting", nullable=False, required=True, type=dict, location="json")
        parser.add_argument("query", nullable=False, required=True, type=str,)
        parser.add_argument("knowledge_id", nullable=False, required=True, type=str)
        args = parser.parse_args()

        # Authorization check
        auth_header = request.headers.get("Authorization")
        if " " not in auth_header:
            return {
                "error_code": 1001,
                "error_msg": "Invalid Authorization header format. Expected 'Bearer <api-key>' format."
            }, 403
        auth_scheme, auth_token = auth_header.split(None, 1)
        auth_scheme = auth_scheme.lower()
        if auth_scheme != "bearer":
            return {
                "error_code": 1001,
                "error_msg": "Invalid Authorization header format. Expected 'Bearer <api-key>' format."
            }, 403
        if auth_token:
            # process your authorization logic here
            pass

        # Call the knowledge retrieval service
        result = ExternalDatasetService.knowledge_retrieval(
            args["retrieval_setting"], args["query"], args["knowledge_id"]
        )
        return result, 200
```

`knowledge_service.py`

```python
import boto3


class ExternalDatasetService:
    @staticmethod
    def knowledge_retrieval(retrieval_setting: dict, query: str, knowledge_id: str):
        # get bedrock client
        client = boto3.client(
            "bedrock-agent-runtime",
            aws_secret_access_key="AWS_SECRET_ACCESS_KEY",
            aws_access_key_id="AWS_ACCESS_KEY_ID",
            # example: us-east-1
            region_name="AWS_REGION_NAME",
        )
        # fetch external knowledge retrieval
        response = client.retrieve(
            knowledgeBaseId=knowledge_id,
            retrievalConfiguration={
                "vectorSearchConfiguration": {"numberOfResults": retrieval_setting.get("top_k"), "overrideSearchType": "HYBRID"}
            },
            retrievalQuery={"text": query},
        )
        # parse response
        results = []
        if response.get("ResponseMetadata") and response.get("ResponseMetadata").get("HTTPStatusCode") == 200:
            if response.get("retrievalResults"):
                retrieval_results = response.get("retrievalResults")
                for retrieval_result in retrieval_results:
                    # filter out results with score less than threshold
                    if retrieval_result.get("score") < retrieval_setting.get("score_threshold", .0):
                        continue
                    result = {
                        "metadata": retrieval_result.get("metadata"),
                        "score": retrieval_result.get("score"),
                        "title": retrieval_result.get("metadata").get("x-amz-bedrock-kb-source-uri"),
                        "content": retrieval_result.get("content").get("text"),
                    }
                    results.append(result)
        return {
            "records": results
        }
```

During the process, you can construct the API endpoint address and the API Key for authentication and use them for the next connections.

### 3. Get the AWS Bedrock Knowledge Base ID

After log in to the AWS Bedrock Knowledge backend and get the ID of the created Knowledge Base, you can use this parameter to connect to the Dify platform in the subsequent steps.

![Get the AWS Bedrock Knowledge Base ID](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/03fd7e383daf419765bbfd05c3742923.png)

### 4. Associate the External Knowledge API

Go to the **"Knowledge"** page in the Dify platform, click **"External Knowledge API"** in the upper right corner, and tap **"Add an External Knowledge API"**.

Follow the prompts on the page and fill in the following information:

* The name of the knowledge base. Custom names are allowed to distinguish different external knowledge APIs connected to the Dify platform;
* API endpoint address, the connection address of the external knowledge base, which can be customized in [Step 2](how-to-connect-aws-bedrock.md#id-2.build-the-backend-api-service). Example: `api-endpoint/retrieval`;
* API Key, the external knowledge base connection key, which can be customized in [Step 2](how-to-connect-aws-bedrock.md#id-2.build-the-backend-api-service).

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/4f2ce69f8c59e788beb91303c68db571.png)

### 5. Connect to External Knowledge Base

Go to the **“Knowledge** page, click **“Connect to an External Knowledge Base”** below the add knowledge base card to jump to the parameter configuration page.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/c3c30c7ed923ee1d7986e92bb35186c6.png)

Fill in the following parameters:

* **Knowledge base name and description**
* **External knowledge base API**

Select the external knowledge base API associated in Step 4.
* **External knowledge base ID**

Fill in the AWS Bedrock knowledge base ID obtained in Step 3.
* **Adjust recall settings**

**Top K:** When a user asks a question, the external knowledge API will be requested to obtain the most relevant content chunks. This parameter is used to filter text chunks with high similarity to user questions. The default value is 3. The higher the value, the more relevant text chunks will be recalled.

**Score threshold:** The similarity threshold for text chunk filtering. Only text chunks with a score exceeding the set score will be recalled. The default value is 0.5. The higher the value, the higher the similarity required between the text and the question, the smaller the number of texts expected to be recalled, and the more accurate the result will be.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/58c324c08c1c5fc23ab31e04967ae449.png)

After the settings are completed, you can establish a connection with the external knowledge base API.

### 6. Test External Knowledge Base Connection and Retrieval

After establishing a connection with an external knowledge base, developers can simulate possible user's question keywords in **"Retrieval Test"** and preview the text chunks retrieval from the AWS Bedrock Knowledge Base.

![Test the connection and retrieval of the external knowledge base](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/fbc64f060f9fda83847428439b07c247.png)

If you are not satisfied with the retrieval results, you can try to modify the retrieval parameters or adjust the retrieval settings of AWS Bedrock Knowledge Base.

![Adjust the text chunking parameters of AWS Bedrock Knowledge Base](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/0984a89e4cf2a1150ec3160da14c656e.png)
