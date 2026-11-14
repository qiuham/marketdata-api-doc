---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/transfer/inter-transfer-list
api_type: REST
updated_at: 2026-11-13 19:21:49.963563
---

# Get Internal Transfer Records

Query the internal transfer records between different [account types](/docs/v5/enum#accounttype) under the same UID.

info

  * If startTime and endTime are not provided, the API returns data from the past 7 days by default.
  * If only startTime is provided, the API returns records from startTime to startTime + 7 days.
  * If only endTime is provided, the API returns records from endTime - 7 days to endTime.
  * If both are provided, the maximum allowed range is 7 days (endTime - startTime ≤ 7 days).



### HTTP Request

GET`/v5/asset/transfer/query-inter-transfer-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
transferId| false| string| UUID. Use the one you generated in [createTransfer](/docs/v5/asset/transfer/create-inter-transfer#response-parameters)  
coin| false| string| Coin, uppercase only  
[status](/docs/v5/enum#transferstatus)| false| string| Transfer status  
startTime| false| integer| The start timestamp (ms) _Note: the query logic is actually effective based on**second** level_  
endTime| false| integer| The end timestamp (ms) _Note: the query logic is actually effective based on**second** level_  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> transferId| string| Transfer ID  
> coin| string| Transferred coin  
> amount| string| Transferred amount  
> [fromAccountType](/docs/v5/enum#accounttype)| string| From account type  
> [toAccountType](/docs/v5/enum#accounttype)| string| To account type  
> timestamp| string| Transfer created timestamp (ms)  
> [status](/docs/v5/enum#transferstatus)| string| Transfer status  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/asset/inter-transfer-list)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/inter-transfer-list-query?coin=USDT&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1670988271299  
    X-BAPI-RECV-WINDOW: 50000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_internal_transfer_records(  
        coin="USDT",  
        limit=1,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInternalTransferRecords({  
        coin: 'USDT',  
        limit: 1,  
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
        "retMsg": "success",  
        "result": {  
        "list": [  
            {  
                "transferId": "selfTransfer_a1091cc7-9364-4b74-8de1-18f02c6f2d5c",  
                "coin": "USDT",  
                "amount": "5000",  
                "fromAccountType": "SPOT",  
                "toAccountType": "UNIFIED",  
                "timestamp": "1667283263000",  
                "status": "SUCCESS"  
            }  
        ],  
        "nextPageCursor": "eyJtaW5JRCI6MTM1ODQ2OCwibWF4SUQiOjEzNTg0Njh9"  
    },  
        "retExtInfo": {},  
        "time": 1670988271677  
    }

---

# 查詢劃轉紀錄 (單帳號內)

獲取單帳號內的劃轉紀錄

信息

  * 如果startTime 和 endTime都沒有傳, API僅返回過去7天的數據.
  * 如果僅傳startTime, API按照 startTime 到 startTime + 7天 來返回數據.
  * 如果僅傳endTime, API按照 endTime - 7天 到 endTime 來返回數據.
  * 如果都傳, 最大間隔允許7天(endTime - startTime ≤ 7 天).



### HTTP 請求

GET`/v5/asset/transfer/query-inter-transfer-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
transferId| false| string| UUID. 使用創建劃轉時用的UUID  
coin| false| string| 幣種  
[status](/docs/zh-TW/v5/enum#transferstatus)| false| string| 劃轉狀態  
startTime| false| integer| 開始時間戳 (毫秒) _注意: 實際查詢時是秒級維度生效_  
endTime| false| integer| 結束時間戳 (毫秒) _注意: 實際查詢時是秒級維度生效_  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> transferId| string| 劃轉Id  
> coin| string| 劃轉幣種  
> amount| string| 劃轉金額  
> [fromAccountType](/docs/zh-TW/v5/enum#accountyype)| string| 劃出賬戶類型  
> [toAccountType](/docs/zh-TW/v5/enum#accountyype)| string| 劃入賬戶類型  
> timestamp| string| 劃轉創建時間戳 (毫秒)  
> [status](/docs/zh-TW/v5/enum#transferstatus)| string| 劃轉狀態  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/asset/inter-transfer-list)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/inter-transfer-list-query?coin=USDT&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1670988271299  
    X-BAPI-RECV-WINDOW: 50000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_internal_transfer_records(  
        coin="USDT",  
        limit=1,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInternalTransferRecords({  
        coin: 'USDT',  
        limit: 1,  
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
        "retMsg": "success",  
        "result": {  
        "list": [  
            {  
                "transferId": "selfTransfer_a1091cc7-9364-4b74-8de1-18f02c6f2d5c",  
                "coin": "USDT",  
                "amount": "5000",  
                "fromAccountType": "SPOT",  
                "toAccountType": "UNIFIED",  
                "timestamp": "1667283263000",  
                "status": "SUCCESS"  
            }  
        ],  
        "nextPageCursor": "eyJtaW5JRCI6MTM1ODQ2OCwibWF4SUQiOjEzNTg0Njh9"  
    },  
        "retExtInfo": {},  
        "time": 1670988271677  
    }