---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/user-data-streams/Event-Account-data
api_type: Account
updated_at: 2026-01-15T23:43:23.749552
---

# Event: Account data

## Event Description[​](/docs/derivatives/options-trading/user-data-streams/Event-Account-data#event-description "Direct link to Event Description")

  * Update under the following conditions: 
    * Account deposit or withdrawal
    * Position info change
    * Periodic update every 10s when having position



## URL PATH[​](/docs/derivatives/options-trading/user-data-streams/Event-Account-data#url-path "Direct link to URL PATH")

`/private`

## Event Name[​](/docs/derivatives/options-trading/user-data-streams/Event-Account-data#event-name "Direct link to Event Name")

`ACCOUNT_UPDATE`

## Update Speed[​](/docs/derivatives/options-trading/user-data-streams/Event-Account-data#update-speed "Direct link to Update Speed")

**50ms**

## Response Example[​](/docs/derivatives/options-trading/user-data-streams/Event-Account-data#response-example "Direct link to Response Example")
    
    
    {  
        "stream": "89ljxuL6jFTN3Ej85aYOqH2BYXQ7eeuNYcGm7ktV",  
        "data": {  
            "e": "ACCOUNT_UPDATE",        // Event type  
            "E": 1762914568643,           // Event time  
            "T": 1762914568619,           // Transaction Time  
            "eq": "10000371.61462086",    // account equity in USDT  
            "aeq": "10000475.51032086",   // account adjusted equity in USDT  
            "b": "10000475.51032086",     // account wallet balance in USDT  
            "m": "-103.89570000",         // position value  
            "u": "16.10430000",           // unrealized pnl  
            "i": "32354.38562539",        // initial margin in USDT  
            "M": "6089.28766956"          // maintenance margin in USDT  
        }  
    }

---

# Account 数据更新推送

## 事件描述[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Account-data#事件描述 "事件描述的直接链接")

账户更新事件的event type 固定为 `ACCOUNT_UPDATE`

  * 当账户信息有变动时，会推送此事件： 
    * 仅当账户信息有变动时(包括资金、仓位发生变化)，才会推送此事件；
    * 有仓位情况下每10s定期更新



## URL PATH[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Account-data#url-path "URL PATH的直接链接")

`/private`

## 事件类型[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Account-data#事件类型 "事件类型的直接链接")

`ACCOUNT_UPDATE`

## 更新速度[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Account-data#更新速度 "更新速度的直接链接")

**50ms**

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Account-data#响应示例 "响应示例的直接链接")
    
    
    {  
        "stream": "89ljxuL6jFTN3Ej85aYOqH2BYXQ7eeuNYcGm7ktV",  
        "data": {  
            "e": "ACCOUNT_UPDATE",        //事件类型  
            "E": 1762914568643,           //事件时间  
            "T": 1762914568619,           //交易时间  
            "eq": "10000371.61462086",    //账户USDT权益  
            "aeq": "10000475.51032086",   //账户调整权益  
            "b": "10000475.51032086",     //账户USDT余额  
            "m": "-103.89570000",         //仓位价值  
            "u": "16.10430000",           //未实现盈利  
            "i": "32354.38562539",        //初始保证金  
            "M": "6089.28766956"          //维持保证金  
        }  
    }