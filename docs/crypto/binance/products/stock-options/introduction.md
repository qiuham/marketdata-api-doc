---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/stock-options/introduction
api_type: Guide
updated_at: 2026-11-21 18:28:04.822626
---

# Introduction

**Stock Option Trading** — trade US-listed stock options with crypto.

The Stock Option Trading API lets you look up option contracts, place and cancel option orders,
exercise long positions, and query positions, orders, fills and settlement events through the SAPI
endpoint family. All endpoints live under the `/sapi/v1/equity/option/*` prefix.

## Before You Start

Option trading must be enabled in the Binance App before calling these endpoints. Enabling it
includes an investor profile questionnaire, an options knowledge test, and acceptance of the
required agreements and risk disclosures. There is no API for account opening. Orders and exercise
requests from an account without options enabled are rejected with `497203`.

## What's Included

| Group             | Endpoints                                                                                                                                                                                                                                            |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Market Data       | Option Expirations, Option Contracts, Option Exchange Info                                                                                                                                                                                           |
| Trade             | Place Option Order, Cancel Option Order, Cancel All Option Orders, Submit Option Exercise                                                                                                                                                            |
| User Data         | Current Open Option Orders, Option Order History, Option Order Detail, Option Trade History, Option Positions, Exercisable Options, Option Exercise Detail, Option Exercise History, Option Settlement Event History, Option Settlement Event Detail |
| User Data Streams | Listen Key, Order Report V2                                                                                                                                                                                                                          |

## Defaults and Conventions

- **Base URL**: same as other SAPI endpoints (see root
  [General Info](../common/sapi/general-info.md)).
- **URL prefix**: `/sapi/v1/equity/option/*`.
- **Symbol**: the OCC option contract symbol, e.g. `NVDA260930C00100000`. Parameters that filter by
  underlying are named `underlyingSymbol` and take the stock ticker, e.g. `NVDA`.
- **Quote asset**: prices are in USD; orders are paid in `USDC` only (USDC:USD 1:1).
- **Order type**: limit orders only, `timeInForce = DAY`, whole contracts only.
- **No market data**: no option prices, quotes, Greeks or implied volatility are provided. The
  Market Data endpoints return contract reference data only.
- **Signing**: same HMAC / Ed25519 scheme as other SAPI endpoints. `MARKET_DATA` endpoints need only
  the `X-MBX-APIKEY` header and are not signed.

See [General Info](./general-info.md) for rate limits and data formats, and
[Common Definition](./common-definition.md) for contract symbols, contract status and position
intent.

---

# 概览

**股票期权交易** —— 使用加密货币交易美股期权。

股票期权交易 API 通过 SAPI 渠道提供合约查询、期权下单与撤单、多头行权，以及持仓、订单、成交与结算事件查询的能力。所有接口挂在
`/sapi/v1/equity/option/*` 前缀下。

## 开始之前

调用这些接口前，需先在 Binance
App 内开通期权交易。开通流程包括投资者画像问卷、期权知识测试，以及签署相关协议与风险披露。SAPI 不提供开户接口。未开通期权的账户下单或提交行权会返回
`497203`。

## 包含的接口

| 分组       | 接口                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------ |
| 合约数据   | 到期日列表、合约列表、合约交易规则                                                                           |
| 交易       | 下单、撤单、全部撤单、提交行权                                                                               |
| 用户数据   | 当前挂单、订单历史、订单详情、成交历史、持仓查询、可行权合约、行权详情、行权历史、结算事件历史、结算事件详情 |
| 用户数据流 | Listen Key、订单回报 V2                                                                                      |

## 默认值与约定

- **Base URL**：与其他 SAPI 接口相同（见根目录 [基本信息](../common/sapi/general-info.md)）。
- **URL 前缀**：`/sapi/v1/equity/option/*`。
- **Symbol**：OCC 合约代码，如 `NVDA260930C00100000`。按标的过滤的参数一律叫
  `underlyingSymbol`，传正股 ticker，如 `NVDA`。
- **计价资产**：价格以 USD 计；下单只接受 `USDC` 支付（USDC:USD 1:1）。
- **订单类型**：只支持限价单，`timeInForce = DAY`，张数必须为整数。
- **不提供行情**：不提供期权价格、报价、Greeks 或隐含波动率。合约数据接口只返回合约参考数据。
- **签名**：与其他 SAPI 接口相同，支持 HMAC / Ed25519。`MARKET_DATA` 接口只需
  `X-MBX-APIKEY`，无需签名。

限频与数据格式见[基本信息](./general-info.md)，合约代码、合约交易状态与持仓意图见[通用枚举定义](./common-definition.md)。