---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/Margin-Coins-Channel
api_type: WebSocket
updated_at: 2026-11-21 19:03:36.494132
---

# Margin Coins Channel

### Description

Push changes to margin coin information. This channel pushes when a margin coin's status is enabled/disabled, or when its discount rate tiers change. A full snapshot of the current margin coin information is pushed immediately after a successful subscription.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "uta",
            "topic": "margin-coins",
            "coin": "BTC"
        }
    ]
}
```

### Request Parameters

| Parameters    | Type               | Required | Description                                         |
|---------------|--------------------|----------|------------------------------------------------------|
| op            | String             | Yes      | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe |
| args          | List&lt;Object&gt; | Yes      | Subscribed channel                                  |
| &gt; instType | String             | Yes      | Product type<br/>`uta` Unified Trading Account       |
| &gt; topic    | String             | Yes      | Topic <br/> `margin-coins` Margin coins channel       |
| &gt; coin     | String             | Yes      | Coin name <br/> e.g. `BTC`                           |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "uta",
    "topic": "margin-coins",
    "coin": "BTC"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    | Type   | Description                                      |
|---------------|--------|----------------------------------------------------|
| event         | String | Event                                            |
| arg           | Object | Subscribed channel                               |
| &gt; instType | String | Product type<br/>`uta` Unified Trading Account   |
| &gt; topic    | String | Topic <br/> `margin-coins` Margin coins channel   |
| &gt; coin     | String | Coin name <br/> e.g. `BTC`                       |
| code          | String | Error code                                        |
| msg           | String | Error message                                    |
| connId        | String | Connection ID                                     |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "data": [
    {
      "coin": "BTC",
      "list": [
        {
          "marginCoin": "BTC",
          "discountRateList": [
            {
              "tierStartValue": "0",
              "discountRate": "0.9"
            },
            {
              "tierStartValue": "10000",
              "discountRate": "0.8"
            }
          ],
          "status": "enabled"
        }
      ]
    }
  ],
  "arg": {
    "instType": "uta",
    "topic": "margin-coins",
    "coin": "BTC"
  },
  "action": "snapshot",
  "ts": 1736371332162
}
```

### Push Parameters

| Parameters    | Parameter Type     | Description                                                               |
|---------------|--------------------|-----------------------------------------------------------------------------|
| arg           | Object             | Subscribed successful channel                                              |
| &gt; instType | String             | Product type<br/>`uta` Unified Trading Account                             |
| &gt; topic    | String             | Topic <br/> `margin-coins` Margin coins channel                             |
| &gt; coin     | String             | Coin name <br/> e.g. `BTC`                                                 |
| action        | String             | Data push action <br/> `snapshot` Full data <br/> `update` Incremental data |
| data          | List&lt;Object&gt; | Subscribed data                                                             |
| &gt; coin     | String             | Coin name                                                                   |
| &gt; list     | List&lt;Object&gt; | List                                                                        |
| &gt;&gt; marginCoin | String        | Margin coin                                                                 |
| &gt;&gt; discountRateList | List&lt;Object&gt; | Discount rate list                                                   |
| &gt;&gt;&gt; tierStartValue | String | Tier start value <br/> e.g. `[0, 10000 U)`: `tierStartValue=0` <br/> `[10000 U, 20000 U)`: `tierStartValue=10000` <br/> `[20000 U, ∞)`: `tierStartValue=20000` |
| &gt;&gt;&gt; discountRate | String | Discount rate <br/> Returned as a decimal, e.g. `0.9` represents 90% |
| &gt;&gt; status | String           | Margin coin status <br/> `enabled` Enabled <br/> `disabled` Disabled      |

</div>

---

# 保证金信息

### 描述

推送保证金币种信息的变更。当保证金币种的状态开启/关闭，或折扣率梯度发生变化时，本频道会推送消息。订阅成功后会立即推送一次当前保证金币种信息的全量快照。

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "uta",
            "topic": "margin-coins",
            "coin": "BTC"
        }
    ]
}
```

### 请求参数

| 参数名        | 类型               | 是否必传 | 描述                                                        |
|---------------|--------------------|------|-----------------------------------------------------------------|
| op            | String             | 是   | 操作 <br/> `subscribe` 订阅 <br/> `unsubscribe` 取消订阅        |
| args          | List&lt;Object&gt; | 是   | 请求订阅的频道列表                                              |
| &gt; instType | String             | 是   | 产品线类型<br/>`uta` 统一账户                                   |
| &gt; topic    | String             | 是   | 频道名 <br/> `margin-coins` 保证金信息频道                       |
| &gt; coin     | String             | 是   | 币种名称 <br/> 如 `BTC`                                         |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "uta",
    "topic": "margin-coins",
    "coin": "BTC"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数

| 参数名        | 类型   | 描述                                              |
|---------------|--------|------------------------------------------------------|
| event         | String | 事件                                               |
| arg           | Object | 请求订阅的频道列表                                 |
| &gt; instType | String | 产品线类型<br/>`uta` 统一账户                       |
| &gt; topic    | String | 频道名 <br/> `margin-coins` 保证金信息频道           |
| &gt; coin     | String | 币种名称 <br/> 如 `BTC`                             |
| code          | String | 错误码                                             |
| msg           | String | 错误信息                                           |
| connId        | String | 连接ID                                             |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送数据"
{
  "data": [
    {
      "coin": "BTC",
      "list": [
        {
          "marginCoin": "BTC",
          "discountRateList": [
            {
              "tierStartValue": "0",
              "discountRate": "0.9"
            },
            {
              "tierStartValue": "10000",
              "discountRate": "0.8"
            }
          ],
          "status": "enabled"
        }
      ]
    }
  ],
  "arg": {
    "instType": "uta",
    "topic": "margin-coins",
    "coin": "BTC"
  },
  "action": "snapshot",
  "ts": 1736371332162
}
```

### 推送参数

| 参数名        | 参数类型           | 描述                                                                   |
|---------------|--------------------|---------------------------------------------------------------------------|
| arg           | Object             | 请求订阅成功的频道列表                                                    |
| &gt; instType | String             | 产品线类型<br/>`uta` 统一账户                                             |
| &gt; topic    | String             | 频道名 <br/> `margin-coins` 保证金信息频道                                 |
| &gt; coin     | String             | 币种名称 <br/> 如 `BTC`                                                   |
| action        | String             | 推送数据的方式 <br/> `snapshot` 全量 <br/> `update` 增量                   |
| data          | List&lt;Object&gt; | 订阅的数据                                                               |
| &gt; coin     | String             | 币种名称                                                                 |
| &gt; list     | List&lt;Object&gt; | 列表                                                                     |
| &gt;&gt; marginCoin | String        | 保证金币种                                                               |
| &gt;&gt; discountRateList | List&lt;Object&gt; | 折扣率列表                                                         |
| &gt;&gt;&gt; tierStartValue | String | 档位起始价值 <br/> 例如：`[0, 10000 U)`：`tierStartValue=0` <br/> `[10000 U, 20000 U)`：`tierStartValue=10000` <br/> `[20000 U, ∞)`：`tierStartValue=20000` |
| &gt;&gt;&gt; discountRate | String | 折扣率 <br/> 小数形式返回，如 `0.9` 代表 90%                        |
| &gt;&gt; status | String           | 保证金币种状态 <br/> `enabled` 开启 <br/> `disabled` 关闭                 |

</div>