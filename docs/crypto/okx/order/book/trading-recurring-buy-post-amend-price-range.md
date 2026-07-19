---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-recurring-buy-post-amend-price-range
anchor_id: order-book-trading-recurring-buy-post-amend-price-range
api_type: API
updated_at: 2026-07-19 19:15:34.739437
---

# POST / Amend price range

#### Rate Limit: 20 requests per 2 seconds  
  
#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/recurring/amend-price-range`

> Request Example
    
    
    POST /api/v5/tradingBot/recurring/amend-price-range
    body
    {
        "algoId": "2837428373700509696",
        "recurringList": [
            {
                "ccy": "BTC",
                "minPx": "80000",
                "maxPx": "120000"
            }
        ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
algoId | String | Yes | Algo order ID  
recurringList | Array | Yes | Price range settings. The currency must be within the scope of the recurring buy currencies  
>ccy | String | Yes | Recurring buy currency  
>minPx | String | Yes | Minimum price of price range. `""` means no limit  
>maxPx | String | Yes | Maximum price of price range. `""` means no limit  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
algoId | String | Algo order ID  
sCode | String | Event execution status code, `0` indicates success  
sMsg | String | Error message if the event execution failed

---

# POST / 编辑价格区间

#### 限速：20次/2s  
  
#### 限速规则：User ID

#### HTTP请求

`POST /api/v5/tradingBot/recurring/amend-price-range`

> 请求示例
    
    
    POST /api/v5/tradingBot/recurring/amend-price-range
    body
    {
        "algoId": "2837428373700509696",
        "recurringList": [
            {
                "ccy": "BTC",
                "minPx": "80000",
                "maxPx": "120000"
            }
        ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
algoId | String | 是 | 策略订单ID  
recurringList | Array | 是 | 价格区间设置，币种必须在策略定投币种范围内  
>ccy | String | 是 | 定投币种  
>minPx | String | 是 | 价格区间最低价，`""` 代表没有限制  
>maxPx | String | 是 | 价格区间最高价，`""` 代表没有限制  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "algoId": "2837428373700509696",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
algoId | String | 策略订单ID  
sCode | String | 事件执行结果的 code，0 代表成功  
sMsg | String | 事件执行失败时的 msg