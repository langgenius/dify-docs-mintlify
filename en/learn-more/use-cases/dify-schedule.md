# Building the Dify Scheduler

> Author: [Leo\_chen](https://github.com/leochen-g), creator of [Dify Schedule](https://github.com/leochen-g/dify-schedule) and [Smart WeChat Assistant](https://github.com/leochen-g/wechat-assistant-pro)

## Overview

Tired of manually running Dify Workflows? Missing scheduled task support? With **Dify Schedule Assistant**, you can easily add scheduling capabilities to Dify Workflows. Using GitHub Actions, you can set up automated task execution with real-time notifications to optimize your workflow efficiency.

> Note: This tool only supports Dify Workflow applications

## 🌟 Core Features

* 🔄 Parallel execution of multiple Workflows
* ⏰ Flexible scheduling (Default: UTC+8 06:30)
* 📱 Multi-channel notifications
  * Enterprise: WeCom, DingTalk, Feishu
  * Personal: WeChat, Email, Server Chan, Pushplus
* 🔒 Secure execution via GitHub Actions
* 🐲 Support for QingLong Panel deployment

## 🚀 Quick Start

Two deployment options available:

1. **Online (GitHub Actions)**
2. **Local (QingLong Panel)**

### Option 1: GitHub Actions

1. **Fork Repository** Visit [Dify Schedule Repository](https://github.com/leochen-g/dify-schedule) and fork it.
2.  **Configure Secrets** Go to **Settings -> Secrets -> New repository secret** and add:

    | Secret Name     | Content                                        | Required |
    | --------------- | ---------------------------------------------- | -------- |
    | `DIFY_BASE_URL` | Dify API URL (Default: https://api.dify.ai/v1) | No       |
    | `DIFY_TOKENS`   | Dify Workflow API keys (separate with `;`)     | Yes      |
    | `DIFY_INPUTS`   | Workflow variables (JSON format)               | No       |

    **Notification Settings (Optional)**

    | Secret Name              | Content                                                                               | Purpose      |
    | ------------------------ | ------------------------------------------------------------------------------------- | ------------ |
    | `EMAIL_USER`             | Sender email (SMTP enabled)                                                           | Email        |
    | `EMAIL_PASS`             | SMTP password                                                                         | Email        |
    | `EMAIL_TO`               | Recipient emails (separate with `,`)                                                  | Email        |
    | `PUSHPLUS_TOKEN`         | [Pushplus](http://www.pushplus.plus/) token                                           | WeChat       |
    | `SERVERPUSHKEY`          | [Server Chan](https://sct.ftqq.com/) key                                              | WeChat       |
    | `DINGDING_WEBHOOK`       | DingTalk bot webhook                                                                  | DingTalk     |
    | `WEIXIN_WEBHOOK`         | WeCom bot webhook                                                                     | WeCom        |
    | `FEISHU_WEBHOOK`         | Feishu bot webhook                                                                    | Feishu       |
    | `AIBOTK_KEY`             | [Smart WeChat Assistant](https://wechat.aibotk.com/?r=dBL0Bn\&f=difySchedule) API Key | WeChat       |
    | `AIBOTK_ROOM_RECIVER`    | WeChat group name                                                                     | Group chat   |
    | `AIBOTK_CONTACT_RECIVER` | WeChat contact nickname                                                               | Private chat |
3. **Enable Workflow** Go to **Actions** tab and enable workflows.

### Option 2: Local Deployment

> QingLong Panel is an open-source task scheduler. [Project Link](https://github.com/whyour/qinglong)

1. **Install QingLong Panel** Follow instructions at [project page](https://github.com/whyour/qinglong).
2.  **Add Subscription** Run:

    ```bash
    ql repo https://github.com/leochen-g/dify-schedule.git "ql_" "utils" "sdk"
    ```
3. **Install Dependencies**
   * Go to【Dependencies】->【NodeJS】
   * Install `axios`
4. **Configure Environment Variables**
   * `DIFY_TOKENS`: Workflow API keys (Required)
   * `DIFY_BASE_URL`: API URL (Optional)
   * Separate multiple tokens with `;`
5. **Notifications**
   * Use QingLong's built-in notification system

## 📸 Notification Preview

|                             WeChat Notification Example                             |                             Email Notification Example                             |
| :---------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: |
| ![WeChat](https://assets-docs.dify.ai/2025/01/48d250d297950452a2c1a95babc06638.png) | ![Email](https://assets-docs.dify.ai/2025/01/192e3ec292686129198a45562fad26cf.png) |

## ❓ Troubleshooting Guide

### Getting API Keys

1. Login to Dify console
2. Access target Workflow
3. Visit API Reference page
4. Get API key

![](https://assets-docs.dify.ai/2025/01/f7239b198b4aeac98d209bfcebae153d.png)

## Common Issues

1. **Connection Issues**
   * Ensure private Dify instances have internet access
   * Verify network and firewall settings
2. **Execution Errors**
   * Verify application type is Workflow
   * Check `DIFY_INPUTS` JSON format
   * Review logs for missing variables

Report other issues on GitHub (remove sensitive information).

## 🤝 Contributing

Welcome community contributions:

* Feature suggestions
* Bug fixes
* Documentation improvements
* New features

Participate via Pull Requests or Issues.
