---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/Contract-Info-Stream
api_type: WebSocket
updated_at: 2026-01-15T23:47:56.623294
---

# Contract Info Stream

## Stream Description[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Contract-Info-Stream#stream-description "Direct link to Stream Description")

ContractInfo stream pushes when contract info updates(listing/settlement/contract bracket update). `bks` field only shows up when bracket gets updated.

## Stream Name[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Contract-Info-Stream#stream-name "Direct link to Stream Name")

`!contractInfo`

## Update Speed[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Contract-Info-Stream#update-speed "Direct link to Update Speed")

**Real-time**

## Response Example[​](/docs/derivatives/usds-margined-futures/websocket-market-streams/Contract-Info-Stream#response-example "Direct link to Response Example")
    
    
    {  
        "e":"contractInfo",          // Event Type  
        "E":1669356423908,           // Event Time  
        "s":"IOTAUSDT",              // Symbol  
        "ps":"IOTAUSDT",             // Pair  
        "ct":"PERPETUAL",            // Contract type  
        "dt":4133404800000,          // Delivery date time   
        "ot":1569398400000,          // onboard date time   
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

# 多资产模式资产汇率指数

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Contract-Info-Stream#数据流描述 "数据流描述的直接链接")

多资产模式资产价格指数

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Contract-Info-Stream#stream-name "Stream Name的直接链接")

`!assetIndex@arr`OR `<assetSymbol>@assetIndex`

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Contract-Info-Stream#更新速度 "更新速度的直接链接")

**1s**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Contract-Info-Stream#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
          "e":"assetIndexUpdate",  
          "E":1686749230000,  
          "s":"ADAUSD",         // asset index symbol  
          "i":"0.27462452",     // 指数价格  
          "b":"0.10000000",     // bid估值折扣  
          "a":"0.10000000",     // ask估值折扣  
          "B":"0.24716207",     // bid价格  
          "A":"0.30208698",     // ask价格  
          "q":"0.05000000",     // 自动兑换bid估值折扣  
          "g":"0.05000000",     // 自动兑换ask估值折扣  
          "Q":"0.26089330",     // 自动兑换bid价格  
          "G":"0.28835575"      // 自动兑换ask价格  
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