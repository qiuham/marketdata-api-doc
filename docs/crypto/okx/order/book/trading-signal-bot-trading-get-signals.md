---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-get-signals
anchor_id: order-book-trading-signal-bot-trading-get-signals
api_type: API
updated_at: 2026-07-03 19:39:33.039040
---

# GET / Signals

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/signal/signals`

> Request Example
    
    
    GET /api/v5/tradingBot/signal/signals?signalSourceType=1
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
signalSourceType | String | Yes | Signal source type  
`1`: Created by yourself  
`2`: Subscribe  
`3`: Free signal  
signalChanId | String | No | Signal channel id  
after | String | No | Pagination of data to return records `signalChanId` earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records `signalChanId` newer than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "signalChanId": "623833708424069120",
                "signalChanName": "test",
                "signalChanDesc": "test",
                "signalChanToken": "test",
                "signalSourceType": "1"
            }
        ],
        "msg": ""
    }
    
    
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
signalChanId | String | Signal channel id  
signalChanName | String | Signal channel name  
signalChanDesc | String | Signal channel description  
signalChanToken | String | User identify when placing orders via signal  
signalSourceType | String | Signal source type  
`1`: Created by yourself  
`2`: Subscribe  
`3`: Free signal

---

# GET / 查询所有信号

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/signal/signals`

> 请求示例
    
    
    GET /api/v5/tradingBot/signal/signals
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
signalSourceType | String | 是 | 信号来源类型  
`1`：自己创建的  
`2`：订阅他人  
`3`：免费信号  
signalChanId | String | 否 | 信号ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的signalChanId  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的signalChanId  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "signalChanId": "623833708424069120",
                "signalChanName": "test",
                "signalChanDesc": "test",
                "signalChanToken": "test",
                "signalSourceType": "1"
            }
        ],
        "msg": ""
    }
    
    
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
signalChanId | String | 信号ID  
signalChanName | String | 信号名称  
signalChanDesc | String | 信号描述  
signalChanToken | String | 信号单的用户身份标识  
signalSourceType | String | 信号来源类型  
`1`：自己创建的  
`2`：订阅他人  
`3`：免费信号