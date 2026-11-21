---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/Introduction
api_type: Guide
updated_at: 2026-11-21 19:02:17.188228
---

# Introduction

:::tip{title="Recommended: Use Unified Trading Account"}
We recommend using the **[Unified Trading Account (UTA)](/docs/uta/uta-intro)** — it consolidates spot, margin, and derivatives into a single account with higher capital efficiency. The Classic Account is in maintenance mode and receives only essential updates.
:::

## API Introduction

Welcome to Bitget Developer document!

This document is the only official document of Bitget API. We will constantly update the functionalities of Bitget API here. Please pay attention to it regularly.

You can switch to APIs for different account types by clicking the top menu, and you can change the documentation language by clicking the language button in the upper-right corner.

On the right side of the document usually displays example of request parameters and response results.

## Updates

Regarding API additions, updates, and offline information, Bitget will issue announcements in advance to notify you. It is recommended that you follow and subscribe to our announcements to obtain relevant information in time.

You can click [Latest News](https://www.bitget.com/support/categories/360002621832) to subscribe to announcements.

## Contact Us

If you have any questions or suggestions, you can contact us by:

- Telegram [Join](https://t.me/bitgetOpenapi)

## Classic Account Introduction

Requires holding specific assets in separate accounts (e.g., USDT in derivatives).

Accounts needed:

1. Fiat account
2. Spot account
3. Margin account
4. Futures account

## Supported trading products

- Spot
- Margin
- USDT-M perpetual
- USDC-M perpetual
- Coin-M perpetual

## Supported margin assets

Margin modes

- Isolated margin
- Cross margin

Position modes

- One-way mode
- Hedging mode — supports different leverage settings for long and short positions.

## HODL mode and auto-margin features

- Manual borrowing and repayment required
- Cross and isolated modes

## Risk management and liquidation

- Triggered when mark price hits liquidation threshold.

## Key Features

### Interface Optimization

We have optimized interface design to reduce redundancy and improve clarity in business scenarios. Interfaces are now more intuitive and easier to use, with consistent naming conventions across all business lines.

### Simplified Symbol Request Rules

We use a single parameter — **symbol** — for all trading pair requests, making API calls more straightforward and consistent across different products.

### Advanced Query Capabilities

Our query interfaces now support cursor-based pagination with `idLessThan` and `limit` parameters, providing more efficient data retrieval. Most query interfaces also support time range filtering with `startTime` and `endTime` parameters.

**Query Priority Rules:**

When querying data, the verification order for returned results is: `id` > `startTime` + `endTime` > `idLessThan`. This means:

1. First, it prioritizes precise queries using the `id`
2. Then narrows down the data range with `startTime` and `endTime`
3. Finally uses the cursor `idLessThan` to retrieve a specified number of data entries based on the `limit`

### Standardized Naming Conventions

We have standardized parameter naming and formats across all business lines (spot, futures, margin) and interface types (REST/WebSocket), ensuring consistency and ease of use.

### Improved Documentation Structure

Interface catalogs are now more detailed and intuitive, making documentation easier to navigate and improving the overall user experience.

### Enhanced Market Depth

For futures and spot trading pairs, we significantly increased the trading pair depth accessible through our interfaces and standardized the tiers across different business lines.

| Business Line | Tier |
|---------------|------|
| Spot | 1/5/15/50/max; default: 100. The max is determined by the highest tier available for the designated trading pair. |
| Future | 1/5/15/50/max; default: 100. The max is determined by the highest tier available for the designated trading pair. |

### Unified Futures Order Types

Trigger orders and trailing stop-loss orders are combined into one unified system, using the `planType` field to differentiate order types.

**Important Fields:**

- **callbackRatio**: Sets the order-triggering percentage for trailing stop-loss
- **stopSurplusTriggerPrice** and **stopLossTriggerPrice**: Determine the trail variance percentage that triggers trailing stop-loss and take-profit orders

### Flexible Position Management

Our futures order placement system supports both one-way and hedging modes with intuitive parameter combinations.

**Field Enumeration Values:**

| Field name | Enumeration value | Description |
|------------|-------------------|-------------|
| side | buy | Buying |
| side | sell | Selling |
| tradeSide | open | Opening a position |
| tradeSide | close | Closing a position |

**Position Mode Operations:**

| Position mode | Parameter entries | Operation | Description |
|---------------|-------------------|-----------|-------------|
| One-way mode | side: buy | Buying | In one-way mode, only side is needed to indicate whether it is a buying or selling order |
| One-way mode | side: sell | Selling | In one-way mode, only side is needed to indicate whether it is a buying or selling order |
| Hedging mode | side: buy; tradeSide: open | Opening a long position | In hedging mode, both side and tradeSide are needed to determine whether it is opening long/short or closing long/short |
| Hedging mode | side: sell; tradeSide: open | Opening a short position | In hedging mode, both side and tradeSide are needed to determine whether it is opening long/short or closing long/short |
| Hedging mode | side: buy; tradeSide: close | Closing a long position | In hedging mode, both side and tradeSide are needed to determine whether it is opening long/short or closing long/short |
| Hedging mode | side: sell; tradeSide: close | Closing a short position | In hedging mode, both side and tradeSide are needed to determine whether it is opening long/short or closing long/short |

### Delivery Futures Symbol Format

For Coin-M delivery futures, the symbol format is: **trading pair + month code + year**

**Examples:**

| Symbol | Description |
|--------|-------------|
| BTCUSD**H**23 | H means March (Q1) and 23 means the year 2023 |
| BTCUSD**M**23 | M means June (Q2) and 23 means the year 2023 |
| BTCUSD**U**23 | U means September (Q3) and 23 means the year 2023 |
| BTCUSD**Z**23 | Z means December (Q4) and 23 means the year 2023 |

**Month Codes:**

| Month code | Month | Month code | Month |
|------------|-------|------------|-------|
| F | January | N | July |
| G | February | Q | August |
| **H** | March | **U** | September |
| J | April | V | October |
| K | May | X | November |
| **M** | June | **Z** | December |

### Comprehensive Trading Pair Information

Our interfaces provide detailed information about trading pairs, including:

- Minimum and maximum trading volumes
- Maximum number of open orders (per trading pair and product)
- Price precision
- Amount precision
- Other essential trading parameters

### Earn Products Support

We offer comprehensive interfaces for crypto Earn products, including:

- **Savings**: Both fixed and flexible options
- **Shark Fin**: Structured products
- Features include information retrieval, PnL statistics, asset analysis, subscription, and redemption

### Crypto Loan Services

Our Crypto Loan API provides a complete solution for users seeking flexible borrowing options:

- Stake crypto assets as collateral
- Borrow fiat currency or cryptocurrencies
- Manage collateral (add/withdraw)
- Handle interest payments and loan repayment
- Automatic liquidation protection

The API covers the entire loan lifecycle: staking collateral, obtaining loans, managing collateral, handling liquidation, paying interest, repaying loans, and redeeming collateral.

:::tip{title="Note"}
Due to the volatile nature of the cryptocurrency market, coin price fluctuations may impact overall returns. Users should carefully consider market risks when using loan services.
:::

---

# 介绍

:::tip{title="推荐：使用统一账户"}
我们推荐使用 **[统一账户（UTA）](/zh-CN/docs/uta/uta-intro)** —— 支持在单一账户内交易现货、杠杆及各类衍生品，资金利用率更高。经典账户已进入维护模式，仅提供必要性更新。
:::

## Bitget API 简介

欢迎使用 Bitget 开发者文档！

此文档是 Bitget API 的唯一官方文档，Bitget API 提供的能力会在此持续更新，请大家及时关注。

你可以通过点击上方菜单来切换获取不同账户类型的 API，还可通过点击右上方的语言按钮来切换文档语言。

文档右侧是针对请求参数以及响应结果的示例。

## 更新关注

关于 API 新增、更新、下线等信息 Bitget 会提前发布公告进行通知，建议您关注和订阅我们的公告，及时获取相关信息。

您可以点击 [最新公告](https://www.bitget.com/zh-CN/support/categories/360002621832) 订阅公告。

## 联系我们

使用过程中如有问题或者建议，您可选择以下方式联系我们：

- Telegram [点击加入](https://t.me/bitgetOpenapi)

## 经典账户介绍

交易者必须持有每个账户中与交易产品相关的特定资产才能参与。例如，衍生品账户需要 USDT 才能交易 USDT 合约。

要管理的账户：

1. 资金账户
2. 现货账户
3. 杠杆账户
4. 合约账户

## 交易产品类型

- 现货
- 杠杆
- USDT 永续
- USDC 永续
- 币本位永续

## 保证金和仓位模式

保证金模式

- 逐仓保证金
- 全仓保证金

仓位模式

- 单向持仓模式
- 双向持仓模式 —— 为多仓和空仓提供不同的杠杆设置。

## 借贷模式

- 支持全仓、逐仓借贷
- 需用户手动借贷 / 手动还款

## 风险管理

- 当标记价格达到强平价格时，将触发强平。

## 核心特性

### 接口优化

我们优化了接口设计，减少冗余并提高业务场景的清晰度。接口现在更加直观易用，所有业务线的命名约定保持一致。

### 简化的交易对请求规则

我们使用单一参数 —— **symbol** —— 处理所有交易对请求，使 API 调用在不同产品间更加简单一致。

### 高级查询功能

我们的查询接口现在支持基于游标的分页，使用 `idLessThan` 和 `limit` 参数，提供更高效的数据检索。大多数查询接口还支持使用 `startTime` 和 `endTime` 参数进行时间范围过滤。

**查询优先级规则：**

查询数据时，返回结果的验证顺序为：`id` > `startTime` + `endTime` > `idLessThan`。这意味着：

1. 首先，优先使用 `id` 进行精确查询
2. 然后使用 `startTime` 和 `endTime` 缩小数据范围
3. 最后使用游标 `idLessThan` 根据 `limit` 检索指定数量的数据条目

### 标准化命名约定

我们在所有业务线（现货、合约、杠杆）和接口类型（REST/WebSocket）中标准化了参数命名和格式，确保一致性和易用性。

### 改进的文档结构

接口目录现在更加详细直观，使文档更易于浏览，提升整体用户体验。

### 增强的市场深度

对于合约和现货交易对，我们显著增加了通过接口可访问的交易对深度，并在不同业务线间标准化了档位。

| 业务线 | 档位 |
|--------|------|
| 现货 | 1/5/15/50/max；默认：100。max 由指定交易对可用的最高档位决定。 |
| 合约 | 1/5/15/50/max；默认：100。max 由指定交易对可用的最高档位决定。 |

### 统一的合约订单类型

触发订单和追踪止损订单合并为一个统一系统，使用 `planType` 字段区分订单类型。

**重要字段：**

- **callbackRatio**：设置追踪止损的订单触发百分比
- **stopSurplusTriggerPrice** 和 **stopLossTriggerPrice**：确定触发追踪止损和止盈订单的追踪变化百分比

### 灵活的仓位管理

我们的合约下单系统支持单向和双向持仓模式，参数组合直观。

**字段枚举值：**

| 字段名 | 枚举值 | 描述 |
|--------|--------|------|
| side | buy | 买入 |
| side | sell | 卖出 |
| tradeSide | open | 开仓 |
| tradeSide | close | 平仓 |

**持仓模式操作：**

| 持仓模式 | 参数组合 | 操作 | 描述 |
|----------|----------|------|------|
| 单向持仓 | side: buy | 买入 | 在单向持仓模式下，只需要 side 来表示是买单还是卖单 |
| 单向持仓 | side: sell | 卖出 | 在单向持仓模式下，只需要 side 来表示是买单还是卖单 |
| 双向持仓 | side: buy; tradeSide: open | 开多仓 | 在双向持仓模式下，需要同时使用 side 和 tradeSide 来确定是开多/开空还是平多/平空 |
| 双向持仓 | side: sell; tradeSide: open | 开空仓 | 在双向持仓模式下，需要同时使用 side 和 tradeSide 来确定是开多/开空还是平多/平空 |
| 双向持仓 | side: buy; tradeSide: close | 平多仓 | 在双向持仓模式下，需要同时使用 side 和 tradeSide 来确定是开多/开空还是平多/平空 |
| 双向持仓 | side: sell; tradeSide: close | 平空仓 | 在双向持仓模式下，需要同时使用 side 和 tradeSide 来确定是开多/开空还是平多/平空 |

### 交割合约 Symbol 格式

对于币本位交割合约，symbol 格式为：**交易对 + 月码 + 年份**

**示例：**

| Symbol | 描述 |
|--------|------|
| BTCUSD**H**23 | H 表示三月（第一季度），23 表示 2023 年 |
| BTCUSD**M**23 | M 表示六月（第二季度），23 表示 2023 年 |
| BTCUSD**U**23 | U 表示九月（第三季度），23 表示 2023 年 |
| BTCUSD**Z**23 | Z 表示十二月（第四季度），23 表示 2023 年 |

**月码：**

| 月码 | 月份 | 月码 | 月份 |
|------|------|------|------|
| F | 一月 | N | 七月 |
| G | 二月 | Q | 八月 |
| **H** | 三月 | **U** | 九月 |
| J | 四月 | V | 十月 |
| K | 五月 | X | 十一月 |
| **M** | 六月 | **Z** | 十二月 |

### 全面的交易对信息

我们的接口提供详细的交易对信息，包括：

- 最小和最大交易量
- 最大持仓订单数（每个交易对和产品）
- 价格精度
- 数量精度
- 其他重要交易参数

### 理财产品支持

我们为加密货币理财产品提供全面的接口，包括：

- **理财宝**：活期和定期选项
- **鲨鱼鳍**：结构化产品
- 功能包括信息检索、收益统计、资产分析、申购和赎回

### 加密货币借贷服务

我们的加密货币借贷 API 为寻求灵活借贷选项的用户提供完整解决方案：

- 质押加密资产作为抵押品
- 借入法币或加密货币
- 管理抵押品（添加/提取）
- 处理利息支付和贷款偿还
- 自动清算保护

API 涵盖整个贷款生命周期：质押抵押品、获得贷款、管理抵押品、处理清算、支付利息、偿还贷款和赎回抵押品。

:::tip{title="注意"}
由于加密货币市场的波动性，币价波动可能影响整体收益。用户在使用借贷服务时应仔细考虑市场风险。
:::