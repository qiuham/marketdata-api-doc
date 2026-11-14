---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/collateral-info
api_type: Account
updated_at: 2026-11-13 19:20:45.443495
---

# Get Collateral Info

Get the collateral information of the current unified margin account, including loan interest rate, loanable amount, collateral conversion rate, whether it can be mortgaged as margin, etc.

### HTTP Request

GET`/v5/account/collateral-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| Asset currency of all current collateral, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> currency| string| Currency of all current collateral  
> hourlyBorrowRate| string| Hourly borrow rate  
> maxBorrowingAmount| string| Max borrow amount. This value is shared across main-sub UIDs  
> freeBorrowingLimit| string| The maximum limit for interest-free borrowing 

  * Only the borrowing caused by contracts unrealised loss has interest-free amount
  * Spot margin borrowing always has interest

  
> freeBorrowAmount| string| The amount of borrowing within your total borrowing amount that is exempt from interest charges  
> borrowAmount| string| Borrow amount  
> otherBorrowAmount| string| The sum of borrowing amount for other accounts under the same main account  
> availableToBorrow| string| Available amount to borrow. This value is shared across main-sub UIDs  
> borrowable| boolean| Whether currency can be borrowed  
> borrowUsageRate| string| Borrow usage rate: sum of main & sub accounts borrowAmount/maxBorrowingAmount, it is an actual value, 0.5 means 50%  
> marginCollateral| boolean| Whether it can be used as a margin collateral currency (platform), `true`: YES, `false`: NO 

  * When marginCollateral=false, then collateralSwitch is meaningless

  
> collateralSwitch| boolean| Whether the collateral is turned on by user (user), `true`: ON, `false`: OFF 

  * When marginCollateral=true, then collateralSwitch is meaningful

  
> collateralRatio| string| **Deprecated** field. Due to the new Tiered Collateral value logic, this field will no longer be accurate starting on February 19, 2025. Please refer to [Get Tiered Collateral Ratio](/docs/v5/spot-margin-uta/tier-collateral-ratio)  
> freeBorrowingAmount| string| **Deprecated** field, always return `""`, please refer to `freeBorrowingLimit`  
[](/docs/api-explorer/v5/account/collateral-info)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/collateral-info?currency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672127952719  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_collateral_info(  
        currency="BTC",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getCollateralInfo('BTC')  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "availableToBorrow": "3",  
                    "freeBorrowingAmount": "",  
                    "freeBorrowAmount": "0",  
                    "maxBorrowingAmount": "3",  
                    "hourlyBorrowRate": "0.00000147",  
                    "borrowUsageRate": "0",  
                    "collateralSwitch": true,  
                    "borrowAmount": "0",  
                    "borrowable": true,  
                    "currency": "BTC",  
                    "otherBorrowAmount": "0",  
                    "marginCollateral": true,  
                    "freeBorrowingLimit": "0",  
                    "collateralRatio": "0.95"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1691565901952  
    }

---

# 查詢抵押品信息

獲取當前統一保證金賬戶的抵押品信息，包括借貸利率，可藉貸金額以及抵押品折算率，是否可抵押作為保證金等信息

### HTTP 請求

GET`/v5/account/collateral-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| 目前所有抵押品的資產幣種  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> currency| string| 目前所有抵押品的資產幣種  
> hourlyBorrowRate| string| 每小時藉款利率  
> maxBorrowingAmount| string| 最大可藉貸額度. 該值由母子帳號共享  
> freeBorrowingLimit| string| 免息借款額上限 

  * 僅合約浮虧時產生的借款擁有免息額度
  * 槓桿交易的借貸總是產生利息

  
> freeBorrowAmount| string| 借款總額中免息部分的借款金額  
> borrowAmount| string| 已用借貸額度  
> otherBorrowAmount| string| 其他帳戶的已借貸總額(同一個母帳戶下)  
> availableToBorrow| string| 用戶剩餘可藉額度. 該值由母子帳號共享  
> borrowable| boolean| 是否是可藉貸的幣種, `true`: 是. `false`: 否  
> borrowUsageRate| string| 借貸資金使用率: 母子帳戶加起來的borrowAmount/maxBorrowingAmount. 這是一個真實值, 0.5则表示50%  
> marginCollateral| boolean| 是否可作為保證金抵押幣種(平台維度), `true`: 是. `false`: 否 

  * 當marginCollateral=false時, 則collateralSwitch無意義

  
> collateralSwitch| boolean| 用戶是否開啟保證金幣種抵押(用戶維度), `true`: 是. `false`: 否 

  * 僅當marginCollateral=true時, 才能主動選擇開關抵押

  
> freeBorrowingAmount| string| **廢棄** 字段, 總是返回空字符串, 請參考`freeBorrowingLimit`  
> collateralRatio| string| **廢棄** 字段, 由於新的階梯價值率邏輯, 該字段從2025年2月19日開始不再準確。請使用[查詢階梯價值率](/docs/zh-TW/v5/spot-margin-uta/tier-collateral-ratio)  
[](/docs/zh-TW/api-explorer/v5/account/collateral-info)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/collateral-info?currency=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672127952719  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_collateral_info(  
        currency="BTC",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getCollateralInfo('BTC')  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "availableToBorrow": "3",  
                    "freeBorrowingAmount": "",  
                    "freeBorrowAmount": "0",  
                    "maxBorrowingAmount": "3",  
                    "hourlyBorrowRate": "0.00000147",  
                    "borrowUsageRate": "0",  
                    "collateralSwitch": true,  
                    "borrowAmount": "0",  
                    "borrowable": true,  
                    "currency": "BTC",  
                    "otherBorrowAmount": "0",  
                    "marginCollateral": true,  
                    "freeBorrowingLimit": "0",  
                    "collateralRatio": "0.95"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1691565901952  
    }