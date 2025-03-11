# Maintain Knowledge via API

> The authentication and invocation methods for the Knowledge Base API are consistent with the Application Service API. However, a single Knowledge Base API token generated has the authority to operate on all visible knowledge bases under the same account. Please pay attention to data security.

### Advantages of Utilizing Knowledge Base API

Leveraging the API for knowledge base maintenance significantly enhances data processing efficiency. It enables seamless data synchronization via command-line interfaces, facilitating automated operations instead of manipulating the user interface.

Key advantages include:

* Automated Synchronization: Enables seamless integration between data systems and the Dify knowledge base, fostering efficient workflow construction.
* Comprehensive Management: Offers functionalities such as knowledge base listing, document enumeration, and detailed querying, facilitating the development of custom data management interfaces.
* Flexible Content Ingestion: Accommodates both plain text and file upload methodologies, supporting batch operations for addition and modification of content chunks.
* Enhanced Productivity: Minimizes manual data handling requirements, thereby optimizing the overall user experience on the Dify platform.

### How to Use

Navigate to the knowledge base page, and you can switch to the **API ACCESS** page from the left navigation. On this page, you can view the dataset API documentation provided by Dify and manage the credentials for accessing the dataset API in **API Keys**.

![Knowledge API Document](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/knowledge-base/knowledge-and-documents-maintenance/2848fc9fc3a7f641f16eee11ed6c6223.png)

### API Requesting Examples

#### **Create a document from text**

This api is based on an existing Knowledge and creates a new document through text based on this Knowledge.

Request example:

```json
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/document/create_by_text' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "text","text": "text","indexing_technique": "high_quality","process_rule": {"mode": "automatic"}}'
```

Response example:

```json
{
  "document": {
    "id": "",
    "position": 1,
    "data_source_type": "upload_file",
    "data_source_info": {
        "upload_file_id": ""
    },
    "dataset_process_rule_id": "",
    "name": "text.txt",
    "created_from": "api",
    "created_by": "",
    "created_at": 1695690280,
    "tokens": 0,
    "indexing_status": "waiting",
    "error": null,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "archived": false,
    "display_status": "queuing",
    "word_count": 0,
    "hit_count": 0,
    "doc_form": "text_model"
  },
  "batch": ""
}
```

#### Create a Document from a file

This API is based on an existing knowledge and creates a new document through a file based on this knowledge.

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/document/create-by-file' \
--header 'Authorization: Bearer {api_key}' \
--form 'data="{"indexing_technique":"high_quality","process_rule":{"rules":{"pre_processing_rules":[{"id":"remove_extra_spaces","enabled":true},{"id":"remove_urls_emails","enabled":true}],"segmentation":{"separator":"###","max_tokens":500}},"mode":"custom"}}";type=text/plain' \
--form 'file=@"/path/to/file"'
```

```bash
{
  "document": {
    "id": "",
    "position": 1,
    "data_source_type": "upload_file",
    "data_source_info": {
      "upload_file_id": ""
    },
    "dataset_process_rule_id": "",
    "name": "Dify.txt",
    "created_from": "api",
    "created_by": "",
    "created_at": 1695308667,
    "tokens": 0,
    "indexing_status": "waiting",
    "error": null,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "archived": false,
    "display_status": "queuing",
    "word_count": 0,
    "hit_count": 0,
    "doc_form": "text_model"
  },
  "batch": ""
}

```

#### Create Documents from a File

This api is based on an existing Knowledge and creates a new document through a file based on this Knowledge.

Request example:

```json
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/document/create-by-file' \
--header 'Authorization: Bearer {api_key}' \
--form 'data="{"indexing_technique":"high_quality","process_rule":{"rules":{"pre_processing_rules":[{"id":"remove_extra_spaces","enabled":true},{"id":"remove_urls_emails","enabled":true}],"segmentation":{"separator":"###","max_tokens":500}},"mode":"custom"}}";type=text/plain' \
--form 'file=@"/path/to/file"'
```

Response example:

```json
{
  "document": {
    "id": "",
    "position": 1,
    "data_source_type": "upload_file",
    "data_source_info": {
      "upload_file_id": ""
    },
    "dataset_process_rule_id": "",
    "name": "Dify.txt",
    "created_from": "api",
    "created_by": "",
    "created_at": 1695308667,
    "tokens": 0,
    "indexing_status": "waiting",
    "error": null,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "archived": false,
    "display_status": "queuing",
    "word_count": 0,
    "hit_count": 0,
    "doc_form": "text_model"
  },
  "batch": ""
}

```

#### Create an Empty Knowledge Base

{% hint style="warning" %}
Only used to create an empty knowledge base.
{% endhint %}

Request example:

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "name", "permission": "only_me"}'
```

Response example:

```json
{
  "id": "",
  "name": "name",
  "description": null,
  "provider": "vendor",
  "permission": "only_me",
  "data_source_type": null,
  "indexing_technique": null,
  "app_count": 0,
  "document_count": 0,
  "word_count": 0,
  "created_by": "",
  "created_at": 1695636173,
  "updated_by": "",
  "updated_at": 1695636173,
  "embedding_model": null,
  "embedding_model_provider": null,
  "embedding_available": null
}
```

#### Get Knowledge Base List

Request example:

```bash
curl --location --request GET 'https://api.dify.ai/v1/datasets?page=1&limit=20' \
--header 'Authorization: Bearer {api_key}'
```

Response example:

```json
{
  "data": [
    {
      "id": "",
      "name": "name",
      "description": "desc",
      "permission": "only_me",
      "data_source_type": "upload_file",
      "indexing_technique": "",
      "app_count": 2,
      "document_count": 10,
      "word_count": 1200,
      "created_by": "",
      "created_at": "",
      "updated_by": "",
      "updated_at": ""
    },
    ...
  ],
  "has_more": true,
  "limit": 20,
  "total": 50,
  "page": 1
}
```

#### Delete a Knowledge Base

Request example:

```json
curl --location --request DELETE 'https://api.dify.ai/v1/datasets/{dataset_id}' \
--header 'Authorization: Bearer {api_key}'
```

Response example:

```json
204 No Content
```

#### Update a Document with Text

This api is based on an existing Knowledge and updates the document through text based on this Knowledge

Request example:

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/update_by_text' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "name","text": "text"}'
```

Response example:

```json
{
  "document": {
    "id": "",
    "position": 1,
    "data_source_type": "upload_file",
    "data_source_info": {
      "upload_file_id": ""
    },
    "dataset_process_rule_id": "",
    "name": "name.txt",
    "created_from": "api",
    "created_by": "",
    "created_at": 1695308667,
    "tokens": 0,
    "indexing_status": "waiting",
    "error": null,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "archived": false,
    "display_status": "queuing",
    "word_count": 0,
    "hit_count": 0,
    "doc_form": "text_model"
  },
  "batch": ""
}
```

#### Update a document with a file

This api is based on an existing Knowledge, and updates documents through files based on this Knowledge.

Request example:

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/update-by-file' \
--header 'Authorization: Bearer {api_key}' \
--form 'data="{"name":"Dify","indexing_technique":"high_quality","process_rule":{"rules":{"pre_processing_rules":[{"id":"remove_extra_spaces","enabled":true},{"id":"remove_urls_emails","enabled":true}],"segmentation":{"separator":"###","max_tokens":500}},"mode":"custom"}}";type=text/plain' \
--form 'file=@"/path/to/file"'
```

Response example:

```json
{
  "document": {
    "id": "",
    "position": 1,
    "data_source_type": "upload_file",
    "data_source_info": {
      "upload_file_id": ""
    },
    "dataset_process_rule_id": "",
    "name": "Dify.txt",
    "created_from": "api",
    "created_by": "",
    "created_at": 1695308667,
    "tokens": 0,
    "indexing_status": "waiting",
    "error": null,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "archived": false,
    "display_status": "queuing",
    "word_count": 0,
    "hit_count": 0,
    "doc_form": "text_model"
  },
  "batch": "20230921150427533684"
}
```

#### Get Document Embedding Status (Progress)

Request example:

```bash
curl --location --request GET 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{batch}/indexing-status' \
--header 'Authorization: Bearer {api_key}'
```

Response example:

```json
{
  "data":[{
    "id": "",
    "indexing_status": "indexing",
    "processing_started_at": 1681623462.0,
    "parsing_completed_at": 1681623462.0,
    "cleaning_completed_at": 1681623462.0,
    "splitting_completed_at": 1681623462.0,
    "completed_at": null,
    "paused_at": null,
    "error": null,
    "stopped_at": null,
    "completed_segments": 24,
    "total_segments": 100
  }]
}
```

#### Delete a Document

Request example:

```bash
curl --location --request DELETE 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}' \
--header 'Authorization: Bearer {api_key}'
```

Response example:

```bash
{
  "result": "success"
}
```

#### Get the Document List of a Knowledge Base

Request example:

```bash
curl --location --request GET 'https://api.dify.ai/v1/datasets/{dataset_id}/documents' \
--header 'Authorization: Bearer {api_key}'
```

Response example:

```json
{
  "data": [
    {
      "id": "",
      "position": 1,
      "data_source_type": "file_upload",
      "data_source_info": null,
      "dataset_process_rule_id": null,
      "name": "dify",
      "created_from": "",
      "created_by": "",
      "created_at": 1681623639,
      "tokens": 0,
      "indexing_status": "waiting",
      "error": null,
      "enabled": true,
      "disabled_at": null,
      "disabled_by": null,
      "archived": false
    },
  ],
  "has_more": false,
  "limit": 20,
  "total": 9,
  "page": 1
}
```

#### Add Chunks to a Document

Request example:

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{"segments": [{"content": "1","answer": "1","keywords": ["a"]}]}'
```

Response example:

```json
{
  "data": [{
    "id": "",
    "position": 1,
    "document_id": "",
    "content": "1",
    "answer": "1",
    "word_count": 25,
    "tokens": 0,
    "keywords": [
        "a"
    ],
    "index_node_id": "",
    "index_node_hash": "",
    "hit_count": 0,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "status": "completed",
    "created_by": "",
    "created_at": 1695312007,
    "indexing_at": 1695312007,
    "completed_at": 1695312007,
    "error": null,
    "stopped_at": null
  }],
  "doc_form": "text_model"
}

```

#### Get Chunks from a Document

Request example:

```bash
curl --location --request GET 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json'
```

Response example:

```bash
{
  "data": [{
    "id": "",
    "position": 1,
    "document_id": "",
    "content": "1",
    "answer": "1",
    "word_count": 25,
    "tokens": 0,
    "keywords": [
        "a"
    ],
    "index_node_id": "",
    "index_node_hash": "",
    "hit_count": 0,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "status": "completed",
    "created_by": "",
    "created_at": 1695312007,
    "indexing_at": 1695312007,
    "completed_at": 1695312007,
    "error": null,
    "stopped_at": null
  }],
  "doc_form": "text_model"
}
```

#### Delete a Chunk in a Document

Request example:

```bash
curl --location --request DELETE 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json'
```

Response example:

```bash
{
  "result": "success"
}
```

#### Update a Chunk in a Document

Request example:

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json'\
--data-raw '{"segment": {"content": "1","answer": "1", "keywords": ["a"], "enabled": false}}'
```

Response example:

```bash
{
  "data": [{
    "id": "",
    "position": 1,
    "document_id": "",
    "content": "1",
    "answer": "1",
    "word_count": 25,
    "tokens": 0,
    "keywords": [
        "a"
    ],
    "index_node_id": "",
    "index_node_hash": "",
    "hit_count": 0,
    "enabled": true,
    "disabled_at": null,
    "disabled_by": null,
    "status": "completed",
    "created_by": "",
    "created_at": 1695312007,
    "indexing_at": 1695312007,
    "completed_at": 1695312007,
    "error": null,
    "stopped_at": null
  }],
  "doc_form": "text_model"
}
```

#### Retrieve Chunks from a Knowledge Base

Request example:

```bash
curl --location --request POST 'https://api.dify.ai/v1/datasets/{dataset_id}/retrieve' \
--header 'Authorization: Bearer {api_key}'\
--header 'Content-Type: application/json'\
--data-raw '{
    "query": "test",
    "retrieval_model": {
        "search_method": "keyword_search",
        "reranking_enable": false,
        "reranking_mode": null,
        "reranking_model": {
            "reranking_provider_name": "",
            "reranking_model_name": ""
        },
        "weights": null,
        "top_k": 1,
        "score_threshold_enabled": false,
        "score_threshold": null
    }
}'
```

Response example:

```bash
{
  "query": {
    "content": "test"
  },
  "records": [
    {
      "segment": {
        "id": "7fa6f24f-8679-48b3-bc9d-bdf28d73f218",
        "position": 1,
        "document_id": "a8c6c36f-9f5d-4d7a-8472-f5d7b75d71d2",
        "content": "Operation guide",
        "answer": null,
        "word_count": 847,
        "tokens": 280,
        "keywords": [
          "install",
          "java",
          "base",
          "scripts",
          "jdk",
          "manual",
          "internal",
          "opens",
          "add",
          "vmoptions"
        ],
        "index_node_id": "39dd8443-d960-45a8-bb46-7275ad7fbc8e",
        "index_node_hash": "0189157697b3c6a418ccf8264a09699f25858975578f3467c76d6bfc94df1d73",
        "hit_count": 0,
        "enabled": true,
        "disabled_at": null,
        "disabled_by": null,
        "status": "completed",
        "created_by": "dbcb1ab5-90c8-41a7-8b78-73b235eb6f6f",
        "created_at": 1728734540,
        "indexing_at": 1728734552,
        "completed_at": 1728734584,
        "error": null,
        "stopped_at": null,
        "document": {
          "id": "a8c6c36f-9f5d-4d7a-8472-f5d7b75d71d2",
          "data_source_type": "upload_file",
          "name": "readme.txt",
          "doc_type": null
        }
      },
      "score": 3.730463140527718e-05,
      "tsne_position": null
    }
  ]
}
```

### Error message

Response example:

```bash
  {
    "code": "no_file_uploaded",
    "message": "Please upload your file.",
    "status": 400
  }

```

| code                          | status | message                                                                                      |
| ----------------------------- | ------ | -------------------------------------------------------------------------------------------- |
| no\_file\_uploaded            | 400    | Please upload your file.                                                                     |
| too\_many\_files              | 400    | Only one file is allowed.                                                                    |
| file\_too\_large              | 413    | File size exceeded.                                                                          |
| unsupported\_file\_type       | 415    | File type not allowed. Supported format: txt, markdown, md, pdf, html, html, xlsx, docx, csv |
| high\_quality\_dataset\_only  | 400    | Current operation only supports 'high-quality' datasets.                                     |
| dataset\_not\_initialized     | 400    | The dataset is still being initialized or indexing. Please wait a moment.                    |
| archived\_document\_immutable | 403    | The archived document is not editable.                                                       |
| dataset\_name\_duplicate      | 409    | The dataset name already exists. Please modify your dataset name.                            |
| invalid\_action               | 400    | Invalid action.                                                                              |
| document\_already\_finished   | 400    | The document has been processed. Please refresh the page or go to the document details.      |
| document\_indexing            | 400    | The document is being processed and cannot be edited.                                        |
| invalid\_metadata             | 400    | The metadata content is incorrect. Please check and verify.                                  |
