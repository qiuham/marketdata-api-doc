---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/user-data-streams/Event-Greek-Update
api_type: REST
updated_at: 2026-01-15T23:43:23.881837
---

# Event: Greek Update

## Event Description[​](/docs/derivatives/options-trading/user-data-streams/Event-Greek-Update#event-description "Direct link to Event Description")

`GREEK_UPDATE` will be triggered when a position changes or periodically every 10 seconds when having position.

## URL PATH[​](/docs/derivatives/options-trading/user-data-streams/Event-Greek-Update#url-path "Direct link to URL PATH")

`/private`

## Event Name[​](/docs/derivatives/options-trading/user-data-streams/Event-Greek-Update#event-name "Direct link to Event Name")

`GREEK_UPDATE`

## Response Example[​](/docs/derivatives/options-trading/user-data-streams/Event-Greek-Update#response-example "Direct link to Response Example")
    
    
    {  
            "e": "GREEK_UPDATE",  
            "E": 1762917544216,  
            "T": 1762917544216,  
            "G": [  
                {  
                    "u": "BTCUSDT",   
                    "d": "-0.01304097",   //delta  
                    "g": "-0.00000124",   //gamma  
                    "t": "16.11648100",   //theta   
                    "v": "-3.83444011"    //vega  
                }  
            ]  
    }

---

# Greek更新推送

## 事件描述[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Greek-Update#事件描述 "事件描述的直接链接")

`GREEK_UPDATE`在仓位变动时或有仓位情况下每10s定期更新

## URL PATH[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Greek-Update#url-path "URL PATH的直接链接")

`/private`

## 事件类型[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Greek-Update#事件类型 "事件类型的直接链接")

`GREEK_UPDATE`

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Greek-Update#响应示例 "响应示例的直接链接")
    
    
    {  
            "e": "GREEK_UPDATE",  
            "E": 1762917544216,  
            "T": 1762917544216,  
            "G": [  
                {  
                    "u": "BTCUSDT",   
                    "d": "-0.01304097",   //delta  
                    "g": "-0.00000124",   //gamma  
                    "t": "16.11648100",   //theta   
                    "v": "-3.83444011"    //vega  
                }  
            ]  
    }