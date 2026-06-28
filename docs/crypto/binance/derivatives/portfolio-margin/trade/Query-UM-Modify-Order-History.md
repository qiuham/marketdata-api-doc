---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History
api_type: Trading
updated_at: 2026-01-15T23:45:56.673684
---

# Query UM Modify Order History(TRADE)

## API Description[​](/docs/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History#api-description "Direct link to API Description")

Get order modification history

## HTTP Request[​](/docs/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History#http-request "Direct link to HTTP Request")

GET `/papi/v1/um/orderAmendment`

## Request Weight(Order)[​](/docs/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History#request-weightorder "Direct link to Request Weight\(Order\)")

**1**

## Request Parameters[​](/docs/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
startTime| LONG| NO| Timestamp in ms to get modification history from INCLUSIVE  
endTime| LONG| NO| Timestamp in ms to get modification history until INCLUSIVE  
limit| INT| NO| Default 500, max 1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `orderId` or `origClientOrderId` must be sent, and the `orderId` will prevail if both are sent.
> 


## Response Example[​](/docs/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "amendmentId": 5363,    // Order modification ID  
            "symbol": "BTCUSDT",  
            "pair": "BTCUSDT",  
            "orderId": 20072994037,  
            "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
            "time": 1629184560899,  // Order modification time  
            "amendment": {  
                "price": {  
                    "before": "30004",  
                    "after": "30003.2"  
                },  
                "origQty": {  
                    "before": "1",  
                    "after": "1"  
                },  
                "count": 3  // Order modification count, representing the number of times the order has been modified  
            },  
            "priceMatch": "NONE"  
        },  
        {  
            "amendmentId": 5361,  
            "symbol": "BTCUSDT",  
            "pair": "BTCUSDT",  
            "orderId": 20072994037,  
            "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
            "time": 1629184533946,  
            "amendment": {  
                "price": {  
                    "before": "30005",  
                    "after": "30004"  
                },  
                "origQty": {  
                    "before": "1",  
                    "after": "1"  
                },  
                "count": 2  
            },  
            "priceMatch": "NONE"  
        },  
        {  
            "amendmentId": 5325,  
            "symbol": "BTCUSDT",  
            "pair": "BTCUSDT",  
            "orderId": 20072994037,  
            "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
            "time": 1629182711787,  
            "amendment": {  
                "price": {  
                    "before": "30002",  
                    "after": "30005"  
                },  
                "origQty": {  
                    "before": "1",  
                    "after": "1"  
                },  
                "count": 1  
            },  
            "priceMatch": "NONE"  
        }  
    ]

---

# 查询UM订单修改历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History#接口描述 "接口描述的直接链接")

查询UM订单修改历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/orderAmendment`

## 请求权重(Order)[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History#请求权重order "请求权重\(Order\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History#请求参数 "请求参数的直接链接")

名称| 类型| 类型| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderId| LONG| NO| 系统订单号  
origClientOrderId| STRING| NO| 用户自定义的订单号  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 默认值 500, 最大值 1000  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 至少需要发送 `orderId` 与 `origClientOrderId`中的一个，同时发送则以 orderId 为准
> 


## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "amendmentId": 5363,    // 修改记录号  
            "symbol": "BTCUSDT",  
            "pair": "BTCUSDT",  
            "orderId": 20072994037,  
            "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
            "time": 1629184560899,  // 修改时间  
            "amendment": {  
                "price": {  
                    "before": "30004",  
                    "after": "30003.2"  
                },  
                "origQty": {  
                    "before": "1",  
                    "after": "1"  
                },  
                "count": 3  // 修改记数，代表该修改记录是这笔订单第几次修改  
            },  
            "priceMatch": "NONE"  
        },  
        {  
            "amendmentId": 5361,  
            "symbol": "BTCUSDT",  
            "pair": "BTCUSDT",  
            "orderId": 20072994037,  
            "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
            "time": 1629184533946,  
            "amendment": {  
                "price": {  
                    "before": "30005",  
                    "after": "30004"  
                },  
                "origQty": {  
                    "before": "1",  
                    "after": "1"  
                },  
                "count": 2  
            },  
            "priceMatch": "NONE"  
        },  
        {  
            "amendmentId": 5325,  
            "symbol": "BTCUSDT",  
            "pair": "BTCUSDT",  
            "orderId": 20072994037,  
            "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
            "time": 1629182711787,  
            "amendment": {  
                "price": {  
                    "before": "30002",  
                    "after": "30005"  
                },  
                "origQty": {  
                    "before": "1",  
                    "after": "1"  
                },  
                "count": 1  
            },  
            "priceMatch": "NONE"  
        }  
    ]