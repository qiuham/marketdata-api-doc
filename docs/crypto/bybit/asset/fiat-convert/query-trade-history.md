---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/fiat-convert/query-trade-history
api_type: REST
updated_at: 2026-05-27 19:15:12.798685
---

# Get Convert History

Returns all the convert history

### HTTP Request

GET`/v5/fiat/query-trade-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
index| false| integer| Page number,started from 1, default 1  
limit| false| integer| Page Size [20-100] 20 records by default,up to 100 records, return 100 when exceeds 100  
startTime| false| string| Query start time(Millisecond timestamp)  
endTime| false| string| Query end time(Millisecond timestamp)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Array of quotes  
> tradeNo| string| Trade order No  
> status| string| Trade status:

  * processing
  * success
  * failed

  
> quoteTxId| string| Quote transaction ID. It is system generated, and it is used to confirm quote  
> exchangeRate| string| Exchange rate  
> fromCoin| string| Convert from coin (coin to sell)  
> fromCoinType| string| From coin type. `fiat` or `crypto`  
> toCoin| string| Convert to coin (coin to buy)  
> toCoinType| string| To coin type. `fiat` or `crypto`  
> fromAmount| string| From coin amount (amount to sell)  
> toAmount| string| To coin amount (amount to buy according to exchange rate)  
> createdAt| string| Trade created timee (Millisecond timestamp)  
> subUserId| string| The user's sub userId in bybit  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/fiat/trade-query-history HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720074159814  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_fiat_convert_history())  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": [  
            {  
                "tradeNo": "TradeNo123456",  
                "status": "success",  
                "quoteTaxId": "QuoteTaxId123456",  
                "exchangeRate": "1.0",  
                "fromCoin": "GEL",  
                "fromCoinType": "fiat",  
                "toCoin": "USDT",  
                "toCoinType": "crypto",  
                "fromAmount": "100",  
                "toAmount": "100",  
                "createdAt": "1764560093588",  
                "subUserId": "123456"  
            }  
        ]  
    }

---

# 查詢兌換歷史

### HTTP 請求

GET`/v5/fiat/query-trade-history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
index| false| integer| 頁碼，默認為 1  
limit| false| integer| 每頁記錄數量，[20-100]，默認為 20 條，最大支持 100 條，超過 100 條時返回 100 條  
startTime| false| string| 查詢開始時間（毫秒級時間戳）  
endTime| false| string| 查詢結束時間（毫秒級時間戳）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| 報價記錄數組  
> tradeNo| string| 交易訂單號  
> status| string| 交易狀態：

  * processing
  * success
  * failed

  
> quoteTxId| string| 報價交易 ID，系統生成，用於確認報價  
> exchangeRate| string| 匯率  
> fromCoin| string| 轉換前的幣種（賣出的幣種）  
> fromCoinType| string| 轉換前的幣種類型：`fiat` 或 `crypto`  
> toCoin| string| 轉換後的幣種（買入的幣種）  
> toCoinType| string| 轉換後的幣種類型：`fiat` 或 `crypto`  
> fromAmount| string| 轉換前的幣種數量（賣出數量）  
> toAmount| string| 轉換後的幣種數量（根據匯率買入的數量）  
> createdAt| string| 交易創建時間（毫秒級時間戳）  
> subUserId| string| 用戶在 Bybit 平台的子用戶 ID  
  
### 請求示例

  * HTTP


    
    
    GET /v5/fiat/trade-query-history HTTP/1.1    
    Host: api-testnet.bybit.com    
    X-BAPI-SIGN: XXXXXX    
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx    
    X-BAPI-TIMESTAMP: 1720074159814    
    X-BAPI-RECV-WINDOW: 5000    
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": [  
            {  
                "tradeNo": "TradeNo123456",  
                "status": "success",  
                "quoteTaxId": "QuoteTaxId123456",  
                "exchangeRate": "1.0",  
                "fromCoin": "GEL",  
                "fromCoinType": "fiat",  
                "toCoin": "USDT",  
                "toCoinType": "crypto",  
                "fromAmount": "100",  
                "toAmount": "100",  
                "createdAt": "1764560093588",  
                "subUserId": "123456"  
            }  
        ]  
    }