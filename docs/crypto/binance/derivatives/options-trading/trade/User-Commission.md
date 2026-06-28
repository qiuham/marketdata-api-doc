---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/trade/User-Commission
api_type: Trading
updated_at: 2026-01-15T23:43:04.845614
---

# User Commission (USER_DATA)

## API Description[​](/docs/derivatives/options-trading/trade/User-Commission#api-description "Direct link to API Description")

Get account commission.

## HTTP Request[​](/docs/derivatives/options-trading/trade/User-Commission#http-request "Direct link to HTTP Request")

GET `/eapi/v1/commission`

## Request Weight[​](/docs/derivatives/options-trading/trade/User-Commission#request-weight "Direct link to Request Weight")

**5**

## Request Parameters[​](/docs/derivatives/options-trading/trade/User-Commission#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/options-trading/trade/User-Commission#response-example "Direct link to Response Example")
    
    
    {  
        "commissions": [  
            {  
                "underlying": "BTCUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            },  
            {  
                "underlying": "ETHUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            },  
            {  
                "underlying": "BNBUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            },  
            {  
                "underlying": "SOLUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            },  
            {  
                "underlying": "XRPUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            },  
            {  
                "underlying": "DOGEUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            }  
        ]  
    }

---

# 用户手续费率(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/options-trading/trade/User-Commission#接口描述 "接口描述的直接链接")

获取用户手续费率.

## HTTP请求[​](/docs/zh-CN/derivatives/options-trading/trade/User-Commission#http请求 "HTTP请求的直接链接")

GET `/eapi/v1/commission`

## 请求权重[​](/docs/zh-CN/derivatives/options-trading/trade/User-Commission#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/options-trading/trade/User-Commission#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/options-trading/trade/User-Commission#响应示例 "响应示例的直接链接")
    
    
    {  
        "commissions": [  
            {  
                "underlying": "BTCUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            },  
            {  
                "underlying": "ETHUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            },  
            {  
                "underlying": "BNBUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            },  
            {  
                "underlying": "SOLUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            },  
            {  
                "underlying": "XRPUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            },  
            {  
                "underlying": "DOGEUSDT",  
                "makerFee": "0.000240",  
                "takerFee": "0.000240"  
            }  
        ]  
    }