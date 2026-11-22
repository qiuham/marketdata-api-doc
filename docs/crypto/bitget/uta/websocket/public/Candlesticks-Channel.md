---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/Candlesticks-Channel
api_type: WebSocket
updated_at: 2026-11-22 19:00:44.671152
---

# Candlestick Channel

### Description

Get the candlestick data of the product

- When there are transactions in the K-line channel, data is pushed once per second.
- When there are no transactions, data is pushed once at the specified time granularity.

:::info{title="Push logic adjustment"}
Effective in **demo trading** on November 4, 2026, and expected in **live trading** on November 17, 2026: after a successful subscription, this channel will no longer push snapshot data (`action`=`snapshot`); only real-time incremental data (`action`=`update`) will be pushed. Before the adjustment takes effect, the first push after subscription is a snapshot of recent data. To obtain historical data, please use the corresponding REST API.
:::

:::warning{title="Notes for Reality stock (rtoken) symbol subscription"}

- Only the market candlestick type is supported.
- Only the `1m`, `5m`, `15m`, `1H`, `4H`, `1D` intervals are supported.
- For the `1m` interval, `volume` and `turnover` are not included in the push data.

:::

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "spot",
            "topic": "kline",
            "symbol": "BTCUSDT",
            "interval": "1D"
        }
    ]
}
```

### Request Parameters

| Parameter               | Type                | Required | Description                                                                                                                                  | 
|-------------------------|---------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| op                      | String              | Yes      | Action <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe                                                                           |
| args                    | List&lt;Object&gt;  | Yes      | Subscribed channel                                                                                                                           |
| &gt; instType           | String              | Yes      | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures   |
| &gt; topic              | String              | Yes      | Topic <br/> `kline` K-line channel                                                                                                           |
| &gt; symbol             | String              | Yes      | Symbol name <br/> e.g., `BTCUSDT`                                                                                                            |
| &gt; interval           | String              | Yes      | Interval <br/> `1m`, `3m`,`5m`, `15m`, `30m`, `1H`, `4H`,`6H`, `12H`, `1D`                                                                   |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "spot",
    "topic": "kline",
    "symbol": "BTCUSDT",
    "interval": "1D"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    | Type   | Description                                                                                                                                | 
|---------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------|
| event         | String | Action <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe <br/> `error` Parameter error                                           |
| arg           | Object | Subscribed channel                                                                                                                         |
| &gt; instType | String | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String | Topic <br/> `kline` K-line channel                                                                                                         |
| &gt; symbol   | String | Symbol name <br/> e.g., `BTCUSDT`                                                                                                          |
| &gt; interval | String | Interval                                                                                                                                   |
| code          | String | Error code                                                                                                                                 |
| msg           | String | Error message                                                                                                                              |
| connId        | String | Connection ID                                                                                                                              |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "data": [
    {
      "volume": "0.423",
      "high": "400005",
      "low": "276670",
      "start": "1710518400000",
      "close": "400005",
      "turnover": "148190.38375",
      "open": "276670"
    }
  ],
  "arg": {
    "instType": "spot",
    "symbol": "BTCUSDT",
    "topic": "kline",
    "interval": "1D"
  },
  "action": "update",
  "ts": 1736370735556
}
```

### Push Parameters

| Parameters      | Type               | Description                                                                                                                                 | 
|-----------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| arg             | Object             | Subscribed channel                                                                                                                          |
| &gt; instType   | String             | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures  |
| &gt; topic      | String             | Topic <br/> `kline`                                                                                                                         |
| &gt; symbol     | String             | Symbol name                                                                                                                                 |
| action          | String             | Push data action <br/> `snapshot` Full data <br/> `update` Incremental data<br/>After the push logic adjustment takes effect, only `update` is pushed                                                                 |
| data            | List&lt;Object&gt; | Subscribed data                                                                                                                             |
| &gt; start      | String             | The timestamp that the system generated the data <br/>A Unix timestamp in milliseconds                                                      |
| &gt; open       | String             | Open price                                                                                                                                  |
| &gt; close      | String             | Close price                                                                                                                                 |
| &gt; high       | String             | Highest price                                                                                                                               |
| &gt; low        | String             | Lowest price                                                                                                                                |
| &gt; volume     | String             | Trade Volume<br/>_The unit is base coin_                                                                                                    |
| &gt; turnover   | String             | Turnover<br/>_The unit is quote coin_                                                                                                        |

</div>

---

# K线

<h3 id="description">描述</h3>
订单K线频道

- k线频道有成交，1s推送一次。
- 没成交，到时间粒度时推送一次

:::info{title="推送逻辑调整"}
模拟盘自 2026 年 11 月 4 日起生效，实盘预计 2026 年 11 月 17 日生效：订阅成功后，本频道不再推送快照数据（`action`=`snapshot`），仅推送实时增量数据（`action`=`update`）。调整生效前，订阅后首次推送为最近数据的快照。如需获取历史数据，请使用对应的 REST 接口。
:::

:::warning{title="Reality 股票（rtoken）symbol 订阅说明"}

- K线类型仅支持 market（市场成交价K线）。
- 仅支持 `1m`、`5m`、`15m`、`1H`、`4H`、`1D` 时间粒度。
- `1m` 粒度下，K线推送数据不包含 `volume`（成交量）和 `turnover`（成交额）。

:::

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "spot",
            "topic": "kline",
            "symbol": "BTCUSDT",
            "interval": "1D"
        }
    ]
}
```

<h3 id="request-parameters">请求参数</h3>
| 参数名           | 参数类型               | 是否必须 | 描述                                                                                                  | 
|:--------------|:-------------------|:-----|:----------------------------------------------------------------------------------------------------|
| op            | String             | 是    | 操作<br/>`subscribe` 订阅 <br/>`unsubscribe` 退订                                                         |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                                           |
| &gt; instType | String             | 是    | 产品线类型<br/>`spot` 现货交易<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String             | 是    | 频道名<br/>`kline`K线频道                                                                                 |
| &gt; symbol   | String             | 是    | 交易对名称<br/>例如`BTCUSDT`                                                                               |
| &gt; interval | String             | 是    | 时间粒度 <br/> 1m,3m,5m,15m,30m,1H,4H,6H,12H,1D                                                         |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "spot",
    "topic": "kline",
    "symbol": "BTCUSDT",
    "interval": "1D"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数

| 返回字段          | 参数类型   | 字段说明                                                                                                | 
|:--------------|:-------|:----------------------------------------------------------------------------------------------------|
| event         | String | 操作<br/>`subscribe` 订阅 <br/>`unsubscribe` 退订  <br/>`error` 参数错误                                      |
| arg           | Object | 订阅的频道                                                                                               |
| &gt; instType | String | 产品线类型<br/>`spot` 现货交易<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String | 频道名<br/>`kline`K线频道                                                                                 |
| &gt; symbol   | String | 交易对名称<br/>例如`BTCUSDT`                                                                               |
| &gt; interval | String | 时间粒度                                                                                                |
| code          | String | 错误码                                                                                                 |
| msg           | String | 错误消息                                                                                                |
| connId        | String | 连接ID                                                                                                 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
  "data": [
    {
      "volume": "0.423",
      "high": "400005",
      "low": "276670",
      "start": "1710518400000",
      "close": "400005",
      "turnover": "148190.38375",
      "open": "276670"
    }
  ],
  "arg": {
    "instType": "spot",
    "symbol": "BTCUSDT",
    "topic": "kline",
    "interval": "1D"
  },
  "action": "update",
  "ts": 1736370735556
}
```

### 推送数据参数

| 返回字段          | 参数类型               | 字段说明                                                                                                | 
|:--------------|:-------------------|:----------------------------------------------------------------------------------------------------|
| arg           | Object             | 订阅成功频道                                                                                              |
| &gt; instType | String             | 产品线类型<br/>`spot` 现货交易<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String             | 频道名<br/>`kline`K线频道                                                                                 |
| &gt; symbol   | String             | 交易对名称                                                                                               |
| action        | String             | 推送数据动作<br/>`snapshot`全量 <br/> `update` 增量<br/>推送逻辑调整生效后，仅推送 `update`                                                           |
| data          | List&lt;Object&gt; | 订阅的数据                                                                                               |
| &gt; start    | String             | 蜡烛开始时间，Unix时间戳的毫秒数格式，如 1597026383085                                                                |
| &gt; open     | String             | 开盘价格                                                                                                |
| &gt; close    | String             | 收盘价格                                                                                                |
| &gt; high     | String             | 最高价格                                                                                                |
| &gt; low      | String             | 最低价格                                                                                                |
| &gt; volume   | String             | 交易量<br/>_单位为基础币_                                                                                    |
| &gt; turnover | String             | 交易额<br/>_单位为计价币_                                                                                    |

</div>