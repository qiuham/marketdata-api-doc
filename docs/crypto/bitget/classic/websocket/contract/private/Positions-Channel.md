---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/private/Positions-Channel
api_type: WebSocket
updated_at: 2026-11-18 08:35:33.284500
---

# Position Channel

### Description

Subscribe the position channel

Data will be pushed when the following events occurred:
1. Open/Close orders are created
2. Open/Close orders are filled
3. Orders are canceled

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "positions",
            "instId": "default"
        }
    ]
}
```

### Request Parameters

| Parameter | Type | Required | Description                                                                                                         | 
| :---- | :---- | :---- |:--------------------------------------------------------------------------------------------------------------------|
| op | String | Yes | Operation, subscribe unsubscribe                                                                                    |
| args | List&lt;Object&gt; | Yes | List of channels to request subscription                                                                            |
| &gt; channel | String | Yes | Channel name: `positions`                                                                                           |
| &gt; instType | String | Yes | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; instId | String | Yes | Symbol name,`default`represents all the symbols，Only default is supported now                                       |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "positions",
        "instId": "default"
    }
}
```

### Response Parameters

| Parameter | Type | Description                                                                                                         | 
| :---- | :---- |:--------------------------------------------------------------------------------------------------------------------|
| event | String | Event                                                                                                               |
| arg | Object | Subscribed channels                                                                                                 |
| &gt; channel | String | Channel name: `positions`                                                                                           |
| &gt; instType | String | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; instId | String | `default`                                                                                                           |
| code | String | Error code                                                                                                          |
| msg | String | Error message                                                                                                       |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
    "action": "snapshot",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "positions",
        "instId": "default"
    },
    "data": [
        {
            "posId": "1",
            "instId": "ETHUSDT",
            "marginCoin": "USDT",
            "marginSize": "9.5",
            "marginMode": "crossed",
            "holdSide": "short",
            "posMode": "hedge_mode",
            "total": "0.1",
            "available": "0.1",
            "frozen": "0",
            "openPriceAvg": "1900",
            "leverage": 20,
            "achievedProfits": "0",
            "unrealizedPL": "0",
            "unrealizedPLR": "0",
            "liquidationPrice": "5788.108475905242",
            "keepMarginRate": "0.005",
            "marginRate": "0.004416374196",
            "cTime": "1695649246169",
            "breakEvenPrice": "24778.97",
            "totalFee": "1.45",
            "deductedFee": "0.388",
            "markPrice": "2500",
            "cashDividend": "0",
            "assetMode": "union",
            "uTime": "1695711602568",            
            "autoMargin": "off"
        }
    ],
    "ts": 1695717430441
}
```

### Push Parameters

| Parameter               | Type | Description                                                                                                                                            | 
|:------------------------| :---- |:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| action                  | String | 'snapshot'                                                                                                                                             |
| arg                     | Object | Channels with successful subscription                                                                                                                  |
| &gt; channel            | String | Channel name: `positions`                                                                                                                              |
| &gt; instType           | String | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures                                     |
| &gt; instId             | String | `default`                                                                                                                                              |
| data                    | List&lt;Object&gt; | Subscription data                                                                                                                                      |
| &gt; posId              | String | Position ID                                                                                                                                            |
| &gt; instId             | String | Product ID,<br/>delivery contract reference：https://www.bitget.com/api-doc/common/release-note                                                         |
| &gt; marginCoin         | String | Currency of occupied margin                                                                                                                            |
| &gt; marginSize         | String | Occupied margin (amount)                                                                                                                               |
| &gt; marginMode         | String | Margin mode                                                                                                                                            |
| &gt; holdSide           | String | Position direction                                                                                                                                     |
| &gt; posMode            | String | Position mode                                                                                                                                          |
| &gt; total              | String | Open position size                                                                                                                                     |
| &gt; available          | String | Size of positions that can be closed                                                                                                                   |
| &gt; frozen             | String | Amount of frozen margin                                                                                                                                |
| &gt; openPriceAvg       | String | Average entry price                                                                                                                                    |
| &gt; leverage           | String | Leverage                                                                                                                                               |
| &gt; achievedProfits    | String | Realized PnL                                                                                                                                           |
| &gt; unrealizedPL       | String | Unrealized PnL                                                                                                                                         |
| &gt; unrealizedPLR      | String | Unrealized ROI                                                                                                                                         |
| &gt; liquidationPrice   | String | Estimated liquidation price                                                                                                                            |
| &gt; keepMarginRate     | String | Maintenance margin rate                                                                                                                                |
| &gt; isolatedMarginRate | String | Actual margin ratio under isolated margin mode                                                                                                         |
| &gt; marginRate         | String | Occupancy rate of margin                                                                                                                               |
| &gt; breakEvenPrice     | String | Position breakeven price                                                                                                                               |
| &gt; totalFee           | String | Funding fee, the accumulated value of funding fee during the position,The initial value is empty, indicating that no funding fee has been charged yet. |
| &gt; deductedFee        | String | Deducted transaction fees: transaction fees deducted during the position                                                                               |
| &gt; markPrice          | String | Mark Price                                                                                                                                             |
| &gt; cashDividend       | String | Cash dividend, unit: USDT                                                                                                                              |
| &gt; assetMode          | String | Account Mode<br/> `union`: Union Margin <br/> `single`: Single Margin                                                                                                                                                                          |
| &gt; cTime              | String | Position creation time, milliseconds format of Unix timestamp, e.g.1597026383085                                                                       |
| &gt; uTime              | String | Lastest position update time, milliseconds format of Unix timestamp, e.g.1597026383085                                                                 |

</div>

---

# 持仓频道

### 描述

订阅仓位频道

以下事件发生时将推送数据：

1. 下开、平仓委托
2. 开、平仓委托成交
3. 撤单

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "positions",
            "instId": "default"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                           | 
| :---- | :---- | :---- |:-----------------------------|
| op | String | 是 | 操作, subscribe unsubscribe    |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表                    |
| &gt; channel | String | 是 | 频道名                          |
| &gt; instType | String | 是 | 产品类型                         |
| &gt; instId | String | 是 | 交易对名称，`default`表示全部交易对，目前只支持`default` |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "positions",
        "instId": "default"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明        | 
| :---- | :---- |:------------|
| event | String | 事件          |
| arg | Object | 订阅的频道       |
| &gt; channel | String | 频道名         |
| &gt; instType | String | 产品类型        |
| &gt; instId | String | `default`   |
| code | String | 错误码，错误时才会返回 |
| msg | String | 错误消息        |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "snapshot",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "positions",
        "instId": "default"
    },
    "data": [
        {
            "posId": "1",
            "instId": "ETHUSDT",
            "marginCoin": "USDT",
            "marginSize": "9.5",
            "marginMode": "crossed",
            "holdSide": "short",
            "posMode": "hedge_mode",
            "total": "0.1",
            "available": "0.1",
            "frozen": "0",
            "openPriceAvg": "1900",
            "leverage": 20,
            "achievedProfits": "0",
            "unrealizedPL": "0",
            "unrealizedPLR": "0",
            "liquidationPrice": "5788.108475905242",
            "keepMarginRate": "0.005",
            "marginRate": "0.004416374196",
            "cTime": "1695649246169",
            "breakEvenPrice": "24778.97",
            "totalFee": "1.45",
            "deductedFee": "0.388",
            "markPrice": "2500",
            "cashDividend": "0",
            "assetMode": "union",
            "uTime": "1695711602568",
            "autoMargin": "off"
        }
    ],
    "ts": 1695717430441
}
```

### 推送数据参数

| 返回字段                    | 参数类型 | 字段说明                                                                              | 
|:------------------------| :---- |:----------------------------------------------------------------------------------|
| action                  | String | 推送动作, 'snapshot'                                                                  |
| arg                     | Object | 订阅成功的频道                                                                           |
| &gt; channel            | String | 频道名                                                                               |
| &gt; instType           | String | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约  |
| &gt; instId             | String | `default`                                                                         |
| data                    | List&lt;Object&gt; | 订阅的数据                                                                             |
| &gt; posId              | String | 持仓ID                                                                              |
| &gt; instId             | String | 产品id，交割合约参考：https://www.bitget.com/zh-CN/api-doc/common/release-note              |
| &gt; marginCoin         | String | 占用保证金的币种                                                                          |
| &gt; marginSize         | String | 占用保证金(数量)                                                                         |
| &gt; marginMode         | String | 保证金模式                                                                             |
| &gt; holdSide           | String | 持仓方向                                                                              |
| &gt; posMode            | String | 持仓模式                                                                              |
| &gt; total              | String | 持仓数量                                                                              |
| &gt; available          | String | 可平仓数量                                                                             |
| &gt; frozen             | String | 冻结数量                                                                              |
| &gt; openPriceAvg       | String | 开仓平均价                                                                             |
| &gt; leverage           | String | 杠杆倍数                                                                              |
| &gt; achievedProfits    | String | 已实现盈亏                                                                             |
| &gt; unrealizedPL       | String | 未实现盈亏                                                                             |
| &gt; unrealizedPLR      | String | 未实现盈亏率                                                                            |
| &gt; liquidationPrice   | String | 预估强平价                                                                             |
| &gt; keepMarginRate     | String | 维持保证金率                                                                            |
| &gt; isolatedMarginRate | String | 逐仓时，实际保证金率                                                                        |
| &gt; marginRate         | String | 保证金占用率                                                                            |
| &gt; breakEvenPrice     | String | 仓位盈亏平衡价                                                                           |
| &gt; totalFee           | String | 资金费用，仓位存续期间，资金费用的累加值 ，初始值为空，表示还没收取过资金费                                            |
| &gt; deductedFee        | String | 已扣手续费，仓位存续期间扣除的交易手续费                                                              |
| &gt; markPrice          | String | 标记价格                                                                              |
| &gt; cashDividend       | String | 现金派息，单位：USDT                                                                      |
| &gt; assetMode          | String | 账户模式<br/>`union`联合保证金<br/>`single`单币种保证金                                                                                                                                           |
| &gt; cTime              | String | 持仓创建时间，Unix时间戳的毫秒数格式，如 1597026383085                                              |
| &gt; uTime              | String | 最近一次持仓更新时间，Unix时间戳的毫秒数格式，如 1597026383085                                          |

</div>