---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/Position-Tier-Channel
api_type: WebSocket
updated_at: 2026-11-21 19:03:39.699168
---

# Position Tier Channel

### Description

Push position tier changes for a trading pair. When the minimum or maximum value of a position tier changes, this channel pushes a message containing the new tier data. A full snapshot of the current position tiers is pushed immediately after a successful subscription.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "position-tier",
            "symbol": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameters    | Type               | Required | Description                                                                                                        |
|---------------|--------------------|----------|------------------------------------------------------------------------------------------------------------------------|
| op            | String             | Yes      | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe                                              |
| args          | List&lt;Object&gt; | Yes      | Subscribed channel                                                                                                  |
| &gt; instType | String             | Yes      | Product type<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String             | Yes      | Topic <br/> `position-tier` Position tier channel                                                                  |
| &gt; symbol   | String             | Yes      | Trading pair <br/> e.g. `BTCUSDT`                                                                                  |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "position-tier",
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
| &gt; topic    | String | Topic <br/> `position-tier` Position tier channel                                                                  |
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
      "list": [
        {
          "tier": "1",
          "leverage": "125",
          "minTierValue": "0",
          "maxTierValue": "50000",
          "mmr": "0.004"
        },
        {
          "tier": "2",
          "leverage": "100",
          "minTierValue": "50000",
          "maxTierValue": "250000",
          "mmr": "0.005"
        }
      ]
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "topic": "position-tier",
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
| &gt; topic    | String             | Topic <br/> `position-tier` Position tier channel                                                                  |
| &gt; symbol   | String             | Trading pair <br/> e.g. `BTCUSDT`                                                                                  |
| action        | String             | Data push action <br/> `snapshot` Full data <br/> `update` Incremental data                                        |
| data          | List&lt;Object&gt; | Subscribed data                                                                                                     |
| &gt; symbol   | String             | Trading pair name                                                                                                   |
| &gt; list     | List&lt;Object&gt; | Position tier list                                                                                                   |
| &gt;&gt; tier         | String     | Tier                                                                                                                 |
| &gt;&gt; leverage     | String     | Effective leverage                                                                                                   |
| &gt;&gt; minTierValue | String     | Minimum value of the current tier                                                                                   |
| &gt;&gt; maxTierValue | String     | Maximum value of the current tier                                                                                   |
| &gt;&gt; mmr          | String     | Maintenance margin rate <br/> Value corresponding to the position tier. A forced reduction or liquidation is triggered when the position's margin rate falls below this value |

</div>

---

# 仓位档位

### 描述

推送交易对仓位档位的变更。当仓位档位的最大或最小价值发生变化时，本频道会推送含新档位数据的消息。订阅成功后会立即推送一次当前仓位档位的全量快照。

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "position-tier",
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
| &gt; topic    | String             | 是   | 频道名 <br/> `position-tier` 仓位档位频道                                                                             |
| &gt; symbol   | String             | 是   | 交易对名称 <br/> 如 `BTCUSDT`                                                                                         |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "position-tier",
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
| &gt; topic    | String | 频道名 <br/> `position-tier` 仓位档位频道                                                                             |
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
      "list": [
        {
          "tier": "1",
          "leverage": "125",
          "minTierValue": "0",
          "maxTierValue": "50000",
          "mmr": "0.004"
        },
        {
          "tier": "2",
          "leverage": "100",
          "minTierValue": "50000",
          "maxTierValue": "250000",
          "mmr": "0.005"
        }
      ]
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "topic": "position-tier",
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
| &gt; topic    | String             | 频道名 <br/> `position-tier` 仓位档位频道                                                                             |
| &gt; symbol   | String             | 交易对名称 <br/> 如 `BTCUSDT`                                                                                         |
| action        | String             | 推送数据的方式 <br/> `snapshot` 全量 <br/> `update` 增量                                                              |
| data          | List&lt;Object&gt; | 订阅的数据                                                                                                           |
| &gt; symbol   | String             | 交易对名称                                                                                                           |
| &gt; list     | List&lt;Object&gt; | 档位列表                                                                                                             |
| &gt;&gt; tier         | String     | 档位                                                                                                                 |
| &gt;&gt; leverage     | String     | 有效杠杆倍数                                                                                                         |
| &gt;&gt; minTierValue | String     | 当前档位最小价值                                                                                                     |
| &gt;&gt; maxTierValue | String     | 当前档位最大价值                                                                                                     |
| &gt;&gt; mmr          | String     | 维持保证金率 <br/> 持仓档位对应的数值。当仓位的保证金率小于维持保证金率时，将会触发强制减仓或爆仓                      |

</div>