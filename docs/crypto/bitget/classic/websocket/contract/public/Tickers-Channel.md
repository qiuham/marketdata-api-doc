---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/public/Tickers-Channel
api_type: WebSocket
updated_at: 2026-11-19 19:06:41.624120
---

# Market Channel

### Description

Retrieve the latest traded price, bid price, ask price and 24-hour trading volume of the instruments. When there is
a change (deal, buy, sell, issue): 300ms to 400ms.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "ticker",
            "instId": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameter     | Type               | Required | Description                              | 
|:--------------|:-------------------|:---------|:-----------------------------------------|
| op            | String             | Yes      | Operation, subscribe unsubscribe         |
| args          | List&lt;Object&gt; | Yes      | List of channels to request subscription |
| &gt; instType | String             | Yes      | Product type                             |
| &gt; channel  | String             | Yes      | Channel name                             |
| &gt; instId   | String             | Yes      | Product ID<br/>E.g. ETHUSDT              |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "USDT-FUTURES",
    "channel": "ticker",
    "instId": "BTCUSDT"
  }
}
```

### Response Parameters

| Parameter     | Type   | Description                 | 
|:--------------|:-------|:----------------------------|
| event         | String | Event                       |
| arg           | Object | Subscribed channels         |
| &gt; instType | String | Product type                |
| &gt; channel  | String | Channel name                |
| &gt; instId   | String | Product ID<br/>E.g. ETHUSDT |
| code          | String | Error code                  |
| msg           | String | Error message               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "data": [
    {
      "lastPr": "87673.6",
      "symbol": "BTCUSDT",
      "indexPrice": "87714.0732915359034044",
      "open24h": "87027.0",
      "nextFundingTime": "1766678400000",
      "bidPr": "87673.6",
      "change24h": "0.00743",
      "quoteVolume": "1521198076.61216",
      "deliveryPrice": "0",
      "askSz": "14.333",
      "low24h": "86542.5",
      "symbolType": "1",
      "openUtc": "87628.9",
      "instId": "BTCUSDT",
      "bidSz": "6.9129",
      "markPrice": "87673.7",
      "high24h": "88022.1",
      "askPr": "87673.7",
      "holdingAmount": "28135.5456",
      "baseVolume": "17398.1612",
      "fundingRate": "0.000055",
      "ts": "1766674540816"
    }
  ],
  "arg": {
    "instType": "USDT-FUTURES",
    "instId": "BTCUSDT",
    "channel": "ticker"
  },
  "action": "snapshot",
  "ts": 1766674540817
}
```

### Push Parameters

| Parameter           | Type   | Description                                                                                                                                                                                                         | 
|:--------------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| arg                 | Object | Channels with successful subscription                                                                                                                                                                               |
| &gt; instType       | String | Product type                                                                                                                                                                                                        |
| &gt; channel        | String | Channel name                                                                                                                                                                                                        |
| &gt; instId         | String | Product ID                                                                                                                                                                                                          |
| action              | String | Push data action, `snapshot`                                                                                                                                                                                        |
| data                | List   | Subscription data                                                                                                                                                                                                   |
| &gt; instId         | String | Product ID, BTCUSDT                                                                                                                                                                                                 |
| &gt;lastPr          | String | Latest price                                                                                                                                                                                                        |
| &gt;askPr           | String | Ask price                                                                                                                                                                                                           |
| &gt;bidPr           | String | Bid price                                                                                                                                                                                                           |
| &gt;high24h         | String | 24h high                                                                                                                                                                                                            |
| &gt;low24h          | String | 24h low                                                                                                                                                                                                             |
| &gt;change24h       | String | 24h change                                                                                                                                                                                                          |
| &gt;fundingRate     | String | Funding rate                                                                                                                                                                                                        |
| &gt;nextFundingTime | String | Next funding rate settlement time,  Milliseconds format of timestamp Unix, e.g. 1597026383085                                                                                                                       |
| &gt;ts              | String | System time, Milliseconds format of current data timestamp Unix, e.g. 1597026383085                                                                                                                                 |
| &gt;markPrice       | String | Mark price                                                                                                                                                                                                          |
| &gt;indexPrice      | String | Index price                                                                                                                                                                                                         |
| &gt;holdingAmount   | String | Open interest                                                                                                                                                                                                       |
| &gt;baseVolume      | String | Trading volume of the coin                                                                                                                                                                                          |
| &gt;quoteVolume     | String | Trading volume of quote currency                                                                                                                                                                                    |
| &gt;openUtc         | String | Price at 00:00 (UTC)                                                                                                                                                                                                |
| &gt;symbolType      | String | SymbolType: 1-&gt;perpetual 2-&gt;delivery                                                                                                                                                                          |
| &gt;symbol          | String | Trading pair                                                                                                                                                                                                        |
| &gt;deliveryPrice   | String | Delivery price of the delivery futures, when symbolType = 1(perpetual) it is always 0<br/>It will be pushed 1 hour before delivery<br/>Returns empty if delivery price does not exist                               |
| &gt;bidSz           | String | Buying amount                                                                                                                                                                                                       |
| &gt;askSz           | String | selling amount                                                                                                                                                                                                      |
| &gt;open24h         | String | Entry price of the last 24 hours, The opening time is compared on a 24-hour basis. i.e.: Now it is 7:00 PM of the 2nd day of the month, then the corresponding opening time is 7:00 PM of the 1st day of the month. |
| ts                  | String | Data streaming time                                                                                                                                                                                                 |

</div>

---

# 行情频道

### 描述

获取产品的最新成交价、买一价、卖一价和24小时交易量等信息，有变化（成交、买一卖一发）时：300ms 至 400ms

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "ticker",
            "instId": "BTCUSDT"
        }
    ]
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                                                                               | 
|:--------------|:-------------------|:-----|:---------------------------------------------------------------------------------|
| op            | String             | 是    | 操作, subscribe unsubscribe                                                        |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                        |
| &gt; instType | String             | 是    | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| &gt; channel  | String             | 是    | 频道名                                                                              |
| &gt; instId   | String             | 是    | 产品ID<br/>如：ETHUSDT                                                               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "USDT-FUTURES",
    "channel": "ticker",
    "instId": "BTCUSDT"
  }
}
```

### 返回参数

| 返回字段          | 参数类型   | 字段说明               | 
|:--------------|:-------|:-------------------|
| event         | String | 事件                 |
| arg           | Object | 订阅的频道              |
| &gt; instType | String | 产品类型               |
| &gt; channel  | String | 频道名                |
| &gt; instId   | String | 产品ID<br/>如：ETHUSDT |
| code          | String | 错误码                |
| msg           | String | 错误消息               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
  "data": [
    {
      "lastPr": "87673.6",
      "symbol": "BTCUSDT",
      "indexPrice": "87714.0732915359034044",
      "open24h": "87027.0",
      "nextFundingTime": "1766678400000",
      "bidPr": "87673.6",
      "change24h": "0.00743",
      "quoteVolume": "1521198076.61216",
      "deliveryPrice": "0",
      "askSz": "14.333",
      "low24h": "86542.5",
      "symbolType": "1",
      "openUtc": "87628.9",
      "instId": "BTCUSDT",
      "bidSz": "6.9129",
      "markPrice": "87673.7",
      "high24h": "88022.1",
      "askPr": "87673.7",
      "holdingAmount": "28135.5456",
      "baseVolume": "17398.1612",
      "fundingRate": "0.000055",
      "ts": "1766674540816"
    }
  ],
  "arg": {
    "instType": "USDT-FUTURES",
    "instId": "BTCUSDT",
    "channel": "ticker"
  },
  "action": "snapshot",
  "ts": 1766674540817
}
```

### 推送数据参数

| 返回字段                | 参数类型   | 字段说明                                                                             | 
|:--------------------|:-------|:---------------------------------------------------------------------------------|
| arg                 | Object | 订阅成功的频道                                                                          |
| &gt; instType       | String | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| &gt; channel        | String | 频道名                                                                              |
| &gt; instId         | String | 产品ID                                                                             |
| action              | String | 推送数据动作，`snapshot`  全量推送数据                                                        |
| data                | List   | 订阅的数据                                                                            |
| &gt;instId          | String | 产品ID                                                                             |
| &gt;lastPr          | String | 最新成交价                                                                            |
| &gt;askPr           | String | 卖一价                                                                              |
| &gt;bidPr           | String | 买一价                                                                              |
| &gt;high24h         | String | 24小时最高价                                                                          |
| &gt;low24h          | String | 24小时最低价                                                                          |
| &gt;change24h       | String | 24小时涨跌幅                                                                          |
| &gt;fundingRate     | String | 资金费率                                                                             |
| &gt;nextFundingTime | String | 下次资金费率结算时间，  Unix时间戳的毫秒数格式，如 1597026383085                                       |
| &gt;ts              | String | 系统时间， 当前数据时间戳 Unix时间戳的毫秒数格式，如 1597026383085                                      |
| &gt;markPrice       | String | 标记价格                                                                             |
| &gt;indexPrice      | String | 指数价格                                                                             |
| &gt;holdingAmount   | String | 持仓量                                                                              |
| &gt;baseVolume      | String | 交易币交易量                                                                           |
| &gt;quoteVolume     | String | 计价币交易额                                                                           |
| &gt;openUtc         | String | UTC 00:00时刻价格                                                                    |
| &gt;symbolType      | String | SymbolType：1-&gt;永续 2-&gt;交割                                                     |
| &gt;symbol          | String | 交易对                                                                              |
| &gt;deliveryPrice   | String | 交割合约交割价，symbolType=1（永续）时为0<br/>交割合约前一小时推送该字段<br/>交割价不存在则返回空                      |
| &gt;bidSz           | String | 买一量                                                                              |
| &gt;askSz           | String | 卖一量                                                                              |
| &gt;open24h         | String | 开盘价 24小时。 开盘时间为24小时相对比，即：现在为2号19点，那么开盘时间对应为1号19点。                                |
| ts                  | String | 数据推送时间                                                                           |

</div>