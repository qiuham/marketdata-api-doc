---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders
api_type: Trading
updated_at: 2026-01-15T23:45:56.864590
---

# Query User's Margin Force Orders(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#api-description "Direct link to API Description")

Query user's margin force orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/margin/forceOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| Currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#response-example "Direct link to Response Example")
    
    
    {  
        "rows": [  
            {  
                "avgPrice": "0.00388359",  
                "executedQty": "31.39000000",  
                "orderId": 180015097,  
                "price": "0.00388110",  
                "qty": "31.39000000",  
                "side": "SELL",  
                "symbol": "BNBBTC",  
                "timeInForce": "GTC",  
                "updatedTime": 1558941374745  
            }  
        ],  
        "total": 1  
    }

---

# 获取账户杠杆强制平仓记录(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#接口描述 "接口描述的直接链接")

获取账户杠杆强制平仓记录

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/forceOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| 当前查询页。 开始值 1. 默认:1  
size| LONG| NO| 默认:10 最大:100  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#响应示例 "响应示例的直接链接")
    
    
    {  
        "rows": [  
            {  
                "avgPrice": "0.00388359",  
                "executedQty": "31.39000000",  
                "orderId": 180015097,  
                "price": "0.00388110",  
                "qty": "31.39000000",  
                "side": "SELL",  
                "symbol": "BNBBTC",  
                "timeInForce": "GTC",  
                "updatedTime": 1558941374745  
            }  
        ],  
        "total": 1  
    }