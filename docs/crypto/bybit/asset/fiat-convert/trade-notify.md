---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/fiat-convert/trade-notify
api_type: REST
updated_at: 2026-05-27 19:15:16.227495
---

# Trade Notify

## Trade Notify

### Webhook URL

  * **Webhook_url** : Provided in the [trade-execute](/docs/v5/asset/fiat-convert/confirm-quote) API.



### Webhook Method

  * **HTTP Method** : `POST`



### Authentication

  * Share the **IP whitelist** with each other.



### Headers
    
    
    Content-Type: application/json  
    timestamp: xxx  
    publicKey: xxx  
    

* * *

### Request Body

The request body is in **JSON** format with the following fields:

Field Name| Type| Description  
---|---|---  
`tradeNo`| string| Trade order number  
`status`| string| Trade status: `processing`, `success`, or `failed`  
`quoteTxId`| string| Quote transaction ID. System generated, used to confirm the quote  
`exchangeRate`| string| Exchange rate  
`fromCoin`| string| Convert from coin (coin to sell)  
`fromCoinType`| string| Coin type of `fromCoin`, either `fiat` or `crypto`  
`toCoin`| string| Convert to coin (coin to buy)  
`toCoinType`| string| Coin type of `toCoin`, either `fiat` or `crypto`  
`fromAmount`| string| From coin amount (amount to sell)  
`toAmount`| string| To coin amount (amount to buy according to the exchange rate)  
`createdAt`| string| Trade created time

---

# 交易通知

## 交易通知

### Webhook URL

  * **Webhook_url** ：在 [trade-execute](/docs/zh-TW/v5/asset/fiat-convert/confirm-quote) API 中提供



### Webhook Method

  * **HTTP Method** ：`POST`



### Authentication

  * 雙方共享 **IP 白名單**



### Headers
    
    
    Content-Type: application/json  
    timestamp: xxx  
    publicKey: xxx  
    

* * *

### Request Body

請求體為 **JSON** 格式，包含以下欄位：

欄位名稱| 型別| 說明  
---|---|---  
`tradeNo`| string| 交易訂單號  
`status`| string| 交易狀態：`processing`、`success` 或 `failed`  
`quoteTxId`| string| 報價交易 ID，由系統產生，用於確認報價  
`exchangeRate`| string| 匯率  
`fromCoin`| string| 兌出幣種（賣出的幣）  
`fromCoinType`| string| `fromCoin` 的幣種類型，`fiat` 或 `crypto`  
`toCoin`| string| 兌入幣種（買入的幣）  
`toCoinType`| string| `toCoin` 的幣種類型，`fiat` 或 `crypto`  
`fromAmount`| string| 兌出幣種數量（賣出數量）  
`toAmount`| string| 兌入幣種數量（依照匯率計算的買入數量）  
`createdAt`| string| 交易建立時間