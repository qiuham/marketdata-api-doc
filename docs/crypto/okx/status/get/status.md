---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#status-get-status
anchor_id: status-get-status
api_type: API
updated_at: 2026-07-11 19:14:49.005336
---

# GET / Status

Get event status of system upgrade.  
  
Planned system maintenance that may result in short interruption (lasting less than 5 seconds) or websocket disconnection (users can immediately reconnect) will not be announced. The maintenance will only be performed during times of low market volatility.

#### Rate Limit: 1 request per 5 seconds

#### HTTP Request

`GET /api/v5/system/status`

> Request Example
    
    
    GET /api/v5/system/status
    
    GET /api/v5/system/status?state=canceled
    
    
    
    
    import okx.Status as Status
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    statusAPI = Status.StatusAPI(
        domain="https://openapi.okx.com",
        flag=flag,
    )
    
    # Get event status of system upgrade
    result = statusAPI.status()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
state | String | No | System maintenance status  
`scheduled`: waiting  
`ongoing`: processing  
`pre_open`: pre_open  
`completed`: completed  
`canceled`: canceled  
Generally, `pre_open` last about 10 minutes. There will be `pre_open` when the time of upgrade is too long.   
If this parameter is not filled, the data with status `scheduled`, `ongoing` and `pre_open` will be returned by default  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "begin": "1672823400000",
                "end": "1672823520000",
                "href": "",
                "preOpenBegin": "",
                "scheDesc": "",
                "serviceType": "8",
                "state": "completed",
                "maintType": "1",
                "env": "1",
                "system": "unified",
                "title": "Trading account system upgrade (in batches of accounts)"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
title | String | The title of system maintenance instructions  
state | String | System maintenance status  
begin | String | Begin time of system maintenance, Unix timestamp format in milliseconds, e.g. `1617788463867`  
end | String | Time of resuming trading totally. Unix timestamp format in milliseconds, e.g. `1617788463867`.  
It is expected end time before `completed`, changed to actual end time after `completed`.  
preOpenBegin | String | The time of pre_open. Canceling orders, placing Post Only orders, and transferring funds to trading accounts are back after `preOpenBegin`.  
href | String | Hyperlink for system maintenance details, if there is no return value, the default value will be empty. e.g. ""  
serviceType | String | Service type  
`0`: WebSocket  
`5`: Trading service  
`6`: Block trading  
`7`: Trading bot  
`8`: Trading service (in batches of accounts)  
`9`: Trading service (in batches of products)  
`10`: Spread trading  
`11`: Copy trading  
`99`: Others (e.g. Suspend partial instruments)  
system | String | System  
`unified`: Trading account  
scheDesc | String | Rescheduled description, e.g. `Rescheduled from 2021-01-26T16:30:00.000Z` to `2021-01-28T16:30:00.000Z`  
maintType | String | Maintenance type  
`1`: Scheduled maintenance  
`2`: Unscheduled maintenance  
`3`: System disruption  
env | String | Environment  
`1`: Production Trading  
`2`: Demo Trading

---

# GET / Status

获取系统升级事件的状态。  
  
由计划系统维护引起的短暂不可用（<5秒）和WebSocket闪断连接（用户可以立即重连）将不会公布。此类维护只会在市场波动性低的时期进行。

#### 限速：1次/5s

#### HTTP请求

`GET /api/v5/system/status`

> 请求示例
    
    
    GET /api/v5/system/status
    
    GET /api/v5/system/status?state=canceled
    
    
    
    
    import okx.Status as Status
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    statusAPI = Status.StatusAPI(
        domain="https://openapi.okx.com",
        flag=flag,
    )
    
    # 获取系统升级事件的状态
    result = statusAPI.status()
    print(result)
    

#### 请求参数

#### 请求示例

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
state | String | 否 | 系统的状态  
`scheduled`：等待中  
`ongoing`：进行中  
`pre_open`：预开放  
`completed`：已完成  
`canceled`：已取消   
当维护时间过长，会存在预开放时间，一般持续10分钟左右。  
不填写此参数，默认返回 等待中、进行中和预开放 的数据  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "begin": "1672823400000",
                "end": "1672823520000",
                "href": "",
                "preOpenBegin": "",
                "scheDesc": "",
                "serviceType": "8",
                "state": "completed",
                "maintType": "1",
                "env": "1",
                "system": "unified",
                "title": "Trading account system upgrade (in batches of accounts)"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
title | String | 系统维护说明的标题  
state | String | 系统维护的状态  
begin | String | 系统维护的开始时间，Unix时间戳的毫秒数格式 如：`1617788463867`  
end | String | 交易全面开放的时间，Unix时间戳的毫秒数格式 如：`1617788463867`   
在维护完成前，是预期结束时间；维护完成后，会变更为实际结束时间。  
preOpenBegin | String | 预开放开始的时间，开放撤单、Post Only 下单和资金转入功能的时间  
href | String | 系统维护详情的超级链接,若无返回值，默认值为空，如 ""  
serviceType | String | 服务类型  
`0`：WebSocket  
`5`：交易服务  
`6`：大宗交易  
`7`：策略交易  
`8`：交易服务 (按账户分批次)  
`9`：交易服务 (按产品分批次)  
`10`：价差交易  
`11`：跟单交易  
`99`：其他（如：停止部分产品交易）  
system | String | 系统  
`unified`：交易账户  
scheDesc | String | 改期进度说明，如 `由 2021-01-26T16:30:00.000Z`改期到`2021-01-28T16:30:00.000Z`  
maintType | String | 维护类型  
`1`：计划维护  
`2`：临时维护  
`3`：系统故障  
env | String | 环境  
`1`：实盘  
`2`：模拟盘