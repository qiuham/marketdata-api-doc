---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/coin-margined-futures/websocket-market-streams/Contract-Info-Stream
api_type: WebSocket
updated_at: 2026-01-15T23:40:32.306113
---

# Contract Info Stream

## Stream Description[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Contract-Info-Stream#stream-description "Direct link to Stream Description")

ContractInfo stream pushes when contract info updates(listing/settlement/contract bracket update). `bks` field only shows up when bracket gets updated.

## Stream Name[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Contract-Info-Stream#stream-name "Direct link to Stream Name")

`!contractInfo`

## Update Speed[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Contract-Info-Stream#update-speed "Direct link to Update Speed")

**Real-time**

## Response Example[​](/docs/derivatives/coin-margined-futures/websocket-market-streams/Contract-Info-Stream#response-example "Direct link to Response Example")
    
    
    {  
        "e":"contractInfo",          // Event Type  
        "E":1669647330375,           // Event Time  
        "s":"APTUSD_PERP",           // Symbol  
        "ps":"APTUSD",               // Pair  
        "ct":"PERPETUAL",            // Contract type  
        "dt":4133404800000,          // Delivery date time   
        "ot":1666594800000,          // onboard date time   
        "cs":"TRADING",              // Contract status   
        "bks":[  
            {  
                "bs":1,              // Notional bracket  
                "bnf":0,             // Floor notional of this bracket  
                "bnc":5000,          // Cap notional of this bracket  
                "mmr":0.01,          // Maintenance ratio for this bracket  
                "cf":0,              // Auxiliary number for quick calculation   
                "mi":21,             // Min leverage for this bracket  
                "ma":50              // Max leverage for this bracket  
            },  
            {  
                "bs":2,  
                "bnf":5000,  
                "bnc":25000,  
                "mmr":0.025,  
                "cf":75,  
                "mi":11,  
                "ma":20  
            }  
        ]  
    }

---

# 交易对信息信息流

## 数据流描述[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Contract-Info-Stream#数据流描述 "数据流描述的直接链接")

Symbol状态更改时推送（上架/下架/bracket调整）; `bks`仅在bracket调整时推出。

## Stream Name[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Contract-Info-Stream#stream-name "Stream Name的直接链接")

`!contractInfo`

## 更新速度[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Contract-Info-Stream#更新速度 "更新速度的直接链接")

**实时**

## 响应示例[​](/docs/zh-CN/derivatives/coin-margined-futures/websocket-market-streams/Contract-Info-Stream#响应示例 "响应示例的直接链接")
    
    
    {  
        "e":"contractInfo",      // 事件类型  
        "E":1669647330375,       // 事件时间  
        "s":"APTUSD_PERP",       // 交易对  
        "ps":"APTUSD",           // 交易对标的  
        "ct":"PERPETUAL",        // 合约类型  
        "dt":4133404800000,      // 结算时间  
        "ot":1666594800000,      // 上架时间  
        "cs":"TRADING",          // 交易对状态  
        "bks":[  
            {  
                "bs":1,          // 层级  
                "bnf":0,         // 该层对应的名义价值下限  
                "bnc":500000,    // 该层对应的名义价值上限  
                "mmr":0.0065,    // 该层对应的维持保证金率  
                "cf":0.0,        // 速算数  
                "mi":51,         // 该层杠杆下界  
                "ma":75          // 该层杠杆上界  
            },  
            {  
                "bs":2,  
                "bnf":5000,  
                "bnc":25000,  
                "mmr":0.025,  
                "cf":75,  
                "mi":11,  
                "ma":20  
            }  
        ]  
    }