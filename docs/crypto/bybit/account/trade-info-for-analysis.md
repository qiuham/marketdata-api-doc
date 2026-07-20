---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/trade-info-for-analysis
api_type: Account
updated_at: 2026-07-20 19:06:26.622817
---

# Get Wallet Balance

Obtain wallet balance, query asset information of each currency. By default, currency information with assets or liabilities of 0 is not returned.

info

  * Under the new logic of UTA manual borrow, `spotBorrow` field corresponding to spot liabilities is detailed in the [ announcement](https://announcements.bybit.com/en/article/bybit-uta-function-optimization-manual-coin-borrowing-will-be-launched-soon-blt5d858199bd12e849/).  

  * Old `walletBalance` = New `walletBalance` \- `spotBorrow`
  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/account/wallet-balance`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[accountType](/docs/v5/enum#accounttype)| **true**|  string| Account type `UNIFIED`. To get Funding wallet balance, please go to this [endpoint](/docs/v5/asset/balance/all-balance)  
coin| false| string| Coin name, uppercase only 

  * If not passed, it returns non-zero asset info
  * You can pass multiple coins to query, separated by comma. `USDT,USDC`

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> accountType| string| Account type  
> accountIMRate| string| Account IM rate 

  * You can refer to this [Glossary](https://www.bybit.com/en/help-center/article/Glossary-Unified-Trading-Account) to understand the below fields calculation and mearning
  * All account wide fields are **not** applicable to isolated margin

  
> accountMMRate| string| Account MM rate  
> totalEquity| string| Account total equity (USD): ∑Asset Equity By USD value of each asset  
> totalWalletBalance| string| Account wallet balance (USD): ∑Asset Wallet Balance By USD value of each asset  
> totalMarginBalance| string| Account margin balance (USD): totalWalletBalance + totalPerpUPL  
> totalAvailableBalance| string| Account available balance (USD), 

  * Cross Margin: totalMarginBalance - Haircut - totalInitialMargin.
  * Porfolio Margin: total Equity - Haircut - totalInitialMargin. 

  
> totalPerpUPL| string| Account Perps and Futures unrealised p&l (USD): ∑Each Perp and USDC Futures upl by base coin  
> totalInitialMargin| string| Account initial margin (USD): ∑Asset Total Initial Margin Base Coin  
> totalMaintenanceMargin| string| Account maintenance margin (USD): ∑ Asset Total Maintenance Margin Base Coin  
> accountIMRateByMp| string| You can **ignore** this field, and refer to `accountIMRate`, which has the same calculation  
> accountMMRateByMp| string| You can **ignore** this field, and refer to `accountMMRate`, which has the same calculation  
> totalInitialMarginByMp| string| You can **ignore** this field, and refer to `totalInitialMargin`, which has the same calculation  
> totalMaintenanceMarginByMp| string| You can **ignore** this field, and refer to `totalMaintenanceMargin`, which has the same calculation  
> accountLTV| string| **Deprecated** field  
> coin| array| Object  
>> coin| string| Coin name, such as BTC, ETH, USDT, USDC  
>> equity| string| Equity of coin. Asset Equity = Asset Wallet Balance + Asset Perp UPL + Asset Future UPL + Asset Option Value = `walletBalance` \- `spotBorrow` \+ `unrealisedPnl` \+ Asset Option Value  
>> usdValue| string| USD value of coin  
>> walletBalance| string| Wallet balance of coin  
>> locked| string| Locked balance due to the Spot open order  
>> spotHedgingQty| string| The spot asset qty that is used to hedge in the portfolio margin, truncate to 8 decimals and "0" by default  
>> borrowAmount| string| Borrow amount of current coin = spot liabilities + derivatives liabilities  
>> accruedInterest| string| Accrued interest  
>> totalOrderIM| string| Pre-occupied margin for order. For portfolio margin mode, it returns ""  
>> totalPositionIM| string| Sum of initial margin of all positions + Pre-occupied liquidation fee. For portfolio margin mode, it returns ""  
>> totalPositionMM| string| Sum of maintenance margin for all positions. For portfolio margin mode, it returns ""  
>> unrealisedPnl| string| Unrealised P&L  
>> cumRealisedPnl| string| Cumulative Realised P&L  
>> bonus| string| Bonus  
>> marginCollateral| boolean| Whether it can be used as a margin collateral currency (platform), `true`: YES, `false`: NO 

  * When marginCollateral=false, then collateralSwitch is meaningless

  
>> collateralSwitch| boolean| Whether the collateral is turned on by user (user), `true`: ON, `false`: OFF 

  * When marginCollateral=true, then collateralSwitch is meaningful

  
>> colRes| string| Platform level collateral restriction status. `-1`: Unknown. `0`: The restriction is not enabled. `1`: The restriction is not enabled. But the crypto is close to the platform's collateral limit. `2`: The restriction is enabled. Adding collateral, enabling the collateral switch, and switching margin mode will all be rejected. Refer to the [announcement](https://announcements.bybit.com/en/article/platform-collateral-limits-launching-june-2-2026-blt7794f992398fa15f/?category=maintenance_updates) for more details.  
>> spotBorrow| string| Borrow amount by spot margin trade and manual borrow amount (does not include borrow amount by spot margin active order). `spotBorrow` field corresponding to spot liabilities is detailed in the [ announcement](https://announcements.bybit.com/en/article/bybit-uta-function-optimization-manual-coin-borrowing-will-be-launched-soon-blt5d858199bd12e849/).  
>> free| string| **Deprecated** since there is no Spot wallet any more  
>> availableToWithdraw| string| **Deprecated** for `accountType=UNIFIED` from 9 Jan, 2025 

  * Transferable balance: you can use [Get Transferable Amount (Unified)](/docs/v5/account/unified-trans-amnt) or [Get All Coins Balance](/docs/v5/asset/balance/all-balance) instead
  * Derivatives available balance:   
**isolated margin** : walletBalance - totalPositionIM - totalOrderIM - locked - bonus  
**cross & portfolio margin**: look at field `totalAvailableBalance`(USD), which needs to be converted into the available balance of accordingly coin through index price
  * Spot (margin) available balance: refer to [Get Borrow Quota (Spot)](/docs/v5/order/spot-borrow-quota)

  
>> availableToBorrow| string| **Deprecated** field, always return `""`. Please refer to `availableToBorrow` in the [Get Collateral Info](/docs/v5/account/collateral-info)  
[](/docs/api-explorer/v5/account/wallet)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/wallet-balance?accountType=UNIFIED&coin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672125440406  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_wallet_balance(  
        accountType="UNIFIED",  
        coin="BTC",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
        const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getWalletBalance({  
            accountType: 'UNIFIED',  
            coin: 'BTC',  
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
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "totalEquity": "3.31216591",  
                    "accountIMRate": "0",  
                    "accountIMRateByMp": "0",  
                    "totalMarginBalance": "3.00326056",  
                    "totalInitialMargin": "0",  
                    "totalInitialMarginByMp": "0",  
                    "accountType": "UNIFIED",  
                    "totalAvailableBalance": "3.00326056",  
                    "accountMMRate": "0",  
                    "accountMMRateByMp": "0",  
                    "totalPerpUPL": "0",  
                    "totalWalletBalance": "3.00326056",  
                    "accountLTV": "0",  
                    "totalMaintenanceMargin": "0",  
                    "totalMaintenanceMarginByMp": "0",  
                    "coin": [  
                        {  
                            "availableToBorrow": "3",  
                            "bonus": "0",  
                            "accruedInterest": "0",  
                            "availableToWithdraw": "0",  
                            "totalOrderIM": "0",  
                            "equity": "0",  
                            "totalPositionMM": "0",  
                            "usdValue": "0",  
                            "spotHedgingQty": "0.01592413",  
                            "unrealisedPnl": "0",  
                            "collateralSwitch": true,  
                            "borrowAmount": "0.0",  
                            "totalPositionIM": "0",  
                            "walletBalance": "0",  
                            "cumRealisedPnl": "0",  
                            "locked": "0",  
                            "marginCollateral": true,  
                            "coin": "BTC",  
                            "spotBorrow": "0"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1690872862481  
    }

---

# 查詢錢包餘額

獲取統一帳戶錢包餘額, 查詢各個幣種的資產信息. 默認不返回資產或負債為0的幣種信息。

信息

  * 在UTA手動借貸新邏輯下，現貨負債對應的`spotBorrow`, 請詳見[公告](https://announcements.bybit.com/en/article/bybit-uta-function-optimization-manual-coin-borrowing-will-be-launched-soon-blt5d858199bd12e849/).
  * 舊 `walletBalance` = 新 `walletBalance` \- `spotBorrow`
  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP 請求

GET`/v5/account/wallet-balance`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[accountType](/docs/zh-TW/v5/enum#accounttype)| **true**|  string| 帳戶類型 `UNIFIED`

  * 要查詢資金帳戶餘額, 可以使用這個[接口](/docs/zh-TW/v5/asset/balance/all-balance)

  
coin| false| string| 幣種名稱 

  * 不傳則返回非零資產信息
  * 可以傳多個幣進行查詢，以逗號分隔, `USDT,USDC`

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> accountType| string| 帳戶類型  
> accountIMRate| string| 帳戶初始保證金率 

  * 您可以參考該[鏈結](https://www.bybit.com/en/help-center/article/Glossary-Unified-Trading-Account)了解統一帳戶下字段含義和計算方式
  * 下面所有帳戶維度的字段都不適用於逐倉模式

  
> accountMMRate| string| 帳戶維持保證金率  
> totalEquity| string| 總凈值為賬戶中每個幣種資產凈值的法幣估值之和 (USD): ∑Asset Equity By USD value of each asset  
> totalWalletBalance| string| 賬戶維度換算成usd的錢包餘額: ∑Asset Wallet Balance By USD value of each asset  
> totalMarginBalance| string| 賬戶維度換算成usd的保證金餘額: totalWalletBalance + totalPerpUPL  
> totalAvailableBalance| string| 賬戶維度換算成usd的可用餘額: 

  * 全倉保證金: totalMarginBalance - Haircut - totalInitialMargin.
  * 組合保證金: total Equity - Haircut - totalInitialMargin 

  
> totalPerpUPL| string| 賬戶維度換算成usd的永續和USDC交割合約的浮動盈虧: ∑Each perp and USDC Futures upl by base coin  
> totalInitialMargin| string| 賬戶維度換算成usd的總初始保證金: ∑Asset Total Initial Margin Base Coin  
> totalMaintenanceMargin| string| 賬戶維度換算成usd的總維持保證金: ∑Asset Total Maintenance Margin Base Coin  
> accountIMRateByMp| string| 可**忽略** , 可以使用`accountIMRate`, 算法和值保持一致  
> accountMMRateByMp| string| 可**忽略** , 可以使用`accountMMRate`, 算法和值保持一致  
> totalInitialMarginByMp| string| 可**忽略** , 可以使用`totalInitialMargin`, 算法和值保持一致  
> totalMaintenanceMarginByMp| string| 可**忽略** , 可以使用`totalMaintenanceMargin`, 算法和值保持一致  
> accountLTV| string| **廢棄** 字段  
> coin| arrays| 幣種列表  
>> coin| string| 幣種名稱，例如 BTC, ETH, USDT, USDC  
>> equity| string| 當前幣種的資產淨值. Asset Equity = Asset Wallet Balance + Asset Perp UPL + Asset Future UPL + Asset Option Value = `walletBalance` \- `spotBorrow` \+ `unrealisedPnl` \+ Asset Option Value  
>> usdValue| string| 當前幣種折算成 usd 的價值  
>> walletBalance| string| 當前幣種的錢包餘額  
>> locked| string| 現貨掛單凍結金額  
>> spotHedgingQty| string| 用於組合保證金(PM)現貨對衝的數量, 截斷至8為小數, 默認為0  
>> borrowAmount| string| 當前幣種的已用借貸額度 = 現貨負債 + 合約浮虧導致借幣產生的借幣負債  
>> accruedInterest| string| 當前幣種的預計要在下一個利息週期收取的利息金額  
>> totalOrderIM| string| 以當前幣種結算的訂單委託預佔用保證金. 組合保證金模式下，該字段返回空字符串  
>> totalPositionIM| string| 以當前幣種結算的所有倉位起始保證金求和 + 所有倉位的預佔用平倉手續費. 組合保證金模式下，該字段返回空字符串  
>> totalPositionMM| string| 以當前幣種結算的所有倉位維持保證金求和. 組合保證金模式下，該字段返回空字符串  
>> unrealisedPnl| string| 以當前幣種結算的所有倉位的未結盈虧之和  
>> cumRealisedPnl| string| 以當前幣種結算的所有倉位的累計已結盈虧之和  
>> bonus| string| 體驗金  
>> marginCollateral| boolean| 是否可作為保證金抵押幣種(平台維度), `true`: 是. `false`: 否 

  * 當marginCollateral=false時, 則collateralSwitch無意義

  
>> collateralSwitch| boolean| 用戶是否開啟保證金幣種抵押(用戶維度), `true`: 是. `false`: 否 

  * 僅當marginCollateral=true時, 才能主動選擇開關抵押

  
>> colRes| string| 平台層面的抵押品限制狀態。`-1`: 未知。`0`: 未啟用限制。`1`: 未啟用限制，但該幣種已接近平台抵押上限。`2`: 已啟用限制，增加抵押品、開啟抵押開關及切換保證金模式的操作均將被拒絕。詳見[公告](https://announcements.bybit.com/en/article/platform-collateral-limits-launching-june-2-2026-blt7794f992398fa15f/?category=maintenance_updates)。  
>> spotBorrow| string| 現貨槓桿交易借入金額以及手工借貸金額（不包含現貨槓桿活躍訂單借入金額）。現貨負債對應的`spotBorrow`, 請詳見[公告](https://announcements.bybit.com/en/article/bybit-uta-function-optimization-manual-coin-borrowing-will-be-launched-soon-blt5d858199bd12e849/).  
>> free| string| **廢棄** , 不再有現貨錢包  
>> availableToWithdraw| string| 該字段從2025年1月9日起已經**廢棄**

  * 可劃轉餘額: 可以使用[查詢可劃轉餘額(统一账户)](/docs/zh-TW/v5/account/unified-trans-amnt) 或 [查詢賬戶所有幣種余額](/docs/zh-TW/v5/asset/balance/all-balance)
  * 合約可用餘額:   
**逐倉** : walletBalance - totalPositionIM - totalOrderIM - locked - bonus  
**全倉/組合保證金** : 使用字段`totalAvailableBalance`(USD), 但需要通過index price来轉換成對應幣種的可用餘額
  * 現貨(槓桿)可用餘額: 可以使用[查詢用戶可用額度 (現貨)](/docs/zh-TW/v5/order/spot-borrow-quota)

  
>> availableToBorrow| string| **廢棄** , 由於母子共享借貸限額, 總是返回`""`. 請通過[查詢抵押品信息](/docs/zh-TW/v5/account/collateral-info)接口查詢`availableToBorrow`  
[](/docs/zh-TW/api-explorer/v5/account/wallet)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/wallet-balance?accountType=UNIFIED&coin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672125440406  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_wallet_balance(  
        accountType="UNIFIED",  
        coin="BTC",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
        const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getWalletBalance({  
            accountType: 'UNIFIED',  
            coin: 'BTC',  
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
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "totalEquity": "18070.32797922",  
                    "accountIMRate": "0.0101",  
                    "accountIMRateByMp": "0.0101",  
                    "totalMarginBalance": "18070.32797922",  
                    "totalInitialMargin": "182.60183684",  
                    "totalInitialMarginByMp": "182.60183684",  
                    "accountType": "UNIFIED",  
                    "totalAvailableBalance": "17887.72614237",  
                    "accountMMRate": "0",  
                    "accountMMRateByMp": "0",  
                    "totalPerpUPL": "-0.11001349",  
                    "totalWalletBalance": "18070.43799271",  
                    "accountLTV": "0.017",  
                    "totalMaintenanceMargin": "0.38106773",  
                    "totalMaintenanceMarginByMp": "0.38106773",  
                    "coin": [  
                        {  
                            "availableToBorrow": "3",  
                            "bonus": "0",  
                            "accruedInterest": "0",  
                            "availableToWithdraw": "0",  
                            "totalOrderIM": "0",  
                            "equity": "0",  
                            "totalPositionMM": "0",  
                            "usdValue": "0",  
                            "spotHedgingQty": "0.01592413",  
                            "unrealisedPnl": "0",  
                            "collateralSwitch": true,  
                            "borrowAmount": "0.0",  
                            "totalPositionIM": "0",  
                            "walletBalance": "0",  
                            "cumRealisedPnl": "0",  
                            "locked": "0",  
                            "marginCollateral": true,  
                            "coin": "BTC",  
                            "spotBorrow": "0"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672125441042  
    }