---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#public-data-rest-api-get-index-components
anchor_id: public-data-rest-api-get-index-components
api_type: REST
updated_at: 2026-07-06 19:54:09.781587
---

# Get index components

Get the index component information data on the market  
  
#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/index-components`

> Request Example
    
    
    GET /api/v5/market/index-components?index=BTC-USD
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # Get the index component information data on the market
    result = marketDataAPI.get_index_components(
        index="BTC-USD"
    )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
index | String | Yes | index, e.g `BTC-USDT`  
Same as `uly`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "components": [
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52733.2",
                    "wgt": "0.25",
                    "cnvPx": "52733.2",
                    "exch": "OKX"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52739.87000000",
                    "wgt": "0.25",
                    "cnvPx": "52739.87000000",
                    "exch": "Binance"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52729.1",
                    "wgt": "0.25",
                    "cnvPx": "52729.1",
                    "exch": "Huobi"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52739.47929397",
                    "wgt": "0.25",
                    "cnvPx": "52739.47929397",
                    "exch": "Poloniex"
                }
            ],
            "last": "52735.4123234925",
            "index": "BTC-USDT",
            "ts": "1630985335599"
        }
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
index | String | Index  
last | String | Latest Index Price  
ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
components | Array of objects | Components  
> exch | String | Name of Exchange  
> symbol | String | Name of Exchange Trading Pairs  
> symPx | String | Price of Exchange Trading Pairs  
> wgt | String | Weights  
> cnvPx | String | Price converted to index

---

# 获取指数成分数据

查询市场上的指数成分信息数据  
  
#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/index-components`

> 请求示例
    
    
    GET /api/v5/market/index-components?index=BTC-USD
    
    
    
    import okx.MarketData as MarketData
    
    flag = "0"  # 实盘:0 , 模拟盘：1
    
    marketDataAPI =  MarketData.MarketAPI(flag=flag)
    
    # 获取指数成分数据
    result = marketDataAPI.get_index_components(
        index="BTC-USD"
    )
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
index | String | 是 | 指数，如 `BTC-USDT`  
与 `uly` 含义相同。  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": {
            "components": [
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52733.2",
                    "wgt": "0.25",
                    "cnvPx": "52733.2",
                    "exch": "OKEx"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52739.87000000",
                    "wgt": "0.25",
                    "cnvPx": "52739.87000000",
                    "exch": "Binance"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52729.1",
                    "wgt": "0.25",
                    "cnvPx": "52729.1",
                    "exch": "Huobi"
                },
                {
                    "symbol": "BTC/USDT",
                    "symPx": "52739.47929397",
                    "wgt": "0.25",
                    "cnvPx": "52739.47929397",
                    "exch": "Poloniex"
                }
            ],
            "last": "52735.4123234925",
            "index": "BTC-USDT",
            "ts": "1630985335599"
        }
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
index | String | 指数名称  
last | String | 最新指数价格  
ts | String | 数据产生时间，Unix时间戳的毫秒数格式， 如`1597026383085`  
components | String | 成分  
> exch | String | 交易所名称  
> symbol | String | 采集的币对名称  
> symPx | String | 采集的币对价格  
> wgt | String | 权重  
> cnvPx | String | 换算成指数后的价格