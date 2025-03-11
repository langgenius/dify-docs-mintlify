# Contribution

### Code Structure
The following code file structure outlines the organization of the project:
```
[cmd/]
├── server                // Server startup entry point
├── lib                   // Shared library entry point
└── test                  // Common test scripts
[build/]                  // Build scripts for different architectures and platforms
[internal/]               // Internal packages
├── controller            // HTTP request handlers
├── middleware            // Request processing middleware
├── server                // Server setup and configuration
├── service               // Controller services
├── static                // Configuration files
│   ├── nodejs_syscall    // Node.js system call whitelist
│   └── python_syscall    // Python system call whitelist
├── types                 // Entity definitions
├── core                  // Core isolation and execution logic
│   ├── lib               // Shared libraries
│   ├── runner            // Code execution
│   │   ├── nodejs        // Node.js executor
|   |   └── python        // Python executor
└── tests                 // CI/CD tests
```

### Principle
The core functionality has two entry points: the `HTTP` service entry for `DifySandbox` and the `dynamic link library` entry. When the Sandbox runs code, it first generates a temporary code file. This file begins by calling the `dynamic link library` to initialize the runtime environment (the `Sandbox`). The user's code is then executed within this temporary file, ensuring that the system remains protected from potentially harmful user-submitted code.

The dynamic link library uses `Seccomp` to restrict system calls. The `static` directory contains `nodejs_syscall` and `python_syscall` files, which provide system call whitelists for both `ARM64` and `AMD64` architectures. There are four files in total. Please do not modify these files unless absolutely necessary.

### How to Contribute
For minor issues like `Typos` and `Bugs`, feel free to submit a `Pull Request`. For major changes or `Feature`-level submissions, please open an `Issue` first to facilitate discussion.

#### To-Do List
Here are some items we're currently considering. If you're interested, you can choose one to contribute:
- [ ] Support for additional programming languages:
    - We currently support `Python` and `Node.js`. Consider adding support for new languages.
    - Remember to account for both `ARM64` and `AMD64` architectures, and provide `CI` testing to ensure security for any new language.
- [ ] Node.js dependency management:
    - We've implemented support for `Python` dependencies, which can be automatically installed during Sandbox initialization. However, due to the complexity of `node_modules`, we haven't yet found a good solution for `Node.js`. This is an area open for improvement.
- [ ] Image processing capabilities:
    - As multimodality becomes increasingly important, supporting image processing in the `Sandbox` would be valuable.
    - Consider adding support for image processing libraries like `Pillow`, and enable passing images into the `Sandbox` for processing in `Dify`.
- [ ] Enhanced `CI` testing:
    - Our current `CI` testing is limited and includes only basic test cases. More comprehensive testing would be beneficial.
- [ ] Multimodal data generation:
    - Explore using the `Sandbox` to generate multimodal data, such as combining text and images.