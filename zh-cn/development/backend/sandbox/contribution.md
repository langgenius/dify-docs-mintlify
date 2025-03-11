# 贡献

### 代码结构
参考如下代码文件结构可以帮助你更好地理解代码的组织方式。
```
[cmd/]
├── server                // Enterpoint for starting the server.
├── lib                   // Enterpoint for Shared libraries.
└── test                  // Common test scripts.
[build/]                  // build scripts for different architectures and platforms.
[internal/]               // Internal packages.
├── controller            // HTTP request handlers.
├── middleware            // Middleware for request processing.
├── server                // Server setup and configuration.
├── service               // Provides service for controller.
├── static                // Configuration files.
│   ├── nodejs_syscall    // Whitelist for nodejs syscall.
│   └── python_syscall    // Whitelist for python syscall.
├── types                 // Entities
├── core                  // Core logic for isolation and execution.
│   ├── lib               // Shared libraries.
│   ├── runner            // Code execution.
│   │   ├── nodejs        // Nodejs runner.
|   |   └── python        // Python runner.
└── tests                 // Tests for CI/CD.
```

### 原理
目前来说，核心逻辑的入口部分有两个，一个是`DifySandbox`的`HTTP`服务入口，另一个是`动态链接库`的入口，在Sandbox尝试运行代码时，它会首先生产一个临时代码文件，在这个文件的最开始，会调用`动态链接库`来初始化运行环境，也就是`Sandbox`，随后才是用户代码的执行，最终执行代码时并不会直接执行用户提交的代码，而是执行这个临时文件，从而确保不会被用户提交的代码破坏系统。

其中，动态链接库中就是使用了`Seccomp`来限制系统调用，其中运行的系统调用位于`static`目录下的`nodejs_syscall`和`python_syscall`文件中，并分别提供了`ARM64`和`AMD64`两种架构的系统调用白名单，一共四份文件，在没有特殊需求的情况下，请不要随意修改这些文件。

### 如何贡献
首先，对于`Typo`、`Bug`等问题，欢迎直接提交`PR`，如果是较大的改动或`Feature`级别的提交，请先提交`Issue`，以便我们更好地讨论。

#### 待办事项
这里是一些我们目前正在考虑的待办事项，如果你有兴趣，可以选择其中一个来贡献。
- [ ] 新编程语言的支持：
    - 我们目前支持`Python`和`Nodejs`，如果你有兴趣，可以尝试添加新的编程语言支持。
    - 请注意，每新增一个语言，都要同时考虑`ARM64`和`AMD64`两种架构，并提供`CI`测试，以便我们能确保新增语言的安全性。
- [ ] Nodejs的依赖问题：
    - 目前我们仅完成了`Python`的依赖支持，可以在`Sandbox`初始化时自动安装`Python`依赖，但对于`Nodejs`，由于其`node_modules`的复杂性，我们目前还没有找到一个很好的解决方案，如果你有兴趣，可以尝试解决这个问题。
- [ ] 图片处理:
    - 在未来、多模态是一个必然的趋势，因此在`Sandbox`支持处理图片也是一个很有意义的事情。
    - 你可以尝试添加对图片处理的支持，比如`Pillow`等库的支持，并支持在`Dify`中传入图片到`Sandbox`中进行处理。
- [ ] 完善的`CI`测试：
    - 目前我们的`CI`测试还不够完善，只有一些简单的用例。
- [ ] 生成多模态数据:
    - 尝试使用`Sandbox`生成多模态数据，比如文本和图片的组合数据。