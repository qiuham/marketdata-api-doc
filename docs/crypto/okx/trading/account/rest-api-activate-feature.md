---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-account-rest-api-activate-feature
anchor_id: trading-account-rest-api-activate-feature
api_type: REST
updated_at: 2026-10-02 19:17:37.863554
---

# Activate feature

If order placement returns error code `54109`, call the following endpoint to activate USDC trading for the account; otherwise, you do not need to call this endpoint.  
  
#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/account/activate-feature`

> Request example
    
    
    POST /api/v5/account/activate-feature
    body
    {
        "feature": "1"
    }
    

#### Request parameters

**Parameter** | **Type** | **Required** | **Description**  
---|---|---|---  
feature | String | Yes | Feature to activate  
`1`: USDC order book trading.  
Call this endpoint only when order placement returns error code `54109`; otherwise, you do not need to call it.  
Error code `51773` only indicates that this activation feature is not supported. Whether you can trade `Crypto-USDC` instruments depends on whether an order can be placed successfully.  
Activation is shared between master accounts and sub-accounts. The master account or any of its sub-accounts only needs to call this endpoint once.  
  
> Response example
    
    
    {
        "code": "0",
        "msg": "",
        "data": []
    }
    

#### Response parameters

None

---

# 开通功能

若下单返回错误码 `54109`，请调用以下接口为账户开通 USDC 交易功能；否则无需调用该接口。  
  
#### 限速：5 次/2 秒

#### 限速规则：User ID

#### HTTP 请求

`POST /api/v5/account/activate-feature`

> 请求示例
    
    
    POST /api/v5/account/activate-feature
    body
    {
        "feature": "1"
    }
    

#### 请求参数

**参数名** | **类型** | **是否必须** | **描述**  
---|---|---|---  
feature | String | 是 | 要开通的具体功能  
`1`：USDC 订单簿交易功能。  
仅当下单返回错误码 `54109` 时，才需要调用该功能；否则无需调用。  
错误码 `51773` 仅表示不支持使用该激活功能。能否交易 `Crypto-USDC` 产品，以是否能够成功下单为准。  
母账户与子账户之间共享开通状态，母账户或任一子账户仅需调用一次。  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": []
    }
    

#### 返回参数

无