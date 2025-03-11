# Moderation

This module is used to review the content input by end-users and the output from LLMs within the application, divided into two types of extension points.

Please read [.](./ "mention") to complete the development and integration of basic API service capabilities.

## Extension Point

`app.moderation.input`: End-user input content review extension point. It is used to review the content of variables passed in by end-users and the input content of dialogues in conversational applications.

`app.moderation.output`: LLM output content review extension point. It is used to review the content output by LLM. When the LLM output is streaming, the content will be requested by the API in chunks of 100 characters to avoid delays in review when the output content is lengthy.

### `app.moderation.input`

#### Request Body

```json
{
    "point": "app.moderation.input", 
        "app_id": string,  
        "inputs": {  
            "var_1": "value_1",
            "var_2": "value_2",
            ...
        },
        "query": string | null  
    }
}
```

* Example

```json
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

```json
{
    "flagged": bool,  
    "action": string, 
    "preset_response": string,  
    "inputs": {  
        "var_1": "value_1",
        "var_2": "value_2",
        ...
    },
    "query": string | null  
}
```

* Example

`action=direct_output`

```json
{
    "flagged": true,
    "action": "direct_output",
    "preset_response": "Your content violates our usage policy."
}
```

`action=overridden`

```
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

### `app.moderation.output`

#### Request Body

```JSON
{
    "point": "app.moderation.output", 
    "params": {
        "app_id": string,  
        "text": string  
    }
}
```

*   Example



    ```JSON
    {
        "point": "app.moderation.output",
        "params": {
            "app_id": "61248ab4-1125-45be-ae32-0ce91334d021",
            "text": "I will kill you."
        }
    }
    ```

#### API Response

```JSON
{
    "flagged": bool,  
    "action": string, 
    "preset_response": string,  
    "text": string  
```

* Example

`action=direct_output`

* ```JSON
  {
      "flagged": true,
      "action": "direct_output",
      "preset_response": "Your content violates our usage policy."
  }
  ```

`action=overridden`

* ```JSON
  {
      "flagged": true,
      "action": "overridden",
      "text": "I will *** you."
  }
  ```

