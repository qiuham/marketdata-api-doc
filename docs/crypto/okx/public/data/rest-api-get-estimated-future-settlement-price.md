---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-estimated-future-settlement-price
anchor_id: public-data-rest-api-get-estimated-future-settlement-price
api_type: REST
updated_at: 2026-07-09 19:38:13.094481
---

# Get estimated future settlement price

Retrieve the estimated settlement price which will only have a return value one hour before the settlement.  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/estimated-settlement-info`

> Request Example
    
    
    GET /api/v5/public/estimated-settlement-info?instId=XRP-USDT-250307
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `XRP-USDT-250307`   
only applicable to `FUTURES`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "estSettlePx": "2.5666068562369959",
                "instId": "XRP-USDT-250307",
                "nextSettleTime": "1741248000000",
                "ts": "1741246429748"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. `XRP-USDT-250307`  
nextSettleTime | String | Next settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estSettlePx | String | Estimated settlement price  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取交割预估结算价格

获取交割合约预估结算价。只有结算前一小时才有返回值。  
  
#### 限速：10次/2s

#### 限速规则：IP + Instrument ID

#### HTTP请求

`GET /api/v5/public/estimated-settlement-info`

> 请求示例
    
    
    GET /api/v5/public/estimated-settlement-info?instId=XRP-USDT-250307
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `XRP-USDT-250307`  
仅适用于`交割`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "estSettlePx": "2.5666068562369959",
                "instId": "XRP-USDT-250307",
                "nextSettleTime": "1741248000000",
                "ts": "1741246429748"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID， 如 `XRP-USDT-250307`  
nextSettleTime | String | 下一次结算时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
estSettlePx | String | 预估结算价格  
ts | String | 数据返回时间，Unix时间戳的毫秒数格式，如 `1597026383085`