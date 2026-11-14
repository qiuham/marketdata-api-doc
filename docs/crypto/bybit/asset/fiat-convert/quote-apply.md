---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/asset/fiat-convert/quote-apply
api_type: REST
updated_at: 2026-11-13 19:21:44.238823
---

# Request a Quote

info

Request by the master UID's api key only

### HTTP Request

POST`/v5/fiat/quote-apply`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
fromCoin| **true**|  string| Convert from coin (coin to sell)  
fromCoinType| **true**|  string| `fiat` or `crypto`  
toCoin| **true**|  string| Convert to coin (coin to buy)  
toCoinType| **true**|  string| `fiat` or `crypto`  
requestAmount| **true**|  string| request coin amount (the amount you want to sell)  
requestCoinType| false| string| coinType you want to sell, `fiat` or `crypto`, default to `fiat`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
quoteTxId| string| Quote transaction ID. It is system generated, and it is used to confirm quote  
exchangeRate| string| Exchange rate  
fromCoin| string| Convert from coin (coin to sell)  
fromCoinType| string| From coin type. `fiat` or `crypto`  
toCoin| string| Convert to coin (coin to buy)  
toCoinType| string| To coin type. `fiat` or `crypto`  
fromAmount| string| From coin amount (amount to sell)  
toAmount| string| To coin amount (amount to buy according to exchange rate)  
expiredTime| string| The expiry time for this quote (milliseconds)  
  
### Request Example

  * HTTP
  * Python


    
    
    POST /v5/fiat/quote-apply HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1720071077014  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
    Content-Length: 172  
      
    {  
        "fromCoin": "ETH",  
        "fromCoinType": "fiat",  
        "toCoin": "BTC",  
        "toCoinType": "crypto",  
        "requestAmount": "0.1",  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.request_a_quote_fiat_convert(  
        fromCoin="ETH",  
        fromCoinType="crypto",  
        toCoin="BTC",  
        toCoinType="crypto",  
        requestAmount="0.1"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "quoteTaxId": "QuoteTaxId123456",  
            "exchangeRate": "1.0",  
            "fromCoin": "ETH",  
            "fromCoinType": "fiat",  
            "toCoin": "BTC",  
            "toCoinType": "crypto",  
            "fromAmount": "0.1",  
            "toAmount": "0.1",  
            "expireTime": "1764561045346"  
        }  
    }

---

# 申請報價

信息

僅可使用主帳號 UID 的 API 密鑰進行請求 

### HTTP 請求

POST`/v5/fiat/quote-apply`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
fromCoin| **true**|  string| 轉換的原幣種（賣出的幣種）  
fromCoinType| **true**|  string| 原幣種類型，可選值：`fiat` 或 `crypto`  
toCoin| **true**|  string| 轉換的目標幣種（買入的幣種）  
toCoinType| **true**|  string| 目標幣種類型，可選值：`fiat` 或 `crypto`  
requestAmount| **true**|  string| 請求的原幣種數量（賣出的數量）  
requestCoinType| false| string| 你想要賣出的 coinType，填入 `fiat` 或 `crypto`，預設為 `fiat`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
quoteTxId| string| 報價交易 ID，系統生成，用於確認報價  
exchangeRate| string| 匯率  
fromCoin| string| 轉換的原幣種（賣出的幣種）  
fromCoinType| string| 原幣種類型，可選值：`fiat` 或 `crypto`  
toCoin| string| 轉換的目標幣種（買入的幣種）  
toCoinType| string| 目標幣種類型，可選值：`fiat` 或 `crypto`  
fromAmount| string| 原幣種數量（賣出的數量）  
toAmount| string| 目標幣種數量（根據匯率買入的數量）  
expiredTime| string| 該報價的過期時間（毫秒）  
  
### 請求示例

  * HTTP


    
    
    POST /v5/fiat/quote-apply HTTP/1.1    
    Host: api-testnet.bybit.com    
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx    
    X-BAPI-TIMESTAMP: 1720071077014    
    X-BAPI-RECV-WINDOW: 5000    
    X-BAPI-SIGN: XXXXXX    
    Content-Type: application/json    
    Content-Length: 172    
      
    {  
        "fromCoin": "ETH",  
        "fromCoinType": "fiat",  
        "toCoin": "BTC",  
        "toCoinType": "crypto",  
        "requestAmount": "0.1"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "quoteTaxId": "QuoteTaxId123456",  
            "exchangeRate": "1.0",  
            "fromCoin": "ETH",  
            "fromCoinType": "fiat",  
            "toCoin": "BTC",  
            "toCoinType": "crypto",  
            "fromAmount": "0.1",  
            "toAmount": "0.1",  
            "expireTime": "1764561045346"  
        }  
    }