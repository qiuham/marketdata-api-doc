---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/spot/faqs/market_orders_faq
api_type: Market Data
updated_at: 2026-11-13 20:24:34.672769
---

# MARKET orders

**Disclaimer:**

  * The commissions and prices used here are fictional and do not reflect the actual setup on the live exchange.
  * The explanation pertains to the behavior on the Spot Exchange.



`MARKET` orders allow users to buy or sell an asset at the best available prices and liquidity until the order is fully filled or the order book's liquidity is exhausted.

If you do not have sufficient balance for the order to be completely filled, the order will be rejected.

If the exchange does not have enough liquidity to fill the order, your `MARKET` order will be partially filled to the extent of available liquidity, and the remaining quantity will expire.

If the order expires due to insufficient liquidity, the `status` field of the API response will be `EXPIRED`.

Additionally, if you monitor the User Data Stream, in the payload `ExecutionReport`, you will see that both the Execution Type (`x`) and Order Status (`X`) are marked as `EXPIRED`.

Please refer to the sample payload below.

**Sample API Response:**
    
    
    Code
    
    {
      "symbol": "LTCBNB",
      "orderId": 32,
      "orderListId": -1,
      "clientOrderId": "8LGC97RRgNPVQk979VIhjt",
      "transactTime": 1719467634105,
      "price": "0.00000000",
      "origQty": "6.00000000",
      "executedQty": "4.00000000",
      "cummulativeQuoteQty": "4.00000000",
      "status": "EXPIRED",
      "timeInForce": "GTC",
      "type": "MARKET",
      "side": "BUY",
      "workingTime": 1719467634105,
      "fills": [
        {
          "price": "1.00000000",
          "qty": "2.00000000",
          "commission": "0.00100000",
          "commissionAsset": "BNB",
          "tradeId": 7
        },
        {
          "price": "1.00000000",
          "qty": "2.00000000",
          "commission": "0.00100000",
          "commissionAsset": "BNB",
          "tradeId": 8
        }
      ],
      "selfTradePreventionMode": "NONE"
    }

**Sample User Data Stream Payload:**
    
    
    Code
    
    {
      "e": "executionReport",
      "E": 1719467634107,
      "s": "LTCBNB",
      "c": "8LGC97RRgNPVQk979VIhjt",
      "S": "BUY",
      "o": "MARKET",
      "f": "GTC",
      "q": "6.00000000",
      "p": "0.00000000",
      "P": "0.00000000",
      "F": "0.00000000",
      "g": -1,
      "C": "",
      "x": "NEW",
      "X": "NEW",
      "r": "NONE",
      "i": 32,
      "l": "0.00000000",
      "z": "0.00000000",
      "L": "0.00000000",
      "n": "0",
      "N": null,
      "T": 1719467634105,
      "t": -1,
      "I": 62,
      "w": true,
      "m": false,
      "M": false,
      "O": 1719467634105,
      "Z": "0.00000000",
      "Y": "0.00000000",
      "Q": "0.00000000",
      "W": 1719467634105,
      "V": "NONE"
    },
    {
      "e": "executionReport",
      "E": 1719467634107,
      "s": "LTCBNB",
      "c": "8LGC97RRgNPVQk979VIhjt",
      "S": "BUY",
      "o": "MARKET",
      "f": "GTC",
      "q": "6.00000000",
      "p": "0.00000000",
      "P": "0.00000000",
      "F": "0.00000000",
      "g": -1,
      "C": "",
      "x": "TRADE",
      "X": "PARTIALLY_FILLED",
      "r": "NONE",
      "i": 32,
      "l": "2.00000000",
      "z": "2.00000000",
      "L": "1.00000000",
      "n": "0.00100000",
      "N": "BNB",
      "T": 1719467634105,
      "t": 7,
      "I": 63,
      "w": false,
      "m": false,
      "M": true,
      "O": 1719467634105,
      "Z": "2.00000000",
      "Y": "2.00000000",
      "Q": "0.00000000",
      "W": 1719467634105,
      "V": "NONE"
    },
    {
      "e": "executionReport",
      "E": 1719467634107,
      "s": "LTCBNB",
      "c": "8LGC97RRgNPVQk979VIhjt",
      "S": "BUY",
      "o": "MARKET",
      "f": "GTC",
      "q": "6.00000000",
      "p": "0.00000000",
      "P": "0.00000000",
      "F": "0.00000000",
      "g": -1,
      "C": "",
      "x": "TRADE",
      "X": "PARTIALLY_FILLED",
      "r": "NONE",
      "i": 32,
      "l": "2.00000000",
      "z": "4.00000000",
      "L": "1.00000000",
      "n": "0.00100000",
      "N": "BNB",
      "T": 1719467634105,
      "t": 8,
      "I": 65,
      "w": false,
      "m": false,
      "M": true,
      "O": 1719467634105,
      "Z": "4.00000000",
      "Y": "2.00000000",
      "Q": "0.00000000",
      "W": 1719467634105,
      "V": "NONE"
    },
    {
      "e": "executionReport",
      "E": 1719467634107,
      "s": "LTCBNB",
      "c": "8LGC97RRgNPVQk979VIhjt",
      "S": "BUY",
      "o": "MARKET",
      "f": "GTC",
      "q": "6.00000000",
      "p": "0.00000000",
      "P": "0.00000000",
      "F": "0.00000000",
      "g": -1,
      "C": "",
      "x": "EXPIRED",
      "X": "EXPIRED",
      "r": "NONE",
      "i": 32,
      "l": "0.00000000",
      "z": "4.00000000",
      "L": "0.00000000",
      "n": "0",
      "N": null,
      "T": 1719467634105,
      "t": -1,
      "I": 67,
      "w": false,
      "m": false,
      "M": false,
      "O": 1719467634105,
      "Z": "4.00000000",
      "Y": "0.00000000",
      "Q": "0.00000000",
      "W": 1719467634105,
      "V": "NONE"
    },
    {
      "e": "outboundAccountPosition",
      "E": 1719467634107,
      "u": 1719467634105,
      "B":
      [
        {
          "a": "LTC",
          "f": "3011.11745670",
          "l": "0.00000000"
        },
        {
          "a": "BNB",
          "f": "996.11865670",
          "l": "0.00000000"
        }
      ]
    }

Was this page helpful?

Last modified on November 12, 2026

[Market Data Only URLs](/en/docs/products/spot/faqs/market_data_only)[One Pays the Other (OPO)](/en/docs/products/spot/faqs/opo)

---

# 市价单

**免责声明:**

  * 此处使用的佣金和价格是虚构的，并不反映实际交易所的设置。
  * 解释是针对现货交易所的行为。



`MARKET` 订单允许用户以最佳可用价格和流动性买入或卖出资产，直到订单全部成交或订单簿的流动性耗尽。

如果您的余额不足以完全填充订单，订单将被拒绝。

如果交易所没有足够的流动性来填充订单，您的 `MARKET` 订单将根据当前可用流动性尽可能成交，未成交的剩余部分将自动失效。

如果由于流动性不足订单过期，API 响应的 `status` 字段将显示为 `EXPIRED`。

此外，如果您监听用户数据流，在 payload `ExecutionReport` 中，您会看到执行类型 (`x`) 和订单状态 (`X`) 都标记为 `EXPIRED`。

请参阅下面的示例 payload。

**示例 API 响应:**
    
    
    Code
    
    {
      "symbol": "LTCBNB",
      "orderId": 32,
      "orderListId": -1,
      "clientOrderId": "8LGC97RRgNPVQk979VIhjt",
      "transactTime": 1719467634105,
      "price": "0.00000000",
      "origQty": "6.00000000",
      "executedQty": "4.00000000",
      "cummulativeQuoteQty": "4.00000000",
      "status": "EXPIRED",
      "timeInForce": "GTC",
      "type": "MARKET",
      "side": "BUY",
      "workingTime": 1719467634105,
      "fills": [
        {
          "price": "1.00000000",
          "qty": "2.00000000",
          "commission": "0.00100000",
          "commissionAsset": "BNB",
          "tradeId": 7
        },
        {
          "price": "1.00000000",
          "qty": "2.00000000",
          "commission": "0.00100000",
          "commissionAsset": "BNB",
          "tradeId": 8
        }
      ],
      "selfTradePreventionMode": "NONE"
    }

**示例用户数据流 Payload:**
    
    
    Code
    
    {
      "e": "executionReport",
      "E": 1719467634107,
      "s": "LTCBNB",
      "c": "8LGC97RRgNPVQk979VIhjt",
      "S": "BUY",
      "o": "MARKET",
      "f": "GTC",
      "q": "6.00000000",
      "p": "0.00000000",
      "P": "0.00000000",
      "F": "0.00000000",
      "g": -1,
      "C": "",
      "x": "NEW",
      "X": "NEW",
      "r": "NONE",
      "i": 32,
      "l": "0.00000000",
      "z": "0.00000000",
      "L": "0.00000000",
      "n": "0",
      "N": null,
      "T": 1719467634105,
      "t": -1,
      "I": 62,
      "w": true,
      "m": false,
      "M": false,
      "O": 1719467634105,
      "Z": "0.00000000",
      "Y": "0.00000000",
      "Q": "0.00000000",
      "W": 1719467634105,
      "V": "NONE"
    }
    {
      "e": "executionReport",
      "E": 1719467634107,
      "s": "LTCBNB",
      "c": "8LGC97RRgNPVQk979VIhjt",
      "S": "BUY",
      "o": "MARKET",
      "f": "GTC",
      "q": "6.00000000",
      "p": "0.00000000",
      "P": "0.00000000",
      "F": "0.00000000",
      "g": -1,
      "C": "",
      "x": "TRADE",
      "X": "PARTIALLY_FILLED",
      "r": "NONE",
      "i": 32,
      "l": "2.00000000",
      "z": "2.00000000",
      "L": "1.00000000",
      "n": "0.00100000",
      "N": "BNB",
      "T": 1719467634105,
      "t": 7,
      "I": 63,
      "w": false,
      "m": false,
      "M": true,
      "O": 1719467634105,
      "Z": "2.00000000",
      "Y": "2.00000000",
      "Q": "0.00000000",
      "W": 1719467634105,
      "V": "NONE"
    }
    {
      "e": "executionReport",
      "E": 1719467634107,
      "s": "LTCBNB",
      "c": "8LGC97RRgNPVQk979VIhjt",
      "S": "BUY",
      "o": "MARKET",
      "f": "GTC",
      "q": "6.00000000",
      "p": "0.00000000",
      "P": "0.00000000",
      "F": "0.00000000",
      "g": -1,
      "C": "",
      "x": "TRADE",
      "X": "PARTIALLY_FILLED",
      "r": "NONE",
      "i": 32,
      "l": "2.00000000",
      "z": "4.00000000",
      "L": "1.00000000",
      "n": "0.00100000",
      "N": "BNB",
      "T": 1719467634105,
      "t": 8,
      "I": 65,
      "w": false,
      "m": false,
      "M": true,
      "O": 1719467634105,
      "Z": "4.00000000",
      "Y": "2.00000000",
      "Q": "0.00000000",
      "W": 1719467634105,
      "V": "NONE"
    }
    {
      "e": "executionReport",
      "E": 1719467634107,
      "s": "LTCBNB",
      "c": "8LGC97RRgNPVQk979VIhjt",
      "S": "BUY",
      "o": "MARKET",
      "f": "GTC",
      "q": "6.00000000",
      "p": "0.00000000",
      "P": "0.00000000",
      "F": "0.00000000",
      "g": -1,
      "C": "",
      "x": "EXPIRED",
      "X": "EXPIRED",
      "r": "NONE",
      "i": 32,
      "l": "0.00000000",
      "z": "4.00000000",
      "L": "0.00000000",
      "n": "0",
      "N": null,
      "T": 1719467634105,
      "t": -1,
      "I": 67,
      "w": false,
      "m": false,
      "M": false,
      "O": 1719467634105,
      "Z": "4.00000000",
      "Y": "0.00000000",
      "Q": "0.00000000",
      "W": 1719467634105,
      "V": "NONE"
    }
    {
      "e": "outboundAccountPosition",
      "E": 1719467634107,
      "u": 1719467634105,
      "B":
      [
        {
          "a": "LTC",
          "f": "3011.11745670",
          "l": "0.00000000"
        },
        {
          "a": "BNB",
          "f": "996.11865670",
          "l": "0.00000000"
        }
      ]
    }

此页面是否有帮助？

Last modified on November 12, 2026

[仅提供市场数据的URL](/zh-CN/docs/products/spot/faqs/market_data_only)[一个订单支付另一个订单（One Pays the Other，简称 OPO）](/zh-CN/docs/products/spot/faqs/opo)