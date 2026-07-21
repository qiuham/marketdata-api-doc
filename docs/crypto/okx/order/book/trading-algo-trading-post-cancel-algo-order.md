---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-algo-trading-post-cancel-algo-order
anchor_id: order-book-trading-algo-trading-post-cancel-algo-order
api_type: API
updated_at: 2026-07-21 19:25:45.320630
---

# POST / Cancel algo order

Cancel unfilled algo orders. A maximum of 10 orders can be canceled per request. Request parameters should be passed in the form of an array.  
  
#### Rate Limit: 20 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### HTTP Request

`POST /api/v5/trade/cancel-algos`

> Request Example
    
    
    POST /api/v5/trade/cancel-algos
    body
    [
        {
            "algoId":"590919993110396111",
            "instId":"BTC-USDT"
        },
        {
            "algoId":"590920138287841222",
            "instId":"BTC-USDT"
        }
    ]
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Cancel unfilled algo orders (not including Iceberg order, TWAP order, Trailing Stop order)
    algo_orders = [
        {"instId": "BTC-USDT", "algoId": "590919993110396111"},
        {"instId": "BTC-USDT", "algoId": "590920138287841222"}
    ]
    
    result = tradeAPI.cancel_algo_order(algo_orders)
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
algoId | String | Conditional | Algo ID  
Either `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used.  
algoClOrdId | String | Conditional | Client-supplied Algo ID  
Either `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "1836489397437468672",
                "clOrdId": "",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
clOrdId | String | ~~Client Order ID as assigned by the client~~(Deprecated)  
algoClOrdId | String | ~~Client-supplied Algo ID~~(Deprecated)  
tag | String | ~~Order tag~~(Deprecated)

---

# POST / 撤销策略委托订单

撤销策略委托订单，每次最多可以撤销10个策略委托单  
  
#### 限速：20个/2s

#### 限速规则（期权以外）：User ID + Instrument ID

#### 限速规则（只限期权）：User ID + Instrument Family

#### HTTP请求

`POST /api/v5/trade/cancel-algos`

> 请求示例
    
    
    POST /api/v5/trade/cancel-algos
    body
    [
        {
            "algoId":"590919993110396111",
            "instId":"BTC-USDT"
        },
        {
            "algoId":"590920138287841222",
            "instId":"BTC-USDT"
        }
    ]
    
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 支持止盈止损，计划委托 类型的策略撤单
    algo_orders = [
        {"instId": "BTC-USDT", "algoId": "590919993110396111"},
        {"instId": "BTC-USDT", "algoId": "590920138287841222"}
    ]
    
    result = tradeAPI.cancel_algo_order(algo_orders)
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID 如 `BTC-USDT`  
algoId | String | 可选 | 策略委托单ID  
`algoId`和`algoClOrdId`必须传一个，若传两个，以`algoId`为主  
algoClOrdId | String | 可选 | 客户自定义策略订单ID  
`algoId`和`algoClOrdId`必须传一个，若传两个，以`algoId`为主  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "1836489397437468672",
                "clOrdId": "",
                "sCode": "0",
                "sMsg": "",
                "tag": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
algoId | String | 策略委托单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
clOrdId | String | ~~客户自定义订单ID~~ （已废弃）  
algoClOrdId | String | ~~客户自定义策略订单ID~~ （已废弃）  
tag | String | ~~订单标签~~ （已废弃）