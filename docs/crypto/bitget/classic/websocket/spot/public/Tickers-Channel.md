---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/spot/public/Tickers-Channel
api_type: WebSocket
updated_at: 2026-11-21 19:03:00.798057
---

# Market Channel

### Description

Get the product's latest price, bid price, bid price and 24h trading volume information. Frequency of data push: 200ms ~ 300ms

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "ticker",
            "instId": "ETHUSDT"
        }
    ]
}
```

### Request Parameters

| Parameter     | Type   | Required           | Description                                      | 
|:--------------|:-------|:-------------------|:-------------------------------------------------|
| op            | String | Yes                | Operation, subscribe unsubscribe                 |
| args          | Array  | List&lt;Object&gt; | Yes<br/>List of channels to request subscription |
| &gt; instType | String | Yes                | Product line type                                |
| &gt; channel  | String | Yes                | Channel name                                     |
| &gt; instId   | String | Yes                | Product ID, e.g. ETHUSDT                         |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "SPOT",
    "channel": "ticker",
    "instId": "ETHUSDT"
  }
}
```

### Response Parameters

| Parameter     | Type   | Description                               | 
|:--------------|:-------|:------------------------------------------|
| event         | String | Yes<br/>Event                             |
| arg           | Object | Subscribed channels                |
| &gt; instType | String | Product type                      |
| &gt; channel  | String | Channel name                      |
| &gt; instId   | String | Product ID, e.g. ETHUSDT          |
| code          | String | Error code, returned only on error |
| msg           | String | Error message                      |

</div>

```json title="Push Data"
{
    "action": "snapshot",
    "arg": {
        "instType": "SPOT",
        "channel": "ticker",
        "instId": "ETHUSDT"
    },
    "data": [
        {
            "instId": "ETHUSDT",
            "lastPr": "2200.10",
            "open24h": "0.00",
            "high24h": "0.00",
            "low24h": "0.00",
            "change24h": "0.00",
            "bidPr": "1792",
            "askPr": "2200.1",
            "bidSz": "0.0084",
            "askSz": "19740.8811",
            "baseVolume": "0.0000",
            "quoteVolume": "0.0000",
            "openUtc": "0.00",
            "changeUtc24h": "0",
            "ts": "1695702438018"
        }
    ],
    "ts": 1695702438029
}
```

### Push Parameters

| Parameter         | Type               | Description                                                                    | 
|:------------------|:-------------------|:-------------------------------------------------------------------------------|
| arg               | Object             | Channels with successful subscription                                          |
| &gt; instType     | String             | Product type                                                                   |
| &gt; channel      | String             | Channel name                                                                   |
| &gt; instId       | String             | Product ID, e.g. ETHUSDT                                                       |
| action            | String             | Push data action: `snapshot`                                                   |
| data              | List&lt;Object&gt; | Subscription data                                                              |
| &gt; instId       | String             | Product ID, e.g. ETHUSDT                                                       |
| &gt; lastPr       | String             | Latest price                                                                   |
| &gt; askPr        | String             | Ask price                                                                      |
| &gt; bidPr        | String             | Bid price                                                                      |
| &gt; open24h      | String             | Entry price of the last 24 hours                                               |
| &gt; high24h      | String             | 24h high                                                                       |
| &gt; low24h       | String             | 24h low                                                                        |
| &gt; baseVolume   | String             | 24h trading volume in left coin                                                |
| &gt; quoteVolume  | String             | 24h trading volume in right coin                                               |
| &gt; ts           | String             | Milliseconds format of data generation time Unix timestamp, e.g. 1597026383085 |
| &gt; openUtc      | String             | UTC&plusmn;00:00 Entry price                                                   |
| &gt; changeUtc24h | String             | Change at UTC+0, 0.01 means 1%.                                                |
| &gt; bidSz        | String             | Buying amount                                                                  |
| &gt; askSz        | String             | Selling amount                                                                 |
| &gt; change24h    | String             | 24-hour change, 0.01 means 1%.                                                 |

---

# 行情频道

### 描述

获取产品的最新成交价、买一价、卖一价和24小时交易量等信息。定时推送频率：200ms 至 300ms

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "SPOT",
            "channel": "ticker",
            "instId": "ETHUSDT"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述 | 
| :---- | :---- | :---- | :---- |
| op | String | 是 | 操作，subscribe unsubscribe |
| args | Array | List&lt;Object&gt; | 是<br/>请求订阅的频道列表 |
| &gt; instType | String | 是 | 产品线类型, `SPOT` |
| &gt; channel | String | 是 | 频道名, `ticker`   |
| &gt; instId | String | 是 | 产品id 例如：ETHUSDT |

</div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "SPOT",
        "channel": "ticker",
        "instId": "ETHUSDT"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明 | 
| :---- | :---- | :---- |
| event | String | 事件 |
| arg | Object | 订阅的频道 |
| &gt; instType | String | 产品类型, `SPOT` |
| &gt; channel | String | 频道名, `ticker` |
| &gt; instId | String | 产品id 例如：ETHUSDT |
| code | String | 错误码，错误时才会返回 |
| msg | String | 错误消息 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "snapshot",
    "arg": {
        "instType": "SPOT",
        "channel": "ticker",
        "instId": "ETHUSDT"
    },
    "data": [
        {
            "instId": "ETHUSDT",
            "lastPr": "2200.10",
            "open24h": "0.00",
            "high24h": "0.00",
            "low24h": "0.00",
            "change24h": "0.00",
            "bidPr": "1792",
            "askPr": "2200.1",
            "bidSz": "0.0084",
            "askSz": "19740.8811",
            "baseVolume": "0.0000",
            "quoteVolume": "0.0000",
            "openUtc": "0.00",
            "changeUtc24h": "0",
            "ts": "1695702438018"
        }
    ],
    "ts": 1695702438029
}
```

### 推送数据参数

| 返回字段 | 参数类型 | 字段说明                                 | 
| :---- | :---- |:-------------------------------------|
| arg | Object | 订阅成功的频道                              |
| &gt; instType | String | 产品类型, `SPOT`                         |
| &gt; channel | String | 频道名, `ticker`                        |
| &gt; instId | String | 产品id 例如：ETHUSDT                      |
| action | String | 推送数据动作: `snapshot`                   |
| data | List&lt;Object&gt; | 订阅的数据                                |
| &gt; instId | String | 产品id 例如：ETHUSDT                      |
| &gt;lastPr | String | 最新成交价                                |
| &gt;askPr | String | 卖一价                                  |
| &gt;bidPr | String | 买一价                                  |
| &gt; open24h | String | 24小时开盘价                              |
| &gt; high24h | String | 24小时最高价                              |
| &gt; low24h | String | 24小时最低价                              |
| &gt; baseVolume | String | 24小时成交量，以左币为单位                       |
| &gt; quoteVolume | String | 24小时成交量，以右币为单位                       |
| &gt; ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 1597026383085 |
| openUtc | String | 零时区 开盘价                              |
| changeUtc24h | String | UTC0时涨跌幅, 0.01表示1%                   |
| &gt;bidSz | String | 买一量                                  |
| &gt;askSz | String | 卖一量                                  |
| &gt;change24h | String | 24小时涨跌幅, 0.01表示1%                    |

</div>