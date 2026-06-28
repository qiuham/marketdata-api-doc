---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/liquidation-records
api_type: REST
updated_at: 2026-05-27 19:16:57.611236
---

# Get Position Info

info

  * Need authentication. **Up to 10 requests** per second per UID. Requires Earn permission on the API key.
  * Returns all active liquidity mining positions. Position amounts are dynamically calculated based on the current market price.



### HTTP Request

GET`/v5/earn/liquidity-mining/position`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productId| false| string| Filter by product ID  
baseCoin| false| string| Filter by base coin, e.g. `BTC`, `ETH`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
positions| array| Active position list  
> positionId| string| Position ID  
> productId| string| Product ID  
> baseCoin| string| Base coin, e.g. `BTC`  
> quoteCoin| string| Quote coin, e.g. `USDT`  
> quoteAmount| string| Current quoteCoin balance in the position (dynamically calculated including leverage)  
> baseAmount| string| Current baseCoin balance in the position (dynamically calculated including leverage)  
> principalQuoteAmount| string| Total quoteCoin principal invested (dynamically calculated)  
> principalBaseAmount| string| Total baseCoin principal invested (dynamically calculated)  
> principalLiquidityValue| string| Principal liquidity value (quoted in quoteCoin, real-time)  
> leveragedValue| string| Total leveraged position value (quoted in quoteCoin, real-time)  
> loan| string| Borrowed amount (in quoteCoin)  
> claimableYield| string| Current claimable yield amount  
> currentApr| string| Current APR (real-time). Divide by 10^8 to get the actual rate  
> leverage| string| Current leverage multiplier  
> margin| string| Current margin amount  
> liquidationPrice| string| Liquidation price (baseCoin price in quoteCoin terms)  
> currentPriceY| string| Current market price of baseCoin (real-time)  
> status| string| Position status: `Active`, `Liquidating`  
> createdTime| string| Position creation time, unix timestamp in milliseconds  
  
* * *

### Request Example
    
    
    GET /v5/earn/liquidity-mining/position?baseCoin=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "positions": [  
                {  
                    "positionId": "1498",  
                    "productId": "5",  
                    "baseCoin": "ETH",  
                    "quoteCoin": "USDT",  
                    "quoteAmount": "1637.7537",  
                    "baseAmount": "0.80131605",  
                    "principalQuoteAmount": "817.5297",  
                    "principalBaseAmount": "0.39999891",  
                    "principalLiquidityValue": "1635.0595",  
                    "leveragedValue": "3275.5075",  
                    "loan": "1640.448",  
                    "claimableYield": "0",  
                    "currentApr": "27856097",  
                    "leverage": "2.003295552626342963",  
                    "margin": "0",  
                    "liquidationPrice": "538.272",  
                    "currentPriceY": "2043.83",  
                    "status": "Active",  
                    "createdTime": "1775116860000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775124245970  
    }

---

# 查詢持倉資訊

信息

  * 需要身份驗證。每個 UID 每秒**最多 10 次請求** 。API 金鑰需要具備 Earn（理財）權限。
  * 返回所有活躍的流動性挖礦持倉。持倉金額根據當前市價動態計算。



### HTTP 請求

GET`/v5/earn/liquidity-mining/position`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
productId| false| string| 按產品 ID 篩選  
baseCoin| false| string| 按基礎幣種篩選，例如：`BTC`, `ETH`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
positions| array| 活躍持倉列表  
> positionId| string| 持倉 ID  
> productId| string| 產品 ID  
> baseCoin| string| 基礎幣種，例如：`BTC`  
> quoteCoin| string| 計價幣種，例如：`USDT`  
> quoteAmount| string| 持倉中當前計價幣種餘額（含槓桿動態計算）  
> baseAmount| string| 持倉中當前基礎幣種餘額（含槓桿動態計算）  
> principalQuoteAmount| string| 已投入的計價幣種本金總額（動態計算）  
> principalBaseAmount| string| 已投入的基礎幣種本金總額（動態計算）  
> principalLiquidityValue| string| 本金流動性價值（以計價幣種計，即時）  
> leveragedValue| string| 槓桿持倉總價值（以計價幣種計，即時）  
> loan| string| 借款金額（以計價幣種計）  
> claimableYield| string| 當前可領取收益金額  
> currentApr| string| 當前年化收益率（即時）。除以 10^8 可得實際利率  
> leverage| string| 當前槓桿倍數  
> margin| string| 當前保證金金額  
> liquidationPrice| string| 強制平倉價格（基礎幣種以計價幣種計）  
> currentPriceY| string| 基礎幣種當前市價（即時）  
> status| string| 持倉狀態：`Active`（活躍），`Liquidating`（強制平倉中）  
> createdTime| string| 持倉建立時間，毫秒級 Unix 時間戳  
  
* * *

### 請求示例
    
    
    GET /v5/earn/liquidity-mining/position?baseCoin=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "positions": [  
                {  
                    "positionId": "1498",  
                    "productId": "5",  
                    "baseCoin": "ETH",  
                    "quoteCoin": "USDT",  
                    "quoteAmount": "1637.7537",  
                    "baseAmount": "0.80131605",  
                    "principalQuoteAmount": "817.5297",  
                    "principalBaseAmount": "0.39999891",  
                    "principalLiquidityValue": "1635.0595",  
                    "leveragedValue": "3275.5075",  
                    "loan": "1640.448",  
                    "claimableYield": "0",  
                    "currentApr": "27856097",  
                    "leverage": "2.003295552626342963",  
                    "margin": "0",  
                    "liquidationPrice": "538.272",  
                    "currentPriceY": "2043.83",  
                    "status": "Active",  
                    "createdTime": "1775116860000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1775124245970  
    }