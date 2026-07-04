---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-cancel-all-after
anchor_id: block-trading-rest-api-cancel-all-after
api_type: REST
updated_at: 2026-07-04 19:38:30.779213
---

# Cancel All After

Cancel all quotes after the countdown timeout.  
  
#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-all-after`

> Request Example
    
    
    POST /api/v5/rfq/cancel-all-after
    body
    {
       "timeOut":"60"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
timeOut | String | Yes | The countdown for quotes cancellation, with second as the unit.  
Range of value can be 0, [10, 120].   
Setting timeOut to 0 disables Cancel All After.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "triggerTime":"1587971460",
                "ts":"1587971400"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
triggerTime | String | The time the cancellation is triggered.  
triggerTime=0 means Cancel All After is disabled.  
ts | String | The time the request is received.  
Users are recommended to send a request to the exchange every second. When the cancel all after is triggered, the trading engine will cancel quotes on behalf of the client one by one and this operation may take up to a few seconds. This feature is intended as a protection mechanism for clients only and clients should not use this feature as part of their trading strategies.

---

# 倒计时全部撤单

在倒计时结束后，取消所有报价单。  
  
#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/rfq/cancel-all-after`

> 请求示例
    
    
    POST /api/v5/rfq/cancel-all-after
    body
    {
       "timeOut":"60"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
timeOut | String | 是 | 取消报价单的倒计时，单位为秒。  
取值范围为 0, [10, 120]  
0 代表不使用该功能。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "triggerTime":"1587971460",
                "ts":"1587971400"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
triggerTime | String | 触发撤单的时间.  
triggerTime=0 代表未使用该功能。  
ts | String | 请求被接收到的时间  
建议用户每一秒调用接口一次。当倒计时全部撤单被触发时，交易引擎将为用户逐一取消报价单，该操作可能持续数秒。该功能起到保护用户的作用，不应作为交易策略使用。