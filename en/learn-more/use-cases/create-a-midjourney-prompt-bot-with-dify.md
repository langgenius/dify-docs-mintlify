# Create a MidJourney Prompt Bot with Dify

via [@op7418](https://twitter.com/op7418) on Twitter

I recently tried out a natural language programming tool called Dify, developed by [@goocarlos](https://twitter.com/goocarlos). It allows someone without coding knowledge to create a web application just by writing prompts. It even generates the API for you, making it easy to deploy your application on your preferred platform.

The application I created using Dify took me only 20 minutes, and the results were impressive. Without Dify, it might have taken me much longer to achieve the same outcome. The specific functionality of the application is to generate Midjourney prompts based on short input topics, assisting users in quickly filling in common Midjourney commands. In this tutorial, I will walk you through the process of creating this application to familiarize you with the platform.

Dify offers two types of applications: conversational applications similar to ChatGPT, which involve multi-turn dialogue, and text generation applications that directly generate text content with the click of a button. Since we want to create a Midjoureny prompt bot, we'll choose the text generator.

You can access Dify here: https://dify.ai/

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/b9e69dc45562f699ef2d6e5f8d71e7ce.png)

Once you've created your application, the dashboard page will display some data monitoring and application settings. Click on "Prompt Engineering" on the left, which is the main working page.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/936c786960ac4bf7936227c58b4754a4.png)

On this page, the left side is for prompt settings and other functions, while the right side provides real-time previews and usage of your created content. The prefix prompts are the triggers that the user inputs after each content, and they instruct the GPT model how to process the user's input information.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/488879620e712ce535106fd58d529bb7.jpeg)

Take a look at my prefix prompt structure: the first part instructs GPT to output a description of a photo in the following structure. The second structure serves as the template for generating the prompt, mainly consisting of elements like 'Color photo of the theme,' 'Intricate patterns,' 'Stark contrasts,' 'Environmental description,' 'Camera model,' 'Lens focal length description related to the input content,' 'Composition description relative to the input content,' and 'The names of four master photographers.' This constitutes the main content of the prompt. In theory, you can now save this to the preview area on the right, input the theme you want to generate, and the corresponding prompt will be generated.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/9c03412aa11d3542940e3bdcc0a85a4e.png)

You may have noticed the "\{{proportion\}}" and "\{{version\}}" at the end. These are variables used to pass user-selected information. On the right side, users are required to choose image proportions and model versions, and these two variables help carry that information to the end of the prompt. Let's see how to set them up.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/ca81600060ffdfb7ec2a6e3c72bd86d7.png)

Our goal is to fill in the user's selected information at the end of the prompt, making it easy for users to copy without having to rewrite or memorize these commands. For this, we use the variable function.

Variables allow us to dynamically incorporate the user's form-filled or selected content into the prompt. For example, I've created two variables: one represents the image proportion, and the other represents the model version. Click the "Add" button to create the variables.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/86d0eb832fd8457dc3cb2e5656f96425.jpeg)

After creation, you'll need to fill in the variable key and field name. The variable key should be in English. The optional setting means the field will be non-mandatory when the user fills it. Next, click "Settings" in the action bar to set the variable content.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/ac8ab15304f9f1ff5fa67e78726e101c.jpeg)

Variables can be of two types: text variables, where users manually input content, and select options where users select from given choices. Since we want to avoid manual commands, we'll choose the dropdown option and add the required choices.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/6a906ca7145c8c32bf9a72fc02b17c0f.png)

Now, let's use the variables. We need to enclose the variable key within double curly brackets {} and add it to the prefix prompt. Since we want the GPT to output the user-selected content as is, we'll include the phrase "Producing the following English photo description based on user input" in the prompt.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/dd064aee30a248ce62f4fb197096c38d.jpeg)

However, there's still a chance that GPT might modify our variable content. To address this, we can lower the diversity in the model selection on the right, reducing the temperature and making it less likely to alter our variable content. You can check the tooltips for other parameters' meanings.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/ea875bf33f674a39318e26b67e561e61.png)

With these steps, your application is now complete. After testing and ensuring there are no issues with the output, click the "Publish" button in the upper right corner to release your application. You and users can access your application through the publicly available URL. You can also customize the application name, introduction, icon, and other details in the settings.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/learn-more/use-cases/3f997d26023f1ee9bc8604eb2eb1cb6e.png)

That's how you create a simple AI application using Dify. You can also deploy your application on other platforms or modify its UI using the generated API. Additionally, Dify supports uploading your own data, such as building a customer service bot to assist with product-related queries. This concludes the tutorial, and a special thanks to @goocarlos for creating such a fantastic product.
