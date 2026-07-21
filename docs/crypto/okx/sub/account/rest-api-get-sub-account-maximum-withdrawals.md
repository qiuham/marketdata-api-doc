---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#sub-account-rest-api-get-sub-account-maximum-withdrawals
anchor_id: sub-account-rest-api-get-sub-account-maximum-withdrawals
api_type: REST
updated_at: 2026-07-21 19:27:32.132766
---

# Get sub-account maximum withdrawals

Retrieve the maximum withdrawal information of a sub-account via the master account (applies to master accounts only). If no currency is specified, the transferable amount of all owned currencies will be returned.  
  
#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/account/subaccount/max-withdrawal`

> Request Example
    
    
    GET /api/v5/account/subaccount/max-withdrawal?subAcct=test1
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
subAcct | String | Yes | Sub-account name  
ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`.  
  
> Response Example
    
    
    {
       "code":"0",
       "data":[
          {
             "ccy":"BTC",
             "maxWd":"3",
             "maxWdEx":"",
             "spotOffsetMaxWd":"3",
             "spotOffsetMaxWdEx":""
          },
          {
             "ccy":"ETH",
             "maxWd":"15",
             "maxWdEx":"",
             "spotOffsetMaxWd":"15",
             "spotOffsetMaxWdEx":""
          },
          {
             "ccy":"USDT",
             "maxWd":"10600",
             "maxWdEx":"",
             "spotOffsetMaxWd":"10600",
             "spotOffsetMaxWdEx":""
          }
       ],
       "msg":""
    }
    

#### Response parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
maxWd | String | Max withdrawal (excluding borrowed assets under `Multi-currency margin`)  
maxWdEx | String | Max withdrawal (including borrowed assets under `Multi-currency margin`)  
spotOffsetMaxWd | String | Max withdrawal under Spot-Derivatives risk offset mode (excluding borrowed assets under `Portfolio margin`)   
Applicable to `Portfolio margin`  
spotOffsetMaxWdEx | String | Max withdrawal under Spot-Derivatives risk offset mode (including borrowed assets under `Portfolio margin`)   
Applicable to `Portfolio margin`

---

# 获取子账户最大可转余额

获取子账户最大可转余额（适用于母账户）。不指定币种会返回所有拥有的币种资产可划转数量。  
  
#### 限速：20次/2s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/account/subaccount/max-withdrawal`

> 请求示例
    
    
    GET /api/v5/account/subaccount/max-withdrawal?subAcct=test1
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
subAcct | String | 是 | 子账户名称  
ccy | String | 否 | 币种，如 `BTC`   
支持多币种查询（不超过20个），币种之间半角逗号分隔  
  
> 返回结果
    
    
    {
       "code":"0",
       "data":[
          {
             "ccy":"BTC",
             "maxWd":"3",
             "maxWdEx":"",
             "spotOffsetMaxWd":"3",
             "spotOffsetMaxWdEx":""
          },
          {
             "ccy":"ETH",
             "maxWd":"15",
             "maxWdEx":"",
             "spotOffsetMaxWd":"15",
             "spotOffsetMaxWdEx":""
          },
          {
             "ccy":"USDT",
             "maxWd":"10600",
             "maxWdEx":"",
             "spotOffsetMaxWd":"10600",
             "spotOffsetMaxWdEx":""
          }
       ],
       "msg":""
    }
    

#### Response Parameters

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种  
maxWd | String | 最大可划转数量（不包含`跨币种保证金模式`借币金额）  
maxWdEx | String | 最大可划转数量（包含`跨币种保证金模式`借币金额）  
spotOffsetMaxWd | String | 现货对冲不支持借币最大可转数量   
仅适用于`组合保证金模式`  
spotOffsetMaxWdEx | String | 现货对冲支持借币的最大可转数量   
仅适用于`组合保证金模式`