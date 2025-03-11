# Text Generator Application

The text generation application is an application that automatically generates high-quality text according to the prompts provided by the user. It can generate various types of text, such as article summaries, translations, etc.

Text generation applications support the following features:

1. Run it once.
2. Run in batches.
3. Save the run results.
4. Generate more similar results.

Let's introduce them separately.

### Run it once

Enter the query content, click the run button, and the result will be generated on the right, as shown in the following figure:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/4c5380cf71066d933082f7c30deacb01.png)

In the generated results section, click the "Copy" button to copy the content to the clipboard. Click the "Save" button to save the content. You can see the saved content in the "Saved" tab. You can also "like" and "dislike" the generated content.

### Run in batches

Sometimes, we need to run an application many times. For example: There is a web application that can generate articles based on topics. Now we want to generate 100 articles on different topics. Then this task has to be done 100 times, which is very troublesome. Also, you have to wait for one task to complete before starting the next one.

In the above scenario, the batch operation function is used, which is convenient to operate (enter the theme into a `csv` file, only need to be executed once), and also saves the generation time (multiple tasks run at the same time). The usage is as follows:

#### Step 1 Enter the batch run page

Click the "Run Batch" tab to enter the batch run page.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/c8381ab7fad14a54c86835dc4b1b6b5d.png)

#### Step 2 Download the template and fill in the content

Click the **"Download the template here"** button to obtain the template file. Edit the file and fill in the required content, then save it as a `.csv` file. Finally, upload the completed file back to Dify.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/bae4859c5cb7404ce901b7979237bb93.png)

#### Step 3 Upload the file and run

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/fc84f62f41c12e14ff85b29e6bf43d27.png)

If you need to export the generated content, you can click the download "button" in the upper right corner to export as a `csv` file.

**Note:** The encoding of the uploaded `csv` file must be `Unicode` encoding. Otherwise, the result will fail. Solution: When exporting to a `csv` file with Excel, WPS, etc., select `Unicode` for encoding.

### Save run results

Click the "Save" button below the generated results to save the running results. In the "Saved" tab, you can see all saved content.

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/3cdd15e87aa1f1aae9f6abadb0f16d1f.png)

### Generate more similar results

If the "More like this" function is turned on the App's Orchestrate page,clicking the "More like this" button in the web application generates content similar to the current result. As shown below:

![](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/application-publishing/launch-your-webapp-quickly/65fb111d8e89a8f7b761859265e42f0a.png)
