---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/side-market-list
api_type: REST
updated_at: 2026-11-13 19:21:14.326369
---

# Get Side Market List

Query the list of available prediction markets (side markets) for a given event. Returns all outcome tokens with current prices, liquidity, and trading status. Use this to discover which outcomes can be traded within an event.

info

  * Results can be sorted by `volume`, `liquidity`, or `endDate`
  * For full event detail including related markets, use [Get Event Detail](/docs/v5/alpha/prediction/event-detail) instead



### HTTP Request

POST`/v5/alpha/prediction/side-market-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
eventId| **true**|  string| Event ID to query markets for  
sortBy| false| string| Sort field. Refer to [predictionSortBy](/docs/v5/enum#predictionsortby-prediction-market--sort-field)  
marketType| false| integer| Filter by market type. Refer to [predictionMarketType](/docs/v5/enum#predictionmarkettype-prediction-market--market-type)  
limit| false| integer| Number of records per page  
pageIndex| false| integer| Page number starting from `1`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Side market records  
> marketId| string| Side market ID  
> eventId| string| Parent event ID  
> marketType| integer| Market type. Refer to [predictionMarketType](/docs/v5/enum#predictionmarkettype-prediction-market--market-type)  
> question| string| Market question (e.g., "Will Argentina win the 2026 FIFA World Cup?")  
> tokens| array| Outcome tokens available in this market  
>> tokenId| string| Outcome token ID  
>> outcome| string| Outcome label (e.g., "YES", "NO", team name)  
>> price| string| Current price (0–1 implied probability)  
>> liquidity| string| Available liquidity in USDC  
> volume24h| string| 24-hour trading volume in USDC  
> endDate| integer| Market resolution timestamp (UTC milliseconds)  
> status| integer| Market status. `1`=Open, `2`=Closed, `3`=Resolved  
total| integer| Total matching records  
pageIndex| integer| Current page number  
pageSize| integer| Items per page  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/side-market-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "eventId": "event_123",  
        "sortBy": "volume",  
        "limit": 20,  
        "pageIndex": 1  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "marketId": "market_001",  
                    "eventId": "event_123",  
                    "marketType": 1,  
                    "question": "Will Argentina win the 2026 FIFA World Cup?",  
                    "tokens": [  
                        {  
                            "tokenId": "token_yes_123",  
                            "outcome": "YES",  
                            "price": "0.65",  
                            "liquidity": "100000"  
                        },  
                        {  
                            "tokenId": "token_no_123",  
                            "outcome": "NO",  
                            "price": "0.35",  
                            "liquidity": "95000"  
                        }  
                    ],  
                    "volume24h": "50000",  
                    "endDate": 1750000000000,  
                    "status": 1  
                }  
            ],  
            "total": 1,  
            "pageIndex": 1,  
            "pageSize": 20  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取市場列表

查詢指定賽事下的可用預測市場（子市場）列表，返回所有結果代幣的當前價格、流動性及交易狀態，用於發現某賽事內可交易的預測結果。

信息

  * 結果可按 `volume`（交易量）、`liquidity`（流動性）或 `endDate`（結束時間）排序
  * 如需包含關聯市場的完整賽事詳情，請使用 [獲取賽事詳情](/docs/zh-TW/v5/alpha/prediction/event-detail)



### HTTP 請求

POST`/v5/alpha/prediction/side-market-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
eventId| **true**|  string| 要查詢的賽事 ID  
sortBy| false| string| 排序字段。參考 [predictionSortBy](/docs/zh-TW/v5/enum#predictionsortby-prediction-market--sort-field)  
marketType| false| integer| 按市場類型篩選。參考 [predictionMarketType](/docs/zh-TW/v5/enum#predictionmarkettype-prediction-market--market-type)  
limit| false| integer| 每頁記錄數  
pageIndex| false| integer| 頁碼，從 `1` 開始  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 子市場記錄  
> marketId| string| 子市場 ID  
> eventId| string| 父賽事 ID  
> marketType| integer| 市場類型。參考 [predictionMarketType](/docs/zh-TW/v5/enum#predictionmarkettype-prediction-market--market-type)  
> question| string| 市場問題（如「阿根廷能贏得 2026 年世界杯嗎？」）  
> tokens| array| 該市場可交易的結果代幣  
>> tokenId| string| 結果代幣 ID  
>> outcome| string| 結果標籤（如 `YES`、`NO` 或隊伍名稱）  
>> price| string| 當前價格（0–1 隱含概率）  
>> liquidity| string| 可用流動性（USDC）  
> volume24h| string| 24 小時交易量（USDC）  
> endDate| integer| 市場結算時間戳（UTC 毫秒）  
> status| integer| 市場狀態。`1`=開放，`2`=已關閉，`3`=已結算  
total| integer| 符合條件的總記錄數  
pageIndex| integer| 當前頁碼  
pageSize| integer| 每頁記錄數  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/side-market-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "eventId": "event_123",  
        "sortBy": "volume",  
        "limit": 20,  
        "pageIndex": 1  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "marketId": "market_001",  
                    "eventId": "event_123",  
                    "marketType": 1,  
                    "question": "Will Argentina win the 2026 FIFA World Cup?",  
                    "tokens": [  
                        {  
                            "tokenId": "token_yes_123",  
                            "outcome": "YES",  
                            "price": "0.65",  
                            "liquidity": "100000"  
                        },  
                        {  
                            "tokenId": "token_no_123",  
                            "outcome": "NO",  
                            "price": "0.35",  
                            "liquidity": "95000"  
                        }  
                    ],  
                    "volume24h": "50000",  
                    "endDate": 1750000000000,  
                    "status": 1  
                }  
            ],  
            "total": 1,  
            "pageIndex": 1,  
            "pageSize": 20  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }