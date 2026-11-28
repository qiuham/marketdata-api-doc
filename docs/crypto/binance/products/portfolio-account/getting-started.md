---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/portfolio-account/getting-started
api_type: Guide
updated_at: 2026-11-28 18:29:14.509933
---

# Getting Started

This section walks a trading team through setting up a Portfolio Account and making its first API
calls. On completion the Portfolio Account will be created, Trading Sub-accounts linked, and API
keys ready.

## Prerequisites

Portfolio Account is available to institutional trading teams that have completed Binance KYB entity
verification. Availability also depends on your jurisdiction and the Binance entity you are
onboarded under.

To begin onboarding, contact your VIP Account Manager or submit the form on the Portfolio Account
landing page. Binance will review the application and enable Portfolio Account on your Manager
Parent Account.

## Step 1 — Create a Portfolio Account

Create the Portfolio Account from the Manager Parent Account. Each Portfolio Account represents one
strategy; a Manager Parent Account can hold up to 5.

Required at creation: name, denominated currency, settlement window, management fee, performance
fee. Optional, can be added later: minimum investment, lock-up period, strategy type, strategy
description.

The settlement window defaults to T+1 and can be set up to T+14.

These terms become locked for existing investors once they subscribe. Confirm them before inviting
investors.

## Step 2 — Set up Trading Sub-accounts

Each Portfolio Account comes with 5 Trading Sub-accounts by default. This is where the team executes
trades. Additional sub-accounts can be requested through your VIP Account Manager.

## Step 3 — Create API keys

All Portfolio Account endpoints require signed requests.

| Key issued on                                                 | Used for                                                                                                           |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Manager Parent Account (Portfolio Account permission enabled) | All trading-team endpoints: portfolio info, NAV history, investor history, redemption calendar, API sharing switch |
| Each Trading Sub-account                                      | Trading, via standard Binance spot, margin and futures endpoints                                                   |
| The investor's own account                                    | All investor-side endpoints                                                                                        |

Keep sub-account trading keys separate from the Manager Parent Account key. Calling a trading-team
endpoint with a key that does not carry the trading-team role returns HTTP 400 with the error code
`-9000` and the message `You have no holdings in this portfolio`.

## Step 4 — Invite investors

Investors are invited by UID and email, which must belong to the same Binance account.

- An invitation is valid for 7 days and can be resent after expiry
- If an investor declines, they cannot be re-invited to the same portfolio for 30 days
- Once accepted, the investor is bound to the Portfolio Account and can submit subscriptions and
  redemptions
- There is no limit on the number of investors per Portfolio Account

A trading team can also invest its own capital via self-investment, which is approved automatically.

## Step 5 — First API calls

Recommended test order:

1. **Portfolio Basic Info** — verify credentials. Confirm the returned `portfolioId` and denominated
   currency match your setup.
2. **Portfolio NAV Info** — confirm the portfolio has an active NAV series.
3. **Redemption Calendar** — confirm investor-level data is visible.
4. **API Sharing Status** — confirm the current investor data-sharing setting.

A new Portfolio Account returns no NAV until its first daily calculation completes. NAV is
calculated daily between 00:00 and 04:00 UTC, so the most recent NAV available is always for the
previous UTC day.

---

# 快速开始

本节指导交易团队完成投资组合账户的设置并发起首次 API 调用。完成后，投资组合账户已创建，交易子账户已关联，API
Key 已就绪。

## 前提条件

投资组合账户面向已完成币安 KYB 实体认证的机构交易团队开放。可用性还取决于您所在的司法辖区以及您所签约的币安实体。

如需开始接入，请联系您的 VIP 客户经理，或提交投资组合账户落地页上的表单。币安审核申请后，将在您的管理人母账户上开通投资组合账户。

## 第 1 步 — 创建投资组合账户

在管理人母账户下创建投资组合账户。每个投资组合账户对应一个策略，一个管理人母账户最多可持有 5 个。

创建时必填：名称、计价币种、结算窗口、管理费、业绩费。可选，可后续补充：最低投资额、锁定期、策略类型、策略说明。

结算窗口默认为 T+1，最长可设置到 T+14。

投资人申购后，这些条款对现有投资人即被锁定。邀请投资人之前请先确认。

## 第 2 步 — 设置交易子账户

每个投资组合账户默认附带 5 个交易子账户，交易团队在此执行交易。如需更多子账户，可通过您的 VIP 客户经理申请。

## 第 3 步 — 创建 API Key

所有投资组合账户接口都需要签名请求。

| Key 签发于                             | 用途                                                                         |
| -------------------------------------- | ---------------------------------------------------------------------------- |
| 管理人母账户（已开通投资组合账户权限） | 所有交易团队接口：投资组合信息、净值历史、投资人历史、赎回日历、API 共享开关 |
| 每个交易子账户                         | 交易，通过标准的币安现货、杠杆和合约接口                                     |
| 投资人自己的账户                       | 所有投资人侧接口                                                             |

请将子账户交易 Key 与管理人母账户 Key 分开保管。使用不具备交易团队角色的 Key 调用交易团队接口，将返回 HTTP
400，错误码 `-9000`，返回信息为 `You have no holdings in this portfolio`。

## 第 4 步 — 邀请投资人

通过 UID 和邮箱邀请投资人，二者必须属于同一个币安账户。

- 邀请有效期为 7 天，过期后可重新发送
- 如果投资人拒绝邀请，30 天内不能再次邀请其加入同一个投资组合
- 接受邀请后，投资人即被绑定到该投资组合账户，可以提交申购和赎回
- 每个投资组合账户的投资人数量没有上限

交易团队也可以通过自我投资的方式投入自有资金，该申购会自动通过审批。

## 第 5 步 — 首次 API 调用

建议的测试顺序：

1. **投资组合基本信息** — 验证凭证。确认返回的 `portfolioId` 和计价币种与您的设置一致。
2. **投资组合净值信息** — 确认该投资组合存在有效的净值序列。
3. **赎回日历** — 确认可以看到投资人维度的数据。
4. **API 共享状态** — 确认当前的投资人数据共享设置。

新建的投资组合账户在首次每日计算完成之前不会返回净值。净值在 UTC
00:00 至 04:00 之间每日计算，因此可获取的最新净值始终是前一个 UTC 日的。