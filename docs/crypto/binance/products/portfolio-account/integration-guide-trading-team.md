---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/portfolio-account/integration-guide-trading-team
api_type: Guide
updated_at: 2026-11-26 18:30:24.004463
---

# Integration Guide — Trading Team

Complete Getting Started first: portfolio created, Trading Sub-accounts linked, API keys issued.

**Step 1 — Confirm your portfolio setup.** Call Portfolio Basic Info with your Manager Parent
Account key. Confirm `portfolioId`, portfolio name and denominated currency match your
configuration. If you manage multiple portfolios, the same call returns all Portfolio Accounts under
your Manager Parent Account. For a new portfolio, NAV is not yet calculated — expected until the
first daily cycle completes.

**Step 2 — Move capital to the Trading Sub-accounts.** Trading does not happen on the Portfolio
Account itself. Transfer assets from the Portfolio Account to its bound Trading Sub-accounts before
trading. Assets can move only between the Portfolio Account and its own sub-accounts; external
transfers and withdrawals are not permitted. Sub-accounts trade through the standard Binance spot,
margin and futures endpoints using their own API keys.

**Step 3 — Onboard investors.** Invite investors through the PA portal. The invitation binds the
investor to the Portfolio Account once accepted. No limit on investors per portfolio.

**Step 4 — Review subscription requests.** When an investor subscribes, their funds are frozen until
you approve or decline. Approval is a web portal action; the API lets you query the resulting
records. After approval, funds arrive in the Portfolio Account within approximately 1 hour, priced
at the applicable NAV. A brand-new portfolio must wait for its first daily cycle before
subscriptions can be processed.

**Step 5 — Monitor NAV and reconcile investor activity.** Poll Portfolio NAV Info for the NAV
series. NAV is struck daily between 00:00 and 04:00 UTC, so the latest value is always for the
previous day. There are no push notifications — schedule polling. Use Query Investor Operation
History for Trading Team V2 to retrieve completed subscription and redemption records for a specific
investor in a specific portfolio and reconcile against your own books.

**Step 6 — Plan liquidity for redemptions.** Investors redeem without trading team approval. Use
Redemption Calendar to see upcoming redemptions for the next 8 days, grouped by settlement date,
across all your portfolios. Move funds from the Trading Sub-accounts back into the Portfolio Account
before each settlement date. The system attempts each transfer daily from T+1 to the deadline;
insufficient balance causes a failed attempt and a retry the next day. If still unsettled at the
deadline the request fails and the investor must resubmit — keep the Portfolio Account funded.

**Step 7 — Manage investor API data sharing.** Use Change API Sharing Switch to enable or disable
investor access to portfolio-level data through the API, and API Sharing Status to confirm the
current setting. Changes take effect immediately.

---

# 集成指南 — 交易团队

请先完成快速开始：已创建投资组合、已关联交易子账户、已签发 API Key。

**第 1 步 — 确认投资组合设置。** 使用管理人母账户的 Key 调用投资组合基本信息接口，确认
`portfolioId`、投资组合名称和计价币种与您的配置一致。如果您管理多个投资组合，同一个调用会返回管理人母账户下的所有投资组合账户。对于新建的投资组合，净值尚未计算 — 在首次每日周期完成前属正常现象。

**第 2 步 — 将资金划转到交易子账户。**
交易不在投资组合账户本身进行。交易前，请将资产从投资组合账户划转到其绑定的交易子账户。资产只能在投资组合账户与其自有子账户之间流转，不允许对外转账或提现。子账户使用各自的 API
Key，通过标准的币安现货、杠杆和合约接口交易。

**第 3 步 — 邀请投资人。**
通过 PA 门户邀请投资人。投资人接受邀请后即被绑定到该投资组合账户。每个投资组合的投资人数量没有上限。

**第 4 步 — 审核申购请求。**
投资人申购后，其资金被冻结，直到您批准或拒绝。审批是网页端操作；API 可用于查询生成的记录。批准后，资金约 1 小时内到达投资组合账户，按适用净值定价。全新的投资组合必须等待首次每日周期完成后才能处理申购。

**第 5 步 — 监控净值并核对投资人活动。** 轮询投资组合净值信息接口获取净值序列。净值每天在 UTC
00:00 至 04:00 之间结算，因此最新值始终是前一天的。没有推送通知，请安排好轮询。使用查询投资人操作历史（适用于交易团队）V2 接口，获取指定投资人在指定投资组合下已完成的申购和赎回记录，并与自己的账簿核对。

**第 6 步 — 规划赎回流动性。**
投资人赎回无需交易团队审批。使用赎回日历查看未来 8 天内即将发生的赎回，按结算日分组，覆盖您所有的投资组合。请在每个结算日之前，把资金从交易子账户划回投资组合账户。系统从 T+1 到截止日每天尝试划转，余额不足会导致尝试失败并在次日重试。如果截止日仍未结算，请求失败，投资人需要重新提交 — 请保持投资组合账户资金充足。

**第 7 步 — 管理投资人 API 数据共享。**
使用修改 API 数据共享开关接口开启或关闭投资人通过 API 访问投资组合层面数据的权限，并使用查询 API 数据共享状态接口确认当前设置。修改立即生效。