---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-sol-staking-get-product-info
anchor_id: financial-product-sol-staking-get-product-info
api_type: API
updated_at: 2026-07-18 20:05:18.090701
---

# GET / Product info

#### Rate Limit: 3 requests per second  
  
#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/product-info`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/product-info
    
    
    
    
    

> Response Example
    
    
    {
        "code": "0",
        "data": {
            "fastRedemptionAvail": "240",
            "fastRedemptionDailyLimit": "240",
            "rate": "5.57",
            "redemptDays": "2",
            "minAmt": "0.01"
        },
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fastRedemptionDailyLimit | String | Fast redemption daily limit  
The master account and sub-accounts share the same limit  
fastRedemptionAvail | String | Currently fast redemption max available amount  
rate | String | Latest OKSOL APY  
redemptDays | String | Redemption days of OKSOL  
minAmt | String | Minimum subscription amount of OKSOL

---

# GET / 获取产品信息

#### 限速：3 次/s  
  
#### 限速规则：User ID

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/product-info`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/product-info
    
    
    
    
    

> 返回结果
    
    
    {
        "code": "0",
        "data": {
            "fastRedemptionAvail": "240",
            "fastRedemptionDailyLimit": "240",
            "rate": "5.57",
            "redemptDays": "2",
            "minAmt": "0.01"
        },
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fastRedemptionDailyLimit | String | 快速赎回每日最高份额  
母账户和子账户共享同一个限额  
fastRedemptionAvail | String | 当前剩余最大可赎回数量  
rate | String | 最新 OKSOL 年化收益率  
redemptDays | String | OKSOL 赎回天数  
minAmt | String | OKSOL 最低申购数量