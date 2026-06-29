---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-get-leading-instruments
anchor_id: order-book-trading-copy-trading-get-leading-instruments
api_type: API
updated_at: 2026-06-29 19:56:29.724145
---

# GET / Leading instruments

Retrieve instruments that are supported to lead by the platform. Retrieve instruments that the lead trader has set.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/copytrading/instruments`

> Request example
    
    
    GET /api/v5/copytrading/instruments
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`, the default value  
  
> Response example
    
    
    {
        "code": "0",
        "data": [
            {
                "enabled": true,
                "instId": "BTC-USDT-SWAP"
            },
            {
                "enabled": true,
                "instId": "ETH-USDT-SWAP"
            },
            {
                "enabled": false,
                "instId": "ADA-USDT-SWAP"
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
enabled | Boolean | Whether instrument is a lead instrument. `true` or `false`

---

# GET / 获取带单产品

获取平台支持带单的产品，以及获取带单员正在带单的产品  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/copytrading/instruments`

> 请求示例
    
    
    GET /api/v5/copytrading/instruments
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约，默认值  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "enabled": true,
                "instId": "BTC-USDT-SWAP"
            },
            {
                "enabled": true,
                "instId": "ETH-USDT-SWAP"
            },
            {
                "enabled": false,
                "instId": "ADA-USDT-SWAP"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
enabled | Boolean | 是否设置了带单 `true` 或 `false`