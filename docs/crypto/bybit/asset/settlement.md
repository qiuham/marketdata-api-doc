---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/settlement
api_type: REST
updated_at: 2026-06-30 19:23:59.322198
---

# Create Internal Transfer

Create the internal transfer between different [account types](/docs/v5/enum#accounttype) under the same UID.

### HTTP Request

POST`/v5/asset/transfer/inter-transfer`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
transferId| **true**|  string| [UUID](https://www.uuidgenerator.net/dev-corner). Please manually generate a UUID  
coin| **true**|  string| Coin, uppercase only  
amount| **true**|  string| Amount  
[fromAccountType](/docs/v5/enum#accounttype)| **true**|  string| From account type  
[toAccountType](/docs/v5/enum#accounttype)| **true**|  string| To account type  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
transferId| string| UUID  
status| string| Transfer status 

  * `STATUS_UNKNOWN`
  * `SUCCESS`
  * `PENDING`
  * `FAILED`

  
[](/docs/api-explorer/v5/asset/create-inter-transfer)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST v5/asset/transfer/inter-transfer HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1670986690556  
    X-BAPI-RECV-WINDOW: 50000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
    {  
        "transferId": "42c0cfb0-6bca-c242-bc76-4e6df6cbcb16",  
        "coin": "BTC",  
        "amount": "0.05",  
        "fromAccountType": "UNIFIED",  
        "toAccountType": "CONTRACT"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_internal_transfer(  
        transferId="42c0cfb0-6bca-c242-bc76-4e6df6cbcb16",  
        coin="BTC",  
        amount="0.05",  
        fromAccountType="UNIFIED",  
        toAccountType="CONTRACT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .createInternalTransfer(  
        '42c0cfb0-6bca-c242-bc76-4e6df6cbcb16',  
        'BTC',  
        '0.05',  
        'UNIFIED',  
        'CONTRACT',  
      )  
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
            "transferId": "42c0cfb0-6bca-c242-bc76-4e6df6cbab16",  
            "status": "SUCCESS"  
        },  
        "retExtInfo": {},  
        "time": 1670986962783  
    }

---

# 劃轉 (單帳號內)

創建單帳號下[帳戶類型](/docs/zh-TW/v5/enum#accounttype)間的劃轉操作

提示

  * 每個帳戶類型有其可接受的幣種限制, 詳情請參考[可劃轉幣種](/docs/zh-TW/v5/asset/transfer/transferable-coin)接口.



### HTTP 請求

POST`/v5/asset/transfer/inter-transfer`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
transferId| **true**|  string| UUID. 請自行手動生成UUID  
coin| **true**|  string| 幣種  
amount| **true**|  string| 劃入數量  
[fromAccountType](/docs/zh-TW/v5/enum#accounttype)| **true**|  string| 轉出賬戶類型  
[toAccountType](/docs/zh-TW/v5/enum#accounttype)| **true**|  string| 轉入賬戶類型  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
transferId| string| UUID  
status| string| 劃轉狀態 

  * `STATUS_UNKNOWN`
  * `SUCCESS`
  * `PENDING`
  * `FAILED`

  
[](/docs/zh-TW/api-explorer/v5/asset/create-inter-transfer)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST v5/asset/transfer/inter-transfer HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1670986690556  
    X-BAPI-RECV-WINDOW: 50000  
    X-BAPI-SIGN: XXXXX  
    Content-Type: application/json  
    {  
        "transferId": "42c0cfb0-6bca-c242-bc76-4e6df6cbcb16",  
        "coin": "BTC",  
        "amount": "0.05",  
        "fromAccountType": "UNIFIED",  
        "toAccountType": "CONTRACT"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.create_internal_transfer(  
        transferId="42c0cfb0-6bca-c242-bc76-4e6df6cbcb16",  
        coin="BTC",  
        amount="0.05",  
        fromAccountType="UNIFIED",  
        toAccountType="CONTRACT",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .createInternalTransfer(  
        '42c0cfb0-6bca-c242-bc76-4e6df6cbcb16',  
        'BTC',  
        '0.05',  
        'UNIFIED',  
        'CONTRACT',  
      )  
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
            "transferId": "42c0cfb0-6bca-c242-bc76-4e6df6cbab16",  
            "status": "SUCCESS"  
        },  
        "retExtInfo": {},  
        "time": 1670986962783  
    }