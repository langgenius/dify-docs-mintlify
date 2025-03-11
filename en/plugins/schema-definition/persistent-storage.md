# Persistent Storage

If you look at the Tool and Endpoint in the plug-in alone, it is not difficult to find that in most cases it can only complete a single round of interaction, the request returns the data, and the task ends.

If there is a need for long-term storage of data, such as the implementation of persistent memory, the plug-in needs to have persistent storage capabilities. **Persistent storage mechanism allows plugins to have the ability to store data persistently in the same Workspace** , currently through the provision of KV database to meet the storage needs , the future may be based on the actual use of the introduction of more flexible and more powerful storage endpoints .

### Storage Key

#### **Entrance**

```python
    self.session.storage
```

#### Endpoints

```python
    def set(self, key: str, val: bytes) -> None:
        pass
```

You can notice that a bytes is passed in, so you can actually store files in it.

### Get Key

#### **Entrance**

```python
    self.session.storage
```

#### **Endpoint**

```python
    def get(self, key: str) -> bytes:
        pass
```

### Delete Key

#### **Entrance**

```python
    self.session.storage
```

#### **Endpoint**

```python
    def delete(self, key: str) -> None:
        pass
```

\
