---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/order-list
api_type: Trading
updated_at: 2026-07-29 18:52:00.443450
---

# Get Coin Delta Amount

Query coin delta amount details for institutional loan hedge product.

info

  * Unified account only
  * Optional `coin` filter; if omitted, returns all coins



### HTTP Request

GET`/v5/ins-loan/coin-delta-amount`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Coin name, uppercase only. e.g. `BTC`. If not passed, returns all coins  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
riskUnitDeltaAmount| string| Risk unit total delta amount limit (USD)  
riskUnitDeltaAvailableAmount| string| Risk unit available delta amount (USD)  
list| array| Object  
> coin| string| Coin name  
> coinDeltaSize| string| Coin delta size (quantity)  
> coinDeltaAvailableAmount| string| Coin delta available amount (USD)  
> coinDeltaAmount| string| Coin delta total amount limit (USD)  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/coin-delta-amount?coin=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1716192000000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "riskUnitDeltaAmount": "500000",  
            "riskUnitDeltaAvailableAmount": "350000",  
            "list": [  
                {  
                    "coin": "BTC",  
                    "coinDeltaSize": "10",  
                    "coinDeltaAvailableAmount": "200000",  
                    "coinDeltaAmount": "300000"  
                },  
                {  
                    "coin": "ETH",  
                    "coinDeltaSize": "100",  
                    "coinDeltaAvailableAmount": "150000",  
                    "coinDeltaAmount": "200000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1716192000000  
    }

---

# 查詢幣種 Delta 額度

查詢機構借貸對沖產品的幣種 Delta 額度詳情。

信息

  * 僅支持統一帳戶
  * `coin` 為可選篩選參數，若不傳則返回所有幣種



### HTTP 請求

GET`/v5/ins-loan/coin-delta-amount`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
coin| false| string| 幣種名稱，僅大寫。如 `BTC`。若不傳，返回所有幣種  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
riskUnitDeltaAmount| string| 風險單元 Delta 總額度限制（USD）  
riskUnitDeltaAvailableAmount| string| 風險單元可用 Delta 額度（USD）  
list| array| Object  
> coin| string| 幣種名稱  
> coinDeltaSize| string| 幣種 Delta 數量  
> coinDeltaAvailableAmount| string| 幣種可用 Delta 額度（USD）  
> coinDeltaAmount| string| 幣種 Delta 總額度限制（USD）  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/coin-delta-amount?coin=BTC HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1716192000000  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
      
    
    
    
      
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "riskUnitDeltaAmount": "500000",  
            "riskUnitDeltaAvailableAmount": "350000",  
            "list": [  
                {  
                    "coin": "BTC",  
                    "coinDeltaSize": "10",  
                    "coinDeltaAvailableAmount": "200000",  
                    "coinDeltaAmount": "300000"  
                },  
                {  
                    "coin": "ETH",  
                    "coinDeltaSize": "100",  
                    "coinDeltaAvailableAmount": "150000",  
                    "coinDeltaAmount": "200000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1716192000000  
    }