---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/private/Account-Channel
api_type: WebSocket
updated_at: 2026-11-25 19:01:21.344538
---

# Account channel

### Description

Subscribe account channel

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
            "channel": "account",
            "coin": "default"
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
| &gt; coin     | String             | Yes      | Coin name，`default` represents all the coins，Only default is supported now                                         |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "USDT-FUTURES",
    "channel": "account",
    "coin": "default"
  }
}
```

### Response Parameters

| Parameter     | Type   | Description                                                                                                                                                   | 
|:--------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| event         | String | Yes<br/>Operation                                                                                                                                             |
| arg           | Object | Subscribed channels                                                                                                                                           |
| &gt; instType | String | Product type<br/>`USDT-FUTURES` USDT professional futures<br/>`COIN-FUTURES` Futures settled in cryptocurrencies<br/>`USDC-FUTURES` USDC professional futures |
| &gt; channel  | String | Channel name                                                                                                                                                  |
| &gt; coin     | String | `default`                                                                                                                                                     |
| code          | String | Error code                                                                                                                                                    |
| msg           | String | Error message                                                                                                                                                 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "action": "snapshot",
  "arg": {
    "instType": "USDT-FUTURES",
    "channel": "account",
    "coin": "default"
  },
  "data": [
    {
      "marginCoin": "USDT",
      "frozen": "0.00000000",
      "available": "11.98545761",
      "maxOpenPosAvailable": "11.98545761",
      "maxTransferOut": "11.98545761",
      "equity": "11.98545761",
      "usdtEquity": "11.985457617660",
      "crossedRiskRate": "0",
      "unrealizedPL": "0.000000000000",
      "unionTotalMargin": "100",
      "unionAvailable": "20",
      "unionMm": "15",
      "assetsMode": "union"
    }
  ],
  "ts": 1695717225146
}
```

### Push Parameters

| Parameter               | Type               | Description                                                                                                                                                   | 
|:------------------------|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| action                  | String             | `snapshot`                                                                                                                                                    |
| arg                     | Object             | Channels to request subscription                                                                                                                              |
| &gt; instType           | String             | Product type<br/>`USDT-FUTURES` USDT professional futures<br/>`COIN-FUTURES` Futures settled in cryptocurrencies<br/>`USDC-FUTURES` USDC professional futures |
| &gt; channel            | String             | Channel name                                                                                                                                                  |
| &gt; coin               | String             | `default`                                                                                                                                                     |
| data                    | List&lt;Object&gt; | Subscription data                                                                                                                                             |
| &gt;marginCoin          | String             | Margin coin                                                                                                                                                   |
| &gt;frozen              | String             | Locked quantity (margin coin)                                                                                                                                 |
| &gt;available           | String             | Currently available assets                                                                                                                                    |
| &gt;maxOpenPosAvailable | String             | Maximum available balance to open positions                                                                                                                   |
| &gt;maxTransferOut      | String             | Maximum transferable amount                                                                                                                                   |
| &gt;equity              | String             | Account assets                                                                                                                                                |
| &gt;usdtEquity          | String             | Account equity in USD                                                                                                                                         |
| &gt;crossedRiskRate     | String             | Risk ratio in cross margin mode                                                                                                                               |
| &gt;unrealizedPL        | String             | Unrealized PnL                                                                                                                                                |
| &gt;unionTotalMargin    | String             | Margin Amount under Union Margin Mode                                                                                                                         |
| &gt;unionAvailable      | String             | Available Balance under Union Margin Mode                                                                                                                     |
| &gt;unionMm             | String             | Maintenance Margin under Union Margin Mode                                                                                                                    |
| &gt;assetsMode          | String             | Account Mode<br/>`union`Unified Margin<br/>`single`Single-Currency Margin                                                                                     |

</div>

---

# 账户频道

### 描述

订阅账户频道

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
            "channel": "account",
            "coin": "default"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                                                                                | 
| :---- | :---- | :---- |:----------------------------------------------------------------------------------|
| op | String | 是 | 操作, subscribe unsubscribe                                                         |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表                                                                         |
| &gt; instType | String | 是 | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约  |
| &gt; channel | String | 是 | 频道名                                                                               |
| &gt; coin | String | 是 | 币种名称，`default`表示全部币种，目前只支持`default`                                               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "account",
        "coin": "default"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明                                                                              | 
| :---- | :---- |:----------------------------------------------------------------------------------|
| event | String | 操作                                                                                |
| arg | Object | 订阅的频道                                                                             |
| &gt; instType | String | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约  |
| &gt; channel | String | 频道名                                                                               |
| &gt; coin | String | `default`                                                                         |
| code | String | 错误码                                                                               |
| msg | String | 错误消息                                                                              |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "snapshot",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "account",
        "coin": "default"
    },
    "data": [
      {
        "marginCoin": "USDT",
        "frozen": "0.00000000",
        "available": "13.98545761",
        "maxOpenPosAvailable": "13.98545761",
        "maxTransferOut": "13.98545761",
        "equity": "13.98545761",
        "usdtEquity": "13.985457617660",
        "crossedRiskRate": "0",
        "unrealizedPL": "0.000000000000",
        "unionTotalMargin": "100",
        "unionAvailable": "20",
        "unionMm": "15",
        "assetsMode": "union"
      }
    ],
    "ts": 1695717225146
}
```

### 推送数据参数

| 返回字段 | 参数类型 | 字段说明                                                                              | 
| :---- | :---- |:----------------------------------------------------------------------------------|
| action | String | 推送动作, `snapshot`                                                                  |
| arg | Object | 请求订阅的频道                                                                           |
| &gt; instType | String | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约  |
| &gt; channel | String | 频道名                                                                               |
| &gt; coin | String | `default`                                                                         |
| data | List&lt;Object&gt; | 订阅的数据                                                                             |
| &gt;marginCoin | String             | 保证金币种                                                                             |
| &gt;frozen     | String             | 锁定数量(保证金币种)                                                                       |
| &gt;available | String             | 当前可用资产                                                                            |
| &gt;maxOpenPosAvailable | String             | 最大可用开仓余额                                                                          |
| &gt;maxTransferOut | String             | 最大可转出                                                                             |
| &gt;equity | String             | 账户权益                                                                              |
| &gt;usdtEquity | String             | 账户权益美金价值                                                                          |
| &gt;crossedRiskRate | String             | 全仓时风险率                                                                            |
| &gt;unrealizedPL | String             | 未实现盈亏                                                                             |
| &gt;unionTotalMargin | String             | 联合保证金模式下的保证金金额                                                                                                                                                           |
| &gt;unionAvailable | String             | 联合保证金模式下的可用                                                                                                                                                              |
| &gt;unionMm | String             | 联合保证金模式下的维持保证金                                                                                                                                                           |
| &gt;assetsMode | String             | 账户模式<br/>`union`联合保证金<br/>`single`单币种保证金                                                                                                                                           |

</div>