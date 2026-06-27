---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders
api_type: Trading
updated_at: 2026-01-15T23:45:56.805678
---

# Query User's CM Force Orders(USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#api-description "Direct link to API Description")

Query User's CM Force Orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/cm/forceOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#request-weight "Direct link to Request Weight")

**20** with symbol, **50** without symbol

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
autoCloseType| ENUM| NO| "LIQUIDATION" for liquidation orders, "ADL" for ADL orders.  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 50; max 100.  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
>   * If "autoCloseType" is not sent, orders with both of the types will be returned
>   * If "startTime" is not sent, data within 7 days before "endTime" can be queried
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "orderId": 165123080,  
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD",  
        "status": "FILLED",  
        "clientOrderId": "autoclose-1596542005017000006",  
        "price": "11326.9",  
        "avgPrice": "11326.9",  
        "origQty": "1",  
        "executedQty": "1",  
        "cumBase": "0.00882854",  
        "timeInForce": "IOC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "origType": "LIMIT",  
        "time": 1596542005019,  
        "updateTime": 1596542005050  
      }  
    ]

---

# 用户CM强平单历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#接口描述 "接口描述的直接链接")

查询用户CM强平单历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/forceOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#请求权重 "请求权重的直接链接")

带 symbol **20** , 不带 symbol **50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
autoCloseType| ENUM| NO| `LIQUIDATION`: 强平单, `ADL`: ADL 减仓单.  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| 默认 50；最大 100.  
recvWindow| LONG| NO| 赋值不能超过 60000  
timestamp| LONG| YES|   
  
  * 如果没有传`autoCloseType`，强平单和 ADL 减仓单都会被返回
  * 如果没有传`startTime`, 只会返回`endTime`之前 7 天内的数据



## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "orderId": 165123080,  
        "symbol": "BTCUSD_200925",  
        "pair": "BTCUSD",  
        "status": "FILLED",  
        "clientOrderId": "autoclose-1596542005017000006",  
        "price": "11326.9",  
        "avgPrice": "11326.9",  
        "origQty": "1",  
        "executedQty": "1",  
        "cumBase": "0.00882854",  
        "timeInForce": "IOC",  
        "type": "LIMIT",  
        "reduceOnly": false,  
        "side": "SELL",  
        "positionSide": "BOTH",  
        "origType": "LIMIT",  
        "time": 1596542005019,  
        "updateTime": 1596542005050,  
      }  
    ]