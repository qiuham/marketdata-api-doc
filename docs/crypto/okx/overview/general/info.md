---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-general-info
anchor_id: overview-general-info
api_type: API
updated_at: 2026-07-03 19:38:38.952319
---

# General Info

**The rules for placing orders at the exchange level are as follows:**

  * The maximum number of pending orders (including post only orders, limit orders and taker orders that are being processed): 4,000 
  * The maximum number of pending orders per trading symbol is 500, the limit of 500 pending orders applies to the following **order types** : 

    * Limit
    * Market
    * Post only
    * Fill or Kill (FOK)
    * Immediate or Cancel (IOC)
    * Market order with Immediate-or-Cancel order (optimal limit IOC)
    * Take Profit / Stop Loss (TP/SL)
    * Limit and market orders triggered under the order types below: 
      * Take Profit / Stop Loss (TP/SL)
      * Trigger
      * Trailing stop
      * Arbitrage
      * Iceberg
      * TWAP
      * Recurring buy
  * The maximum number of pending spread orders: 500 across all spreads

  * The maximum number of pending algo orders: 

    * TP/SL order: 100 per instrument
    * Trigger order: 500
    * Trailing order: 50
    * Iceberg order: 100
    * TWAP order: 20
  * The maximum number of grid trading

    * Spot grid: 100
    * Contract grid: 100

  

**The rules for trading are as follows:**

  * When the number of maker orders matched with a taker order exceeds the maximum number limit of 1000, the taker order will be canceled. 
    * The limit orders will only be executed with a portion corresponding to 1000 maker orders and the remainder will be canceled.
    * Fill or Kill (FOK) orders will be canceled directly.

  

**The rules for the returning data are as follows:**

  * `code` and `msg` represent the request result or error reason when the return data has `code`, and has not `sCode`;

  * It is `sCode` and `sMsg` that represent the request result or error reason when the return data has `sCode` rather than `code` and `msg`.

  

**`instFamily` and `uly` parameter explanation:**

  * The following explanation is based on the `BTC` contract, other contracts are similar.
  * `uly` is the index, like "BTC-USD", and there is a one-to-many relationship with the settlement and margin currency (`settleCcy`).
  * `instFamily` is the trading instrument family, like `BTC-USD_UM`, and there is a one-to-one relationship with the settlement and margin currency (`settleCcy`).
  * The following table shows the corresponding relationship of `uly`, `instFamily`, `settleCcy` and `instId`.

**Contract Type** | **uly** | **instFamily** | **settleCcy** | **Delivery contract instId** | **Swap contract instId**  
---|---|---|---|---|---  
USDT-margined contract | BTC-USDT | BTC-USDT | USDT | BTC-USDT-250808 | BTC-USDT-SWAP  
USDC-margined contract | BTC-USDC | BTC-USDC | USDC | BTC-USDC-250808 | BTC-USDC-SWAP  
USD-margined contract | BTC-USD | **BTC-USD_UM** | **USDⓈ** | **BTC-USD_UM-250808** | **BTC-USD_UM-SWAP**  
Coin-margined contract | BTC-USD | **BTC-USD** | **BTC** | **BTC-USD-250808** | **BTC-USD-SWAP**  
  
Note:  
1\. USDⓈ represents USD and multiple USD stable coins, like USDC, USDG.  
2\. The settlement and margin currency refers to the `settleCcy` field returned by the [Get instruments](/docs-v5/en/#trading-account-rest-api-get-instruments) endpoint.

---

# 基本信息

**交易所层面的下单规则如下：**

  * 未成交订单（包括 post only，limit和处理中的taker单）的最大挂单数：4,000个
  * 单个交易产品未成交订单的最大挂单数为500个，被计入到 500 笔挂单数量限制的**订单类型** 包括： 

    * 限价委托 (Limit)
    * 市价委托 (Market)
    * 只挂单 (Post only)
    * 全部成交或立即取消 (FOK)
    * 立即成交并取消剩余 (IOC)
    * 市价委托立即成交并取消剩余 (optimal limit IOC)
    * 止盈止损 (TP/SL)
    * 以下类型的订单触发的限价和市价委托： 
      * 止盈止损 (TP/SL)
      * 计划委托 (Trigger)
      * 移动止盈止损 (Trailing stop)
      * 套利下单 (Arbitrage)
      * 冰山策略 (Iceberg)
      * 时间加权策略 (TWAP)
      * 定投 (Recurring buy)
  * 价差订单最大挂单数：所有价差订单挂单合计500个

  * 策略委托订单最大挂单数： 

    * 止盈止损：100个 每个Instrument ID
    * 计划委托：500个  

    * 移动止盈止损：50个  

    * 冰山委托：100个  

    * 时间加权委托：20个  

  * 网格策略最大个数： 

    * 现货网格：100个
    * 合约网格：100个  

  

**交易限制规则如下：**

  * 当taker订单匹配的maker订单数量超过最大限制1000笔时，taker订单将被取消 
    * 限价单仅成交与1000笔maker订单相对应的部分，并取消剩余；
    * 全部成交或立即取消（FOK）订单将直接被取消。

  

**返回数据规则如下：**

  * 当返回数据中，有`code`，且没有`sCode`字段时，`code`和`msg`代表请求结果或者报错原因；

  * 当返回中有`sCode`字段时，代表请求结果或者报错原因的是`sCode`和`sMsg`，而不是`code`和`msg`。

  

**`instFamily` 和 `uly` 参数说明：** \- 以下说明以 `BTC` 合约为例，其他币种的合约同理。 \- `uly` 是指数，如："BTC-USD"，与盈亏结算和保证金币种 (`settleCcy`) 会存在一对多的关系。 \- `instFamily` 是交易品种，如：`BTC-USD_UM`，与盈亏结算和保证金币种 (`settleCcy`) 一一对应。 \- 以下表格详细展示了 `uly`, `instFamily`，`settleCcy` 和 `instId` 的对应关系。

**合约类型** | **uly** | **instFamily** | **settleCcy** | **交割合约 instId** | **永续合约 instId**  
---|---|---|---|---|---  
USDT 本位合约 | BTC-USDT | BTC-USDT | USDT | BTC-USDT-250808 | BTC-USDT-SWAP  
USDC 本位合约 | BTC-USDC | BTC-USDC | USDC | BTC-USDC-250808 | BTC-USDC-SWAP  
USD 本位合约 | BTC-USD | **BTC-USD_UM** | **USDⓈ** | **BTC-USD_UM-250808** | **BTC-USD_UM-SWAP**  
币本位合约 | BTC-USD | **BTC-USD** | **BTC** | **BTC-USD-250808** | **BTC-USD-SWAP**  
  
注意：  
1\. USDⓈ 代表 USD 以及多种 USD 稳定币，如：USD, USDC, USDG。  
2\. 盈亏结算和保证金币种指的[获取交易产品基础信息（私有）](/docs-v5/zh/#trading-account-rest-api-get-instruments)接口返回的 `settleCcy` 字段。