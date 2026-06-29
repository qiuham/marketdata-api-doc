---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/deposit/internal-deposit-record
api_type: REST
updated_at: 2026-06-29 19:25:46.526834
---

# Get Internal Deposit Records (off-chain)

Query deposit records within the Bybit platform. These transactions are not on the blockchain.

Rules

  * The maximum difference between the start time and the end time is 30 days
  * Support to get deposit records by Master or Sub Member Api Key



### HTTP Request

GET`/v5/asset/deposit/query-internal-record`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
txID| false| string| Internal transfer transaction ID  
startTime| false| integer| Start time (ms). Default value: 30 days before the current time  
endTime| false| integer| End time (ms). Default value: current time  
coin| false| string| Coin name: for example, BTC. Default value: all  
cursor| false| string| Cursor, used for pagination  
limit| false| integer| Number of items per page, [`1`, `50`]. Default value: 50  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
rows| array| Object  
> id| string| ID  
> type| integer| `1`: Internal deposit  
> coin| string| Deposit coin  
> amount| string| Deposit amount  
> status| integer| 

  * 1=Processing
  * 2=Success
  * 3=deposit failed

  
> address| string| Email address or phone number  
> createdTime| string| Deposit created timestamp  
> fromMemberId| string| Sender UID  
> txID| string| Internal transfer transaction ID  
> taxDepositRecordsId| string| This field is used for tax purposes by Bybit EU (Austria) users, declare tax id  
> taxStatus| integer| This field is used for tax purposes by Bybit EU (Austria) users 

  * 0: No reporting required
  * 1: Reporting pending
  * 2: Reporting completed

  
nextPageCursor| string| cursor information: used for pagination. Default value: `""`  
[](/docs/api-explorer/v5/asset/internal-deposit-record)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/deposit/query-internal-record HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682099024473  
    X-BAPI-RECV-WINDOW: 50000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_internal_deposit_records(  
        startTime=1667260800000,  
        endTime=1667347200000,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInternalDepositRecords({  
        startTime: 1667260800000,  
        endTime: 1667347200000,  
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
            "rows": [  
                {  
                    "id": "1103",  
                    "amount": "0.1",  
                    "type": 1,  
                    "coin": "ETH",  
                    "address": "xxxx***@gmail.com",  
                    "status": 2,  
                    "createdTime": "1705393280",  
                    "fromMemberId": "118027304",  
                    "txID": "77c37e5c-d9fa-41e5-bd13-c9b59d95"，  
                    "taxDepositRecordsId": "0",  
                    "taxStatus": 0,  
                }  
            ],  
            "nextPageCursor": "eyJtaW5JRCI6MTEwMywibWF4SUQiOjExMDN9"  
        },  
        "retExtInfo": {},  
        "time": 1705395632689  
    }

---

# 查詢充值記錄 (平台转账)

查詢Bybit平台內部充值紀錄

規則

  * 開始時間和截止時間差最大限制為30天
  * 支持使用母、子帳戶的api key查詢各自的入金紀錄



### HTTP 請求

GET`/v5/asset/deposit/query-internal-record`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
txID| false| string| 內部轉帳交易ID  
startTime| false| integer| 開始時間 (精確到毫秒)。 默認為當前時間之前30天  
endTime| false| integer| 結束時間 (精確到毫秒)。 默認為當前時間  
coin| false| string| 幣種名：舉例，BTC。默認全部  
cursor| false| string| 游標信息：用來分頁。 默認空  
limit| false| integer| 每頁條數, [`1`, `50`] 默認為50  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
rows| array| Object  
> id| string| ID  
> type| integer| `1`: 內部充值  
> coin| string| 充值的幣種  
> amount| string| 充值的數量  
> txID| string| 交易ID。充值失敗/取消充值：為空  
> status| integer| 

  * 1=處理中
  * 2=已完成
  * 3=充值失敗

  
> address| string| 郵箱地址或者手機號  
> fromMemberId| string| 來源UID  
> createdTime| string| 充值創建時間戳  
txID| string| 內部轉帳交易ID  
> taxDepositRecordsId| string| Bybit EU（奧地利）用戶用於稅務目的, 保稅記錄id  
> taxStatus| integer| Bybit EU（奧地利）用戶用於稅務目的 

  * 0: No reporting required
  * 1: Reporting pending
  * 2: Reporting completed

  
nextPageCursor| string| 游標信息：用來分頁  
[](/docs/zh-TW/api-explorer/v5/asset/internal-deposit-record)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/deposit/query-internal-record HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682099024473  
    X-BAPI-RECV-WINDOW: 50000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_internal_deposit_records(  
        startTime=1667260800000,  
        endTime=1667347200000,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInternalDepositRecords({  
        startTime: 1667260800000,  
        endTime: 1667347200000,  
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
            "rows": [  
                {  
                    "id": "1103",  
                    "amount": "0.1",  
                    "type": 1,  
                    "coin": "ETH",  
                    "address": "xxxx***@gmail.com",  
                    "status": 2,  
                    "createdTime": "1705393280",  
                    "txID": "77c37e5c-d9fa-41e5-bd13-c9b59d95"，  
                    "taxDepositRecordsId": "0",  
                    "taxStatus": 0,  
                }  
            ],  
            "nextPageCursor": "eyJtaW5JRCI6MTEwMywibWF4SUQiOjExMDN9"  
        },  
        "retExtInfo": {},  
        "time": 1705395632689  
    }