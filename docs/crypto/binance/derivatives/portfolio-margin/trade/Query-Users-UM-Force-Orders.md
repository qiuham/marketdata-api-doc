---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders
api_type: Trading
updated_at: 2026-01-15T23:45:56.928478
---

# Query User's UM Force Orders (USER_DATA)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#api-description "Direct link to API Description")

Query User's UM Force Orders

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/forceOrders`

## Request Weight[​](/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#request-weight "Direct link to Request Weight")

**20** with symbol, **50** without symbol

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
autoCloseType| ENUM| NO| `LIQUIDATION` for liquidation orders, `ADL` for ADL orders.  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 50; max 100.  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
>   * If `autoCloseType` is not sent, orders with both of the types will be returned
>   * If `startTime` is not sent, data within 7 days before `endTime` can be queried
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "orderId": 6071832819,   
        "symbol": "BTCUSDT",   
        "status": "FILLED",   
        "clientOrderId": "autoclose-1596107620040000020",   
        "price": "10871.09",   
        "avgPrice": "10913.21000",   
        "origQty": "0.001",   
        "executedQty": "0.001",   
        "cumQuote": "10.91321",   
        "timeInForce": "IOC",   
        "type": "LIMIT",   
        "reduceOnly": false,   
        "side": "SELL",   
        "positionSide": "BOTH",   
        "origType": "LIMIT",   
        "time": 1596107620044,   
        "updateTime": 1596107620087  
      }  
    ]

---

# 用户强平单历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#接口描述 "接口描述的直接链接")

查询用户UM强平单历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/forceOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#请求权重 "请求权重的直接链接")

带symbol **20** , 不带symbol **50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
autoCloseType| ENUM| NO| `LIQUIDATION`: 强平单, `ADL`: ADL 减仓单.  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| 默认 50；最大 100.  
recvWindow| LONG| NO| 赋值不能超过 60000  
timestamp| LONG| YES|   
  
>   * 如果没有传`autoCloseType`，强平单和 ADL 减仓单都会被返回
>   * 如果没有传`startTime`, 只会返回`endTime`之前 7 天内的数据
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        orderId: 6071832819,  
        symbol: "BTCUSDT",  
        status: "FILLED",  
        clientOrderId: "autoclose-1596107620040000020",  
        price: "10871.09",  
        avgPrice: "10913.21000",  
        origQty: "0.001",  
        executedQty: "0.001",  
        cumQuote: "10.91321",  
        timeInForce: "IOC",  
        type: "LIMIT",  
        reduceOnly: false,  
        side: "SELL",  
        positionSide: "BOTH",  
        origType: "LIMIT",  
        time: 1596107620044,  
        updateTime: 1596107620087,  
      },  
    ]