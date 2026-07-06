---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#block-trading-rest-api-get-block-ticker
anchor_id: block-trading-rest-api-get-block-ticker
api_type: REST
updated_at: 2026-07-06 19:53:41.650280
---

# Get block ticker

Retrieve the latest block trading volume in the last 24 hours.  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/block-ticker`

> Request Example
    
    
    GET /api/v5/market/block-ticker?instId=LTC-USD-SWAP
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Retrieve the latest block trading volume in the last 24 hours
    result = marketDataAPI.get_block_ticker(
        instId="BTC-USDT"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP`  
  
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

# 获取大宗交易单个产品行情信息

获取最近24小时大宗交易量  
  
#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/block-ticker`

> 请求示例
    
    
    GET /api/v5/market/block-ticker?instId=BTC-USD-SWAP
    
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取大宗交易单个产品行情信息
    result = marketDataAPI.get_block_ticker(
        instId="BTC-USDT"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
instId | String | 是 | 产品ID，如 `BTC-USD-SWAP`  
  
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