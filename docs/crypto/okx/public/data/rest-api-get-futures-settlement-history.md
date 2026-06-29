---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-futures-settlement-history
anchor_id: public-data-rest-api-get-futures-settlement-history
api_type: REST
updated_at: 2026-06-29 19:57:14.424545
---

# Get futures settlement history

Retrieve settlement records of futures in the last 3 months.  
  
#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP + (Instrument Family)

#### HTTP Request

`GET /api/v5/public/settlement-history`

> Request Example
    
    
    GET /api/v5/public/settlement-history?instFamily=XRP-USD
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instFamily | String | Yes | Instrument family  
after | String | No | Pagination of data to return records earlier than (not include) the requested `ts`  
before | String | No | Pagination of data to return records newer than (not include) the requested `ts`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "instId": "XRP-USDT-250307",
                        "settlePx": "2.5192078615298715"
                    }
                ],
                "ts": "1741161600000"
            },
            {
                "details": [
                    {
                        "instId": "XRP-USDT-250307",
                        "settlePx": "2.5551316341327384"
                    }
                ],
                "ts": "1741075200000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ts | String | Settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
details | Array of objects | Settlement info  
> instId | String | Instrument ID  
> settlePx | String | Settlement price

---

# 获取交割结算记录

获取3个月内的交割合约的结算记录  
  
#### 限速：40次/2s

#### 限速规则：IP + (Instrument Family)

#### HTTP请求

`GET /api/v5/public/settlement-history`

> 请求示例
    
    
    GET /api/v5/public/settlement-history?instFamily=XRP-USDT
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instFamily | String | 是 | 交易品种  
after | String | 否 | 请求此时间戳之前（不包含）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（不包含）的分页内容，传的值为对应接口的`ts`  
limit | String | 否 | 分页返回的结果集数量，最大为`100`，不填默认返回`100`条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "details": [
                    {
                        "instId": "XRP-USDT-250307",
                        "settlePx": "2.5192078615298715"
                    }
                ],
                "ts": "1741161600000"
            },
            {
                "details": [
                    {
                        "instId": "XRP-USDT-250307",
                        "settlePx": "2.5551316341327384"
                    }
                ],
                "ts": "1741075200000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 结算日期，Unix时间戳的毫秒数格式，如 `1597026383085`  
details | Array of objects | 详细数据  
> instId | String | 产品ID  
> settlePx | String | 结算价格