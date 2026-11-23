---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/open-platform/airdrop-creation
api_type: Guide
updated_at: 2026-11-23 18:30:00.581841
---

# How to Create an Airdrop Campaign on Binance Web3 Open Platform?

## Airdrop Campaign Overview

| **Owner** | **Step**               | **Description**                                  |
| --------- | ---------------------- | ------------------------------------------------ |
| Project   | Campaign preparation   | List your dApp and develop your API              |
|           | Campaign configuration | Set up airdrop campaign                          |
|           | Funds deposit          | Deposit campaign reward                          |
|           | Submit campaign        | Submit the campaign to Binance                   |
| Binance   | Campaign review        | Binance reviews the campaign setting and approve |
|           | Campaign launch        | Binance list campaign on Web3 Wallet             |

## Airdrop Campaign Tutorial

### Campaign preparation

- Develop API for the on-chain tasks, and register the API on Open Platform > Airdrop Campaign >
  Task Verification API
  - API specifications: [Doc](/products/web3-task-verification/apis)
  - API registration:
    - Click on the “+ Create New API” button

![create-new-api](/img/web3-dapp/create-new-api.png)

- Input the API Name and the API Pre-fix.<br/> API Name: Give your API an arbitrary name. It is an
  unused variable.<br/> API Pre-Fix: Initial segment of your API URL path. Please contact your dev
  in charge of the API development to get the API Pre-Fix.

![create-popup](/img/web3-dapp/create-popup.png)

### Campaign configuration

- **Start to create a new Airdrop:**
  - Click on the “+ Create Airdrop” button to create a new airdrop campaign.
  - Note: All settings can not be changed after you submit the airdrop campaign, so please make sure
    and re-check after you finish the configuration.

![create-airdrop](/img/web3-dapp/create-airdrop.png)

- **Step1: Basic information setting**
  - Airdrop Name: the title of this airdrop campaign which can be seen by users. E.g.: Binance 1M$
    BNB Airdrop!
  - Airdrop Period(UTC): the airdrop campaign start date and time, and end date and time\
     Please set up a test campaign with an immediate start date first for Binance Wallet team to
    test and sign off for you to set up the official campaign again for the launch. The test
    campaign should have everything else ready and equal to your formal campaign but the actual
    launch date and the reward amount.
  - Airdrop Rules Link: the page links to a page to introduce the campaign rules.
  - Airdrop Rules Highlight: the highlights of this airdrop campaign mechanism. In the campaign
    rules link, the project should include the general background of this campaign, the
    pre-requirement for users to participate, the task design with as precise as possible details
    for example on which chain for how many tokens etc, and the eligibility criteria for users to
    receive reward. A tutorial is recommended as the last section of this page to increase the task
    completion rate.
  - Campaign chain: the campaign chain, and rewards claim chain. Please note these two chains will
    have to be the same so that your users can successfully claim the reward later.
  - Total rewards: the total reward description in the sum of this airdrop campaign.
  - Campaign rewards type: 2 types supported
  - Token (Pending TGE): applicable for tokens has not launched now.
  - Token (Completed TGE): applicable for tokens launched already.

![campaign-form](/img/web3-dapp/campaign-form.png)

- Token (Pending TGE) application flow:
  - This process is only needed when you select the Token (Pending TGE) type of reward.
  - Click on the “Contact” button and fill in the necessary information. And then wait for Binance’s
    approval. Alternatively, you can directly reach out and share your Campaign ID with your POC at
    Binance Wallet to whitelist your Campaign ID and thus you can proceed for the next step.

![campaign-form-2-1](/img/web3-dapp/campaign-form-2-1.png)

- **Step2: Eligibility setting**
  - Anti-Sybil Level setting：
    - Level 1: 1 wallet address can join the campaign once, and claim rewards once (once the wallet
      address completes tasks).

    - Level 2: 1 Binance user (identified by Binance account UID) can join the campaign once, and
      claim rewards once.

    - Level 3: 1 real users (identified by Binance account UID, and excluded batch registration
      user) can join the campaign once, and claim rewards once.

    - Please make sure to have a consistent description in your rules page regarding campaign
      participation eligibility.

  - Restricted Countries / Regions for Participants
    - Users from the countries/regions you selected will be blocked when they try to join your
      airdrop campaign.

    - Please select based on your product’s geo-blocking rules.

![campaign-form-2-2](/img/web3-dapp/campaign-form-2-2.png)

- **Step3: Task/Reward setting**
  - Select templates:
    - Select an option based on how many dApps will be included in this campaign:
      - Single dApp: you will only ask users to interact with one dApp to complete the on-chain
        tasks

      - Multiple dApps: you will ask users to interact with multiple dApps to complete different
        on-chain tasks

![campaign-form-3-1](/img/web3-dapp/campaign-form-3-1.png)

- Select your Dapp:
  - Click the “Add dApp” button to select your dApp

  - _Note: you only can select dApps listed on Binance. If you can not find your dApp, please submit
    your dApp listing application first._

![campaign-form-3-2](/img/web3-dapp/campaign-form-3-2.png)

- Add task
  - 2 Task Type: 
    - On-chain task: requires users to execute some on-chain actions.

    - Social task: require users to follow X account / Repost X post.

* On-chain task: 
  - Task Title: a summary text for the task. E.g., Stake task

  - Task Tutorial Link: a page link redirects to the task tutorials. It is highly recommended to add
    a tutorial for on-chain tasks.
    - Please input the full URL including “https\://”

  - dApp URL for the task: the link user can finish the task. 
    - Please input the full URL including “https\://”

  - Task description: a detailed description of the task content. Please make sure your task
    description contains precise details: on which chain, for how many tokens and avoid confusions
    regarding the token number and values etc. A detailed and precise will greatly help you avoid
    unnecessary customer support pressure.
    - A good example: Swap 2 $BNB token on BSC chain. (Assume the current price is $700/BNB)
    - A bad example: Swap 1400 $BNB.
      - No instruction on which chain
      - Confusion about 1400 dollar worth of BNB or 1400 BNB
      - Token price is often fluctuating. To insure your API can successfully verify the task
        completion status over the campaign period, we require projects to specify the number of
        tokens instead of dollar value of tokens.

  - Task verification: select your API registered and input your task ID. 
    - If you can not find your API, please go to Open Platform > Airdrop Campaign > Task Verify API
      to register your API first.

    - Please ensure the task ID you use is provided and confirmed by your dev. Task ID is a string
      identifier used to represent a specific task within the `task` parameter of the API.

![new-task](/img/web3-dapp/new-task.png)

- Social task
  - Social Channel: now only X is supported.

  - Task Content: 
    - Follow an X account: require users to follow an X account.
      - Need to input X username. Please don’t include @ in the username.

    - Repost an X post: require users to repost an X post. 
      - Need to input the X post link. Please make sure to include https :// in the link.

      - The repost content is required to be related with Binance Wallet and please do have your POC
        at Binance Wallet preview and approve the content in advance.

      - If your project would like to have users to repost about the on-going campaign announcement,
        please reach out to your POC at Binance Wallet and synchronize the timeline and to-dos in
        advance so that your link can be updated in time once your post and campaign are live.

![social-task](/img/web3-dapp/social-task.png)

- **Reward:**
  - **3 Reward Type:**
    - Task Reward: for users who complete the task.
      - Enable the reward by toggling on the “Enable Task Reward” toggle.

![reward-type](/img/web3-dapp/reward-type.png)

- DApp Completion Reward: for users who complete all tasks under a dApp. Only available when the
  “Multiple DApps” template is selected.
  - Enable the reward by toggling on the “DApp Completion Reward” toggle.

![reward-toggle](/img/web3-dapp/reward-toggle.png)

- Airdrop Completion Reward: for users who complete all tasks under a dApp. 
  - Enable the reward by toggling on the “Airdrop Completion Reward” toggle.

![completion-reward](/img/web3-dapp/completion-reward.png)

- **Reward Setting:** 
  - All the 3 Reward types share the same setting. The setting is different based on the Rewards
    Mechanism you selected.

| Rewards Mechanism             | Description                                                                                                                      | Settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FCFS (First come first serve) | Users who complete the task first to get a share of the reward, which is a fixed amount.                                         | • Rewards Type: Only can select Token (Completed TGE)<br/>• Chain: the same with your Campaign chain<br/>• Number of Winners: the reward share amount<br/>• Token Name:<br/> - If the token is a native token, then select from the dropdown list<br/> - If the token is not a native token, then input the token smart contract address<br/>• Reward per Winner: the amount of tokens for each winner<br/> • Please do not ask all the users to verify their task completion status at once - e.g. verify your holding status on January 1 23:59 UTC - to avoid unnecessary API queries crash from your side |
| Shared                        | Users who completed the task split the reward pool equally, the reward amount is the Total Reward / User who completed the task. | • Rewards Type: Can select both of the 2 token types<br/>• Chain: same with FCFS<br/>• Number of Winners: the maximum number of users who can share the reward pool<br/>• Token Name: same with FCFS<br/>• Total Reward: the total reward amount                                                                                                                                                                                                                                                                                                                                                              |
| Lucky Draw                    | Select a certain amount of users from all users who complete the task                                                            | • Rewards Type: can select both of the 2 token types<br/>• Chain: same with FCFS<br/>• Number of Winners: the number of users will be selected<br/>• Token Name: same with FCFS<br/>• Reward per Winner: the reward amount for each user                                                                                                                                                                                                                                                                                                                                                                      |

![edit-dapp-reward](/img/web3-dapp/edit-dapp-reward.png)

- After you finish the setting, click on the “Submit” button and notify your campaign POC at Binance
  Wallet to check your submission and kick off review and testing process.

![submit-campaign](/img/web3-dapp/submit-campaign.png)

- **Step4: Deposit the rewards**
  - For campaigns including Token (Completed TGE), click the “Deposit” button to finish the reward
    deposit. Please do note that incompletion of deposit will lead to failure of campaign submission
    and thus potential delays of your campaign launch, so please do align with your finance team in
    advance.
  - For campaigns only with Token (Pending TGE), you don’t need to deposit.

![deposit-reward](/img/web3-dapp/deposit-reward.png)

- **Step5: Submit airdrop campaign**
  - Click on the submit button to submit the campaign for Binance review.
    - Usually, Binance needs 7 working days to finish the campaign review.

    - If the campaign is approved: you can find the campaign status in Waiting Online/ Online
      status. After that, your campaign will be listed on Web3 Wallet.

    - If the campaign is rejected: you’ll see the campaign in rejected status. And you can modify
      the campaign and resubmit.

![campaign-submit](/img/web3-dapp/campaign-submit.png)

---

# How to Create an Airdrop Campaign on Binance Web3 Open Platform?

## Airdrop Campaign Overview

| **Owner** | **Step**               | **Description**                                  |
| --------- | ---------------------- | ------------------------------------------------ |
| Project   | Campaign preparation   | List your dApp and develop your API              |
|           | Campaign configuration | Set up airdrop campaign                          |
|           | Funds deposit          | Deposit campaign reward                          |
|           | Submit campaign        | Submit the campaign to Binance                   |
| Binance   | Campaign review        | Binance reviews the campaign setting and approve |
|           | Campaign launch        | Binance list campaign on Web3 Wallet             |

## Airdrop Campaign Tutorial

### Campaign preparation

- Develop API for the on-chain tasks, and register the API on Open Platform > Airdrop Campaign >
  Task Verification API
  - API specifications: [Doc](/products/web3-task-verification/apis)
  - API registration:
    - Click on the “+ Create New API” button

![create-new-api](/img/web3-dapp/create-new-api.png)

- Input the API Name and the API Pre-fix.<br/> API Name: Give your API an arbitrary name. It is an
  unused variable.<br/> API Pre-Fix: Initial segment of your API URL path. Please contact your dev
  in charge of the API development to get the API Pre-Fix.

![create-popup](/img/web3-dapp/create-popup.png)

### Campaign configuration

- **Start to create a new Airdrop:**
  - Click on the “+ Create Airdrop” button to create a new airdrop campaign.
  - Note: All settings can not be changed after you submit the airdrop campaign, so please make sure
    and re-check after you finish the configuration.

![create-airdrop](/img/web3-dapp/create-airdrop.png)

- **Step1: Basic information setting**
  - Airdrop Name: the title of this airdrop campaign which can be seen by users. E.g.: Binance 1M$
    BNB Airdrop!
  - Airdrop Period(UTC): the airdrop campaign start date and time, and end date and time\
     Please set up a test campaign with an immediate start date first for Binance Wallet team to
    test and sign off for you to set up the official campaign again for the launch. The test
    campaign should have everything else ready and equal to your formal campaign but the actual
    launch date and the reward amount.
  - Airdrop Rules Link: the page links to a page to introduce the campaign rules.
  - Airdrop Rules Highlight: the highlights of this airdrop campaign mechanism. In the campaign
    rules link, the project should include the general background of this campaign, the
    pre-requirement for users to participate, the task design with as precise as possible details
    for example on which chain for how many tokens etc, and the eligibility criteria for users to
    receive reward. A tutorial is recommended as the last section of this page to increase the task
    completion rate.
  - Campaign chain: the campaign chain, and rewards claim chain. Please note these two chains will
    have to be the same so that your users can successfully claim the reward later.
  - Total rewards: the total reward description in the sum of this airdrop campaign.
  - Campaign rewards type: 2 types supported
  - Token (Pending TGE): applicable for tokens has not launched now.
  - Token (Completed TGE): applicable for tokens launched already.

![campaign-form](/img/web3-dapp/campaign-form.png)

- Token (Pending TGE) application flow:
  - This process is only needed when you select the Token (Pending TGE) type of reward.
  - Click on the “Contact” button and fill in the necessary information. And then wait for Binance’s
    approval. Alternatively, you can directly reach out and share your Campaign ID with your POC at
    Binance Wallet to whitelist your Campaign ID and thus you can proceed for the next step.

![campaign-form-2-1](/img/web3-dapp/campaign-form-2-1.png)

- **Step2: Eligibility setting**
  - Anti-Sybil Level setting：
    - Level 1: 1 wallet address can join the campaign once, and claim rewards once (once the wallet
      address completes tasks).

    - Level 2: 1 Binance user (identified by Binance account UID) can join the campaign once, and
      claim rewards once.

    - Level 3: 1 real users (identified by Binance account UID, and excluded batch registration
      user) can join the campaign once, and claim rewards once.

    - Please make sure to have a consistent description in your rules page regarding campaign
      participation eligibility.

  - Restricted Countries / Regions for Participants
    - Users from the countries/regions you selected will be blocked when they try to join your
      airdrop campaign.

    - Please select based on your product’s geo-blocking rules.

![campaign-form-2-2](/img/web3-dapp/campaign-form-2-2.png)

- **Step3: Task/Reward setting**
  - Select templates:
    - Select an option based on how many dApps will be included in this campaign:
      - Single dApp: you will only ask users to interact with one dApp to complete the on-chain
        tasks

      - Multiple dApps: you will ask users to interact with multiple dApps to complete different
        on-chain tasks

![campaign-form-3-1](/img/web3-dapp/campaign-form-3-1.png)

- Select your Dapp:
  - Click the “Add dApp” button to select your dApp

  - _Note: you only can select dApps listed on Binance. If you can not find your dApp, please submit
    your dApp listing application first._

![campaign-form-3-2](/img/web3-dapp/campaign-form-3-2.png)

- Add task
  - 2 Task Type: 
    - On-chain task: requires users to execute some on-chain actions.

    - Social task: require users to follow X account / Repost X post.

* On-chain task: 
  - Task Title: a summary text for the task. E.g., Stake task

  - Task Tutorial Link: a page link redirects to the task tutorials. It is highly recommended to add
    a tutorial for on-chain tasks.
    - Please input the full URL including “https\://”

  - dApp URL for the task: the link user can finish the task. 
    - Please input the full URL including “https\://”

  - Task description: a detailed description of the task content. Please make sure your task
    description contains precise details: on which chain, for how many tokens and avoid confusions
    regarding the token number and values etc. A detailed and precise will greatly help you avoid
    unnecessary customer support pressure.
    - A good example: Swap 2 $BNB token on BSC chain. (Assume the current price is $700/BNB)
    - A bad example: Swap 1400 $BNB.
      - No instruction on which chain
      - Confusion about 1400 dollar worth of BNB or 1400 BNB
      - Token price is often fluctuating. To insure your API can successfully verify the task
        completion status over the campaign period, we require projects to specify the number of
        tokens instead of dollar value of tokens.

  - Task verification: select your API registered and input your task ID. 
    - If you can not find your API, please go to Open Platform > Airdrop Campaign > Task Verify API
      to register your API first.

    - Please ensure the task ID you use is provided and confirmed by your dev. Task ID is a string
      identifier used to represent a specific task within the `task` parameter of the API.

![new-task](/img/web3-dapp/new-task.png)

- Social task
  - Social Channel: now only X is supported.

  - Task Content: 
    - Follow an X account: require users to follow an X account.
      - Need to input X username. Please don’t include @ in the username.

    - Repost an X post: require users to repost an X post. 
      - Need to input the X post link. Please make sure to include https :// in the link.

      - The repost content is required to be related with Binance Wallet and please do have your POC
        at Binance Wallet preview and approve the content in advance.

      - If your project would like to have users to repost about the on-going campaign announcement,
        please reach out to your POC at Binance Wallet and synchronize the timeline and to-dos in
        advance so that your link can be updated in time once your post and campaign are live.

![social-task](/img/web3-dapp/social-task.png)

- **Reward:**
  - **3 Reward Type:**
    - Task Reward: for users who complete the task.
      - Enable the reward by toggling on the “Enable Task Reward” toggle.

![reward-type](/img/web3-dapp/reward-type.png)

- DApp Completion Reward: for users who complete all tasks under a dApp. Only available when the
  “Multiple DApps” template is selected.
  - Enable the reward by toggling on the “DApp Completion Reward” toggle.

![reward-toggle](/img/web3-dapp/reward-toggle.png)

- Airdrop Completion Reward: for users who complete all tasks under a dApp. 
  - Enable the reward by toggling on the “Airdrop Completion Reward” toggle.

![completion-reward](/img/web3-dapp/completion-reward.png)

- **Reward Setting:** 
  - All the 3 Reward types share the same setting. The setting is different based on the Rewards
    Mechanism you selected.

| Rewards Mechanism             | Description                                                                                                                      | Settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FCFS (First come first serve) | Users who complete the task first to get a share of the reward, which is a fixed amount.                                         | • Rewards Type: Only can select Token (Completed TGE)<br/>• Chain: the same with your Campaign chain<br/>• Number of Winners: the reward share amount<br/>• Token Name:<br/> - If the token is a native token, then select from the dropdown list<br/> - If the token is not a native token, then input the token smart contract address<br/>• Reward per Winner: the amount of tokens for each winner<br/> • Please do not ask all the users to verify their task completion status at once - e.g. verify your holding status on January 1 23:59 UTC - to avoid unnecessary API queries crash from your side |
| Shared                        | Users who completed the task split the reward pool equally, the reward amount is the Total Reward / User who completed the task. | • Rewards Type: Can select both of the 2 token types<br/>• Chain: same with FCFS<br/>• Number of Winners: the maximum number of users who can share the reward pool<br/>• Token Name: same with FCFS<br/>• Total Reward: the total reward amount                                                                                                                                                                                                                                                                                                                                                              |
| Lucky Draw                    | Select a certain amount of users from all users who complete the task                                                            | • Rewards Type: can select both of the 2 token types<br/>• Chain: same with FCFS<br/>• Number of Winners: the number of users will be selected<br/>• Token Name: same with FCFS<br/>• Reward per Winner: the reward amount for each user                                                                                                                                                                                                                                                                                                                                                                      |

![edit-dapp-reward](/img/web3-dapp/edit-dapp-reward.png)

- After you finish the setting, click on the “Submit” button and notify your campaign POC at Binance
  Wallet to check your submission and kick off review and testing process.

![submit-campaign](/img/web3-dapp/submit-campaign.png)

- **Step4: Deposit the rewards**
  - For campaigns including Token (Completed TGE), click the “Deposit” button to finish the reward
    deposit. Please do note that incompletion of deposit will lead to failure of campaign submission
    and thus potential delays of your campaign launch, so please do align with your finance team in
    advance.
  - For campaigns only with Token (Pending TGE), you don’t need to deposit.

![deposit-reward](/img/web3-dapp/deposit-reward.png)

- **Step5: Submit airdrop campaign**
  - Click on the submit button to submit the campaign for Binance review.
    - Usually, Binance needs 7 working days to finish the campaign review.

    - If the campaign is approved: you can find the campaign status in Waiting Online/ Online
      status. After that, your campaign will be listed on Web3 Wallet.

    - If the campaign is rejected: you’ll see the campaign in rejected status. And you can modify
      the campaign and resubmit.

![campaign-submit](/img/web3-dapp/campaign-submit.png)