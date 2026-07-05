---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-collateral-assets
anchor_id: trading-account-rest-api-set-collateral-assets
api_type: REST
updated_at: 2026-07-05 19:33:20.956020
---

# Set collateral assets

#### Rate Limit: 5 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/set-collateral-assets`

> Request Example
    
    
    # Set all assets to be collateral
    POST /api/v5/account/set-collateral-assets
    body
    {
        "type":"all",
        "collateralEnabled":true
    }
    
    
    # Set custom assets to be non-collateral
    POST /api/v5/account/set-collateral-assets
    body
    {
        "type":"custom",
        "ccyList":["BTC","ETH"],
        "collateralEnabled":false
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | true | Type  
`all`  
`custom`  
collateralEnabled | Boolean | true | Whether or not set the assets to be collateral  
`true`: Set to be collateral  
`false`: Set to be non-collateral  
ccyList | Array of strings | conditional | Currency list, e.g. ["BTC","ETH"]  
If type=`custom`, the parameter is required.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
          {
            "type":"all",
            "ccyList":["BTC","ETH"],
            "collateralEnabled":false
          }
        ]  
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
type | String | Type  
`all`  
`custom`  
collateralEnabled | Boolean | Whether or not set the assets to be collateral  
`true`: Set to be collateral  
`false`: Set to be non-collateral  
ccyList | Array of strings | Currency list, e.g. ["BTC","ETH"]

---

# 设置质押币种

#### 限速：5次/2s  
  
#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/account/set-collateral-assets`

> 请求示例
    
    
    # 设置全部币种为可质押资产
    POST /api/v5/account/set-collateral-assets
    body
    {
        "type":"all",
        "collateralEnabled":true
    }
    
    
    # 设置自定义不可质押资产
    POST /api/v5/account/set-collateral-assets
    body
    {
        "type":"custom",
        "ccyList":["BTC","ETH"],
        "collateralEnabled":false
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 是 | 设置币种类型  
`all`：全部  
`custom`：自定义  
collateralEnabled | Boolean | 是 | 是否设置为质押币种  
`true`：设置为质押币  
`false`：取消质押币的设置  
ccyList | Array of strings | 可选 | 币种列表，如 ["BTC","ETH"]  
当type=`custom`,该字段必传。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
          {
            "type":"all",
            "ccyList":["BTC","ETH"],
            "collateralEnabled":false
          }
        ]  
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
type | String | 设置币种类型  
`all`：全部  
`custom`：自定义  
collateralEnabled | Boolean | 是否已设置为质押币种  
`true`：设置为质押币  
`false`：取消质押币的设置  
ccyList | Array of strings | 币种列表，如 ["BTC","ETH"]