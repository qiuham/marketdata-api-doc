---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-exchange-rate
anchor_id: public-data-rest-api-get-exchange-rate
api_type: REST
updated_at: 2026-07-06 19:54:09.467533
---

# Get exchange rate

This interface provides the average exchange rate data for 2 weeks

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/exchange-rate`

> Request Example
    
    
    GET /api/v5/market/exchange-rate
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve average exchange rate data for 2 weeks
    result = marketDataAPI.get_exchange_rate()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "usdCny": "7.162"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
usdCny | String | Exchange rate

---

# 获取法币汇率

该接口提供的是2周的平均汇率数据

#### 限速：1次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/exchange-rate`

> 请求示例
    
    
    GET /api/v5/market/exchange-rate
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取法币汇率
    result = marketDataAPI.get_exchange_rate(
    )
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "usdCny": "7.162"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
usdCny | String | 人民币兑美元汇率