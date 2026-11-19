---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/private/Equity-Channel
api_type: WebSocket
updated_at: 2026-11-19 19:06:35.613613
---

# Equity Channel

### Description

Subscribe equity channel

Data will be pushed when the following events occurred:

1. Transfer balance to Futures account
2. Trading voucher deposit
3. Open/close orders are filled

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "equity"
        }
    ]
}
```

### Request Parameters

| Parameter     | Type               | Required | Description                                                                                                        | 
|:--------------|:-------------------|:---------|:-------------------------------------------------------------------------------------------------------------------|
| op            | String             | Yes      | Operation, subscribe unsubscribe                                                                                   |
| args          | List&lt;Object&gt; | Yes      | List of channels to request subscription                                                                           |
| &gt; instType | String             | Yes      | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures |
| &gt; channel  | String             | Yes      | Channel name                                                                                                       |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "USDT-FUTURES",
    "channel": "equity",
    "instId": "default"
  }
}
```

### Response Parameters

| Parameter     | Type   | Description                                                                                                        | 
|:--------------|:-------|:-------------------------------------------------------------------------------------------------------------------|
| event         | String | Yes<br/>Operation                                                                                                  |
| arg           | Object | Subscribed channels                                                                                                |
| &gt; instType | String | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures |
| &gt; channel  | String | Channel name                                                                                                       |
| &gt; instId   | String | Product ID `default`                                                                                               |
| code          | String | Error code                                                                                                         |
| msg           | String | Error message                                                                                                      |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "action": "snapshot",
  "arg": {
    "instType": "USDT-FUTURES",
    "channel": "equity",
    "instId": "default"
  },
  "data": [
    {
      "btcEquity": "0.0021",
      "usdtEquity": "13.985457617660",
      "usdtUnrealized": "0.000000000000",
      "unionTotalMargin": "100",
      "unionAvailable": "11",
      "unionMm": "11"
    }
  ],
  "ts": 1695717225146
}
```

### Push Parameters

| Parameter            | Type               | Description                                                                                                        |
|:---------------------|:-------------------|:-------------------------------------------------------------------------------------------------------------------|
| action               | String             | action, `snapshot`                                                                                                 |
| arg                  | Object             | Channel                                                                                                            |
| &gt; instType        | String             | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures |
| &gt; channel         | String             | Channel name                                                                                                       |
| &gt; instId          | String             | Product ID `default`                                                                                               |
| data                 | List&lt;Object&gt; | Subscribed data                                                                                                    |
| &gt;usdtEquity       | String             | Account equity (USDT)                                                                                              |
| &gt;btcEquity        | String             | Account equity (BTC)                                                                                               |
| &gt;usdtUnrealized   | String             | Unrealized profit and loss （USDT）                                                                                  |
| &gt;unionTotalMargin | String             | Total multi-asset margin                                                                                           |
| &gt;unionAvailable   | String             | Available balance under multi-asset margin mode                                                                    |
| &gt;unionMm          | String             | Maintenance margin under multi-asset margin mode                                                                   |

</div>

---

# 权益频道

### 描述

订阅权益频道

以下事件发生时推送数据：

1. 划转资金到合约账户
2. 活动金， 或者体验金充值到合约账户
3. 开/平仓委托成交

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "equity"
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

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "USDT-FUTURES",
    "channel": "equity",
    "instId": "default"
  }
}
```

### 返回参数

| 返回字段          | 参数类型   | 字段说明                                                                             | 
|:--------------|:-------|:---------------------------------------------------------------------------------|
| event         | String | 操作                                                                               |
| arg           | Object | 订阅的频道                                                                            |
| &gt; instType | String | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| &gt; channel  | String | 频道名                                                                              |
| &gt; instId   | String | 产品ID `default`                                                                   |
| code          | String | 错误码                                                                              |
| msg           | String | 错误消息                                                                             |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
  "action": "snapshot",
  "arg": {
    "instType": "USDT-FUTURES",
    "channel": "equity",
    "instId":"default"
  },
  "data": [
    {
      "btcEquity": "0.0021",
      "usdtEquity": "13.985457617660",
      "usdtUnrealized": "0.000000000000",
      "unionTotalMargin": "100",
      "unionAvailable": "20",
      "unionMm": "15"
    }
  ],
  "ts": 1695717225146
}
```

### 推送数据参数

| 返回字段                 | 参数类型               | 字段说明                                                                             | 
|:---------------------|:-------------------|:---------------------------------------------------------------------------------|
| action               | String             | 推送动作, `snapshot`                                                                 |
| arg                  | Object             | 请求订阅的频道                                                                          |
| &gt; instType        | String             | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约 |
| &gt; channel         | String             | 频道名                                                                              |
| &gt; instId          | String             | 产品ID `default`                                                                   |
| data                 | List&lt;Object&gt; | 订阅的数据                                                                            |
| &gt;usdtEquity       | String             | 账户权益 (USDT)                                                                      |
| &gt;btcEquity        | String             | 账户权益 (BTC)                                                                       |
| &gt;usdtUnrealized   | String             | 未实现盈亏 (USDT)                                                                     |
| &gt;unionTotalMargin | String             | 联合保证金                                                                            |
| &gt;unionAvailable   | String             | 联合保证金模式下的可用                                                                      |
| &gt;unionMm          | String             | 联合保证金模式下的维持保证金                                                                   |

</div>