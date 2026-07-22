---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-rest-api-get-ticker-public
anchor_id: spread-trading-rest-api-get-ticker-public
api_type: REST
updated_at: 2026-07-22 19:20:17.582768
---

# Get ticker (Public)

Retrieve the latest price snapshot, best bid/ask price and quantity.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/sprd-ticker`

> Request Example
    
    
    GET /api/v5/market/sprd-ticker?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USDT-SWAP  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "last": "14.5",
                "lastSz": "0.5",
                "askPx": "8.5",
                "askSz": "12.0",
                "bidPx": "0.5",
                "bidSz": "12.0",
                "open24h": "4",
                "high24h": "14.5",
                "low24h": "-2.2",
                "vol24h": "6.67",
                "ts": "1715331406485"
            }
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
last | String | Last traded price  
lastSz | String | Last traded size  
askPx | String | Best ask price  
askSz | String | Best ask size  
bidPx | String | Best bid price  
bidSz | String | Best bid size  
open24h | String | Open price in the past 24 hours  
high24h | String | Highest price in the past 24 hours  
low24h | String | Lowest price in the past 24 hours  
vol24h | String | 24h trading volume  
The unit is USD for inverse spreads, and the corresponding baseCcy for linear and hybrid spreads.  
ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. 1597026383085.

---

# 获取单个Spread产品行情信息（公共）

获取单个Spread产品行情信息，包括最新成交价，买一卖一价及数量。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/sprd-ticker`

> 请求示例
    
    
    GET /api/v5/market/sprd-ticker?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 是 | spread ID, 如 BTC-USDT_BTC-USDT-SWAP  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "last": "14.5",
                "lastSz": "0.5",
                "askPx": "8.5",
                "askSz": "12.0",
                "bidPx": "0.5",
                "bidSz": "12.0",
                "open24h": "4",
                "high24h": "14.5",
                "low24h": "-2.2",
                "vol24h": "6.67",
                "ts": "1715331406485"
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | spread ID  
last | String | 最新成交价  
lastSz | String | 最新成交的数量  
askPx | String | 卖一价  
askSz | String | 卖一价对应的数量  
bidPx | String | 买一价  
bidSz | String | 买一价对应的数量  
open24h | String | 24小时开盘价  
high24h | String | 24小时最高价  
low24h | String | 24小时最低价  
vol24h | String | 24小时交易量  
正向及混合价差，单位为交易货币；反向价差，单位为美元  
ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 1597026383085