---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Balance-Update
api_type: REST
updated_at: 2026-01-15T23:46:07.477786
---

# Event: Margin Balance Update

## Event Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Balance-Update#event-description "Direct link to Event Description")

Margin Balance Update

## Event Name[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Balance-Update#event-name "Direct link to Event Name")

`balanceUpdate`

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Balance-Update#response-example "Direct link to Response Example")
    
    
    {  
      "e": "balanceUpdate",         //Event Type  
      "E": 1573200697110,           //Event Time  
      "a": "BTC",                   //Asset  
      "d": "100.00000000",          //Balance Delta  
      "U": 1027053479517            //event updateId  
      "T": 1573200697068            //Clear Time  
    }

---

# 杠杆账户余额更新事件

## 事件描述[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Margin-Balance-Update#事件描述 "事件描述的直接链接")

杠杆账户余额更新事件

## 事件类型[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Margin-Balance-Update#事件类型 "事件类型的直接链接")

`balanceUpdate`

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Margin-Balance-Update#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "balanceUpdate",         //时间类型  
      "E": 1573200697110,           //事件时间  
      "a": "BTC",                   //资产  
      "d": "100.00000000",          //变动数量  
      "U": 1027053479517            //事件更新ID  
      "T": 1573200697068            //Time  
    }