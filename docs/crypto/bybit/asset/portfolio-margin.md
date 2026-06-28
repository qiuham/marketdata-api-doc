---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/portfolio-margin
api_type: REST
updated_at: 2026-05-27 19:15:19.143017
---

# Get USDC Session Settlement

Query session settlement records of USDC perpetual and futures

info

  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/asset/settlement-record`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`(USDC contract)  
symbol| false| string| Symbol name, like `BTCPERP`, uppercase only  
startTime| false| integer| The start timestamp (ms) 

  * startTime and endTime are not passed, return 30 days by default
  * Only startTime is passed, return range between startTime and startTime + 30 days 
  * Only endTime is passed, return range between endTime-30 days and endTime
  * If both are passed, the rule is endTime - startTime <= 30 days

  
endTime| false| integer| The end time. timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> symbol| string| Symbol name  
> side| string| `Buy`,`Sell`  
> size| string| Position size  
> sessionAvgPrice| string| Settlement price  
> markPrice| string| Mark price  
> realisedPnl| string| Realised PnL  
> createdTime| string| Created time (ms)  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/asset/settlement)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/settlement-record?category=linear HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672284883483  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_usdc_contract_settlement(  
        category="linear",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSettlementRecords({ category: 'linear' })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "116952%3A1%2C116952%3A1",  
            "category": "linear",  
            "list": [  
                {  
                    "realisedPnl": "-71.28",  
                    "symbol": "BTCPERP",  
                    "side": "Buy",  
                    "markPrice": "16620",  
                    "size": "1.5",  
                    "createdTime": "1672214400000",  
                    "sessionAvgPrice": "16620"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672284884285  
    }

---

# 查詢USDC合約結算紀錄

查詢USDC合約的結算紀錄

信息

  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP 請求

GET`/v5/asset/settlement-record`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `linear`  
symbol| false| string| 合約名稱  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近30天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 30天
  * 若只傳startTime，則查詢startTime和startTime+30天的數據
  * 若只傳endTime，則查詢endTime-30天和endTime的數據

  
endTime| false| integer| 結束時間 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱  
> side| string| `Buy`,`Sell`  
> size| string| 倉位大小  
> sessionAvgPrice| string| 結算價格  
> markPrice| string| 標記價格  
> realisedPnl| string| 已實現盈虧  
> createdTime| string| 結算時間 (毫秒)  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/asset/settlement)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/settlement-record?category=linear HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672284883483  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_usdc_contract_settlement(  
        category="linear",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getSettlementRecords({ category: 'linear' })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "nextPageCursor": "116952%3A1%2C116952%3A1",  
            "category": "linear",  
            "list": [  
                {  
                    "realisedPnl": "-71.28",  
                    "symbol": "BTCPERP",  
                    "side": "Buy",  
                    "markPrice": "16620",  
                    "size": "1.5",  
                    "createdTime": "1672214400000",  
                    "sessionAvgPrice": "16620"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672284884285  
    }