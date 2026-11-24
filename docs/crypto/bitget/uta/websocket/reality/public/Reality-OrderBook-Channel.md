---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/reality/public/Reality-OrderBook-Channel
api_type: WebSocket
updated_at: 2026-11-24 19:01:39.722475
---

# Reality Orderbook Channel

### Description

Subscribe to real-time depth data of a specified Reality (US stock) trading pair.

Every push is a full snapshot (`snapshot`). The depth data returned is raw (unaggregated) depth.

Complete depth data is available during both trading sessions and non-trading sessions. The depth copy is pushed every 500ms when it has changed, or every 10s when unchanged.

This is the merged (onshore + offshore) depth. See also **Reality Orderbook Segmented Channel**, which breaks down onshore and offshore quantities separately.

:::warning{title="Access requirements"}

This channel requires API Key authentication. You must contact your Business Development (BD) representative in advance to apply for whitelist access.

:::

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "reality-orderbook",
            "symbol": "RAAPLUSDT"
        }
    ]
}
```

### Request Parameters

| Parameters    | Type   | Required | Description                                            |
|---------------|--------|----------|----------------------------------------------------------|
| op            | String | Yes      | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe |
| args          | List&lt;Object&gt; | Yes | Subscribed channel                                    |
| &gt; instType | String | Yes      | Product type <br/> Fixed to `UTA`                       |
| &gt; topic    | String | Yes      | Topic <br/> Fixed to `reality-orderbook`                 |
| &gt; symbol   | String | Yes      | Symbol name <br/> e.g., `RAAPLUSDT`                       |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "reality-orderbook",
    "symbol": "RAAPLUSDT"
  }
}
```

### Response Parameters

| Parameters    | Type   | Description                                              |
|---------------|--------|------------------------------------------------------------|
| event         | String | Event <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe <br/> `error` Parameter error |
| arg           | Object | Subscribed channel                                          |
| &gt; instType | String | Product type <br/> Fixed to `UTA`                           |
| &gt; topic    | String | Topic <br/> Fixed to `reality-orderbook`                     |
| &gt; symbol   | String | Symbol name                                                 |
| code          | String | Error code                                                  |
| msg           | String | Error message                                               |

</div>

<div className="api-br-5"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "arg": {
    "instType": "UTA",
    "topic": "reality-orderbook",
    "symbol": "RAAPLUSDT"
  },
  "action": "snapshot",
  "ts": 1740000000000,
  "data": {
    "a": [
      ["227.55", "80"],
      ["227.60", "300"]
    ],
    "b": [
      ["227.50", "100"],
      ["227.45", "250"]
    ]
  }
}
```

### Push Parameters

| Return Field   | Parameter Type     | Description                                                              |
|-----------------|--------------------|---------------------------------------------------------------------------|
| arg             | Object             | Subscribed channel                                                        |
| &gt; instType   | String             | Product type <br/> Fixed to `UTA`                                          |
| &gt; topic      | String             | Topic <br/> Fixed to `reality-orderbook`                                   |
| &gt; symbol     | String             | Symbol name                                                                |
| action          | String             | Data push action <br/> `snapshot` Full push                                |
| ts              | String             | Data push timestamp <br/> A Unix timestamp in milliseconds                 |
| data            | Object             | Subscribed data                                                            |
| &gt; a          | List&lt;Array&gt;  | Sell asks. Each item is [price, size], sorted by price in ascending order  |
| &gt; &gt; a[0]   | String             | Sell price                                                                 |
| &gt; &gt; a[1]   | String             | Sell quantity                                                              |
| &gt; b          | List&lt;Array&gt;  | Buy bids. Each item is [price, size], sorted by price in descending order  |
| &gt; &gt; b[0]   | String             | Buy price                                                                  |
| &gt; &gt; b[1]   | String             | Buy quantity                                                               |

</div>

---

# Reality深度频道

### 描述

订阅 Reality 美股指定交易对的实时深度数据。

每次均推送全量快照（`snapshot`）。该接口返回的深度数据是不合并的原始深度。

交易时段及非交易时段均可获取完整深度数据。深度副本有变化则每500ms推送一次，无变化则每10s推送一次。

该频道为场内+场外的融合深度。另见**Reality分层订单簿频道**，分别返回场内与场外数量。

:::warning{title="接入要求"}

该频道需 API Key 认证，且要提前联系 BD 申请开通白名单权限。

:::

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "reality-orderbook",
            "symbol": "RAAPLUSDT"
        }
    ]
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                          |
|:--------------|:-------------------|:-----|:----------------------------|
| op            | String             | 是    | 操作<br/>`subscribe` 订阅 <br/>`unsubscribe` 退订 |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                    |
| &gt; instType | String             | 是    | 产品线类型<br/>固定传 `UTA`          |
| &gt; topic    | String             | 是    | 频道名<br/>固定传 `reality-orderbook` |
| &gt; symbol   | String             | 是    | 交易对名称<br/>例如`RAAPLUSDT`      |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "reality-orderbook",
    "symbol": "RAAPLUSDT"
  }
}
```

### 返回参数

| 返回字段          | 参数类型   | 字段说明                                          |
|:--------------|:-------|:----------------------------------------------|
| event         | String | 操作<br/>`subscribe` 订阅 <br/>`unsubscribe` 退订  <br/>`error` 参数错误 |
| arg           | Object | 订阅的频道                                          |
| &gt; instType | String | 产品线类型<br/>固定传 `UTA`                            |
| &gt; topic    | String | 频道名<br/>固定传 `reality-orderbook`                |
| &gt; symbol   | String | 交易对名称                                          |
| code          | String | 错误码                                            |
| msg           | String | 错误消息                                           |

</div>

<div className="api-br-5"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
  "arg": {
    "instType": "UTA",
    "topic": "reality-orderbook",
    "symbol": "RAAPLUSDT"
  },
  "action": "snapshot",
  "ts": 1740000000000,
  "data": {
    "a": [
      ["227.55", "80"],
      ["227.60", "300"]
    ],
    "b": [
      ["227.50", "100"],
      ["227.45", "250"]
    ]
  }
}
```

### 推送数据参数

| 返回字段          | 参数类型               | 字段说明                                    |
|:--------------|:-------------------|:----------------------------------------|
| arg           | Object             | 订阅成功的频道                                  |
| &gt; instType | String             | 产品线类型<br/>固定传 `UTA`                      |
| &gt; topic    | String             | 频道名<br/>固定传 `reality-orderbook`          |
| &gt; symbol   | String             | 交易对名称                                    |
| action        | String             | 推送数据动作<br/>`snapshot` 全量                 |
| ts            | String             | 数据推送时间戳，Unix 时间戳的毫秒数格式                   |
| data          | Object             | 订阅的数据                                    |
| &gt; a        | List&lt;Array&gt;  | 卖盘档位，每项为 [price, size]，按价格升序排列          |
| &gt; &gt; a[0] | String             | 卖出价格                                     |
| &gt; &gt; a[1] | String             | 卖出数量                                     |
| &gt; b        | List&lt;Array&gt;  | 买盘档位，每项为 [price, size]，按价格降序排列          |
| &gt; &gt; b[0] | String             | 买入价格                                     |
| &gt; &gt; b[1] | String             | 买入数量                                     |

</div>