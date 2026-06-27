---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/account/Query-Isolated-Margin-Fee-Data
api_type: Account
updated_at: 2026-05-27 18:56:21.217109
---

# Query Isolated Margin Fee Data (USER_DATA)

## API Description[​](/docs/margin_trading/account/Query-Isolated-Margin-Fee-Data#api-description "Direct link to API Description")

Get isolated margin fee data collection with any vip level or user's current specific data as <https://www.binance.com/en/margin-fee>

## HTTP Request[​](/docs/margin_trading/account/Query-Isolated-Margin-Fee-Data#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/isolatedMarginData`

## Request Weight[​](/docs/margin_trading/account/Query-Isolated-Margin-Fee-Data#request-weight "Direct link to Request Weight")

**1 when a single is specified;(IP)** **10 when the symbol parameter is omitted(IP)**

## Request Parameters[​](/docs/margin_trading/account/Query-Isolated-Margin-Fee-Data#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
vipLevel| INT| NO| User's current specific margin data will be returned if vipLevel is omitted  
symbol| STRING| NO|   
recvWindow| LONG| NO| No more than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/account/Query-Isolated-Margin-Fee-Data#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "vipLevel": 0,  
            "symbol": "BTCUSDT",  
            "leverage": "10",  
            "data": [  
                {  
                    "coin": "BTC",  
                    "dailyInterest": "0.00026125",  
                    "borrowLimit": "270"  
                },  
                {  
                    "coin": "USDT",  
                    "dailyInterest": "0.000475",  
                    "borrowLimit": "2100000"  
                }  
            ]  
        }  
    ]

---

# 获取逐仓杠杆利率及限额 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/account/Query-Isolated-Margin-Fee-Data#接口描述 "接口描述的直接链接")

通过VIP等级或用户当前VIP等级获取逐仓杠杆利率及限额， 如： <https://www.binance.com/en/margin-fee>

## HTTP请求[​](/docs/zh-CN/margin_trading/account/Query-Isolated-Margin-Fee-Data#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/isolatedMarginData`

## 请求权重[​](/docs/zh-CN/margin_trading/account/Query-Isolated-Margin-Fee-Data#请求权重 "请求权重的直接链接")

**1 指定交易对;(IP)** **10 交易对参数缺失(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/account/Query-Isolated-Margin-Fee-Data#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
vipLevel| INT| NO| 默认为用户当前VIP等级  
symbol| STRING| NO|   
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/account/Query-Isolated-Margin-Fee-Data#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "vipLevel": 0,  
            "symbol": "BTCUSDT",  
            "leverage": "10",  
            "data": [  
                {  
                    "coin": "BTC",  
                    "dailyInterest": "0.00026125",  
                    "borrowLimit": "270"  
                },  
                {  
                    "coin": "USDT",  
                    "dailyInterest": "0.000475",  
                    "borrowLimit": "2100000"  
                }  
            ]  
        }  
    ]