---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-post-cancel-all-after
anchor_id: order-book-trading-trade-post-cancel-all-after
api_type: API
updated_at: 2026-07-11 19:12:33.181606
---

# POST / Cancel All After

Cancel all pending orders after the countdown timeout. Applicable to all trading symbols through order book (except Spread trading)  
  
  
#### Rate Limit: 1 request per second

#### Rate limit rule: User ID + tag

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/cancel-all-after`

> Request Example
    
    
    POST /api/v5/trade/cancel-all-after
    {
       "timeOut":"60"
    }
    
    
    
    import okx.Trade as Trade
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading: 0, Demo trading: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # Set cancel all after
    result = tradeAPI.cancel_all_after(
        timeOut="10"
    )
    
    print(result)
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
timeOut | String | Yes | The countdown for order cancellation, with second as the unit.  
Range of value can be 0, [10, 120].   
Setting timeOut to 0 disables Cancel All After.  
tag | String | No | CAA order tag   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "triggerTime":"1587971460",
                "tag":"",
                "ts":"1587971400"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
triggerTime | String | The time the cancellation is triggered.  
triggerTime=0 means Cancel All After is disabled.  
tag | String | CAA order tag  
ts | String | The time the request is received.  
Users are recommended to send heartbeat to the exchange every second. When the cancel all after is triggered, the trading engine will cancel orders on behalf of the client one by one and this operation may take up to a few seconds. This feature is intended as a protection mechanism for clients only and clients should not use this feature as part of their trading strategies.    
To use tag level CAA, first, users need to set tags for their orders using the `tag` request parameter in the placing orders endpoint. When calling the CAA endpoint, if the `tag` request parameter is not provided, the default will be to set CAA at the account level. In this case, all pending orders for all order book trading symbols under that sub-account will be cancelled when CAA triggers, consistent with the existing logic. If the `tag` request parameter is provided, CAA will be set at the order tag level. When triggered, only pending orders of order book trading symbols with the specified tag will be canceled, while orders with other tags or no tags will remain unaffected.   
  
Users can run a maximum of 20 tag level CAAs simultaneously under the same sub-account. The system will only count live tag level CAAs. CAAs that have been triggered or revoked by the user will not be counted. The user will receive error code 51071 when exceeding the limit.

---

# POST / 倒计时全部撤单

在倒计时结束后，取消所有挂单。适用于所有撮合交易产品（不包括价差交易）。  
  
#### 限速：1次/s

#### 限速规则：User ID + tag

#### 权限：交易

#### HTTP请求

`POST /api/v5/trade/cancel-all-after`

> 请求示例
    
    
    POST /api/v5/trade/cancel-all-after
    {
       "timeOut":"60"
    }
    
    
    
    import okx.Trade as Trade
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘: 0, 模拟盘: 1
    
    tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
    
    # 设置倒计时全部撤单
    result = tradeAPI.cancel_all_after(
        timeOut="10"
    )
    
    print(result)
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
timeOut | String | 是 | 取消挂单的倒计时，单位为秒  
取值范围为 0, [10, 120]  
0 代表不使用该功能  
tag | String | 否 | CAA订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "triggerTime":"1587971460",
                "tag":"",
                "ts":"1587971400"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
triggerTime | String | 触发撤单的时间  
triggerTime=0 代表未使用该功能  
tag | String | CAA订单标签  
ts | String | 请求被接收到的时间  
建议用户每一秒调用接口一次。当倒计时全部撤单被触发时，交易引擎将为用户逐一取消其挂单，该操作可能持续数秒。该功能起到保护用户的作用，不应作为交易策略使用。    
为使用标签维度倒计时全部撤单，首先，用户需使用现有下单接口的tag请求参数，为订单设置标签。调用CAA接口时，若不传入tag请求参数，则默认设置账户维度CAA，CAA触发时，撤销该子账户下的所有撮合交易产品挂单；若传入tag请求参数，则默认设置订单标签维度CAA，CAA触发时，带有此tag的撮合交易产品挂单将被撤销，带有其他tag或没有tag的订单将不受影响。   
  
同一子账户下，用户最多能同时运行20个标签维度的CAA。系统仅计数活跃的标签维度CAA，已被触发或被用户主动撤销的将不被计入。超过限制时，用户将收到错误码51071。