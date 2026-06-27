---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/fixed-saving/redeem
api_type: REST
updated_at: 2026-05-27 19:17:38.542167
---

# Get Airdrop Products

info

Does not need authentication. Guest access is supported. Authenticated users receive a product list filtered based on account eligibility.

### HTTP Request

GET`/v5/earn/hold-to-earn/product`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
products| array| Object  
> coinName| string| Investment coin name, e.g., `"USDE"`, `"USDTB"`, `"USD1"`  
> yields| array| Yield coin object, e.g., `"USDE"`, `"WLFI"`. May differ from `coinName` for cross-coin airdrops (e.g., USD1 holdings → WLFI rewards)  
>> coinName| string| Yield coin name  
>> apy| string| Yesterday's APR, formatted for direct display, e.g., `"10%"`, `"3.5%"`. Returns `"0%"` when no yield was distributed yesterday for the yield coin  
> status| string| Product stage, `NotStarted`, `Online`, `Ended`  
> apy| string| Yesterday's avg APR cross all yield coins, formatted for direct display, e.g., `"10%"`, `"3.5%"`. Returns `"0%"` when no yield was distributed yesterday  
> announcementUrl| string| Activity rules announcement URL  
  
info

  * Products are filtered by compliance rules, region (EEA), Islamic account status, whitelist membership, and product status. Only products the current user is eligible to participate in are returned.
  * When `coinName != yields.coinName`, it is a cross-coin airdrop
  * Results are sorted by product creation time, newest first.



* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/hold-to-earn/product HTTP/1.1  
    Host: api.bybit.com  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "products": [  
                {  
                    "coinName": "USDE",  
                    "yields": [  
                        {  
                            "coinName": "USDE",  
                            "apy": "0.210604%"  
                        }  
                    ],  
                    "status": "Online",  
                    "announcementUrl": "https://testnet.bybit.com/en/earn/usde-page",  
                    "apy": "0.210604%"  
                },  
                {  
                    "coinName": "USDTB",  
                    "yields": [  
                        {  
                            "coinName": "USDTB",  
                            "apy": "0.029978%"  
                        }  
                    ],  
                    "status": "Online",  
                    "announcementUrl": "https://testnet.bybit.com/en/earn/usdtb-page",  
                    "apy": "0.029978%"  
                },  
                {  
                    "coinName": "USD1",  
                    "yields": [  
                        {  
                            "coinName": "WLFI",  
                            "apy": "10%"  
                        }  
                    ],  
                    "status": "Ended",  
                    "announcementUrl": "https://testnet.bybit.com/en/earn/usd1-page",  
                    "apy": "10%"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1779348459085  
    }

---

# 獲取空投產品列表

信息

不需要鑑權。支援訪客存取，已登入用戶將根據帳戶資格獲得過濾後的產品列表。

### HTTP 請求

GET`/v5/earn/hold-to-earn/product`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
products| array| Object  
> coinName| string| **投資幣種** 名稱，如 `"USDE"`、`"USDTB"`、`"USD1"`。跨幣種空投時可與 `coinName` 不同（例如 USD1 持倉 → WLFI 獎勵）  
> yields| string| **收益幣種** 明細  
>> coinName| string| 收益幣種  
>> apy| string| 該收益幣種**昨日 APR** ，已格式化為可直接展示的文案，如 `"10%"`、`"3.5%"`  
> status| string| 產品當前階段，`NotStarted`, `Online`, `Ended`  
> apy| string| **昨日綜合APR** ，昨日無收益時返回 `"0%"`  
> announcementUrl| string| **活動規則連結** （公告頁 URL）  
  
信息

  * 產品列表經過合規規則、地區（EEA）、伊斯蘭帳戶、灰度名單及產品狀態多重過濾，僅返回當前用戶可見且可參與的產品。
  * 當 `coinName != yields.coinName` 時，為跨幣種空投，前端需同時展示投資幣與收益幣。
  * 結果按產品創建時間倒序排列（較新在前）。



* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/hold-to-earn/product HTTP/1.1  
    Host: api.bybit.com  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "products": [  
                {  
                    "coinName": "USDE",  
                    "yields": [  
                        {  
                            "coinName": "USDE",  
                            "apy": "0.210604%"  
                        }  
                    ],  
                    "status": "Online",  
                    "announcementUrl": "https://testnet.bybit.com/en/earn/usde-page",  
                    "apy": "0.210604%"  
                },  
                {  
                    "coinName": "USDTB",  
                    "yields": [  
                        {  
                            "coinName": "USDTB",  
                            "apy": "0.029978%"  
                        }  
                    ],  
                    "status": "Online",  
                    "announcementUrl": "https://testnet.bybit.com/en/earn/usdtb-page",  
                    "apy": "0.029978%"  
                },  
                {  
                    "coinName": "USD1",  
                    "yields": [  
                        {  
                            "coinName": "WLFI",  
                            "apy": "10%"  
                        }  
                    ],  
                    "status": "Ended",  
                    "announcementUrl": "https://testnet.bybit.com/en/earn/usd1-page",  
                    "apy": "10%"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1779348459085  
    }