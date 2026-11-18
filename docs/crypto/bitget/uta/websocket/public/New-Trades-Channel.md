---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/New-Trades-Channel
api_type: WebSocket
updated_at: 2026-11-18 19:00:54.086232
---

# Public Trades Channel

### Description

To subscribe the public trades channel

During Reality market closed hours, on-exchange trade data can be obtained via this channel; during market open hours, off-exchange trade data is currently available via [Get Reality Fills](/docs/catalog/reality/market-data#get-reality-fills).

:::info{title="Push logic adjustment"}
Effective in **demo trading** on November 4, 2026, and expected in **live trading** on November 17, 2026: after a successful subscription, this channel will no longer push snapshot data (`action`=`snapshot`); only real-time incremental data (`action`=`update`) will be pushed. Before the adjustment takes effect, the first push after subscription is a snapshot of recent data. To obtain historical data, please use the corresponding REST API.
:::

Real-time Push

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "publicTrade",
            "symbol": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameters  |  Type       | Required | Description                                                                                                                                |
|------------------|----------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------|
| op               | String               | Yes      | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe                                                                      |
| args             | List&lt;Object&gt;    | Yes      | Subscribed channel                                                                                                                         |
| &gt; instType    | String               | Yes      | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic       | String               | Yes      | Topic <br/> `publicTrade` Public trade                                                                                                     |
| &gt; [symbol](/docs/catalog/market/market-data#get-instruments)      | String               | Yes      | Symbol name <br/> e.g. `BTCUSDT`                                                                                                           |


</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "publicTrade",
    "symbol": "BTCUSDT"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    | Type   | Description                                                                                                                                |
|---------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------|
| event         | String | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe <br/> `error` Parameter error                                        |
| arg           | Object | Subscribed channel                                                                                                                         |
| &gt; instType | String | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String | Topic <br/> `publicTrade` Public trade channel                                                                                             |
| &gt; symbol   | String | Symbol name                                                                                                                                |
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
      "p": "100000",
      "S": "buy",
      "T": "1736348770627",
      "v": "0.00118",
      "i": "1260903622036942849",
      "L": "1234568787787878787",
      "isRPI": "no"
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "symbol": "BTCUSDT",
    "topic": "publicTrade"
  },
  "action": "update",
  "ts": 1736371104297
}
```

### Push Parameters

| Parameters    | Type               | Description                                                                                                                                |
|---------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| arg           | Object             | Subscribed channel                                                                                                                         |
| &gt; instType | String             | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String             | Topic <br/> `publicTrade`                                                                                                                  |
| &gt; symbol   | String             | Symbol name                                                                                                                                |
| action        | String             | Push data action <br/> `snapshot` Full data <br/> `update` Incremental data<br/>After the push logic adjustment takes effect, only `update` is pushed                                                                |
| data          | List&lt;Object&gt; | Subscribed data                                                                                                                            |
| &gt; i        | String             | Fill execution ID                                                                                                                          |
| &gt; L        | String             | Execution correlation ID                                                                                                                   |
| &gt; p        | String             | Fill price                                                                                                                                 |
| &gt; v        | String             | Fill size <br/>`COIN-Futures`：The unit is **quote coin** <br/>`Others`：The unit is **base coin**<br/>                                      |
| &gt; S        | String             | Fill side <br/> `sell`/`buy`                                                                                                               |
| &gt; T        | String             | Fill timestamp <br/> A Unix timestamp in milliseconds                                                                                      |
| &gt; isRPI    | String             | Whether it is an RPI fill<br/>`yes` Yes<br/>`no` No                                                                                        |


</div>

---

# 平台成交

### 描述

订阅平台成交

在 Reality 休盘期间，场内数据可以通过本频道获取；开盘期间，场外数据请通过 [Get Reality Fills](/zh-CN/docs/catalog/reality/market-data#get-reality-fills) 获取。

:::info{title="推送逻辑调整"}
模拟盘自 2026 年 11 月 4 日起生效，实盘预计 2026 年 11 月 17 日生效：订阅成功后，本频道不再推送快照数据（`action`=`snapshot`），仅推送实时增量数据（`action`=`update`）。调整生效前，订阅后首次推送为最近数据的快照。如需获取历史数据，请使用对应的 REST 接口。
:::

实时推送

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "spot",
            "topic": "publicTrade",
            "symbol": "BTCUSDT"
        }
    ]
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                                                                                                  | 
|:--------------|:-------------------|:-----|:----------------------------------------------------------------------------------------------------|
| op            | String             | 是    | 操作<br/>`subscribe` 订阅 <br/>`unsubscribe` 退订                                                         |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                                           |
| &gt; instType | String             | 是    | 产品线类型<br/>`spot` 现货交易<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String             | 是    | 频道名<br/>`publicTrade`平台成交                                                                           |
| &gt; [symbol](/zh-CN/docs/catalog/market/market-data#get-instruments)   | String             | 是    | 交易对名称<br/>例如`BTCUSDT`                                                                               |


</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "spot",
    "topic": "publicTrade",
    "symbol": "BTCUSDT"
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
| &gt; topic    | String | 频道名<br/>`publicTrade`平台成交频道                                                                         |
| &gt; symbol   | String | 交易对名称                                                                                               |
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
      "p": "100000",
      "S": "buy",
      "T": "1736348770627",
      "v": "0.00118",
      "i": "1260903622036942849",
      "L": "1234568787787878787",
      "isRPI": "no"
    }
  ],
  "arg": {
    "instType": "spot",
    "symbol": "BTCUSDT",
    "topic": "publicTrade"
  },
  "action": "update",
  "ts": 1736371104297
}
```

### 推送数据参数

| 返回字段          | 参数类型               | 字段说明                                                                                                | 
|:--------------|:-------------------|:----------------------------------------------------------------------------------------------------|
| arg           | Object             | 订阅成功频道                                                                                              |
| &gt; instType | String             | 产品线类型<br/>`spot` 现货交易<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String             | 频道名<br/>`publicTrade`平台成交频道                                                                         |
| &gt; symbol   | String             | 交易对名称                                                                                               |
| action        | String             | 推送数据动作<br/>`snapshot`全量 <br/> `update` 增量<br/>推送逻辑调整生效后，仅推送 `update`                                                           |
| data          | List&lt;Object&gt; | 订阅的数据                                                                                               |
| &gt; i        | String             | 成交ID                                                                                                |
| &gt; L        | String             | 成交关联ID                                                                                              |
| &gt; p        | String             | 成交价格                                                                                                |
| &gt; v        | String             | 成交数量<br/>币本位合约：单位为**quote coin**<br/>其他：单位为**base coin**<br/>                                       |
| &gt; S        | String             | 成交方向<br/>`buy`买 <br/> `sell` 卖                                                                      |
| &gt; T        | String             | 成交时间戳                                                                                               |
| &gt; isRPI    | String             | 是否为RPI类型成交<br/>`yes` 是<br/>`no` 否                                                                   |


</div>