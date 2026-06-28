---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/user-data-streams/Event-Account-Configuration-Update
api_type: Account
updated_at: 2026-01-15T23:40:10.978828
---

# Event: Account Configuration Update (Leverage Update)

## Event Description[​](/docs/derivatives/coin-margined-futures/user-data-streams/Event-Account-Configuration-Update#event-description "Direct link to Event Description")

When the account configuration is changed, the event type will be pushed as `ACCOUNT_CONFIG_UPDATE` When the leverage of a trade pair changes, the payload will contain the object `ac` to represent the account configuration of the trade pair, where `s` represents the specific trade pair and `l` represents the leverage

## Event Name[​](/docs/derivatives/coin-margined-futures/user-data-streams/Event-Account-Configuration-Update#event-name "Direct link to Event Name")

`ACCOUNT_CONFIG_UPDATE`

## Response Example[​](/docs/derivatives/coin-margined-futures/user-data-streams/Event-Account-Configuration-Update#response-example "Direct link to Response Example")
    
    
    {  
        "e":"ACCOUNT_CONFIG_UPDATE",       // Event Type  
        "E":1611646737479,		           // Event Time  
        "T":1611646737476,		           // Transaction Time  
        "ac":{								  
        "s":"BTCUSD_PERP",				   // symbol  
        "l":25						       // leverage  
        }  
    }

---

# 杠杆倍数等账户配置更新推送

## 事件描述[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Event-Account-Configuration-Update#事件描述 "事件描述的直接链接")

当账户配置发生变化时会推送此类事件类型统一为`ACCOUNT_CONFIG_UPDATE` 当交易对杠杆倍数发生变化时推送消息体会包含对象`ac`表示交易对账户配置，其中`s`代表具体的交易对，`l`代表杠杆倍数

## 事件类型[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Event-Account-Configuration-Update#事件类型 "事件类型的直接链接")

`ACCOUNT_CONFIG_UPDATE`

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/user-data-streams/Event-Account-Configuration-Update#响应示例 "响应示例的直接链接")
    
    
    {  
        "e":"ACCOUNT_CONFIG_UPDATE",       // 事件类型  
        "E":1611646737479,		           // 事件时间  
        "T":1611646737476,		           // 撮合时间  
        "ac":{								  
        "s":"BTCUSD_PERP",				   // 交易对  
        "l":25						       // 杠杆倍数  
        }  
    }