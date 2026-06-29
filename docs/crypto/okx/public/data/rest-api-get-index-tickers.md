---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-index-tickers
anchor_id: public-data-rest-api-get-index-tickers
api_type: REST
updated_at: 2026-06-29 19:57:19.435088
---

# Get index tickers

Retrieve index tickers.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/index-tickers`

> Request Example
    
    
    GET /api/v5/market/index-tickers?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve index tickers
    result = marketDataAPI.get_index_tickers(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
quoteCcy | String | Conditional | Quote currency   
Currently there is only an index with `USD/USDT/BTC/USDC` as the quote currency.  
instId | String | Conditional | Index, e.g. `BTC-USD`  
Either `quoteCcy` or `instId` is required.   
Same as `uly`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT",
                "idxPx": "43350",
                "high24h": "43649.7",
                "sodUtc0": "43444.1",
                "open24h": "43640.8",
                "low24h": "43261.9",
                "sodUtc8": "43328.7",
                "ts": "1649419644492"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Index  
idxPx | String | Latest index price  
high24h | String | Highest price in the past 24 hours  
low24h | String | Lowest price in the past 24 hours  
open24h | String | Open price in the past 24 hours  
sodUtc0 | String | Open price in the UTC 0  
sodUtc8 | String | Open price in the UTC 8  
ts | String | Index price update time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取指数行情

获取指数行情数据  
  
#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/index-tickers`

> 请求示例
    
    
    GET /api/v5/market/index-tickers?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取指数行情
    result = marketDataAPI.get_index_tickers(
        instId="BTC-USD"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
quoteCcy | String | 可选 | 指数计价单位， 目前只有 `USD/USDT/BTC/USDC`为计价单位的指数，`quoteCcy`和`instId`必须填写一个  
instId | String | 可选 | 指数，如 `BTC-USD`  
与 `uly` 含义相同。  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT",
                "idxPx": "43350",
                "high24h": "43649.7",
                "sodUtc0": "43444.1",
                "open24h": "43640.8",
                "low24h": "43261.9",
                "sodUtc8": "43328.7",
                "ts": "1649419644492"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 指数  
idxPx | String | 最新指数价格  
high24h | String | 24小时指数最高价格  
low24h | String | 24小时指数最低价格  
open24h | String | 24小时指数开盘价格  
sodUtc0 | String | UTC 0 时开盘价  
sodUtc8 | String | UTC+8 时开盘价  
ts | String | 指数价格更新时间，Unix时间戳的毫秒数格式，如`1597026383085`