---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/private/History-Positions-Channel
api_type: WebSocket
updated_at: 2026-11-24 19:00:33.166405
---

# History Position Channel

Data will be pushed when the position totally closed

### Description

Subscribe the position channel

Data will be pushed when the position totally closed

<div className="api-aligning">

```json title="Request Example"
{
    "args":[
        {
            "channel":"positions-history",
            "instId":"default",
            "instType":"USDT-FUTURES"
        }
    ],
    "op":"subscribe"
}
```

### Request Parameters

| Parameter | Type | Required | Description                                                                                                         | 
| :---- | :---- | :---- |:--------------------------------------------------------------------------------------------------------------------|
| op | String | Yes | subscribe unsubscribe                                                                                               |
| args | List&lt;Object&gt; | Yes | List of channels to request subscription                                                                            |
| &gt; channel | String | Yes | Channel name: `positions-history`                                                                                   |
| &gt; instType | String | Yes | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; instId | String | Yes | Symbol name,`default`represents all the symbols，Only default is supported now                                       |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event":"subscribe",
    "arg":{
        "instType":"USDT-FUTURES",
        "channel":"positions-history",
        "instId":"default"
    }
}
```

### Response Parameters

| Parameter | Type | Description                                                                                                         | 
| :---- | :---- |:--------------------------------------------------------------------------------------------------------------------|
| event | String | Event                                                                                                               |
| arg | Object | Subscribed channels                                                                                                 |
| &gt; channel | String | Channel name: `positions-history`                                                                                   |
| &gt; instType | String | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; instId | String | `default`                                                                                                           |
| code | String | Error code                                                                                                          |
| msg | String | Error message                                                                                                       |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
    "action":"snapshot",
    "arg":{
        "instType":"USDT-FUTURES",
        "channel":"positions-history",
        "instId":"default"
    },
    "data":[
        {
            "posId":"1",
            "instId":"BTCUSDT",
            "marginCoin":"USDT",
            "marginMode":"crossed",
            "holdSide":"short",
            "posMode":"one_way_mode",
            "openPriceAvg":"20000.0",
            "closePriceAvg":"26221.0",
            "openSize":"0.010",
            "closeSize":"0.010",
            "achievedProfits":"-62.21000000",
            "settleFee":"-0.02277989",
            "openFee":"-0.12000000",
            "closeFee":"-0.15732600",
            "cTime":"1696907951177",
            "uTime":"1697090609976"
        }
    ],
    "ts":1697099840122
}
```

### Push Parameters

| Parameter               | Type   | Description                                                                                                         | 
|:------------------------| :----- |:--------------------------------------------------------------------------------------------------------------------|
| action                  | String | 'snapshot'                                                                                                          |
| arg                     | Object | Channels with successful subscription                                                                               |
| &gt; channel            | String | Channel name: `positions-history`                                                                                   |
| &gt; instType           | String | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; instId             | String | `default`                                                                                                           |
| data                    | List&lt;Object&gt; | Subscription data                                                                                                   |
| &gt; posId              | String | Position ID                                                                                                         |
| &gt; instId             | String | Product ID<br/>delivery contract reference：https://www.bitget.com/api-doc/common/release-note                       |
| &gt; marginCoin         | String | Currency of occupied margin                                                                                         |
| &gt; marginMode         | String | Margin mode<br/>`fixed`: isolated mode<br/>`crossed`: crossed mode                                                  |
| &gt; holdSide           | String | Position direction                                                                                                  |
| &gt; posMode            | String | Position mode                                                                                                       |
| &gt; openPriceAvg       | String | Average entry price                                                                                                 |
| &gt; closePriceAvg      | String | Average close price                                                                                                 |
| &gt; openSize           | String | Open size                                                                                                           |
| &gt; closeSize          | String | Close size                                                                                                          |
| &gt; achievedProfits    | String | Realized PnL                                                                                                        |
| &gt; settleFee          | String | Settle fee                                                                                                          |
| &gt; openFee            | String | Total open fee                                                                                                      |
| &gt; closeFee           | String | Total close fee                                                                                                     |                                                                                                                                                             |
| &gt; cTime              | String | Position creation time, milliseconds format of Unix timestamp, e.g.1597026383085                                    |
| &gt; uTime              | String | Lastest position update time, milliseconds format of Unix timestamp, e.g.1597026383085                              |

</div>

---

# 历史持仓频道

推送规则：仓位完全平仓时

### 描述

订阅仓位频道

推送规则：仓位完全平仓时

<div className="api-aligning">

```json title="请求示例"
{
    "args":[
        {
            "channel":"positions-history",
            "instId":"default",
            "instType":"USDT-FUTURES"
        }
    ],
    "op":"subscribe"
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                                                                                | 
| :---- | :---- | :---- |:----------------------------------------------------------------------------------|
| op | String | 是 | 操作, subscribe unsubscribe                                                         |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表                                                                         |
| &gt; channel | String | 是 | 频道名                                                                               |
| &gt; instType | String | 是 | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约  |
| &gt; instId | String | 是 | 交易对名称，`default`表示全部交易对，目前只支持`default`                                             |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event":"subscribe",
    "arg":{
        "instType":"USDT-FUTURES",
        "channel":"positions-history",
        "instId":"default"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明                                                                              | 
| :---- | :---- |:----------------------------------------------------------------------------------|
| event | String | 事件                                                                                |
| arg | Object | 订阅的频道                                                                             |
| &gt; channel | String | 频道名                                                                               |
| &gt; instType | String | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约  |
| &gt; instId | String | `default`                                                                         |
| code | String | 错误码，错误时才会返回                                                                       |
| msg | String | 错误消息                                                                              |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action":"snapshot",
    "arg":{
        "instType":"USDT-FUTURES",
        "channel":"positions-history",
        "instId":"default"
    },
    "data":[
        {
            "posId":"1",
            "instId":"BTCUSDT",
            "marginCoin":"USDT",
            "marginMode":"crossed",
            "holdSide":"short",
            "posMode":"one_way_mode",
            "openPriceAvg":"20000.0",
            "closePriceAvg":"26221.0",
            "openSize":"0.010",
            "closeSize":"0.010",
            "achievedProfits":"-62.21000000",
            "settleFee":"-0.02277989",
            "openFee":"-0.12000000",
            "closeFee":"-0.15732600",
            "cTime":"1696907951177",
            "uTime":"1697090609976"
        }
    ],
    "ts":1697099840122
}
```

### 推送数据参数

| 返回字段                    | 参数类型 | 字段说明                                                                              | 
|:------------------------| :---- |:----------------------------------------------------------------------------------|
| action                  | String | 'snapshot'                                                                        |
| arg                     | Object | 订阅成功的频道                                                                           |
| &gt; channel            | String | 频道名                                                                               |
| &gt; instType           | String | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约  |
| &gt; instId             | String | `default`                                                                         |
| data                    | List&lt;Object&gt; | 订阅的数据                                                                             |
| &gt; posId              | String | 持仓ID                                                                              |
| &gt; instId             | String | 产品id，交割合约参考：https://www.bitget.com/zh-CN/api-doc/common/release-note              |
| &gt; marginCoin         | String | 占用保证金的币种                                                                          |
| &gt; marginMode         | String | 保证金模式<br/>`fixed`: 逐仓<br/>`crossed`: 全仓                                           |
| &gt; holdSide           | String | 持仓方向                                                                              |
| &gt; posMode            | String | 持仓模式                                                                              |
| &gt; openPriceAvg       | String | 开仓平均价                                                                             |
| &gt; closePriceAvg      | String | 平仓平均价                                                                             |
| &gt; openSize           | String | 已开仓量                                                                              |
| &gt; closeSize          | String | 已平仓量                                                                              |
| &gt; achievedProfits    | String | 已实现盈亏                                                                             |
| &gt; settleFee          | String | 资金费用                                                                              |
| &gt; openFee            | String | 仓位开仓总手续费                                                                          |
| &gt; closeFee           | String | 仓位平仓总手续费                                                                          |                                                                                                                                                             |
| &gt; cTime              | String | 持仓创建时间，Unix时间戳的毫秒数格式，如 1597026383085                                              |
| &gt; uTime              | String | 最近一次持仓更新时间，Unix时间戳的毫秒数格式，如 1597026383085                                          |

</div>