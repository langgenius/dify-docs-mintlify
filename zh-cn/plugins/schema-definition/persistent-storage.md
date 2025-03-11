# 持久化存储

如果单独审视插件中的 Tool 及 Endpoint，不难发现大多数情况下其只能完成单轮交互，请求后返回数据，任务结束。

如果有需要长期储存的数据，如实现持久化的记忆，需要插件具备持久化存储能力。**持久化储机制能够让插件具备在相同 Workspace 持久存储数据的能力**，目前通过提供 KV 数据库满足存储需求，未来可能会根据实际的使用情况推出更灵活更强大的储存接口。

### 储存 Key

#### **入口**

```python
    self.session.storage
```

#### **接口**

```python
    def set(self, key: str, val: bytes) -> None:
        pass
```

可以注意到传入的是一个 bytes，因此实际上你可以在其中储存文件。

### 获取 Key

#### **入口**

```python
    self.session.storage
```

#### **接口**

```python
    def get(self, key: str) -> bytes:
        pass
```

### 删除 Key

#### **入口**

```python
    self.session.storage
```

#### **接口**

```python
    def delete(self, key: str) -> None:
        pass
```
