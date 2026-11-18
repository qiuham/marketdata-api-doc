---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/reality/public/Reality-Fills-Channel
api_type: WebSocket
updated_at: 2026-11-18 08:37:15.988355
---

# Reality Fills Channel

### Description

Pushes real-time, trade-by-trade rToken fill data, covering both internal fills (matched in the internal order book) and lit market fills (routed to an external broker). Each fill carries the execution venue `execVenue`.

Push rules:
1. Fills are pushed trade by trade as `update`: each new fill is pushed in real time; nothing is pushed when there are no new fills
2. No snapshot of historical fills is pushed after subscription
3. Fills in `data` are sorted by `ts` in descending order

All fills are presented from the taker's perspective.

:::warning{title="Notes"}

- This channel requires API Key authentication, and please contact your BD in advance to apply for whitelist access.
- This channel pushes **platform public fills**, not your own fills. For your own fills, use the private [Fast Fill Channel](/docs/uta/websocket/private/Fast-Fill-Channel).
- The general public trades channel and REST API no longer return fills of Reality (rToken) trading pairs. Please migrate to this channel or [Get Reality Fills](/docs/catalog/reality/market-data#get-reality-fills).

:::

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "reality-fills",
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
| &gt; topic    | String | Yes      | Topic <br/> Fixed to `reality-fills`                     |
| &gt; symbol   | String | Yes      | Symbol name <br/> e.g., `RAAPLUSDT`. Only Reality trading pairs are supported |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "reality-fills",
    "symbol": "RAAPLUSDT"
  }
}
```

### Response Parameters

| Parameters    | Type   | Description                                              |
|---------------|--------|------------------------------------------------------------|
| event         | String | Event <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe <br/> `error` Error |
| arg           | Object | Subscribed channel                                          |
| &gt; instType | String | Product type <br/> Fixed to `UTA`                           |
| &gt; topic    | String | Topic <br/> Fixed to `reality-fills`                         |
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
    "topic": "reality-fills",
    "symbol": "RAAPLUSDT"
  },
  "action": "update",
  "ts": "1762052401056",
  "data": [
    {
      "symbol": "RAAPLUSDT",
      "execId": "1234567893",
      "price": "227.48",
      "size": "10",
      "side": "sell",
      "execVenue": "lit_market",
      "ts": "1762052401050"
    }
  ]
}
```

### Push Parameters

| Return Field   | Parameter Type     | Description                                                              |
|-----------------|--------------------|---------------------------------------------------------------------------|
| arg             | Object             | Subscribed channel                                                        |
| &gt; instType   | String             | Product type <br/> Fixed to `UTA`                                          |
| &gt; topic      | String             | Topic <br/> Fixed to `reality-fills`                                       |
| &gt; symbol     | String             | Symbol name                                                                |
| action          | String             | Data push action <br/> Fixed to `update` Incremental fills |
| ts              | String             | Data push timestamp <br/> A Unix timestamp in milliseconds                 |
| data            | List&lt;Object&gt; | Fill list, sorted by `ts` in descending order                              |
| &gt; symbol     | String             | Symbol name                                                                |
| &gt; execId     | String             | Fill ID <br/> Same as the REST APIs; can be used for de-duplication        |
| &gt; price      | String             | Fill price                                                                 |
| &gt; size       | String             | Fill quantity <br/> Unit: base coin                                        |
| &gt; side       | String             | Taker side <br/> `buy` Taker buy <br/> `sell` Taker sell                   |
| &gt; execVenue  | String             | Execution venue <br/> `internal_market` Internal fill: matched in the internal order book <br/> `lit_market` Lit market fill: routed to an external broker and executed on the public market <br/> Note: `execVenue` is where the fill actually took place, which differs from the `venue` order parameter |
| &gt; ts         | String             | Fill time <br/> A Unix timestamp in milliseconds                           |

</div>

---

# Reality公共成交频道

### 描述

实时逐笔推送 rtoken 成交数据，包括内部成交（在内部订单簿成交）与公开市场成交（路由到外部券商成交），每笔成交带成交发生地标识 `execVenue`。

推送规则：
1. 推送模式为逐笔推送 `update`：每产生一笔新成交即实时推送；无成交时不推送
2. 订阅成功后不推送历史成交快照
3. `data` 内成交按 `ts` 倒序排列

成交统一为 taker（主动方）视角。

:::warning{title="注意事项"}

- 该频道需 API Key 认证，且要提前联系 BD 申请开通白名单权限。
- 本频道推送的是**平台公共成交**，不是个人成交；个人成交请使用私有 [快速成交](/zh-CN/docs/uta/websocket/private/Fast-Fill-Channel) 频道。
- 通用公共成交频道与 REST 接口不再返回 Reality（rToken）交易对的成交数据，请迁移至本频道或 [获取Reality平台成交数据](/zh-CN/docs/catalog/reality/market-data#get-reality-fills) 接口。

:::

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "reality-fills",
            "symbol": "RAAPLUSDT"
        }
    ]
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                          |
|---------------|--------------------|------|-----------------------------|
| op            | String             | 是    | 操作 <br/> `subscribe` 订阅 <br/> `unsubscribe` 取消订阅 |
| args          | List&lt;Object&gt; | 是    | 订阅的频道列表                     |
| &gt; instType | String             | 是    | 产品类型 <br/> 固定 `UTA`         |
| &gt; topic    | String             | 是    | 频道名 <br/> 固定 `reality-fills` |
| &gt; symbol   | String             | 是    | 交易对 <br/> 如 `RAAPLUSDT`，仅支持 Reality 交易对 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅响应示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "reality-fills",
    "symbol": "RAAPLUSDT"
  }
}
```

### 返回参数

| 返回字段          | 参数类型   | 字段说明                        |
|---------------|--------|-----------------------------|
| event         | String | 事件 <br/> `subscribe` 订阅成功 <br/> `unsubscribe` 取消订阅成功 <br/> `error` 操作失败 |
| arg           | Object | 订阅的频道                       |
| &gt; instType | String | 产品类型 <br/> 固定 `UTA`         |
| &gt; topic    | String | 频道名 <br/> 固定 `reality-fills` |
| &gt; symbol   | String | 交易对                         |
| code          | String | 错误码                         |
| msg           | String | 错误信息                        |

</div>

<div className="api-br-5"></div>

<div className="api-aligning">

```json title="推送示例"
{
  "arg": {
    "instType": "UTA",
    "topic": "reality-fills",
    "symbol": "RAAPLUSDT"
  },
  "action": "update",
  "ts": "1762052401056",
  "data": [
    {
      "symbol": "RAAPLUSDT",
      "execId": "1234567893",
      "price": "227.48",
      "size": "10",
      "side": "sell",
      "execVenue": "lit_market",
      "ts": "1762052401050"
    }
  ]
}
```

### 推送参数

| 返回字段           | 参数类型               | 字段说明                                    |
|----------------|--------------------|-----------------------------------------|
| arg            | Object             | 订阅的频道                                   |
| &gt; instType  | String             | 产品类型 <br/> 固定 `UTA`                     |
| &gt; topic     | String             | 频道名 <br/> 固定 `reality-fills`             |
| &gt; symbol    | String             | 交易对                                     |
| action         | String             | 推送类型 <br/> 固定 `update` 增量成交 |
| ts             | String             | 推送时间 <br/> Unix 毫秒时间戳                   |
| data           | List&lt;Object&gt; | 成交列表，按 `ts` 倒序                          |
| &gt; symbol    | String             | 交易对                                     |
| &gt; execId    | String             | 成交 ID <br/> 与 REST 接口一致，可用于去重           |
| &gt; price     | String             | 成交价格                                    |
| &gt; size      | String             | 成交数量 <br/> 单位为 base coin               |
| &gt; side      | String             | 交易方向（taker 视角） <br/> `buy` 主动买入 <br/> `sell` 主动卖出 |
| &gt; execVenue | String             | 成交发生地 <br/> `internal_market` 内部成交：在内部订单簿成交 <br/> `lit_market` 公开市场成交：路由到外部券商，在公开市场成交 <br/> 注：`execVenue` 为实际成交地，不同于下单参数 `venue` |
| &gt; ts        | String             | 成交时间 <br/> Unix 毫秒时间戳                   |

</div>