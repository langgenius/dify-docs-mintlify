# Iteration

### Definition

Sequentially performs the same operations on array elements until all results are outputted, functioning as a task batch processor. Iteration nodes typically work in conjunction with array variables.

For example, when processing long text translations, inputting all content directly into an LLM node may reach the single conversation limit. To address the issue, upstream nodes first split the long text into multiple chunks, then use iteration nodes to perform batch translations, thus avoiding the message limit of a single LLM conversation.

***

### Functional Description

Using iteration nodes requires input values to be formatted as list objects. The node sequentially processes all elements in the array variable from the iteration start node, applying identical processing steps to each element. Each processing cycle is called an iteration, culminating in the final output.

An iteration node consists of three core components: **Input Variables**, **Iteration Workflow**, and **Output Variables**.

**Input Variables:** Accepts only Array type data.

**Iteration Workflow:** Supports multiple workflow nodes to orchestrate task sequences within the iteration node.

**Output Variables:** Outputs only array variables (`Array[List]`). 

![Iteration Node Functional Description](https://assets-docs.dify.ai/2024/12/7c94bccbb6f8dc4570c69c2bf02ec6d3.png)

### Scenarios

#### **Example 1: Long Article Iteration Generator**

![Long Story Generator](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/3a403551d48b178d0a41ce2a5748dd2d.png)

1. Enter the story title and outline in the **Start Node**.
2. Use a **Generate Subtitles and Outlines Node** to use LLM to generate the complete content from user input.
3. Use a **Extract Subtitles and Outlines Node** to convert the complete content into an array format.
4. Use an **Iteration Node** to wrap an **LLM Node** and generate content for each chapter through multiple iterations.
5. Add a **Direct Answer Node** inside the iteration node to achieve streaming output after each iteration.

**Detailed Configuration Steps**

1. Configure the story title (title) and outline (outline) in the **Start Node**.

![Start Node Configuration](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/3af1c2ed0df00f19e584bcf511302f55.png)

2. Use a **Generate Subtitles and Outlines Node** to convert the story title and outline into complete text.

![Template Node](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/55f1eceb43bd6e301078a08584988b18.png)

3. Use a **Extract Subtitles and Outlines Node** to convert the story text into an array (Array) structure. The parameter to extract is `sections`, and the parameter type is `Array[Object]`.

![Parameter Extraction](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d3beee536ff3c35f4e1eb1ab610f35d7.png)

{% hint style="info" %}
The effectiveness of parameter extraction is influenced by the model's inference capability and the instructions given. Using a model with stronger inference capabilities and adding examples in the **instructions** can improve the parameter extraction results.
{% endhint %}

4. Use the array-formatted story outline as the input for the iteration node and process it within the iteration node using an **LLM Node**.

![Configure Iteration Node](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/ac91582998868004b298afe2f04e5589.png)

Configure the input variables `GenerateOverallOutline/output` and `Iteration/item` in the LLM Node.

![Configure LLM Node](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d849ff9164482a83ea8a091fde9cb4d1.png)

{% hint style="info" %}
Built-in variables for iteration: `items[object]` and `index[number]`.

`items[object]` represents the input item for each iteration;

`index[number]` represents the current iteration round;
{% endhint %}

5. Configure a **Direct Reply Node** inside the iteration node to achieve streaming output after each iteration.

![Configure Answer Node](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/64da09ab904f74c8ec45e098c81f95be.png)

6. Complete debugging and preview.

![Generate by Iterating Through Story Chapters](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/f443508d9ecc6d30094297243f590e6a.png)

#### **Example 2: Long Article Iteration Generator (Another Arrangement)**

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/6e973b52bb3960bf948f92df8ae2f910.png)

* Enter the story title and outline in the **Start Node**.
* Use an **LLM Node** to generate subheadings and corresponding content for the article.
* Use a **Code Node** to convert the complete content into an array format.
* Use an **Iteration Node** to wrap an **LLM Node** and generate content for each chapter through multiple iterations.
* Use a **Template Conversion** Node to convert the string array output from the iteration node back to a string.
* Finally, add a **Direct Reply Node** to directly output the converted string.

***

### Advanced Feature

#### Parallel Mode

The iteration node supports parallel processing, improving execution efficiency when enabled.

![Enable parallel mode](https://assets-docs.dify.ai/2024/12/516af5e7427fce9a58fa9d9b583230d4.png)

Below illustrates the comparison between parallel and sequential execution in the iteration node.

![Sequential and Parallel Processing Flow Diagram](https://assets-docs.dify.ai/2024/12/2656dec26d6357556a280fcd69ccd9a7.png)

Parallel mode supports up to 10 concurrent iterations. When processing more than 10 tasks, the first 10 elements execute simultaneously, with remaining tasks processed after the completion of the initial batch.

{% hint style="info" %}
Avoid placing Direct Answer, Variable Assignment, or Tool nodes within the iteration node to prevent potential errors.
{% endhint %}

* **Error response method**

Iteration nodes process multiple tasks and may encounter errors during element processing. To prevent a single error from interrupting all tasks, configure the **Error Response Method**:

* **Terminated**: Terminates the iteration node and outputs error messages when an exception is detected.
* **Continue on error**: Ignores error messages and continues processing remaining elements. The output contains successful results with null values for errors.
* **Remove abnormal output**: Ignores error messages and continues processing remaining elements. The output contains only successful results.

Input and output variables maintain a one-to-one correspondence. For example:

* Input: \[1, 2, 3]
* Output: \[result-1, result-2, result-3]

Error handling examples:

* With **Continue on error**: \[result-1, null, result-3]
* With **Remove abnormal output**: \[result-1, result-3]

***

### Reference

#### How to Obtain Array-Formatted Content

Array variables can be generated via the following nodes as iteration node inputs:

* [Code Node](code.md)

![Parameter Extraction](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/d3beee536ff3c35f4e1eb1ab610f35d7.png)

* [Parameter Extraction](parameter-extractor.md)

![Parameter Extraction](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/b5a9d4bee95d7a1331bb7ff7433e47a3.png)

* [Knowledge Base Retrieval](knowledge-retrieval.md)
* [Iteration](iteration.md)
* [Tools](tools.md)
* [HTTP Request](http-request.md)

***

#### How to Convert an Array to Text

The output variable of the iteration node is in array format and cannot be directly output. You can use a simple step to convert the array back to text.

**Convert Using a Code Node**

![Code Node Conversion](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/8be2372b00a802e981efe6f0ceff815b.png)

CODE Example:

```python
def main(articleSections: list):
    data = articleSections
    return {
        "result": "/n".join(data)
    }
```

**Convert Using a Template Node**

![Template Node Conversion](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/8c0bcc5de453dea2776d2755449bd971.png)

CODE Example:

```django
{{ articleSections | join("/n") }}
```
