---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/Margin-Loan-Channel
api_type: WebSocket
updated_at: 2026-11-25 19:02:15.841224
---

# Margin Loan Channel

### Description

Push changes to margin loan parameters for a coin. This channel pushes when the loan limit (per-user or platform), interest-free quota, or interest discount changes, or when the coin's margin loan availability is listed/delisted. A full snapshot of the current loan parameters is pushed immediately after a successful subscription. In addition, a heartbeat push is sent every 60 seconds regardless of whether the above conditions are triggered.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "uta",
            "topic": "margin-loan",
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
| &gt; topic    | String             | Yes      | Topic <br/> `margin-loan` Margin loan channel         |
| &gt; coin     | String             | Yes      | Coin name <br/> e.g. `BTC`                           |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "uta",
    "topic": "margin-loan",
    "coin": "BTC"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    | Type   | Description                                    |
|---------------|--------|--------------------------------------------------|
| event         | String | Event                                          |
| arg           | Object | Subscribed channel                             |
| &gt; instType | String | Product type<br/>`uta` Unified Trading Account |
| &gt; topic    | String | Topic <br/> `margin-loan` Margin loan channel   |
| &gt; coin     | String | Coin name <br/> e.g. `BTC`                     |
| code          | String | Error code                                      |
| msg           | String | Error message                                  |
| connId        | String | Connection ID                                   |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "data": [
    {
      "coin": "BTC",
      "dailyInterest": "0.00008568",
      "annualInterest": "0.03127320",
      "limit": "500",
      "masterSubLimit": "2000",
      "interestFreeLimit": "",
      "platformRemaingQuota": "12000",
      "status": "enabled"
    }
  ],
  "arg": {
    "instType": "uta",
    "topic": "margin-loan",
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
| &gt; topic    | String             | Topic <br/> `margin-loan` Margin loan channel                              |
| &gt; coin     | String             | Coin name <br/> e.g. `BTC`                                                 |
| action        | String             | Data push action <br/> `snapshot` Full data <br/> `update` Incremental data |
| data          | List&lt;Object&gt; | Subscribed data                                                             |
| &gt; coin     | String             | Coin name                                                                   |
| &gt; dailyInterest | String        | Daily interest rate <br/> Returned as a decimal, e.g. `0.01` represents 1% |
| &gt; annualInterest | String       | Annual interest rate <br/> Returned as a decimal, e.g. `0.01` represents 1% |
| &gt; limit    | String             | Single-account loan limit <br/> Unit: the loan coin                        |
| &gt; masterSubLimit | String       | Master/sub-account loan limit <br/> Unit: the loan coin                    |
| &gt; interestFreeLimit | String    | Single-account interest-free limit <br/> Unit: the loan coin <br/> Returns empty if the coin has no interest-free limit |
| &gt; platformRemaingQuota | String | Platform remaining quota <br/> Unit: the loan coin                         |
| &gt; status   | String             | Margin loan coin status <br/> `enabled` Enabled <br/> `disabled` Disabled  |

</div>

---

# 杠杆借币

### 描述

推送币种杠杆借币参数的变更。当借贷限额（个人/平台）、免息额度或利率折扣发生变化，或借贷币种开放/下架状态发生变更时，本频道会推送消息。订阅成功后会立即推送一次当前借贷参数的全量快照。除上述条件触发推送外，本频道每 60 秒推送一次定时快照。

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "uta",
            "topic": "margin-loan",
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
| &gt; topic    | String             | 是   | 频道名 <br/> `margin-loan` 杠杆借币频道                          |
| &gt; coin     | String             | 是   | 币种名称 <br/> 如 `BTC`                                         |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "uta",
    "topic": "margin-loan",
    "coin": "BTC"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数

| 参数名        | 类型   | 描述                                            |
|---------------|--------|----------------------------------------------------|
| event         | String | 事件                                             |
| arg           | Object | 请求订阅的频道列表                               |
| &gt; instType | String | 产品线类型<br/>`uta` 统一账户                     |
| &gt; topic    | String | 频道名 <br/> `margin-loan` 杠杆借币频道            |
| &gt; coin     | String | 币种名称 <br/> 如 `BTC`                           |
| code          | String | 错误码                                           |
| msg           | String | 错误信息                                         |
| connId        | String | 连接ID                                           |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送数据"
{
  "data": [
    {
      "coin": "BTC",
      "dailyInterest": "0.00008568",
      "annualInterest": "0.03127320",
      "limit": "500",
      "masterSubLimit": "2000",
      "interestFreeLimit": "",
      "platformRemaingQuota": "12000",
      "status": "enabled"
    }
  ],
  "arg": {
    "instType": "uta",
    "topic": "margin-loan",
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
| &gt; topic    | String             | 频道名 <br/> `margin-loan` 杠杆借币频道                                    |
| &gt; coin     | String             | 币种名称 <br/> 如 `BTC`                                                   |
| action        | String             | 推送数据的方式 <br/> `snapshot` 全量 <br/> `update` 增量                   |
| data          | List&lt;Object&gt; | 订阅的数据                                                               |
| &gt; coin     | String             | 币种名称                                                                 |
| &gt; dailyInterest | String        | 日利率 <br/> 小数形式返回，如 `0.01` 代表 1%                              |
| &gt; annualInterest | String       | 年利率 <br/> 小数形式返回，如 `0.01` 代表 1%                              |
| &gt; limit    | String             | 单账户限额 <br/> 单位为借贷币种                                           |
| &gt; masterSubLimit | String       | 母子账户限额 <br/> 单位为借贷币种                                         |
| &gt; interestFreeLimit | String    | 单账户免息限额 <br/> 单位为借贷币种 <br/> 如借贷币种没有免息限额，则该字段返回空 |
| &gt; platformRemaingQuota | String | 平台剩余额度 <br/> 单位为借贷币种                                         |
| &gt; status   | String             | 借贷币种状态 <br/> `enabled` 开启 <br/> `disabled` 关闭                   |

</div>