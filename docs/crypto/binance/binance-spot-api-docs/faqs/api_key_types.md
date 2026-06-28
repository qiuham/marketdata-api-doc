---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/faqs/api_key_types
api_type: REST
updated_at: 2026-05-27 18:53:50.928610
---

# Commission Rates

**Disclaimer:**

  * The commissions and prices used here are fictional, and do not imply anything about the actual setup on the live exchange.
  * This applies only for the SPOT Exchange.



### What are Commission Rates?[​](/docs/binance-spot-api-docs/faqs/commission_faq#what-are-commission-rates "Direct link to What are Commission Rates?")

These are the rates that determine the commission to be paid on trades when your order fills for any amount.

### What are the different types of rates?[​](/docs/binance-spot-api-docs/faqs/commission_faq#what-are-the-different-types-of-rates "Direct link to What are the different types of rates?")

There are 3 types:

  * `standardCommission` \- Standard commission rates on trades from the order.
  * `taxCommission` \- Tax commission rates on trades from the order.
  * `specialCommission` \- Extra commission that will be added in specific circumstances.



Standard commission rate may be reduced, depending on promotions for specific trading pairs, applicable discounts, etc.

### How do I know what the commission rates are?[​](/docs/binance-spot-api-docs/faqs/commission_faq#how-do-i-know-what-the-commission-rates-are "Direct link to How do I know what the commission rates are?")

You can find them using the following requests:

REST API: `GET /api/v3/account/commission`

WebSocket API: `account.commission`

You can also find out the commission rates to a trade from an order using the test order requests with `computeCommissionRates`.

### What is the difference between the response sending a test order with `computeCommissionRates` vs the response from querying commission rates?[​](/docs/binance-spot-api-docs/faqs/commission_faq#what-is-the-difference-between-the-response-sending-a-test-order-with-computecommissionrates-vs-the-response-from-querying-commission-rates "Direct link to what-is-the-difference-between-the-response-sending-a-test-order-with-computecommissionrates-vs-the-response-from-querying-commission-rates")

A test order with `computeCommissionRates` returns detailed commission rates for that specific order:
    
    
    {  
        "standardCommissionForOrder": {  
            "maker": "0.00000050",  
            "taker": "0.00000060"  
        },  
        "specialCommissionForOrder": {  
            "maker": "0.05000000",  
            "taker": "0.06000000"  
        },  
        "taxCommissionForOrder": {  
            "maker": "0.00000228",  
            "taker": "0.00000230"  
        },  
        "discount": {  
            "enabledForAccount": true,  
            "enabledForSymbol": true,  
            "discountAsset": "BNB",  
            "discount": "0.25000000"  
        }  
    }  
    

Note: It does not show buyer/seller commissions separately, as these are already taken into account based on the order side.

In contrast, querying commission rates returns your current commission rates for the symbol on your account.
    
    
    {  
        "symbol": "BTCUSDT",  
        "standardCommission": {  
            "maker": "0.00000040",  
            "taker": "0.00000050",  
            "buyer": "0.00000010",  
            "seller": "0.00000010"  
        },  
        "specialCommission": {  
            "maker": "0.04000000",  
            "taker": "0.05000000",  
            "buyer": "0.01000000",  
            "seller": "0.01000000"  
        },  
        "taxCommission": {  
            "maker": "0.00000128",  
            "taker": "0.00000130",  
            "buyer": "0.00000100",  
            "seller": "0.00000100"  
        },  
        "discount": {  
            "enabledForAccount": true,  
            "enabledForSymbol": true,  
            "discountAsset": "BNB",  
            "discount": "0.25000000"  
        }  
    }  
    

### How is the commission calculated?[​](/docs/binance-spot-api-docs/faqs/commission_faq#how-is-the-commission-calculated "Direct link to How is the commission calculated?")

Using an example commission configuration:
    
    
    {  
        "symbol": "BTCUSDT",  
        "standardCommission": {  
            "maker": "0.00000010",  
            "taker": "0.00000020",  
            "buyer": "0.00000030",  
            "seller": "0.00000040"  
        },  
        "specialCommission": {  
            "maker": "0.01000000",  
            "taker": "0.02000000",  
            "buyer": "0.03000000",  
            "seller": "0.04000000"  
        },  
        "taxCommission": {  
            "maker": "0.00000112",  
            "taker": "0.00000114",  
            "buyer": "0.00000118",  
            "seller": "0.00000116"  
        },  
        "discount": {  
            "enabledForAccount": true,  
            "enabledForSymbol": true,  
            "discountAsset": "BNB",  
            "discount": "0.25000000"  
        }  
    }  
    

If you placed an order with the following parameters which took immediately and fully filled in a single trade:

Parameter| Value  
---|---  
symbol| BTCUSDT  
price| 35,000  
quantity| 0.49975  
side| SELL  
type| MARKET  
  
Since you sold BTC for USDT, the commission will be paid either in USDT or BNB.

When standard commission is calculated, the received amount is multiplied with the sum of the rates.

Since this order is on the `SELL` side, the received amount is the notional value. (For orders on the `BUY` side, the received amount would be `quantity`.) The order type was `MARKET`, making this the taker order for the trade.
    
    
    Standard Commission = Notional value * (taker + seller)  
                        = (35000 * 0.49975) * (0.00000020 + 0.00000040)  
                        = 17491.25000000 * 0.00000060  
                        = 0.01049475 USDT  
    

Tax commission (if applicable) is calculated similarly:
    
    
    Tax commission = Notional value * (taker + seller)  
                   = (35000 * 0.49975) * (0.00000114 + 0.00000116)  
                   = 17491.25000000 * 0.00000230  
                   = 0.04022988 USDT  
    

Special commission (if applicable) is calculated as:
    
    
    Special commission = Notional value * (taker + seller)  
                   = (35000 * 0.49975) * (0.02000000 + 0.04000000)  
                   = 17491.25000000 * 0.06000030  
                   = 1049.47500000 USDT  
    

If not paying in BNB, the total commission are summed up and deducted from your received amount of `USDT`.

Since `enabledforAccount` and `enabledForSymbol` under `discount` is set to `true`, this means the commission will be paid in BNB assuming you have a sufficient balance.

If paying with BNB, then the standard commission will be reduced based on the `discount`.

First the standard commission and tax commission will be converted into BNB based on the exchange rate. For this example, assume that 1 BNB = 260 USDT.
    
    
    Standard commission (Discounted and in BNB) = (Standard commission * BNB exchange rate) * discount  
                                                = (0.01049475 * 1/260) * 0.25  
                                                = 0.000040364 * 0.25  
                                                = 0.000010091  
    

Note that the discount **does not apply to tax commissions or special commissions**.
    
    
    Tax Commission (in BNB) = Tax commission * BNB exchange rate  
                            = 0.04022988 * (1/260)  
                            = 0.00015473  
      
    Special Commission (in BNB) = Special commission * BNB exchange rate  
                            = 1049.47500000 * (1/260)  
                            = 4.036442308  
      
    
    
    
    Total Commission (in BNB) = Standard commission (Discounted) + Tax commission (in BNB) + Special commission (in BNB)  
                              = 0.000010091 + 0.00015473 + 4.036442308  
                              = 4.036607129  
    

If you do not have enough BNB to pay the discounted commission, the full commission will be taken out of your received amount of USDT instead.

---

# 佣金率

**免责声明：**

  * 本文所用的佣金和价格都是虚构的，并不代表现实交易中的设置。
  * 本内容只适用于现货交易所。



### 什么是佣金率？[​](/docs/zh-CN/binance-spot-api-docs/faqs/commission_faq#什么是佣金率 "什么是佣金率？的直接链接")

这些比率是用来决定当您的任何金额订单成交后，您所需要支付的佣金金额数目。

### 佣金率有哪些不同的类型？[​](/docs/zh-CN/binance-spot-api-docs/faqs/commission_faq#佣金率有哪些不同的类型 "佣金率有哪些不同的类型？的直接链接")

有以下3种类型：

  * 标准佣金（`standardCommission`） - 来自订单的标准交易佣金率。
  * 税务佣金（`taxCommission`） - 来自订单的税费佣金率。
  * 特殊佣金（`specialCommission`） - 在特定情况下，将会被收取的额外佣金。



标准佣金率可能会被降低，具体情况取决于特定交易对的促销活动、可适用的折扣等。

### 我怎么才能知道佣金率是多少？[​](/docs/zh-CN/binance-spot-api-docs/faqs/commission_faq#我怎么才能知道佣金率是多少 "我怎么才能知道佣金率是多少？的直接链接")

您可以通过以下请求找到它们：

REST API: `GET /api/v3/account/commission`

WebSocket API: `account.commission`

您也可以通过在测试订单请求中使用 `computeCommissionRates` 来找出订单交易的佣金比率。

### 在发送测试订单中使用`computeCommissionRates`得到的响应与查询佣金率的响应之间有什么不同？[​](/docs/zh-CN/binance-spot-api-docs/faqs/commission_faq#在发送测试订单中使用computecommissionrates得到的响应与查询佣金率的响应之间有什么不同 "在发送测试订单中使用computecommissionrates得到的响应与查询佣金率的响应之间有什么不同的直接链接")

使用 `computeCommissionRates` 的测试订单会返回该特定订单的详细佣金率：
    
    
    {  
        "standardCommissionForOrder": {  
            "maker": "0.00000050",  
            "taker": "0.00000060"  
        },  
        "specialCommissionForOrder": {  
            "maker": "0.05000000",  
            "taker": "0.06000000"  
        },  
        "taxCommissionForOrder": {  
            "maker": "0.00000228",  
            "taker": "0.00000230"  
        },  
        "discount": {  
            "enabledForAccount": true,  
            "enabledForSymbol": true,  
            "discountAsset": "BNB",  
            "discount": "0.25000000"  
        }  
    }  
    

注意：因为买方/卖方佣金已根据订单方向计算在内，所以买方/卖方佣金不会被单独显示出来。

相反，查询佣金率的响应则提供了针对于您的帐户中该交易对的当前佣金率。
    
    
    {  
        "symbol": "BTCUSDT",  
        "standardCommission": {  
            "maker": "0.00000040",  
            "taker": "0.00000050",  
            "buyer": "0.00000010",  
            "seller": "0.00000010"  
        },  
        "specialCommission": {  
            "maker": "0.04000000",  
            "taker": "0.05000000",  
            "buyer": "0.01000000",  
            "seller": "0.01000000"  
        },  
        "taxCommission": {  
            "maker": "0.00000128",  
            "taker": "0.00000130",  
            "buyer": "0.00000100",  
            "seller": "0.00000100"  
        },  
        "discount": {  
            "enabledForAccount": true,  
            "enabledForSymbol": true,  
            "discountAsset": "BNB",  
            "discount": "0.25000000"  
        }  
    }  
    

### 佣金是怎么计算的？[​](/docs/zh-CN/binance-spot-api-docs/faqs/commission_faq#佣金是怎么计算的 "佣金是怎么计算的？的直接链接")

以下面的这个佣金配置为例：
    
    
    {  
        "symbol": "BTCUSDT",  
        "standardCommission": {  
            "maker": "0.00000010",  
            "taker": "0.00000020",  
            "buyer": "0.00000030",  
            "seller": "0.00000040"  
        },  
        "specialCommission": {  
            "maker": "0.01000000",  
            "taker": "0.02000000",  
            "buyer": "0.03000000",  
            "seller": "0.04000000"  
        },  
        "taxCommission": {  
            "maker": "0.00000112",  
            "taker": "0.00000114",  
            "buyer": "0.00000118",  
            "seller": "0.00000116"  
        },  
        "discount": {  
            "enabledForAccount": true,  
            "enabledForSymbol": true,  
            "discountAsset": "BNB",  
            "discount": "0.25000000"  
        }  
    }  
    

如果您使用了下列参数来下一个订单，该订单立即执行并通过一次交易就全部成交：

参数| 取值  
---|---  
symbol| BTCUSDT  
price| 35,000  
quantity| 0.49975  
side| SELL  
type| MARKET  
  
由于您卖出了 `BTC` 来换取 `USDT` ，佣金将以 `USDT` 或 `BNB` 形式支付。

在计算标准佣金（`standard commission`）时，所接收的金额会与费率之和相乘。

由于此订单在`卖方` （`SELL`）一侧，所接收的金额是`名义价值` （`notional value`）。 对于`买方` （`BUY`）一侧的订单，所接收的金额则是`数量` （`quantity`）。 因为订单类型为`市价` （`MARKET`）的关系，使得此订单成为交易的`吃单方` （`taker`）。
    
    
    标准佣金 = 名义价值 * (taker + seller)  
                        = (35000 * 0.49975) * (0.00000020 + 0.00000040)  
                        = 17491.25000000 * 0.00000060  
                        = 0.01049475 USDT  
    

如果适用，税务佣金（`tax commission`）的计算方式类似于标准佣金：
    
    
    税务佣金 = 名义价值 * (taker + seller)  
                   = (35000 * 0.49975) * (0.00000114 + 0.00000116)  
                   = 17491.25000000 * 0.00000230  
                   = 0.04022988 USDT  
    

如果适用，特殊佣金（`special commission`）的计算方式如下：
    
    
    特殊佣金 = 名义价值 * (taker + seller)  
                   = (35000 * 0.49975) * (0.02000000 + 0.04000000)  
                   = 17491.25000000 * 0.06000030  
                   = 1049.47500000 USDT  
    

如果您不使用`BNB`支付佣金，佣金总数会被加起来并从您所接收的`USDT`金额中扣除。

由于`discount`下的`enabledforAccount`和`enabledForSymbol`被设置为`true`，这意味着如果您所持有的余额足够，那么佣金将用`BNB`支付。

如果用`BNB`支付，那么基于折扣（`discount`），您所需要支付的标准佣金将会减少。

首先，标准佣金和税务佣金将根据汇率转换成`BNB`。在这个例子中，假设1 BNB = 260 USDT。
    
    
    标准佣金(打折后以BNB支付) = (标准佣金 * BNB 汇率) * 折扣  
                                                = (0.01049475 * 1/260) * 0.25  
                                                = 0.000040364 * 0.25  
                                                = 0.000010091  
    

请注意，折扣（`discount`）**不适用于税务佣金（`taxCommission`）或特殊佣金（`special commission`）**。
    
    
    税务佣金 (以BNB支付) = 税务佣金 * BNB 汇率  
                            = 0.04022988 * (1/260)  
                            = 0.00015473  
      
    特殊佣金 (以BNB支付) = 特殊佣金 * BNB 汇率  
                            = 1049.47500000 * (1/260)  
                            = 4.036442308  
      
    
    
    
    佣金总数 (以BNB支付) = 标准佣金(打折后) + 税务佣金 (以BNB支付) + 特殊佣金 (以BNB支付)  
                            = 0.000010091 + 0.00015473 + 4.036442308  
                            = 4.036607129  
    

如果您的`BNB`余额不足以支付折扣后的佣金，那么全部佣金将从您所接收的`USDT`金额中扣除。