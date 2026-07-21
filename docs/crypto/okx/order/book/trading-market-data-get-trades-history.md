---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-trades-history
anchor_id: order-book-trading-market-data-get-trades-history
api_type: API
updated_at: 2026-07-21 19:26:22.537263
---

# GET / Trades history

Retrieve the recent transactions of an instrument from the last 3 months with pagination.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/history-trades`

> Request Example
    
    
    GET /api/v5/market/history-trades?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the recent transactions of an instrument from the last 3 months with pagination
    result = marketDataAPI.get_history_trades(
        instId="BTC-USD-SWAP"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
type | String | No | Pagination Type   
`1`: tradeId `2`: timestamp  
The default is `1`  
after | String | No | Pagination of data to return records earlier than the requested tradeId or ts.  
before | String | No | Pagination of data to return records newer than the requested tradeId.   
Do not support timestamp for pagination. The latest data will be returned when using `before` individually  
limit | String | No | Number of results per request. The maximum and default both are `100`  
  
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

---

# GET / 获取交易产品公共历史成交数据

查询市场上的成交信息数据，可以分页获取最近3个月的数据。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/history-trades`

> 请求示例
    
    
    GET /api/v5/market/history-trades?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取交易产品公共历史成交数据
    result = marketDataAPI.get_history_trades(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
type | String | 否 | 分页类型  
`1`：tradeId 分页 `2`：时间戳分页  
默认为`1`：tradeId 分页  
after | String | 否 | 请求此 ID 或 ts 之前的分页内容，传的值为对应接口的 tradeId 或 ts  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的 tradeId。  
不支持时间戳分页。单独使用时，会返回最新的数据。  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
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