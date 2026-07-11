---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-signal-bot-trading-get-signal-bot-event-history
anchor_id: order-book-trading-signal-bot-trading-get-signal-bot-event-history
api_type: API
updated_at: 2026-07-11 19:12:58.494678
---

# GET / Signal bot event history

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/signal/event-history`

> Request Example
    
    
    GET /api/v5/tradingBot/signal/event-history?algoId=623833708424069120
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
after | String | No | Pagination of data to return records `eventCtime` earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records `eventCtime` newer than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "alertMsg": "{\"marketPosition\":\"short\",\"prevMarketPosition\":\"long\",\"action\":\"sell\",\"instrument\":\"ETHUSDT.P\",\"timestamp\":\"2023-10-16T10:50:00.000Z\",\"maxLag\":\"60\",\"investmentType\":\"base\",\"amount\":\"2\"}",
                "algoId": "623833708424069120",
                "eventCtime": "1697453400959",
                "eventProcessMsg": "Processed reverse entry signal and placed ETH-USDT-SWAP order with all available balance",
                "eventStatus": "success",
                "eventType": "signal_processing",
                "eventUtime": "",
                "triggeredOrdData": [
                    {
                        "clOrdId": "O634100754731765763"
                    },
                    {
                        "clOrdId": "O634100754752737282"
                    }
                ]
            }
         ],
         "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
alertMsg | String | Alert message  
algoId | String | Algo ID  
eventType | String | Event type  
`system_action`  
`user_action`  
`signal_processing`  
eventCtime | String | Event timestamp of creation. Unix timestamp format in milliseconds, e.g. `1597026383085`  
eventUtime | String | Event timestamp of update. Unix timestamp format in milliseconds, e.g. `1597026383085`  
eventProcessMsg | String | Event process message  
eventStatus | String | Event status  
`success`  
`failure`  
triggeredOrdData | Array of objects | Triggered sub order data  
> clOrdId | String | Sub order client-supplied id

---

# GET / 获取信号策略历史事件

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/signal/event-history`

> 请求示例
    
    
    GET /api/v5/tradingBot/signal/event-history?algoId=623833708424069120
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略ID  
after | String | 否 | 请求`eventCtime`在此时间之前（更旧的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求`eventCtime`此时间之后（更新的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "alertMsg": "{\"marketPosition\":\"short\",\"prevMarketPosition\":\"long\",\"action\":\"sell\",\"instrument\":\"ETHUSDT.P\",\"timestamp\":\"2023-10-16T10:50:00.000Z\",\"maxLag\":\"60\",\"investmentType\":\"base\",\"amount\":\"2\"}",
                "algoId": "623833708424069120",
                "eventCtime": "1697453400959",
                "eventProcessMsg": "Processed reverse entry signal and placed ETH-USDT-SWAP order with all available balance",
                "eventStatus": "success",
                "eventType": "signal_processing",
                "eventUtime": "",
                "triggeredOrdData": [
                    {
                        "clOrdId": "O634100754731765763"
                    },
                    {
                        "clOrdId": "O634100754752737282"
                    }
                ]
            }
         ],
         "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
alertMsg | String | 提示信息  
algoId | String | 策略ID  
eventType | String | 事件类型  
`system_action`：系统行为  
`user_action`：用户行为  
`signal_processing`：信号下单  
eventCtime | String | 事件发生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
eventUtime | String | 事件更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
eventProcessMsg | String | 事件处理信息  
eventStatus | String | 事件处理状态  
`success`：成功  
`failure`：失败  
triggeredOrdData | Array of objects | 信号触发的子订单的信息  
> clOrdId | String | 子订单自定义ID