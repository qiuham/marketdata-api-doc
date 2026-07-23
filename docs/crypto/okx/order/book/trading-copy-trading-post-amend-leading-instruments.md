---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-copy-trading-post-amend-leading-instruments
anchor_id: order-book-trading-copy-trading-post-amend-leading-instruments
api_type: API
updated_at: 2026-07-23 19:21:48.695352
---

# POST / Amend leading instruments

The leading trader can amend current leading instruments, need to set initial leading instruments while applying to become a leading trader.  
All non-leading instruments can't have position or pending orders for the current request when setting non-leading instruments as leading instruments.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/set-instruments`

> Request example
    
    
    POST /api/v5/copytrading/set-instruments
    body
    {
        "instId": "BTC-USDT-SWAP,ETH-USDT-SWAP"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`SPOT`  
`SWAP`, the default value  
instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP. If there are multiple instruments, separate them with commas.  
The value of `instId` must include all instruments that you are going to have the lead trading with because the previous settings will be overwritten after the current request is set successfully  

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
            }
        ],
        "msg": ""
    }
    

#### Response parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
enabled | Boolean | Whether you set it successfully  
`true` or `false`

---

# POST / 交易员修改带单产品

交易员修改带单产品的设置。初始带单产品在申请带单交易员时进行设置。  
非带单产品修改为带单产品时，该次请求中所有的非带单产品不能有持仓或者挂单。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/copytrading/set-instruments`

> 请求示例
    
    
    POST /api/v5/copytrading/set-instruments
    body
    {
        "instId": "BTC-USDT-SWAP,ETH-USDT-SWAP"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 产品类型  
SPOT：币币  
SWAP：永续合约，默认值  
instId | String | 是 | 产品ID，如 BTC-USDT-SWAP，多个产品用半角逗号隔开  
如果进行多个产品带单，`instId`传值需要包括所有将要带单的产品，因为当前请求设置成功后，之前的设置会被覆盖掉  

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
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品id， 如 BTC-USDT-SWAP  
enabled | Boolean | `true` 或 `false`  
`true` 代表设置成功  
`false` 代表设置失败