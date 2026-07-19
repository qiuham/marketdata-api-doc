---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-markets
anchor_id: public-data-rest-api-get-markets
api_type: REST
updated_at: 2026-07-19 19:16:20.051094
---

# Get markets

Get markets for events in OKX prediction markets. Return data in expTime and floorStrike descending order.  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/event-contract/markets`

> Request Example
    
    
    GET /api/v5/public/event-contract/markets?seriesId=BTC-ABOVE-DAILY
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
seriesId | String | Yes | Series ID, e.g. `BTC-ABOVE-DAILY`  
eventId | String | No | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600`  
instId | String | No | Instrument ID, e.g. `BTC-ABOVE-DAILY-260224-1600-65000`  
state | String | No | Filter by market status.  
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
                "instId": "BTC-ABOVE-DAILY-260224-1600-65000",
                "listTime": "1769697132335",
                "expTime": "1769697132335",
                "state": "live",
                "fixTime": "",
                "outcome": "0",
                "floorStrike": "120000",
                "capStrike": "",
                "settleValue": "",
                "disputed": false,
                "hitDir": ""
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`  
eventId | String | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600`  
instId | String | Instrument ID, e.g. `BTC-ABOVE-DAILY-260224-1600-65000`  
listTime | String | Listing time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
fixTime | String | Strike price fixing time, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable to `price_up_down` settlement method.  
expTime | String | Strike time for this event, Unix timestamp format in milliseconds, e.g. `1597026383085`. Updated once the market is settled.  
state | String | Market state.  
`preopen`  
`live`  
`settling`  
`expired`  
disputed | Boolean | Whether the market has been disputed.  
`true`  
`false`  
outcome | String | Market outcome.  
`0`: Not available  
`1`: YES  
`2`: NO.  
`1`/`2` only applicable when state is `expired`  
floorStrike | String | Minimum expiration value that leads to a YES outcome  
capStrike | String | Maximum expiration value that leads to a YES outcome for `between` method. `"INF"` indicates no upper bound (the topmost bracket).  
Returns `""` for non-`between` methods.  
settleValue | String | Settlement value  
Only return when the state is `expired`  
hitDir | String | Hit direction. Only applicable when the settlement method is `hit`.  
`up`: price hit from below  
`dn`: price hit from above  
`""`: not applicable (non-`hit` methods)

---

# 获取市场

获取 OKX 预测市场某事件下的市场列表。返回数据按 expTime 和 floorStrike 降序排列。  
  
#### 限速：10次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/event-contract/markets`

> 请求示例
    
    
    GET /api/v5/public/event-contract/markets?seriesId=BTC-ABOVE-DAILY
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
seriesId | String | 是 | 系列 ID，如 `BTC-ABOVE-DAILY`  
eventId | String | 否 | 事件 ID，如 `BTC-ABOVE-DAILY-260224-1600`  
instId | String | 否 | 产品 ID，如 `BTC-ABOVE-DAILY-260224-1600-65000`  
state | String | 否 | 市场状态过滤。  
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
                "instId": "BTC-ABOVE-DAILY-260224-1600-65000",
                "listTime": "1769697132335",
                "expTime": "1769697132335",
                "state": "live",
                "fixTime": "",
                "outcome": "0",
                "floorStrike": "120000",
                "capStrike": "",
                "settleValue": "",
                "disputed": false,
                "hitDir": ""
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
seriesId | String | 系列 ID，如 `BTC-ABOVE-DAILY`  
eventId | String | 事件 ID，如 `BTC-ABOVE-DAILY-260224-1600`  
instId | String | 产品 ID，如 `BTC-ABOVE-DAILY-260224-1600-65000`  
listTime | String | 上线时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
fixTime | String | 行权价格确定时间。Unix时间戳的毫秒数格式，如 `1597026383085`。仅适用于 `price_up_down` 结算方式。  
expTime | String | 该事件的行权时间。Unix时间戳的毫秒数格式，如 `1597026383085`。结算后更新。  
state | String | 市场状态。  
`preopen`  
`live`  
`settling`  
`expired`  
disputed | Boolean | 是否存在争议。  
`true`  
`false`  
outcome | String | 市场结果。  
`0`：未确定  
`1`：YES  
`2`：NO。  
`1`/`2` 仅在 state 为 `expired` 时适用  
floorStrike | String | 导致 YES 结果的最低到期价格  
capStrike | String | `between` 结算方式中导致 YES 结果的最大到期值。`"INF"` 表示无上限（最高区间）。  
非 `between` 方式返回 `""`。  
settleValue | String | 结算价格。  
仅在 state 为 `expired` 时返回  
hitDir | String | 触及方向。仅在结算方式为 `hit` 时适用。  
`up`：价格从下方触及  
`dn`：价格从上方触及  
`""`：不适用（非 `hit` 方式）