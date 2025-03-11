# AlphaVantage Stock Analysis Tool

> Tool developed by [@zhuhao](https://github.com/hwzhuhao).

{% hint style="warning" %}
"Tools" has been fully upgraded to the "Plugins". For more details, please refer to [Install and Use Plugins](https://docs.dify.ai/plugins/quick-start/install-plugins). The content below has been archived.
{% endhint %}

AlphaVantage is a comprehensive online platform offering financial market data and APIs, enabling individual investors and developers to easily access stock quotes, technical indicators, and in-depth stock analysis. Dify has integrated the AlphaVantage tool, and the following are the steps to configure and use the AlphaVantage tool in Dify.

## 1. Obtaining an AlphaVantage API Key

To get started, acquire an API Key from [AlphaVantage](https://www.alphavantage.co/support/#api-key).

## 2. Configuring AlphaVantage in Dify

Navigate to the Dify dashboard and select `Tools > AlphaVantage > To Authorize` to input your API Key.

## 3. Implementing the Tool

- **In Chatflow / Workflow Applications**

Both Chatflow and Workflow applications support the integration of the `AlphaVantage` block. After adding a node, utilize [variables](https://docs.dify.ai/v/zh-hans/guides/workflow/variables) to reference the user's input query in the "Input Variables → Stock Code" field. In the "End" node, use variables to reference the output from the `AlphaVantage` block.

- **In Agent Applications**

Incorporate the `AlphaVantage` tool into your Agent application. Users can then input stock codes or general stock descriptions in the chat interface to trigger the tool and retrieve precise financial data.
