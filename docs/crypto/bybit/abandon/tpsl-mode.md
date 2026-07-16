---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/abandon/tpsl-mode
api_type: REST
updated_at: 2026-07-16 18:48:44.088599
---

# Get Borrow History

Get interest records, sorted in reverse order of creation time.

### HTTP Request

GET`/v5/account/borrow-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| `USDC`,`USDT`,`BTC`,`ETH` etc, uppercase only  
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
list| array| Object  
> currency| string| `USDC`,`USDT`,`BTC`,`ETH`  
> createdTime| integer| Created timestamp (ms)  
> borrowCost| string| Interest  
> hourlyBorrowRate| string| Hourly Borrow Rate  
> InterestBearingBorrowSize| string| Interest Bearing Borrow Size  
> costExemption| string| Cost exemption  
> borrowAmount| string| Total borrow amount  
> unrealisedLoss| string| Unrealised loss  
> freeBorrowedAmount| string| The borrowed amount for interest free  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/account/borrow-history)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/borrow-history?currency=BTC&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672277745427  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrow_history(  
        currency="BTC",  
        limit=1,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getBorrowHistory({  
        currency: 'USDT',  
        startTime: 1670601600000,  
        endTime: 1673203200000,  
        limit: 30,  
        cursor: 'nextPageCursorToken',  
      })  
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
            "nextPageCursor": "2671153%3A1%2C2671153%3A1",  
            "list": [  
                {  
                    "borrowAmount": "1.06333265702840778",  
                    "costExemption": "0",  
                    "freeBorrowedAmount": "0",  
                    "createdTime": 1697439900204,  
                    "InterestBearingBorrowSize": "1.06333265702840778",  
                    "currency": "BTC",  
                    "unrealisedLoss": "0",  
                    "hourlyBorrowRate": "0.000001216904",  
                    "borrowCost": "0.00000129"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1697442206478  
    }

---

# 查詢利息記錄

獲取利息記錄，按照創建時間倒敘排列

### HTTP 請求

GET`/v5/account/borrow-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| USDC、USDT、BTC、ETH  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近30天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 30天
  * 若只傳startTime，則查詢startTime和startTime+30天的數據
  * 若只傳endTime，則查詢endTime-30天和endTime的數據

  
endTime| false| integer| 結束時間 (毫秒)  
limit| false| integer| 每頁數量, 最大50. 默認每頁20條  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> currency| string| USDC、USDT、BTC、ETH  
> createdTime| integer| 時間戳（毫秒）  
> borrowCost| string| 利息  
> hourlyBorrowRate| string| 利率  
> InterestBearingBorrowSize| string| 豁免利息額度  
> costExemption| string| 豁免計息成本  
> borrowAmount| string| 當前總借貸  
> unrealisedLoss| string| 浮動虧損  
> freeBorrowedAmount| string| 借款中免息的數額  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/account/borrow-history)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/borrow-history?currency=BTC&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672277745427  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_borrow_history(  
        currency="BTC",  
        limit=1,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getBorrowHistory({  
        currency: 'USDT',   
        startTime: 1670601600000,   
        endTime: 1673203200000,   
        limit: 30,   
        cursor: 'nextPageCursorToken',   
      })  
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
            "nextPageCursor": "2671153%3A1%2C2671153%3A1",  
            "list": [  
                {  
                    "borrowAmount": "1.06333265702840778",  
                    "costExemption": "0",  
                    "freeBorrowedAmount": "0",  
                    "createdTime": 1697439900204,  
                    "InterestBearingBorrowSize": "1.06333265702840778",  
                    "currency": "BTC",  
                    "unrealisedLoss": "0",  
                    "hourlyBorrowRate": "0.000001216904",  
                    "borrowCost": "0.00000129"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1697442206478  
    }