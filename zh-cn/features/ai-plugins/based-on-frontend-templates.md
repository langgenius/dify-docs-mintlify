# 基于 WebApp 模板

如果开发人员从零开始开发新产品，或者处于产品原型设计阶段，你可以使用Dify快速启动人工智能网站。同时，Dify希望开发者能够完全自由地创造出不同形式的前端应用。为此，我们提供:

* **SDK** 用于快速访问各种语言的dify API
* **WebApp Template** 用于为每种类型的应用程序搭建WebApp开发脚手架

根据麻省理工学院的许可，WebApp模板是开源的。你可以自由地修改和部署它们以实现dify的所有功能，或者作为实现你自己的应用程序的参考代码.

你可以在GitHub上找到这些模板:

* [Conversational app](https://github.com/langgenius/webapp-conversation)
* [Text generation app](https://github.com/langgenius/webapp-text-generator)

使用WebApp模板的最快捷方式是通过github点击 "**Use this template**" , 这相当于派生一个新的存储库. 然后你需要配置dify应用ID和API密钥, 比如:

```javascript
export const APP_ID = ''
export const API_KEY = ''
```

More config in `config/index.ts`:

```
export const APP_INFO: AppInfo = {
  "title": 'Chat APP',
  "description": '',
  "copyright": '',
  "privacy_policy": '',
  "default_language": 'zh-Hans'
}

export const isShowPrompt = true
export const promptTemplate = ''
```

每个WebApp模板都提供了一个包含部署说明的自述文件。通常，WebApp模板包含一个轻量级的后端服务，以确保开发者的API密钥不会直接暴露给用户.

这些WebApp模板可以帮助你快速构建AI应用的原型，并使用dify的所有功能。如果你在此基础上开发自己的应用程序或新模板，请随时与我们分享.
