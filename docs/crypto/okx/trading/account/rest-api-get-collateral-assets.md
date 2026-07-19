---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-get-collateral-assets
anchor_id: trading-account-rest-api-get-collateral-assets
api_type: REST
updated_at: 2026-07-19 19:14:49.871084
---

# Get collateral assets

#### Rate Limit: 5 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/account/collateral-assets`

> Request Example
    
    
    GET /api/v5/account/collateral-assets
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. "BTC" or "BTC,ETH".  
collateralEnabled | Boolean | No | Whether or not to be a collateral asset  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
              {
                "ccy":"BTC",
                "collateralEnabled": true
              },
              {
                "ccy":"ETH",
                "collateralEnabled": false
              }
        ]  
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
collateralEnabled | Boolean | Whether or not to be a collateral asset

---

# 查看质押币种

#### 限速：5次/2s  
  
#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/collateral-assets`

> 请求示例
    
    
    GET /api/v5/account/collateral-assets
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种  
支持多币种查询（不超过20个），币种之间半角逗号分隔，如 "BTC,ETH"  
collateralEnabled | Boolean | 否 | 是否为质押币  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
              {
                "ccy":"BTC",
                "collateralEnabled": true
              },
              {
                "ccy":"ETH",
                "collateralEnabled": false
              }
        ]  
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 币种，如 `BTC`  
collateralEnabled | Boolean | 是否为质押币