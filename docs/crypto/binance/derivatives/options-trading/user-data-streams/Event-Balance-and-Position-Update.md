---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/user-data-streams/Event-Balance-and-Position-Update
api_type: REST
updated_at: 2026-01-15T23:43:23.818822
---

# Event: Balance and Position Update

## Event Description[​](/docs/derivatives/options-trading/user-data-streams/Event-Balance-and-Position-Update#event-description "Direct link to Event Description")

Event type is `ACCOUNT_UPDATE`.

  * When balance or position get updated, this event will be pushed.

    * `ACCOUNT_UPDATE` will be pushed only when update happens on user's account, including changes on balances, positions.
    * Unfilled orders or cancelled orders will not make the event `ACCOUNT_UPDATE` pushed, since there's no change on positions.
    * "position" in `ACCOUNT_UPDATE`: Only symbols of changed positions will be pushed.
  * The field "m" represents the reason type for the event and may shows the following possible types:

    * DEPOSIT
    * WITHDRAW
    * ORDER
  * The field "bc" represents the balance change except for PnL and commission.




## Event Name[​](/docs/derivatives/options-trading/user-data-streams/Event-Balance-and-Position-Update#event-name "Direct link to Event Name")

`BALANCE_POSITION_UPDATE`

## Response Example[​](/docs/derivatives/options-trading/user-data-streams/Event-Balance-and-Position-Update#response-example "Direct link to Response Example")
    
    
    {  
            "e": "BALANCE_POSITION_UPDATE",  
            "E": 1762917544216,  
            "T": 1762917544206,  
            "m": "ORDER",  
            "B": [  
                {  
                    "a": "USDT",                  // Margin asset    
                    "b": "10000471.37940900",     // Account balance    
                    "bc": "0"                     // Balance Change except PnL and Commission  
                }  
            ],  
            "P": [  
                {  
                    "s": "BTC-251123-126000-C",   // symbol   
                    "c": "-0.1000",               // position quantity  
                    "p": "-120.00000000",         // Position value    
                    "a": "1200.00000000"          // Average entry price     
                }  
            ]  
    }

---

# Balance 和 Position 更新推送

## 事件描述[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Balance-and-Position-Update#事件描述 "事件描述的直接链接")

账户更新事件的 event type 固定为 `ACCOUNT_UPDATE`

  * 当账户信息有变动时，会推送此事件：

    * 仅当账户信息有变动时(包括资金、仓位等发生变化)，才会推送此事件；
    * 订单状态变化没有引起账户和持仓变化的，不会推送此事件；
    * position 信息：仅当 symbol 仓位有变动时推送。
  * 字段"m"代表了事件推出的原因，包含了以下可能类型:

    * DEPOSIT
    * WITHDRAW
    * ORDER
  * 字段"bc"代表了钱包余额的改变量，即 balance change，但注意其不包含仓位盈亏及交易手续费。




## 事件类型[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Balance-and-Position-Update#事件类型 "事件��类型的直接链接")

`BALANCE_POSITION_UPDATE`

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/user-data-streams/Event-Balance-and-Position-Update#响应示例 "响应示例的直接链接")
    
    
    {  
            "e": "BALANCE_POSITION_UPDATE",  
            "E": 1762917544216,  
            "T": 1762917544206,  
            "m": "ORDER",  
            "B": [  
                {  
                    "a": "USDT",                  // 资产  
                    "b": "10000471.37940900",     // 钱包余额  
                    "bc": "0"                     // 除去盈亏与交易手续费以外的钱包余额改变量  
                }  
            ],  
            "P": [  
                {  
                    "s": "BTC-251123-126000-C",   // 交易对  
                    "c": "-0.1000",               // 仓位  
                    "p": "-120.00000000",         // 仓位价值   
                    "a": "1200.00000000"          // 仓位均价  
                }  
            ]  
    }