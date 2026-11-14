---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/faqs/sor_faq
api_type: REST
updated_at: 2026-11-13 20:24:37.133927
---

# Smart Order Routing (SOR)

**Disclaimer:**

  * The symbols and values used here are fictional, and do not imply anything about the actual setup on the live exchange.
  * For simplicity, the examples in this document do not include commission.



### What is Smart Order Routing (SOR)?

**Smart Order Routing (SOR)** allows you to potentially get better liquidity by filling an order with liquidity from other order books with the same base asset and interchangeable quote assets. **Interchangeable quote assets** are quote assets with fixed 1 to 1 exchange rate, such as stablecoins pegged to the same fiat currency.

Note that even though the quote assets are interchangeable, when selling the base asset you will always receive the quote asset of the symbol in your order.

When you place an order using SOR, it goes through the eligible order books, looks for best price levels for each order book in that SOR configuration, and takes from those books if possible.

**Note:** If the order using SOR cannot fully fill based on the eligible order books' liquidity, `LIMIT IOC` or `MARKET` orders will immediately expire, while `LIMIT GTC` orders will place the remaining quantity on the order book you originally submitted the order to.

**Example 1**

Let's consider a SOR configuration containing the symbols `BTCUSDT`, `BTCUSDC` and `BTCUSDP`, and the following `ASK` (`SELL` side) order books for those symbols:
    
    
    Code
    
    BTCUSDT quantity 3 price 30,800
    BTCUSDT quantity 3 price 30,500
    
    BTCUSDC quantity 1 price 30,000
    BTCUSDC quantity 1 price 28,000
    
    BTCUSDP quantity 1 price 35,000
    BTCUSDP quantity 1 price 29,000

If you send a `LIMIT GTC BUY` order for `BTCUSDT` with `quantity=0.5` and `price=31000`, you would match with the best SELL price on the BTCUSDT book at 30,500. You would spend 15,250 USDT and receive 0.5 BTC.

If you send a `LIMIT GTC BUY` order _using SOR_ for `BTCUSDT` with `quantity=0.5` and `price=31000`, you would match with the best SELL price across _all symbols in the SOR_ , which is BTCUSDC at price 28,000. You would spend 14,000 USDT (_not_ USDC!) and receive 0.5 BTC.
    
    
    Code
    
    {
        "symbol": "BTCUSDT",
        "orderId": 2,
        "orderListId": -1,
        "clientOrderId": "sBI1KM6nNtOfj5tccZSKly",
        "transactTime": 1689149087774,
        "price": "31000.00000000",
        "origQty": "0.50000000",
        "executedQty": "0.50000000",
        "cummulativeQuoteQty": "14000.00000000",
        "status": "FILLED",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "workingTime": 1689149087774,
        "fills": [
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "28000.00000000",
                "qty": "0.50000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 0
            }
        ],
        "workingFloor": "SOR",
        "selfTradePreventionMode": "NONE",
        "usedSor": true
    }

**Example 2**

Using the same order book as Example 1:
    
    
    Code
    
    BTCUSDT quantity 3 price 30,800
    BTCUSDT quantity 3 price 30,500
    
    BTCUSDC quantity 1 price 30,000
    BTCUSDC quantity 1 price 28,000
    
    BTCUSDP quantity 1 price 35,000
    BTCUSDP quantity 1 price 29,000

If you send a `LIMIT GTC BUY` order for `BTCUSDT` with `quantity=5` and `price=31000`, you would:

  * match with the 3 BTCUSDT at 30,500, and buy 3 BTC for 91,500 USDT
  * then match with the 3 BTCUSDT at 30,800, and buy 2 BTC for 61,600 USDT



In total, you spend 153,100 USDT and receive 5 BTC.

If you send the same `LIMIT GTC BUY` order _using SOR_ for `BTCUSDT` with `quantity=5` and `price=31000`, you would:

  * match with 1 BTCUSDC at 28,000, and buy 1 BTC for 28,000 USDT
  * match with 1 BTCUSDP at 29,000, and buy 1 BTC for 29,000 USDT
  * match with 1 BTCUSDC at 30,000, and buy 1 BTC for 30,000 USDT
  * match with 3 BTCUSDT at 30,500, and buy 2 BTC for 61,000 USDT



In total, you spend 148,000 USDT and receive 5 BTC.
    
    
    Code
    
    {
        "symbol": "BTCUSDT",
        "orderId": 2,
        "orderListId": -1,
        "clientOrderId": "tHonoNjWfOSaKiTygN3bfY",
        "transactTime": 1689146154686,
        "price": "31000.00000000",
        "origQty": "5.00000000",
        "executedQty": "5.00000000",
        "cummulativeQuoteQty": "148000.00000000",
        "status": "FILLED",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "workingTime": 1689146154686,
        "fills": [
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "28000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 0
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "29000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 1
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 2
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30500.00000000",
                "qty": "2.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 3
            }
        ],
        "workingFloor": "SOR",
        "selfTradePreventionMode": "NONE",
        "usedSor": true
    }

**Example 3**

Using the same order book as Example 1 and 2:
    
    
    Code
    
    BTCUSDT quantity 3 price 30,800
    BTCUSDT quantity 3 price 30,500
    
    BTCUSDC quantity 1 price 30,000
    BTCUSDC quantity 1 price 28,000
    
    BTCUSDP quantity 1 price 35,000
    BTCUSDP quantity 1 price 29,000

If you send a `MARKET BUY` order for `BTCUSDT` _using SOR_ with `quantity=11`, there is only 10 BTC in total available across all eligible order books. Once all the order books in SOR configuration have been exhausted, the remaining quantity of 1 expires.
    
    
    Code
    
    {
        "symbol": "BTCUSDT",
        "orderId": 2,
        "orderListId": -1,
        "clientOrderId": "jdFYWTNyzplbNvVJEzQa0o",
        "transactTime": 1689149513461,
        "price": "0.00000000",
        "origQty": "11.00000000",
        "executedQty": "10.00000000",
        "cummulativeQuoteQty": "305900.00000000",
        "status": "EXPIRED",
        "timeInForce": "GTC",
        "type": "MARKET",
        "side": "BUY",
        "workingTime": 1689149513461,
        "fills": [
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "28000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 0
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "29000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 1
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 2
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30500.00000000",
                "qty": "3.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 3
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30800.00000000",
                "qty": "3.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 4
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "35000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 5
            }
        ],
        "workingFloor": "SOR",
        "selfTradePreventionMode": "NONE",
        "usedSor": true
    }

**Example 4**

Let's consider a SOR configuration containing the symbols `BTCUSDT`, `BTCUSDC` and `BTCUSDP` and the following `BID` (`BUY` side) order book for those symbols:
    
    
    Code
    
    BTCUSDT quantity 5 price 29,500
    
    BTCUSDC quantity 5 price 35,000
    BTCUSDC quantity 5 price 30,000
    
    BTCUSDP quantity 5 price 28,000

If you send a `LIMIT GTC SELL` order for `BTCUSDT` with `price=29000` and `quantity=10`, you would sell 5 BTC and receive 147,500 USDT. Since there is no better price available on the BTCUSDT book, the remaining (unfilled) quantity of the order will rest there at the price of 29,000.

If you send a `LIMIT GTC SELL` order _using SOR_ for `BTCUSDT`, you would:

  * match with 5 BTCUSDC at 35,000 and sell 5 BTC for 175,000 USDT
  * match with 5 BTCUSDC at 30,000 and sell 5 BTC for 150,000 USDT



In total, you sell 10 BTC and receive 325,000 USDT.
    
    
    Code
    
    {
        "symbol": "BTCUSDT",
        "orderId": 1,
        "orderListId": -1,
        "clientOrderId": "W1iXSng1fS77dvanQJDGA5",
        "transactTime": 1689147920113,
        "price": "29000.00000000",
        "origQty": "10.00000000",
        "executedQty": "10.00000000",
        "cummulativeQuoteQty": "325000.00000000",
        "status": "FILLED",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "SELL",
        "workingTime": 1689147920113,
        "fills": [
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "35000.00000000",
                "qty": "5.00000000",
                "commission": "0.00000000",
                "commissionAsset": "USDT",
                "tradeId": -1,
                "allocId": 0
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30000.00000000",
                "qty": "5.00000000",
                "commission": "0.00000000",
                "commissionAsset": "USDT",
                "tradeId": -1,
                "allocId": 1
            }
        ],
        "workingFloor": "SOR",
        "selfTradePreventionMode": "NONE",
        "usedSor": true
    }

**Summary: The goal of SOR is to potentially access better liquidity across order books with interchangeable quote assets. Better liquidity access can fill orders more fully and at better prices during an order's taker phase.**

### What symbols support SOR?

You can find the current SOR configuration in Exchange Information (`GET /api/v3/exchangeInfo` for Rest, and `exchangeInfo` on Websocket API).
    
    
    Code
    
    {
      "sors": [
        {
          "baseAsset": "BTC",
          "symbols": ["BTCUSDT", "BTCUSDC", "BTCUSDP"]
        }
      ]
    }

The `sors` field is optional. It is omitted in responses if SOR is not available.

### How do I place an order using SOR?

On the Rest API, the request is `POST /api/v3/sor/order`.

On the WebSocket API, the request is `sor.order.place`.

### In the API response, there's a field called `workingFloor`. What does that field mean?

This is a term used to determine where the order's last activity occurred (filling, expiring, or being placed as new, etc.).

If the `workingFloor` is `SOR`, this means your order interacted with other eligible order books in the SOR configuration.

If the `workingFloor` is `EXCHANGE`, this means your order interacted on the order book that you sent that order to.

### In the API response, `fills` contain fields `matchType` and `allocId`. What do they mean?

`matchType` field indicates a non-standard order fill.

When your order is filled by SOR, you will see `matchType: ONE_PARTY_TRADE_REPORT`, indicating that you did not trade directly on the exchange (`tradeId: -1`). Instead your order is filled by _allocations_.

`allocId` field identifies the allocation so that you can query it later.

### What are allocations?

**An allocation** is a transfer of an asset from the exchange to your account. For example, when SOR takes liquidity from eligible order books, your order is filled by allocations. In this case you don't trade directly, but rather receive allocations from SOR corresponding to the trades made by SOR on your behalf.
    
    
    Code
    
    [
      {
        symbol: "BTCUSDT", // Symbol the order was submitted to
        allocationId: 0,
        allocationType: "SOR",
        orderId: 2,
        orderListId: -1,
        price: "30000.00000000", // Price of the fill
        qty: "5.00000000", // Quantity of the fill
        quoteQty: "150000.00000000",
        commission: "0.00000000",
        commissionAsset: "BTC",
        time: 1688379272280, // Time the allocation occurred
        isBuyer: true,
        isMaker: false,
        isAllocator: false,
      },
    ];

### How do I query orders that used SOR?

You can find them the same way you query any other order. The main difference is that in the response for an order that used SOR there are two extra fields: `usedSor` and `workingFloor`.

### How do I get details of my fills for orders that used SOR?

When SOR orders trade against order books other than the symbol submitted with the order, the order is filled with an **allocation** and not a trade. Orders placed with SOR can potentially have both allocations and trades.

In the API response, you can review the `fills` fields. Allocations have an `allocId` and `"matchType": "ONE_PARTY_TRADE_REPORT"`, while trades will have a non-negative `tradeId`.

Allocations can be queried using `GET /api/v3/myAllocations` (Rest API) or `myAllocations` (WebSocket API).

Trades can be queried using `GET /api/v3/myTrades` (Rest API) or `myTrades` (WebSocket API).

Was this page helpful?

Last modified on November 12, 2026

[Simple Binary Encoding (SBE)](/en/docs/products/spot/faqs/sbe_faq)[SPOT API Glossary](/en/docs/products/spot/faqs/spot_glossary)

---

# 智能订单路由 (SOR)

**声明:**

  * 这里使用的符号和数值是虚构的，并不意味着真实交易所中的设置。
  * 为简单起见，本文档中的示例不包括佣金。



### 什么是智能订单路由 (SOR)?

**智能订单路由** （Smart Order Routing，简称SOR）允许客户通过使用具有相同基础资产(`base asset `)和可互换报价资产(`interchangeable quote assets`)的其他订单簿(order books)中的流动性来潜在获得更好的流动性。可互换报价资产是具有固定的1比1兑换率的报价资产，例如与同一法定货币挂钩的稳定币。

请注意，尽管报价资产(quote assets)是可互换的，但在出售基础资产(base asset)时，您将始终收到订单中交易对(symbol)对应的报价资产(quote asset)。

当您使用`SOR`下单时，它会在SOR配置的订单簿(order books)里，寻找每个订单簿的最佳价格水平，并在可能的情况下从中交易。

**注意：** 如果使用SOR的订单无法根据符合条件的订单簿流动性完全成交，IOC限价单(`LIMIT IOC`)或市价单(`MARKET`)将立即过期，而GTC限价单(`LIMIT GTC`)将把剩余数量放置在您最初提交订单的订单簿(order book)上。

**示例 1**

让我们考虑一个包含交易对`BTCUSDT`，`BTCUSDC`和`BTCUSDP`的SOR配置，并给出以下这些符号的卖出(`ASK`)方向的订单簿:
    
    
    Code
    
    BTCUSDT quantity 3 price 30,800
    BTCUSDT quantity 3 price 30,500
    
    BTCUSDC quantity 1 price 30,000
    BTCUSDC quantity 1 price 28,000
    
    BTCUSDP quantity 1 price 35,000
    BTCUSDP quantity 1 price 29,000

如果您以价格为31000、数量为0.5的限价挂单买入`BTCUSDT`，并且在`BTCUSDT`的订单簿中找到最佳的卖出价格为30,500 USDT，您将花费15,250 USDT 并收到0.5 BTC。

如果您通过使用SOR下达了一笔GTC限价买单(`LIMIT GTC BUY`)，购买`BTCUSDT`，数量为 0.5，价格为 31000，您将与SOR涵盖的所有交易对中最佳的卖出价格相匹配，即`BTCUSDC`，价格为 28,000。您将花费 14,000 USDT（不是 USDC！），并收到 0.5 BTC。
    
    
    Code
    
    {
        "symbol": "BTCUSDT",
        "orderId": 2,
        "orderListId": -1,
        "clientOrderId": "sBI1KM6nNtOfj5tccZSKly",
        "transactTime": 1689149087774,
        "price": "31000.00000000",
        "origQty": "0.50000000",
        "executedQty": "0.50000000",
        "cummulativeQuoteQty": "14000.00000000",
        "status": "FILLED",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "workingTime": 1689149087774,
        "fills": [
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "28000.00000000",
                "qty": "0.50000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 0
            }
        ],
        "workingFloor": "SOR",
        "selfTradePreventionMode": "NONE",
        "usedSor": true
    }

**示例 2**

使用示例1中同样的订单簿:
    
    
    Code
    
    BTCUSDT quantity 3 price 30,800
    BTCUSDT quantity 3 price 30,500
    
    BTCUSDC quantity 1 price 30,000
    BTCUSDC quantity 1 price 28,000
    
    BTCUSDP quantity 1 price 35,000
    BTCUSDP quantity 1 price 29,000

如果您下达一笔GTC限价买单(`LIMIT GTC BUY`)购买`BTCUSDT`，数量为 5，价格为 31,000，则：

  * 与 `BTCUSDT` 订单簿中价格为 30,500 USDT 的 3 个 `BTCUSDT` 成交，以 91,500 USDT 的价格购买 3 个 BTC。
  * 然后与 `BTCUSDT` 订单簿中价格为 30,800 USDT 的 3 个 `BTCUSDT` 成交，以 61,600 USDT 的价格购买 2 个 BTC。



总计您花费了 153,100 USDT 并获得了 5 BTC。

如果您通过使用SOR下达相同的GTC限价买单(`LIMIT GTC BUY`)购买 `BTCUSDT`，数量为 5，价格为 31,000，则：

  * 与 `BTCUSDC` 订单簿中价格为 28,000 的 1 个 BTCUSDC 成交，以 28,000 USDT 的价格购买 1 个 BTC。
  * 与 `BTCUSDP` 订单簿中价格为 29,000 的 1 个 BTCUSDP 成交，以 29,000 USDT 的价格购买 1 个 BTC。
  * 与 `BTCUSDC` 订单簿中价格为 30,000 的 1 个 BTCUSDC 成交，以 30,000 USDT 的价格购买 1 个 BTC。
  * 与 `BTCUSDT` 订单簿中价格为 30,500 的 3 个 BTCUSDT 成交，以 61,000 USDT 的价格购买 2 个 BTC。



总计您花费了 148,000 USDT 并获得了 5 BTC。
    
    
    Code
    
    {
        "symbol": "BTCUSDT",
        "orderId": 2,
        "orderListId": -1,
        "clientOrderId": "tHonoNjWfOSaKiTygN3bfY",
        "transactTime": 1689146154686,
        "price": "31000.00000000",
        "origQty": "5.00000000",
        "executedQty": "5.00000000",
        "cummulativeQuoteQty": "148000.00000000",
        "status": "FILLED",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "workingTime": 1689146154686,
        "fills": [
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "28000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 0
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "29000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 1
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 2
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30500.00000000",
                "qty": "2.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 3
            }
        ],
        "workingFloor": "SOR",
        "selfTradePreventionMode": "NONE",
        "usedSor": true
    }

**示例 3**

使用示例1和2中同样的订单簿:
    
    
    Code
    
    BTCUSDT quantity 3 price 30,800
    BTCUSDT quantity 3 price 30,500
    
    BTCUSDC quantity 1 price 30,000
    BTCUSDC quantity 1 price 28,000
    
    BTCUSDP quantity 1 price 35,000
    BTCUSDP quantity 1 price 29,000

如果您通过使用SOR下市价买单(`MARKET` `BUY`) 购买 `BTCUSDT`，数量为 11，但在所有符合条件的订单簿中总共只有 10 个BTC可供交易。一旦所有SOR配置中的订单簿都耗尽了，剩余的数量1将过期。
    
    
    Code
    
    {
        "symbol": "BTCUSDT",
        "orderId": 2,
        "orderListId": -1,
        "clientOrderId": "jdFYWTNyzplbNvVJEzQa0o",
        "transactTime": 1689149513461,
        "price": "0.00000000",
        "origQty": "11.00000000",
        "executedQty": "10.00000000",
        "cummulativeQuoteQty": "305900.00000000",
        "status": "EXPIRED",
        "timeInForce": "GTC",
        "type": "MARKET",
        "side": "BUY",
        "workingTime": 1689149513461,
        "fills": [
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "28000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 0
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "29000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 1
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 2
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30500.00000000",
                "qty": "3.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 3
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30800.00000000",
                "qty": "3.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 4
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "35000.00000000",
                "qty": "1.00000000",
                "commission": "0.00000000",
                "commissionAsset": "BTC",
                "tradeId": -1,
                "allocId": 5
            }
        ],
        "workingFloor": "SOR",
        "selfTradePreventionMode": "NONE",
        "usedSor": true
    }

**示例 4**

假设有一个包含 `BTCUSDT`, `BTCUSDC` 和 `BTCUSDP` 交易对的SOR配置, 以及下面这些交易对买方(`BID`)的订单簿：
    
    
    Code
    
    BTCUSDT quantity 5 price 29,500
    
    BTCUSDC quantity 5 price 35,000
    BTCUSDC quantity 5 price 30,000
    
    BTCUSDP quantity 5 price 28,000

如果您在`BTCUSDT`下一笔GTC限价卖单(`LIMIT GTC SELL`) 订单，价格是29000, 卖出10 BTC，那么您将卖出 5 个 BTC 并获得 147,500 USDT。由于`BTCUSDT`订单簿上没有更好的价格可用，订单的剩余（未成交）数量将会以29,000的价格保持在订单簿上。

如果您通过使用SOR下GTC限价卖单(`LIMIT GTC SELL`) 卖出 `BTCUSDT`，则会：

  * 与 `BTCUSDC` 订单簿中价格为 35,000 的 5 个 BTCUSDC 成交，以 175,000 USDT 的价格出售 5 个 BTC。
  * 与 `BTCUSDC` 订单簿中价格为 30,000 的 5 个 BTCUSDC 成交，以 150,000 USDT 的价格出售 5 个 BTC。



总计您卖出 10 个 BTC 并获得 325,000 USDT。
    
    
    Code
    
    {
        "symbol": "BTCUSDT",
        "orderId": 1,
        "orderListId": -1,
        "clientOrderId": "W1iXSng1fS77dvanQJDGA5",
        "transactTime": 1689147920113,
        "price": "29000.00000000",
        "origQty": "10.00000000",
        "executedQty": "10.00000000",
        "cummulativeQuoteQty": "325000.00000000",
        "status": "FILLED",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "SELL",
        "workingTime": 1689147920113,
        "fills": [
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "35000.00000000",
                "qty": "5.00000000",
                "commission": "0.00000000",
                "commissionAsset": "USDT",
                "tradeId": -1,
                "allocId": 0
            },
            {
                "matchType": "ONE_PARTY_TRADE_REPORT",
                "price": "30000.00000000",
                "qty": "5.00000000",
                "commission": "0.00000000",
                "commissionAsset": "USDT",
                "tradeId": -1,
                "allocId": 1
            }
        ],
        "workingFloor": "SOR",
        "selfTradePreventionMode": "NONE",
        "usedSor": true
    }

**概要：SOR的目标是潜在地在具有可互换报价资产(`interchangeable quote assets`)的订单簿之间获得更好的流动性。更好的流动性可以使订单以更好的价格，并更充分成交。**

### 什么交易对支持SOR?

当前SOR配置可以在交易所信息接口查询(Restful接口`GET /api/v3/exchangeInfo`, Websocket API的 `exchangeInfo`).
    
    
    Code
    
    {
      "sors": [
        {
          "baseAsset": "BTC",
          "symbols": ["BTCUSDT", "BTCUSDC", "BTCUSDP"]
        }
      ]
    }

`sors` 字段是可选的。如果 SOR 不可用， 该字段在响应中会被忽略。

### 如何下SOR订单?

通过Rest API接口 `POST /api/v3/sor/order`.

通过WebSocket API接口 `sor.order.place`.

### 在API响应里, 有个字段workingFloor是什么意思?

这是一个用于确定订单的最后更新操作（成交、过期或作为新订单下达等）的术语。

如果 workingFloor 是 SOR，这表示您的订单与SOR配置中的其他符合条件的订单簿进行了交互。

如果 workingFloor 是 EXCHANGE，这表示您的订单在您发送该订单的订单簿上进行了交互。

### 如果查询订单是否使用过SOR?

您可以像查询任何其他订单一样来查询。主要的区别是对于使用SOR的订单，在响应中会有两个额外的字段：`usedSor` 和 `workingFloor`。

### 什么是分配?

**分配** 是从交易所转移资产到您的账户。例如，当SOR从符合条件的订单簿中获取流动性时，您的订单将通过分配来填充。在这种情况下，您不直接进行交易，而是通过SOR代表您进行交易，并接收对应于SOR为您进行的交易的分配。
    
    
    Code
    
    [
      {
        symbol: "BTCUSDT", // Symbol the order was submitted to
        allocationId: 0,
        allocationType: "SOR",
        orderId: 2,
        orderListId: -1,
        price: "30000.00000000", // Price of the fill
        qty: "5.00000000", // Quantity of the fill
        quoteQty: "150000.00000000",
        commission: "0.00000000",
        commissionAsset: "BTC",
        time: 1688379272280, // Time the allocation occurred
        isBuyer: true,
        isMaker: false,
        isAllocator: false,
      },
    ];

### 如何获取使用SOR的订单成交细节？

当SOR订单与非提交订单的订单簿进行交易时，订单将通过分配（allocation）而不是交易(trade)来成交。使用SOR下达的订单可能同时拥有分配和交易。

在API响应中，您可以查看`fills`字段。分配具有`allocId`和`matchType`: "ONE_PARTY_TRADE_REPORT"，而交易将具有非负的`tradeId`。

您可以使用以下方式查询分配和交易：

查询分配：使用Rest API接口 `GET /api/v3/myAllocations` 或 WebSocket API 的 `myAllocations`。

查询交易：使用Rest API接口 `GET /api/v3/myTrades` 或 WebSocket API 的 `myTrades`。

此页面是否有帮助？

Last modified on November 12, 2026

[简单二进制编码（SBE）](/zh-CN/docs/products/spot/faqs/sbe_faq)[现货交易API术语表](/zh-CN/docs/products/spot/faqs/spot_glossary)