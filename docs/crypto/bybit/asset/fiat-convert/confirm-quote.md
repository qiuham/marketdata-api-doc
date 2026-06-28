---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/fiat-convert/confirm-quote
api_type: REST
updated_at: 2026-06-28 19:08:47.336123
---

# Get Convert Status

Returns the details of this convert.

### HTTP Request

GET`/v5/fiat/trade-query`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tradeNo| false| string| Trade order No,tradeNo or merchantRequestId must be provided  
merchantRequestId| false| string| Customised request ID,tradeNo or merchantRequestId must be provided  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| object| object  
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
> createdAt| string| Trade created time  
> subUserId| string| The user's sub userId in bybit  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/fiat/trade-query?tradeNo=TradeNo123456 HTTP/1.1    
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
    print(session.get_fiat_convert_status(  
        tradeNo="TradeNo123456"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
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
            "createdAt": "1764558832014",  
            "subUserId": "123456"  
        }  
    }

---

# 查詢報價單狀態

### HTTP 請求

GET`/v5/fiat/trade-query`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tradeNo| 否| string| 交易訂單號，`tradeNo` 或 `merchantRequestId` 必須提供一個  
merchantRequestId| 否| string| 自定義請求 ID，`tradeNo` 或 `merchantRequestId` 必須提供一個  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| object| object  
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
> createdAt| string| 交易創建時間  
> subUserId| string| 用戶在 Bybit 平台的子用戶 ID  
  
### 請求示例

  * HTTP


    
    
    GET /v5/fiat/trade-query?tradeNo=TradeNo123456 HTTP/1.1    
    Host: api-testnet.bybit.com    
    X-BAPI-SIGN: XXXXXX    
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx    
    X-BAPI-TIMESTAMP: 1720074159814    
    X-BAPI-RECV-WINDOW: 5000    
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
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
            "createdAt": "1764558832014",  
            "subUserId": "123456"  
        }  
    }