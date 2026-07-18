---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/broker/reward/issue-voucher
api_type: REST
updated_at: 2026-07-18 18:52:30.404267
---

# Get Voucher Spec

### HTTP Request

POST`/v5/broker/award/info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
id| **true**|  string| Voucher ID  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Voucher ID  
coin| string| Coin  
amountUnit| string| 

  * `AWARD_AMOUNT_UNIT_USD`
  * `AWARD_AMOUNT_UNIT_COIN`

  
productLine| string| Product line  
subProductLine| string| Sub product line  
totalAmount| Object| Total amount of voucher  
usedAmount| string| Used amount of voucher  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/broker/award/info HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1726107086048  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 22  
      
    {  
        "id": "80209"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_voucher_spec(  
        id="80209",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getBrokerVoucherSpec({  
        accountId: '5714139',  
        awardId: '189528',  
        specCode: 'demo000',  
        withUsedAmount: false,  
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
            "id": "80209",  
            "coin": "USDT",  
            "amountUnit": "AWARD_AMOUNT_UNIT_USD",  
            "productLine": "PRODUCT_LINE_CONTRACT",  
            "subProductLine": "SUB_PRODUCT_LINE_CONTRACT_DEFAULT",  
            "totalAmount": "10000",  
            "usedAmount": "100"  
        },  
        "retExtInfo": {},  
        "time": 1726107086313  
    }

---

# 查詢代金券參數

### HTTP 請求

POST`/v5/broker/award/info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
id| **true**|  string| 代金券ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 代金券ID  
coin| string| 幣種  
amountUnit| string| 計價單位

  * `AWARD_AMOUNT_UNIT_USD`
  * `AWARD_AMOUNT_UNIT_COIN`

  
productLine| string| 業務線  
subProductLine| string| 子業務線  
totalAmount| Object| 代金券總金額  
usedAmount| string| 代金券已發出金額  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/broker/award/info HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1726107086048  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 22  
      
    {  
        "id": "80209"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_voucher_spec(  
        id="80209",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getBrokerVoucherSpec({  
        accountId: '5714139',  
        awardId: '189528',  
        specCode: 'demo000',  
        withUsedAmount: false,  
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
            "id": "80209",  
            "coin": "USDT",  
            "amountUnit": "AWARD_AMOUNT_UNIT_USD",  
            "productLine": "PRODUCT_LINE_CONTRACT",  
            "subProductLine": "SUB_PRODUCT_LINE_CONTRACT_DEFAULT",  
            "totalAmount": "10000",  
            "usedAmount": "100"  
        },  
        "retExtInfo": {},  
        "time": 1726107086313  
    }