---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-dca-trading-get-dca-cycle-list
anchor_id: order-book-trading-dca-trading-get-dca-cycle-list
api_type: API
updated_at: 2026-07-04 19:37:55.257575
---

# GET / DCA cycle list

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate Limit Rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/dca/cycle-list`

> Request Example
    
    
    GET /api/v5/tradingBot/dca/cycle-list?algoId=2833925189933756416&algoOrdType=contract_dca
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo ID  
algoOrdType | String | Yes | Algo order type  
`contract_dca`: Contract DCA order  
`spot_dca`: Spot DCA order  
instId | String | No | Instrument ID  
after | String | No | Pagination of data to return records earlier than the requested `cycleId`  
before | String | No | Pagination of data to return records newer than the requested `cycleId`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoClOrdId": "",
                "cycleId": "9876543",
                "currentCycle": true,
                "realizedPnl": "12.5",
                "startTime": "1597026383085",
                "endTime": "",
                "fee": "-0.3",
                "avgPx": "41500",
                "tpPx": "43000"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo ID  
algoClOrdId | String | Client-supplied Algo ID  
cycleId | String | Cycle ID  
currentCycle | Boolean | Whether it is the current cycle  
`true` or `false`  
realizedPnl | String | Realized PnL  
startTime | String | Cycle start time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
endTime | String | Cycle end time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
fee | String | Accumulated fee in the cycle  
Negative number represents the user transaction fee charged by the platform. Positive number represents rebate.  
avgPx | String | Average open price  
tpPx | String | Take-profit price

---

# GET / 获取马丁周期列表

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/tradingBot/dca/cycle-list`

> 请求示例
    
    
    GET /api/v5/tradingBot/dca/cycle-list?algoId=2833925189933756416&algoOrdType=contract_dca
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单 ID  
algoOrdType | String | 是 | 策略订单类型  
`contract_dca`：合约马丁委托  
`spot_dca`：现货马丁委托  
instId | String | 否 | 产品 ID  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 `cycleId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 `cycleId`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2833925189933756416",
                "algoClOrdId": "",
                "cycleId": "9876543",
                "currentCycle": true,
                "realizedPnl": "12.5",
                "startTime": "1597026383085",
                "endTime": "",
                "fee": "-0.3",
                "avgPx": "41500",
                "tpPx": "43000"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单 ID  
algoClOrdId | String | 客户端自定义策略单ID  
cycleId | String | 策略周期 ID  
currentCycle | Boolean | 是否是当轮周期  
`true` 或 `false`  
realizedPnl | String | 已实现盈亏  
startTime | String | 周期开启时间，Unix 时间戳毫秒数，如 `1597026383085`  
endTime | String | 周期结束时间，Unix 时间戳毫秒数，如 `1597026383085`  
fee | String | 累计手续费金额，正数代表平台返佣，负数代表平台扣除  
avgPx | String | 开仓均价  
tpPx | String | 止盈价格