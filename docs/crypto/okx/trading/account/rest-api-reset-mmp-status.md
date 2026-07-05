---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-reset-mmp-status
anchor_id: trading-account-rest-api-reset-mmp-status
api_type: REST
updated_at: 2026-07-05 19:33:21.574249
---

# Reset MMP Status

You can unfreeze by this endpoint once MMP is triggered.  
  
  
Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/mmp-reset`

> Request Example
    
    
    POST /api/v5/account/mmp-reset
    body
    {
        "instType":"OPTION",
        "instFamily":"BTC-USD"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | No | Instrument type  
`OPTION`  
The default is `OPTION  
instFamily | String | Yes | Instrument family  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
result | Boolean | Result of the request `true`, `false`

---

# 重置 MMP 状态

一旦 MMP 被触发，可以使用该接口解冻。  
仅适用于组合保证金账户模式下的期权订单，且有 MMP 权限。  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/account/mmp-reset`

> 请求示例
    
    
    POST /api/v5/account/mmp-reset
    body
    {
        "instType":"OPTION",
        "instFamily":"BTC-USD"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 否 | 交易产品类型  
`OPTION`:期权  
默认为期权  
instFamily | String | 是 | 交易品种  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
result | Boolean | 重置结果  
`true`:将做市商保护状态重置为了 inactive 状态  
false：重置失败