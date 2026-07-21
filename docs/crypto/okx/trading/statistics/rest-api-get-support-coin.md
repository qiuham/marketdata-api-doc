---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#trading-statistics-rest-api-get-support-coin
anchor_id: trading-statistics-rest-api-get-support-coin
api_type: REST
updated_at: 2026-07-21 19:27:11.172692
---

# Get support coin

Retrieve the currencies supported by the trading statistics endpoints.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/trading-data/support-coin`

> Request Example
    
    
    GET /api/v5/rubik/stat/trading-data/support-coin
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # Retrieve the currencies supported by the trading statistics endpoints
    result = tradingDataAPI.get_support_coin()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": {
            "contract": [
                "ADA",
                "BTC"
            ],
            "option": [
                "BTC"
            ],
            "spot": [
                "ADA",
                "BTC"
            ]
        },
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
contract | Array of strings | Currency supported by derivatives trading data  
option | Array of strings | Currency supported by option trading data  
spot | Array of strings | Currency supported by spot trading data

---

# 获取交易大数据支持币种

获取支持交易大数据的币种

#### 限速：5次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/rubik/stat/trading-data/support-coin`

> 请求示例
    
    
    GET /api/v5/rubik/stat/trading-data/support-coin
    
    
    
    import okx.TradingData as TradingData_api
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)
    
    # 获取交易大数据支持币种
    result = tradingDataAPI.get_support_coin()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": {
            "contract": [
                "ADA",
                "BTC",
            ],
            "option": [
                "BTC"
            ],
            "spot": [
                "ADA",
                "BTC",
            ]
        },
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
contract | Array of strings | 合约交易大数据接口功能支持的币种  
option | Array of strings | 期权交易大数据接口功能支持的币种  
spot | Array of strings | 现货交易大数据接口功能支持的币种