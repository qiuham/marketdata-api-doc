---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/broker/reward/voucher
api_type: REST
updated_at: 2026-06-28 19:09:52.993153
---

# Query Point Balance

Query the user's card reward point balance, including available points, pending (frozen) points, account status, and related information.

### HTTP Request

POST`/v5/card/reward/points/balance`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Business return code. `0`: success; non-zero: failure  
retMsg| string| Return message  
result| object|   
> accountId| string| Account ID  
> availablePoint| string| Available points  
> pendingPoint| string| Pending (frozen) points  
> status| string| Account status  
> updateTime| string| Last update time (Unix ms timestamp)  
> settlementPeriod| integer| Settlement period  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/reward/points/balance HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/reward/points/balance"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    response = requests.post(url, headers=headers)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/reward/points/balance';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
      
    axios.post(url, {}, { headers })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "accountId": "100001",  
            "availablePoint": 5000,  
            "pendingPoint": 200,  
            "status": "active",  
            "updateTime": 1672211918471,  
            "settlementPeriod": 30  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }

---

# 查詢積分餘額

查詢用戶卡片獎勵積分餘額，包含可用積分、凍結積分、賬戶狀態等信息。

### HTTP 請求

POST`/v5/card/reward/points/balance`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 業務返回碼。`0`: 成功；非零: 失敗  
retMsg| string| 返回消息  
result| object|   
> accountId| string| 賬戶 ID  
> availablePoint| string| 可用積分  
> pendingPoint| string| 凍結積分  
> status| string| 賬戶狀態  
> updateTime| string| 更新時間（Unix 毫秒時間戳）  
> settlementPeriod| integer| 結算週期  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/reward/points/balance HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/reward/points/balance"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    response = requests.post(url, headers=headers)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/reward/points/balance';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
      
    axios.post(url, {}, { headers })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "accountId": "100001",  
            "availablePoint": 5000,  
            "pendingPoint": 200,  
            "status": "active",  
            "updateTime": 1672211918471,  
            "settlementPeriod": 30  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }