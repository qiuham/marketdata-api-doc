---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams
api_type: WebSocket
updated_at: 2026-01-15T23:43:45.952262
---

# Kline/Candlestick Streams

## Stream Description[​](/docs/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams#stream-description "Direct link to Stream Description")

The Kline/Candlestick Stream push updates to the current klines/candlestick every 1000 milliseconds (if existing).

**Kline/Candlestick chart intervals:**

m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

"1m", "3m", "5m", "15m" "30m" "1h", "2h", "4h", "6h", "12h", "1d", "3d", "1w",

## URL PATH[​](/docs/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams#url-path "Direct link to URL PATH")

`/market`

## Stream Name[​](/docs/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams#stream-name "Direct link to Stream Name")

`<symbol>@kline_<interval>`

## Update Speed[​](/docs/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams#update-speed "Direct link to Update Speed")

**1000ms**

## Response Example[​](/docs/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams#response-example "Direct link to Response Example")
    
    
    {  
        "e":"kline",                        // event type     
        "E":1638747660000,                  // event time     
        "s":"BTC-200630-9000-P",            // Option trading symbol     
        "k":{                               
            "t":1638747660000,              // kline start time     
            "T":1638747719999,              // kline end time    
            "s":"BTC-200630-9000-P",        // Option trading symbol     
            "i":"1m",                       // candle period     
            "f":0,                          // first trade ID    
            "L":0,                          // last trade ID     
            "o":"1000",                     // open     
            "c":"1000",                     // close     
            "h":"1000",                     // high      
            "l":"1000",                     // low     
            "v":"0",                        // volume(in contracts)     
            "n":0,                          // number of trades     
            "x":false,                      // current candle has been completed Y/N     
            "q":"0",                        // completed trade amount   (in quote asset)              
            "V":"0",                        // taker completed trade volume (in contracts)               
            "Q":"0"                         // taker trade amount(in quote asset)     
        }  
    }

---

# K线

## 数据流描述[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams#数据流描述 "数据流描述的直接链接")

K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。推送间隔1000毫秒(如有刷新)

**订阅Kline需要提供间隔参数，最短为分钟线，最长为月线。支持以下间隔:**

m -> 分钟; h -> 小时; d -> 天; w -> 周; M -> 月

  * 1m
  * 3m
  * 5m
  * 15m
  * 30m
  * 1h
  * 2h
  * 4h
  * 6h
  * 8h
  * 12h
  * 1d
  * 3d
  * 1w
  * 1M



## URL PATH[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams#url-path "URL PATH的直接链接")

`/market`

## Stream Name[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams#stream-name "Stream Name的直接链接")

`<symbol>@kline_<interval>`

## 更新速度[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams#更新速度 "更新速度的直接链接")

**1000ms**

## 响应示例[​](/docs/zh-CN/derivatives/options-trading/websocket-market-streams/Kline-Candlestick-Streams#响应示例 "响应示例的直接链接")
    
    
    {  
        "e":"kline",                        // 事件类型  
        "E":1638747660000,                  // 事件时间  
        "s":"BTC-200630-9000-P",            // 交易对    
        "k":{                               
            "t":1638747660000,              // 这根K线的起始时间  
            "T":1638747719999,              // 这根K线的结束时间  
            "s":"BTC-200630-9000-P",        // 交易对    
            "i":"1m",                       // K线间隔  
            "f":0,                          // 这根K线期间第一笔成交ID  
            "L":0,                          // 这根K线期间末一笔成交ID  
            "o":"1000",                     // 这根K线期间第一笔成交价     
            "c":"1000",                     // 这根K线期间末一笔成交价     
            "h":"1000",                     // 这根K线期间最高成交价      
            "l":"1000",                     // 这根K线期间最低成交价     
            "v":"0",                        // 这根K线期间成交量     
            "n":0,                          // 这根K线期间成交笔数  
            "x":false,                      // 这根K线是否完结(是否已经开始下一根K线)  
            "q":"0",                        // 这根K线期间成交额  
            "V":"0",                        // 主动买入的成交额  
            "Q":"0"                         // 主动买入的成交量  
        }  
    }