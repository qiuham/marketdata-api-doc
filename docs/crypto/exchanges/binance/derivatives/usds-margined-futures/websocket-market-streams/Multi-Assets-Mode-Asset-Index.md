---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Multi-Assets-Mode-Asset-Index
api_type: WebSocket
updated_at: 2026-01-15T23:48:08.137381
---

# Multi-Assets Mode Asset Index

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Multi-Assets-Mode-Asset-Index#stream-description "Direct link to Stream Description")

Asset index for multi-assets mode user

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Multi-Assets-Mode-Asset-Index#stream-name "Direct link to Stream Name")

`!assetIndex@arr` OR `<assetSymbol>@assetIndex`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Multi-Assets-Mode-Asset-Index#update-speed "Direct link to Update Speed")

**1s**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Multi-Assets-Mode-Asset-Index#response-example "Direct link to Response Example")
    
    
    [  
        {  
          "e":"assetIndexUpdate",  
          "E":1686749230000,  
          "s":"ADAUSD",           // asset index symbol  
          "i":"0.27462452",       // index price  
          "b":"0.10000000",       // bid buffer  
          "a":"0.10000000",       // ask buffer  
          "B":"0.24716207",       // bid rate  
          "A":"0.30208698",       // ask rate  
          "q":"0.05000000",       // auto exchange bid buffer  
          "g":"0.05000000",       // auto exchange ask buffer   
          "Q":"0.26089330",       // auto exchange bid rate  
          "G":"0.28835575"        // auto exchange ask rate  
        },  
        {  
          "e":"assetIndexUpdate",  
          "E":1686749230000,  
          "s":"USDTUSD",  
          "i":"0.99987691",    
          "b":"0.00010000",  
          "a":"0.00010000",  
          "B":"0.99977692",  
          "A":"0.99997689",  
          "q":"0.00010000",  
          "g":"0.00010000",  
          "Q":"0.99977692",  
          "G":"0.99997689"  
        }  
    ]

---

# 交易对信息信息流

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Multi-Assets-Mode-Asset-Index#数据流描述 "数据流描述的直接链接")

Symbol状态更改时推送（上架/下架/bracket调整）; `bks`仅在bracket调整时推出。

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Multi-Assets-Mode-Asset-Index#stream-name "Stream Name的直接链接")

`!contractInfo`

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Multi-Assets-Mode-Asset-Index#更新速度 "更新速度的直接链接")

**实时**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Multi-Assets-Mode-Asset-Index#响应示例 "响应示例的直接链接")
    
    
    {  
        "e":"contractInfo",      // 事件类型  
        "E":1669356423908,       // 事件时间  
        "s":"IOTAUSDT",          // 交易对  
        "ps":"IOTAUSDT",         // 交易对标的  
        "ct":"PERPETUAL",        // 合约类型  
        "dt":4133404800000,      // 结算时间  
        "ot":1569398400000,      // 上架时间  
        "cs":"TRADING",          // 交易对状态  
        "bks":[  
            {  
                "bs":1,          // 层级  
                "bnf":0,         // 该层对应的名义价值下限  
                "bnc":5000,      // 该层对应的名义价值上限  
                "mmr":0.01,      // 该层对应的维持保证金率  
                "cf":0,          // 速算数  
                "mi":21,         // 该层杠杆下界  
                "ma":50          // 该层杠杆上界  
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