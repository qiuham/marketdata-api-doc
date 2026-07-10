---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-candlesticks-history
anchor_id: order-book-trading-market-data-get-candlesticks-history
api_type: API
updated_at: 2026-07-10 19:31:20.423202
---

# GET / Candlesticks history

Retrieve history candlestick charts from recent years(It is last 3 months supported for 1s candlestick).

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/history-candles`

> Request Example
    
    
    GET /api/v5/market/history-candles?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve history candlestick charts from recent years
    result = marketDataAPI.get_history_candlesticks(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USDT`  
after | String | No | Pagination of data to return records earlier than the requested `ts`  
before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually  
bar | String | No | Bar size, the default is `1m`  
e.g. [1s/1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8 opening price k-line: [6H/12H/1D/2D/3D/1W/1M/3M]  
UTC+0 opening price k-line: [6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]  
limit | String | No | Number of results per request. The maximum is `300`. The default is `100`.  
adjust | String | No | Price adjustment type for equity perpetual contracts.  
`forward`: Forward adjustment.  
If this field is omitted, unadjusted data is returned by default.  
Only applicable to equity perpetual contracts.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         [
            "1597026383085",
            "3.721",
            "3.743",
            "3.677",
            "3.708",
            "8422410",
            "22698348.04828491",
            "12698348.04828491",
            "1"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
            "24912403",
            "67632347.24399722",
            "37632347.24399722",
            "1"
        ]
        ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085`  
o | String | Open price  
h | String | Highest price  
l | String | Lowest price  
c | String | Close price  
vol | String | Trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
volCcy | String | Trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
volCcyQuote | String | Trading volume, the value is the quantity in quote currency  
e.g. The unit is USDT for BTC-USDT and BTC-USDT-SWAP;  
The unit is USD for BTC-USD-SWAP  
confirm | String | The state of candlesticks  
`0`: K line is uncompleted  
`1`: K line is completed  
  
The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,volCcy,volCcyQuote,confirm] 

1s candle is not supported by OPTION, but it is supported by other business lines (SPOT, MARGIN, FUTURES and SWAP)  When `adjust=forward`, the historical OHLC prices are multiplied by the adjustment factor for the relevant period. For stock splits, `vol` and `volCcy` are also adjusted proportionally. `volCcyQuote` is not adjusted. This parameter is only effective for equity perpetual contracts.

---

# GET / 获取交易产品历史K线数据

获取最近几年的历史k线数据(1s k线支持查询最近3个月的数据)

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/history-candles`

> 请求示例
    
    
    GET /api/v5/market/history-candles?instId=BTC-USDT
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取交易产品历史K线数据
    result = marketDataAPI.get_history_candlesticks(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USDT`  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的`ts`  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的`ts`, 单独使用时，会返回最新的数据。  
bar | String | 否 | 时间粒度，默认值`1m`  
如 [1s/1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8开盘价k线：[6H/12H/1D/2D/3D/1W/1M/3M]  
UTC+0开盘价k线：[6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]  
limit | String | 否 | 分页返回的结果集数量，最大为300，不填默认返回100条  
adjust | String | 否 | 复权类型，仅适用于股票永续合约。  
`forward`：前复权。  
不填时默认返回不复权数据。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         [
            "1597026383085",
            "3.721",
            "3.743",
            "3.677",
            "3.708",
            "8422410",
            "22698348.04828491",
            "12698348.04828491",
            "1"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
            "24912403",
            "67632347.24399722",
            "37632347.24399722",
            "1"
        ]
        ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ts | String | 开始时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
o | String | 开盘价格  
h | String | 最高价格  
l | String | 最低价格  
c | String | 收盘价格  
vol | String | 交易量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
volCcy | String | 交易量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
volCcyQuote | String | 交易量，以计价货币为单位  
如 `BTC-USDT`和`BTC-USDT-SWAP`，单位均是`USDT`  
`BTC-USD-SWAP`单位是`USD`  
confirm | String | K线状态  
`0`：K线未完结  
`1`：K线已完结  
返回值数组顺序分别为是：[ts,o,h,l,c,vol,volCcy,volCcyQuote,confirm]  期权不支持 1s K线， 其他业务线 (币币, 杠杆, 交割和永续)支持  当传入 `adjust=forward` 时，历史K线的开高低收（OHLC）价格将乘以对应时期的复权因子。对于拆股，成交量（`vol`、`volCcy`）也会按相同比例调整。成交金额（`volCcyQuote`）不做调整。该参数仅对股票永续合约有效。