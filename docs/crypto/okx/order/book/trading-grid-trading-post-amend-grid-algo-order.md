---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-grid-trading-post-amend-grid-algo-order
anchor_id: order-book-trading-grid-trading-post-amend-grid-algo-order
api_type: API
updated_at: 2026-07-04 19:37:44.432191
---

# POST / Amend grid algo order

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/amend-order-algo`

> Request Example
    
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body
    {
        "algoId":"448965992920907776",
        "instId":"BTC-USDT-SWAP",
        "slTriggerPx":"1200",
        "tpTriggerPx":""
    }
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body 
    {
       "algoId":"578963447615062016",
       "instId":"BTC-USDT",
       "triggerParams":[
           {
               "triggerAction":"stop",  
               "triggerStrategy":"price",   
               "triggerPx":"1000"
           }
       ]
    }
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body 
    {
       "algoId":"578963447615062016",
       "instId":"BTC-USDT-SWAP",
       "triggerParams":[
           {
               "triggerAction":"stop",  
               "triggerStrategy":"instant",   
               "stopType":"1"
           }
       ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
slTriggerPx | String | No | New stop-loss trigger price  
if slTriggerPx is set "" means stop-loss trigger price is canceled.  
Either `slTriggerPx` or `tpTriggerPx` is required.  
tpTriggerPx | String | No | New take-profit trigger price  
if tpTriggerPx is set "" means take-profit trigger price is canceled.  
tpRatio | String | No | Take profit ratio, 0.1 represents 10%, only applicable to contract grid  
if it is set "" means take-profit ratio is canceled.  
slRatio | String | No | Stop loss ratio, 0.1 represents 10%, only applicable to contract grid`  
if it is set "" means stop-loss ratio is canceled.  
topUpAmt | String | No | Top up amount, only applicable to spot grid  
triggerParams | Array of objects | No | Trigger Parameters  
> triggerAction | String | Yes | Trigger action  
`start`  
`stop`  
> triggerStrategy | String | Yes | Trigger strategy  
`instant`  
`price`  
`rsi`  
> triggerPx | String | No | Trigger Price  
This field is only valid when `triggerStrategy` is `price`  
> stopType | String | No | Stop type  
Spot grid `1`: Sell base currency `2`: Keep base currency  
Contract grid `1`: Market Close All positions `2`: Keep positions  
This field is only valid when `triggerAction` is `stop`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "algoClOrdId": "",
                "algoId":"448965992920907776",
                "sCode":"0",
                "sMsg":"",
                "tag": ""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
sCode | String | The code of the event execution result, `0` means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
tag | String | Order tag

---

# POST / 修改网格策略订单

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/tradingBot/grid/amend-order-algo`

> 请求示例
    
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body
    {
        "algoId":"448965992920907776",
        "instId":"BTC-USDT-SWAP",
        "slTriggerPx":"1200",
        "tpTriggerPx":""
    }
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body 
    {
       "algoId":"578963447615062016",
       "instId":"BTC-USDT",
       "triggerParams":[
           {
               "triggerAction":"stop",  
               "triggerStrategy":"price",   
               "triggerPx":"1000"
           }
       ]
    }
    
    POST /api/v5/tradingBot/grid/amend-order-algo
    body 
    {
       "algoId":"578963447615062016",
       "instId":"BTC-USDT-SWAP",
       "triggerParams":[
           {
               "triggerAction":"stop",  
               "triggerStrategy":"instant",   
               "stopType":"1"
           }
       ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
instId | String | 是 | 产品ID，如`BTC-USDT-SWAP`  
slTriggerPx | String | 可选 | 新的止损触发价  
当值为""则代表取消止损触发价  
`slTriggerPx`、`tpTriggerPx`至少要传一个值  
tpTriggerPx | String | 可选 | 新的止盈触发价  
当值为""则代表取消止盈触发价  
tpRatio | String | 否 | 止盈比率，0.1 代表 10%，仅适用于合约网格  
当值为""则代表取消止盈比率  
slRatio | String | 否 | 止损比率，0.1 代表 10%，仅适用于合约网格  
当值为""则代表取消止损比率  
topUpAmt | String | 否 | 增加的投资额，仅适用于现货网格  
triggerParams | Array of objects | 否 | 信号触发参数  
> triggerAction | String | 是 | 触发行为  
`start`：网格启动  
`stop`：网格停止  
> triggerStrategy | String | 是 | 触发策略  
`instant`：立即触发  
`price`：价格触发  
`rsi`：rsi指标触发  
> triggerPx | String | 否 | 触发价格  
该字段只在`triggerStrategy`为`price`下有效  
> stopType | String | 否 | 策略停止类型  
现货 `1`：卖出交易币，`2`：不卖出交易币  
合约网格 `1`：停止平仓，`2`：停止不平仓   
该字段只在`triggerAction`为`stop`时有效  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "algoClOrdId": "",
                "algoId": "448965992920907776",
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
algoId | String | 策略订单ID  
algoClOrdId | String | 用户自定义策略ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
tag | String | 订单标签