---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-delivery-exercise-history
anchor_id: public-data-rest-api-get-delivery-exercise-history
api_type: REST
updated_at: 2026-07-18 20:04:35.189690
---

# Get delivery/exercise history

Retrieve delivery records of Futures and exercise records of Options in the last 3 months.  
  
#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP + (Instrument Type + instFamily)

#### HTTP Request

`GET /api/v5/public/delivery-exercise-history`

> Request Example
    
    
    GET /api/v5/public/delivery-exercise-history?instType=OPTION&instFamily=BTC-USD
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # Production trading: 0, Demo trading: 1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # Retrieve delivery records of Futures and exercise records of Options in the last 3 months
    result = publicDataAPI.get_delivery_exercise_history(
        instType="FUTURES",
        uly="BTC-USD"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`FUTURES`  
`OPTION`  
instFamily | String | Yes | Instrument family, only applicable to `FUTURES`/`OPTION`  
after | String | No | Pagination of data to return records earlier than the requested `ts`  
before | String | No | Pagination of data to return records newer than the requested `ts`  
limit | String | No | Number of results per request. The maximum is `100`; The default is `100`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ts":"1597026383085",
                "details":[
                    {
                        "type":"delivery",
                        "insId":"BTC-USD-190927",
                        "px":"0.016"
                    }
                ]
            },
            {
                "ts":"1597026383085",
                "details":[
                    {
                        "insId":"BTC-USD-200529-6000-C",
                        "type":"exercised",
                        "px":"0.016"
                    },
                    {
                        "insId":"BTC-USD-200529-8000-C",
                        "type":"exercised",
                        "px":"0.016"
                    }
                ]
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ts | String | Delivery/exercise time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
details | Array of objects | Delivery/exercise details  
> insId | String | Delivery/exercise contract ID  
> px | String | Delivery/exercise price  
> type | String | Type   
`delivery`   
`exercised`   
`expired_otm`:Out of the money

---

# 获取交割和行权记录

获取3个月内的交割合约的交割记录和期权的行权记录  
  
#### 限速：40次/2s

#### 限速规则：IP + (Instrument Type + instFamily)

#### HTTP请求

`GET /api/v5/public/delivery-exercise-history`

> 请求示例
    
    
    GET /api/v5/public/delivery-exercise-history?instType=OPTION&uly=BTC-USD
    
    
    
    import okx.PublicData as PublicData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    publicDataAPI = PublicData.PublicAPI(flag=flag)
    
    # 获取交割和行权记录
    result = publicDataAPI.get_delivery_exercise_history(
        instType="FUTURES",
        uly="BTC-USD"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`FUTURES`：交割合约  
`OPTION`：期权  
instFamily | String | 是 | 交易品种  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`ts`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ts":"1597026383085",
                "details":[
                    {
                        "type":"delivery",
                        "insId":"BTC-USD-190927",
                        "px":"0.016"
                    }
                ]
            },
            {
                "ts":"1597026383085",
                "details":[
                    {
                        "insId":"BTC-USD-200529-6000-C",
                        "type":"exercised",
                        "px":"0.016"
                    },
                    {
                        "insId":"BTC-USD-200529-8000-C",
                        "type":"exercised",
                        "px":"0.016"
                    }
                ]
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 交割/行权日期，Unix时间戳的毫秒数格式，如 `1597026383085`  
details | Array of objects | 详细数据  
> insId | String | 交割/行权的合约ID  
> px | String | 交割/行权的价格  
> type | String | 类型   
`delivery`：交割   
`exercised`：实值已行权   
`expired_otm`：虚值已过期