---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/bybit-card/asset-records
api_type: REST
updated_at: 2026-05-27 19:16:13.398373
---

# Query Cashback Detail

Query the cashback detail for a specific card reward order, including point amount, cashback value, currency, and order status.

### HTTP Request

POST`/v5/card/reward/point/cashback/detail`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
bizTxnId| **true**|  string| Order ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
retCode| integer| Business return code. `0`: success; non-zero: failure  
retMsg| string| Return message  
result| object|   
> points| string| Point amount  
> amt| string| Cashback amount  
> ccy| string| Currency  
> ccyType| string| Currency type. `FIAT`: fiat currency, `CRYPTO`: crypto currency  
> createTime| string| Creation time  
> bizTxnId| string| Order ID  
> sourceId| integer| Coupon/voucher ID  
> sourceCode| string| External order ID  
> orderStatus| integer| Order status  
> orderSubStatus| integer| Order sub-status  
> orderShowStatus| string| Display status. `NO_PAY`: Unpaid, `ORDER_PENDING_SHOW`: Pending, `ORDER_SUCCESS`: Success, `ORDER_FAIL`: Failed  
> failedBizCode| string| Failure reason code  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/reward/point/cashback/detail?bizTxnId=TXN20230101001 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/reward/point/cashback/detail"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    params = {  
        "bizTxnId": "TXN20230101001"  
    }  
    response = requests.post(url, headers=headers, params=params)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/reward/point/cashback/detail';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const params = { bizTxnId: 'TXN20230101001' };  
      
    axios.post(url, {}, { headers, params })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "points": "500",  
            "amt": "1.00",  
            "ccy": "USDT",  
            "ccyType": "CRYPTO",  
            "createTime": "2023-01-01 12:00:00",  
            "bizTxnId": "TXN20230101001",  
            "sourceId": 12345,  
            "sourceCode": "ORD20230101001",  
            "orderStatus": 1,  
            "orderSubStatus": 0,  
            "orderShowStatus": "ORDER_SUCCESS",  
            "failedBizCode": ""  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }

---

# 查詢 Cashback 明細

查詢指定卡片獎勵訂單的 cashback 返現明細，包含積分數、返現金額、幣種及訂單狀態等。

### HTTP 請求

POST`/v5/card/reward/point/cashback/detail`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
bizTxnId| **true**|  string| 訂單號  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
retCode| integer| 業務返回碼。`0`: 成功；非零: 失敗  
retMsg| string| 返回消息  
result| object|   
> points| string| 積分數  
> amt| string| 返現金額  
> ccy| string| 幣種  
> ccyType| string| 幣種類型。`FIAT`: 法幣，`CRYPTO`: 數字貨幣  
> createTime| string| 創建時間  
> bizTxnId| string| 訂單號  
> sourceId| integer| 卡券 ID  
> sourceCode| string| 外部訂單號  
> orderStatus| integer| 訂單狀態  
> orderSubStatus| integer| 訂單子狀態  
> orderShowStatus| string| 展示狀態。`NO_PAY`: 未支付，`ORDER_PENDING_SHOW`: 處理中，`ORDER_SUCCESS`: 成功，`ORDER_FAIL`: 失敗  
> failedBizCode| string| 失敗原因碼  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/card/reward/point/cashback/detail?bizTxnId=TXN20230101001 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211918471  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    import requests  
      
    url = "https://api-testnet.bybit.com/v5/card/reward/point/cashback/detail"  
    headers = {  
        "X-BAPI-API-KEY": "xxxxxxxxxxxxxxxxxx",  
        "X-BAPI-SIGN": "XXXXX",  
        "X-BAPI-TIMESTAMP": "1672211918471",  
        "X-BAPI-RECV-WINDOW": "5000"  
    }  
    params = {  
        "bizTxnId": "TXN20230101001"  
    }  
    response = requests.post(url, headers=headers, params=params)  
    print(response.json())  
    
    
    
    const axios = require('axios');  
      
    const url = 'https://api-testnet.bybit.com/v5/card/reward/point/cashback/detail';  
    const headers = {  
      'X-BAPI-API-KEY': 'xxxxxxxxxxxxxxxxxx',  
      'X-BAPI-SIGN': 'XXXXX',  
      'X-BAPI-TIMESTAMP': '1672211918471',  
      'X-BAPI-RECV-WINDOW': '5000'  
    };  
    const params = { bizTxnId: 'TXN20230101001' };  
      
    axios.post(url, {}, { headers, params })  
      .then(response => console.log(response.data))  
      .catch(error => console.error(error));  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "points": "500",  
            "amt": "1.00",  
            "ccy": "USDT",  
            "ccyType": "CRYPTO",  
            "createTime": "2023-01-01 12:00:00",  
            "bizTxnId": "TXN20230101001",  
            "sourceId": 12345,  
            "sourceCode": "ORD20230101001",  
            "orderStatus": 1,  
            "orderSubStatus": 0,  
            "orderShowStatus": "ORDER_SUCCESS",  
            "failedBizCode": ""  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }