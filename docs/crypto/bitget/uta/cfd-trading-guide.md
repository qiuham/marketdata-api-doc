---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/cfd-trading-guide
api_type: Guide
updated_at: 2026-11-28 18:59:34.054385
---

# CFD Trading Guide

## Overview

Bitget CFD (Contract for Difference) supports trading on a variety of mainstream assets, covering gold, crude oil, forex indices, and more. Trading pair names follow formats such as `XAUUSD`, `XAUUSD.s`, and `XAUUSD.pro`.

To meet the programmatic trading needs of quantitative teams and algorithmic traders, Bitget Open API supports CFD trading. Traders can use the API to automate order execution, fund transfers, and data queries directly from their CFD accounts.

**Note:** The API does not support opening CFD accounts. Before trading CFD via the API, users must first complete the CFD account opening process on the Bitget website or App. Once your CFD account has been opened, you can start trading through the API.

## Supported API Features

The CFD Open API currently supports the following core features:

1. Trading operations
   - Fund transfers: Transfer assets into or out of CFD accounts.
   - Order execution: Open and close positions at market price, place limit orders, and cancel orders.
   - Risk management: Set take-profit and stop-loss conditions when placing orders, or modify TP/SL settings for existing positions.
2. Data queries
   - Account and historical data: Query CFD account information, historical fund records, and order history.
   - Market data: Access real-time CFD market data and instrument configuration parameters.

## Trading Modes and Instrument Code Rules (⚠️ Important for API Calls)

Each account is assigned to a single trading mode, and instrument code suffixes vary by mode. When calling the order placement API, users must provide an instrument code that matches their account's current trading mode. Otherwise, the system will return an error and reject the order. Details are as follows:

| Trading mode | API instrument code format | Example |
|---|---|---|
| Zero-fee mode | Instrument name with the `.s` suffix | `XAUUSD.s`, `EURUSD.s` |
| ECN mode | Instrument name without a suffix | `XAUUSD`, `EURUSD` |
| Pro mode | Instrument name with the `.pro` suffix | `XAUUSD.pro`, `XAGUSD.pro` |

**Note:** Confirm your account's trading mode before calling the order placement API.

For more details about CFD, please refer to:

- [CFD Beginner's Guide](https://www.bitget.com/support/articles/12560603840554)
- [CFD Trading Mode Explained](https://www.bitget.com/support/articles/12560603894277)
- [Bitget Open API now supports CFD trading](https://www.bitget.com/support/articles/12560603894278)

---

# CFD 交易指南

## 概述

Bitget CFD（差价合约）支持多种主流资产交易，涵盖黄金、原油及外汇指数等，交易对名称格式如 `XAUUSD`，`XAUUSD.s`，`XAUUSD.pro`。

为满足量化团队与算法交易者对程序化执行的需求，Bitget Open API 支持 CFD 交易。交易者可通过 API 接口直接对 CFD 账户进行订单执行、资金划转及数据查询等自动化管理操作。

**注意：** API 接口不支持自动完成开户流程。在使用 API 进行 CFD 交易前，用户必须先在 Bitget 网页端或 App 端完成 CFD 账户开户。开户完成后即可使用 API 进行交易操作。

## 支持的 API 功能范围

目前 CFD Open API 已开放以下核心功能接口：

1. 交易操作类
   - 资金划转：支持将资产划入或划出 CFD 账户；
   - 订单执行：支持市价开仓、平仓，以及限价挂单、撤单；
   - 风控设置：支持在下单时预设止盈止损条件，或对现有仓位的止盈止损参数进行修改。
2. 数据查询类
   - 账户与历史数据：支持查询 CFD 账户信息、历史资金流水及历史订单记录；
   - 市场数据：支持获取 CFD 实时行情数据及交易品种配置参数。

## 交易模式与品种代码规则（⚠️ 接口调用必读）

每个账户均归属于唯一的交易模式，且不同模式下的品种代码后缀存在严格区分。用户在调用下单接口时，必须传入与当前账户模式相匹配的品种代码，否则系统将返回错误并拒绝下单。具体规则如下：

| 交易模式 | API 品种代码格式 | 调用传参示例 |
|---|---|---|
| 0 手续费模式 | 品种名称带 `.s` 后缀 | `XAUUSD.s`、`EURUSD.s` |
| ECN 模式 | 品种名称无后缀 | `XAUUSD`、`EURUSD` |
| Pro 模式 | 品种名称带 `.pro` 后缀 | `XAUUSD.pro`、`XAGUSD.pro` |

**注意：** 请在调用下单接口前确认当前账户所属的交易模式。

关于 CFD 的详情信息，请参考：

- [CFD新手指南](https://www.bitget.com/zh-CN/support/articles/12560603840554)
- [CFD交易模式说明](https://www.bitget.com/zh-CN/support/articles/12560603894277)
- [Bitget Open API 正式支持 CFD 交易](https://www.bitget.com/zh-CN/support/articles/12560603894278)