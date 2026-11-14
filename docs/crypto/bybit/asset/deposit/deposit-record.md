---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/deposit/deposit-record
api_type: REST
updated_at: 2026-11-13 19:21:37.590196
---

# Get Deposit Records (on-chain)

Query deposit records

tip

  * `endTime` \- `startTime` should be less than 30 days. Query last 30 days records by default.
  * Support using **main or sub** UID api key to query deposit records respectively.



### HTTP Request

GET`/v5/asset/deposit/query-record`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
id| false| string| Internal ID: Can be used to uniquely identify and filter the deposit. When combined with other parameters, this field takes the highest priority  
txID| false| string| Transaction ID: Please note that data generated before Jan 1, 2024 cannot be queried using txID  
coin| false| string| Coin, uppercase only  
startTime| false| integer| The start timestamp (ms) _Note: the query logic is actually effective based on**second** level_  
endTime| false| integer| The end timestamp (ms) _Note: the query logic is actually effective based on**second** level_  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
rows| array| Object  
> coin| string| Coin  
> chain| string| Chain  
> amount| string| Amount  
> txID| string| Transaction ID  
> [status](/docs/v5/enum#depositstatus)| integer| Deposit status  
> toAddress| string| Deposit target address  
> tag| string| Tag of deposit target address  
> depositFee| string| Deposit fee  
> successAt| string| Deposit's success time  
> confirmations| string| Number of confirmation blocks  
> txIndex| string| Transaction sequence number  
> blockHash| string| Hash number on the chain  
> batchReleaseLimit| string| The deposit limit for this coin in this chain. `"-1"` means no limit  
> depositType| string| The deposit type. `0`: normal deposit, `10`: the deposit reaches daily deposit limit, `20`: hit AML deposit, please go to web to submit materials, `50`: The deposit has been blocked due to an account or compliance restriction, pls go to web to withdraw the funds  
> fromAddress| string| From address of deposit, only shown when the deposit comes from on-chain and from address is unique, otherwise gives `""`  
> taxDepositRecordsId| string| This field is used for tax purposes by Bybit EU (Austria) users, declare tax id  
> taxStatus| integer| This field is used for tax purposes by Bybit EU (Austria) users 

  * 0: No reporting required
  * 1: Reporting pending
  * 2: Reporting completed

  
> id| string| Unique ID  
> requestId| string| Request ID  
> travelRuleStatus| integer| Travel Rule review status, non-compliance area can ignore this field

  * `0`: Approved — review passed, proceed with subsequent flow
  * `1`: CollectInfo — counterparty info required, re-submit questionnaire
  * `2`: Pending — under review, poll the deposit query endpoint
  * `3`: Rejected — rejected or failed (including cancelled)

  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/asset/deposit-record)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/deposit/query-record?coin=USDT&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672191991544  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_deposit_records(  
        coin="USDT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getDepositRecords({  
        coin: 'USDT'  
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
                    "coin": "USDT",  
                    "chain": "TRX",  
                    "amount": "999.0496",  
                    "txID": "04bf3fbad2fc85b107a42cfdc5ff83110092b606ca754efa0f032f8b94b3262e",  
                    "status": 3,  
                    "toAddress": "TDGYpm5zPacnEqKV34TJPuhJhHom9hcXAy",  
                    "tag": "",  
                    "depositFee": "",  
                    "successAt": "1742728163000",  
                    "confirmations": "50",  
                    "txIndex": "0",  
                    "blockHash": "000000000436ab4dabc8a4a87beb2262d2d87f6761a825494c4f1d5ae11b27e8",  
                    "batchReleaseLimit": "-1",  
                    "depositType": "0",  
                    "fromAddress": "TJ7hhYhVhaxNx6BPyq7yFpqZrQULL3JSdb",  
                    "taxDepositRecordsId": "0",  
                    "taxStatus": 0,  
                    "id": "160237231",  
                    "requestId": "d54a802dfc364921a68684389a2c72bd"  
                }  
            ],  
            "nextPageCursor": "eyJtaW5JRCI6MTYwMjM3MjMxLCJtYXhJRCI6MTYwMjM3MjMxfQ=="  
        },  
        "retExtInfo": {},  
        "time": 1750798211884  
    }

---

# 查詢充值紀錄 (鏈上)

提示

  * `endTime` \- `startTime`需要小於等於30天，默認查詢最近30天的紀錄
  * 支持母子帳號的API key查詢各自的充值紀錄



### HTTP 請求

GET`/v5/asset/deposit/query-record`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
id| false| string| 內部ID: 可用於唯一篩選入金紀錄. 當跟其他參數組合時, 具有最高優先級  
txID| false| string| 鏈上交易ID: 請注意2024年1月1日之前的入金紀錄, 無法通過txID來篩選  
coin| false| string| 幣種  
startTime| false| integer| 開始時間戳 (毫秒) _注意: 實際查詢時是秒級維度生效_  
endTime| false| integer| 結束時間戳 (毫秒) _注意: 實際查詢時是秒級維度生效_  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `50`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
rows| array| Object  
> coin| string| 幣種  
> chain| string| 鏈名  
> amount| string| 充值金額  
> txID| string| 交易Id. 充值失敗或取消充值時為空  
> [status](/docs/zh-TW/v5/enum#depositstatus)| integer| 充值狀態  
> toAddress| string| 充值的目標地址  
> tag| string| 充值目標地址的tag  
> depositFee| string| 充值手續費  
> successAt| string| 最後更新時間  
> confirmations| string| 确认区块的数量  
> txIndex| string| 交易序列号  
> blockHash| string| 鏈上的哈希數  
> batchReleaseLimit| string| 當前幣鏈每日充值限額. `"-1"`表示無限制  
> depositType| string| 入金類型. `0`: 正常充值, `10`: 充值觸發每日限額, `20`: 觸發AML充值，請前往網頁端提交材料，`50`: 帳戶存在限制，無法正常上帳，請前往網頁端提走資金  
> fromAddress| string| 入金來源地址, 僅當入金來自鏈上且來源地址唯一時返回地址, 其餘則返回`""`  
> taxDepositRecordsId| string| Bybit EU（奧地利）用戶用於稅務目的, 保稅記錄id  
> taxStatus| integer| Bybit EU（奧地利）用戶用於稅務目的 

  * 0: No reporting required
  * 1: Reporting pending
  * 2: Reporting completed

  
> id| string| 內部ID, 唯一鍵  
> requestId| string| 請求 ID  
> travelRuleStatus| integer| Travel Rule 審核狀態，非合規區可以忽略該字段 

  * `0`: Approved — 已通過，可繼續後續流程
  * `1`: CollectInfo — 需補充對手方信息，請重新提交問卷
  * `2`: Pending — 審核中，請輪詢入金查詢接口
  * `3`: Rejected — 已拒絕或失敗（含取消）

  
nextPageCursor| string| 游標，用於翻頁  
[](/docs/zh-TW/api-explorer/v5/asset/deposit-record)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/deposit/query-record?coin=USDT&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672191991544  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_deposit_records(  
        coin="USDT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getDepositRecords({  
        coin: 'USDT'  
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
                    "coin": "USDT",  
                    "chain": "TRX",  
                    "amount": "999.0496",  
                    "txID": "04bf3fbad2fc85b107a42cfdc5ff83110092b606ca754efa0f032f8b94b3262e",  
                    "status": 3,  
                    "toAddress": "TDGYpm5zPacnEqKV34TJPuhJhHom9hcXAy",  
                    "tag": "",  
                    "depositFee": "",  
                    "successAt": "1742728163000",  
                    "confirmations": "50",  
                    "txIndex": "0",  
                    "blockHash": "000000000436ab4dabc8a4a87beb2262d2d87f6761a825494c4f1d5ae11b27e8",  
                    "batchReleaseLimit": "-1",  
                    "depositType": "0",  
                    "fromAddress": "TJ7hhYhVhaxNx6BPyq7yFpqZrQULL3JSdb",  
                    "taxDepositRecordsId": "0",  
                    "taxStatus": 0,  
                    "id": "160237231",  
                    "requestId": "d54a802dfc364921a68684389a2c72bd"  
                }  
            ],  
            "nextPageCursor": "eyJtaW5JRCI6MTYwMjM3MjMxLCJtYXhJRCI6MTYwMjM3MjMxfQ=="  
        },  
        "retExtInfo": {},  
        "time": 1750798211884  
    }