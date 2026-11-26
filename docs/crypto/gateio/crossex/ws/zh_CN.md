---
exchange: gateio
source_url: https://www.gate.com/docs/developers/crossex/ws/zh_CN
api_type: WebSocket
updated_at: 2026-11-26 18:59:32.709604
---

# CrossEx WebSocket v1.0.0

* Python 
  * Shell 

v1.0.0 · Stable


CrossEx 提供简单而强大的 Websocket API，将交易状态集成到您的业务或应用程序中。

##  服务器地址

  * 线上地址： 
    * 公有行情：wss://api.gateio.ws/ws/crossex/public
    * 私有推送：wss://api.gateio.ws/ws/crossex
  * 心跳：客户端应每 30 秒内发送一次协议层 Ping 帧。公有连接也接受内容为 `ping` 的文本帧并返回 `pong` 文本帧。私有连接另有应用层心跳。
  * 私有连接数量限制：每个 UID 和频道最多 20 个连接。
  * 公有连接限额按服务器配置执行。默认每 IP 最多 100 个连接、每 IP 每分钟最多 60 次操作、每个连接的每个频道最多订阅 1000 个交易对。

##  变更日志

**Oct 12 2026**

  1. CrossEx新增美股、港股、韩股和日股股票及ETF行情、订单和证券仓位推送
  2. 新增证券仓位订阅频道（security_position）

**Sep 15 2026**

  1. CrossEx新增支持LIGHTER交易所

**Aug 27 2026**

  1. 响应返回label错误码，和Rest请求一致

**Aug 11 2026**

  1. CrossEx新增Hyperliquid逐仓保证金功能，支持修改保证金模式及增加、减少逐仓保证金
  2. CrossEx闪兑支持Hyperliquid USDC币种，同时支持还款负债

**Jul 15 2026**

  1. 新增批量撤单 API 频道（batch_cancel_orders）

**Jul 9 2026**

  1. 新增ADL排名订阅频道（adl_rank），提供交易所底层rank和CrossEx自身rank

**Jul 2 2026**

  1. CrossEx新增支持DERIBIT交易所

**Jun 9 2026**

  1. CrossEx新增支持HYPERLIQUID交易所

**May 19 2026**

  1. CrossEx新增支持KRAKEN交易所

**Mar 24 2026**

  1. 新增Ticker订阅频道（ticker），提供各大交易所现货/合约的ticker推送
  2. 新增公有成交订阅频道（trade），提供各大交易所现货/合约的逐笔成交推送
  3. 新增K线订阅频道（kline_x），支持1m/5m/15m/30m/1h/4h/1d多个周期
  4. 新增合约资金费率订阅频道（funding_rate），提供合约的资金费率推送
  5. 新增合约持仓总量订阅频道（open_interest），提供合约的持仓总量推送（除BINANCE外）

**Mar 12 2026**

  1. CrossEx新增支持BYBIT交易所

**Feb 27 2026**

  1. 新增公有行情推送，包括最新成交价，指数价格，标记价格
  2. 新增增量订单簿深度和全量订单簿深度订阅

**Jan 21 2026**

  1. 增加channel完全平仓
  2. 添加连接数量限制说明
  3. 添加所有 API 的限频说明

**Jan 19 2026**

  1. 新增杠杆仓位订阅/取消订阅
  2. 新增杠杆利息订阅/取消订阅
  3. 新增修改现货杠杆的杠杆倍数

##  Websocket API 概述

###  事件

每个通用频道（例如订单、资产等）都支持 2 种不同的事件消息，它们是：

  1. **`subscribe`** (**推荐使用**)

订阅，接受服务器的新数据推送。

  2. **`unsubscribe`**

如果取消订阅，服务器将不会发送新数据推送。

###  请求参数

公有连接用于订阅和退订行情，`payload` 是交易对数组。私有连接还支持登录、交易请求和应用层心跳。

请使用 REST 币对查询返回的完整 `symbol`。Aster 合约使用 `ASTER_FUTURE_{Base}_{Counter}`。Hyperliquid HIP-3 币对可能带有 DEX 前缀，例如 `HYPERLIQUID_FUTURE_xyz:XYZ100_USDC`。

请求参数名称 | 类型 | 必选 | 描述  
---|---|---|---  
`time` | Integer | 见各频道 | 请求时间戳（秒），私有连接必填  
`channel` | String | 见各频道 | 请求频道，登录请求可以省略  
`event` | String | 是 | 请求事件，取值参见相应频道  
`payload` | Array/Object | 见各频道 | 订阅、鉴权或交易参数  
`request_id` | String | 否 | 私有连接的可选请求 ID，最长 128 字符。支持回传的请求见各频道说明  
  
###  推送参数

消息中的 `time` 和 `time_ms` 分别是秒和毫秒时间戳。根据连接类型及消息事件读取相应字段。

推送参数消息 | `event` | 业务数据及结果  
---|---|---  
公有行情订阅或退订回执 | `subscribe` / `unsubscribe` | `result.status` 为 `success` 或 `failed`。失败详情见 `error.code` 和 `error.message`  
公有行情更新 | `update` | 行情数据在 `result`。订阅成功后，如果服务端有可用的初始数据，也通过此事件发送  
私有请求回执 | 与请求事件对应 | `result.code` 为字符串，`"100000"` 表示成功。失败原因见 `result.message`，可用时还会返回 `result.label`。具体请求的响应数据在 `payload`  
私有业务推送 | `subscribe` | 订单、成交、仓位等业务数据在 `payload`  
  
###  错误

以下为私有 WebSocket 的 `result.code`。公有行情错误见公有行情错误码。

错误Code | Message  
---|---  
`100001` | `参数丢失或无效`  
`100002` | `未登陆`  
`100003` | `连接达到最大数`  
`100004` | `超时`  
`100005` | `操作失败`  
`100006` | `登陆失败`  
`100007` | `网络错误，请稍后再试`  
  
##  鉴权

WARNING

注意: 您使用的 GateAPIv4 密钥对必须至少启用 CrossEx 读取权限， 如果启用了密钥的白名单，则您的出站 IP 地址必须在密钥的 IP 白名单中。

如果频道是私有的，例如，客户端请求需要携带身份验证信息。例如： `order`检索用户订单更新的频道。

身份验证通过请求正文中的`payload`字段发送，格式如下:

名称 | 类型 | 描述  
---|---|---  
`method` | String | 验证方式: `api_key`  
`api_key` | String | apiKey 的值  
`sign` | String | 签名结果  
  
WebSocket 认证使用与 Gate APIv4 API 相同的签名计算方法，即`HexEncode(HMAC_SHA512(secret, signature_string))`, 但有以下区别:

  1. 签名字符串拼接方式： `channel=<channel>&event=<event>&time=<time>`, 其中 `<channel>`, `<event>`, `<time>` 是对应的请求信息
  2. 身份验证信息在请求正文中的 `payload`字段中发送。

您可以登录账户获取 CrossEx 账户的 api_key 和 secret。
    
    
    # example WebSocket signature calculation implementation in Python
    import hmac, hashlib, json, time
    
    
    def gen_sign(channel, event, timestamp):
        # GateAPIv4 key pair
        api_key = 'YOUR_API_KEY'
        api_secret = 'YOUR_API_SECRET'
    
        s = 'channel=%s&event=%s&time=%d' % (channel, event, timestamp)
        sign = hmac.new(api_secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        return {'method': 'api_key', 'api_key': api_key, 'sign': sign}
    
    
    request = {
        'time': int(time.time()),
        'event': 'login',
        'payload': {
            'method': 'api_key',
            'api_key': 'YOUR_API_KEY',
            'sign': gen_sign('', 'login', int(time.time()))['sign']
        }
    }
    print(json.dumps(request))
    

#  认证

**» event** : login

**» method** : api_key

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件 login  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | object | 是 | none  
»» method | body | string | 是 | 验证方式  
»» api_key | body | string | 是 | api key  
»» sign | body | string | 是 | 签名  
  
##  返回数据结构

返回数据结构名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | object | true | none |  | none  
»» conn_id | string | true | none |  | 连接ID  
» result | object | true | none |  | 登陆结果  
»» code | string | true | none |  | 响应码  
»» message | string | true | none |  | 响应消息  
» time | integer | true | none |  | 时间戳（秒）  
» time_ms | integer | true | none |  | 时间戳（毫秒）  
  
请求示例
    
    
    {
      "time": 1754272114,
      "event": "login",
      "request_id": "request-1",
      "payload": {
        "method": "api_key",
        "api_key": "0d5245a5d8be8ac0e96ed8aaa47386cf",
        "sign": "568e694ebf998fc0e9a26ab26c8cb962d8649fd61fbfc61f068251ae8169f00066b3205bb2491c1625e111f18c4bf1e6bcf8d3fd519eaea8b7335edea960eee2"
      }
    }
    

返回示例
    
    
    {
      "event": "login",
      "request_id": "request-1",
      "payload": {
        "conn_id": "644ff57f-add4-407a-97aa-b654c4ede839"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168928
    }
    

#  私有连接心跳

私有 WebSocket 支持应用层心跳。发送 `event=ping`、`channel=crossex.ping` 和当前秒级时间戳。无需登录，也无需传 `payload`。此请求会刷新连接活跃时间。

请求示例
    
    
    {
      "time": 1795392000,
      "event": "ping",
      "channel": "crossex.ping"
    }
    

响应示例
    
    
    {
      "time": 1795392000,
      "time_ms": 1795392000000,
      "event": "ping",
      "channel": "crossex.pong",
      "result": {
        "code": "100000",
        "message": "success"
      }
    }
    

#  最新成交价订阅

`last_price`

最新成交价频道提供各大交易所的现货/杠杆，合约的最新成交价格更新推送

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» payload | body | [string] | 是 | 订阅/取消币对，暂不支持全部订阅  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : last_price

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

无需认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "last_price",
      "payload": [
        "BINANCE_SPOT_BTC_USDT",
        "OKX_FUTURE_BTC_USDT",
        "GATE_FUTURE_ETH_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» result | object | true | none | 结果 | none  
»» s | string | true | none | 交易对 | Symbol  
»» lp | string | true | none | 最新成交价 | LastPrice  
  
推送示例
    
    
    {
      "time": 1771988975,
      "channel": "last_price",
      "event": "update",
      "result": {
        "s": "BINANCE_SPOT_BTC_USDT",
        "lp": "65873.49000000"
      },
      "time_ms": 1771988975033
    }
    

#  指数价格订阅

`index_price`

指数频道提供各大交易所的现货杠杆的指数价格更新推送

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» payload | body | [string] | 是 | 订阅/取消币对，暂不支持全部订阅  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : index_price

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

无需认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "index_price",
      "payload": [
        "BINANCE_MARGIN_BTC_USDT",
        "OKX_MARGIN_BTC_USDT",
        "GATE_MARGIN_ETH_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» result | object | true | none | 结果 | none  
»» s | string | true | none | 交易对 | Symbol  
»» ip | string | true | none | 指数价格 | IndexPrice  
  
推送示例
    
    
    {
      "time": 1771990104,
      "channel": "index_price",
      "event": "update",
      "result": {
        "s": "BINANCE_MARGIN_BTC_USDT",
        "ip": "65590.40739130"
      },
      "time_ms": 1771990104116
    }
    

#  标记价格订阅

`mark_price`

指数频道提供各大交易所的现货杠杆的指数价格更新推送

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» payload | body | [string] | 是 | 订阅/取消币对，暂不支持全部订阅  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : mark_price

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

无需认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "mark_price",
      "payload": [
        "BINANCE_FUTURE_BTC_USDT",
        "OKX_FUTURE_BTC_USDT",
        "GATE_FUTURE_ETH_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» result | object | true | none | 结果 | none  
»» s | string | true | none | 交易对 | Symbol  
»» mp | string | true | none | 标记价格 | MarkPrice  
  
推送示例
    
    
    {
      "time": 1771990349,
      "channel": "mark_price",
      "event": "update",
      "result": {
        "s": "BINANCE_FUTURE_BTC_USDT",
        "mp": "65566.30000000"
      },
      "time_ms": 1771990349113
    }
    

#  全量有限档订单簿订阅

`order_book_x`

其中 `x` 表示订单簿快照档位，不同交易所支持的档位如下：

  * BINANCE：[5, 10, 20]
  * OKX：[1, 5]
  * GATE： 
    * SPOT：[5, 10, 20, 30, 50, 100]
    * FUTURE：[1, 5, 10, 20, 50, 100]
  * BYBIT：[1]
  * KRAKEN：不支持 `order_book_x` 快照档位，请使用 `order_book_update`
  * HYPERLIQUID：[1, 5, 10, 20]
  * DERIBIT：[1, 5, 10, 20]
  * LIGHTER：[1, 5, 10, 20, 30, 50, 100, 400]
  * ASTER：[1, 5, 10, 20]
  * 股票及 ETF：[1, 5, 10, 20, 30, 50, 100, 400]

全量有限档订单簿频道提供各大交易所的现货/合约订单簿深度全量有限档推送，并支持股票及ETF。股票及ETF盘口价格使用上市市场原生计价币种（USD/HKD/KRW/JPY）。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» payload | body | [string] | 是 | 订阅/取消币对，暂不支持全部订阅  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : order_book_x

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

无需认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "order_book_5",
      "payload": [
        "BINANCE_SPOT_BTC_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» result | object | true | none | 结果 | none  
»» ts | long | true | none | 毫秒时间戳 | Symbol  
»» s | string | true | none | 交易对 | Symbol  
»» a | array | true | none | 卖盘深度 | [Price,Qty]  
»» b | array | true | none | 买盘深度 | [Price,Qty]  
  
推送示例
    
    
    {
      "time": 1771990690,
      "channel": "order_book_5",
      "event": "update",
      "result": {
        "ts": 1771990690844,
        "s": "BINANCE_SPOT_BTC_USDT",
        "a": [
          [
            "65485.33000000",
            "2.25708000"
          ],
          [
            "65485.34000000",
            "0.00025000"
          ],
          [
            "65485.38000000",
            "0.15432000"
          ],
          [
            "65485.39000000",
            "0.50423000"
          ],
          [
            "65486.26000000",
            "0.00208000"
          ]
        ],
        "b": [
          [
            "65485.32000000",
            "0.04107000"
          ],
          [
            "65485.31000000",
            "0.00097000"
          ],
          [
            "65485.20000000",
            "0.00008000"
          ],
          [
            "65485.10000000",
            "0.00018000"
          ],
          [
            "65484.99000000",
            "0.00045000"
          ]
        ]
      },
      "time_ms": 1771990690844
    }
    

#  增量订单簿订阅

`order_book_update`

增量订单簿频道提供各大交易所的现货和合约订单簿深度更新。股票及 ETF 仅支持有限档订单簿快照。若订阅股票或 ETF 的 `order_book_update`，将返回错误码 `1000119`。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» payload | body | [string] | 是 | 订阅/取消币对，暂不支持全部订阅  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : order_book_update

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

无需认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "order_book_update",
      "payload": [
        "BINANCE_FUTURE_BTC_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» result | object | true | none | 结果 | none  
»» snapshot | boolean | true | none | 是否是快照(是可全量覆盖，否则增量更新) | Snapshot  
»» ts | long | true | none | 毫秒时间戳 | Timestamp  
»» s | string | true | none | 交易对 | Symbol  
»» U | integer | true | none | 开始序列号 | StartIndex  
»» u | integer | true | none | 结束序列号 | EndIndex  
»» a | array | true | none | 卖盘深度 | [Price,Qty]  
»» b | array | true | none | 买盘深度 | [Price,Qty]  
  
推送示例
    
    
    {
      "time": 1771991193,
      "channel": "order_book_update",
      "event": "update",
      "result": {
        "snapshot": false,
        "ts": 1771991193314,
        "s": "BINANCE_FUTURE_BTC_USDT",
        "U": 88686516370,
        "u": 88686516769,
        "a": [
          [
            "65475.36000000",
            "0.00000000"
          ],
          [
            "65475.37000000",
            "0.00000000"
          ]
        ],
        "b": [
          [
            "65479.75000000",
            "0.96961000"
          ],
          [
            "65478.71000000",
            "0.03395000"
          ]
        ]
      },
      "time_ms": 1771991193344
    }
    

#  Ticker订阅

`ticker`

ticker频道提供各大交易所的现货/合约的ticker推送，并支持股票及ETF。股票及 ETF 价格使用上市市场原生计价币种（USD、HKD、KRW 或 JPY）。股票 ticker 的盘口和成交量字段可能没有可用值。可订阅有限档订单簿获取最优买卖价。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» payload | body | [string] | 是 | 订阅/取消币对，暂不支持全部订阅  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : ticker

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

无需认证

请求示例
    
    
    {
      "event": "subscribe",
      "channel": "ticker",
      "payload": [
        "BINANCE_FUTURE_BTC_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» result | object | true | none | 结果 | none  
»» s | string | true | none | 交易对 | Symbol  
»» lp | string | true | none | 最新成交价 | LastPrice  
»» bp | string | false | none | 最优买价 | 随数据源提供  
»» bs | string | false | none | 最优买量 | 随数据源提供  
»» ap | string | false | none | 最优卖价 | 随数据源提供  
»» as | string | false | none | 最优卖量 | 随数据源提供  
»» o | string | false | none | 24 小时开盘价，股票及 ETF 为当日开盘价 | 随数据源提供  
»» h | string | false | none | 24 小时最高价 | 随数据源提供  
»» l | string | false | none | 24 小时最低价 | 随数据源提供  
»» v | string | false | none | 24 小时基础币种成交量 | 随数据源提供  
»» q | string | false | none | 24h成交量(quote) | QuoteVolume24h  
»» ts | long | true | none | 交易所毫秒时间戳 | Timestamp  
  
推送示例
    
    
    {
      "time": 1770709567,
      "channel": "ticker",
      "event": "update",
      "result": {
        "s": "BINANCE_FUTURE_BTC_USDT",
        "lp": "67280.50",
        "bp": "67280.20",
        "bs": "35",
        "ap": "67280.70",
        "as": "28",
        "o": "69100.00",
        "h": "69100.00",
        "l": "66000.00",
        "v": "825432",
        "q": "5523487123.55",
        "ts": 1710001234567
      },
      "time_ms": 1770709567032
    }
    

股票推送示例（价格单位为 HKD）
    
    
    {
      "time": 1795392000,
      "time_ms": 1795392000000,
      "channel": "ticker",
      "event": "update",
      "result": {
        "s": "HK_STOCK_00700_USDT",
        "lp": "424.8",
        "o": "428",
        "h": "430",
        "l": "423",
        "ts": 1795392000000
      }
    }
    

#  行情列表订阅

`market_list`

公有行情频道，无需认证。使用 `event=subscribe` 或 `event=unsubscribe`，在 `payload` 中传入交易对数组。现货、合约、股票及 ETF 的可用交易对与 `ticker` 一致。

订阅请求
    
    
    {
      "time": 1795392000,
      "event": "subscribe",
      "channel": "market_list",
      "payload": ["BINANCE_FUTURE_BTC_USDT"]
    }
    

订阅回执
    
    
    {
      "time": 1795392000,
      "time_ms": 1795392000000,
      "event": "subscribe",
      "channel": "market_list",
      "payload": ["BINANCE_FUTURE_BTC_USDT"],
      "result": {"status": "success"}
    }
    

##  行情列表推送

`result` 字段 | 类型 | 必选 | 说明  
---|---|---|---  
`symbol` | string | 是 | 交易对  
`last_price` | string | 否 | 最新价。Hyperliquid 在此频道返回中间价。股票及 ETF 使用原生计价币种  
`change_rate_24h` | string | 否 | 24 小时涨跌幅的百分数数值，例如 `"6.78"` 表示上涨 6.78%  
`quote_volume_24h` | string | 否 | 按报价币种计的 24 小时成交额  
  
数据源暂无相应值时，推送会省略对应的可选字段。

行情更新
    
    
    {
      "time": 1795392000,
      "time_ms": 1795392000000,
      "event": "update",
      "channel": "market_list",
      "result": {
        "symbol": "BINANCE_FUTURE_BTC_USDT",
        "last_price": "67280.50",
        "change_rate_24h": "6.78",
        "quote_volume_24h": "5523487123.55"
      }
    }
    

#  公有成交订阅

`trade`

trade频道提供各大交易所的现货/合约的逐笔公有成交推送

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» payload | body | [string] | 是 | 订阅/取消币对，暂不支持全部订阅  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : trade

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

无需认证

请求示例
    
    
    {
      "event": "subscribe",
      "channel": "trade",
      "payload": [
        "BINANCE_FUTURE_BTC_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» result | object | true | none | 结果 | none  
»» s | string | true | none | 交易对 | Symbol  
»» i | string | true | none | 成交ID(交易所原始格式) | TradeId  
»» p | string | true | none | 成交价 | Price  
»» q | string | true | none | 成交量(base) | Quantity  
»» S | string | true | none | 方向 | BUY/SELL  
»» ts | long | true | none | 交易所毫秒时间戳 | Timestamp  
  
推送示例
    
    
    {
      "time": 1770709567,
      "channel": "trade",
      "event": "update",
      "result": {
        "s": "BTCUSDT",
        "i": "18473628192",
        "p": "67250.12",
        "q": "0.015",
        "S": "BUY",
        "ts": 1710001234567,
        "m": false
      },
      "time_ms": 1770709567032
    }
    

#  K线订阅

`kline_x`

  * kline_1m,kline_5m,kline_15m,kline_30m,kline_1h,kline_4h,kline_1d;

kline频道提供各大交易所的现货/合约的k线推送，并支持股票及ETF。股票及ETF的K线价格使用上市市场原生计价币种（USD/HKD/KRW/JPY）。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» payload | body | [string] | 是 | 订阅/取消币对，暂不支持全部订阅  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : kline

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

无需认证

请求示例
    
    
    {
      "channel": "kline_1m",
      "event": "subscribe",
      "payload": [
        "BYBIT_FUTURE_BTC_USDT",
        "BINANCE_FUTURE_ETH_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» result | object | true | none | 结果 | none  
»» s | string | true | none | 交易对 | Symbol  
»» o | string | true | none | 开盘价 | OpenPrice  
»» h | string | true | none | 最高价 | HighPrice  
»» l | string | true | none | 最低价 | LowPrice  
»» c | string | true | none | 收盘价 | ClosePrice  
»» v | string | true | none | 成交量 | Volume  
»» t | long | true | none | K线开始时间(毫秒) | StartTime  
»» T | long | true | none | K线结束时间(毫秒) | EndTime  
»» x | boolean | true | none | 是否已确认(0:未完成 1:已完成) | Confirm  
  
推送示例
    
    
    {
      "channel": "kline_1m",
      "event": "update",
      "result": {
        "s": "BYBIT_FUTURE_BTC_USDT",
        "o": "95000",
        "h": "95100",
        "l": "94900",
        "c": "95050",
        "v": "1234.5",
        "t": 1710000000000,
        "T": 1710000059999,
        "x": true
      }
    }
    

#  合约的资金费率订阅

`funding_rate`

funding_rate频道提供各大交易所的合约的资金费率推送

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» payload | body | [string] | 是 | 订阅/取消币对，暂不支持全部订阅  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : funding_rate

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

无需认证

请求示例
    
    
    {
      "event": "subscribe",
      "channel": "funding_rate",
      "payload": [
        "BINANCE_FUTURE_BTC_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» result | object | true | none | 结果 | none  
»» s | string | true | none | 交易对 | Symbol  
»» r | string | true | none | 当前资金费率 | FundingRate  
»» T | long | true | none | 下次结算毫秒时间戳 | NextFundingTime  
  
推送示例
    
    
    {
      "time": 1773382659,
      "channel": "funding_rate",
      "event": "update",
      "result": {
        "s": "BINANCE_FUTURE_BTC_USDT",
        "r": "0.00002534",
        "T": 1773388800000
      },
      "time_ms": 1773382659999
    }
    

#  合约的持仓总量订阅

`open_interest`

`open_interest` 提供合约持仓总量更新。Binance 和 Aster 不支持此频道，订阅时分别返回错误码 `1000104` 和 `1000115`。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» payload | body | [string] | 是 | 订阅/取消币对，暂不支持全部订阅  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : open_interest

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

无需认证

请求示例
    
    
    {
      "event": "subscribe",
      "channel": "open_interest",
      "payload": [
        "OKX_FUTURE_BTC_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» result | object | true | none | 结果 | none  
»» s | string | true | none | 交易对 | Symbol  
»» oi | string | true | none | 持仓量 | OpenInterest  
»» oiV | string | false | none | 持仓价值 | OpenInterestValue  
  
推送示例
    
    
    {
      "time": 1773384822,
      "channel": "open_interest",
      "event": "update",
      "result": {
        "s": "OKX_FUTURE_BTC_USDT",
        "oi": "2929823.88000001813",
        "oiV": "29298.2388000001813"
      },
      "time_ms": 1773384822164
    }
    

#  订单订阅/取消订阅

`order`

订单频道提供了一种接收用户订单更新的方式，包括股票及ETF订单。股票及ETF的 `exchange_type` 为 `US/HK/KR/JP`，`business_type` 为 `STOCK/ETF`，价格和成交额使用上市市场原生计价币种。

合约 Rebase 调整仓位时，会推送一笔平旧仓订单和一笔开新仓订单。两笔订单的 `state` 均为 `FILLED`，`attribute` 为 `REBASE`。成交频道会推送对应的成交记录。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | [string] | 是 | 订阅/取消币对 !all 代表全部  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : order

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

需要认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "order",
      "request_id": "request-1",
      "payload": [
        "GATE_FUTURE_ETH_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» payload | object | true | none | 数据集 | none  
»» user_id | string | true | none | 用户id | none  
»» order_id | string | true | none | 订单号 | Order ID  
»» text | string | true | none | 客户订单号 | Customer-defined order ID  
»» state | string | true | none | 订单状态 | Order State:   
NEW: The order is legal and waiting to be sent to the exchange  
OPEN: The order has been placed on the orderbook of the exchange  
PARTIALLY_FILLED: The order has been partially completed  
FILLED: The order has been fully executed  
FAIL: The order verification in CrossEx did not pass. Please check the order reason  
REJECT：The order was rejected by the exchange. Please check the order reason  
»» symbol | string | true | none | 交易对 | Trading pair unique identifier ,example:  
BINANCE_SPOT_BTC_USDT, BINANCE_FUTURE_BTC_USDT  
»» side | string | true | none | 方向 | Side(BUY,SELL)  
»» type | string | true | none | 类型 | Type(LIMIT, MARKET)  
»» attribute | string | true | none | 订单属性 | `COMMON` 普通单、`LIQ` 强平接管单、`REDUCE` 强平减仓单、`ADL` 自动减仓、`SETTLEMENT` 下架清算、`REBASE` Rebase 系统订单  
»» exchange_type | string | true | none | 交易所或上市市场 | `BINANCE`、`OKX`、`GATE`、`BYBIT`、`KRAKEN`、`HYPERLIQUID`、`DERIBIT`、`LIGHTER`、`ASTER`。股票及 ETF 返回 `US`、`HK`、`KR` 或 `JP`  
»» business_type | string | true | none | 业务类型 | `SPOT`、`FUTURE`、`MARGIN`、`CONVERT`、`STOCK`、`ETF`  
»» qty | string | true | none | 基础货币数量 | Order base quantity  
»» quote_qty | string | true | none | 报价币种数量 | Order quote quantity  
»» price | string | true | none | 委托价格 | 股票及 ETF 使用上市市场原生计价币种  
»» time_in_force | string | true | none | Time in force 策略 | Timeinforce (default GTC, enums:GTC,IOC,FOK,POC,RPI)  
»» executed_qty | string | true | none | 已成交数量 | Executed quantity  
»» executed_amount | string | true | none | 已成交金额 | 股票及 ETF 使用上市市场原生计价币种  
»» executed_avg_price | string | true | none | 已成交均价 | 股票及 ETF 使用上市市场原生计价币种  
»» fee_coin | string | true | none | 手续费币种 | Transaction fee coin  
»» fee | string | true | none | 手续费 | Transaction fee amount  
»» reduce_only | string | true | none | 只减仓 | Reduce position orders only, "true" or "false"  
»» leverage | string | true | none | 杠杆 | Order leverage  
»» reason | string | true | none | 订单原因 | 拒单或撤单原因。Rebase 系统订单会返回 `POSITION_REBASE_RATIO=<比例>`  
»» last_executed_qty | string | true | none | 最新已成交量 | Last transaction quantity  
»» last_executed_price | string | true | none | 最新已成交价 | 股票及 ETF 使用上市市场原生计价币种  
»» last_executed_amount | string | true | none | 最新已成交金额 | 股票及 ETF 使用上市市场原生计价币种  
»» position_side | string | true | none | 仓位方向 | Position side(NONE/LONG/SHORT)  
»» create_time | string | true | none | 创建时间 | Create time  
»» update_time | string | true | none | 更新时间 | Update time  
» result | object | true | none | 更新时间 |   
»» code | string | true | none | 返回码 |   
» time | integer | true | none | 时间戳（秒） |   
» time_ms | integer | true | none | 时间戳（毫秒） |   
  
推送示例
    
    
    {
      "channel": "order",
      "event": "subscribe",
      "payload": {
        "attribute": "COMMON",
        "business_type": "FUTURE",
        "create_time": "1756434169096",
        "exchange_type": "OKX",
        "executed_amount": "0",
        "executed_avg_price": "0",
        "executed_qty": "0",
        "fee": "0",
        "fee_coin": "",
        "last_executed_amount": "0",
        "last_executed_price": "0",
        "last_executed_qty": "0",
        "leverage": "3",
        "order_id": "2072652940337152",
        "position_side": "NONE",
        "price": "0.8499",
        "qty": "10",
        "quote_qty": "0",
        "reason": "{\"label\":\"TRADE_INSUFFICIENT_AVAILABLE_MARGIN_ERROR\",\"message\":\"Insufficient availableMargin\"}",
        "reduce_only": "false",
        "side": "BUY",
        "state": "FAIL",
        "symbol": "OKX_FUTURE_ADA_USDT",
        "text": "2072652940337152",
        "time_in_force": "GTC",
        "type": "MARKET",
        "update_time": "1756434169098",
        "user_id": "2124485957"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168968
    }
    

#  资产订阅/取消订阅

`asset`

资产频道提供了一种接收用户资产更新的方式。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | [string] | 是 | 订阅/取消币种集合 !all 代表全部  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : asset

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 币种列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的币种不会被覆盖。

WARNING

需要认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "asset",
      "request_id": "request-1",
      "payload": [
        "USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» payload | object | true | none | 数据集 | none  
»» user_id | string | false | none | 用户id | none  
»» coin | string | false | none | 币种 | none  
»» exchange_type | string | false | none | 交易所 | none  
»» price | string | false | none | 币种价格 | none  
»» balance | string | false | none | 余额 | none  
»» upnl | string | false | none | 未结盈亏 | none  
»» equity | string | false | none | 权益 | none  
»» futures_initial_margin | string | false | none | 合约初始保证金 | none  
»» futures_maintenance_margin | string | false | none | 合约维持保证金 | none  
»» borrowing_initial_margin | string | false | none | 币种的借款起始保证金 | none  
»» borrowing_maintenance_margin | string | false | none | 币种的借款维持保证金 | none  
»» available_balance | string | false | none | 可用余额 | none  
»» liability | string | false | none | 负债 |   
» result | object | true | none | 更新时间 |   
»» code | string | true | none | 返回码 |   
»» message | string | true | none | 响应信息 |   
» time | integer | true | none | 时间戳（秒） |   
» time_ms | integer | true | none | 时间戳（毫秒） |   
  
推送示例
    
    
    {
      "channel": "asset",
      "event": "subscribe",
      "payload": {
        "user_id": "2124492766",
        "coin": "USDT",
        "exchange_type": "CROSSEX",
        "price": "1",
        "balance": "9967.013209",
        "upnl": "0",
        "equity": "9967.013209",
        "futures_initial_margin": "1.236",
        "futures_maintenance_margin": "0",
        "borrowing_initial_margin": "0",
        "borrowing_maintenance_margin": "0",
        "available_balance": "9940.013209",
        "liability": "0"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756465636,
      "time_ms": 1756465636463
    }
    

#  成交订阅/取消订阅

`usertrades`

成交频道提供了一种接收用户成交更新的方式。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | [string] | 是 | 订阅/取消币种集合 !all 代表全部  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : usertrades

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

需要认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "usertrades",
      "request_id": "request-1",
      "payload": [
        "GATE_FUTURE_ETH_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» payload | object | true | none | 数据集 | none  
»» user_id | string | false | none | 用户ID | none  
»» transaction_id | string | false | none | 成交记录ID | none  
»» order_id | string | false | none | 订单ID | none  
»» text | string | false | none | 用户订单号 | none  
»» symbol | string | false | none | 交易对 | none  
»» exchange_type | string | false | none | 交易所或上市市场 | 股票及 ETF 返回 `US`、`HK`、`KR` 或 `JP`  
»» business_type | string | false | none | 业务类型 | 股票及 ETF 分别为 `STOCK` 和 `ETF`  
»» side | string | false | none | 买卖方向 | none  
»» qty | string | false | none | 成交数量 | none  
»» price | string | false | none | 成交价格 | 股票及 ETF 使用上市市场原生计价币种（USD、HKD、KRW 或 JPY）  
»» fx_rate | string | false | none | 该笔成交的结算汇率 | 1 单位原生计价币种折合的 USDT。无可用汇率时为 `""`  
»» fee | string | false | none | 手续费 | none  
»» fee_coin | string | false | none | 手续费币种 | none  
»» fee_rate | string | false | none | 手续费率 | none  
»» match_role | string | false | none | 成交角色 | none  
»» rpnl | string | false | none | 实现盈亏 | none  
»» position_mode | string | false | none | 仓位模式 | none  
»» position_side | string | false | none | 仓位方向 | none  
»» create_time | string | false | none | 创建时间 | none  
» result | object | true | none | 更新时间 |   
»» code | string | true | none | 返回码 |   
» time | integer | true | none | 时间戳（秒） |   
» time_ms | integer | true | none | 时间戳（毫秒） |   
  
该例中的成交本金折合 25.4 USDT，计算方式为 `qty × price × fx_rate`。手续费单独通过 `fee` 和 `fee_coin` 表示。

推送示例
    
    
    {
      "channel": "usertrades",
      "event": "subscribe",
      "payload": {
        "user_id": "2124492766",
        "transaction_id": "2072784922594048",
        "order_id": "2072784922592768",
        "text": "2072784922592768",
        "symbol": "GATE_SPOT_ADA_USDT",
        "exchange_type": "GATE",
        "business_type": "SPOT",
        "side": "BUY",
        "qty": "13.36",
        "price": "0.8228",
        "fx_rate": "",
        "fee": "0.004008000000000000",
        "fee_coin": "ADA",
        "fee_rate": "0.0003",
        "match_role": "TAKER",
        "rpnl": "0",
        "position_mode": "SINGLE",
        "position_side": "",
        "create_time": "1756465636528"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168984
    }
    

股票成交推送示例
    
    
    {
      "time": 1795392000,
      "time_ms": 1795392000000,
      "channel": "usertrades",
      "event": "subscribe",
      "payload": {
        "user_id": "59138103",
        "transaction_id": "2072784922594048",
        "order_id": "2072784922592768",
        "text": "stock-buy-1",
        "symbol": "HK_STOCK_00700_USDT",
        "exchange_type": "HK",
        "business_type": "STOCK",
        "side": "BUY",
        "qty": "2",
        "price": "100",
        "fx_rate": "0.127",
        "fee": "0.0254",
        "fee_coin": "USDT",
        "fee_rate": "0.001",
        "match_role": "TAKER",
        "rpnl": "0",
        "position_mode": "SINGLE",
        "position_side": "NONE",
        "create_time": "1795392000000"
      },
      "result": {
        "code": "100000",
        "message": "success"
      }
    }
    

#  仓位订阅/取消订阅

`position`

合约进入 Rebase 后，仓位的标记价格、市值和未结盈亏等指标暂停重算，可能保留上次计算值。

仓位频道提供了一种接收用户仓位更新的方式。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | [string] | 是 | !all 代表全部  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : position

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表，`!all` 表示订阅所有交易对  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

需要认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "position",
      "request_id": "request-1",
      "payload": [
        "GATE_FUTURE_ETH_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» payload | object | true | none | 数据集 | none  
»» user_id | string | false | none | 用户id | none  
»» position_id | string | false | none | 仓位id | none  
»» symbol | string | false | none | 交易对 | none  
»» position_side | string | false | none | 仓位方向 | none  
»» initial_margin | string | false | none | 初始保证金 | none  
»» isolated_margin | string | false | none | 逐仓保证金。全仓时为0，仅逐仓有效 | none  
»» margin_mode | string | false | none | 保证金模式（CROSS/ISOLATED） | none  
»» maintenance_margin | string | false | none | 维持保证金 | none  
»» position_qty | string | false | none | 仓位数量 | none  
»» position_value | string | false | none | 仓位价值 | none  
»» upnl | string | false | none | 未结盈亏 | none  
»» upnl_rate | string | false | none | 未结盈亏比 | none  
»» entry_price | string | false | none | 仓位入场均价 | none  
»» liq_price | string | false | none | 强平价格。全仓时为0，仅逐仓有效；逐仓时为0代表不强平 | none  
»» mark_price | string | false | none | 标记价格 | none  
»» leverage | string | false | none | 仓位杠杆 | none  
»» max_leverage | string | false | none | 最大杠杆 | none  
»» risk_limit | string | false | none | 风险限额 | none  
»» fee | string | false | none | 仓位手续费 | none  
»» funding_fee | string | false | none | 仓位资金费 | none  
»» funding_time | string | false | none | 仓位资金费收取时间 | none  
»» create_time | string | false | none | 仓位创建时间 | none  
»» update_time | string | false | none | 仓位更新时间 | none  
»» closed_pnl | string | false | none | 已结盈亏 | none  
» result | object | true | none | 更新时间 |   
»» code | string | true | none | 返回码 |   
» time | integer | true | none | 时间戳（秒） |   
» time_ms | integer | true | none | 时间戳（毫秒） |   
  
推送示例
    
    
    {
      "channel": "position",
      "event": "subscribe",
      "payload": {
        "create_time": "1756434169096",
        "entry_price": "0",
        "fee": "0",
        "funding_fee": "0",
        "funding_time": "0",
        "initial_margin": "0",
        "isolated_margin": "0",
        "margin_mode": "CROSS",
        "leverage": "3",
        "maintenance_margin": "0",
        "liq_price": "0",
        "mark_price": "0.8499",
        "max_leverage": "20",
        "position_id": "20087051449819136",
        "position_qty": "0",
        "position_side": "NONE",
        "position_value": "0",
        "risk_limit": "1",
        "symbol": "OKX_FUTURE_ADA_USDT",
        "update_time": "1756434169098",
        "upnl": "0",
        "upnl_rate": "0",
        "user_id": "2124485957",
        "closed_pnl": "12"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168984
    }
    

#  证券仓位订阅/取消订阅

`security_position`

证券仓位频道用于接收股票及ETF仓位更新。价格、持仓价值和未结盈亏使用上市市场原生计价币种（USD/HKD/KRW/JPY）。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | subscribe、unsubscribe  
» channel | body | string | 是 | security_position  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助识别响应  
» payload | body | [string] | 是 | 股票或ETF交易对列表，`!all` 表示全部  
  
您可以多次订阅或取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

需要认证

请求示例
    
    
    {
      "time": 1791777600,
      "event": "subscribe",
      "channel": "security_position",
      "request_id": "request-1",
      "payload": [
        "HK_STOCK_00700_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 描述  
---|---|---|---  
» channel | string | true | 频道名  
» event | string | true | 事件  
» payload | object | true | 证券仓位数据  
»» user_id | string | false | 用户ID  
»» symbol | string | false | 股票或ETF交易对  
»» price | string | false | 最新价格，单位为上市市场原生计价币种  
»» entry_price | string | false | 持仓成本价，单位为上市市场原生计价币种  
»» diluted_cost_price | string | false | 摊薄成本价，单位为上市市场原生计价币种  
»» upnl | string | false | 未结盈亏，单位为上市市场原生计价币种  
»» position_qty | string | false | 持仓数量  
»» position_value | string | false | 持仓价值，单位为上市市场原生计价币种  
» result | object | true | 订阅响应  
»» code | string | true | 返回码  
» time | integer | true | 时间戳（秒）  
» time_ms | integer | true | 时间戳（毫秒）  
  
推送示例
    
    
    {
      "channel": "security_position",
      "event": "subscribe",
      "payload": {
        "user_id": "59138103",
        "symbol": "HK_STOCK_00700_USDT",
        "price": "424.8",
        "entry_price": "428",
        "diluted_cost_price": "428",
        "upnl": "-0.032",
        "position_qty": "0.01",
        "position_value": "4.248"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1791777600,
      "time_ms": 1791777600000
    }
    

#  杠杆仓位订阅/取消订阅

`margin_position`

杠杆仓位频道提供了一种接收用户杠杆仓位更新的方式。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | [string] | 是 | !all 代表全部  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : margin_position

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表，`!all` 表示订阅所有交易对  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

需要认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "margin_position",
      "request_id": "request-1",
      "payload": [
        "GATE_MARGIN_ETH_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» payload | object | true | none | 数据集 | none  
»» user_id | string | false | none | 用户id | none  
»» position_id | string | false | none | 仓位id | none  
»» symbol | string | false | none | 交易币对EXCHANGE_MARGIN_BASE_COUNTER | none  
»» position_side | string | false | none | 仓位方向 | none  
»» initial_margin | string | false | none | 仓位初始保证金 | none  
»» maintenance_margin | string | false | none | 仓位维持保证金 | none  
»» asset_qty | string | false | none | 仓位资产数量 | none  
»» asset_coin | string | false | none | 仓位资产币种 | none  
»» position_value | string | false | none | 仓位价值 | none  
»» liability | string | false | none | 负债数量 | none  
»» liability_coin | string | false | none | 负债币种 | none  
»» interest | string | false | none | 已扣利息 | none  
»» max_position_qty | string | false | none | 最大持仓量 | none  
»» entry_price | string | false | none | 持仓成本价(开仓均价) | none  
»» index_price | string | false | none | 指数价格 | none  
»» upnl | string | false | none | 未结盈亏 | none  
»» upnl_rate | string | false | none | 未结盈亏比 | none  
»» leverage | string | false | none | 开仓杠杆 | none  
»» max_leverage | string | false | none | 最大杠杆 | none  
»» create_time | string | false | none | 创建时间 | none  
»» update_time | string | false | none | 更新时间 | none  
» result | object | true | none | 更新时间 |   
»» code | string | true | none | 返回码 |   
» time | integer | true | none | 时间戳（秒） |   
» time_ms | integer | true | none | 时间戳（毫秒） |   
  
推送示例
    
    
    {
      "channel": "margin_position",
      "event": "subscribe",
      "payload": {
        "user_id": "20251115",
        "position_id": "20116122196200192",
        "symbol": "OKX_MARGIN_DOGE_USDT",
        "position_side": "LONG",
        "initial_margin": "3.339831063595188875",
        "maintenance_margin": "0.20743774877",
        "asset_qty": "61.72130605",
        "asset_coin": "DOGE",
        "position_value": "9.9969999409185",
        "liability": "10.00003424116",
        "liability_coin": "USDT",
        "interest": "0.0000343",
        "max_position_qty": "61.72130605",
        "entry_price": "0.162018605585874506",
        "index_price": "0.16197",
        "upnl": "-0.0030343002415",
        "upnl_rate": "-0.000909",
        "leverage": "3",
        "max_leverage": "8",
        "create_time": "1763365175843",
        "update_time": "1763365689548"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168984
    }
    

#  杠杆利息订阅/取消订阅

`margin_interest`

杠杆利息频道提供了一种接收用户杠杆利息更新的方式。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | [string] | 是 | !all 代表全部  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : margin_interest

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表，`!all` 表示订阅所有交易对  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

需要认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "margin_interest",
      "request_id": "request-1",
      "payload": [
        "GATE_MARGIN_ETH_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» payload | object | true | none | 数据集 | none  
»» user_id | string | false | none | 用户id | none  
»» symbol | string | false | none | 交易对 | none  
»» exchange_type | string | false | none | 扣息所属交易所 | 例如 `OKX`  
»» interest_id | string | false | none | 扣息Id | none  
»» liability_id | string | false | none | 负债源id 可以是订单Id/仓位Id | none  
»» liability | string | false | none | 负债 | none  
»» liability_coin | string | false | none | 币种 | none  
»» interest | string | false | none | 利息 | none  
»» interest_rate | string | false | none | 利率 | none  
»» interest_type | string | false | none | 扣息类型 | none  
»» create_time | string | false | none | 仓位创建时间 | none  
» result | object | true | none | 更新时间 |   
»» code | string | true | none | 返回码 |   
» time | integer | true | none | 时间戳（秒） |   
» time_ms | integer | true | none | 时间戳（毫秒） |   
  
###  详细说明

**» interest_type** : 扣息类型 PERIODIC_POSITION整点仓位收息、PERIODIC_OPEN_ORDER整点挂单收息、IMMEDIATE_OPEN_ORDER开单收息

推送示例
    
    
    {
      "channel": "margin_interest",
      "event": "subscribe",
      "payload": {
        "user_id": "20251115",
        "symbol": "OKX_MARGIN_DOGE_USDT",
        "exchange_type": "OKX",
        "interest_id": "2101724189861376",
        "liability_id": "2101724189861120",
        "liability": "10",
        "liability_coin": "USDT",
        "interest": "0.0000343",
        "interest_rate": "0.00000343",
        "interest_type": "IMMEDIATE_OPEN_ORDER",
        "create_time": "1763365295219"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168984
    }
    

#  ADL排名订阅/取消订阅

`adl_rank`

ADL排名频道提供了一种接收用户ADL排名更新的方式。

**推送类型** : `continuous`

**更新频率** : `real-time`

##  客户端订阅

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | [string] | 是 | !all 代表全部  
  
###  详细说明

**» event** : subscribe、unsubscribe

**» channel** : adl_rank

格式:

详细说明名称 | 类型 | 必选 | 描述  
---|---|---|---  
`payload` | `Array[String]` | 是 | 交易对列表，`!all` 表示订阅所有交易对  
  
您可以多次订阅/取消订阅。除非明确取消订阅，否则之前订阅的交易对不会被覆盖。

WARNING

需要认证

请求示例
    
    
    {
      "time": 1754272114,
      "event": "subscribe",
      "channel": "adl_rank",
      "request_id": "request-1",
      "payload": [
        "BINANCE_FUTURE_ADA_USDT"
      ]
    }
    

##  服务端推送

推送参数:

名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none | 频道名 | none  
» event | string | true | none | 事件 | none  
» payload | object | true | none | 数据集 | none  
»» user_id | string | false | none | 用户id | none  
»» symbol | string | false | none | 交易对 | none  
»» crossex_adl_rank | string | false | none | CrossEx ADL排名 | 1-5，数字越大排名越前  
»» exchange_adl_rank | string | false | none | 交易所原始ADL排名 | Binance：0-4，数字越大越靠前；OKX：0-5，数字越大越靠前；Gate：1-5，数字越小越靠前；Kraken：20,40,80,100，数字越小越靠前  
» result | object | true | none | 更新时间 |   
»» code | string | true | none | 返回码 |   
» time | integer | true | none | 时间戳（秒） |   
» time_ms | integer | true | none | 时间戳（毫秒） |   
  
推送示例
    
    
    {
      "channel": "adl_rank",
      "event": "subscribe",
      "payload": {
        "user_id": "20251115",
        "symbol": "BINANCE_FUTURE_ADA_USDT",
        "crossex_adl_rank": "1",
        "exchange_adl_rank": "1"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168984
    }
    

#  下单

`place_order`

提供了一种通过 WebSocket 下单的方式。

限频: 每10秒100次请求（同REST下单共享限频）。股票及ETF额外按用户共享每秒1次下单限频。

股票及ETF仅支持跨所账户模式和GTC，必须使用 `qty` 下单，不支持 `quote_qty`；委托价格使用上市市场原生计价币种。

股票及 ETF 买单按委托价格及当时的行情汇率计算 USDT 冻结本金。缺少可用的行情汇率或市价单所需的最新价时，`result.label` 为 `COMMON_FAIL_ORDER_ERROR`。

Hyperliquid、Lighter 和 Aster 合约不支持 `FOK`。

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | none  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | object | 是 | none  
»» header | body | object | 否 | 请求头信息  
»»» X-Gate-Channel-Id | body | string | 否 | broker返佣渠道id  
»» text | body | string¦null | 否 | 用户自定义id  
»» symbol | body | string | 是 | 唯一标识符：Exchange_Business_Base_Counter  
»» side | body | string | 是 | 交易方向  
»» qty | body | string¦null | 否 | 交易币种数量  
»» price | body | string¦null | 否 | 价格  
»» type | body | string¦null | 否 | 订单类型（默认LIMIT，支持类型列举：LIMIT、MARKET）  
»» time_in_force | body | string¦null | 否 | 执行方式  
»» quote_qty | body | string¦null | 否 | 报价币种数量  
»» reduce_only | body | boolean¦null | 否 | 只减仓  
»» position_side | body | string¦null | 否 | 仓位方向  
  
###  详细说明

**» event** : api

**» channel** : place_order

**»» text** : 用户自定义id 客户定义的订单ID，仅支持字母（a-z）、数字（0-9）、符号（-，_）

**»» symbol** : 唯一标识符：Exchange_Business_Base_Counter 示例：

  * 如果您想在BINANCE交易所上为ADA/USDT交易对下现货订单，您可以使用这样的唯一标识符：`BINANCE_SPOT_ADA_USDT`;
  * 如果您想在OKX交易所上为ADA/USDT交易对下U本位永续合约订单，您可以使用这样的唯一标识符：`OKX_FUTURE_ADA_USDT`;
  * 如果您想在GATE交易所上为ADA/USDT交易对下现货杠杆订单，您可以使用这样的唯一标识符：`GATE_MARGIN_ADA_USDT`;
  * 如果您想在BYBIT交易所上为ADA/USDT交易对下现货订单，您可以使用这样的唯一标识符：`BYBIT_SPOT_ADA_USDT`;
  * 如果您想在KRAKEN交易所上为ADA/USD交易对下合约订单，您可以使用这样的唯一标识符：`KRAKEN_FUTURE_ADA_USD`;
  * 如果您想在HYPERLIQUID交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`HYPERLIQUID_FUTURE_ADA_USDC`;
  * 如果您想在DERIBIT交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`DERIBIT_FUTURE_ADA_USDC`;
  * 如果您想在LIGHTER交易所上为ADA/USDC交易对下合约订单，您可以使用这样的唯一标识符：`LIGHTER_FUTURE_ADA_USDC`;
  * 如果您想交易美股AAPL，可以使用这样的唯一标识符：`US_STOCK_AAPL_USDT`;
  * 如果您想交易港股00700，可以使用这样的唯一标识符：`HK_STOCK_00700_USDT`;
  * 如果您想交易美股ETF SPY，可以使用这样的唯一标识符：`US_ETF_SPY_USDT`;
  * 目前支持现货订单、U本位永续合约订单、现货杠杆订单、股票订单和ETF订单。股票及ETF仅支持跨所账户模式

**»» side** : 买 BUY 卖 SELL

**»» qty** : 交易币种数量 订单数量（强制性，除非现货市场买入；股票及ETF必须传qty）

**»» price** : 价格 限价订单价格（限价订单必须）。股票及ETF使用上市市场原生计价币种（USD/HKD/KRW/JPY）

**»» time_in_force** : 执行方式 默认GTC，支持类型枚举：GTC，IOC，FOK，POC，RPI。股票及ETF仅支持GTC

**»» quote_qty** : 报价币种数量 订单报价数量，仅用于现货市场买入订单；股票及ETF不支持

**»» reduce_only** : 只减仓 true、false

**»» position_side** : 仓位方向 不传单仓。LONG, SHORT 枚举值: LONG SHORT NONE

##  返回结果

返回结果名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none |  | 频道名  
place_order  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | object | true | none |  | 下单请求参数  
»» order_id | string | true | none |  | 订单号  
»» text | string | true | none |  | 客户端ID  
» result | object | true | none |  | 下单结果  
»» code | string | true | none |  | none  
»» message | string | true | none |  | none  
» time | integer | true | none |  | 时间戳（秒）  
» time_ms | integer | true | none |  | 时间戳（毫秒）  
  
请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "place_order",
      "request_id": "request-1",
      "payload": {
        "header": {
          "X-Gate-Channel-Id": "broker-api"
        },
        "text": "test1",
        "symbol": "GATE_FUTURE_ETH_USDT",
        "side": "BUY",
        "qty": "0.01",
        "price": "2800",
        "type": "LIMIT"
      }
    }
    

返回示例
    
    
    {
      "channel": "place_order",
      "event": "api",
      "request_id": "request-1",
      "payload": {
        "order_id": "2072652940337152",
        "text": "2072652940337152"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  取消订单

`cancel_order`

提供了一种通过 WebSocket 取消订单的方式。

限频: 每10秒100次请求（同REST下单共享限频）

##  客户端请求

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 通道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | string | 是 | 订单号(支持订单id或text)  
  
###  详细说明

**» event** : api

**» channel** : cancel_order

##  返回结果

返回结果名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none |  | 通道名  
cancel_order  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» result | object | true | none |  | 取消订单结果  
»» code | string | true | none |  | 响应码  
»» message | string | true | none |  | 响应信息  
» time | integer | true | none |  | 时间戳（秒）  
» time_ms | integer | true | none |  | 时间戳（毫秒）  
  
请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "cancel_order",
      "request_id": "request-1",
      "payload": "2065058175870464"
    }
    

返回示例
    
    
    {
      "channel": "cancel_order",
      "event": "api",
      "request_id": "request-1",
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  批量取消订单

`batch_cancel_orders`

提供了一种通过 WebSocket 批量取消订单的方式。每个订单可使用订单 ID 或用户自定义 ID 撤销；两者同时传入时优先使用订单 ID。

限频: 每10秒100次请求（同 REST 撤单共享限频）

##  客户端请求

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 通道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | array | 是 | 待撤销的订单列表  
»» order_id | body | string | 否 | 订单 ID，与 text 必传其一  
»» text | body | string | 否 | 用户创建订单时指定的自定义 ID，与 order_id 必传其一  
  
###  详细说明

**» event** : api

**» channel** : batch_cancel_orders

##  返回结果

返回结果名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none |  | 通道名  
batch_cancel_orders  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | array | true | none |  | 批量撤单请求处理结果  
»» order_id | string | true | none |  | 订单 ID  
»» text | string | true | none |  | 用户创建订单时指定的自定义 ID  
»» accepted | string | true | none |  | 是否受理成功，字符串 true 或 false  
»» label | string | true | none |  | 受理失败时的错误标识，成功时为空  
»» message | string | true | none |  | 受理失败时的错误信息，成功时为空  
» result | object | true | none |  | 接口调用结果  
»» code | string | true | none |  | 响应码  
»» message | string | true | none |  | 响应信息  
» time | integer | true | none |  | 时间戳（秒）  
» time_ms | integer | true | none |  | 时间戳（毫秒）  
  
请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "batch_cancel_orders",
      "request_id": "request-1",
      "payload": [
        {
          "order_id": "2065058175870464"
        },
        {
          "text": "crossex-test-1"
        }
      ]
    }
    

返回示例
    
    
    {
      "channel": "batch_cancel_orders",
      "event": "api",
      "request_id": "request-1",
      "payload": [
        {
          "order_id": "2065058175870464",
          "text": "crossex-test-1",
          "accepted": "true",
          "label": "",
          "message": ""
        },
        {
          "order_id": "999999",
          "text": "",
          "accepted": "false",
          "label": "TRADE_ORDER_NOT_FOUND_ERROR",
          "message": "The order was not found"
        }
      ],
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  修改订单

`update_order`

可以只修改数量或价格。省略某项或传入 `"0"` 表示沿用该项原值。至少提供一个新的正数值。

限频: 每10秒100次请求（同REST下单共享限频）

##  客户端请求

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 释义 | 说明  
---|---|---|---|---|---  
» time | body | integer | 是 |  | 时间戳（秒）  
» event | body | string | 是 |  | 事件  
» channel | body | string | 是 |  | 通道名  
» request_id | body | string | 否 |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | object | 是 |  | none  
»» order_id | body | string | 是 | 订单ID | 支持订单id或text  
»» qty | body | string | 否 | 修改后的数量 | 省略或传 `"0"` 时沿用原值  
»» price | body | string | 否 | 修改后的价格 | 省略或传 `"0"` 时沿用原值  
  
###  详细说明

**» event** : api

**» channel** : update_order

##  返回结果

返回结果名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none |  | 通道名  
update_order  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | object | true | none |  | none  
»» order_id | string | true | none |  | 订单ID  
»» text | string | true | none |  | 客户端ID  
» result | object | true | none |  | 修改结果  
»» code | string | true | none |  | 响应码  
»» message | string | true | none |  | 响应消息  
» time | integer | true | none |  | 时间戳（秒）  
» time_ms | integer | true | none |  | 时间戳（毫秒）  
  
请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "update_order",
      "request_id": "request-1",
      "payload": {
        "order_id": "2065057827622656",
        "price": "2801"
      }
    }
    

返回示例
    
    
    {
      "channel": "update_order",
      "event": "api",
      "request_id": "request-1",
      "payload": {
        "order_id": "2072652940337152",
        "text": "2072652940337152"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  修改合约的杠杆倍数

`set_leverage`

提供了一种通过 WebSocket 修改合约杠杆倍数的方式。

限频: 每10秒100次请求（同REST下单共享限频）

##  客户端请求

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | object | 是 | none  
»» symbol | body | string | 是 | 币对  
»» leverage | body | string | 是 | 倍数  
  
##  详细说明

**» event** : api

**» channel** : set_leverage

##  返回结果

返回结果名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none |  | 频道名  
set_leverage  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | object | true | none |  | none  
»» symbol | string | true | none |  | 币对  
»» leverage | string | true | none |  | 倍数  
» result | object | true | none |  | 修改结果  
»» code | string | true | none |  | 响应码  
»» message | string | true | none |  | 响应消息  
» time | integer | true | none |  | 时间戳（秒）  
» time_ms | integer | true | none |  | 时间戳（毫秒）  
  
请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "set_leverage",
      "request_id": "request-1",
      "payload": {
        "symbol": "GATE_FUTURE_ETH_USDT",
        "leverage": "5"
      }
    }
    

返回示例
    
    
    {
      "channel": "set_leverage",
      "event": "api",
      "request_id": "request-1",
      "payload": {
        "symbol": "GATE_FUTURE_ETH_USDT",
        "leverage": "10"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  修改现货杠杆的杠杆倍数

`set_margin_leverage`

提供了一种通过 WebSocket 修改现货杠杆倍数的方式。

限频: 每10秒100次请求（同REST下单共享限频）

##  客户端请求

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | object | 是 | none  
»» symbol | body | string | 是 | 币对  
»» leverage | body | string | 是 | 倍数  
  
##  详细说明

**» event** : api

**» channel** : set_margin_leverage

##  返回结果

返回结果名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none |  | 频道名  
set_leverage  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | object | true | none |  | none  
»» symbol | string | true | none |  | 币对  
»» leverage | string | true | none |  | 倍数  
» result | object | true | none |  | 修改结果  
»» code | string | true | none |  | 响应码  
»» message | string | true | none |  | 响应消息  
» time | integer | true | none |  | 时间戳（秒）  
» time_ms | integer | true | none |  | 时间戳（毫秒）  
  
请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "set_margin_leverage",
      "request_id": "request-1",
      "payload": {
        "symbol": "OKX_MARGIN_ADA_USDT",
        "leverage": "5"
      }
    }
    

返回示例
    
    
    {
      "channel": "set_margin_leverage",
      "event": "api",
      "request_id": "request-1",
      "payload": {
        "symbol": "OKX_MARGIN_ADA_USDT",
        "leverage": "5"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  更改账户合约仓位模式和账户模式

`update_accounts`

提供了一种通过 WebSocket 更改账户合约仓位模式和账户模式的方式。

每60秒100次请求

##  客户端请求

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | object | 是 | none  
»» position_mode | body | string | 否 | 仓位模式  
»» account_mode | body | string | 否 | 账户模式  
»» exchange_type | body | string | 否 | 交易所。分所模式修改合约仓位模式时必填，支持 `ASTER` 等交易所  
  
###  详细说明

**» event** : api

**» channel** : update_accounts

**»» position_mode** : SINGLE/DUAL

**»» account_mode** : CROSS_EXCHANGE/ISOLATED_EXCHANGE

**»» exchange_type** : BINANCE/OKX/GATE/BYBIT/KRAKEN/HYPERLIQUID/DERIBIT/LIGHTER/CROSSEX，当账户模式为ISOLATED_EXCHANGE时，修改合约仓位模式必须指定交易所

##  返回结果

返回结果名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none |  | 频道名  
update_accounts  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | object | true | none |  | none  
»» position_mode | string | false | none |  | 仓位模式  
»» account_mode | string | false | none |  | 账户模式  
»» exchange_type | string | false | none |  | 交易所  
» result | object | true | none |  | 修改结果  
»» code | string | true | none |  | 响应码  
»» message | string | true | none |  | 响应信息  
» time | integer | true | none |  | 时间戳（秒）  
» time_ms | integer | true | none |  | 时间戳（毫秒）  
  
请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "update_accounts",
      "request_id": "request-1",
      "payload": {
        "account_mode": "ISOLATED_EXCHANGE",
        "position_mode": "DUAL",
        "exchange_type": "BINANCE"
      }
    }
    

返回示例
    
    
    {
      "channel": "update_accounts",
      "event": "api",
      "request_id": "request-1",
      "payload": {
        "account_mode": "ISOLATED_EXCHANGE",
        "position_mode": "DUAL",
        "exchange_type": "BINANCE"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  完全平仓

`close_position`

提供了一种通过 WebSocket 完全平仓的方式。

每天100次请求

##  客户端请求

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | object | 是 | none  
»» symbol | body | string | 是 | 币对  
»» position_side | body | string | 否 | 仓位方向  
  
##  详细说明

**» event** : api

**» channel** : close_position

##  返回结果

返回结果名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none |  | 频道名  
close_position  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | object | true | none |  | none  
»» order_id | string | true | none |  | 订单号  
»» text | string | true | none |  | 客户端ID  
  
请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "close_position",
      "request_id": "request-1",
      "payload": {
        "symbol": "GATE_MARGIN_ETH_USDT",
        "position_side": "LONG"
      }
    }
    

返回示例
    
    
    {
      "channel": "close_position",
      "event": "api",
      "request_id": "request-1",
      "payload": {
        "order_id": "2072652940337152",
        "text": "2072652940337152"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  修改合约仓位保证金模式

`set_margin_mode`

提供了一种通过 WebSocket 修改合约仓位保证金模式的方式。

仅支持Hyperliquid合约交易币对，存在挂单或仓位时不允许修改。

限频: 每10秒100次请求（同REST接口共享限频）

##  客户端请求

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | object | 是 | none  
»» symbol | body | string | 是 | Hyperliquid合约交易币对  
»» margin_mode | body | string | 是 | 保证金模式（CROSS/ISOLATED）  
  
##  详细说明

**» event** : api

**» channel** : set_margin_mode

##  返回结果

返回结果名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none |  | 频道名  
set_margin_mode  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | object | true | none |  | none  
»» symbol | string | true | none |  | 合约交易币对  
»» margin_mode | string | true | none |  | 保证金模式（CROSS/ISOLATED）  
» result | object | true | none |  | 修改结果  
»» code | string | true | none |  | 响应码  
»» message | string | true | none |  | 响应信息  
» time | integer | true | none |  | 时间戳（秒）  
» time_ms | integer | true | none |  | 时间戳（毫秒）  
  
请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "set_margin_mode",
      "request_id": "request-1",
      "payload": {
        "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
        "margin_mode": "ISOLATED"
      }
    }
    

返回示例
    
    
    {
      "channel": "set_margin_mode",
      "event": "api",
      "request_id": "request-1",
      "payload": {
        "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
        "margin_mode": "ISOLATED"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  增加或减少逐仓保证金

`update_isolated_margin`

提供了一种通过 WebSocket 增加或减少逐仓保证金的方式。

仅支持Hyperliquid逐仓合约仓位，正数为增加保证金，负数为减少保证金。

限频: 每10秒100次请求（同REST接口共享限频）

##  客户端请求

##  请求参数

请求参数名称 | 位置 | 类型 | 必选 | 说明  
---|---|---|---|---  
» time | body | integer | 是 | 时间戳（秒）  
» event | body | string | 是 | 事件  
» channel | body | string | 是 | 频道名  
» request_id | body | string | 否 | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | body | object | 是 | none  
»» symbol | body | string | 是 | Hyperliquid合约交易币对  
»» margin | body | string | 是 | 保证金调整金额，正数为增加，负数为减少，超过两位小数时向零截断  
»» position_side | body | string | 否 | 仓位方向（NONE/LONG/SHORT），单向持仓不传时默认为NONE  
  
##  详细说明

**» event** : api

**» channel** : update_isolated_margin

追加金额折合 USDT 后不得超过账户可用保证金的 80%。双向持仓必须在 `position_side` 中传入 `LONG` 或 `SHORT`。单向持仓省略该字段时使用 `NONE`。

##  返回结果

返回结果名称 | 类型 | 必选 | 约束 | 释义 | 说明  
---|---|---|---|---|---  
» channel | string | true | none |  | 频道名  
update_isolated_margin  
» event | string | true | none |  | 事件  
api  
» request_id | string | false | none |  | 请求 id，服务器会发回，帮助你识别服务器响应的是哪个请求  
» payload | object | true | none |  | none  
»» symbol | string | true | none |  | 合约交易币对  
»» margin | string | true | none |  | 本次增加或减少的逐仓保证金  
»» position_size | string | true | none |  | 仓位方向  
» result | object | true | none |  | 修改结果  
»» code | string | true | none |  | 响应码  
»» message | string | true | none |  | 响应信息  
» time | integer | true | none |  | 时间戳（秒）  
» time_ms | integer | true | none |  | 时间戳（毫秒）  
  
单向持仓减少逐仓保证金请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "update_isolated_margin",
      "request_id": "request-1",
      "payload": {
        "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
        "margin": "-30",
        "position_side": "NONE"
      }
    }
    

双向持仓增加多仓逐仓保证金请求示例
    
    
    {
      "time": 1754272114,
      "event": "api",
      "channel": "update_isolated_margin",
      "request_id": "request-2",
      "payload": {
        "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
        "margin": "30",
        "position_side": "LONG"
      }
    }
    

返回示例
    
    
    {
      "channel": "update_isolated_margin",
      "event": "api",
      "request_id": "request-1",
      "payload": {
        "symbol": "HYPERLIQUID_FUTURE_CXMT_USDC",
        "margin": "-30",
        "position_side": "NONE"
      },
      "result": {
        "code": "100000",
        "message": "success"
      },
      "time": 1756434168,
      "time_ms": 1756434168948
    }
    

#  返回码

##  `code` 说明

code 说明返回码 | 说明  
---|---  
100000 | 成功  
100001 | 参数丢失或无效  
100002 | 未登陆  
100003 | 连接达到最大数  
100004 | 超时  
100005 | 操作失败  
100006 | 登陆失败  
100007 | 网络错误，请稍后再试  
  
##  `label` 说明

私有请求失败时，`result.label` 的含义与 [REST 错误说明](/docs/developers/crossex/zh_CN/#异常-label-列表)一致。股票及 ETF 下单常见的错误包括 `SECURITY_ORDER_NOT_SUPPORT`（账户模式不支持）、`SECURITY_ORDER_ONLY_SUPPORT_GTC`（只允许 `GTC`）和 `COMMON_FAIL_ORDER_ERROR`（例如缺少行情汇率）。

合约 Rebase 期间，`place_order`、`update_order`、`set_leverage`、`update_isolated_margin`、`close_position` 对受影响交易对返回 `result.label=TRADE_REBASE_TASK_STARTED`。客户端可通过 REST 的币对查询查看 `state` 是否为 `rebase`。

包含 `label` 的响应示例
    
    
    {
      "time": 1787560434,
      "channel": "not_exist",
      "event": "api",
      "result": {
        "code": "100001",
        "label": "COMMON_PARAM_BIND_ERROR",
        "message": "Invalid Parameter, please check api doc"
      },
      "time_ms": 1787560434000,
      "request_id": "xxx"
    }
    

##  公有行情错误码

公有订阅或退订失败时，`result.status` 为 `failed`，`error.code` 为整数，`error.message` 提供具体原因。

`error.code` | 说明  
---|---  
`1000000` | 存在不支持的交易对，详情见 `error.message`  
`1000001` | Binance 有限档盘口仅支持 5、10、20 档  
`1000002` | OKX 有限档盘口仅支持 1、5 档  
`1000003` | Gate 合约有限档盘口仅支持 1、5、10、20、50、100 档  
`1000004` | Gate 现货有限档盘口仅支持 5、10、20、30、50、100 档  
`1000005` | `index_price` 只支持 `MARGIN` 币对  
`1000006` | 频道无效，或 `mark_price` 请求中含非合约币对。通过 `error.message` 区分  
`1000007` | 请求事件无效  
`1000008` | `payload` 无效  
`1000100` | 请求消息格式无效  
`1000101` | Bybit 有限档盘口仅支持 1 档  
`1000102` | 当前连接在该频道已达到订阅交易对数量上限  
`1000103` | 当前 IP 达到公有 WS 连接数上限  
`1000104` | Binance 合约不支持 `open_interest`  
`1000105` | `funding_rate` 和 `open_interest` 只支持合约币对  
`1000106` | Kraken 不提供有限档盘口，使用 `order_book_update`  
`1000107` | Kraken 不支持 WebSocket K 线  
`1000108` | Hyperliquid 现货交易对缺少原生币种映射  
`1000109` | Deribit 有限档盘口仅支持 1、5、10、20 档  
`1000110` | Deribit K 线仅支持 1m、5m、15m、30m、1h、1d  
`1000111` | Hyperliquid 有限档盘口仅支持 1、5、10、20 档  
`1000112` | 当前 IP 达到每分钟操作次数上限  
`1000113` | Lighter 合约交易对缺少原生市场 ID 映射  
`1000114` | Aster 有限档盘口仅支持 1、5、10、20 档  
`1000115` | Aster 合约不支持 `open_interest`  
`1000116` | 连接的发送缓冲已满  
`1000117` | 订阅未能完成，可稍后重试  
`1000119` | 股票和 ETF 不支持 `order_book_update`  
  
Last Updated: 11/26/2026, 4:46:36 PM