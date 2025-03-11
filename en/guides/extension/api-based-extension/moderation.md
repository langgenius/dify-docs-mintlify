# Sensitive Content Moderation

This module is used to review the content input by end-users and the output content of the LLM within the application. It is divided into two types of extension points.

### Extension Points

* `app.moderation.input` - Extension point for reviewing end-user input content
  * Used to review the variable content passed in by end-users and the input content of conversational applications.
* `app.moderation.output` - Extension point for reviewing LLM output content
  * Used to review the content output by the LLM.
  * When the LLM output is streamed, the content will be segmented into 100-character blocks for API requests to avoid delays in reviewing longer outputs.

### app.moderation.input Extension Point

#### Request Body

```
{
    "point": "app.moderation.input", // Extension point type, fixed as app.moderation.input here
    "params": {
        "app_id": string,  // Application ID
        "inputs": {  // Variable values passed in by end-users, key is the variable name, value is the variable value
            "var_1": "value_1",
            "var_2": "value_2",
            ...
        },
        "query": string | null  // Current dialogue input content from the end-user, fixed parameter for conversational applications.
    }
}
```

* Example
  * ```
    {
        "point": "app.moderation.input",
        "params": {
            "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
            "inputs": {
                "var_1": "I will kill you.",
                "var_2": "I will fuck you."
            },
            "query": "Happy everydays."
        }
    }
    ```

#### API Response

```
{
    "flagged": bool,  // Whether it violates the moderation rules
    "action": string, // Action to take, direct_output for directly outputting a preset response; overridden for overriding the input variable values
    "preset_response": string,  // Preset response (returned only when action=direct_output)
    "inputs": {  // Variable values passed in by end-users, key is the variable name, value is the variable value (returned only when action=overridden)
        "var_1": "value_1",
        "var_2": "value_2",
        ...
    },
    "query": string | null  // Overridden current dialogue input content from the end-user, fixed parameter for conversational applications. (returned only when action=overridden)
}
```

* Example
  * `action=direct_output`
    * ```
      {
          "flagged": true,
          "action": "direct_output",
          "preset_response": "Your content violates our usage policy."
      }
      ```
  * `action=overridden`
    * ```
      {
          "flagged": true,
          "action": "overridden",
          "inputs": {
              "var_1": "I will *** you.",
              "var_2": "I will *** you."
          },
          "query": "Happy everydays."
      }
      ```

### app.moderation.output Extension Point

#### Request Body

```
{
    "point": "app.moderation.output", // Extension point type, fixed as app.moderation.output here
    "params": {
        "app_id": string,  // Application ID
        "text": string  // LLM response content. When the LLM output is streamed, this will be content segmented into 100-character blocks.
    }
}
```

* Example
  * ```
    {
        "point": "app.moderation.output",
        "params": {
            "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
            "text": "I will kill you."
        }
    }
    ```

#### API Response

```
{
    "flagged": bool,  // Whether it violates the moderation rules
    "action": string, // Action to take, direct_output for directly outputting a preset response; overridden for overriding the input variable values
    "preset_response": string,  // Preset response (returned only when action=direct_output)
    "text": string  // Overridden LLM response content (returned only when action=overridden)
}
```

* Example
  * `action=direct_output`
    * ```
      {
          "flagged": true,
          "action": "direct_output",
          "preset_response": "Your content violates our usage policy."
      }
      ```
  * `action=overridden`
    * ```
      {
          "flagged": true,
          "action": "overridden",
          "text": "I will *** you."
      }
      ```