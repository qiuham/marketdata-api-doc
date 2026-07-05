---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-set-risk-offset-amount
anchor_id: trading-account-rest-api-set-risk-offset-amount
api_type: REST
updated_at: 2026-07-05 19:33:18.464211
---

# Set risk offset amount

Set risk offset amount. This does not represent the actual spot risk offset amount. Only applicable to Portfolio Margin Mode.  
  
#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/account/set-riskOffset-amt`

> Request Example
    
    
    # Set spot risk offset amount
    POST /api/v5/account/set-riskOffset-amt
    body
    {
       "ccy": "BTC",
       "clSpotInUseAmt": "0.5"
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency  
clSpotInUseAmt | String | Yes | Spot risk offset amount defined by users  
  
> Response Example
    
    
    {
       "code": "0",
       "msg": "",
       "data": [
          {
             "ccy": "BTC",
             "clSpotInUseAmt": "0.5"
          }
       ]
    }
    

#### Response Parameters

Parameters | Types | Description  
---|---|---  
ccy | String | Currency  
clSpotInUseAmt | String | Spot risk offset amount defined by users

---

# 设置现货对冲占用

用户自定义现货对冲占用数量，不代表实际现货对冲占用数量。仅适用于组合保证金模式。  
  
#### 限速：10次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/account/set-riskOffset-amt`

> 请求示例
    
    
    # 设置现货对冲占用
    POST /api/v5/account/set-riskOffset-amt
    {
       "ccy": "BTC",
       "clSpotInUseAmt": "0.5"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种，如 `BTC`  
clSpotInUseAmt | String | 是 | 用户自定义现货对冲数量  
  
> 返回示例
    
    
    {
       "code": "0",
       "msg": "",
       "data": [
          {
             "ccy": "BTC",
             "clSpotInUseAmt": "0.5"
          }
       ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
clSpotInUseAmt | String | 用户自定义现货对冲数量