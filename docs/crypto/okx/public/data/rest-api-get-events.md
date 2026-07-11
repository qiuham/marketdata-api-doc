---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-events
anchor_id: public-data-rest-api-get-events
api_type: REST
updated_at: 2026-07-11 19:13:48.856151
---

# Get events

Get events for a series in OKX prediction markets. Returns all event records, including expired ones. Return data in expTime and eventId descending order.  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Public

#### HTTP Request

`GET /api/v5/public/event-contract/events`

> Request Example
    
    
    GET /api/v5/public/event-contract/events?seriesId=BTC-ABOVE-DAILY
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
seriesId | String | Yes | Series ID, e.g. `BTC-ABOVE-DAILY`  
eventId | String | No | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600`  
state | String | No | Event state filter.  
`preopen`  
`live`  
`settling`  
`expired`  
limit | String | No | Number of results per request. Maximum is 100. Default is 100.  
before | String | No | Pagination. Returns records newer than the requested `expTime`, not included.  
after | String | No | Pagination. Returns records earlier than the requested `expTime`, not included.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "eventId": "BTC-ABOVE-DAILY-260224-1600",
                "expTime": "1769697132335",
                "state": "live"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`  
eventId | String | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600`  
fixTime | String | Strike price fixing time, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable to `price_up_down` settlement method.  
expTime | String | The specific strike time this event is based on, Unix timestamp format in milliseconds, e.g. `1597026383085`  
state | String | Event state.  
`preopen`  
`live`  
`settling`  
`expired`

---

# 获取事件

获取 OKX 预测市场某系列下的事件列表，包含已到期事件。返回数据按 expTime 和 eventId 降序排列。  
  
#### 限速：10次/2s

#### 限速规则：IP

#### 权限：公共

#### HTTP请求

`GET /api/v5/public/event-contract/events`

> 请求示例
    
    
    GET /api/v5/public/event-contract/events?seriesId=BTC-ABOVE-DAILY
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
seriesId | String | 是 | 系列 ID，如 `BTC-ABOVE-DAILY`  
eventId | String | 否 | 事件 ID，如 `BTC-ABOVE-DAILY-260224-1600`  
state | String | 否 | 事件状态过滤。  
`preopen`  
`live`  
`settling`  
`expired`  
limit | String | 否 | 返回结果数量，最大 100，默认 100  
before | String | 否 | 分页，返回早于请求 `expTime` 的更新记录，不包含该时间戳  
after | String | 否 | 分页，返回晚于请求 `expTime` 的更旧记录，不包含该时间戳  
  
> 返回示例
    
    
    {
        "code": "0",
        "data": [
            {
                "seriesId": "BTC-ABOVE-DAILY",
                "eventId": "BTC-ABOVE-DAILY-260224-1600",
                "expTime": "1769697132335",
                "state": "live"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`  
eventId | String | 事件 ID，如 `BTC-ABOVE-DAILY-260224-1600`  
fixTime | String | 执行价格确定时间。Unix时间戳的毫秒数格式，如 `1597026383085`。仅适用于 `price_up_down` 结算方式。  
expTime | String | 该事件的行权时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
state | String | 事件状态。  
`preopen`  
`live`  
`settling`  
`expired`