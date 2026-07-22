---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-post-create-signal
anchor_id: order-book-trading-signal-bot-trading-post-create-signal
api_type: API
updated_at: 2026-07-22 19:19:30.186258
---

# POST / Create signal

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/create-signal`

> Request Example
    
    
    POST /api/v5/tradingBot/signal/create-signal
    body
    {
      "signalChanName": "long short",
      "signalDesc": "this is the first version"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
signalChanName | String | Yes | Signal channel name  
signalChanDesc | String | No | Signal channel description  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
           {
               "signalChanId" :"572112109",
               "signalChanToken":"dojuckew331lkx"
           }
    
        ],
        "msg": ""
    }
    
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
signalChanId | String | Signal channel Id  
signalChanToken | String | User identify when placing orders via signal

---

# POST / 创建信号

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/signal/create-signal`

> 请求示例
    
    
    POST /api/v5/tradingBot/signal/create-signal
    body
    {
      "signalChanName": "long short",
      "signalDesc": "this is the first version"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
signalChanName | String | 是 | 信号名称  
signalChanDesc | String | 否 | 信号描述  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
           {
               "signalChanId" :"572112109",
               "signalChanToken":"dojuckew331lkx"
           }
    
        ],
        "msg": ""
    }
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
signalChanId | String | 信号ID  
signalChanToken | String | 信号单的用户身份标识