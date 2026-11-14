---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/unified-trans-amnt
api_type: Account
updated_at: 2026-11-13 19:20:57.949266
---

# Get Transferable Amount (Unified)

Query the available amount to transfer of a specific coin in the Unified wallet.

info

Formula of Asset Available Balance for withdraw: 

  1. Reverse calculate Asset Available Amount = X, using `totalAvailableBalance` in [Get Wallet Balance](/docs/v5/account/wallet-balance) and the asset's tiered collateral ratio   

  2. Asset Available Balance for withdraw = min(X, asset withdraw Available balance)


  * under Cross marin mode: asset withdraw Available balance = asset wallet balance + min(unrealised pnl,0) + asset reservation - frozen + negative option value - bonus - Positive Option OrderIM + orderloss   

  * under Portfolio margin mode: asset withdraw Available balance = asset wallet balance + min(unrealised pnl,0) + asset reservation - frozen - max(bonus, Pm spot Hedged Balance) + orderloss + min(optionValue,0)   



  3. During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/account/withdrawal`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coinName| **true**|  string| Coin name, uppercase only. Supports up to 20 coins per request, use comma to separate. `BTC,USDC,USDT,SOL`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
availableWithdrawal| string| Transferable amount for the 1st coin in the request  
availableWithdrawalMap| Object| Transferable amount map for each requested coin. In the map, key is the requested coin, and value is the accordingly amount(string)  
e.g., "availableWithdrawalMap":{"BTC":"4.54549050","SOL":"33.16713007","XRP":"10805.54548970","ETH":"17.76451865"}  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/withdrawal?coinName=BTC,SOL,ETH,XRP HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739861239242  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_transferable_amount(  
        coinName="BTC,SOL,ETH,XRP"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "availableWithdrawal": "4.54549050",  
            "availableWithdrawalMap": {  
                "BTC": "4.54549050",  
                "SOL": "33.16713007",  
                "XRP": "10805.54548970",  
                "ETH": "17.76451865"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1739858984601  
    }

---

# 查詢可劃轉餘額(统一账户)

查詢統一帳戶錢包裡指定幣種的可劃轉餘額

信息

資產可劃轉餘額計算公式：

  1. 使用 [查詢錢包餘額](/docs/zh-TW/v5/account/wallet-balance) `totalAvailableBalance`和該資產階梯質押率，反向計算資產可用金額 = X,  

  2. 資產可劃轉餘額 = min(X, 資產現貨可提現餘額)


  * 在全倉保證金模式下: 資產現貨可提現餘額 = asset wallet balance + min(unrealised pnl,0) + asset reservation - frozen + negative option value - bonus - Positive Option OrderIM + orderloss   

  * 在組合保證金模式下: 資產現貨可提現餘額 = asset wallet balance + min(unrealised pnl,0) + asset reservation - frozen - max(bonus, Pm spot Hedged Balance) + orderloss + min(optionValue,0)   



  3. 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP 請求

GET`/v5/account/withdrawal`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coinName| **true**|  string| 幣種名稱, 僅大寫. 支持最多20個幣種批量查詢, 用逗號分隔. `BTC,SOL,USDT,USDC`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
availableWithdrawal| string| 請求中第一個幣種的可劃轉餘額  
availableWithdrawalMap| Object| 每個請求幣種的可劃轉餘額的對象。在映射中，鍵是請求的幣種，值是相應的金額(字符串)  
例如, "availableWithdrawalMap":{"BTC":"4.54549050","SOL":"33.16713007","XRP":"10805.54548970","ETH":"17.76451865"}  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/withdrawal?coinName=BTC,SOL,ETH,XRP HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739861239242  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "availableWithdrawal": "4.54549050",  
            "availableWithdrawalMap": {  
                "BTC": "4.54549050",  
                "SOL": "33.16713007",  
                "XRP": "10805.54548970",  
                "ETH": "17.76451865"  
            }  
        },  
        "retExtInfo": {},  
        "time": 1739858984601  
    }