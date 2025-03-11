# Subscription Management

### Upgrading Dify Team Subscription

Team owners and administrators can upgrade the team subscription plan. Click the **"Upgrade"** button in the upper right corner of the Dify team homepage, select an appropriate package, and complete the payment to upgrade the team's subscription.

### Managing Dify Team Subscription

After subscribing to Dify's paid services (Professional or Team plan), team owners and administrators can navigate to **"Settings"** → **"Billing"** to manage the team's billing and subscription details.

On the billing page, you can view the usage statistics for various team resources.

![Team billing management](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/07eb0d03a33e2e01df44dbf3cf241f14.png)

### Frequently Asked Questions

#### 1. How to upgrade/downgrade the team plan or cancel a subscription?

Team owners and administrators can navigate to **Settings** → **Billing**, then click on **Manage billing and subscription** to change the subscription plan.

* Upgrading from Professional to Team plan requires paying the difference for the current month and takes effect immediately.
* Downgrading from Team to Professional plan takes effect immediately.

![Changing the paid plan](https://assets-docs.dify.ai/dify-enterprise-mintlify/en/guides/management/c572ba8806b41eb6564fc658d3d8124b.jpeg)

Upon cancellation of the subscription plan, **the team will automatically transition to the Sandbox/Free plan at the end of the current billing cycle**. Subsequently, any team members and resources exceeding the Sandbox/Free plan limitations will become inaccessible.

#### 2. What changes will occur to the team's available resources after upgrading the subscription plan?

| Resource                                                                     | Free      | Professional   | Team            |
| ---------------------------------------------------------------------------- | --------- | -------------- | --------------- |
| Team member limit                                                            | 1         | 3              | Unlimited       |
| Application limit                                                            | 10        | 50             | Unlimited       |
| Vector space capacity                                                        | 5MB       | 200MB          | 1GB             |
| [Marked replies](https://docs.dify.ai/guides/biao-zhu/logs) for applications | 10        | 2000           | 5000            |
| Document uploads for knowledge base                                          | 50        | 500            | 1000            |
| OpenAI conversation quota                                                    | 200 total | 5000 per month | 10000 per month |

Note:

* When upgrading from Free to Professional, all resources are increased as shown in the table.
* When upgrading from Professional to Team, resources are further expanded, with some becoming unlimited.

After upgrading the subscription plan:

* The OpenAI conversation quota will be reset to the new limit for the current billing cycle.
* Previously used computational resources (e.g., vector space usage, document uploads) will not be reset or removed.

#### 3. What if I forget to renew subscription on time?

If you forget to renew your subscription, the team will automatically downgrade to the Sandbox/Free version. Except for the team owner, others will not be able to continue accessing the team. Excess computational resources within the team (such as documents, vector space, etc.) will also be locked.

#### 4. Will deleting the team owner's account affect the team?

A team needs to be bound to one team owner. If the team ownership is not transferred to another team member in time, all data of the current team will be deleted along with the owner's account.

#### 5. What are the differences between the subscription versions?

For a detailed feature comparison, please refer to the [Dify pricing](https://dify.ai/pricing).
