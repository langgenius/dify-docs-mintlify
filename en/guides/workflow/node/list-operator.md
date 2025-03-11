# List Operator

File list variables support simultaneous uploading of multiple file types such as document files, images, audio, and video files. When application users upload files, all files are stored in the same `Array[File]` array-type variable, which **is not conducive to subsequent individual file processing.**

> The `Array` data type means that the actual value of the variable could be \[1.mp3, 2.png, 3.doc]. LLMs only support reading single values such as image files or text content as input variables and cannot directly read array variables.

#### Node Functionality

The list operator can filter and extract attributes such as file format type, file name, and size, passing different format files to corresponding processing nodes to achieve precise control over different file processing flows.

For example, in an application that allows users to upload both document files and image files simultaneously, different files need to be sorted through the **list operation node**, with different files being handled by different processes.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/522a0c932aab93d4f3970168412f759e.png)

List operation nodes are generally used to extract information from array variables, converting them into variable types that can be accepted by downstream nodes through setting conditions. Its structure is divided into input variables, filter conditions, sorting, taking the first N items, and output variables.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/812d1b2f167065e17df8392b2cb3cc8a.png)

**Input Variables**

The list operation node only accepts variables with the following data structures:

* Array\[string]
* Array\[number]
* Array\[file]

**Filter Conditions**

Process arrays in input variables by adding filter conditions. Sort out all array variables that meet the conditions from the array, which can be understood as filtering the attributes of variables.

Example: Files may contain multiple dimensions of attributes, such as file name, file type, file size, etc. Filter conditions allow setting screening conditions to select and extract specific files from array variables.

Supports extracting the following variables:

* type: File category, including image, document, audio, and video types
* size: File size
* name: File name
* url: Refers to files uploaded by application users via URL, can fill in the complete URL for filtering
* extension: File extension
* mime\_type: [MIME types](https://datatracker.ietf.org/doc/html/rfc2046) are standardized strings used to identify file content types. Example: "text/html" indicates an HTML document.
* transfer\_method: File upload method, divided into local upload or upload via URL

**Sorting**

Provides the ability to sort arrays in input variables, supporting sorting based on file attributes.

* Ascending order(ASC): Default sorting option, sorted from small to large. For letters and text, sorted in alphabetical order (A - Z)
* Descending order(DESC): Sorted from large to small, for letters and text, sorted in reverse alphabetical order (Z - A)

This option is often used in conjunction with first\_record and last\_record in output variables.

**Take First N Items**

You can choose a value between 1-20, used to select the first n items of the array variable.

**Output Variables**

Array elements that meet all filter conditions. Filter conditions, sorting, and limitations can be enabled separately. If enabled simultaneously, array elements that meet all conditions are returned.

* Result: Filtering result, data type is array variable. If the array contains only 1 file, the output variable contains only 1 array element;
* first\_record: The first element of the filtered array, i.e., result\[0];
* last\_record: The last element of the filtered array, i.e., result\[array.length-1].

***

#### Configuration Example

In file interaction Q\&A scenarios, application users may upload document files or image files simultaneously. LLMs only support the ability to recognize image files and do not support reading document files. At this time, the List Operation node is needed to preprocess the array of file variables and send different file types to corresponding processing nodes. The orchestration steps are as follows:

1. Enable the [Features](../additional-features.md) function and check both "Images" and "Document" types in the file types.
2. Add two list operation nodes, setting to extract image and document variables respectively in the "List Operator" conditions.
3. Extract document file variables and pass them to the "Doc Extractor" node; extract image file variables and pass them to the "LLM" node.
4. Add a "Answer" node at the end, filling in the output variable of the LLM node.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/610358293217e54b55b7e1d4d16bf83c.png)

After the application user uploads both document files and images, document files are automatically diverted to the doc extractor node, and image files are automatically diverted to the LLM node to achieve joint processing of mixed files.
