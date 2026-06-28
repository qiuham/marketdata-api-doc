---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/User-Exercise-Record
api_type: Trading
updated_at: 2026-01-15T23:43:04.908060
---

# User Exercise Record (USER_DATA)

## API Description[​](/docs/derivatives/options-trading/trade/User-Exercise-Record#api-description "Direct link to API Description")

Get account exercise records.

## HTTP Request[​](/docs/derivatives/options-trading/trade/User-Exercise-Record#http-request "Direct link to HTTP Request")

GET `/eapi/v1/exerciseRecord`

## Request Weight[​](/docs/derivatives/options-trading/trade/User-Exercise-Record#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/trade/User-Exercise-Record#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| Option trading pair, e.g BTC-200730-9000-C  
startTime| LONG| NO| startTime  
endTime| LONG| NO| endTime  
limit| INT| NO| default 1000, max 1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/trade/User-Exercise-Record#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "id": "1125899906842624042",  
            "currency": "USDT",  
            "symbol": "BTC-220721-25000-C",  
            "exercisePrice": "25000.00000000",  
            "quantity": "1.00000000",  
            "amount": "0.00000000",  
            "fee": "0.00000000",  
            "createDate": 1658361600000,  
            "priceScale": 2,  
            "quantityScale": 2,  
            "optionSide": "CALL",  
            "positionSide": "LONG",  
            "quoteAsset": "USDT"  
        }  
    ]

---

# 用户行权历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/User-Exercise-Record#接口描述 "接口描述的直接链接")

获取用户行权历史.

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/User-Exercise-Record#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/exerciseRecord`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/User-Exercise-Record#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/User-Exercise-Record#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对如 BTC-200730-9000-C  
startTime| LONG| NO| 起始时间如1593511200000  
endTime| LONG| NO| 结束时间如1593512200000  
limit| INT| NO| 默认1000, 最大1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/User-Exercise-Record#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "id": "1125899906842624042",          
            "currency": "USDT",                  // 结算资产  
            "symbol": "BTC-220721-25000-C",      // 交易对  
            "exercisePrice": "25000.00000000",   // 行权价  
            "quantity": "1.00000000",            // 数量  
            "amount": "0.00000000",              // 金额  
            "fee": "0.00000000",                 // 手续费  
            "createDate": 1658361600000,         // 行权时间  
            "priceScale": 2,                     // 价格精度  
            "quantityScale": 2,                  // 数量精度  
            "optionSide": "CALL",                // 期权种类  
            "positionSide": "LONG",              // 仓位方向  
            "quoteAsset": "USDT"                 // 报价资产  
        }  
    ]