---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/reality/public/Reality-OrderBook-Segmented-Channel
api_type: WebSocket
updated_at: 2026-11-18 08:37:17.948362
---

# Reality Orderbook Segmented Channel

### Description

Subscribe to real-time segmented depth data of a specified Reality (US stock) trading pair (up to 50 levels). Each price level reports onshore (internal) and offshore (external) quantities separately.

Every push is a full snapshot (`snapshot`). The depth copy is pushed every 500ms when it has changed, or every 10s when unchanged.

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
            "topic": "reality-orderbook-segmented",
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
| &gt; topic    | String | Yes      | Topic <br/> Fixed to `reality-orderbook-segmented`           |
| &gt; symbol   | String | Yes      | Symbol name <br/> e.g., `RAAPLUSDT`                       |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "reality-orderbook-segmented",
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
| &gt; topic    | String | Topic <br/> Fixed to `reality-orderbook-segmented`               |
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
    "topic": "reality-orderbook-segmented",
    "symbol": "RAAPLUSDT"
  },
  "action": "snapshot",
  "ts": 1740000000000,
  "data": {
    "a": [
      ["227.55", "60", "20"],
      ["227.60", "200", "100"]
    ],
    "b": [
      ["227.50", "80", "20"],
      ["227.45", "250", "0"]
    ]
  }
}
```

### Push Parameters

| Return Field   | Parameter Type     | Description                                                              |
|-----------------|--------------------|---------------------------------------------------------------------------|
| arg             | Object             | Subscribed channel                                                        |
| &gt; instType   | String             | Product type <br/> Fixed to `UTA`                                          |
| &gt; topic      | String             | Topic <br/> Fixed to `reality-orderbook-segmented`                             |
| &gt; symbol     | String             | Symbol name                                                                |
| action          | String             | Data push action <br/> `snapshot` Full push                                |
| ts              | String             | Data push timestamp <br/> A Unix timestamp in milliseconds                 |
| data            | Object             | Subscribed data                                                            |
| &gt; a          | List&lt;Array&gt;  | Sell asks. Each item is [price, onshore qty, offshore qty], sorted by price in ascending order |
| &gt; &gt; a[0]   | String             | Sell price                                                                 |
| &gt; &gt; a[1]   | String             | Sell onshore (internal) quantity                                          |
| &gt; &gt; a[2]   | String             | Sell offshore (external) quantity                                         |
| &gt; b          | List&lt;Array&gt;  | Buy bids. Each item is [price, onshore qty, offshore qty], sorted by price in descending order |
| &gt; &gt; b[0]   | String             | Buy price                                                                  |
| &gt; &gt; b[1]   | String             | Buy onshore (internal) quantity                                           |
| &gt; &gt; b[2]   | String             | Buy offshore (external) quantity                                          |

</div>

---

# Reality分层订单簿频道

### 描述

订阅指定 Reality（美股）交易对的实时分层深度数据（最多50档）。每个价位分别返回场内（内部）与场外（外部）数量。

每次推送均为全量快照（`snapshot`）。深度副本有变化则每500ms推送一次，无变化则每10s推送一次。

:::warning{title="接入要求"}

该频道需要 API Key 身份验证，请提前联系您的业务对接人（BD）申请白名单权限。

:::

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "reality-orderbook-segmented",
            "symbol": "RAAPLUSDT"
        }
    ]
}
```

### 请求参数

| 参数名         | 参数类型 | 是否必须 | 描述                                            |
|---------------|--------|--------|---------------------------------------------------|
| op            | String | 是      | 操作 <br/> `subscribe` 订阅 <br/> `unsubscribe` 取消订阅 |
| args          | List&lt;Object&gt; | 是 | 订阅频道                                    |
| &gt; instType | String | 是      | 产品类型 <br/> 固定为 `UTA`                       |
| &gt; topic    | String | 是      | 频道名 <br/> 固定为 `reality-orderbook-segmented`      |
| &gt; symbol   | String | 是      | 交易对名称 <br/> 例如：`RAAPLUSDT`                  |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="响应示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "reality-orderbook-segmented",
    "symbol": "RAAPLUSDT"
  }
}
```

### 响应参数

| 参数名        | 参数类型 | 描述                                              |
|---------------|--------|------------------------------------------------------|
| event         | String | 事件 <br/> `subscribe` 订阅 <br/> `unsubscribe` 取消订阅 <br/> `error` 参数错误 |
| arg           | Object | 订阅频道                                          |
| &gt; instType | String | 产品类型 <br/> 固定为 `UTA`                           |
| &gt; topic    | String | 频道名 <br/> 固定为 `reality-orderbook-segmented`          |
| &gt; symbol   | String | 交易对名称                                           |
| code          | String | 错误码                                              |
| msg           | String | 错误信息                                            |

</div>

<div className="api-br-5"></div>

<div className="api-aligning">

```json title="推送数据"
{
  "arg": {
    "instType": "UTA",
    "topic": "reality-orderbook-segmented",
    "symbol": "RAAPLUSDT"
  },
  "action": "snapshot",
  "ts": 1740000000000,
  "data": {
    "a": [
      ["227.55", "60", "20"],
      ["227.60", "200", "100"]
    ],
    "b": [
      ["227.50", "80", "20"],
      ["227.45", "250", "0"]
    ]
  }
}
```

### 推送参数

| 返回字段       | 参数类型           | 字段说明                                                              |
|-----------------|--------------------|---------------------------------------------------------------------------|
| arg             | Object             | 订阅频道                                                        |
| &gt; instType   | String             | 产品类型 <br/> 固定为 `UTA`                                          |
| &gt; topic      | String             | 频道名 <br/> 固定为 `reality-orderbook-segmented`                             |
| &gt; symbol     | String             | 交易对名称                                                                |
| action          | String             | 推送类型 <br/> `snapshot` 全量推送                                |
| ts              | String             | 推送时间 <br/> Unix毫秒时间戳                 |
| data            | Object             | 订阅的数据                                                            |
| &gt; a          | List&lt;Array&gt;  | 卖方深度，每项为 [价格, 场内数量, 场外数量]，按价格升序排列 |
| &gt; &gt; a[0]   | String             | 卖方价格                                                                 |
| &gt; &gt; a[1]   | String             | 卖方场内（内部）数量                                          |
| &gt; &gt; a[2]   | String             | 卖方场外（外部）数量                                         |
| &gt; b          | List&lt;Array&gt;  | 买方深度，每项为 [价格, 场内数量, 场外数量]，按价格降序排列 |
| &gt; &gt; b[0]   | String             | 买方价格                                                                  |
| &gt; &gt; b[1]   | String             | 买方场内（内部）数量                                           |
| &gt; &gt; b[2]   | String             | 买方场外（外部）数量                                          |

</div>