---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-trades
anchor_id: order-book-trading-market-data-get-trades
api_type: API
updated_at: 2026-06-29 19:56:39.222087
---

# GET / Trades

Retrieve the recent transactions of an instrument.

#### Rate Limit: 100 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/trades`

> Request Example
    
    
    GET /api/v5/market/trades?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the recent transactions of an instrument
    result = marketDataAPI.get_trades(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
limit | String | No | Number of results per request. The maximum is `500`; The default is `100`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29963.2",
                "tradeId": "242720720",
                "ts": "1654161646974"
            },
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29964.1",
                "tradeId": "242720719",
                "ts": "1654161641568"
            }
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
tradeId | String | Trade ID  
px | String | Trade price  
sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
side | String | Trade side of taker   
`buy`   
`sell`  
source | String | Order source  
`0`: normal order  
`1`: Enhanced Liquidity Program order  
ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
Up to 500 most recent historical public transaction data can be retrieved.

---

# GET / 获取交易产品公共成交数据

查询市场上的成交信息数据

#### 限速：100次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/trades`

> 请求示例
    
    
    GET /api/v5/market/trades?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取交易产品公共成交数据
    result = marketDataAPI.get_trades(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
limit | String | 否 | 分页返回的结果集数量，最大为500，不填默认返回100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29963.2",
                "tradeId": "242720720",
                "ts": "1654161646974"
            },
            {
                "instId": "BTC-USDT",
                "side": "sell",
                "sz": "0.00001",
                "source": "0",
                "px": "29964.1",
                "tradeId": "242720719",
                "ts": "1654161641568"
            }
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
tradeId | String | 成交ID  
px | String | 成交价格  
sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
side | String | 吃单方向  
`buy`：买  
`sell`：卖  
source | String | 订单来源  
`0`：普通订单  
`1`：流动性增强计划订单  
ts | String | 成交时间，Unix时间戳的毫秒数格式， 如`1597026383085`  
最多获取最近500条历史公共成交数据