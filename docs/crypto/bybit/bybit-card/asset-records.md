---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bybit-card/asset-records
api_type: REST
updated_at: 2026-07-16 18:51:39.770894
---

# Query Point Records

Query the user's card reward point transaction records. Supports pagination and filtering by time range, type, and direction.

### HTTP Request

POST`/v5/card/reward/points/records`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
type| false| string| Point type filter  
pageSize| false| integer| Number of items per page. Default: `10`. Min: `1`  
pageNo| false| integer| Page number. Default: `1`. Min: `1`  
startTime| false| integer| Start time (Unix timestamp)  
endTime| false| integer| End time (Unix timestamp)  
outOrderId| false| string| External order ID  
bizId| false| string| Point order ID  
bizTxnId| false| string| consumeIdLifecycle  
side| false| string| Point direction. `1`: Earn points, `2`: Deduct points  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Business return code. `0`: success; non-zero: failure  
retMsg| string| Return message  
result| object|   
> pageSize| integer| Number of items per page  
> pageNo| integer| Current page number  
> totalCount| integer| Total number of records  
> data| array| Point record list  
>> outOrderId| string| External order ID  
>> point| integer| Point amount  
>> side| string| Point direction  
>> type| string| Type  
>> subType| string| Sub-type  
>> createTime| integer| Creation time (Unix ms timestamp)  
>> updateTime| integer| Update time (Unix ms timestamp)  
>> bizId| string| Point order ID  
>> bizTxnId| string| consumeIdLifecycle  
>> transactionDate| string| Transaction date and time  
>> transactionId| string| Transaction ID  
>> transactionAmount| string| Transaction amount / Paid with fiat  
>> basicCurrency| string| Transaction currency  
>> merchCategoryDesc| string| Merchant category  
>> merchName| string| Merchant name  
>> merchCountry| string| Location (country)  
>> merchCity| string| Location (city)  
>> pan4| string| Card's last 4 digits  
>> payFiatAmount| string| Pay with fiat  
>> transactionCurrencyAmount| string| Pay with crypto  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/reward/points/records?pageSize=10&pageNo=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/reward/points/records"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    params = {  
        "pageSize": 10,  
        "pageNo": 1  
    }  
    response = requests.post(url, headers=headers, params=params)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/reward/points/records';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const params = { pageSize: 10, pageNo: 1 };  
      
    axios.post(url, {}, { headers, params })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "pageSize": 10,  
            "pageNo": 1,  
            "totalCount": 50,  
            "data": [  
                {  
                    "outOrderId": "ORD20230101001",  
                    "point": 100,  
                    "side": "1",  
                    "type": "CASHBACK",  
                    "subType": "",  
                    "createTime": 1672211918471,  
                    "updateTime": 1672211918471,  
                    "bizId": "BIZ20230101001",  
                    "bizTxnId": "TXN20230101001",  
                    "transactionDate": "2023-01-01 12:00:00",  
                    "transactionId": "TXN20230101001",  
                    "transactionAmount": "100.00",  
                    "basicCurrency": "USD",  
                    "merchCategoryDesc": "Grocery Stores",  
                    "merchName": "Amazon",  
                    "merchCountry": "US",  
                    "merchCity": "New York",  
                    "pan4": "1234",  
                    "payFiatAmount": "0",  
                    "transactionCurrencyAmount": "100.00"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }

---

# 查詢積分流水

查詢用戶卡片獎勵積分變動流水，支持分頁查詢，可按時間範圍、類型和方向過濾。

### HTTP 請求

POST`/v5/card/reward/points/records`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
type| false| string| 積分類型過濾  
pageSize| false| integer| 每頁條數，默認 `10`，最小值 `1`  
pageNo| false| integer| 頁碼，默認 `1`，最小值 `1`  
startTime| false| integer| 開始時間（時間戳）  
endTime| false| integer| 結束時間（時間戳）  
outOrderId| false| string| 外部訂單號  
bizId| false| string| 積分訂單號  
bizTxnId| false| string| consumeIdLifecycle  
side| false| string| 積分方向。`1`: 加積分，`2`: 退積分  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 業務返回碼。`0`: 成功；非零: 失敗  
retMsg| string| 返回消息  
result| object|   
> pageSize| integer| 每頁條數  
> pageNo| integer| 當前頁碼  
> totalCount| integer| 總記錄數  
> data| array| 積分流水列表  
>> outOrderId| string| 外部訂單號  
>> point| integer| 積分數  
>> side| string| 積分方向  
>> type| string| 類型  
>> subType| string| 子類型  
>> createTime| integer| 創建時間（Unix 毫秒時間戳）  
>> updateTime| integer| 更新時間（Unix 毫秒時間戳）  
>> bizId| string| 積分訂單號  
>> bizTxnId| string| consumeIdLifecycle  
>> transactionDate| string| 交易日期及時間  
>> transactionId| string| 交易 ID  
>> transactionAmount| string| 交易金額 / 法幣支付金額  
>> basicCurrency| string| 交易貨幣  
>> merchCategoryDesc| string| 商戶類別  
>> merchName| string| 商戶名稱  
>> merchCountry| string| 商戶所在國家  
>> merchCity| string| 商戶所在城市  
>> pan4| string| 卡後 4 位  
>> payFiatAmount| string| 法幣支付金額  
>> transactionCurrencyAmount| string| 加密貨幣支付金額  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/reward/points/records?pageSize=10&pageNo=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/reward/points/records"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    params = {  
        "pageSize": 10,  
        "pageNo": 1  
    }  
    response = requests.post(url, headers=headers, params=params)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/reward/points/records';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const params = { pageSize: 10, pageNo: 1 };  
      
    axios.post(url, {}, { headers, params })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "pageSize": 10,  
            "pageNo": 1,  
            "totalCount": 50,  
            "data": [  
                {  
                    "outOrderId": "ORD20230101001",  
                    "point": 100,  
                    "side": "1",  
                    "type": "CASHBACK",  
                    "subType": "",  
                    "createTime": 1672211918471,  
                    "updateTime": 1672211918471,  
                    "bizId": "BIZ20230101001",  
                    "bizTxnId": "TXN20230101001",  
                    "transactionDate": "2023-01-01 12:00:00",  
                    "transactionId": "TXN20230101001",  
                    "transactionAmount": "100.00",  
                    "basicCurrency": "USD",  
                    "merchCategoryDesc": "Grocery Stores",  
                    "merchName": "Amazon",  
                    "merchCountry": "US",  
                    "merchCity": "New York",  
                    "pan4": "1234",  
                    "payFiatAmount": "0",  
                    "transactionCurrencyAmount": "100.00"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }