---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/withdraw/withdraw-address
api_type: REST
updated_at: 2026-07-01 19:26:44.095882
---

# Get Withdrawal Records

Query withdrawal records.

tip

  * `endTime` \- `startTime` should be less than 30 days. Query last 30 days records by default.
  * Can query by the master UID's api key **only**



### HTTP Request

GET`/v5/asset/withdraw/query-record`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
withdrawID| false| string| Withdraw ID  
txID| false| string| Transaction hash ID  
coin| false| string| Coin, uppercase only  
withdrawType| false| integer| Withdraw type. `0`(default): on chain. `1`: off chain. `2`: all  
startTime| false| integer| The start timestamp (ms)  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `50`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
rows| array| Object  
> txID| string| Transaction ID. It returns `""` when withdrawal failed, withdrawal cancelled  
> coin| string| Coin  
> chain| string| Chain  
> amount| string| Amount  
> withdrawFee| string| Withdraw fee  
> [status](/docs/v5/enum#withdrawstatus)| string| Withdraw status  
> toAddress| string| To withdrawal address. Shows the Bybit UID for internal transfers  
> tag| string| Tag  
> createTime| string| Withdraw created timestamp (ms)  
> updateTime| string| Withdraw updated timestamp (ms)  
> withdrawId| string| Withdraw ID  
> withdrawType| integer| Withdraw type. `0`: on chain. `1`: off chain  
> tax| string| Tax amount. Applicable to specific users based on Tax Centre configuration. Default: `"0"`  
> taxRate| string| Tax rate. Applicable to specific users based on Tax Centre configuration. Default: `"0"`  
> taxType| string| Tax type. Applicable to specific users based on Tax Centre configuration. Default: `""`  
nextPageCursor| string| Cursor. Used for pagination  
[](/docs/api-explorer/v5/asset/withdraw-record)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/withdraw/query-record?coin=USDT&withdrawType=2&limit=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672194949557  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_withdrawal_records(  
        coin="USDT",  
        withdrawType=2,  
        limit=2,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getWithdrawalRecords({  
        coin: 'USDT',  
        withdrawType: 2,  
        limit: 2,  
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
                    "coin": "USDC",  
                    "chain": "ETH",  
                    "amount": "41.43008",  
                    "txID": "0x3d7bddb797f0e86420c982c0723653b8b728fd0ec9953b6b354445848d83a185",  
                    "status": "success",  
                    "toAddress": "0xE3De6d711e0951d34777b5Cd93c827F822ee8514",  
                    "tag": "",  
                    "withdrawFee": "5",  
                    "createTime": "1742738305000",  
                    "updateTime": "1742738340000",  
                    "withdrawId": "131629076",  
                    "withdrawType": 0,  
                    "fee": "",  
                    "tax": "",  
                    "taxRate": "",  
                    "taxType": ""  
                },  
                {  
                    "coin": "USDT",  
                    "chain": "SOL",  
                    "amount": "951",  
                    "txID": "53j7mUftUboJ2TVb1q3zjwNi9gNGWyQ8xhEpkFovzqaTf8LzuZKzr83XjbG62TZWBkWbn27km7SD6Sc9e1BuWUfJ",  
                    "status": "success",  
                    "toAddress": "DhTEGye1vq2PPr8DPWit4HTDprnvnDiqpVHnHSY1Y82p",  
                    "tag": "",  
                    "withdrawFee": "1",  
                    "createTime": "1742729329000",  
                    "updateTime": "1742729437000",  
                    "withdrawId": "131603458",  
                    "withdrawType": 0,  
                    "fee": "",  
                    "tax": "",  
                    "taxRate": "",  
                    "taxType": ""  
                }  
            ],  
            "nextPageCursor": "eyJtaW5JRCI6MTMxNjAzNDU4LCJtYXhJRCI6MTMxNjI5MDc2fQ=="  
        },  
        "retExtInfo": {},  
        "time": 1750777316807  
    }

---

# 查詢提現紀錄

提示

  * `endTime` \- `startTime`需要小於等於30天. 默認查詢最近30天的紀錄。
  * 僅支持**母帳號** 的API key



### HTTP 請求

GET`/v5/asset/withdraw/query-record`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
withdrawID| false| string| 提現Id  
txID| false| string| 交易哈希ID  
coin| false| string| 幣種  
withdrawType| false| integer| 提現類型. `0`(默認): 鏈上提幣. `1`: 平台內部轉帳. `2`: 所有方式  
startTime| false| integer| 開始時間戳 (毫秒)  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `50`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
rows| array| Object  
> txID| string| 交易Id，提現失敗/提現撤銷：為空  
> coin| string| 幣種  
> chain| string| 鏈名  
> amount| string| 提幣金額  
> withdrawFee| string| 提幣手續費  
> [status](/docs/zh-TW/v5/enum#withdrawstatus)| string| 提幣狀態  
> toAddress| string| 提現目標地址. 內部轉帳：顯示Bybit UID  
> tag| string| 標籤  
> createTime| string| 提現創建時間戳 (毫秒)  
> updateTime| string| 提現更新時間戳 (毫秒)  
> withdrawId| string| 提現Id  
> withdrawType| integer| 提現類型. `0`: 鏈上提幣. `1`: 內部轉帳  
> tax| string| 稅額。根據稅務中心配置對特定用戶有具體值。默認返回 `"0"`  
> taxRate| string| 稅率。根據稅務中心配置對特定用戶有具體值。默認返回 `"0"`  
> taxType| string| 稅類型。根據稅務中心配置對特定用戶有具體值。默認返回 `""`  
[](/docs/zh-TW/api-explorer/v5/asset/withdraw-record)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/withdraw/query-record?coin=USDT&withdrawType=2&limit=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672194949557  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_withdrawal_records(  
        coin="USDT",  
        withdrawType=2,  
        limit=2,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getWithdrawalRecords({  
        coin: 'USDT',  
        withdrawType: 2,  
        limit: 2,  
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
                    "coin": "USDC",  
                    "chain": "ETH",  
                    "amount": "41.43008",  
                    "txID": "0x3d7bddb797f0e86420c982c0723653b8b728fd0ec9953b6b354445848d83a185",  
                    "status": "success",  
                    "toAddress": "0xE3De6d711e0951d34777b5Cd93c827F822ee8514",  
                    "tag": "",  
                    "withdrawFee": "5",  
                    "createTime": "1742738305000",  
                    "updateTime": "1742738340000",  
                    "withdrawId": "131629076",  
                    "withdrawType": 0,  
                    "fee": "",  
                    "tax": "",  
                    "taxRate": "",  
                    "taxType": ""  
                },  
                {  
                    "coin": "USDT",  
                    "chain": "SOL",  
                    "amount": "951",  
                    "txID": "53j7mUftUboJ2TVb1q3zjwNi9gNGWyQ8xhEpkFovzqaTf8LzuZKzr83XjbG62TZWBkWbn27km7SD6Sc9e1BuWUfJ",  
                    "status": "success",  
                    "toAddress": "DhTEGye1vq2PPr8DPWit4HTDprnvnDiqpVHnHSY1Y82p",  
                    "tag": "",  
                    "withdrawFee": "1",  
                    "createTime": "1742729329000",  
                    "updateTime": "1742729437000",  
                    "withdrawId": "131603458",  
                    "withdrawType": 0,  
                    "fee": "",  
                    "tax": "",  
                    "taxRate": "",  
                    "taxType": ""  
                }  
            ],  
            "nextPageCursor": "eyJtaW5JRCI6MTMxNjAzNDU4LCJtYXhJRCI6MTMxNjI5MDc2fQ=="  
        },  
        "retExtInfo": {},  
        "time": 1750777316807  
    }