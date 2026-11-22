---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/rate-limit/institutional/institutional-rate-limit
api_type: Rate Limit
updated_at: 2026-11-22 19:00:31.524507
---

# Institutional Rate Limit

### Overview

[The institutional rate limit](https://www.bitget.com/support/articles/12560603890581) is an independent rate-limiting system designed exclusively for **MM (Market Maker) and PRO** institutional users. Supports fine-grained quota allocation and management at the UID level.


### Key Concepts

| Term                                | Definition                                                                           |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Master-Sub Account Rate Limit Cap   | The maximum configurable request rate across the master account and all sub-accounts |
| Single Account Rate Limit Cap       | The maximum configurable request rate for a single master or sub-account             |
| Master-Sub Account Rate Limit Quota | The actual configured request rate for the master and all sub-accounts combined      |
| Single Account Rate Limit Quota     | The actual configured request rate for a single account                              |
| Master-Sub Account Rate Limit Usage | The actual request rate being used across the master and all sub-accounts            |
| Single Account Rate Limit Usage     | The actual request rate being used by a single account                               |


### Quota Allocation

Rate limit quotas are updated based on the user's MM&PRO tier:

- **PRO users**: Quotas are updated daily
- **MM users**: Quotas are updated monthly

Sub-account quotas can be modified by the master account via the following API:
- [`POST /api/v3/user/set-rate-limit-quota`](/docs/catalog/institutional-rate-limit/uta-user-rate-limit#set-ratelimit-quota) — Set rate limit quotas for sub-accounts (Up to 50 UIDs can be configured per request)

The current quota allocation can be queried via:
- [`GET /api/v3/user/rate-limit-quota`](/docs/catalog/institutional-rate-limit/uta-user-rate-limit#get-ratelimit-quota) — Query rate limit quotas for accounts

### Business Rules

1. The single account rate limit Quota must not exceed the single account rate limit Cap.
2. The sum of all sub-account rate limit Quotas (i.e., the Master-Sub Quota) must not exceed the Master-Sub Cap.
3. If adjusting a sub-account's Quota causes the total Master-Sub Quota to exceed the Master-Sub Cap, the API call will be rejected.
4. The institutional rate limit applies to virtual sub-accounts, regular sub-accounts, managed sub-accounts, Agent sub-accounts, and Copper sub-accounts under the master account.
    - **Managed sub-accounts** in managed mode: read the trading team master account's single account Cap; do not participate in the Master-Sub total rate limit calculation.
    - **Managed sub-accounts** in non-managed mode: API trading is not supported.
    - **Agent sub-accounts / Copper sub-accounts**: treated as virtual sub-accounts.
5. Websocket and REST will share the rate limit.
6. For order cancellation and modification requests, the `category` parameter must be added in the request parameters in order to trigger the configured rate limit.
7. Rate limits include placing orders, canceling orders, and modifying orders (Rate limits are calculated independently).


### MM/PRO Rate Limit Tiers

Rate limit quotas are determined by the user's MM or PRO tier. The tables below show the rate limit tiers.

#### MM Rate Limit Tiers

**Single Account**

| MM Tier | Sub-Accounts | Spot Rate Limit Cap | Futures Rate Limit Cap |
|:--------|:-------------|:--------------------|:-----------------------|
| Tier 1  | 300          | 600/s               | 600/s                  |
| Tier 2  | 300          | 500/s               | 500/s                  |
| Tier 3  | 200          | 400/s               | 400/s                  |
| Tier 4  | 200          | 200/s               | 200/s                  |
| Tier 5  | 200          | 200/s               | 200/s                  |

**Master-Sub Account**

| MM Tier | Sub-Accounts | Spot Rate Limit Cap | Futures Rate Limit Cap |
|:--------|:-------------|:--------------------|:-----------------------|
| Tier 1  | 300          | 120,000/s           | 120,000/s              |
| Tier 2  | 300          | 100,000/s           | 100,000/s              |
| Tier 3  | 200          | 80,000/s            | 80,000/s               |
| Tier 4  | 200          | 40,000/s            | 40,000/s               |
| Tier 5  | 200          | 40,000/s            | 40,000/s               |

#### PRO Rate Limit Tiers

**Single Account**

| PRO Tier | Sub-Accounts | Spot Rate Limit Cap | Futures Rate Limit Cap |
|:---------|:-------------|:--------------------|:-----------------------|
| PRO1     | 200          | 200/s               | 200/s                  |
| PRO2     | 200          | 200/s               | 200/s                  |
| PRO3     | 200          | 400/s               | 400/s                  |
| PRO4     | 300          | 400/s               | 400/s                  |
| PRO5     | 300          | 500/s               | 500/s                  |
| PRO6     | 300          | 600/s               | 600/s                  |

**Master-Sub Account**

| PRO Tier | Sub-Accounts | Spot Rate Limit Cap | Futures Rate Limit Cap |
|:---------|:-------------|:--------------------|:-----------------------|
| PRO1     | 200          | 40,000/s            | 40,000/s               |
| PRO2     | 200          | 40,000/s            | 40,000/s               |
| PRO3     | 200          | 80,000/s            | 80,000/s               |
| PRO4     | 300          | 80,000/s            | 80,000/s               |
| PRO5     | 300          | 100,000/s           | 100,000/s              |
| PRO6     | 300          | 120,000/s           | 120,000/s              |


### Classic Account Rate Limits

For classic spot and futures accounts under MM and PRO rate limits:

| MM Tier | Sub-Accounts | Spot Classic | Futures Classic |
|:--------|:-------------|:-------------|:----------------|
| Tier 1  | 300          | 100/s        | 100/s           |
| Tier 2  | 300          | 80/s         | 80/s            |
| Tier 3  | 200          | 80/s         | 80/s            |
| Tier 4  | 200          | 60/s         | 60/s            |
| Tier 5  | 200          | 60/s         | 60/s            |

| PRO Tier | Sub-Accounts | Spot Classic | Futures Classic |
|:---------|:-------------|:-------------|:----------------|
| PRO1     | 200          | 60/s         | 60/s            |
| PRO2     | 200          | 80/s         | 80/s            |
| PRO3     | 200          | 100/s        | 100/s           |
| PRO4     | 300          | 100/s        | 100/s           |
| PRO5     | 300          | 100/s        | 100/s           |
| PRO6     | 300          | 100/s        | 100/s           |

---

# 限频规则

### 概述

[机构限频规则](https://www.bitget.com/zh-CN/support/articles/12560603890581)是面向 **MM（做市商）和 PRO** 机构用户设计的独立限频体系，支持 UID 维度的限频配额精细化管理。


### 名词释义

| 名词 | 释义 |
|---|---|
| 母子账户限频硬顶 Cap | 母子账户总请求量的最大配置上限 |
| 单账户限频硬顶 Cap | 单一母账户或子账户请求量的最大配置上限 |
| 母子账户限频 Quota | 母子账户总请求量的实际配置值 |
| 单账户限频 Quota | 单一母账户或子账户请求量的实际配置值 |
| 母子账户限频 Usage | 母子账户总请求量的实际使用值 |
| 单账户限频 Usage | 单一母账户或子账户请求量的实际使用值 |


### 配额分配

限频配额跟随用户等级定期更新：

- **PRO 用户**：每日更新
- **MM 用户**：每月更新

子账户额度可通过以下 API 由母账户进行分配：
- [`POST /api/v3/user/set-rate-limit-quota`](/zh-CN/docs/catalog/institutional-rate-limit/uta-user-rate-limit#set-ratelimit-quota) — 设置子账户限频配额（单次最多支持配置 50 个 UID）

当前额度分配情况可通过以下 API 查询：
- [`GET /api/v3/user/rate-limit-quota`](/zh-CN/docs/catalog/institutional-rate-limit/uta-user-rate-limit#get-ratelimit-quota) — 查询账户限频配额

### 业务规则

1. 单账户限频 Quota 数值不得超过单账户限频 Cap，否则接口报错。
2. 所有子账户的单账户限频 Quota 总和（即母子账户限频 Quota）不得超过母子账户限频硬顶 Cap。
3. 如果调整某账户限频 Quota 后，母子账户限频 Quota 超出母子账户硬顶 Cap，则当次接口调用不会成功。
4. 母子账户限频总量作用于母账户下的虚拟子账户、普通子账户、托管子账户、Agent 子账户、Copper 子账户。
    - **托管子账户**在托管状态下：读取交易团队母账户的单账户限频硬顶 Cap，不参与母子总限频计算。
    - **托管子账户**在非托管状态下：不支持 API 交易。
    - **Agent 子账户 / Copper 子账户**：视作虚拟子账户。
5. Websocket和REST共享限频
6. 撤单和改单需要传入`category`入参来触发配置的限频
7. 限频包含下单、撤单和改单(限频独立计算)

### MM/PRO限频梯度


限频额度跟随用户 MM/PRO 等级确定，以下为限频梯度。

#### MM 限频梯度

**单账户限频**

| MM 等级 | 子账户数 | 现货限频硬顶Cap | 合约限频硬顶Cap |
|:---|:---|:---|:---|
| 1 级 | 300 | 600/s | 600/s |
| 2 级 | 300 | 500/s | 500/s |
| 3 级 | 200 | 400/s | 400/s |
| 4 级 | 200 | 200/s | 200/s |
| 5 级 | 200 | 200/s | 200/s |

**母子账户限频**

| MM 等级 | 子账户数 | 现货限频硬顶Cap | 合约限频硬顶Cap |
|:---|:---|:---|:---|
| 1 级 | 300 | 120,000/s | 120,000/s |
| 2 级 | 300 | 100,000/s | 100,000/s |
| 3 级 | 200 | 80,000/s | 80,000/s |
| 4 级 | 200 | 40,000/s | 40,000/s |
| 5 级 | 200 | 40,000/s | 40,000/s |

#### PRO 限频梯度

**单账户限频**

| PRO 等级 | 子账户数 | 现货限频硬顶Cap | 合约限频硬顶Cap |
|:---|:---|:---|:---|
| PRO1 | 200 | 200/s | 200/s |
| PRO2 | 200 | 200/s | 200/s |
| PRO3 | 200 | 400/s | 400/s |
| PRO4 | 300 | 400/s | 400/s |
| PRO5 | 300 | 500/s | 500/s |
| PRO6 | 300 | 600/s | 600/s |

**母子账户限频**

| PRO 等级 | 子账户数 | 现货限频硬顶Cap | 合约限频硬顶Cap |
|:---|:---|:---|:---|
| PRO1 | 200 | 40,000/s | 40,000/s |
| PRO2 | 200 | 40,000/s | 40,000/s |
| PRO3 | 200 | 80,000/s | 80,000/s |
| PRO4 | 300 | 80,000/s | 80,000/s |
| PRO5 | 300 | 100,000/s | 100,000/s |
| PRO6 | 300 | 120,000/s | 120,000/s |


### 经典账户限频配置

经典现货及经典合约账户的机构限频配置：

| MM 等级 | 子账户数 | 现货经典账户 | 合约经典账户 |
|:---|:---|:---|:---|
| 1 级 | 300 | 100/s | 100/s |
| 2 级 | 300 | 80/s | 80/s |
| 3 级 | 200 | 80/s | 80/s |
| 4 级 | 200 | 60/s | 60/s |
| 5 级 | 200 | 60/s | 60/s |

| PRO 等级 | 子账户数 | 现货经典账户 | 合约经典账户 |
|:---|:---|:---|:---|
| PRO1 | 200 | 60/s | 60/s |
| PRO2 | 200 | 80/s | 80/s |
| PRO3 | 200 | 100/s | 100/s |
| PRO4 | 300 | 100/s | 100/s |
| PRO5 | 300 | 100/s | 100/s |
| PRO6 | 300 | 100/s | 100/s |