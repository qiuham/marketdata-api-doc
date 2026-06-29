---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/broker/exchange-broker/rate-limit/query-all
api_type: REST
updated_at: 2026-06-29 19:27:06.828291
---

# Get Sub Account Deposit Records

Exchange broker can query subaccount's deposit records by **main** UID's API key without specifying uid.

> API rate limit: 300 req / min

tip

  * `endTime` \- `startTime` should be less than 30 days. Queries for the last 30 days worth of records by default.
  * Sort by deposit creation time in descending order.



### HTTP Request

GET`/v5/broker/asset/query-sub-member-deposit-record`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
id| false| string| Internal ID: Can be used to uniquely identify and filter the deposit. When combined with other parameters, this field takes the highest priority  
txID| false| string| Transaction ID: Please note that data generated before Jan 1, 2024 cannot be queried using txID  
subMemberId| false| string| Sub UID  
coin| false| string| Coin, uppercase only  
startTime| false| integer| The start timestamp (ms) _Note: the query logic is actually effective based on**second** level_  
endTime| false| integer| The end timestamp (ms) _Note: the query logic is actually effective based on**second** level_  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
rows| array| Object  
> id| string| Unique ID  
> subMemberId| string| Sub account user ID  
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
> depositType| string| The deposit type. `0`: normal deposit, `10`: the deposit reaches daily deposit limit, `20`: abnormal deposit  
> fromAddress| string| From address of deposit, only shown when the deposit comes from on-chain and from address is unique, otherwise gives `""`  
> taxDepositRecordsId| string| This field is used for tax purposes by Bybit EU (Austria) users, declare tax id  
> taxStatus| integer| This field is used for tax purposes by Bybit EU (Austria) users 

  * 0: No reporting required
  * 1: Reporting pending
  * 2: Reporting completed

  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/broker/asset/query-sub-member-deposit-record?coin=USDT&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672192441294  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_subaccount_deposit_records(  
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
      .getBrokerSubAccountDeposits({  
        limit: 50,  
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
            "rows": [],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1672192441742  
    }

---

# 查詢子帳號充值紀錄

經紀商僅能通過**主帳號** 的API key來查詢子帳號的充值紀錄

> API頻率: 300次/分

提示

  * `endTime` \- `startTime` 需要小於等於30天. 默認查詢最近30天的紀錄
  * 按照充值創建時間倒序排序



### HTTP 請求

GET`/v5/broker/asset/query-sub-member-deposit-record`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
id| false| string| 內部ID: 可用於唯一篩選入金紀錄. 當跟其他參數組合時, 具有最高優先級  
txID| false| string| 鏈上交易ID: 請注意2024年1月1日之前的入金紀錄, 無法通過txID來篩選  
subMemberId| false| string| 子帳號  
coin| false| string| 幣種  
startTime| false| integer| 開始時間戳 (毫秒) _注意: 實際查詢時是秒級維度生效_  
endTime| false| integer| 結束時間戳 (毫秒) _注意: 實際查詢時是秒級維度生效_  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `50`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
rows| array| Object  
> id| string| 內部ID, 唯一鍵  
> subMemberId| string| 子帳戶UID  
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
> depositType| string| 入金類型. `0`: 正常充值, `10`: 充值觸發每日限額, `20`: 異常充值  
> fromAddress| string| 入金來源地址, 僅當入金來自鏈上且來源地址唯一時返回地址, 其餘則返回`""`  
> taxDepositRecordsId| string| Bybit EU（奧地利）用戶用於稅務目的, 保稅記錄id  
> taxStatus| integer| Bybit EU（奧地利）用戶用於稅務目的 

  * 0: No reporting required
  * 1: Reporting pending
  * 2: Reporting completed

  
nextPageCursor| string| 游標，用於翻頁  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/broker/asset/query-sub-member-deposit-record?coin=USDT&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672192441294  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_subaccount_deposit_records(  
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
      .getBrokerSubAccountDeposits({  
        limit: 50,  
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
            "rows": [],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1672192441742  
    }