---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/private/strategy
api_type: WebSocket
updated_at: 2026-06-28 19:15:48.921370
---

# Wallet

Subscribe to the wallet stream to see changes to your wallet in **real-time**.

info

  * There is no snapshot event given at the time when the subscription is successful
  * The unrealised PnL change does not trigger an event
  * Under the new logic of UTA manual borrow, `spotBorrow` field corresponding to spot liabilities is detailed in the [ announcement](https://announcements.bybit.com/en/article/bybit-uta-function-optimization-manual-coin-borrowing-will-be-launched-soon-blt5d858199bd12e849/).  
Old `walletBalance` = New `walletBalance` \- `spotBorrow`



**Topic:** `wallet`

### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| number| Data created timestamp (ms)  
data| array| Object  
> accountType| string| Account type `UNIFIED`  
> accountIMRate| string| Account IM rate 

  * You can refer to this [Glossary](https://www.bybit.com/en/help-center/article/Glossary-Unified-Trading-Account) to understand the below fields calculation and mearning
  * All account wide fields are **not** applicable to isolated margin

  
> accountMMRate| string| Account MM rate  
> totalEquity| string| Account total equity (USD): ∑Asset Equity By USD value of each asset  
> totalWalletBalance| string| Account wallet balance (USD): ∑Asset Wallet Balance By USD value of each asset  
> totalMarginBalance| string| Account margin balance (USD): totalWalletBalance + totalPerpUPL  
> totalAvailableBalance| string| Account available balance (USD), 

  * Cross Margin: totalMarginBalance - Haircut - totalInitialMargin.
  * Porfolio Margin: total Equity - Haircut - totalInitialMargin 

  
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
>> usdValue| string| USD value of coin. If this coin cannot be collateral, then it is 0  
>> walletBalance| string| Wallet balance of coin  
>> locked| string| Locked balance due to the Spot open order  
>> spotHedgingQty| string| The spot asset qty that is used to hedge in the portfolio margin, truncate to 8 decimals and "0" by default  
>> borrowAmount| string| Borrow amount of coin = spot liabilities + derivatives liabilities  
>> accruedInterest| string| Accrued interest  
>> totalOrderIM| string| Pre-occupied margin for order. For portfolio margin mode, it returns ""  
>> totalPositionIM| string| Sum of initial margin of all positions + Pre-occupied liquidation fee. For portfolio margin mode, it returns ""  
>> totalPositionMM| string| Sum of maintenance margin for all positions. For portfolio margin mode, it returns ""  
>> unrealisedPnl| string| Unrealised P&L  
>> cumRealisedPnl| string| Cumulative Realised P&L  
>> bonus| string| Bonus  
>> collateralSwitch| boolean| Whether it can be used as a margin collateral currency (platform) 

  * When marginCollateral=false, then collateralSwitch is meaningless

  
>> marginCollateral| boolean| Whether the collateral is turned on by user (user) 

  * When marginCollateral=true, then collateralSwitch is meaningful

  
>> colRes| string| Platform level collateral restriction status. `-1`: Unknown. `0`: The restriction is not enabled. `1`: The restriction is not enabled. But the crypto is close to the platform's collateral limit. `2`: The restriction is enabled. Adding collateral, enabling the collateral switch, and switching margin mode will all be rejected. Refer to the [announcement](https://announcements.bybit.com/en/article/platform-collateral-limits-launching-june-2-2026-blt7794f992398fa15f/?category=maintenance_updates) for more details.  
>> spotBorrow| string| Borrow amount by spot margin trade and manual borrow amount(does not include borrow amount by spot margin active order). `spotBorrow` field corresponding to spot liabilities is detailed in the [ announcement](https://announcements.bybit.com/en/article/bybit-uta-function-optimization-manual-coin-borrowing-will-be-launched-soon-blt5d858199bd12e849/).  
>> free| string| **Deprecated** since there is no Spot wallet any more  
>> availableToBorrow| string| **Deprecated** field, always return `""`. Please refer to `availableToBorrow` in the [Get Collateral Info](/docs/v5/account/collateral-info)  
>> availableToWithdraw| string| **Deprecated** for `accountType=UNIFIED` from 9 Jan, 2025 

  * Transferable balance: you can use [Get Transferable Amount (Unified)](/docs/v5/account/unified-trans-amnt) or [Get All Coins Balance](/docs/v5/asset/balance/all-balance) instead
  * Derivatives available balance:   
**isolated margin** : walletBalance - totalPositionIM - totalOrderIM - locked - bonus  
**cross & portfolio margin**: look at field `totalAvailableBalance`(USD), which needs to be converted into the available balance of accordingly coin through index price
  * Spot (margin) available balance: refer to [Get Borrow Quota (Spot)](/docs/v5/order/spot-borrow-quota)

  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "wallet"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="private",  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    def handle_message(message):  
        print(message)  
    ws.wallet_stream(callback=handle_message)  
    while True:  
        sleep(1)  
    

### Stream Example
    
    
    {  
        "id": "592324d2bce751-ad38-48eb-8f42-4671d1fb4d4e",  
        "topic": "wallet",  
        "creationTime": 1700034722104,  
        "data": [  
            {  
                "accountIMRate": "0",  
                "accountIMRateByMp": "0",  
                "accountMMRate": "0",  
                "accountMMRateByMp": "0",  
                "totalEquity": "10262.91335023",  
                "totalWalletBalance": "9684.46297164",  
                "totalMarginBalance": "9684.46297164",  
                "totalAvailableBalance": "9556.6056555",  
                "totalPerpUPL": "0",  
                "totalInitialMargin": "0",  
                "totalInitialMarginByMp": "0",  
                "totalMaintenanceMargin": "0",  
                "totalMaintenanceMarginByMp": "0",  
                "coin": [  
                    {  
                        "coin": "BTC",  
                        "equity": "0.00102964",  
                        "usdValue": "36.70759517",  
                        "walletBalance": "0.00102964",  
                        "availableToWithdraw": "0.00102964",  
                        "availableToBorrow": "",  
                        "borrowAmount": "0",  
                        "accruedInterest": "0",  
                        "totalOrderIM": "",  
                        "totalPositionIM": "",  
                        "totalPositionMM": "",  
                        "unrealisedPnl": "0",  
                        "cumRealisedPnl": "-0.00000973",  
                        "bonus": "0",  
                        "collateralSwitch": true,  
                        "marginCollateral": true,  
                        "locked": "0",  
                        "spotHedgingQty": "0.01592413",  
                        "spotBorrow": "0"  
                    }  
                ],  
                "accountLTV": "0",  
                "accountType": "UNIFIED"  
            }  
        ]  
    }

---

# 錢包

訂閱錢包數據推送

**Topic:** `wallet`

信息

  * 在訂閱成功後不會立馬推送快照數據, 只有當餘額發生變化時, 才會觸發推送
  * 浮動盈虧的變化不會觸發推送



### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息id  
topic| string| Topic名  
creationTime| number| 消息數據創建時間  
data| array| Object  
> accountType| string| 帳戶類型 `UNIFIED`  
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
> coin| array| Object. 幣種列表  
>> coin| string| 幣種名稱，例如 BTC, ETH, USDT, USDC  
>> equity| string| 當前幣種的資產淨值: Asset Equity = Asset Wallet Balance + Asset Perp UPL + Asset Future UPL + Asset Option Value = `walletBalance` \- `spotBorrow` \+ `unrealisedPnl` \+ Asset Option Value  
>> usdValue| string| 當前幣種折算成 usd 的價值, 如果該幣種不能作為保證金的抵押品, 則該數值為0  
>> walletBalance| string| 當前幣種的錢包餘額 = 現貨負債 + 合約浮虧導致借幣產生的借幣負債  
>> locked| string| 現貨掛單凍結金額  
>> spotHedgingQty| string| 用於組合保證金(PM)現貨對衝的數量, 截斷至8為小數, 默認為0  
>> borrowAmount| string| 當前幣種的已用借貸額度  
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

  * 可劃轉餘額: 可以使用[查詢可劃轉餘額(统一账户)](/docs/zh-TW/v5/websocket/v5/account/unified-trans-amnt) 或 [查詢賬戶所有幣種余額](/docs/zh-TW/v5/websocket/v5/asset/balance/all-balance)
  * 合約可用餘額:   
**逐倉** : walletBalance - totalPositionIM - totalOrderIM - locked - bonus  
**全倉/組合保證金** : 使用字段`totalAvailableBalance`(USD), 但需要通過index price来轉換成對應幣種的可用餘額
  * 現貨(槓桿)可用餘額: 可以使用[查詢用戶可用額度 (現貨)](/docs/zh-TW/v5/websocket/v5/order/spot-borrow-quota)

  
>> availableToBorrow| string| **廢棄** , 由於母子共享借貸限額, 總是返回`""`. 請通過[查詢抵押品信息](/docs/zh-TW/v5/websocket/v5/account/collateral-info)接口查詢`availableToBorrow`  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "wallet"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="private",  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    def handle_message(message):  
        print(message)  
    ws.wallet_stream(callback=handle_message)  
    while True:  
        sleep(1)  
    

### 推送示例
    
    
    {  
        "id": "592324d2bce751-ad38-48eb-8f42-4671d1fb4d4e",  
        "topic": "wallet",  
        "creationTime": 1700034722104,  
        "data": [  
            {  
                "accountIMRate": "0",  
                "accountIMRateByMp": "0",  
                "accountMMRate": "0",  
                "accountMMRateByMp": "0",  
                "totalEquity": "10262.91335023",  
                "totalWalletBalance": "9684.46297164",  
                "totalMarginBalance": "9684.46297164",  
                "totalAvailableBalance": "9556.6056555",  
                "totalPerpUPL": "0",  
                "totalInitialMargin": "0",  
                "totalInitialMarginByMp": "0",  
                "totalMaintenanceMargin": "0",  
                "totalMaintenanceMarginByMp": "0",  
                "coin": [  
                    {  
                        "coin": "BTC",  
                        "equity": "0.00102964",  
                        "usdValue": "36.70759517",  
                        "walletBalance": "0.00102964",  
                        "availableToWithdraw": "0.00102964",  
                        "availableToBorrow": "",  
                        "borrowAmount": "0",  
                        "accruedInterest": "0",  
                        "totalOrderIM": "",  
                        "totalPositionIM": "",  
                        "totalPositionMM": "",  
                        "unrealisedPnl": "0",  
                        "cumRealisedPnl": "-0.00000973",  
                        "bonus": "0",  
                        "collateralSwitch": true,  
                        "marginCollateral": true,  
                        "locked": "0",  
                        "spotHedgingQty": "0.01592413"  
                    }  
                ],  
                "accountLTV": "0",  
                "accountType": "UNIFIED"  
            }  
        ]  
    }