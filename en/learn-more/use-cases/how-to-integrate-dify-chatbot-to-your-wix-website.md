# Integrating Dify Chatbot into Your Wix Website

Wix, a popular website creation platform, allows users to visually design their websites through drag-and-drop functionality. By leveraging Wix's iframe code feature, you can seamlessly integrate a Dify chatbot into your Wix site.

This functionality extends beyond chatbot integration, enabling you to display content from external servers and other sources within your Wix pages. Examples include weather widgets, stock tickers, calendars, or any custom web elements.

This guide will walk you through the process of embedding a Dify chatbot into your Wix website using iframe code. The same method can be applied to integrate Dify applications into other websites, blogs, or web pages.

## 1. Obtaining the Dify Application iFrame Code Snippet

Assuming you've already created a [Dify AI application](https://docs.dify.ai/guides/application-orchestrate/creating-an-application), follow these steps to acquire the iFrame code snippet:

1. Log into your Dify account
2. Select the Dify application you wish to embed
3. Click the "Publish" button in the upper right corner
4.  On the publish page, choose the "Embed Into Site" option

    ![Embed Into Site Option](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/238daf21d6632d7d20cc9a6b882194f9.png)
5.  Select an appropriate style and copy the displayed iFrame code. For example:

    ![iFrame Code Example](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/ebab9e1f734d80e793db3675a46099fb.png)

## 2. Embedding the iFrame Code Snippet in Your Wix Site

1. Log into your Wix website and open the page you want to edit
2. Click the blue `+` (Add Elements) button on the left side of the page
3.  Select **Embed Code**, then click **Embed HTML** to add an HTML iFrame element to the page

    ![Add HTML iFrame](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/43b79d103da8beb69619e8f122609b89.png)
4. In the `HTML Settings` box, select the `Code` option
5. Paste the iFrame code snippet you obtained from your Dify application
6. Click the **Update** button to save and preview your changes

Here's an example of an iFrame code snippet for embedding a Dify Chatbot:

```bash
<iframe src="https://udify.app/chatbot/ez1pf83HVV3JgWO4" style="width: 100%; height: 100%; min-height: 700px" frameborder="0" allow="microphone"></iframe>
```

![Insert Dify iFrame Code](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/fb257be087645aaa5eb2ae01a4a15d8d.png)

> ⚠️ Ensure the address in the iFrame code begins with HTTPS. HTTP addresses will not display correctly.

## 3. Customizing Your Dify Chatbot

You can adjust the Dify Chatbot's button style, position, and other settings.

### 3.1 Customizing Style

Modify the `style` attribute in the iFrame code to customize the Chatbot button's appearance. For example:

```bash
<iframe src="https://udify.app/chatbot/ez1pf83HVV3JgWO4" style="width: 100%; height: 100%; min-height: 700px" frameborder="0" allow="microphone"></iframe>

# Add a 2-pixel wide solid black border: border: 2px solid #000

→

<iframe src="https://udify.app/chatbot/ez1pf83HVV3JgWO4" style="width: 80%; height: 80%; min-height: 500px; border: 2px solid #000;" frameborder="0" allow="microphone"></iframe>
```

This code adds a 2-pixel wide solid black border to the chatbot interface.

### 3.2 Customizing Position

Adjust the button's position by modifying the `position` value in the `style` attribute. For example:

```bash
<iframe src="https://udify.app/chatbot/ez1pf83HVV3JgWO4" style="width: 100%; height: 100%; min-height: 700px" frameborder="0" allow="microphone"></iframe>

# Fix the Chatbot to the bottom right corner of the webpage, 20 pixels from the bottom and right edges.

→

<iframe src="https://udify.app/chatbot/ez1pf83HVV3JgWO4" style="width: 100%; height: 100%; min-height: 700px; position: fixed; bottom: 20px; right: 20px;" frameborder="0" allow="microphone"></iframe>
```

This code fixes the Chatbot to the bottom right corner of the webpage, 20 pixels from the bottom and right edges.

## FAQ

**1. iFrame Content Not Displaying**

* Verify that the URL starts with HTTPS
* Check for typos in the `iframe` code
* Verify the embedded content complies with Wix's security policies

**2. iFrame Content is Cropped**

Modify the `width` and `height` percentage values in the `iframe` code to resolve content truncation issues.
