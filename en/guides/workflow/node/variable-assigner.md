# Variable Assigner

### Definition

The variable assigner node is used to assign values to writable variables. Currently supported writable variables include:

* [conversation variables](https://docs.dify.ai/guides/workflow/key-concepts#conversation-variables).

Usage: Through the variable assigner node, you can assign workflow variables to conversation variables for temporary storage, which can be continuously referenced in subsequent conversations.

![](https://assets-docs.dify.ai/2024/11/83d0b9ef4c1fad947b124398d472d656.png)

***

### Usage Scenario Examples

Using the variable assigner node, you can write context from the conversation process, files uploaded to the dialog box, and user preference information into conversation variables. These stored variables can then be referenced in subsequent conversations to direct different processing flows or formulate responses.

**Scenario 1**

**Automatically judge and extract content**, store history in the conversation, record important user information through the session variable array within the conversation, and use this history content to personalize responses in subsequent chats.

Example: After the conversation starts, LLM will automatically determine whether the user's input contains facts, preferences, or chat history that need to be remembered. If it has, LLM will first extract and store those information, then use it as context to respond. If there is no new information to remember, LLM will directly use the previously relevant memories to answer questions.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/8d0492814b1515f50e87b2900ff400db.png)

**Configuration process:**

1. **Set Conversation Variables:**
   * First, set up a Conversation Variables array `memories`, of type array\[object] to store user information, preferences, and chat history.
2. **Determine and Extract Memories:**
   * Add a Conditional Branching node, using LLM to determine whether the user's input contains new information that needs to be remembered.
   * If there's new information, follow the upper branch and use an LLM node to extract this information.
   * If there's no new information, go down the branch and directly use existing memories to answer.
3. **Variable Assignment/Writing:**
   * In the upper branch, use the variable assigner node to append the newly extracted information to the `memories` array.
   * Use the escape function to convert the text string output by LLM into a format suitable for storage in an array\[object].
4. **Variable Reading and Usage:**
   * In subsequent LLM nodes, convert the contents of the `memories` array to a string and insert it into the prompt of LLM as context.
   * Use these memories to generate personalized responses.

The code for the node in the upper diagram is as follows:

1. Escape the string to object

```python
import json

def main(arg1: str) -> object:
    try:
        # Parse the input JSON string
        input_data = json.loads(arg1)
        
        # Extract the memory object
        memory = input_data.get("memory", {})
        
        # Construct the return object
        result = {
            "facts": memory.get("facts", []),
            "preferences": memory.get("preferences", []),
            "memories": memory.get("memories", [])
        }
        
        return {
            "mem": result
        }
    except json.JSONDecodeError:
        return {
            "result": "Error: Invalid JSON string"
        }
    except Exception as e:
        return {
            "result": f"Error: {str(e)}"
        }
```

2. Escape object as string

```python
import json

def main(arg1: list) -> str:
    try:
        # Assume arg1[0] is the dictionary we need to process
        context = arg1[0] if arg1 else {}
        
        # Construct the memory object
        memory = {"memory": context}
        
        # Convert the object to a JSON string
        json_str = json.dumps(memory, ensure_ascii=False, indent=2)
        
        # Wrap the JSON string in <answer> tags
        result = f"<answer>{json_str}</answer>"
        
        return {
            "result": result
        }
    except Exception as e:
        return {
            "result": f"<answer>Error: {str(e)}</answer>"
        }
```

**Scenario 2**

**Recording initial user preferences input**: Remember the user's language preference input during the conversation and continue to use this language for responses in subsequent chatting.

Example: Before the chatting, the user specifies "English" in the `language` input box. This language will be written to the conversation variable, and the LLM will reference this information when responding, continuing to use "English" in subsequent conversations.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/1867d608a7d009431b73377ed65b427b.png)

**Configuration Guide:**

**Set conversation variable**: First, set a conversation variable `language`. Add a condition judgment node at the beginning of the conversation flow to check if the `language` variable is empty.

**Variable writing/assignment**: At the start of the first round of chatting, if the `language` variable is empty, use an LLM node to extract the user's input language, then use a variable assigner node to write this language type into the conversation variable `language`.

**Variable reading**: In subsequent conversation rounds, the `language` variable has stored the user's language preference. The LLM node references the language variable to respond using the user's preferred language type.

**Scenario 3**

**Assisting with Checklist checks**: Record user inputs within the conversation using conversation variables, update the contents of the Checklist, and check for missing items in subsequent conversations.

Example: After starting the conversation, the LLM will ask the user to input items related to the Checklist in the chatting box. Once the user mentions content from the Checklist, it will be updated and stored in the Conversation Variable. The LLM will remind the user to continue supplementing missing items after each round of dialogue.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/workflow/node/c4362b01298b12e7d6fcd9e798f3165a.png)

**Configuration Process:**

* **Set conversation variable:** First, set a conversation variable `ai_checklist`, and reference this variable within the LLM as context for checking.
* **variable assigner/writing**: During each round of dialogue, check the value in `ai_checklist` within the LLM node and compare it with user input. If the user provides new information, update the Checklist and write the output content to `ai_checklist` using the variable assigner node.
* **Variable reading:** Read the value in `ai_checklist` and compare it with user input in each round of dialogue until all checklist items are completed.

***

### Using the Variable Assigner Node

Click the `+` icon on the right side of the node and select the **“Variable Assignment”** node. Configure the target variables and their corresponding source variables. This node allows you to assign values to multiple variables simultaneously.

![](https://assets-docs.dify.ai/2024/11/ee15dee864107ba5a93b459ebdfc32cf.png)

**Setting Variables:**

Variable: Select the variable to be assigned, i.e., specify the target conversation variable that needs to be assigned.

Set Variable: Select the variable to assign, i.e., specify the source variable that needs to be converted.

The variable assignment logic illustrated in the image above assigns the user’s language preference, specified on the initial page `Start/language`, to the system-level conversation variable `language`.

### **Operation Modes for Specifying Variables**

The data type of the target variable determines its operation method. Below are the operation modes for different variable types:

1.	Target variable data type: `String`

	•	**Overwrite**: Directly overwrite the target variable with the source variable.
	•	**Clear**: Clear the contents of the selected target variable.
	•	**Set**: Manually assign a value without requiring a source variable.

2.	Target variable data type: `Number`

	•	**Overwrite**: Directly overwrite the target variable with the source variable.
	•	**Clear**: Clear the contents of the selected target variable.
	•	**Set**: Manually assign a value without requiring a source variable.
	•	**Arithmetic**: Perform addition, subtraction, multiplication, or division on the target variable.

3.	Target variable data type: `Object`

	•	**Overwrite**: Directly overwrite the target variable with the source variable.
	•	**Clear**: Clear the contents of the selected target variable.
	•	**Set**: Manually assign a value without requiring a source variable.

4.	Target variable data type: `Array`

	•	**Overwrite**: Directly overwrite the target variable with the source variable.
	•	**Clear**: Clear the contents of the selected target variable.
	•	**Append**: Add a new element to the array in the target variable.
	•	**Extend**: Add a new array to the target variable, effectively adding multiple elements at once.

