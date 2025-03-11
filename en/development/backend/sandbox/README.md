# DifySandbox

### Introduction
`DifySandbox` is a lightweight, fast, and secure code execution environment that supports multiple programming languages, including Python and Node.js. It serves as the underlying execution environment for various components in Dify Workflow, such as the Code node, Template Transform node, LLM node, and the Code Interpreter in the Tool node. DifySandbox ensures system security while enabling Dify to execute user-provided code.

### Features
- **Multi-language Support**: DifySandbox is built on Seccomp, a low-level security mechanism that enables support for multiple programming languages. Currently, it supports Python and Node.js.
- **System Security**: It implements a whitelist policy, allowing only specific system calls to prevent unexpected security breaches.
- **File System Isolation**: User code runs in an isolated file system environment.
- **Network Isolation**:
    - **DockerCompose**: Utilizes a separate Sandbox network and proxy containers for network access, maintaining intranet system security while offering flexible proxy configuration options.
    - **K8s**: Network isolation strategies can be directly configured using Egress policies.

### Project Repository
You can access the [DifySandbox](https://github.com/langgenius/dify-sandbox) repository to obtain the project source code and follow the project documentation for deployment and usage instructions.

### Contribution
Please refer to the [Contribution Guide](contribution.md) to learn how you can participate in the development of DifySandbox.
