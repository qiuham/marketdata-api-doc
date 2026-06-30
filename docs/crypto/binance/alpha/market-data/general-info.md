---
exchange: binance
source_url: https://developers.binance.com/docs/alpha/market-data/general-info
api_type: WebSocket
updated_at: 2026-06-30 19:11:30.085991
---

# WebSocket Market Data API

## Basic Info[​](/docs/alpha/market-data/websocket-market-data#basic-info "Direct link to Basic Info")

  * The base URL for all WSS endpoints listed in this document is: `wss://nbstream.binance.com/w3w/wsa/stream`



## Subscribe / Unsubscribe Streams in Real Time[​](/docs/alpha/market-data/websocket-market-data#subscribe--unsubscribe-streams-in-real-time "Direct link to Subscribe / Unsubscribe Streams in Real Time")

  * You can subscribe to or unsubscribe from streams by sending messages over WebSocket. Examples are shown below.
  * The `id` in the request is used as a unique identifier to correlate request/response messages. The following formats are accepted: 
    * 64-bit signed integer
    * Alphanumeric string; max length 36
    * null
  * If `result` in the corresponding response is `null`, it indicates the request was sent successfully.



### Subscribe to a stream[​](/docs/alpha/market-data/websocket-market-data#subscribe-to-a-stream "Direct link to Subscribe to a stream")

Request
    
    
    {  
      "method": "SUBSCRIBE",  
      "params": [  
        "came@allTokens@ticker24"  
      ],  
      "id": 1  
    }  
    

Response
    
    
    {  
      "result": null,  
      "id": 1  
    }  
    

* * *

### Unsubscribe from a stream[​](/docs/alpha/market-data/websocket-market-data#unsubscribe-from-a-stream "Direct link to Unsubscribe from a stream")

Request
    
    
    {  
      "method": "UNSUBSCRIBE",  
      "params": [  
        "came@allTokens@ticker24"  
      ],  
      "id": 1  
    }  
    

Response
    
    
    {  
      "result": null,  
      "id": 1  
    }  
    

* * *

### List current subscriptions[​](/docs/alpha/market-data/websocket-market-data#list-current-subscriptions "Direct link to List current subscriptions")

Request
    
    
    {  
      "method": "LIST_SUBSCRIPTION",  
      "id": 3  
    }  
    

Response
    
    
    {  
      "result": ["came@allTokens@ticker24"],  
      "id": 3  
    }  
    

* * *

## Streams[​](/docs/alpha/market-data/websocket-market-data#streams "Direct link to Streams")

### came@allTokens@ticker24[​](/docs/alpha/market-data/websocket-market-data#camealltokensticker24 "Direct link to came@allTokens@ticker24")
    
    
    {  
      "data": {  
        "d": [  
          {  
            "ca": "0x8fce7206e3043dd360f115afa956ee31b90b787c@56", // Contract address@Chain ID  
            "cnt24": 10426, // Number of trades in the last 24h  
            "fdv": "72834145.18711072", // Fully Diluted Valuation (FDV)  
            "hc": "6822", // Number of holders  
            "liq": "1442996.98151177662835", // Liquidity  
            "mc": "13542034.24008014", // Market cap  
            "p": "0.072849536538593663", // Current price  
            "pc24": "-2.32", // 24h price change %  
            "s": "1",  
            "t": 1771825733000, // Timestamp (ms)  
            "vol24": "12930712.213702157742688594285" // 24h volume  
          }  
        ],  
        "e": "tickerList"  
      },  
      "stream": "came@allTokens@ticker24"  
    }  
    

* * *

### <symbol>@aggTrade[​](/docs/alpha/market-data/websocket-market-data#symbolaggtrade "Direct link to <symbol>@aggTrade")
    
    
    {  
      "data": {  
        "E": 1771828569861, // Event time (ms)  
        "T": 1771828569702, // Trade time (ms)  
        "a": 2684294, // Aggregated trade ID  
        "e": "aggTrade", // Event type  
        "f": 2684294, // First trade ID in the aggregation  
        "l": 2684294, // Last trade ID in the aggregation  
        "m": false, // Is the buyer the market maker  
        "p": "0.08530000", // Price  
        "q": "879.24000000", // Quantity  
        "s": "ALPHA_474USDT" // Symbol  
      },  
      "stream": "alpha_474usdt@aggTrade"  
    }  
    

* * *

### <symbol>@fulldepth@<interval>[​](/docs/alpha/market-data/websocket-market-data#symbolfulldepthinterval "Direct link to <symbol>@fulldepth@<interval>")

interval: 0ms, 100ms, 500ms  
This stream returns all available depth, which includes UI and API orders.
    
    
    {  
      "data": {  
        "E": 1771828614381, // Event time (ms)  
        "T": 1771828614258, // Matching time (ms)  
        "U": 42648947917, // First updateId in this event  
        "a": [  
          ["0.07680652", "0.00000000"],  
          ["0.08529794", "0.00000000"]  
        ],  
        "b": [  
          ["0.08513788", "0.00000000"],  
          ["0.08520502", "23.47000000"],  
          ["0.08521196", "320.94000000"],  
          ["0.08529880", "0.00000000"],  
          ["0.08529885", "0.00000000"]  
        ],  
        "e": "depthUpdate",  
        "pu": 42648947321, // Previous updateId from the last push  
        "s": "ALPHA_474USDT",  
        "u": 42648948229 // Last updateId in this event  
      },  
      "stream": "alpha_474usdt@fulldepth@500ms"  
    }  
    

* * *

### came@contractAddress@chainId@kline_<interval>[​](/docs/alpha/market-data/websocket-market-data#camecontractaddresschainidkline_interval "Direct link to came@contractAddress@chainId@kline_<interval>")

interval: 1s, 1m, 5m, 15m, 1h, 4h, 1d
    
    
    {  
      "data": {  
        "ca": "G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG@CT_501", // Contract address@Chain ID  
        "e": "kline",  
        "k": {  
          "c": "0.15584957424118055058", // Close price  
          "ct": 1771828656000, // Kline close time  
          "h": "0.15584957424118055058", // High price  
          "i": "1s", // Interval  
          "l": "0.15584372258086979622", // Low price  
          "o": "0.15584372258086979622", // Open price  
          "ot": 1771828655000, // Kline open time  
          "v": "2.8584092999332775480" // Volume  
        }  
      },  
      "stream": "came@G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG@CT_501@kline_1s"  
    }  
    

* * *

### <symbol>@bookTicker[​](/docs/alpha/market-data/websocket-market-data#symbolbookticker "Direct link to <symbol>@bookTicker")
    
    
    {  
      "data": {  
        "A": "2.00353200", // ask1Quantity  
        "B": "0.91076900", // bid1Quantity  
        "E": 1773108379067, // eventTime  
        "T": 1773108379054, // transactionTime  
        "a": "9.30000000", // ask1Price  
        "b": "8.30000000", // bid1Price  
        "e": "bookTicker", // eventType  
        "s": "ALPHA_116USDT", // symbol  
        "u": 6663207693 // updateId  
      },  
      "stream": "alpha_116usdt@bookTicker"  
    }  
    

* * *

### !bookTicker[​](/docs/alpha/market-data/websocket-market-data#bookticker "Direct link to !bookTicker")
    
    
    {  
      "data": {  
        "A": "2.00353200", // ask1Quantity  
        "B": "0.91076900", // bid1Quantity  
        "E": 1773108379067, // eventTime  
        "T": 1773108379054, // transactionTime  
        "a": "9.30000000", // ask1Price  
        "b": "8.30000000", // bid1Price  
        "e": "bookTicker", // eventType  
        "s": "ALPHA_116USDT", // symbol  
        "u": 6663207693 // updateId  
      },  
      "stream": "!bookTicker"  
    }  
    

* * *

### <symbol>@miniTicker[​](/docs/alpha/market-data/websocket-market-data#symbolminiticker "Direct link to <symbol>@miniTicker")
    
    
    {  
      "data": {  
        "E": 1773109449908, // eventTime  
        "c": "8.40000000", // closePrice  
        "e": "24hrMiniTicker", // eventType  
        "h": "8.50000000", // highPrice  
        "l": "8.30000000", // lowPrice  
        "o": "8.40000000", // openPrice  
        "q": "543810.36005090", // quoteVolume  
        "s": "ALPHA_116USDT", // symbol  
        "v": "64739.03978900" // volume  
      },  
      "stream": "alpha_116usdt@miniTicker"  
    }  
    

* * *

### !miniTicker@arr[​](/docs/alpha/market-data/websocket-market-data#minitickerarr "Direct link to !miniTicker@arr")
    
    
    {  
      "data": {  
        "E": 1773109449908, // eventTime  
        "c": "8.40000000", // closePrice  
        "e": "24hrMiniTicker", // eventType  
        "h": "8.50000000", // highPrice  
        "l": "8.30000000", // lowPrice  
        "o": "8.40000000", // openPrice  
        "q": "543810.36005090", // quoteVolume  
        "s": "ALPHA_116USDT", // symbol  
        "v": "64739.03978900" // volume  
      },  
      "stream": "!miniTicker@arr"  
    }  
    

* * *

### <symbol>@ticker[​](/docs/alpha/market-data/websocket-market-data#symbolticker "Direct link to <symbol>@ticker")
    
    
    {  
      "data": {  
        "C": 1773109631555, // endTime  
        "E": 1773109631569, // eventTime  
        "F": 19847634, // firstTradeId  
        "L": 19911287, // lastTradeId  
        "O": 1773023220000, // startTime  
        "P": "0.00", // priceChangePercent  
        "Q": "0.49293200", // lastTradeVolume  
        "c": "8.40000000", // closePrice  
        "e": "24hrTicker", // eventType  
        "h": "8.50000000", // highPrice  
        "l": "8.30000000", // lowPrice  
        "n": 217505, // tradeNum  
        "o": "8.40000000", // openPrice  
        "p": "0.00000000", // priceChange  
        "q": "543907.35169250", // quoteVolume  
        "s": "ALPHA_116USDT", // symbol  
        "v": "64750.63418500", // volume  
        "w": "8.40003127" // averagePrice  
      },  
      "stream": "alpha_116usdt@ticker"  
    }  
    

* * *

### !ticker@arr[​](/docs/alpha/market-data/websocket-market-data#tickerarr "Direct link to !ticker@arr")
    
    
    {  
      "data": {  
        "C": 1773109631555, // endTime  
        "E": 1773109631569, // eventTime  
        "F": 19847634, // firstTradeId  
        "L": 19911287, // lastTradeId  
        "O": 1773023220000, // startTime  
        "P": "0.00", // priceChangePercent  
        "Q": "0.49293200", // lastTradeVolume  
        "c": "8.40000000", // closePrice  
        "e": "24hrTicker", // eventType  
        "h": "8.50000000", // highPrice  
        "l": "8.30000000", // lowPrice  
        "n": 217505, // tradeNum  
        "o": "8.40000000", // openPrice  
        "p": "0.00000000", // priceChange  
        "q": "543907.35169250", // quoteVolume  
        "s": "ALPHA_116USDT", // symbol  
        "v": "64750.63418500", // volume  
        "w": "8.40003127" // averagePrice  
      },  
      "stream": "!ticker@arr"  
    }  
    

* * *

### <symbol>@trade[​](/docs/alpha/market-data/websocket-market-data#symboltrade "Direct link to <symbol>@trade")
    
    
    {  
      "data": {  
        "E": 1773110023891, // eventTime  
        "T": 1773110023877, // tradeTime  
        "e": "trade", // eventType  
        "m": false, // isBuyerMaker  
        "p": "8.40000000", // fillPrice  
        "q": "0.97915700", // fillQty  
        "s": "ALPHA_116USDT", // symbol  
        "t": 19911650 // tradeId  
      },  
      "stream": "alpha_116usdt@trade"  
    }  
    

* * *

### <symbol>@depth<levels>@<interval>[​](/docs/alpha/market-data/websocket-market-data#symboldepthlevelsinterval "Direct link to <symbol>@depth<levels>@<interval>")

levels: optional, available values: [5, 10, 20]  
interval: optional, available values: [0ms, 100ms, 500ms]  
Please note that only UI orders will be shown.
    
    
    {  
      "data": {  
        "E": 1773110222878, // eventTime  
        "T": 1773110222767, // transactionTime  
        "U": 6663367135, // firstUpdateId  
        "a": [  
          [  
            "8.30000000", // price  
            "8.02776700" // qty  
          ]  
        ],  
        "b": [  
          [  
            "8.40000000", // price  
            "1266.84789600" // qty  
          ]  
        ],  
        "e": "depthUpdate", // eventType  
        "pu": 6663366971, // previousUpdateId  
        "s": "ALPHA_116USDT", // symbol  
        "u": 6663367147 // lastUpdateId  
      },  
      "stream": "alpha_116usdt@depth"  
    }  
    

* * *

### <symbol>@kline_<interval>[​](/docs/alpha/market-data/websocket-market-data#symbolkline_interval "Direct link to <symbol>@kline_<interval>")

available values: [1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M]
    
    
    {  
      "data": {  
        "E": 1773111055144, // eventTime  
        "e": "kline", // eventType  
        "k": {  
          "B": "0", // ignore  
          "L": 19912765, // lastTradeId  
          "Q": "534.64960920", // takerBuyQuoteAssetVolume  
          "T": 1773111059999, // endTime  
          "V": "63.64876300", // takerBuyBaseAssetVolume  
          "c": "8.40000000", // closePrice  
          "f": 19912696, // firstTradeId  
          "h": "8.40000000", // highPrice  
          "i": "1m", // interval  
          "l": "8.40000000", // lowPrice  
          "n": 218, // tradeNum  
          "o": "8.40000000", // openPrice  
          "q": "534.64960920", // quoteAssetVolume  
          "s": "ALPHA_116USDT", // symbol  
          "t": 1773111000000, // startTime  
          "v": "63.64876300", // volume  
          "x": false // klineComplete  
        },  
        "s": "ALPHA_116USDT" // symbol  
      },  
      "stream": "alpha_116usdt@kline_1m"  
    }

---

# WebSocket 行情接口

## 基本信息[​](/docs/zh-CN/alpha/market-data/websocket-market-data#基本信息 "基本信息的直接链接")

  * 本篇所列出的所有wss接口的baseurl为: `wss://nbstream.binance.com/w3w/wsa/stream`



## 实时订阅/取消数据流[​](/docs/zh-CN/alpha/market-data/websocket-market-data#实时订阅取消数据流 "实时订阅/取消数据流的直接链接")

  * 以下数据可以通过 WebSocket 发送以实现订阅或取消订阅数据流。示例如下.
  * 请求中的id被用作唯一标识来区分来回传递的消息。以下格式被接受: 
    * 64位有符号整数
    * 字母数字字符串；最大长度36
    * null
  * 如果相应内容中的result 为 null，表示请求发送成功。



### 订阅一个信息流[​](/docs/zh-CN/alpha/market-data/websocket-market-data#订阅一个信息流 "订阅一个信息流的直接链接")

请求
    
    
    {  
        "method": "SUBSCRIBE",  
        "params": [  
            "came@allTokens@ticker24"  
        ],  
        "id": 1  
    }  
    

响应
    
    
    {  
      "result": null,  
      "id": 1  
    }  
    

* * *

### 取消订阅一个信息流[​](/docs/zh-CN/alpha/market-data/websocket-market-data#取消订阅一个信息流 "取消订阅一个信息流的直接链接")

请求
    
    
    {  
        "method": "UNSUBSCRIBE",  
        "params": [  
            "came@allTokens@ticker24"  
        ],  
        "id": 1  
    }  
    

响应
    
    
    {  
      "result": null,  
      "id": 1  
    }  
    

* * *

### 已订阅信息流[​](/docs/zh-CN/alpha/market-data/websocket-market-data#已订阅信息流 "已订阅信息流的直接链接")

请求
    
    
    {  
        "method": "LIST_SUBSCRIPTION",  
        "id": 3  
    }  
    

响应
    
    
    {  
        "result": ["came@allTokens@ticker24"],  
        "id": 3  
    }  
    

* * *

## Streams[​](/docs/zh-CN/alpha/market-data/websocket-market-data#streams "Streams的直接链接")

### came@allTokens@ticker24[​](/docs/zh-CN/alpha/market-data/websocket-market-data#camealltokensticker24 "came@allTokens@ticker24的直接链接")
    
    
    {  
        "data": {  
            "d": [  
                {  
                    "ca": "0x8fce7206e3043dd360f115afa956ee31b90b787c@56", // 合约地址@链ID  
                    "cnt24": 10426, // 24小时成交笔数  
                    "fdv": "72834145.18711072", // 完全稀释市值 (FDV)  
                    "hc": "6822", // 持有者数量  
                    "liq": "1442996.98151177662835", // 流动性  
                    "mc": "13542034.24008014", // 市值  
                    "p": "0.072849536538593663", // 当前价格  
                    "pc24": "-2.32", // 24小时价格变化%  
                    "s": "1",  
                    "t": 1771825733000, // 时间戳 (ms)  
                    "vol24": "12930712.213702157742688594285" // 24小时交易量  
                }  
            ],  
            "e": "tickerList"  
        },  
        "stream": "came@allTokens@ticker24"  
    }  
    

* * *

### <symbol>@aggTrade[​](/docs/zh-CN/alpha/market-data/websocket-market-data#symbolaggtrade "<symbol>@aggTrade的直接链接")
    
    
    {  
        "data": {  
            "E": 1771828569861, // 事件时间 (ms)  
            "T": 1771828569702, // 成交时间 (ms)  
            "a": 2684294, // 聚合交易ID  
            "e": "aggTrade", // 事件类型  
            "f": 2684294, // 被归集的首个交易ID  
            "l": 2684294, // 末个交易ID  
            "m": false, // 是否为做市方  
            "p": "0.08530000", // 成交价格  
            "q": "879.24000000", // 成交数量  
            "s": "ALPHA_474USDT" // 交易对符号  
        },  
        "stream": "alpha_474usdt@aggTrade"  
    }  
    

* * *

### <symbol>@fulldepth@<interval>[​](/docs/zh-CN/alpha/market-data/websocket-market-data#symbolfulldepthinterval "<symbol>@fulldepth@<interval>的直接链接")

interval: 0ms, 100ms, 500ms  
这条数据流会返回所有可用的深度信息，其中包括 UI 和 API 的订单
    
    
    {  
        "data": {  
            "E": 1771828614381, // 事件时间 (ms)  
            "T": 1771828614258, // 撮合时间 (ms)  
            "U": 42648947917, // 本次更新首个updateId  
            "a": [  
                [  
                    "0.07680652",  
                    "0.00000000"  
                ],  
                [  
                    "0.08529794",  
                    "0.00000000"  
                ]  
            ],  
            "b": [  
                [  
                    "0.08513788",  
                    "0.00000000"  
                ],  
                [  
                    "0.08520502",  
                    "23.47000000"  
                ],  
                [  
                    "0.08521196",  
                    "320.94000000"  
                ],  
                [  
                    "0.08529880",  
                    "0.00000000"  
                ],  
                [  
                    "0.08529885",  
                    "0.00000000"  
                ]  
            ],  
            "e": "depthUpdate",  
            "pu": 42648947321, // 上次推送的updateId  
            "s": "ALPHA_474USDT",  
            "u": 42648948229 // 本次更新末个updateId  
        },  
        "stream": "alpha_474usdt@fulldepth@500ms"  
    }  
    

* * *

### came@contractAddress@chainId@kline_<interval>[​](/docs/zh-CN/alpha/market-data/websocket-market-data#camecontractaddresschainidkline_interval "came@contractAddress@chainId@kline_<interval>的直接链接")

interval: 1s, 1m, 5m, 15m, 1h, 4h, 1d
    
    
    {  
        "data": {  
            "ca": "G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG@CT_501", // 合约地址@链ID  
            "e": "kline",  
            "k": {  
                "c": "0.15584957424118055058", // 收盘价  
                "ct": 1771828656000, // k线结束时间  
                "h": "0.15584957424118055058", // 最高价  
                "i": "1s", // interval  
                "l": "0.15584372258086979622", // 最低价  
                "o": "0.15584372258086979622", // 开盘价  
                "ot": 1771828655000, // k线开始时间  
                "v": "2.8584092999332775480" // 成交量  
            }  
        },  
        "stream": "came@G7vQWurMkMMm2dU3iZpXYFTHT9Biio4F4gZCrwFpKNwG@CT_501@kline_1s"  
    }  
    

* * *

### <symbol>@bookTicker[​](/docs/zh-CN/alpha/market-data/websocket-market-data#symbolbookticker "<symbol>@bookTicker的直接链接")
    
    
    {  
      "data": {  
        "A": "2.00353200", // 卖一数量  
        "B": "0.91076900", // 买一数量  
        "E": 1773108379067, // 事件时间  
        "T": 1773108379054, // 成交时间/交易时间  
        "a": "9.30000000", // 卖一价格  
        "b": "8.30000000", // 买一价格  
        "e": "bookTicker", // 事件类型  
        "s": "ALPHA_116USDT", // 交易对  
        "u": 6663207693 // 更新 ID  
      },  
      "stream": "alpha_116usdt@bookTicker"  
    }  
    

* * *

### !bookTicker[​](/docs/zh-CN/alpha/market-data/websocket-market-data#bookticker "!bookTicker的直接链接")
    
    
    {  
      "data": {  
        "A": "2.00353200", // 卖一数量  
        "B": "0.91076900", // 买一数量  
        "E": 1773108379067, // 事件时间  
        "T": 1773108379054, // 成交时间/交易时间  
        "a": "9.30000000", // 卖一价格  
        "b": "8.30000000", // 买一价格  
        "e": "bookTicker", // 事件类型  
        "s": "ALPHA_116USDT", // 交易对  
        "u": 6663207693 // 更新 ID  
      },  
      "stream": "!bookTicker"  
    }  
    

* * *

### <symbol>@miniTicker[​](/docs/zh-CN/alpha/market-data/websocket-market-data#symbolminiticker "<symbol>@miniTicker的直接链接")
    
    
    {  
      "data": {  
        "E": 1773109449908, // 事件时间  
        "c": "8.40000000", // 收盘价  
        "e": "24hrMiniTicker", // 事件类型  
        "h": "8.50000000", // 最高价  
        "l": "8.30000000", // 最低价  
        "o": "8.40000000", // 开盘价  
        "q": "543810.36005090", // 计价资产成交额  
        "s": "ALPHA_116USDT", // 交易对  
        "v": "64739.03978900" // 基础资产成交量  
      },  
      "stream": "alpha_116usdt@miniTicker"  
    }  
    

* * *

### !miniTicker@arr[​](/docs/zh-CN/alpha/market-data/websocket-market-data#minitickerarr "!miniTicker@arr的直接链接")
    
    
    {  
      "data": {  
        "E": 1773109449908, // 事件时间  
        "c": "8.40000000", // 收盘价  
        "e": "24hrMiniTicker", // 事件类型  
        "h": "8.50000000", // 最高价  
        "l": "8.30000000", // 最低价  
        "o": "8.40000000", // 开盘价  
        "q": "543810.36005090", // 计价资产成交额  
        "s": "ALPHA_116USDT", // 交易对  
        "v": "64739.03978900" // 基础资产成交量  
      },  
      "stream": "!miniTicker@arr"  
    }  
    

* * *

### <symbol>@ticker[​](/docs/zh-CN/alpha/market-data/websocket-market-data#symbolticker "<symbol>@ticker的直接链接")
    
    
    {  
      "data": {  
        "C": 1773109631555, // 统计结束时间  
        "E": 1773109631569, // 事件时间  
        "F": 19847634, // 首笔成交 ID  
        "L": 19911287, // 末笔成交 ID  
        "O": 1773023220000, // 统计开始时间  
        "P": "0.00", // 涨跌幅  
        "Q": "0.49293200", // 最近一笔成交量  
        "c": "8.40000000", // 收盘价  
        "e": "24hrTicker", // 事件类型  
        "h": "8.50000000", // 最高价  
        "l": "8.30000000", // 最低价  
        "n": 217505, // 成交笔数  
        "o": "8.40000000", // 开盘价  
        "p": "0.00000000", // 涨跌额  
        "q": "543907.35169250", // 计价资产成交额  
        "s": "ALPHA_116USDT", // 交易对  
        "v": "64750.63418500", // 基础资产成交量  
        "w": "8.40003127" // 平均价  
      },  
      "stream": "alpha_116usdt@ticker"  
    }  
    

* * *

### !ticker@arr[​](/docs/zh-CN/alpha/market-data/websocket-market-data#tickerarr "!ticker@arr的直接链接")
    
    
    {  
      "data": {  
        "C": 1773109631555, // 统计结束时间  
        "E": 1773109631569, // 事件时间  
        "F": 19847634, // 首笔成交 ID  
        "L": 19911287, // 末笔成交 ID  
        "O": 1773023220000, // 统计开始时间  
        "P": "0.00", // 涨跌幅  
        "Q": "0.49293200", // 最近一笔成交量  
        "c": "8.40000000", // 收盘价  
        "e": "24hrTicker", // 事件类型  
        "h": "8.50000000", // 最高价  
        "l": "8.30000000", // 最低价  
        "n": 217505, // 成交笔数  
        "o": "8.40000000", // 开盘价  
        "p": "0.00000000", // 涨跌额  
        "q": "543907.35169250", // 计价资产成交额  
        "s": "ALPHA_116USDT", // 交易对  
        "v": "64750.63418500", // 基础资产成交量  
        "w": "8.40003127" // 平均价  
      },  
      "stream": "!ticker@arr"  
    }  
    

* * *

### <symbol>@trade[​](/docs/zh-CN/alpha/market-data/websocket-market-data#symboltrade "<symbol>@trade的直接链接")
    
    
    {  
      "data": {  
        "E": 1773110023891, // 事件时间  
        "T": 1773110023877, // 成交时间  
        "e": "trade", // 事件类型  
        "m": false, // 是否为买方挂单成交  
        "p": "8.40000000", // 成交价  
        "q": "0.97915700", // 成交量  
        "s": "ALPHA_116USDT", // 交易对  
        "t": 19911650 // 成交 ID  
      },  
      "stream": "alpha_116usdt@trade"  
    }  
    

* * *

### <symbol>@depth<levels>@<interval>[​](/docs/zh-CN/alpha/market-data/websocket-market-data#symboldepthlevelsinterval "<symbol>@depth<levels>@<interval>的直接链接")

levels：可选，取值：[5, 10, 20]  
interval：可选，取值：[0ms, 100ms, 500ms]  
请注意：这里只会展示 UI 订单。
    
    
    {  
      "data": {  
        "E": 1773110222878, // 事件时间  
        "T": 1773110222767, // 成交时间/交易时间  
        "U": 6663367135, // 首个更新 ID  
        "a": [  
          [  
            "8.30000000", // 价格  
            "8.02776700" // 数量  
          ]  
        ],  
        "b": [  
          [  
            "8.40000000", // 价格  
            "1266.84789600" // 数量  
          ]  
        ],  
        "e": "depthUpdate", // 事件类型  
        "pu": 6663366971, // 上一个更新 ID  
        "s": "ALPHA_116USDT", // 交易对  
        "u": 6663367147 // 最后更新 ID  
      },  
      "stream": "alpha_116usdt@depth"  
    }  
    

* * *

### <symbol>@kline_<interval>[​](/docs/zh-CN/alpha/market-data/websocket-market-data#symbolkline_interval "<symbol>@kline_<interval>的直接链接")

可选 interval 取值：[1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M]
    
    
    {  
      "data": {  
        "E": 1773111055144, // 事件时间  
        "e": "kline", // 事件类型  
        "k": {  
          "B": "0", // 忽略  
          "L": 19912765, // 末笔成交 ID  
          "Q": "534.64960920", // 主动买入成交额  
          "T": 1773111059999, // K 线结束时间  
          "V": "63.64876300", // 主动买入成交量  
          "c": "8.40000000", // 收盘价  
          "f": 19912696, // 首笔成交 ID  
          "h": "8.40000000", // 最高价  
          "i": "1m", // K 线周期  
          "l": "8.40000000", // 最低价  
          "n": 218, // 成交笔数  
          "o": "8.40000000", // 开盘价  
          "q": "534.64960920", // 成交额  
          "s": "ALPHA_116USDT", // 交易对  
          "t": 1773111000000, // K 线开始时间  
          "v": "63.64876300", // 成交量  
          "x": false // K 线是否已完结  
        },  
        "s": "ALPHA_116USDT" // 交易对  
      },  
      "stream": "alpha_116usdt@kline_1m"  
    }