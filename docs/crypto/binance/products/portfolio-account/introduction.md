---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/portfolio-account/introduction
api_type: Guide
updated_at: 2026-11-27 18:30:02.739722
---

# Introduction

Portfolio Account (PA) is Binance's institutional fund infrastructure. It lets a trading team manage
capital from multiple investors in a single pooled structure, without building its own custody, NAV
calculation or fee machinery.

Investors are not given separate managed accounts. Their capital is pooled into one Portfolio
Account and the trading team runs a single strategy across that pool. The team manages the strategy;
Binance handles investor binding, subscriptions and redemptions, daily NAV calculation, fee accrual,
custody and performance calculation.

Capital Connect (CC) is the distribution layer on top of Portfolio Account. It lists eligible
portfolios to institutional investors using performance data calculated by Binance from the
portfolio's own NAV history. Trading teams cannot self-report or edit performance data at any point.

For more information, please refer to the
[Binance Portfolio Account](https://www.binance.com/en/portfolio-account) page.

## Terminology

One term per concept. These are used consistently throughout this documentation and in all API
fields.

| Term                    | Meaning                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| Allocation              | The unit of ownership in a Portfolio Account. An investor holds a number of allocations. |
| NAV per allocation      | The price of one allocation. API field: `navPerAllocation`.                              |
| Investor equity         | allocations × NAV per allocation. API field: `investorNav`.                              |
| Portfolio net assets    | Total value of the Portfolio Account. Not exposed to investors.                          |
| Allocations outstanding | Sum of all investors' allocations. Not exposed to investors.                             |

## What the API covers

| Role         | Available via API                                                                                                     | Requires the web portal                                    |
| ------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Trading team | Portfolio info, NAV history, investor transaction history, redemption calendar, API sharing switch                    | Create portfolios, approve subscriptions, invite investors |
| Investor     | NAV per allocation, own allocations and equity, own transaction history, portfolio risk metrics, realtime asset value | Subscribe, redeem, accept invitations                      |

## Where to go next

| If you are                                           | Start here                                                                            |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Setting up for the first time                        | [Getting Started](./getting-started.md)                                               |
| Wanting to understand NAV, fees, lock-up, settlement | [Core Concepts](./core-concepts.md)                                                   |
| A trading team integrating                           | [Integration Guide — Trading Team](./integration-guide-trading-team.md)               |
| Preparing a portfolio for public listing             | [Integration Guide — Capital Connect Listing](./integration-guide-capital-connect.md) |
| An investor integrating                              | [Integration Guide — Investor](./integration-guide-investor.md)                       |
| Looking for signing, limits, error codes             | [Basics](./basics.md)                                                                 |
| Endpoint reference                                   | [API Reference](/catalog/vip-and-institutional-portfolio-account/api/rest-api)        |

---

# 概述

投资组合账户（Portfolio
Account，PA）是币安面向机构的基金基础设施。交易团队可以在单一的资金池结构中管理来自多个投资人的资金，而无需自行搭建托管、净值（NAV）计算或费用核算体系。

投资人不会获得单独的托管账户，其资金被汇集到同一个投资组合账户中，由交易团队在整个资金池上运行同一个策略。交易团队负责管理策略；币安负责投资人绑定、申购与赎回、每日净值计算、费用计提、托管以及业绩计算。

Capital
Connect（CC）是建立在投资组合账户之上的分发层。它基于币安根据投资组合自身净值历史计算出的业绩数据，向机构投资人展示符合条件的投资组合。交易团队在任何时候都无法自行上报或修改业绩数据。

更多信息，请参阅[币安投资组合账户](https://www.binance.com/zh-CN/portfolio-account)。

## 术语

每个概念只使用一个术语，本文档及所有 API 字段中保持一致。

| 术语               | 含义                                                   |
| ------------------ | ------------------------------------------------------ |
| 份额（Allocation） | 投资组合账户中的所有权单位。投资人持有一定数量的份额。 |
| 每份净值           | 一份份额的价格。API 字段：`navPerAllocation`。         |
| 投资人权益         | 份额 × 每份净值。API 字段：`investorNav`。             |
| 投资组合净资产     | 投资组合账户的总价值。不向投资人暴露。                 |
| 已发行份额总数     | 所有投资人份额之和。不向投资人暴露。                   |

## API 覆盖范围

| 角色     | 可通过 API 完成                                                        | 需要通过网页端完成                 |
| -------- | ---------------------------------------------------------------------- | ---------------------------------- |
| 交易团队 | 投资组合信息、净值历史、投资人交易历史、赎回日历、API 共享开关         | 创建投资组合、审批申购、邀请投资人 |
| 投资人   | 每份净值、自身份额与权益、自身交易历史、投资组合风险指标、实时资产价值 | 申购、赎回、接受邀请               |

## 接下来看哪里

| 如果你是                       | 从这里开始                                                                |
| ------------------------------ | ------------------------------------------------------------------------- |
| 首次接入                       | [快速开始](./getting-started.md)                                          |
| 想了解净值、费用、锁定期、结算 | [核心概念](./core-concepts.md)                                            |
| 正在对接的交易团队             | [集成指南 — 交易团队](./integration-guide-trading-team.md)                |
| 准备公开上架投资组合           | [集成指南 — Capital Connect 上架](./integration-guide-capital-connect.md) |
| 正在对接的投资人               | [集成指南 — 投资人](./integration-guide-investor.md)                      |
| 查找签名、限频、错误码         | [基础信息](./basics.md)                                                   |
| 查看接口详情                   | [API 参考](/catalog/vip-and-institutional-portfolio-account/api/rest-api) |