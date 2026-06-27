---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/Account-Trade-List
api_type: Trading
updated_at: 2026-01-15T23:42:29.333237
---

# Account Trade List (USER_DATA)

## API Description[​](/docs/derivatives/options-trading/trade/Account-Trade-List#api-description "Direct link to API Description")

Get trades for a specific account and symbol.

## HTTP Request[​](/docs/derivatives/options-trading/trade/Account-Trade-List#http-request "Direct link to HTTP Request")

`GET /eapi/v1/userTrades (HMAC SHA256)`

## Request Weight[​](/docs/derivatives/options-trading/trade/Account-Trade-List#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/trade/Account-Trade-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| Option symbol, e.g BTC-200730-9000-C  
fromId| LONG| NO| Trade id to fetch from. Default gets most recent trades, e.g 4611875134427365376  
startTime| LONG| NO| Start time, e.g 1593511200000  
endTime| LONG| NO| End time, e.g 1593512200000  
limit| INT| NO| Default 100; max 1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/trade/Account-Trade-List#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "id": 4611875134427365377,          // unique id  
        "tradeId": 239,                     // trade id  
        "orderId": 4611875134427365377,     // order id  
        "symbol": "BTC-200730-9000-C",      // option symbol  
        "price": "100",                     // trade price  
        "quantity": "1",                    // trade quantity  
        "fee": "0",                         // fee(negative is fee deduction)  
        "realizedProfit": "0.00000000",     // realized profit/loss  
        "side": "BUY",                      // order side  
        "type": "LIMIT",                    // order type    
        "liquidity": "TAKER",               // TAKER or MAKER        
        "time": 1592465880683               // trade time  
        "priceScale": 2,  
        "quantityScale": 2,  
        "optionSide": "CALL",  
        "quoteAsset": "USDT"  
      }   
    ]

---

# 账户成交历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/Account-Trade-List#接口描述 "接口描述的直接链接")

查询账户成交历史

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/Account-Trade-List#http请求 "HTTP请求的直接链接")

`GET /eapi/v1/userTrades`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/Account-Trade-List#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/Account-Trade-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对  
fromId| LONG| NO| 返回该fromId及之后的成交，缺省返回最近的成交  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 返回的结果集数量 默认值:100 最大值:1000.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/Account-Trade-List#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "id": 4611875134427365377,          // id  
        "tradeId": 239,                     // 交易id  
        "orderId": 4611875134427365377,     // 订单id  
        "symbol": "BTC-200730-9000-C",      // 交易对  
        "price": "100",                     // 成交价  
        "quantity": "1",                    // 成交量  
        "fee": "-1.04378629",               // 手续费（负数为扣费）   
        "realizedProfit": "0.00000000",     // 已实现盈亏  
        "side": "BUY",                      // 订单方向  
        "type": "LIMIT",                    // 订单类型   
        "liquidity": "TAKER",               // TAKER or MAKER        
        "time": 1592465880683               // 交易时间  
        "priceScale": 2,                    // 价格精度  
        "quantityScale": 2,                 // 数量精度   
        "optionSide": "CALL",               // 期权种类  
        "quoteAsset": "USDT"                // 报价资产  
      }   
    ]