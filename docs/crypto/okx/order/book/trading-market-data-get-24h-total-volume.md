---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-24h-total-volume
anchor_id: order-book-trading-market-data-get-24h-total-volume
api_type: API
updated_at: 2026-07-02 19:43:58.324262
---

# GET / 24H total volume

The 24-hour trading volume is calculated on a rolling basis.  
  
#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/platform-24-volume`

> Request Example
    
    
    GET /api/v5/market/platform-24-volume
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve 24 total volume
    result = marketDataAPI.get_volume()
    print(result)
    

> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
             "volCny": "230900886396766",
             "volUsd": "34462818865189",
             "ts": "1657856040389"
         }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
volUsd | String | 24-hour total trading volume from the order book trading in "USD"  
volCny | String | 24-hour total trading volume from the order book trading in "CNY"  
ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# GET / 获取平台24小时总成交量

24小时成交量滚动计算  
  
#### 限速：2次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/platform-24-volume`

> 请求示例
    
    
    GET /api/v5/market/platform-24-volume
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取平台24小时总成交量
    result = marketDataAPI.get_volume()
    print(result)
    

> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
             "volCny": "230900886396766",
             "volUsd": "34462818865189",
             "ts": "1657856040389"
         }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
volUsd | String | 订单簿交易近24小时总成交量，以美元为单位  
volCny | String | 订单簿交易近24小时总成交量，以人民币为单位  
ts | String | 接口返回数据时间