---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/order-estimate
api_type: REST
updated_at: 2026-11-13 19:21:10.957787
---

# Get Order Estimate

Estimate the outcome of a prediction market buy or sell order before execution. This is a **mandatory** step — always show the estimate to the user and obtain explicit confirmation before calling [Buy](/docs/v5/alpha/prediction/buy) or [Sell](/docs/v5/alpha/prediction/sell).

info

  * **BUY** : set `side=1`, `amount` = USDC to invest, include `payTokenCode="USDC"`
  * **SELL** : set `side=2`, `amount` = number of shares to sell
  * Phase 1 supports `orderType=1` (FOK) only
  * Always display `estimatedCost`, `estimatedReceive`, `feeAmount`, and `toWin` (BUY only) to the user before proceeding
  * Do NOT call [Buy](/docs/v5/alpha/prediction/buy) or [Sell](/docs/v5/alpha/prediction/sell) without explicit user confirmation after viewing the estimate



### HTTP Request

POST`/v5/alpha/prediction/order-estimate`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenId| **true**|  string| Outcome token ID (from [Get Event Detail](/docs/v5/alpha/prediction/event-detail))  
side| **true**|  integer| Trade direction. Refer to [predictionSide](/docs/v5/enum#predictionside-prediction-market--trade-direction)  
eventId| **true**|  string| Event ID associated with the token  
amount| **true**|  string| BUY: USDC to invest. SELL: number of shares to sell (positive decimal as string)  
orderType| **true**|  integer| Order type. Refer to [predictionOrderType](/docs/v5/enum#predictionordertype-prediction-market--order-type). Phase 1: `1` (FOK) only  
payTokenCode| false| string| Payment token code. Required for BUY. Phase 1 fixed to `USDC`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
avgPrice| string| Estimated average execution price per share (0–1)  
estimatedCost| string| BUY: USDC to pay. SELL: shares to sell  
estimatedReceive| string| BUY: estimated shares received. SELL: estimated USDC received  
toWin| string| BUY only: amount to win if outcome is correct (shares × 1 USDC)  
feeAmount| string| Total platform fee (USDC) = `serverFee` \+ `polymarketFee`  
feeDetail| object| Fee breakdown  
> serverFee| string| Platform service fee (USDC)  
> polymarketFee| string| Polymarket protocol fee (USDC)  
slippage| string| Slippage applied to this estimate  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/order-estimate HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenId": "token_yes_123",  
        "side": 1,  
        "eventId": "event_123",  
        "amount": "100",  
        "orderType": 1,  
        "payTokenCode": "USDC"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "avgPrice": "0.65",  
            "estimatedCost": "100",  
            "estimatedReceive": "153.84",  
            "toWin": "153.84",  
            "feeAmount": "1.00",  
            "feeDetail": {  
                "serverFee": "0.70",  
                "polymarketFee": "0.30"  
            },  
            "slippage": "0.05"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取委托預估

在執行前預估預測市場買入或賣出委托的結果。這是**必填步驟** ——在調用 [買入](/docs/zh-TW/v5/alpha/prediction/buy) 或 [賣出](/docs/zh-TW/v5/alpha/prediction/sell) 前，必須先向用戶展示預估結果並取得明確確認。

信息

  * **買入** ：設置 `side=1`，`amount` 為投入的 USDC，需包含 `payTokenCode="USDC"`
  * **賣出** ：設置 `side=2`，`amount` 為賣出的份額數量
  * 第一階段僅支持 `orderType=1`（FOK）
  * 向用戶展示 `estimatedCost`、`estimatedReceive`、`feeAmount`，買入時還需展示 `toWin`
  * 未取得用戶明確確認前，請勿調用 [買入](/docs/zh-TW/v5/alpha/prediction/buy) 或 [賣出](/docs/zh-TW/v5/alpha/prediction/sell)



### HTTP 請求

POST`/v5/alpha/prediction/order-estimate`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenId| **true**|  string| 結果代幣 ID（從 [獲取賽事詳情](/docs/zh-TW/v5/alpha/prediction/event-detail) 獲取）  
side| **true**|  integer| 交易方向。參考 [predictionSide](/docs/zh-TW/v5/enum#predictionside-prediction-market--trade-direction)  
eventId| **true**|  string| 代幣對應的賽事 ID  
amount| **true**|  string| 買入：投入的 USDC；賣出：賣出的份額數量（正數字符串）  
orderType| **true**|  integer| 委托類型。參考 [predictionOrderType](/docs/zh-TW/v5/enum#predictionordertype-prediction-market--order-type)。第一階段：`1`（FOK）  
payTokenCode| false| string| 支付代幣代碼。買入時必填，第一階段固定為 `USDC`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
avgPrice| string| 預估平均成交價格（0–1）  
estimatedCost| string| 買入：需支付的 USDC；賣出：賣出的份額  
estimatedReceive| string| 買入：預估獲得的份額；賣出：預估獲得的 USDC  
toWin| string| 僅限買入：若結果正確可獲得的金額（份額 × 1 USDC）  
feeAmount| string| 總手續費（USDC）= `serverFee` \+ `polymarketFee`  
feeDetail| object| 手續費明細  
> serverFee| string| 平台服務費（USDC）  
> polymarketFee| string| Polymarket 協議費（USDC）  
slippage| string| 本次預估所用的滑點  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/order-estimate HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenId": "token_yes_123",  
        "side": 1,  
        "eventId": "event_123",  
        "amount": "100",  
        "orderType": 1,  
        "payTokenCode": "USDC"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "avgPrice": "0.65",  
            "estimatedCost": "100",  
            "estimatedReceive": "153.84",  
            "toWin": "153.84",  
            "feeAmount": "1.00",  
            "feeDetail": {  
                "serverFee": "0.70",  
                "polymarketFee": "0.30"  
            },  
            "slippage": "0.05"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }