---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-account-mode
anchor_id: trading-account-rest-api-set-account-mode
api_type: REST
updated_at: 2026-07-06 19:52:28.895458
---

# Set account mode

You need to set on the Web/App for the first set of every account mode. If users plan to switch account modes while holding positions, they should first call the preset endpoint to conduct necessary settings, then call the precheck endpoint to get unmatched information, margin check, and other related information, and finally call the account mode switch endpoint to switch account modes.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/set-account-level`

> Request Example
    
    
    POST /api/v5/account/set-account-level
    body
    {
        "acctLv":"1"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
acctLv | String | Yes | Account mode  
`1`: Spot mode  
`2`: Futures mode   
`3`: Multi-currency margin code   
`4`: Portfolio margin mode  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "acctLv": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
acctLv | String | Account mode

---

# 设置账户模式

账户模式的首次设置，需要在网页或手机app上进行。若用户计划在持有仓位的情况下切换账户模式，应该先调用预设置接口进行必要的预设置，再调用预检查接口获取不匹配信息、保证金校验等相关信息，最后调用账户模式切换接口进行账户模式切换。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/account/set-account-level`

> 请求示例
    
    
    POST /api/v5/account/set-account-level
    body
    {
        "acctLv":"1"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
acctLv | String | 是 | 账户模式  
`1`: 现货模式  
`2`: 合约模式   
`3`: 跨币种保证金模式   
`4`: 组合保证金模式  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data" :[
              {
                "acctLv":"1"
              }
        ]  
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
acctLv | String | 账户模式