---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-fee-type
anchor_id: trading-account-rest-api-set-fee-type
api_type: REST
updated_at: 2026-07-22 19:18:48.763334
---

# Set fee type

Set the fee type.   
  
fee type selection is only effective for Spot. 

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/set-fee-type`

> Request Example
    
    
    POST /api/v5/account/set-fee-type 
    body
    {
        "feeType":"0"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
feeType | String | Yes | Fee type  
`0`: fee is charged in the currency you receive from the trade (default)  
`1`: fee is always charged in the quote currency of the trading pair (only effective for Spot)  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "feeType": "0"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
feeType | String | Fee type  
`0`: fee is charged in the currency you receive from the trade  
`1`: fee is always charged in the quote currency of the trading pair

---

# 设置手续费计价方式

设置手续费计价方式。  
  
手續費計價方式選擇對現貨生效。 

#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/account/set-fee-type`

> 请求示例
    
    
    POST /api/v5/account/set-fee-type 
    body
    {
        "feeType": "0"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
feeType | String | 是 | 手续费计价方式  
`0`: 按交易获得的币种收取手续费（默认）  
`1`: 始终按交易对的计价币种收取手续费（仅适用于现货）  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "feeType": "0"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
feeType | String | 手续费计价方式  
`0`: 按交易获得的币种收取手续费  
`1`: 始终按交易对的计价币种收取手续费