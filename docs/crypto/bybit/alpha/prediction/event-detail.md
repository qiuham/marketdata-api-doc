---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/prediction/event-detail
api_type: REST
updated_at: 2026-11-13 19:21:07.756041
---

# Get Event Detail

Get detailed information for a prediction market event, including all outcome markets and current prices. Call this before placing orders to obtain `tokenId` and verify market status.

info

  * `slug` takes priority over `eventId` when both are provided
  * Set `hasMoreMarkets=true` to include markets from related sub-events
  * `price` represents probability (0–1): a price of `0.65` means ~65% chance of that outcome



### HTTP Request

POST`/v5/alpha/prediction/event-detail`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
eventId| false| string| Event ID. Use `slug` when available  
slug| false| string| URL-friendly event slug. Takes priority over `eventId`  
hasMoreMarkets| false| boolean| Whether to include markets from related sub-events. Default: `false`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
eventId| string| Event ID  
slug| string| URL-friendly slug  
title| string| Event question  
description| string| Event description and resolution criteria  
category| string| Event category  
endDate| integer| Resolution timestamp (UTC milliseconds)  
resolved| boolean| Whether the event has been resolved  
volume| string| Total trading volume (USD)  
liquidity| string| Total available liquidity (USD)  
markets| array| Outcome markets within this event  
> tokenId| string| Outcome token ID. Used in buy/sell/estimate requests  
> outcome| string| Outcome label, e.g. `YES`, `NO`, or team name  
> price| string| Current price (0–1, represents probability)  
> side| integer| Trade direction. Refer to [predictionSide](/docs/v5/enum#predictionside-prediction-market--trade-direction)  
> volume| string| Token trading volume (USD)  
> liquidity| string| Token available liquidity (USD)  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/event-detail HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "slug": "will-argentina-win-world-cup-2026"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "eventId": "event_123",  
            "slug": "will-argentina-win-world-cup-2026",  
            "title": "Will Argentina win the 2026 World Cup?",  
            "description": "Argentina must win the FIFA 2026 World Cup final.",  
            "category": "Sports",  
            "endDate": 1750000000000,  
            "resolved": false,  
            "volume": "1500000",  
            "liquidity": "500000",  
            "markets": [  
                {  
                    "tokenId": "token_yes_123",  
                    "outcome": "YES",  
                    "price": "0.65",  
                    "side": 1,  
                    "volume": "900000",  
                    "liquidity": "300000"  
                },  
                {  
                    "tokenId": "token_no_123",  
                    "outcome": "NO",  
                    "price": "0.35",  
                    "side": 2,  
                    "volume": "600000",  
                    "liquidity": "200000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取賽事詳情

查詢預測市場賽事的完整信息，包括所有可交易市場及其結果代幣。在買入前需先調用此接口獲取 `tokenId` 並確認市場處於開放狀態。

信息

  * 通過 `eventId` 查詢單個賽事
  * 響應中包含該賽事下所有市場及其代幣，每個代幣代表一種可購買的預測結果



### HTTP 請求

POST`/v5/alpha/prediction/event-detail`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
eventId| **true**|  string| 賽事 ID  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
eventId| string| 賽事 ID  
eventName| string| 賽事名稱  
eventType| integer| 賽事類型。參考 [predictionEventType](/docs/zh-TW/v5/enum#predictioneventtype-prediction-market--event-type)  
startTime| integer| 賽事開始時間戳（UTC 毫秒）  
endTime| integer| 賽事結束時間戳（UTC 毫秒）  
status| integer| 賽事狀態。`1`=開放，`2`=已關閉，`3`=已結算  
markets| array| 該賽事下的市場列表  
> marketId| string| 市場 ID  
> marketType| integer| 市場類型。參考 [predictionMarketType](/docs/zh-TW/v5/enum#predictionmarkettype-prediction-market--market-type)  
> question| string| 市場問題（如「阿根廷能贏得 2026 年世界杯嗎？」）  
> tokens| array| 該市場可交易的結果代幣  
>> tokenId| string| 結果代幣 ID，用於委托接口  
>> outcome| string| 結果標籤（如 `YES`、`NO` 或隊伍名稱）  
>> price| string| 當前價格（0–1，代表隱含概率）  
>> liquidity| string| 可用流動性（USDC）  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/prediction/event-detail HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "eventId": "event_123"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "eventId": "event_123",  
            "eventName": "2026 FIFA World Cup",  
            "eventType": 1,  
            "startTime": 1748995200000,  
            "endTime": 1753228800000,  
            "status": 1,  
            "markets": [  
                {  
                    "marketId": "market_001",  
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
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }