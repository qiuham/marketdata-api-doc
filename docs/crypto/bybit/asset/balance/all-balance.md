---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/balance/all-balance
api_type: REST
updated_at: 2026-11-13 19:21:27.288351
---

# Get All Coins Balance

You could get all coin balance of all account types under the master account, and sub account.

important

  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/asset/transfer/query-account-coins-balance`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
memberId| false| string| User Id. It is **required** when you use master api key to check sub account coin balance  
[accountType](/docs/v5/enum#accounttype)| **true**|  string| Account type  
coin| false| string| Coin name, uppercase only 

  * Query all coins if not passed
  * Can query multiple coins, separated by comma. `USDT,USDC,ETH`

**Note:** this field is **mandatory** for accountType=`UNIFIED`, and supports up to 10 coins each request  
withBonus| false| integer| `0`(default): not query bonus. `1`: query bonus  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[accountType](/docs/v5/enum#accounttype)| string| Account type  
memberId| string| UserID  
balance| array| Object  
> coin| string| Currency  
> walletBalance| string| Wallet balance  
> transferBalance| string| Transferable balance  
> bonus| string| Bonus  
[](/docs/api-explorer/v5/asset/all-balance)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/query-account-coins-balance?accountType=FUND&coin=USDC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675866354698  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_coins_balance(  
        accountType="FUND",  
        coin="USDC",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getAllCoinsBalance({ accountType: 'FUND', coin: 'USDC' })  
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
            "memberId": "XXXX",  
            "accountType": "FUND",  
            "balance": [  
                {  
                    "coin": "USDC",  
                    "transferBalance": "0",  
                    "walletBalance": "0",  
                    "bonus": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1675866354913  
    }

---

# 查詢賬戶所有幣種余額

支持查詢母帳戶的各個帳戶類型的幣種餘額，以及母帳戶下各子帳戶的各個帳戶類型的幣種餘額。

important

  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP 請求

GET`/v5/asset/transfer/query-account-coins-balance`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
memberId| false| string| 用戶ID. 當使用母帳號api key查詢子帳戶的幣種餘額時，該字段**必傳**  
[accountType](/docs/zh-TW/v5/enum#accounttype)| **true**|  string| 賬戶類型  
coin| false| string| 幣種類型, 支持傳入多個幣種   
**注意:** 對於accountType=UNIFIED, coin參數是**必傳** 字段, 並且最多支持單次查詢10個幣種  
withBonus| false| integer| 是否查詢體驗金. `0`(默認)：不查詢; `1`：查詢  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
[accountType](/docs/zh-TW/v5/enum#accounttype)| string| 賬戶類型  
memberId| string| 用戶ID  
balance| Object|   
> coin| string| 幣種類型  
> walletBalance| string| 錢包余額  
> transferBalance| string| 可划余額  
> bonus| string| 体验金  
[](/docs/zh-TW/api-explorer/v5/asset/all-balance)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/query-account-coins-balance?accountType=FUND&coin=USDC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675866354698  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_coins_balance(  
        accountType="FUND",  
        coin="USDC",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getAllCoinsBalance({ accountType: 'FUND', coin: 'USDC' })  
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
            "memberId": "533285",  
            "accountType": "FUND",  
            "balance": [  
                {  
                    "coin": "USDT",  
                    "transferBalance": "1010",  
                    "walletBalance": "1010",  
                    "bonus": ""  
                },  
                {  
                    "coin": "USDC",  
                    "transferBalance": "0",  
                    "walletBalance": "0",  
                    "bonus": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1675865290069  
    }