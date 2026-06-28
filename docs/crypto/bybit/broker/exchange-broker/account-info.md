---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/broker/exchange-broker/account-info
api_type: REST
updated_at: 2026-05-27 19:16:01.063654
---

# Get Account Info

info

  * Use exchange broker master account to query



> API rate limit: 10 req / sec

### HTTP Request

GET`/v5/broker/account-info`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
subAcctQty| string| The qty of sub account has been created  
maxSubAcctQty| string| The max limit of sub account can be created  
baseFeeRebateRate| Object| Rebate percentage of the base fee  
> spot| string| Rebate percentage of the base fee for spot, e.g., 10.00%  
> derivatives| string| Rebate percentage of the base fee for derivatives, e.g., 10.00%  
markupFeeRebateRate| Object| Rebate percentage of the mark up fee  
> spot| string| Rebate percentage of the mark up fee for spot, e.g., 10.00%  
> derivatives| string| Rebate percentage of the mark up fee for derivatives, e.g., 10.00%  
> convert| string| Rebate percentage of the mark up fee for convert, e.g., 10.00%  
ts| string| System timestamp (ms)  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/broker/account-info HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1701399431920  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_exchange_broker_account_info())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getExchangeBrokerAccountInfo()  
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
            "subAcctQty": "2",  
            "maxSubAcctQty": "20",  
            "baseFeeRebateRate": {  
                "spot": "10.0%",  
                "derivatives": "10.0%"  
            },  
            "markupFeeRebateRate": {  
                "spot": "6.00%",  
                "derivatives": "9.00%",  
                "convert": "3.00%",  
            },  
            "ts": "1701395633402"  
        },  
        "retExtInfo": {},  
        "time": 1701395633403  
    }

---

# 查詢帳戶信息

信息

  * 使用經紀商的母帳戶進行查詢



> API頻率: 10次/秒

### HTTP 請求

GET`/v5/broker/account-info`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
subAcctQty| string| 已創建的子帳戶數量  
maxSubAcctQty| string| 允許創建的子帳戶數量上限  
baseFeeRebateRate| Object| 基礎費率返佣  
> spot| string| 現貨交易基礎費率返佣, 例如, 10.00%  
> derivatives| string| 期貨交易基礎費率返佣, 例如, 10.00%  
markupFeeRebateRate| Object| 加點費率返佣  
> spot| string| 現貨交易加點費率返佣, 例如, 10.00%  
> derivatives| string| 期貨交易加點費率返佣, 例如, 10.00%  
> convert| string| 閃兌加點費率返佣, 例如, 10.00%  
ts| string| 系統時間戳 (毫秒)  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/broker/account-info HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1701399431920  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_exchange_broker_account_info())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getExchangeBrokerAccountInfo()  
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
            "subAcctQty": "2",  
            "maxSubAcctQty": "20",  
            "baseFeeRebateRate": {  
                "spot": "10.0%",  
                "derivatives": "10.0%"  
            },  
            "markupFeeRebateRate": {  
                "spot": "6.00%",  
                "derivatives": "9.00%",  
                "convert": "3.00%"  
            },  
            "ts": "1701395633402"  
        },  
        "retExtInfo": {},  
        "time": 1701395633403  
    }