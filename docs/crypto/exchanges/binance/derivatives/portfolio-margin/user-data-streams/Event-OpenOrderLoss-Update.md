---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Event-OpenOrderLoss-Update
api_type: REST
updated_at: 2026-01-15T23:46:07.614452
---

# Event: OpenOrderLoss Update

## Event Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-OpenOrderLoss-Update#event-description "Direct link to Event Description")

Cross margin order margin stream

## Event Name[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-OpenOrderLoss-Update#event-name "Direct link to Event Name")

`openOrderLoss`

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-OpenOrderLoss-Update#response-example "Direct link to Response Example")
    
    
    {  
        "e": "openOrderLoss",      //Event Type  
        "E": 1678710578788,        // Event Time  
        "O": [  
            {                    // Update Data  
            "a": "BUSD",  
            "o": "-0.1232313"       // Amount  
            },   
            {  
            "a": "BNB",  
            "o": "-12.1232313"  
            }  
        ]  
    }

---

# 杠杆账户全仓挂单占用事件

## 事件描述[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-OpenOrderLoss-Update#事件描述 "事件描述的直接链接")

杠杆账户全仓挂单占用事件

## 事件类型[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-OpenOrderLoss-Update#事件类型 "事件类型的直接链接")

`openOrderLoss`

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-OpenOrderLoss-Update#�响应示例 "响应示例的直接链接")
    
    
    {  
        "e": "openOrderLoss",      //Event Type  
        "E": 1678710578788,        // Event Time  
        "O": [  
            {                    // Update Data  
            "a": "BUSD",  
            "o": "-0.1232313"       // Amount  
            },   
            {  
            "a": "BNB",  
            "o": "-12.1232313"  
            }  
        ]  
    }