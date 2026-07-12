---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-get-one-click-repay-history-new
anchor_id: order-book-trading-trade-get-one-click-repay-history-new
api_type: API
updated_at: 2026-07-12 19:15:32.730809
---

# GET / One-click repay history (New)

Get the history and status of one-click repay trades in the past 7 days. Only applicable to `SPOT mode`.  
  
#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/one-click-repay-history-v2`

> Request Example
    
    
    GET /api/v5/trade/one-click-repay-history-v2
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    result = tradeAPI.oneclick_repay_history_v2()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
after | String | No | Pagination of data to return records earlier than (included) the requested time `ts` , Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than (included) the requested time `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "USDC",
                "fillDebtSz": "9.079631989",
                "ordIdInfo": [
                    {
                        "cTime": "1742194485439",
                        "fillPx": "1",
                        "fillSz": "9.088651",
                        "instId": "USDC-USDT",
                        "ordId": "2338478342062235648",
                        "ordType": "ioc",
                        "px": "1.0049",
                        "side": "buy",
                        "state": "filled",
                        "sz": "9.0886514537313433"
                    },
                    {
                        "cTime": "1742194482326",
                        "fillPx": "83271.9",
                        "fillSz": "0.00010969",
                        "instId": "BTC-USDT",
                        "ordId": "2338478237607288832",
                        "ordType": "ioc",
                        "px": "82856.7",
                        "side": "sell",
                        "state": "filled",
                        "sz": "0.000109696512171"
                    }
                ],
                "repayCcyList": [
                    "USDC",
                    "BTC"
                ],
                "status": "filled",
                "ts": "1742194481852"
            },
            {
                "debtCcy": "USDC",
                "fillDebtSz": "100",
                "ordIdInfo": [],
                "repayCcyList": [
                    "USDC",
                    "BTC"
                ],
                "status": "filled",
                "ts": "1742192217511"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
debtCcy | String | Debt currency  
repayCcyList | Array of strings | Repay currency list, e.g. ["USDC","BTC"]  
fillDebtSz | String | Amount of debt currency transacted  
status | String | Current status of one-click repay   
`running`: Running   
`filled`: Filled   
`failed`: Failed  
ordIdInfo | Array of objects | Order info  
> ordId | String | Order ID  
> instId | String | Instrument ID, e.g. `BTC-USDT`  
> ordType | String | Order type  
`ioc`: Immediate-or-cancel order  
> side | String | Side  
`buy`  
`sell`  
> px | String | Price  
> sz | String | Quantity to buy or sell  
> fillPx | String | Last filled price.  
If none is filled, it will return "".  
> fillSz | String | Last filled quantity  
> state | String | State  
`filled`  
`canceled`  
> cTime | String | Creation time for order, Unix timestamp format in milliseconds, e.g. `1597026383085`  
ts | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 获取一键还债历史记录(新)

查询一键还债近7天的历史记录与进度状态。仅适用于`现货模式`。  
  
#### 限速：1次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/trade/one-click-repay-history-v2`

> 请求示例
    
    
    GET /api/v5/trade/one-click-repay-history-v2
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    result = tradeAPI.oneclick_repay_history_v2()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
after | String | 否 | 查询在指定请求时间`ts`之前(包含)的内容，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在指定请求时间`ts`之后(包含)的内容，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回的结果集数量，默认为`100`，最大为`100`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "debtCcy": "USDC",
                "fillDebtSz": "9.079631989",
                "ordIdInfo": [
                    {
                        "cTime": "1742194485439",
                        "fillPx": "1",
                        "fillSz": "9.088651",
                        "instId": "USDC-USDT",
                        "ordId": "2338478342062235648",
                        "ordType": "ioc",
                        "px": "1.0049",
                        "side": "buy",
                        "state": "filled",
                        "sz": "9.0886514537313433"
                    },
                    {
                        "cTime": "1742194482326",
                        "fillPx": "83271.9",
                        "fillSz": "0.00010969",
                        "instId": "BTC-USDT",
                        "ordId": "2338478237607288832",
                        "ordType": "ioc",
                        "px": "82856.7",
                        "side": "sell",
                        "state": "filled",
                        "sz": "0.000109696512171"
                    }
                ],
                "repayCcyList": [
                    "USDC",
                    "BTC"
                ],
                "status": "filled",
                "ts": "1742194481852"
            },
            {
                "debtCcy": "USDC",
                "fillDebtSz": "100",
                "ordIdInfo": [],
                "repayCcyList": [
                    "USDC",
                    "BTC"
                ],
                "status": "filled",
                "ts": "1742192217511"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
debtCcy | String | 负债币种  
repayCcyList | Array of strings | 偿还币种列表，如 ["USDC","BTC"]  
fillDebtSz | String | 对应的负债币种成交数量  
status | String | 当前还债进度/状态  
`running`：进行中   
`filled`：已完成   
`failed`：失败  
ordIdInfo | Array of objects | 相关订单信息  
> ordId | String | 订单ID  
> instId | String | 产品ID，如 `BTC-USDT`  
> ordType | String | 订单类型  
`ioc`：立即成交并取消剩余  
> side | String | 订单方向  
`buy`  
`sell`  
> px | String | 委托价格  
> sz | String | 委托数量  
> fillPx | String | 最新成交价格  
如果成交数量为0，该字段为""  
> fillSz | String | 最新成交数量  
> state | String | 订单状态  
`filled`：完全成交  
`canceled`：撤单成功  
> cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
ts | String | 请求时间，Unix时间戳的毫秒数格式，如 `1597026383085`