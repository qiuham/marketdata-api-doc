---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Event-Liability-Update
api_type: REST
updated_at: 2026-01-15T23:46:04.817352
---

# Event: Liability Update

## Event Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Liability-Update#event-description "Direct link to Event Description")

Margin Liability update

## Event Name[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Liability-Update#event-name "Direct link to Event Name")

`liabilityChange`

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Liability-Update#response-example "Direct link to Response Example")
    
    
    {  
      "e": "liabilityChange",        //Event Type  
      "E": 1573200697110,            //Event Time  
      "a": "BTC",                    //Asset  
      "t": “BORROW”                  //Type  
      "T": 1352286576452864727,     //Transaction ID  
      "p": "1.03453430",             //Principal  
      "i": "0",                      //Interest  
      "l": "1.03476851"              //Total Liability  
    }

---

# 杠杆账户负债更新

## 数据流描述[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Liability-Update#数据流描述 "数据流描述的直接链接")

杠杆账户负债更新

## Stream Name[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Liability-Update#stream-name "Stream Name的直接链接")

`liabilityChange`

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Liability-Update#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "liabilityChange",       //Event Type  
      "E": 1573200697110,           //Event Time  
      "a": "BTC",                   //Asset  
      "t": “BORROW”                 //Type  
      "T": 1352286576452864727,    //Transaction ID  
      "p": "1.03453430",            //Principal  
      "i": "0",                     //Interest  
      "l": "1.03476851"             //Total Liability  
    }