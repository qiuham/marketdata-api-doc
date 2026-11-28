---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bybit-card/card-limit
api_type: REST
updated_at: 2026-11-28 18:48:33.189079
---

# Query Card Limits

Query limits for the authenticated user's card, based on the user, card product, and card type. Returns system limits, user-configured limits, and current usage.

tip

Only limits for cards belonging to the authenticated user can be queried

All amounts are JSON numbers in the currency specified by `baseFiat`. Values that are not provided can be `null`.

### HTTP Request

POST`/v5/card/limit/get`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
cardId| true| string| Card ID belonging to the authenticated user. Cannot be missing, `null`, empty, or whitespace-only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Business return code. `0`: success; non-zero: failure  
retMsg| string| Return message  
result| object| Query result. `null` on failure  
> limitItems| array| Limit item list. The number of items depends on the product and available limit data  
>> baseFiat| string| Base fiat currency code for all amounts in this item. Can be `null`  
>> itemType| string| Limit type. `SPENDING`: Spending, `ATM_WITHDRAW`: ATM withdrawal. Other types are returned as their original strings, including `"3"`: Total cash, `"4"`: Cash-like spending other than ordinary payments, `"5"`: QR Pay. Can be `null`  
>> singleAllowed| number| System limit per transaction. Can be `null`  
>> singleCustomLimit| number| User-configured limit per transaction. Can be `null`  
>> dailyUsed| number| Accumulated usage for the current day. Can be `null`  
>> dailyAllowed| number| System daily limit. Can be `null`  
>> dailyCustomLimit| number| User-configured daily limit. Can be `null`  
>> monthlyUsed| number| Accumulated usage for the current month. Can be `null`  
>> monthlyAllowed| number| System monthly limit. Can be `null`  
>> monthlyCustomLimit| number| User-configured monthly limit. Can be `null`  
>> yearlyUsed| number| Accumulated usage for the current year. Can be `null`  
>> yearlyAllowed| number| System yearly limit. Can be `null`  
>> lifeTimeUsed| number| Accumulated lifetime usage. Can be `null`  
>> lifeTimeAllowed| number| System lifetime limit. Can be `null`  
retExtInfo| object| Extended information. Defaults to `{}`  
time| integer| Response time (Unix ms timestamp)  
  
### Error Codes

retCode| retMsg| Comments  
---|---|---  
913110400| CARD NOT EXISTS| Card does not exist or does not belong to the authenticated user  
913110000| cardId cannot be blank| `cardId` is missing, `null`, empty, or whitespace-only  
913100000| SYSTEM ERROR| Request binding failure or system error  
  
Global error responses may omit `retExtInfo` and `time`.

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/limit/get HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "cardId": "180585395564494848"  
    }  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/limit/get"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    body = {  
        "cardId": "180585395564494848"  
    }  
    response = requests.post(url, headers=headers, json=body)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/limit/get';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const body = { cardId: '180585395564494848' };  
      
    axios.post(url, body, { headers })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "limitItems": [  
                {  
                    "baseFiat": "USD",  
                    "itemType": "SPENDING",  
                    "singleAllowed": 2500,  
                    "singleCustomLimit": null,  
                    "dailyUsed": 1000,  
                    "dailyAllowed": 5000,  
                    "dailyCustomLimit": null,  
                    "monthlyUsed": 5000,  
                    "monthlyAllowed": 50000,  
                    "monthlyCustomLimit": null,  
                    "yearlyUsed": null,  
                    "yearlyAllowed": null,  
                    "lifeTimeUsed": null,  
                    "lifeTimeAllowed": null  
                },  
                {  
                    "baseFiat": "USD",  
                    "itemType": "ATM_WITHDRAW",  
                    "singleAllowed": 500,  
                    "singleCustomLimit": null,  
                    "dailyUsed": 200,  
                    "dailyAllowed": 1000,  
                    "dailyCustomLimit": null,  
                    "monthlyUsed": 1000,  
                    "monthlyAllowed": 10000,  
                    "monthlyCustomLimit": null,  
                    "yearlyUsed": null,  
                    "yearlyAllowed": null,  
                    "lifeTimeUsed": null,  
                    "lifeTimeAllowed": null  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }

---

# 查詢卡片限額

根據用戶、卡產品及卡片類型，查詢已認證用戶本人的卡片限額。返回系統限額、用戶設置的限額及當前用量。

提示

僅可查詢屬於已認證用戶本人的卡片限額

所有金額均為 JSON number，幣種由 `baseFiat` 指定；未提供的值可以為 `null`。

### HTTP 請求

POST`/v5/card/limit/get`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
cardId| true| string| 已認證用戶本人的卡片 ID，不可缺少、為 `null`、空字符串或僅包含空白字符  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 業務返回碼。`0`: 成功；非零: 失敗  
retMsg| string| 返回消息  
result| object| 查詢結果，失敗時為 `null`  
> limitItems| array| 限額項列表，數量取決於產品及可用的限額數據  
>> baseFiat| string| 本項所有金額的基礎法幣代碼，可以為 `null`  
>> itemType| string| 限額類型。`SPENDING`: 消費, `ATM_WITHDRAW`: ATM 取款。其他類型以原始字符串返回，包括 `"3"`: 總現金, `"4"`: 非普通支付的現金類消費, `"5"`: QR Pay。可以為 `null`  
>> singleAllowed| number| 系統單筆限額，可以為 `null`  
>> singleCustomLimit| number| 用戶設置的單筆限額，可以為 `null`  
>> dailyUsed| number| 當前日累計用量，可以為 `null`  
>> dailyAllowed| number| 系統日限額，可以為 `null`  
>> dailyCustomLimit| number| 用戶設置的日限額，可以為 `null`  
>> monthlyUsed| number| 當前月累計用量，可以為 `null`  
>> monthlyAllowed| number| 系統月限額，可以為 `null`  
>> monthlyCustomLimit| number| 用戶設置的月限額，可以為 `null`  
>> yearlyUsed| number| 當前年累計用量，可以為 `null`  
>> yearlyAllowed| number| 系統年限額，可以為 `null`  
>> lifeTimeUsed| number| 生命週期累計用量，可以為 `null`  
>> lifeTimeAllowed| number| 系統生命週期限額，可以為 `null`  
retExtInfo| object| 擴展信息，默認為 `{}`  
time| integer| 響應時間（Unix 毫秒時間戳）  
  
### 錯誤碼

retCode| retMsg| 說明  
---|---|---  
913110400| CARD NOT EXISTS| 卡片不存在或不屬於已認證用戶本人  
913110000| cardId cannot be blank| `cardId` 缺少、為 `null`、空字符串或僅包含空白字符  
913100000| SYSTEM ERROR| 請求參數綁定失敗或系統異常  
  
全局異常響應可以缺少 `retExtInfo` 和 `time`。

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/limit/get HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "cardId": "180585395564494848"  
    }  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/limit/get"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    body = {  
        "cardId": "180585395564494848"  
    }  
    response = requests.post(url, headers=headers, json=body)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/limit/get';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const body = { cardId: '180585395564494848' };  
      
    axios.post(url, body, { headers })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "limitItems": [  
                {  
                    "baseFiat": "USD",  
                    "itemType": "SPENDING",  
                    "singleAllowed": 2500,  
                    "singleCustomLimit": null,  
                    "dailyUsed": 1000,  
                    "dailyAllowed": 5000,  
                    "dailyCustomLimit": null,  
                    "monthlyUsed": 5000,  
                    "monthlyAllowed": 50000,  
                    "monthlyCustomLimit": null,  
                    "yearlyUsed": null,  
                    "yearlyAllowed": null,  
                    "lifeTimeUsed": null,  
                    "lifeTimeAllowed": null  
                },  
                {  
                    "baseFiat": "USD",  
                    "itemType": "ATM_WITHDRAW",  
                    "singleAllowed": 500,  
                    "singleCustomLimit": null,  
                    "dailyUsed": 200,  
                    "dailyAllowed": 1000,  
                    "dailyCustomLimit": null,  
                    "monthlyUsed": 1000,  
                    "monthlyAllowed": 10000,  
                    "monthlyCustomLimit": null,  
                    "yearlyUsed": null,  
                    "yearlyAllowed": null,  
                    "lifeTimeUsed": null,  
                    "lifeTimeAllowed": null  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }