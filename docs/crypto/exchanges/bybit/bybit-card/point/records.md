---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bybit-card/point/records
api_type: REST
updated_at: 2026-05-27 19:16:17.409647
---

# Query Tier Info

Query the user's card reward tier level and spending limit information, including used limit, total limit, tier level, and auto cashback setting.

### HTTP Request

POST`/v5/card/reward/points/tier`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Business return code. `0`: success; non-zero: failure  
retMsg| string| Return message  
result| object|   
> usedLimit| string| Used spending limit (in USD, converted from points × 0.002, rounded to 2 decimal places)  
> limit| string| Total spending limit  
> unit| string| Limit unit (e.g. `USD`)  
> tier| string| User tier level  
> autoCashback| boolean| Whether auto cashback is enabled  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/reward/points/tier HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/reward/points/tier"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    response = requests.post(url, headers=headers)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/reward/points/tier';  
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
            "usedLimit": "10.00",  
            "limit": "500.00",  
            "unit": "1",  
            "tier": "GOLD",  
            "autoCashback": true  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }

---

# 查詢 Tier 信息

查詢用戶卡片獎勵 Tier 等級及消費額度信息，包含已消費額度、總額度、用戶 Tier 等級及是否開啟自動 cashback 等。

### HTTP 請求

POST`/v5/card/reward/points/tier`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 業務返回碼。`0`: 成功；非零: 失敗  
retMsg| string| 返回消息  
result| object|   
> usedLimit| string| 已消費額度（單位 USD，積分 × 0.002 轉換，保留兩位小數，四捨五入）  
> limit| string| 總額度  
> unit| string| 額度單位（如 `USD`）  
> tier| string| 用戶 Tier 等級  
> autoCashback| boolean| 是否開啟自動 cashback  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/reward/points/tier HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/reward/points/tier"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    response = requests.post(url, headers=headers)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/reward/points/tier';  
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
            "usedLimit": "10.00",  
            "limit": "500.00",  
            "unit": "1",  
            "tier": "GOLD",  
            "autoCashback": true  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }