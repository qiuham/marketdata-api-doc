---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Account-Update
api_type: Account
updated_at: 2026-01-15T23:46:07.414489
---

# Event: Margin Account Update

## Event Description[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Account-Update#event-description "Direct link to Event Description")

`outboundAccountPosition` is sent any time an account balance has changed and contains the assets that were possibly changed by the event that generated the balance change.

## Event Name[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Account-Update#event-name "Direct link to Event Name")

`outboundAccountPosition`

## Response Example[​](/docs/derivatives/portfolio-margin/user-data-streams/Event-Margin-Account-Update#response-example "Direct link to Response Example")
    
    
    {  
      "e": "outboundAccountPosition", //Event type  
      "E": 1564034571105,             //Event Time  
      "u": 1564034571073,             //Time of last account update  
      "U": 1027053479517,             // time updateID  
      "B": [                          //Balances Array  
        {  
          "a": "ETH",                 //Asset  
          "f": "10000.000000",        //Free  
          "l": "0.000000"             //Locked  
        }  
      ]  
    }

---

# 杠杆账户更新事件

## 事件描述[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Margin-Account-Update#事件描述 "事件描述的直接链接")

每当帐户余额发生更改时，都会发送一个事件`outboundAccountPosition`，其中包含可能由生成余额变动的事件而变动的资产。

## 事件类型[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Margin-Account-Update#事件类型 "事件类型的直接链接")

`outboundAccountPosition`

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-Margin-Account-Update#响应示例 "��响应示例的直接链接")
    
    
    {  
      "e": "outboundAccountPosition", // 事件类型  
      "E": 1564034571105,             // 事件时间  
      "u": 1564034571073,             // 账户末次更新时间戳  
      "U": 1027053479517,             // 时间更新ID  
      "B": [                          // 余额  
        {  
          "a": "ETH",                 // 资产名称  
          "f": "10000.000000",        // 可用余额  
          "l": "0.000000"             // 冻结余额  
        }  
      ]  
    }