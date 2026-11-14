---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/broker/reward/get-issue-voucher
api_type: REST
updated_at: 2026-11-13 19:22:16.186165
---

# Get Issued Voucher

### HTTP Request

POST`/v5/broker/award/distribution-record`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
accountId| **true**|  string| User ID  
awardId| **true**|  string| Voucher ID  
specCode| **true**|  string| Customised unique spec code, up to 8 characters  
withUsedAmount| false| boolean| Whether or not to return the amount used by the user 

  * `true`
  * `false` (default)

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
accountId| string| User ID  
awardId| string| Voucher ID  
specCode| string| Spec code  
amount| string| Amount of voucher  
isClaimed| boolean| `true`, `false`  
startAt| string| Claim start timestamp (sec)  
endAt| string| Claim end timestamp (sec)  
effectiveAt| string| Voucher effective timestamp (sec) after claimed  
ineffectiveAt| string| Voucher inactive timestamp (sec) after claimed  
usedAmount| string| Amount used by the user  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/broker/award/distribution-record HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1726112099846  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 111  
      
    {  
        "accountId": "5714139",  
        "awardId": "189528",  
        "specCode": "demo000",  
        "withUsedAmount": false  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_issued_voucher(  
        id="80209",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getBrokerIssuedVoucher({  
        id: '80209',  
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
        "retMsg": "",  
        "result": {  
            "accountId": "5714139",  
            "awardId": "189528",  
            "specCode": "demo000",  
            "amount": "1",  
            "isClaimed": true,  
            "startAt": "1725926400",  
            "endAt": "1733788800",  
            "effectiveAt": "1726531200",  
            "ineffectiveAt": "1733817600",  
            "usedAmount": "",  
        }  
    }

---

# 查詢已發放代金券

### HTTP 請求

POST`/v5/broker/award/distribution-record`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
accountId| **true**|  string| 用戶ID  
awardId| **true**|  string| 代金券ID  
specCode| **true**|  string| 自定義標識碼  
withUsedAmount| false| boolean| 是否返回用戶已使用金額 

  * `true`
  * `false` (默認)

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
accountId| string| 用戶ID  
awardId| string| 代金券ID  
specCode| string| 自定義標識碼  
amount| string| 代金券金額  
isClaimed| boolean| 是否已領取`true`, `false`  
startAt| string| 可領取開始時間 (秒級時間戳)  
endAt| string| 可領取結束始時間 (秒級時間戳)  
effectiveAt| string| 領取後生效時間 (秒級時間戳)  
ineffectiveAt| string| 領取後失效時間 (秒級時間戳)  
usedAmount| string| 用戶已使用金額  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/broker/award/distribution-record HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1726112099846  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 111  
      
    {  
        "accountId": "5714139",  
        "awardId": "189528",  
        "specCode": "demo000",  
        "withUsedAmount": false  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_issued_voucher(  
        id="80209",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getBrokerIssuedVoucher({  
        id: '80209',  
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
        "retMsg": "",  
        "result": {  
            "accountId": "5714139",  
            "awardId": "189528",  
            "specCode": "demo000",  
            "amount": "1",  
            "isClaimed": true,  
            "startAt": "1725926400",  
            "endAt": "1733788800",  
            "effectiveAt": "1726531200",  
            "ineffectiveAt": "1733817600",  
            "usedAmount": "",  
        }  
    }