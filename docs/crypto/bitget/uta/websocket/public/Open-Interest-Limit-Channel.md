---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/Open-Interest-Limit-Channel
api_type: WebSocket
updated_at: 2026-11-18 19:00:54.842585
---

# Open Interest Limit Channel

### Description

Push changes to the single-user open interest (OI) limit for a trading pair. When the OI limit quota changes, this channel pushes a message containing the new values. A full snapshot of the current limit is pushed immediately after a successful subscription.

For stock contracts, the OI limit differs from crypto contracts: the single-UID limit can be up to 20%, and the single-user (master + sub-accounts) limit can be up to 40%.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "open-interest-limit",
            "symbol": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameters    | Type               | Required | Description                                                                                                        |
|---------------|--------------------|----------|----------------------------------------------------------------------------------------------------------------------|
| op            | String             | Yes      | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe                                              |
| args          | List&lt;Object&gt; | Yes      | Subscribed channel                                                                                                  |
| &gt; instType | String             | Yes      | Product type<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String             | Yes      | Topic <br/> `open-interest-limit` Open interest limit channel                                                      |
| &gt; symbol   | String             | Yes      | Trading pair <br/> e.g. `BTCUSDT`                                                                                  |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "open-interest-limit",
    "symbol": "BTCUSDT"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    | Type   | Description                                                                                                        |
|---------------|--------|------------------------------------------------------------------------------------------------------------------------|
| event         | String | Event                                                                                                                |
| arg           | Object | Subscribed channel                                                                                                  |
| &gt; instType | String | Product type<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String | Topic <br/> `open-interest-limit` Open interest limit channel                                                      |
| &gt; symbol   | String | Trading pair <br/> e.g. `BTCUSDT`                                                                                  |
| code          | String | Error code                                                                                                           |
| msg           | String | Error message                                                                                                       |
| connId        | String | Connection ID                                                                                                        |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "data": [
    {
      "symbol": "BTCUSDT",
      "notionalValue": "1000000",
      "singlePositionRatio": "0.1",
      "totalNotionalValue": "5000000",
      "totalPositionRatio": "0.2"
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "topic": "open-interest-limit",
    "symbol": "BTCUSDT"
  },
  "action": "snapshot",
  "ts": 1736371332162
}
```

### Push Parameters

| Parameters    | Parameter Type     | Description                                                                                                        |
|---------------|--------------------|------------------------------------------------------------------------------------------------------------------------|
| arg           | Object             | Subscribed successful channel                                                                                       |
| &gt; instType | String             | Product type<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String             | Topic <br/> `open-interest-limit` Open interest limit channel                                                      |
| &gt; symbol   | String             | Trading pair <br/> e.g. `BTCUSDT`                                                                                  |
| action        | String             | Data push action <br/> `snapshot` Full data <br/> `update` Incremental data                                        |
| data          | List&lt;Object&gt; | Subscribed data                                                                                                     |
| &gt; symbol   | String             | Trading pair name, pushed on change                                                                                |
| &gt; notionalValue | String       | Individual user position notional value, pushed on change                                                          |
| &gt; singlePositionRatio | String | Single UID contract position ratio, pushed on change <br/> Returned as a decimal, e.g. `0.1` represents 10%  |
| &gt; totalNotionalValue | String  | Master/sub-account position notional value, pushed on change                                                      |
| &gt; totalPositionRatio | String  | Master/sub-account contract position ratio, pushed on change <br/> Returned as a decimal, e.g. `0.1` represents 10% |

</div>

---

# OI限仓

### 描述

推送交易对单用户持仓限额（OI 限仓）的变更。限仓额度发生变更时，本频道会推送含新值的消息。订阅成功后会立即推送一次当前限额的全量快照。

股票合约的 OI 限仓与 crypto 合约不同：单 UID 最高支持到 20%，单用户（主账户+子账户）最高支持到 40%。

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "open-interest-limit",
            "symbol": "BTCUSDT"
        }
    ]
}
```

### 请求参数

| 参数名        | 类型               | 是否必传 | 描述                                                                                                                 |
|---------------|--------------------|------|------------------------------------------------------------------------------------------------------------------------|
| op            | String             | 是   | 操作 <br/> `subscribe` 订阅 <br/> `unsubscribe` 取消订阅                                                              |
| args          | List&lt;Object&gt; | 是   | 请求订阅的频道列表                                                                                                     |
| &gt; instType | String             | 是   | 产品线类型<br/>`usdt-futures` USDT合约 <br/> `coin-futures` 币本位合约 <br/> `usdc-futures` USDC合约                  |
| &gt; topic    | String             | 是   | 频道名 <br/> `open-interest-limit` 合约OI限仓频道                                                                     |
| &gt; symbol   | String             | 是   | 交易对名称 <br/> 如 `BTCUSDT`                                                                                         |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "open-interest-limit",
    "symbol": "BTCUSDT"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数

| 参数名        | 类型   | 描述                                                                                                                 |
|---------------|--------|------------------------------------------------------------------------------------------------------------------------|
| event         | String | 事件                                                                                                                 |
| arg           | Object | 请求订阅的频道列表                                                                                                   |
| &gt; instType | String | 产品线类型<br/>`usdt-futures` USDT合约 <br/> `coin-futures` 币本位合约 <br/> `usdc-futures` USDC合约                  |
| &gt; topic    | String | 频道名 <br/> `open-interest-limit` 合约OI限仓频道                                                                     |
| &gt; symbol   | String | 交易对名称 <br/> 如 `BTCUSDT`                                                                                         |
| code          | String | 错误码                                                                                                               |
| msg           | String | 错误信息                                                                                                             |
| connId        | String | 连接ID                                                                                                               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送数据"
{
  "data": [
    {
      "symbol": "BTCUSDT",
      "notionalValue": "1000000",
      "singlePositionRatio": "0.1",
      "totalNotionalValue": "5000000",
      "totalPositionRatio": "0.2"
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "topic": "open-interest-limit",
    "symbol": "BTCUSDT"
  },
  "action": "snapshot",
  "ts": 1736371332162
}
```

### 推送参数

| 参数名        | 参数类型           | 描述                                                                                                                 |
|---------------|--------------------|------------------------------------------------------------------------------------------------------------------------|
| arg           | Object             | 请求订阅成功的频道列表                                                                                                 |
| &gt; instType | String             | 产品线类型<br/>`usdt-futures` USDT合约 <br/> `coin-futures` 币本位合约 <br/> `usdc-futures` USDC合约                  |
| &gt; topic    | String             | 频道名 <br/> `open-interest-limit` 合约OI限仓频道                                                                     |
| &gt; symbol   | String             | 交易对名称 <br/> 如 `BTCUSDT`                                                                                         |
| action        | String             | 推送数据的方式 <br/> `snapshot` 全量 <br/> `update` 增量                                                              |
| data          | List&lt;Object&gt; | 订阅的数据                                                                                                           |
| &gt; symbol   | String             | 交易对名称，变化后推送                                                                                               |
| &gt; notionalValue | String       | 单用户持仓名义价值，变化后推送                                                                                       |
| &gt; singlePositionRatio | String | 单 UID 合约持仓占比，变化后推送 <br/> 小数形式返回，如 `0.1` 代表 10%                                                  |
| &gt; totalNotionalValue | String  | 子母账户持仓名义价值，变化后推送                                                                                     |
| &gt; totalPositionRatio | String  | 子母账户合约持仓占比，变化后推送 <br/> 小数形式返回，如 `0.1` 代表 10%                                                  |

</div>