---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/portfolio-account/core-concepts
api_type: Guide
updated_at: 2026-11-27 18:30:11.136974
---

# Core Concepts

## NAV and pricing

NAV is calculated once per day, between 00:00 and 04:00 UTC, for the preceding UTC day. There is no
intraday NAV strike.

Subscriptions and redemptions are priced using the most recently completed daily NAV. A brand-new
portfolio must complete its first daily cycle before any subscription can be processed.

## Subscriptions

1. Investor submits a subscription for an amount in the portfolio's denominated currency, at or
   above the portfolio minimum
2. Funds are frozen in the investor's account
3. Trading team approves or declines — a web portal action
4. On approval, funds arrive in the Portfolio Account within approximately 1 hour, priced at the
   applicable NAV, and allocations are issued

allocations issued = amount ÷ `navPerAllocation` at the strike

## Redemptions and settlement

Redemptions do not require trading team approval. The system processes them automatically, subject
to lock-up and settlement terms.

The investor submits the number of allocations to redeem and a redemption time expressed as T+N days
from the request date, where T+N is the portfolio's configured settlement window.

| Stage                   | Behaviour                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------- |
| After approval          | System attempts the transfer daily, from T+1 up to and including the selected settlement date         |
| Attempt succeeds        | Request becomes `COMPLETED`; funds land in the investor's master account spot wallet                  |
| Attempt fails           | Typically insufficient Portfolio Account balance. System retries the next day                         |
| Not settled by deadline | Request becomes `FAILED`. Allocations remain in the portfolio; the investor must submit a new request |

Trading teams must keep the Portfolio Account funded ahead of settlement dates. Use the Redemption
Calendar endpoint to see upcoming obligations.

## Fees

| Fee             | Calculation                                                        | Timing                     |
| --------------- | ------------------------------------------------------------------ | -------------------------- |
| Management fee  | daily AUM × annual rate ÷ 365                                      | Accrued and deducted daily |
| Performance fee | (current NAV − average entry NAV) × performance rate × allocations | Crystallises on redemption |

## Lock-up vs settlement window

Two different questions:

|                   | Controls                                              | Set by       | Range                         |
| ----------------- | ----------------------------------------------------- | ------------ | ----------------------------- |
| Lock-up period    | When an investor may redeem                           | Trading team | e.g. 30 days, 90 days, 1 year |
| Settlement window | How long the payout takes once redemption is approved | Trading team | T+1 to T+14                   |

During lock-up, redemption is unavailable and the UI shows "Redemption unavailable until [date]".

## Investor data visibility

Investor-side endpoints expose the investor's own position and the portfolio's risk profile as
ratios. They never return portfolio total net assets, total allocations outstanding, or any other
investor's data.

| Data                                           | Investor visibility                   |
| ---------------------------------------------- | ------------------------------------- |
| `navPerAllocation` (daily and realtime)        | ✅ Visible                            |
| Investor's own allocations and equity          | ✅ Visible                            |
| Investor's own subscription/redemption history | ✅ Visible                            |
| Portfolio risk metrics (ratios and multiples)  | ✅ Visible, subject to sharing switch |
| Portfolio total net assets                     | ❌ Not returned                       |
| Allocations outstanding                        | ❌ Not returned                       |
| Other investors' positions or identities       | ❌ Not returned                       |

## API data sharing switch

Trading teams control whether investors can query portfolio-level data through the API.

| Switch state      | Investor-side API behaviour                                                                        |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| `enabled = true`  | Investor-side endpoints return data normally                                                       |
| `enabled = false` | Portfolio-level endpoints return an error indicating the trading team has not enabled data sharing |

---

# 核心概念

## 净值与定价

净值每天计算一次，在 UTC 00:00 至 04:00 之间，针对前一个 UTC 日。不存在日内净值结算。

申购和赎回按最近一次完成的每日净值定价。全新的投资组合必须完成首次每日计算周期后，才能处理任何申购。

## 申购

1. 投资人以投资组合的计价币种提交申购金额，金额不得低于投资组合的最低投资额
2. 资金在投资人账户中被冻结
3. 交易团队批准或拒绝 — 网页端操作
4. 批准后，资金约 1 小时内到达投资组合账户，按适用净值定价并发行份额

发行份额 = 金额 ÷ 结算时的 `navPerAllocation`

## 赎回与结算

赎回无需交易团队审批，由系统自动处理，受锁定期和结算条款约束。

投资人提交要赎回的份额数量，以及以申请日起算的 T+N 天表示的赎回时间，其中 T+N 在投资组合配置的结算窗口之内。

| 阶段           | 行为                                                              |
| -------------- | ----------------------------------------------------------------- |
| 审批之后       | 系统每日尝试划转，从 T+1 开始，直到所选结算日（含当日）           |
| 尝试成功       | 请求变为 `COMPLETED`；资金到达投资人主账户的现货钱包              |
| 尝试失败       | 通常是投资组合账户余额不足，系统次日重试                          |
| 截止日仍未结算 | 请求变为 `FAILED`。份额仍保留在投资组合中，投资人需要重新提交请求 |

交易团队必须在结算日之前为投资组合账户备足资金。可通过赎回日历接口查看即将到期的赎回义务。

## 费用

| 费用   | 计算方式                                     | 时点           |
| ------ | -------------------------------------------- | -------------- |
| 管理费 | 每日 AUM × 年化费率 ÷ 365                    | 每日计提并扣除 |
| 业绩费 | （当前净值 − 平均入场净值）× 业绩费率 × 份额 | 赎回时结晶     |

## 锁定期与结算窗口

这是两个不同的问题：

|          | 控制内容                   | 设置方   | 范围                    |
| -------- | -------------------------- | -------- | ----------------------- |
| 锁定期   | 投资人何时可以赎回         | 交易团队 | 例如 30 天、90 天、1 年 |
| 结算窗口 | 赎回获批后到账需要多长时间 | 交易团队 | T+1 至 T+14             |

锁定期内不可赎回，界面会显示 "Redemption unavailable until [date]"。

## 投资人数据可见性

投资人侧接口只暴露投资人自身的持仓，以及以比率形式呈现的投资组合风险画像，不会返回投资组合总净资产、已发行份额总数或其他任何投资人的数据。

| 数据                             | 投资人可见性            |
| -------------------------------- | ----------------------- |
| `navPerAllocation`（每日及实时） | ✅ 可见                 |
| 投资人自身的份额与权益           | ✅ 可见                 |
| 投资人自身的申购/赎回历史        | ✅ 可见                 |
| 投资组合风险指标（比率和倍数）   | ✅ 可见，受共享开关控制 |
| 投资组合总净资产                 | ❌ 不返回               |
| 已发行份额总数                   | ❌ 不返回               |
| 其他投资人的持仓或身份           | ❌ 不返回               |

## API 数据共享开关

交易团队控制投资人能否通过 API 查询投资组合层面的数据。

| 开关状态          | 投资人侧 API 行为                                      |
| ----------------- | ------------------------------------------------------ |
| `enabled = true`  | 投资人侧接口正常返回数据                               |
| `enabled = false` | 投资组合层面的接口返回错误，提示交易团队未开启数据共享 |