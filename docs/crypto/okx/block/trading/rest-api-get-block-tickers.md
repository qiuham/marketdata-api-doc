---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-get-block-tickers
anchor_id: block-trading-rest-api-get-block-tickers
api_type: REST
updated_at: 2026-07-01 19:54:47.121507
---

# Get block tickers

Retrieve the latest block trading volume in the last 24 hours.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/block-tickers`

> Request Example
    
    
    GET /api/v5/market/block-tickers?instType=SWAP
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the latest block trading volume in the last 24 hours
    result = marketDataAPI.get_block_tickers(
        instType="SPOT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instType | String | Yes | Instrument type  
`SPOT`  
`SWAP`  
`FUTURES`  
`OPTION`  
instFamily | String | No | Instrument family, e.g. `BTC-USD`  
Applicable to `FUTURES`/`SWAP`/`OPTION`  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
            "instType":"SWAP",
            "instId":"LTC-USD-SWAP",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "ts":"1597026383085"
         },
         {
            "instType":"SWAP",
            "instId":"BTC-USD-SWAP",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "ts":"1597026383085"
        }
      ]
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
instId | String | Instrument ID  
instType | String | Instrument type  
volCcy24h | String | 24h trading volume, with a unit of `currency`.   
If it is a `derivatives` contract, the value is the number of base currency.   
If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency.  
vol24h | String | 24h trading volume, with a unit of `contract`.   
If it is a `derivatives` contract, the value is the number of contracts.   
If it is `SPOT`/`MARGIN`, the value is the quantity in base currency.  
ts | String | Block ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 获取大宗交易所有产品行情信息

获取最近24小时大宗交易量

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/block-tickers`

> 请求示例
    
    
    GET /api/v5/market/block-tickers?instType=SWAP
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取大宗交易所有产品行情信息
    result = marketDataAPI.get_block_tickers(
        instType="SPOT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instType | String | 是 | 产品类型  
`SPOT`：币币  
`SWAP`：永续合约  
`FUTURES`：交割合约  
`OPTION`：期权  
instFamily | String | 否 | 交易品种  
适用于`交割`/`永续`/`期权`，如 `BTC-USD`  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         {
            "instType":"SWAP",
            "instId":"LTC-USD-SWAP",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "ts":"1597026383085"
         },
         {
            "instType":"SWAP",
            "instId":"BTC-USD-SWAP",
            "volCcy24h":"2222",
            "vol24h":"2222",
            "ts":"1597026383085"
        }
      ]
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
instId | String | 产品ID  
instType | String | 产品类型  
volCcy24h | String | 24小时成交量，以`币`为单位  
如果是`衍生品`合约，数值为交易货币的数量。  
如果是`币币/币币杠杆`，数值为计价货币的数量。  
vol24h | String | 24小时成交量，以`张`为单位  
如果是`衍生品`合约，数值为合约的张数。  
如果是`币币/币币杠杆`，数值为交易货币的数量。  
ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`