# Build An Article Reader Using File Upload

> Author: Steven Lynn. Dify Technical Writer.

In Dify, you can use the knowledge base to allow agent to obtain accurate information from a large amount of text content. However, in many cases, the local files provided are not large enough to warrant the use of the knowledge base. In such cases, you can use the file upload feature to directly provide local files as context for the LLM to read.

In this experiment, we will build the article reader as a case study. This assistant will ask questions based on the uploaded document, helping users to read papers and other materials with those questions in mind.

## You Will Learn

* File upload usage
* Basic usage of Chatflow
* Prompt writing skill
* Iteration node usage
* Doc extractor and list operator usage

## **Prerequisites**

Create a Chatflow in Dify. Make sure you have added a model provider and have sufficient quota.

{% @arcade/embed flowId="MKWZLfD4CtDJNQIOfLrI" url="https://app.arcade.software/share/MKWZLfD4CtDJNQIOfLrI" %}



## **Adding Nodes**

In this experiment, at least four types of nodes are required: start node, document extractor node, LLM node, and answer node.

### **Start Node**

In the start node, you need to add a file variable. File upload is supported in v0.10.0 Dify, allowing you to add files as variable.

For more information on file upload, please read: [File Upload](../../guides/workflow/file-upload.md)

In the start node, you need to add a file variable and check the document in the supported file types.

{% @arcade/embed flowId="oJXuUOTVI3UwWnSGafqE" url="https://app.arcade.software/share/oJXuUOTVI3UwWnSGafqE" %}



Some readers might notice the `sys.files` in the system variables, which are files or file lists uploaded by users in the dialog box.

The difference between creating your own file variables is that this feature requires enabling file upload in the functions and setting the upload file types, and each time a new file is uploaded in the dialog, this variable will be overwritten.

{% @arcade/embed flowId="zJDTlwV4OrEt1GKqbaQ0" url="https://app.arcade.software/share/zJDTlwV4OrEt1GKqbaQ0" %}



Please choose the appropriate file upload method according to your business scenario.

### **Doc Extractor**

**LLM cannot read files directly.** This is a common misconception among many users when they first use file upload, as they might think simply using the file as a variable in an LLM node would work. However, in reality, the LLM reads nothing from file variables.

Thus, Dify introduced the **doc extractor**, which can extract text from the file variable and output it as a text variable.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/bc4b1492bd10ef782457ec6a709997f9.png)

### **LLM**

In this experiment, two LLM nodes need to be designed: structure extraction and question generation.

#### **Structure Extraction**

The structure extraction node can extract the structure of the original text, summarizing key content.

The prompts are as follow:

```
Read the following article content and perform the task
{{Result variable of the document extractor}}
# Task

- **Main Objective**: Thoroughly analyze the structure of the article.
- **Objective**: Detail the content of each part of the article.
- **Requirements**: Analyze as detailed as possible.
- **Restrictions**: No specific format restrictions, but the analysis must be organized and logical.
- **Expected Output**: A detailed analysis of the article structure, including the main content and role of each part.

# Reasoning Order

- **Reasoning Part**: By carefully reading the article, identify and analyze its structure.
- **Conclusion Part**: Provide specific content and role for each part.

# Output Format

- **Analysis Format**: Each part should be listed in a headline format, followed by a detailed explanation of that part's content.
- **Structure Form**: Markdown, to enhance readability.
- **Specific Description**: The content and role of each part, including but not limited to the introduction, body, conclusion, citations, etc.
```

#### **Question Generation**

The question generation node can summarize the issues of the article from the content summarized by the structure extraction node, assisting the reader in thinking through the questions during the reading process.

The prompts are as follow:

```
Read the following article content and perform the task
{{Output of the structure extraction}}
# Task

- **Main Objective**: Thoroughly read the above text, and propose as many questions as possible for each part of the article.
- **Requirements**: Questions should be meaningful and valuable, worthy of consideration.
- **Restrictions**: No specific restrictions.
- **Expected Output**: A series of questions for each part of the article, each question should have depth and thinking value.

# Reasoning Order

- **Reasoning Part**: Thoroughly read the article, analyze the content of each part, and consider the deep questions each part may raise.
- **Conclusion Part**: Pose meaningful and valuable questions, ensuring they provoke in-depth thought.

# Output Format

- **Format**: Each question should be listed separately, numbered.
- **Content**: Propose questions for each part of the article (such as introduction, background, methods, results, discussion, conclusion, etc.).
- **Quantity**: As many as possible, but each question should be meaningful and valuable.
```

## **Question 1: Handling Multiple Uploaded Files**

To handle multiple uploaded files, an iterative node is needed.

The iterative node is similar to the while loop in many programming languages, except that Dify has no conditional restrictions, and the **input variable can only be of type `array` (list)**. The reason is that Dify will execute all the content in the list until it is done.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/cc9cbf8b718b8abbf84cd8649a08c1a3.png)

Therefore, you need to adjust the file variable in the start node to an `array` type, i.e., a file list.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/8eff802e3e1e3da466c5dc9ac56c50f2.png)

## **Question 2: Handling Specific Files from a File List**

In Question 1, some readers might notice that Dify will process all files before ending the loop, while in some cases, only a part of the files need to be operated on, not all. For this issue, you can process the file list in Dify using the **list operation** node. List operations can operate on all array-type variables, not just file lists.

For example, limit the analysis to only document-type files and sort the files to be processed in order of file names.

Before the iterative node, add a list operation, adjust the **filter condiftion** and **order by**, then change the input of the iterative node to the output of the list operation node.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/workshop/intermediate/287690e1fef87af270c0d5020d25d6cf.png)
