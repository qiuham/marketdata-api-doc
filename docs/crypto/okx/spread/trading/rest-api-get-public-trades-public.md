---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-rest-api-get-public-trades-public
anchor_id: spread-trading-rest-api-get-public-trades-public
api_type: REST
updated_at: 2026-07-20 19:36:42.241451
---

# Get public trades (Public)

Retrieve the recent transactions of an instrument (at most 500 records per request). Results are returned in counter chronological order.   
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/sprd/public-trades`

> Request Example
    
    
    GET /api/v5/sprd/public-trades?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get public trades
    result = spreadAPI.get_public_trades(sprdId='ETH-USDT-SWAP_ETH-USDT-230929')
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | No | Spread ID, e.g. BTC-USDT_BTC-USDT-SWAP  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDC-SWAP",
                "side": "sell",
                "sz": "0.1",
                "px": "964.1",
                "tradeId": "242720719",
                "ts": "1654161641568"
            }
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
tradeId | String | Trade ID  
px | String | Trade price  
sz | String | Trade quantity  
side | String | Trade side of the taker.   
`buy`   
`sell`  
ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.

---

# 获取公共成交数据（公共）

查询市场上的Spread成交信息数据，每次请求最多返回500条结果。结果按时间倒序返回。  
  
#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/sprd/public-trades`

> 请求示例
    
    
    GET /api/v5/sprd/public-trades?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取公共交易信息
    result = spreadAPI.get_public_trades(sprdId='ETH-USDT-SWAP_ETH-USDT-230929')
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 否 | Spread ID，例如BTC-USDT_BTC-USDT-SWAP  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDC-SWAP",
                "side": "sell",
                "sz": "0.1",
                "px": "964.1",
                "tradeId": "242720719",
                "ts": "1654161641568"
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | spread ID  
tradeId | String | 交易ID  
px | String | 成交价格  
sz | String | 成交数量  
side | String | Taker的交易方向 `buy`：买 `sell`：卖  
ts | String | 交易时间，Unix时间戳的毫秒数格式， 如 ： `1597026383085`  
最多可以查询到最近500条公共成交信息。