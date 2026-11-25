---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-market-maker-program-post-register-glp-c-pairs
anchor_id: overview-market-maker-program-post-register-glp-c-pairs
api_type: API
updated_at: 2026-11-25 18:59:29.179863
---

# POST / Register GLP-C pairs

Register one or more instruments for the GLP-C (Global Liquidity Program — Category C) market maker program. GLP-C assesses market maker order book depth on tail-end trading pairs on an hourly basis. Supports batch registration; each instrument returns an individual result code.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/users/glp/c/register-pairs`

> Request Example
    
    
    POST /api/v5/users/glp/c/register-pairs
    body
    {
        "instIds": ["DOGE-USDT", "SHIB-USDT", "PEPE-USDT-SWAP"]
    }
    

#### Request Parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
instIds | Array of strings | Yes | List of instrument IDs to register for GLP-C  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "sCode": "0",
                "sMsg": ""
            },
            {
                "instId": "SHIB-USDT",
                "sCode": "0",
                "sMsg": ""
            },
            {
                "instId": "PEPE-USDT-SWAP",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
sCode | String | Result code for this instrument. `0` means success  
sMsg | String | Result message for this instrument

---

# POST / 注册 GLP-C 币对

为 GLP-C（全球流动性计划 — C 类）做市商激励项目注册一个或多个交易产品。GLP-C 以每小时为周期，考核做市商在长尾币对上的订单簿挂单深度。支持批量注册，每个产品独立返回结果码。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/users/glp/c/register-pairs`

> 请求示例
    
    
    POST /api/v5/users/glp/c/register-pairs
    body
    {
        "instIds": ["DOGE-USDT", "SHIB-USDT", "PEPE-USDT-SWAP"]
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
instIds | Array of strings | 是 | 要注册 GLP-C 的产品ID列表  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "DOGE-USDT",
                "sCode": "0",
                "sMsg": ""
            },
            {
                "instId": "SHIB-USDT",
                "sCode": "0",
                "sMsg": ""
            },
            {
                "instId": "PEPE-USDT-SWAP",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
sCode | String | 该产品的结果码。`0` 表示成功  
sMsg | String | 该产品的结果消息