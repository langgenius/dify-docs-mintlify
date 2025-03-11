# 1.2 Import Data from Website

The knowledge base supports crawling content from public web pages using third-party tools such as [Jina Reader](https://jina.ai/reader/) and [Firecrawl](https://www.firecrawl.dev/), parsing it into Markdown content, and importing it into the knowledge base.

{% hint style="info" %}
​[Firecrawl](https://www.firecrawl.dev/) and [Jina Reader](https://jina.ai/reader/) are both open-source web parsing tools that can convert web pages into clean Markdown format text that is easy for LLMs to recognize, while providing easy-to-use API services.
{% endhint %}

The following sections will introduce the usage methods for Firecrawl and Jina Reader respectively.

### Firecrawl <a href="#how-to-configure" id="how-to-configure"></a>

#### **1. Configure Firecrawl API credentials**

Click on the avatar in the upper right corner, then go to the **DataSource** page, and click the **Configure** button next to Firecrawl.

![Configuring Firecrawl credentials](https://assets-docs.dify.ai/2024/12/d468cf996f591b4b2bd0ffb5de62bad4.png)

Log in to the [Firecrawl website](https://www.firecrawl.dev/) to complete registration, get your API Key, and then enter and save it in Dify.

![Get the API Key and save it in Dify](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRncMhlfeYTrpujwzDIqw%2Fuploads%2FtAwcLoAYT1A2v12pfJC3%2Fimage.png?alt=media&token=3b5b784f-2808-431f-8595-2638d038c190)

#### 2. Scrape target webpage

On the knowledge base creation page, select **Sync from website**, choose Firecrawl as the provider, and enter the target URL to be crawled.

The configuration options include: Whether to crawl sub-pages, Page crawling limit, Page scraping max depth, Excluded paths, Include only paths, and Content extraction scope. After completing the configuration, click **Run** to preview the parsed pages.

![Execute scraping](https://assets-docs.dify.ai/2024/12/3e63b4ced9770e21d5132c3aa8e5d2de.png)

#### 3. Review import results

After importing the parsed text from the webpage, it is stored in the knowledge base documents. View the import results and click **Add URL** to continue importing new web pages.

***

### Jina Reader

#### 1. Configuring Jina Reader Credentials

Click on the avatar in the upper right corner, then go to the **DataSource** page, and click the **Configure** button next to Jina Reader.

![Configuring Jina Reader](https://assets-docs.dify.ai/2024/12/28b37f9b36fe808b2d3302c48fce5ea3.png)

Log in to the [Jina Reader website](https://jina.ai/reader/), complete registration, obtain the API Key, then fill it in and save.

#### 2. Using Jina Reader to Crawl Web Content

On the knowledge base creation page, select **Sync from website**, choose Jina Reader as the provider, and enter the target URL to be crawled.

![Web crawling configuration ](https://assets-docs.dify.ai/2024/12/f9170b2a2ab1be94bc85ff3ed3c3e723.png)

Configuration options include: whether to crawl subpages, maximum number of pages to crawl, and whether to use sitemap for crawling. After completing the configuration, click the **Run** button to preview the page links to be crawled.

![Executing the crawl process](https://assets-docs.dify.ai/2024/12/a875f21a751551c03109c76308c577ee.png)

After importing the parsed text from web pages into the knowledge base, you can review the imported results in the documents section. To add more web pages, click the **Add URL** button on the right to continue importing new pages.

![Importing parsed web text into the knowledge base](https://assets-docs.dify.ai/2024/12/03494dc3c882ac1c74b464ea931e2533.png)

After crawling is complete, the content from the web pages will be incorporated into the knowledge base.
