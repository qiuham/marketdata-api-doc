---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-get-account-rate-limit
anchor_id: order-book-trading-trade-get-account-rate-limit
api_type: API
updated_at: 2026-07-19 19:15:05.213859
---

# GET / Account rate limit

Get account rate limit related information.   

Only new order requests and amendment order requests will be counted towards this limit. For batch order requests consisting of multiple orders, each order will be counted individually.   

For details, please refer to [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit)

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/account-rate-limit`

> Request Example
    
    
    # Get the account rate limit
    GET /api/v5/trade/account-rate-limit
    
    

#### Request Parameters

None

> Response Example
    
    
    {
       "code":"0",
       "data":[
          {
             "accRateLimit":"2000",
             "fillRatio":"0.1234",
             "mainFillRatio":"0.1234",
             "nextAccRateLimit":"2000",
             "ts":"123456789000"
          }
       ],
       "msg":""
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fillRatio | String | Sub account fill ratio during the monitoring period.   
Applicable to users with trading fee tier >= VIP 5; other users will receive `""`.  
If there has been no trading activity on the account in the past 7 days, `""` will be returned.  
If there is no executed volume during the monitoring period, `"0"` will be returned.  
If there is executed volume but no order operation count during the monitoring period, `"9999"` will be returned.  
mainFillRatio | String | Master account aggregated fill ratio during the monitoring period.   
Applicable to users with trading fee tier >= VIP 5; other users will receive `""`.  
If there has been no trading activity on the account in the past 7 days, `""` will be returned.  
If there is no executed volume during the monitoring period, `"0"` will be returned.  
accRateLimit | String | Current sub-account rate limit per 2 seconds  
nextAccRateLimit | String | Expected sub-account rate limit (per 2 seconds) in the next monitoring period.   
Applicable to users with trading fee tier >= VIP 5; other users will receive `""`.  
ts | String | Data update timestamp   
For users with trading fee tier >= VIP 5, the data will be generated daily at 08:00 am (UTC)   
For users with trading fee tier < VIP 5, the current timestamp will be returned.

---

# GET / 获取账户限速

获取账户限速相关信息  

仅有新订单及修改订单请求会被计入此限制。对于包含多个订单的批量请求，每个订单将被单独计数。  

更多细节，请见 [基于成交比率的子账户限速](/docs-v5/zh/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit)

#### 限速：1次/s

#### 限速规则：User ID

#### HTTP请求

`GET /api/v5/trade/account-rate-limit`

> 请求示例
    
    
    # 获取账户限速相关信息
    GET /api/v5/trade/account-rate-limit
    
    

#### 请求参数

None

> 返回结果
    
    
    {
       "code":"0",
       "data":[
          {
             "accRateLimit":"2000",
             "fillRatio":"0.1234",
             "mainFillRatio":"0.1234",
             "nextAccRateLimit":"2000",
             "ts":"123456789000"
          }
       ],
       "msg":`""`
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fillRatio | String | 监测期内子账户的成交比率。   
适用于交易费等级 >= VIP 5 的用户，其他用户返回 `""`。  
若账户在过去 7 天内无任何成交数据，则返回 `""`。  
若监测期内无成交量，则返回 `"0"`。  
若监测期内有成交量但无下单操作数，则返回 `"9999"`。  
mainFillRatio | String | 监测期内母账户合计成交比率。  
适用于交易费等级 >= VIP 5 的用户，其他用户返回 `""`。  
若账户在过去 7 天内无任何成交数据，则返回 `""`。  
若监测期内无成交量，则返回 `"0"`。  
accRateLimit | String | 当前子账户交易限速（每两秒）  
nextAccRateLimit | String | 下一评估周期预计的子账户交易限速（每两秒）。  
适用于交易费等级 >= VIP 5的用户，其余用户返回 `""` 。  
ts | String | 数据更新时间   
对于交易费等级>= VIP 5的用户，数据将于每日 08:00（UTC）生成   
对于交易费等级 < VIP 5的用户，返回当前时间戳 。