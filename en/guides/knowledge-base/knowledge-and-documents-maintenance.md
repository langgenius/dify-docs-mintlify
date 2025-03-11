# Manage Knowledge

> The knowledge page is accessible only to the team owner, team administrators, and users with editor permissions.

Click the **Knowledge** button at the top of the Dify platform and select the knowledge you want to manage. Navigate to Settings in the left sidebar to configure it.

Here, you can modify the knowledge base’s name, description, permissions, indexing method, embedding model and retrieval settings.

![Knowledge base settings](https://assets-docs.dify.ai/2024/12/20fc93428f8f20f7acfce665c4ed4ddf.png)

* **Knowledge Name**: Used to distinguish among different knowledge bases.
* **Knowledge Description**: Used to describe the information represented by the documents in the knowledge base.
* **Permission**: Defines access control for the knowledge base with three levels:
  * **"Only Me"**: Restricts access to the knowledge base owner.
  * **"All team members"**: Grants access to every member of the team.
  *   **"Partial team members"**: Allows selective access to specific team members.

      Users without appropriate permissions cannot access the knowledge base. When granting access to team members (Options 2 or 3), authorized users are granted full permissions, including the ability to view, edit, and delete knowledge base content.
* **Indexing Mode**: For detailed explanations, please refer to the [documentation](create-knowledge-and-upload-documents/3.-select-the-indexing-method-and-retrieval-setting.md).
* **Embedding Model**: Allows you to modify the embedding model for the knowledge base. Changing the embedding model will re-embed all documents in the knowledge base, and the original embeddings will be deleted.
* **Retrieval Settings**: For detailed explanations, please refer to the [documentation](../../learn-more/extended-reading/retrieval-augment/retrieval.md).

***

#### View Linked Applications in the Knowledge Base

On the left side of the knowledge base, you can see all linked Apps. Hover over the circular icon to view the list of all linked apps. Click the jump button on the right to quickly browser them.

![Viewing the Linked Apps](https://assets-docs.dify.ai/2024/12/28899b9b0eba8996f364fb74e5b94c7f.png)

You can manage your knowledge base documents either through a web interface or via an API.

#### Maintain Knowledge Documents

You can administer all documents and their corresponding chunks directly in the knowledge base. For more details, refer to the following documentation:

{% content-ref url="knowledge-and-documents-maintenance/maintain-knowledge-documents.md" %}
[maintain-knowledge-documents.md](knowledge-and-documents-maintenance/maintain-knowledge-documents.md)
{% endcontent-ref %}

#### Maintain Knowledge Base Via API

Dify Knowledge Base provides a comprehensive set of standard APIs. Developers can use these APIs to perform routine management and maintenance tasks, such as adding, deleting, updating, and retrieving documents and chunks. For more details, refer to the following documentaiton:

{% content-ref url="knowledge-and-documents-maintenance/maintain-dataset-via-api.md" %}
[maintain-dataset-via-api.md](knowledge-and-documents-maintenance/maintain-dataset-via-api.md)
{% endcontent-ref %}

![Knowledge base API management](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/knowledge-base/02cf8bc06990606ff1d60b73ce7a82c8.png)
