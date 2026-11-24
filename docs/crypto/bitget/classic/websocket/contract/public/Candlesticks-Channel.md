---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/public/Candlesticks-Channel
api_type: WebSocket
updated_at: 2026-11-24 19:00:36.856059
---

# Candlestick Channel

### Description

If intended to query history data in a customized time range, please refer to Get Candle Data

When there are transactions in the K-line channel, data is pushed once per second.

When there are no transactions, data is pushed once at the specified time granularity.

:::info{title="Push logic adjustment"}
Effective in **demo trading** on November 4, 2026, and expected in **live trading** on November 17, 2026: after a successful subscription, this channel will no longer push snapshot data (`action`=`snapshot`); only real-time incremental data (`action`=`update`) will be pushed. Before the adjustment takes effect, the first push after subscription is a snapshot of recent data. To obtain historical data, please use the corresponding REST API.
:::

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "candle1m",
            "instId": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameter | Type | Required | Description | 
| :---- | :---- | :---- | :---- |
| op | String | Yes | Operation, subscribe unsubscribe  |
| args | List&lt;Object&gt; | Yes | List of channels to request subscription |
| &gt; instType | String | Yes | Product type  |
| &gt; channel | String | Yes | Channel name, candle1m (1 minute) candle5m (5 minutes) candle15m (15 minutes) candle30m (30 minutes) candle1H (1 hour) candle4H (4 hours) candle12H (12 hours)<br/>candle1D (1 day) candle1W (1 week) candle6H (6 hours) candle3D (3 days) candle1M (1-month line) candle6Hutc (6-hour line, UTC) candle12Hutc (12-hour line, UTC)<br/>candle1Dutc (1-day line, UTC) candle3Dutc (3-day line, UTC) candle1Wutc (weekly line, UTC) candle1Mutc (monthly line. UTC) |
| &gt; instId | String | Yes | Product ID<br/>E.g. ETHUSDT |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "candle1m",
        "instId": "BTCUSDT"
    }
}
```

### Response Parameters

| Parameter     | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 
|:--------------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| event         | String  | Yes<br/>Event                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| arg           | Object  | Subscribed channels                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| &gt; channel  | String  | Channel name, candle1m (1 minute) candle5m (5 minutes) candle15m (15 minutes) candle30m (30 minutes) candle1H (1 hour) candle4H (4 hours) candle12H (12 hours)<br/>candle1D (1 day) candle1W (1 week) candle6H (6 hours) candle3D (3 days) candle1M (1-month line) candle6Hutc (6-hour line, UTC) candle12Hutc (12-hour line, UTC)<br/>candle1Dutc (1-day line, UTC) candle3Dutc (3-day line, UTC) candle1Wutc (weekly line, UTC) candle1Mutc (monthly line. UTC) |
| &gt; instType | String  | Product type                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| &gt; instId   | String  | Product ID<br/>E.g. ETHUSDT                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| code          | String  | Error code, returned only on error                                                                                                                                                                                                                                                                                                                                                                                                                                |
| msg           | String  | Error message                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
    "action": "update",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "candle1m",
        "instId": "BTCUSDT"
    },
    "data": [
        [
            "1695685500000",
            "27000",
            "27000.5",
            "27000",
            "27000.5",
            "0.057",
            "1539.0155",
            "1539.0155"
        ]
    ],
    "ts": 1695715462250
}
```

### Push Parameters

| Parameter         | Type               | Description                                                          | 
|:------------------|:-------------------|:---------------------------------------------------------------------|
| action            | String             | Push data action, `snapshot` or `update`<br/>After the push logic adjustment takes effect, only `update` is pushed |
| arg               | Object             | Channels with successful subscription                                |
| &gt; channel      | String             | Channel name                                                         |
| &gt; instId       | String             | Product ID                                                           | E.g. ETHUSDT |
| &gt; instType     | String             | Product type                                                         |
| data              | List&lt;String&gt; | Subscription data                                                    |
| &gt; index[0]     | String             | Start time, milliseconds format of Unix timestamp, e.g.1597026383085 |
| &gt; index[1]     | String             | Opening price                                                        |
| &gt; index[2]     | String             | Highest price                                                        |
| &gt; index[3]     | String             | Lowest price                                                         |
| &gt; index[4]     | String             | Closing price                                                        |
| &gt; index[5]     | String             | The value is the trading volume of left coin                         | Trading volume of the coin |
| &gt; index[6]     | String             | Trading volume of quote currency                                     |
| &gt; index[7]     | String             | Trading volume of USDT                                               |
| ts                | String             | Data streaming time                                                  |

</div>

---

# K线频道

### 描述

订单K线频道

k线频道有成交，1s推送一次

没成交，到时间粒度时推送一次

:::info{title="推送逻辑调整"}
模拟盘自 2026 年 11 月 4 日起生效，实盘预计 2026 年 11 月 17 日生效：订阅成功后，本频道不再推送快照数据（`action`=`snapshot`），仅推送实时增量数据（`action`=`update`）。调整生效前，订阅后首次推送为最近数据的快照。如需获取历史数据，请使用对应的 REST 接口。
:::

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "candle1m",
            "instId": "BTCUSDT"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                                                                                                                                                                                                                                                                                                                                       | 
| :---- | :---- | :---- |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| op | String | 是 | 操作, subscribe unsubscribe                                                                                                                                                                                                                                                                                                                |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表                                                                                                                                                                                                                                                                                                                                |
| &gt; instType | String | 是 | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约                                                                                                                                                                                                                                                         |
| &gt; channel | String | 是 | 频道名，candle1m (1分钟) candle5m (5分钟) candle15m (15分钟) candle30m (30分钟) candle1H (1小时) candle4H (4小时) candle12H (12小时)<br/>candle1D (1天) candle1W (1周) candle6H (6小时) candle3D  (3天) candle1M (1月线) candle6Hutc (零时区 6小时线) candle12Hutc (零时区12小时线)<br/>candle1Dutc (零时区 1日线) candle3Dutc (零时区 3日线) candle1Wutc (零时区 周线) candle1Mutc (零时区 月线) |
| &gt; instId | String | 是 | 产品ID<br/>如：ETHUSDT                                                                                                                                                                                                                                                                                                                       |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "candle1m",
        "instId": "BTCUSDT"
    }
}
```

### 返回参数

| 返回字段          | 参数类型     | 字段说明                                                                                                                                                                                                                                                                                                                                     | 
|:--------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| event         | String   | 事件                                                                                                                                                                                                                                                                                                                                       |
| arg           | Object   | 订阅的频道                                                                                                                                                                                                                                                                                                                                    |
| &gt; channel  | String   | 频道名，candle1m (1分钟) candle5m (5分钟) candle15m (15分钟) candle30m (30分钟) candle1H (1小时) candle4H (4小时) candle12H (12小时)<br/>candle1D (1天) candle1W (1周) candle6H (6小时) candle3D  (3天) candle1M (1月线) candle6Hutc (零时区 6小时线) candle12Hutc (零时区12小时线)<br/>candle1Dutc (零时区 1日线) candle3Dutc (零时区 3日线) candle1Wutc (零时区 周线) candle1Mutc (零时区 月线) |
| &gt; instType | String   | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约<br/>                                                                                                                                                                                                                                                    |
| &gt; instId   | String   | 产品ID, 如：ETHUSDT                                                                                                                                                                                                                                                                                                                          |
| code          | String   | 错误码                                                                                                                                                                                                                                                                                                                                      |
| msg           | String   | 错误消息                                                                                                                                                                                                                                                                                                                                     |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "update",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "candle1m",
        "instId": "BTCUSDT"
    },
    "data": [
        [
            "1695685500000",
            "27000",
            "27000.5",
            "27000",
            "27000.5",
            "0.057",
            "1539.0155",
            "1539.0155"
        ]
    ],
    "ts": 1695715462250
}
```

### 推送数据参数

| 返回字段               | 参数类型               | 字段说明                                                                             | 
|:-------------------|:-------------------|:---------------------------------------------------------------------------------|
| action             | String             | 推送动作, `snapshot` or `update`<br/>推送逻辑调整生效后，仅推送 `update`                                                     |
| arg                | Object             | 订阅成功的频道                                                                          |
| &gt; channel       | String             | 频道名                                                                              |
| &gt; instId        | String             | 产品ID, 如：ETHUSDT                                                                  |
| &gt; instType      | String             | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| data               | List&lt;String&gt; | 订阅的数据                                                                            |
| &gt; index[0]      | String             | 开始时间，Unix时间戳的毫秒数格式，如 1597026383085                                               |
| &gt; index[1]      | String             | 开盘价格                                                                             |
| &gt; index[2]      | String             | 最高价格                                                                             |
| &gt; index[3]      | String             | 最低价格                                                                             |
| &gt; index[4]      | String             | 收盘价格                                                                             |
| &gt; index[5]      | String             | 数值为左币交易量, 交易币成交量                                                                 |
| &gt; index[6]      | String             | 计价币成交量                                                                           |
| &gt; index[7]      | String             | 折合USDT量                                                                          |
| ts                 | String             | 数据推送时间                                                                           |

</div>