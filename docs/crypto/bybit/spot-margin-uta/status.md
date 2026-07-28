---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/status
api_type: REST
updated_at: 2026-07-28 19:04:34.872037
---

# Get Instruments Info

Query for the instrument specification of spread combinations.

info

  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/spread/instrument`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| false| string| Spread combination symbol name  
baseCoin| false| string| Base coin, uppercase only  
limit| false| integer| Limit for data size per page. [`1`, `500`]. Default: `200`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array<object>| instrument info  
> symbol| string| Spread combination symbol name  
> contractType| string| Product type 

  * `FundingRateArb`: perpetual & spot combination
  * `CarryTrade`: futures & spot combination
  * `FutureSpread`: different expiry futures combination
  * `PerpBasis`: futures & perpetual

  
> status| string| Spread status. `Trading`, `Settling`  
> baseCoin| string| Base coin  
> quoteCoin| string| Quote coin  
> settleCoin| string| Settle coin  
> tickSize| string| The step to increase/reduce order price  
> minPrice| string| Min. order price  
> maxPrice| string| Max. order price  
> lotSize| string| Order qty precision  
> minSize| string| Min. order qty  
> maxSize| string| Max. order qty  
> launchTime| string| Launch timestamp (ms)  
> deliveryTime| string| Delivery timestamp (ms)  
> legs| array<object>| Legs information  
>> symbol| string| Legs symbol name  
>> contractType| string| Legs contract type. `LinearPerpetual`, `LinearFutures`, `Spot`  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/spread/instrument?limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spread_get_instruments_info(  
        limit=1  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "contractType": "FundingRateArb",  
                    "status": "Trading",  
                    "baseCoin": "SOL",  
                    "quoteCoin": "USDT",  
                    "settleCoin": "USDT",  
                    "tickSize": "0.0001",  
                    "minPrice": "-1999.9998",  
                    "maxPrice": "1999.9998",  
                    "lotSize": "0.1",  
                    "minSize": "0.1",  
                    "maxSize": "50000",  
                    "launchTime": "1743675300000",  
                    "deliveryTime": "0",  
                    "legs": [  
                        {  
                            "symbol": "SOLUSDT",  
                            "contractType": "LinearPerpetual"  
                        },  
                        {  
                            "symbol": "SOLUSDT",  
                            "contractType": "Spot"  
                        }  
                    ]  
                }  
            ],  
            "nextPageCursor": "first%3D100008%26last%3D100008"  
        },  
        "retExtInfo": {},  
        "time": 1744076802479  
    }

---

# 查詢價差產品的規格信息

警告

  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP請求

GET`/v5/spread/instrument`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| false| string| 價差產品名稱  
baseCoin| false| string| 交易幣種  
limit| false| integer| 每頁數量限制. [`1`, `500`]. 默認: `200`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array<object>| 規格信息  
> symbol| string| 價差產品名稱  
> contractType| string| 價差分類 

  * `FundingRateArb`: 永續 & 現貨組合
  * `CarryTrade`: 到期合約& 現貨組合
  * `FutureSpread`: 不同到期日合約組合
  * `PerpBasis`: 到期合約& 永續組合

  
> status| string| 價差產品交易狀態, `Trading`, `Settling`  
> baseCoin| string| 交易幣種  
> quoteCoin| string| 報價幣種  
> settleCoin| string| 結算幣種  
> tickSize| string| 修改價格的步長  
> minPrice| string| 訂單最小價格  
> maxPrice| string| 訂單最大價格  
> lotSize| string| 訂單數量精度  
> minSize| string| 單筆訂單最小下單量  
> maxSize| string| 單筆訂單最大下單量  
> launchTime| string| 發佈時間 (ms)  
> deliveryTime| string| 交割時間 (ms)  
> legs| array<object>| 單腿信息  
>> symbol| string| 單腿合約名稱  
>> contractType| string| 單腿合約類型, `LinearPerpetual`: 永續合約, `LinearFutures`: 交割合約, `Spot`: 現貨  
nextPageCursor| string| 游標，用於翻頁  
  
### 請求示例
    
    
    GET /v5/spread/instrument?limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "contractType": "FundingRateArb",  
                    "status": "Trading",  
                    "baseCoin": "SOL",  
                    "quoteCoin": "USDT",  
                    "settleCoin": "USDT",  
                    "tickSize": "0.0001",  
                    "minPrice": "-1999.9998",  
                    "maxPrice": "1999.9998",  
                    "lotSize": "0.1",  
                    "minSize": "0.1",  
                    "maxSize": "50000",  
                    "launchTime": "1743675300000",  
                    "deliveryTime": "0",  
                    "legs": [  
                        {  
                            "symbol": "SOLUSDT",  
                            "contractType": "LinearPerpetual"  
                        },  
                        {  
                            "symbol": "SOLUSDT",  
                            "contractType": "Spot"  
                        }  
                    ]  
                }  
            ],  
            "nextPageCursor": "first%3D100008%26last%3D100008"  
        },  
        "retExtInfo": {},  
        "time": 1744076802479  
    }