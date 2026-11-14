---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/position-list
api_type: REST
updated_at: 2026-11-13 19:21:14.245189
---

# Get Position List

Query the authenticated user's active prediction market positions. Call this before placing a sell order to confirm the position exists.

### HTTP Request

POST`/v5/alpha/prediction/position-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenId| false| string| Filter by outcome token ID  
eventId| false| string| Filter by event ID  
limit| false| integer| Number of records per page  
pageIndex| false| integer| Page number starting from `1`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
positions| array| Active position records  
> positionId| string| Position ID  
> tokenId| string| Outcome token ID  
> eventId| string| Event ID  
> outcomeName| string| Outcome label (e.g., `YES`, `NO`, or team name)  
> shares| string| Total shares held  
> cost| string| Total USDC cost of this position  
> avgPrice| string| Average cost price per share  
> currentPrice| string| Current market price per share (0–1)  
> value| string| Current market value of the position (USDC)  
> unrealizedPnl| string| Unrealized profit/loss (USDC)  
> unrealizedPnlRate| string| Unrealized P&L as decimal ratio (e.g. `0.107` = 10.7%)  
> createdAt| integer| Position open timestamp (UTC milliseconds)  
> finished| boolean| Whether the associated event has ended  
total| integer| Total matching records  
totalAssetUsd| string| Total asset value across all positions (USD)  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/position-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "limit": 20,  
        "pageIndex": 1  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "positions": [  
                {  
                    "positionId": "pos_001",  
                    "tokenId": "token_yes_123",  
                    "eventId": "event_123",  
                    "outcomeName": "YES",  
                    "shares": "153.84",  
                    "cost": "100.00",  
                    "avgPrice": "0.65",  
                    "currentPrice": "0.72",  
                    "value": "110.77",  
                    "unrealizedPnl": "10.77",  
                    "unrealizedPnlRate": "0.107",  
                    "createdAt": 1704067200000,  
                    "finished": false  
                }  
            ],  
            "total": 1,  
            "totalAssetUsd": "110.77"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取持倉列表

查詢已登錄用戶的預測市場當前持倉。在下賣出委托前，可先調用此接口確認持倉是否存在。

### HTTP 請求

POST`/v5/alpha/prediction/position-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenId| false| string| 按結果代幣 ID 篩選  
eventId| false| string| 按賽事 ID 篩選  
limit| false| integer| 每頁記錄數  
pageIndex| false| integer| 頁碼，從 `1` 開始  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
positions| array| 當前持倉記錄  
> positionId| string| 持倉 ID  
> tokenId| string| 結果代幣 ID  
> eventId| string| 賽事 ID  
> outcomeName| string| 結果標籤（如 `YES`、`NO` 或隊伍名稱）  
> shares| string| 持有的總份額  
> cost| string| 本倉位的總 USDC 成本  
> avgPrice| string| 每份額的平均成本價  
> currentPrice| string| 代幣當前市場價格（0–1）  
> value| string| 倉位當前市值（USDC）  
> unrealizedPnl| string| 未實現盈虧（USDC）  
> unrealizedPnlRate| string| 未實現盈虧比率（如 `0.107` = 10.7%）  
> createdAt| integer| 開倉時間戳（UTC 毫秒）  
> finished| boolean| 對應賽事是否已結束  
total| integer| 符合條件的總記錄數  
totalAssetUsd| string| 所有倉位的總資產價值（USD）  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/position-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "limit": 20,  
        "pageIndex": 1  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "positions": [  
                {  
                    "positionId": "pos_001",  
                    "tokenId": "token_yes_123",  
                    "eventId": "event_123",  
                    "outcomeName": "YES",  
                    "shares": "153.84",  
                    "cost": "100.00",  
                    "avgPrice": "0.65",  
                    "currentPrice": "0.72",  
                    "value": "110.77",  
                    "unrealizedPnl": "10.77",  
                    "unrealizedPnlRate": "0.107",  
                    "createdAt": 1704067200000,  
                    "finished": false  
                }  
            ],  
            "total": 1,  
            "totalAssetUsd": "110.77"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }