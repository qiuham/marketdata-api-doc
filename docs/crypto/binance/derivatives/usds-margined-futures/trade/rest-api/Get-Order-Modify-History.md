---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History
api_type: Trading
updated_at: 2026-01-15T23:47:17.385729
---

# Get Order Modify History (USER_DATA)

## API Description[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History#api-description "Direct link to API Description")

Get order modification history

## HTTP Request[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History#http-request "Direct link to HTTP Request")

GET `/fapi/v1/orderAmendment`

## Request Weight[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History#request-weight "Direct link to Request Weight")

**1**

## Request Parameters[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
startTime| LONG| NO| Timestamp in ms to get modification history from INCLUSIVE  
endTime| LONG| NO| Timestamp in ms to get modification history until INCLUSIVE  
limit| INT| NO| Default 50; max 100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Either `orderId` or `origClientOrderId` must be sent, and the `orderId` will prevail if both are sent.
>   * Order modify history longer than 3 month is not avaliable
> 


## Response Example[​](/docs/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "amendmentId": 5363,	// Order modification ID  
            "symbol": "BTCUSDT",  
            "pair": "BTCUSDT",  
            "orderId": 20072994037,  
            "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
            "time": 1629184560899,	// Order modification time  
            "amendment": {  
                "price": {  
                    "before": "30004",  
                    "after": "30003.2"  
                },  
                "origQty": {  
                    "before": "1",  
                    "after": "1"  
                },  
                "count": 3	// Order modification count, representing the number of times the order has been modified  
            }  
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
            }  
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
            }  
        }  
    ]

---

# 查询订单修改历史 (USER_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History#接口描述 "接口描述的直接链接")

查询订单修改历史

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/orderAmendment`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对  
orderId| LONG| NO| 系统订单号  
origClientOrderId| STRING| NO| 用户自定义的订单号  
startTime| LONG| NO| 起始时间  
endTime| LONG| NO| 结束时间  
limit| INT| NO| 返回的结果集数量 默认值:50 最大值:100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 至少需要发送 `orderId` 与 `origClientOrderId`中的一个，同时发送则以 `orderId` 为准
>   * 接口仅保留最近三个月订单修改历史
> 


## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Get-Order-Modify-History#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "amendmentId": 5363,	// 修改记录号  
            "symbol": "BTCUSDT",  
            "pair": "BTCUSDT",  
            "orderId": 20072994037,  
            "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
            "time": 1629184560899,	// 修改时间  
            "amendment": {  
                "price": {  
                    "before": "30004",  
                    "after": "30003.2"  
                },  
                "origQty": {  
                    "before": "1",  
                    "after": "1"  
                },  
                "count": 3	// 修改记数，代表该修改记录是这笔订单第几次修改  
            }  
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
            }  
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
            }  
        }  
    ]