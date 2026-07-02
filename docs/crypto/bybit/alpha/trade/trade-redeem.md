---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/trade/trade-redeem
api_type: Trading
updated_at: 2026-07-02 19:15:10.446238
---

# Get Single Coin Balance

Query the balance of a specific coin in a specific [account type](/docs/v5/enum#accounttype). Supports querying sub UID's balance. Also, you can check the transferable amount from master to sub account, sub to master account or sub to sub account, especially for user who has an institutional loan.

important

  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/asset/transfer/query-account-coin-balance`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
memberId| false| string| UID. **Required** when querying sub UID balance with master api key  
toMemberId| false| string| UID. **Required** when querying the transferable balance between different UIDs  
[accountType](/docs/v5/enum#accounttype)| **true**|  string| Account type  
[toAccountType](/docs/v5/enum#accounttype)| false| string| To account type. **Required** when querying the transferable balance between different account types  
coin| **true**|  string| Coin, uppercase only  
withBonus| false| integer| `0`(default): not query bonus. `1`: query bonus  
withTransferSafeAmount| false| integer| Whether query delay withdraw/transfer safe amount 

  * `0`(default): false, `1`: true
  * What is [delay withdraw amount](/docs/v5/asset/balance/delay-amount)?

  
withLtvTransferSafeAmount| false| integer| For OTC loan users in particular, you can check the transferable amount under risk level

  * `0`(default): false, `1`: true
  * `toAccountType` is mandatory

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
accountType| string| Account type  
bizType| integer| Biz type  
accountId| string| Account ID  
memberId| string| Uid  
balance| Object|   
> coin| string| Coin  
> walletBalance| string| Wallet balance  
> transferBalance| string| Transferable balance  
> bonus| string| bonus  
> transferSafeAmount| string| Safe amount to transfer. Keep `""` if not query  
> ltvTransferSafeAmount| string| Transferable amount for ins loan account. Keep `""` if not query  
[](/docs/api-explorer/v5/asset/account-coin-balance)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/query-account-coin-balance?accountType=UNIFIED&coin=USDT&toAccountType=FUND&withLtvTransferSafeAmount=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: xxxxx  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1690254520644  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_coin_balance(  
        accountType="UNIFIED",  
        coin="BTC",  
        memberId=592324,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getCoinBalance({  
        accountType: 'UNIFIED',  
        coin: 'USDT',  
        toAccountType: 'FUND',  
        withLtvTransferSafeAmount: 1,  
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
        "retMsg": "success",  
        "result": {  
            "accountType": "UNIFIED",  
            "bizType": 1,  
            "accountId": "1631385",  
            "memberId": "1631373",  
            "balance": {  
                "coin": "USDT",  
                "walletBalance": "11999",  
                "transferBalance": "11999",  
                "bonus": "0",  
                "transferSafeAmount": "",  
                "ltvTransferSafeAmount": "7602.4861"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1690254521256  
    }

---

# 查詢帳戶單個幣種餘額

獲取某[帳戶類型](/docs/zh-TW/v5/enum#accounttype)下某指定幣種的餘額。支持通過輸入子帳戶id來查詢子帳戶的某個帳戶類型下的某個幣種餘額 同時, 支持查詢母子帳戶、子子帳戶、子母帳戶之間的可劃轉金額，特別是針對於擁有機構借貸的用戶。

信息

  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP 請求

GET`/v5/asset/transfer/query-account-coin-balance`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
memberId| false| string| 用戶Id. 當查詢子帳號的餘額時，該字段**必傳**  
toMemberId| false| string| 劃入帳戶UID. 當查詢不同uid間劃轉時, 該字段**必傳**  
[accountType](/docs/zh-TW/v5/enum#accounttype)| **true**|  string| 帳戶類型  
[toAccountType](/docs/zh-TW/v5/enum#accounttype)| false| string| 劃入帳戶類型. 當查詢不同帳戶類型間的劃轉時, 該字段**必傳**  
coin| **true**|  string| 幣種  
withBonus| false| integer| 是否查詢體驗金. `0`(默認): 不查詢,`1`: 查詢.  
withTransferSafeAmount| false| integer| 是否查詢延遲提幣安全限額 

  * `0`(默認)：否, `1`：是
  * 什麼是[延遲提幣](/docs/zh-TW/v5/asset/balance/delay-amount)?

  
withLtvTransferSafeAmount| false| integer| 特別用於機構借貸用戶, 可以查詢風險水平內的可劃轉餘額

  * `0`(default)：false, `1`：true
  * 此時`toAccountType`字段**必傳**

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
accountType| string| 賬戶類型  
bizType| integer| 帳戶業務子類型  
accountId| string| 賬戶ID  
memberId| string| 用戶ID  
balance| Object|   
> coin| string| 幣種類型  
> walletBalance| string| 錢包余額  
> transferBalance| string| 可划余額  
> bonus| string| 可用金額中包含的体验金  
> transferSafeAmount| string| 可劃轉的安全限額. 若不查詢，則返回`""`  
> ltvTransferSafeAmount| string| 機構借貸用戶的可劃轉餘額. 若不查詢，則返回`""`  
[](/docs/zh-TW/api-explorer/v5/asset/account-coin-balance)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/asset/transfer/query-account-coin-balance?accountType=UNIFIED&coin=USDT&toAccountType=FUND&withLtvTransferSafeAmount=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: xxxxx  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1690254520644  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_coin_balance(  
        accountType="UNIFIED",  
        coin="BTC",  
        memberId=592324,  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getCoinBalance({  
        accountType: 'UNIFIED',  
        coin: 'USDT',  
        toAccountType: 'FUND',  
        withLtvTransferSafeAmount: 1,  
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
        "retMsg": "success",  
        "result": {  
            "accountType": "UNIFIED",  
            "bizType": 1,  
            "accountId": "1631385",  
            "memberId": "1631373",  
            "balance": {  
                "coin": "USDT",  
                "walletBalance": "11999",  
                "transferBalance": "11999",  
                "bonus": "0",  
                "transferSafeAmount": "",  
                "ltvTransferSafeAmount": "7602.4861"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1690254521256  
    }