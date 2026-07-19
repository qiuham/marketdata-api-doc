---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-premium-history
anchor_id: public-data-rest-api-get-premium-history
api_type: REST
updated_at: 2026-07-19 19:16:25.978871
---

# Get premium history

It will return premium data in the past 6 months.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/premium-history`

> Request Example
    
    
    GET /api/v5/public/premium-history?instId=BTC-USDT-SWAP
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`  
Applicable to `SWAP`  
after | String | No | Pagination of data to return records earlier than the requested ts(not included)  
before | String | No | Pagination of data to return records newer than the requested ts(not included)  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "premium": "0.0000578896878167",
                "ts": "1713925924000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. `BTC-USDT-SWAP`  
premium | String | Premium index  
formula: [Max (0, Impact bid price – Index price) – Max (0, Index price – Impact ask price)] / Index price  
ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取溢价历史数据

获取最近6个月的溢价历史数据  
  
#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/public/premium-history`

> 请求示例
    
    
    GET /api/v5/public/premium-history?instId=BTC-USDT-SWAP
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT-SWAP`  
适用于`永续`  
after | String | 否 | 请求此时间戳（不包含）之前的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳（不包含）之后的分页内容，传的值为对应接口的`ts`  
limit | String | 否 | 分页返回的结果集数量，最大为`100`。默认返回`100`条。  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "instId": "BTC-USDT-SWAP",
                "premium": "0.0000578896878167",
                "ts": "1713925924000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID ，如 `BTC-USDT-SWAP`  
premium | String | 溢价指数  
公式：[max (0，深度加权买价 - 指数价格) – max (0，指数价格 – 深度加权卖价)] / 指数价格  
ts | String | 数据产生的时间，Unix时间戳的毫秒数格式，如 `1597026383085`