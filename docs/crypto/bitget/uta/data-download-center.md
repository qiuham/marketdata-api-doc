---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/data-download-center
api_type: Guide
updated_at: 2026-11-18 08:36:24.064865
---

# Data Download Center

There are two ways to get historical data:

1. **Web download**: Bitget's web download centers let you export the full history — in most cases as far back as **January 1, 2018**.
2. **API**: Some historical market data (e.g. open interest history) cannot be downloaded from the web and is available through API endpoints; many market data and account/trade history endpoints only return data within a recent time window (e.g. 90 days).

This page maps each type of historical data to where you can get it.

| Method | Covers | Jump to |
|:---|:---|:---|
| 🌐 Web: Market Data | Candlestick / Trades / Depth | [↓ Section](#-market-data-download-center) |
| 🌐 Web: Funding Rate | Historical funding rates | [↓ Section](#-historical-funding-rate) |
| 🌐 Web: Personal Account Data | Classic spot/futures/margin, earn orders, UTA orders | [↓ Section](#-personal-account-data) |
| 🔌 API: Historical Market Data | Open interest, funding rate, candlesticks, liquidations, risk reserve, borrow rates, long/short ratios, etc. | [↓ Section](#-historical-market-data-via-api) |

---

## 🌐 Web Download

### 📊 Market Data Download Center

:::info{title="Download entry point"}
<a href="https://www.bitget.com/data-download"><strong>bitget.com/data-download</strong></a> — historical candlestick, trades, and depth data.
:::

#### 💰 Spot

| Data Type | Description |
|:---|:---|
| 🕯️ Candlestick | OHLC and volume candlestick data for each trading pair, including historical data beyond the API's default query range |
| 🔄 Trades | Public fills on the platform, including historical fills beyond the API's 90-day query window |
| 📉 Depth | A snapshot of bid/ask order book depth, including merged depth by price precision |

#### 📈 Futures

| Data Type | Description |
|:---|:---|
| 🕯️ Candlestick | OHLC and volume candlestick data for each contract (including index/mark price variants), including historical data beyond the API's default query range |
| 🔄 Trades | Public fills on the platform, including historical fills beyond the API's 90-day query window |
| 📉 Depth | A bid/ask depth snapshot with price levels merged by precision |

---

### 💸 Historical Funding Rate

:::info{title="Download entry point"}
<a href="https://www.bitget.com/trade-info/funding_rate"><strong>bitget.com/trade-info/funding_rate</strong></a> — view and download historical funding rates for futures on the web.
:::

After opening the link, switch to the **Funding rate history** tab and a download button will appear.

To fetch them programmatically, use the [Get Funding Rate History](/docs/catalog/market/derivatives#get-funding-rate-history) endpoint (last 90 days).

---

### 📦 Personal Account Data

API endpoints are limited to a recent query window (typically 90 days). If you need older personal order, fill, or financial data, the web <a href="https://www.bitget.com/asset/export/downOrders">Export Center</a> offers broader download coverage, organized by account type and business category.

:::info{title="Download entry point"}
<a href="https://www.bitget.com/asset/export/downOrders"><strong>bitget.com/asset/export/downOrders</strong></a>
:::

#### 💰 Classic Spot

| Data Type | Description |
|:---|:---|
| 📋 Order History | All spot orders placed on the account, including filled, partially filled, and cancelled orders |
| 🔄 Fill History | Execution details of spot orders, including price, quantity, and fees |
| 💵 Financial Records | Spot account balance changes, such as trade debits/credits, transfers, and promotional rewards |
| 🏦 Deposit/Withdrawal Records | Crypto deposit and withdrawal records on the spot account |

#### 📈 Classic Futures

| Data Type | Description |
|:---|:---|
| 📋 Order History | Futures orders, including limit and market orders |
| 📊 Positions History | Closed historical positions, including open/close price, PnL, and leverage |
| 🔄 Fill History | Execution details of futures orders |
| 💵 Financial Records | Futures account balance changes, such as funding fees, realized PnL, and transfers |

#### ⚖️ Classic Margin

| Data Type | Description |
|:---|:---|
| 📋 Order History | Orders placed on cross or isolated margin accounts |
| 💵 Financial Records | Margin account balance changes, including borrowing, repayment, and interest |

#### 💎 Earn Orders

| Data Type | Description |
|:---|:---|
| 🪙 Savings | Subscription, redemption, and interest payout records for flexible/fixed savings products |
| ⛓️ On-chain Earn | Orders for on-chain earn products such as staking and liquidity mining |
| 🔀 Dual Investment | Subscription and settlement records for Dual Investment products |
| 🦈 Shark Fin | Subscription and settlement records for Shark Fin structured products |

#### 🏦 UTA

| Data Type | Description |
|:---|:---|
| 📋 Order History | Order records across spot, futures, margin, and other business lines under a Unified Trading Account |
| 📊 Positions History | Closed historical positions under a Unified Trading Account |
| 💵 Financial Records | Balance change records for a Unified Trading Account |
| 🔀 Coin Conversion Records | History of in-account coin-to-coin conversions |

:::tip{title="Data range"}
Unless otherwise noted on the page, data is available as early as **January 1, 2018**.
:::

---

## 🔌 Historical Market Data via API

The following historical market data can be fetched directly through the API. Except where a permission is noted, the endpoints below are public and require no API key.

:::tip{title="Note"}
Query ranges, pagination, and rate limits differ per endpoint — refer to each endpoint's documentation. For candlestick, trade, and depth data beyond the API's range, use the web download above.
:::

#### 📈 Futures Market & Funding Rate

| Data Type | Endpoint | Description |
|:---|:---|:---|
| 📊 Open Interest History | [Get Open Interest History](/docs/catalog/market/derivatives#get-open-interest-history) | Historical futures open interest and value at `5m` ~ `1d` granularity |
| 📊 Current Open Interest | [Get Open Interest (OI)](/docs/catalog/market/derivatives) | Current futures open interest |
| 💸 Funding Rate History | [Get Funding Rate History](/docs/catalog/market/derivatives#get-funding-rate-history) | Last 90 days, paginated |
| 💥 Liquidations History | [Get Liquidations History](/docs/catalog/market/derivatives#get-liquidations-history) | Last 3 days only, with some delay |
| 🧮 Index Price Components | [Get Index Price Components](/docs/catalog/market/derivatives#get-index-price-components) | Constituent exchanges and weights of the index price |

#### 🕯️ Candlesticks & Trades

| Data Type | Endpoint | Description |
|:---|:---|:---|
| 🕯️ Recent Candlesticks | [Get Kline/Candlestick](/docs/catalog/market/market-data#get-kline-candlestick) | Latest 1000 candles; market/mark/index/premium types |
| 🕰️ Historical Candlesticks | [Get Kline/Candlestick History](/docs/catalog/market/market-data#get-kline-candlestick-history) | Candles older than 90 days; max 90-day range per query |
| 🔄 Recent Trades | [Get Recent Public Fills](/docs/catalog/market/market-data#get-recent-public-fills) | Recent public fills only; use web download for older data |

#### 📊 Long/Short Ratios & Fund Flow

| Data Type | Endpoint | Description |
|:---|:---|:---|
| ⚖️ Futures Long/Short Ratio | [Get Futures Long Short Ratio Data](/docs/catalog/market/trading-stats#get-futures-long-short-ratio-data) | `5m` ~ `1d` granularity |
| 🐋 Top Trader Position Ratio | [Get Futures Active Long Short Position Data](/docs/catalog/market/trading-stats#get-futures-active-long-short-position-data) | `5m` ~ `1d` granularity |
| 👥 Top Trader Account Ratio | [Get Futures Active Long Short Account Data](/docs/catalog/market/trading-stats#get-futures-active-long-short-account-data) | `5m` ~ `1d` granularity |
| 🔁 Futures Taker Buy/Sell Volume | [Get Futures Active Buy Sell Volume Data](/docs/catalog/market/trading-stats#get-futures-active-buy-sell-volume-data) | `5m` ~ `1d` granularity |
| 💰 Spot Fund Flow | [Get Spot Fund Flow Data](/docs/catalog/market/trading-stats#get-spot-fund-flow-data) | `15m` ~ `1d` granularity |
| 🐋 Spot Whale Net Flow | [Get Spot Whale Net Flow Data](/docs/catalog/market/trading-stats#get-spot-whale-net-flow-data) | Net inflow of large spot traders |
| ⚖️ Margin Long/Short Ratio | [Get Margin Long Short Ratio Data](/docs/catalog/market/trading-stats#get-margin-long-short-ratio-data) | `24h` / `30d` periods |

#### 🛡️ Risk & Borrowing

| Data Type | Endpoint | Description |
|:---|:---|:---|
| 🛡️ Risk Reserve (Daily) | [Get Risk Reserve(Daily)](/docs/catalog/market/trading-risk-rules) | Last 30 days |
| 🛡️ Risk Reserve (Hourly) | [Get Risk Reserve(Hourly)](/docs/catalog/market/trading-risk-rules) | Hourly risk reserve records |
| 🏦 Borrow Interest Rate History | [Get Interest Rate History](/docs/catalog/market/trading-risk-rules#get-interest-rate-history) | Hourly granularity, last 1 month; requires UTA read-only permission |

---

# 历史数据下载指南

如需获取历史数据，可以通过以下两种途径：

1. **网页端下载**：Bitget 网页端提供下载中心，支持导出全部历史数据——多数情况下最早可至 **2018 年 1 月 1 日**。
2. **API 获取**：部分历史行情数据（如合约持仓量历史）网页端无法下载，可通过 API 接口查询；部分行情接口及账户/交易历史接口，仅支持查询近期一段时间内的数据（如 90 天）。

本文将各类历史数据对应到可获取的入口，按需查阅即可。

| 获取方式 | 覆盖范围 | 跳转 |
|:---|:---|:---|
| 🌐 网页端：行情数据 | K 线 / 成交 / 深度 | [↓ 查看](#-行情数据下载) |
| 🌐 网页端：资金费率 | 历史资金费率 | [↓ 查看](#-历史资金费率) |
| 🌐 网页端：个人账户数据 | 经典现货/合约/杠杆、理财订单、统一账户订单 | [↓ 查看](#-个人账户数据) |
| 🔌 API：历史行情数据 | 持仓量、资金费率、K 线、爆仓、风险准备金、借币利率、多空比等 | [↓ 查看](#-通过-api-获取历史行情数据) |

---

## 🌐 网页端下载

### 📊 行情数据下载

:::info{title="下载入口"}
<a href="https://www.bitget.com/zh-CN/data-download"><strong>bitget.com/zh-CN/data-download</strong></a> —— 历史K线、成交、深度数据。
:::

#### 💰 现货

| 数据类型 | 说明 |
|:---|:---|
| 🕯️ K线 | 各交易对的开高低收、成交量等K线数据，包含超出接口默认查询范围的历史数据 |
| 🔄 成交 | 平台公开成交记录，包含超出接口90天查询范围的历史成交 |
| 📉 深度 | 买卖盘挂单深度快照，包含按价格精度合并档位后的深度数据 |

#### 📈 合约

| 数据类型 | 说明 |
|:---|:---|
| 🕯️ K线 | 各合约的开高低收、成交量等K线数据（含指数价格、标记价格），包含超出接口默认查询范围的历史数据 |
| 🔄 成交 | 平台公开成交记录，包含超出接口90天查询范围的历史成交 |
| 📉 深度 | 按价格精度合并档位后的买卖盘深度快照 |

---

### 💸 历史资金费率

:::info{title="下载入口"}
<a href="https://www.bitget.com/zh-CN/trade-info/funding_rate"><strong>bitget.com/zh-CN/trade-info/funding_rate</strong></a> —— 网页端查看并下载合约历史资金费率。
:::

点击链接进入后，切换到「历史资金费率」标签页，即可看到下载按钮。

如需通过程序批量获取，请使用 [获取历史资金费率](/zh-CN/docs/catalog/market/derivatives#get-funding-rate-history) 接口（最近 90 天）。

---

### 📦 个人账户数据

API 接口受限于查询时间窗口（通常是 90 天），如果你需要查询用户更久远的个人订单、成交、资金流水等历史数据，网页端<a href="https://www.bitget.com/zh-CN/asset/export/downOrders">导出中心</a>按账户类型和业务品类，提供了更完整的数据下载能力，覆盖范围比单个 API 接口更广。

:::info{title="下载入口"}
<a href="https://www.bitget.com/zh-CN/asset/export/downOrders"><strong>bitget.com/zh-CN/asset/export/downOrders</strong></a>
:::

#### 💰 经典现货

| 数据类型 | 说明 |
|:---|:---|
| 📋 历史委托 | 账户在现货市场下达的全部委托订单记录，包含已成交、部分成交、已撤销等各类终态订单 |
| 🔄 成交明细 | 现货订单实际成交的明细记录，包含成交价格、数量、手续费等 |
| 💵 资金流水 | 现货账户资金变动流水，如交易扣款/入账、转账、活动奖励等 |
| 🏦 充提记录 | 现货账户的加密货币充值与提现记录 |

#### 📈 经典合约

| 数据类型 | 说明 |
|:---|:---|
| 📋 历史委托 | 合约市场的委托订单记录，包含限价单、市价单等 |
| 📊 历史仓位 | 已平仓的历史持仓记录，包含开平仓价格、盈亏、杠杆倍数等 |
| 🔄 成交明细 | 合约订单的成交明细记录 |
| 💵 资金流水 | 合约账户资金变动流水，如资金费率、已实现盈亏、转账等 |

#### ⚖️ 经典杠杆

| 数据类型 | 说明 |
|:---|:---|
| 📋 历史委托 | 全仓/逐仓杠杆账户的委托订单记录 |
| 💵 资金流水 | 杠杆账户资金变动流水，包含借币、还币、利息扣除等 |

#### 💎 理财订单

| 数据类型 | 说明 |
|:---|:---|
| 🪙 简单赚币 | 活期/定期理财产品的申购、赎回、收益发放记录 |
| ⛓️ 链上赚币 | 链上理财（如 Staking、流动性挖矿）相关订单记录 |
| 🔀 双币投资 | 双币投资产品的申购与结算记录 |
| 🦈 鲨鱼鳍 | 鲨鱼鳍结构化产品的申购与结算记录 |

#### 🏦 统一账户

| 数据类型 | 说明 |
|:---|:---|
| 📋 历史委托 | 统一账户下现货、合约、杠杆等各业务线的委托订单记录 |
| 📊 历史仓位 | 统一账户已平仓的历史持仓记录 |
| 💵 财务记录 | 统一账户资金变动的财务流水 |
| 🔀 兑币记录 | 统一账户内币种闪兑的历史记录 |

:::tip{title="数据范围"}
除非页面另有说明，以上数据最早可导出至 **2018 年 1 月 1 日**。
:::

---

## 🔌 通过 API 获取历史行情数据

以下历史行情数据可直接通过 API 获取。除标注需权限的接口外，其余均为公共接口，无需 API Key。

:::tip{title="提示"}
各接口的可查询时间范围、分页方式与限频规则不同，请以接口文档为准。如需超出接口范围的 K 线、成交、深度数据，请使用上文的网页端下载。
:::

#### 📈 合约行情与资金费率

| 数据类型 | 接口 | 说明 |
|:---|:---|:---|
| 📊 合约持仓量历史 | [获取合约持仓量历史](/zh-CN/docs/catalog/market/derivatives#get-open-interest-history) | 按 `5m` ~ `1d` 粒度查询合约历史持仓量与持仓价值 |
| 📊 当前持仓量 | [获取未平仓合约持仓量](/zh-CN/docs/catalog/market/derivatives) | 查询合约当前持仓量 |
| 💸 历史资金费率 | [获取历史资金费率](/zh-CN/docs/catalog/market/derivatives#get-funding-rate-history) | 最近 90 天，支持分页 |
| 💥 历史爆仓数据 | [获取历史爆仓数据](/zh-CN/docs/catalog/market/derivatives#get-liquidations-history) | 仅返回最近 3 天，数据有一定延迟 |
| 🧮 指数价格成分 | [获取指数价格成分](/zh-CN/docs/catalog/market/derivatives#get-index-price-components) | 指数价格的构成交易所及权重 |

#### 🕯️ K 线与成交

| 数据类型 | 接口 | 说明 |
|:---|:---|:---|
| 🕯️ 近期 K 线 | [获取 K 线数据](/zh-CN/docs/catalog/market/market-data#get-kline-candlestick) | 最近 1000 条，支持行情/标记/指数/溢价 K 线 |
| 🕰️ 历史 K 线 | [获取历史 K 线数据](/zh-CN/docs/catalog/market/market-data#get-kline-candlestick-history) | 可获取 90 天以前的 K 线，单次查询时间范围最大 90 天 |
| 🔄 近期成交 | [获取平台近期成交数据](/zh-CN/docs/catalog/market/market-data#get-recent-public-fills) | 仅近期公开成交，更早数据请网页端下载 |

#### 📊 多空比与资金流向

| 数据类型 | 接口 | 说明 |
|:---|:---|:---|
| ⚖️ 合约多空比 | [获取合约多空比信息](/zh-CN/docs/catalog/market/trading-stats#get-futures-long-short-ratio-data) | `5m` ~ `1d` 粒度 |
| 🐋 大户持仓量多空比 | [获取合约大户持仓量多空比信息](/zh-CN/docs/catalog/market/trading-stats#get-futures-active-long-short-position-data) | `5m` ~ `1d` 粒度 |
| 👥 大户账户多空比 | [获取合约大户账户多空比信息](/zh-CN/docs/catalog/market/trading-stats#get-futures-active-long-short-account-data) | `5m` ~ `1d` 粒度 |
| 🔁 合约主动买卖量 | [获取合约主动买卖量信息](/zh-CN/docs/catalog/market/trading-stats#get-futures-active-buy-sell-volume-data) | `5m` ~ `1d` 粒度 |
| 💰 现货资金流向 | [获取现货资金流向信息](/zh-CN/docs/catalog/market/trading-stats#get-spot-fund-flow-data) | `15m` ~ `1d` 粒度 |
| 🐋 现货大户净流入 | [获取现货大户净流入信息](/zh-CN/docs/catalog/market/trading-stats#get-spot-whale-net-flow-data) | 现货大户资金净流入 |
| ⚖️ 杠杆多空对比 | [获取杠杆多空对比信息](/zh-CN/docs/catalog/market/trading-stats#get-margin-long-short-ratio-data) | `24h` / `30d` 周期 |

#### 🛡️ 风控与借贷

| 数据类型 | 接口 | 说明 |
|:---|:---|:---|
| 🛡️ 风险准备金（日） | [获取风险准备金(天)](/zh-CN/docs/catalog/market/trading-risk-rules) | 最近 30 天记录 |
| 🛡️ 风险准备金（小时） | [获取风险准备金(小时)](/zh-CN/docs/catalog/market/trading-risk-rules) | 小时级风险准备金记录 |
| 🏦 借币利率历史 | [获取借币利率历史](/zh-CN/docs/catalog/market/trading-risk-rules#get-interest-rate-history) | 1 小时粒度，保留最近 1 个月，需统一账户只读权限 |