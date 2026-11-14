---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/transfer/unitransfer-list
api_type: REST
updated_at: 2026-11-13 19:21:53.290287
---

# Get Universal Transfer Records

Query universal transfer records

tip

  * Main acct api key or Sub acct api key are both supported
  * Main acct api key needs "SubMemberTransfer" permission
  * Sub acct api key needs "SubMemberTransferList" permission



info

  * If startTime and endTime are not provided, the API returns data from the past 7 days by default.
  * If only startTime is provided, the API returns records from startTime to startTime + 7 days.
  * If only endTime is provided, the API returns records from endTime - 7 days to endTime.
  * If both are provided, the maximum allowed range is 7 days (endTime - startTime ≤ 7 days).



### HTTP Request

GET`/v5/asset/transfer/query-universal-transfer-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
transferId| false| string| UUID. Use the one you generated in [createTransfer](/docs/v5/asset/transfer/create-inter-transfer#response-parameters)  
coin| false| string| Coin, uppercase only  
[status](/docs/v5/enum#transferstatus)| false| string| Transfer status. `SUCCESS`,`FAILED`,`PENDING`  
startTime| false| integer| The start timestamp (ms) _Note: the query logic is actually effective based on**second** level_  
endTime| false| integer| The end timestamp (ms) _Note: the query logic is actually effective based on**second** level_  
fromMemberId| false| string| From UID  
toMemberId| false| string| To UID  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> transferId| string| Transfer ID  
> coin| string| Transferred coin  
> amount| string| Transferred amount  
> fromMemberId| string| From UID  
> toMemberId| string| To UID  
> withdrawReqId| string| Deduction req ID (internal use), can be used to map the `id` in [Get Transaction Log](/docs/v5/account/transaction-log)  
> depositReqId| string| Credit req ID (internal use), can be used to map the `id` in [Get Transaction Log](/docs/v5/account/transaction-log)  
> fromAccountType| string| From account type  
> toAccountType| string| To account type  
> timestamp| string| Transfer created timestamp (ms)  
> [status](/docs/v5/enum#transferstatus)| string| Transfer status  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/asset/unitransfer-list)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/query-universal-transfer-list?limit=1&cursor=eyJtaW5JRCI6MTc5NjU3OCwibWF4SUQiOjE3OTY1Nzh9 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672190762800  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_universal_transfer_records(  
        limit=1,  
        cursor="eyJtaW5JRCI6MTc5NjU3OCwibWF4SUQiOjE3OTY1Nzh9",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getUniversalTransferRecords({  
        limit: 1,  
        cursor: 'eyJtaW5JRCI6MTc5NjU3OCwibWF4SUQiOjE3OTY1Nzh9',  
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
                    "transferId": "30effa41-501f-4020-acd8-e57d9f81e23d",  
                    "coin": "USDC",  
                    "amount": "1000",  
                    "timestamp": "1672134373000",  
                    "status": "SUCCESS",  
                    "fromAccountType": "UNIFIED",  
                    "toAccountType": "UNIFIED",  
                    "fromMemberId": "533285",  
                    "toMemberId": "592324",  
                    "withdrawReqId": "30effa41-501f-4020-acd8-e57d9f81e23d",  
                    "depositReqId": "c1fb8ebe-e309-472c-8485-c1b78f2048bb"  
                }  
            ],  
            "nextPageCursor": "eyJtaW5JRCI6MTc4OTYwNSwibWF4SUQiOjE3ODk2MDV9"  
        },  
        "retExtInfo": {},  
        "time": 1672190763079  
    }

---

# 查詢萬能劃轉紀錄

提示

  * 母子帳號的api key都支持調用
  * 母帳號的api key需擁有"母子帳戶劃轉"(SubMemberTransfer)權限
  * 子帳號的api key需擁有"母子帳戶劃轉"(SubMemberTransferList)權限



信息

  * 如果startTime 和 endTime都沒有傳, API僅返回過去7天的數據.
  * 如果僅傳startTime, API按照 startTime 到 startTime + 7天 來返回數據.
  * 如果僅傳endTime, API按照 endTime - 7天 到 endTime 來返回數據.
  * 如果都傳, 最大間隔允許7天(endTime - startTime ≤ 7 天).



### HTTP 請求

GET`/v5/asset/transfer/query-universal-transfer-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
transferId| false| string| UUID. 使用創建萬能劃轉時的UUID  
coin| false| string| 幣種  
[status](/docs/zh-TW/v5/enum#transferstatus)| false| string| 劃轉狀態. `SUCCESS`,`FAILED`,`PENDING`  
startTime| false| integer| 開始時間戳 (毫秒) _注意: 實際查詢時是秒級維度生效_  
endTime| false| integer| 結束時間戳 (毫秒) _注意: 實際查詢時是秒級維度生效_  
fromMemberId| false| string| 劃出UID  
toMemberId| false| string| 劃入UID  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> transferId| string| 劃轉Id  
> coin| string| 劃轉幣種  
> amount| string| 劃轉金額  
> fromMemberId| string| 劃出UID  
> toMemberId| string| 劃入UID  
> withdrawReqId| string| 扣錢流水id（內部使用）， 可以用於跟[查詢交易日誌](/docs/zh-TW/v5/account/transaction-log)裡的`id`做映射  
> depositReqId| string| 加錢流水id（內部使用）， 可以用於跟[查詢交易日誌](/docs/zh-TW/v5/account/transaction-log)裡的`id`做映射  
> fromAccountType| string| 劃出賬戶類型  
> toAccountType| string| 劃入賬戶類型  
> timestamp| string| 劃轉創建時間戳 (毫秒)  
> [status](/docs/zh-TW/v5/enum#transferstatus)| string| 劃轉狀態  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/asset/unitransfer-list)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/query-universal-transfer-list?limit=1&cursor=eyJtaW5JRCI6MTc5NjU3OCwibWF4SUQiOjE3OTY1Nzh9 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672190762800  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_universal_transfer_records(  
        limit=1,  
        cursor="eyJtaW5JRCI6MTc5NjU3OCwibWF4SUQiOjE3OTY1Nzh9",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getUniversalTransferRecords({  
        limit: 1,  
        cursor: 'eyJtaW5JRCI6MTc5NjU3OCwibWF4SUQiOjE3OTY1Nzh9',  
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
                    "transferId": "30effa41-501f-4020-acd8-e57d9f81e23d",  
                    "coin": "USDC",  
                    "amount": "1000",  
                    "timestamp": "1672134373000",  
                    "status": "SUCCESS",  
                    "fromAccountType": "UNIFIED",  
                    "toAccountType": "UNIFIED",  
                    "fromMemberId": "533285",  
                    "toMemberId": "592324",  
                    "withdrawReqId": "30effa41-501f-4020-acd8-e57d9f81e23d",  
                    "depositReqId": "c1fb8ebe-e309-472c-8485-c1b78f2048bb"  
                }  
            ],  
            "nextPageCursor": "eyJtaW5JRCI6MTc4OTYwNSwibWF4SUQiOjE3ODk2MDV9"  
        },  
        "retExtInfo": {},  
        "time": 1672190763079  
    }