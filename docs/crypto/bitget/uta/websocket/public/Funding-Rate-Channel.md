---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/Funding-Rate-Channel
api_type: WebSocket
updated_at: 2026-11-28 19:00:03.523641
---

# Funding Rate Channel

### Description

Subscribe to the funding rate channel. A full snapshot (current funding rate, next funding rate, upper/lower rate limits, and settlement period) is pushed immediately after a successful subscription.

In addition, this channel pushes:
- When the funding rate settlement period temporarily switches from 8h/4h to 1h, a message containing the new period
- When the settlement period reverts from 1h back to the original period, a message containing the reverted period
- When a cash dividend event occurs
- A heartbeat push every 60 seconds regardless of whether the above conditions are triggered

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "funding-rate",
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
| &gt; topic    | String             | Yes      | Topic <br/> `funding-rate` Funding rate channel                                                                    |
| &gt; symbol   | String             | Yes      | Trading pair <br/> e.g. `BTCUSDT`                                                                                  |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "funding-rate",
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
| &gt; topic    | String | Topic <br/> `funding-rate` Funding rate channel                                                                    |
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
      "fundingRate": "0.000071",
      "fundingRateInterval": "8",
      "nextUpdate": "1743062400000",
      "minFundingRate": "-0.003",
      "maxFundingRate": "0.003",
      "lastFundingRate": "0.000071",
      "nextFundingRate": "0.000088",
      "baseInterestRate": "0.0001",
      "impactMarginNotional": "20000",
      "cashDividend": null,
      "cashDividendNextUpdate": null
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "topic": "funding-rate",
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
| &gt; topic    | String             | Topic <br/> `funding-rate` Funding rate channel                                                                    |
| &gt; symbol   | String             | Trading pair <br/> e.g. `BTCUSDT`                                                                                  |
| action        | String             | Data push action <br/> `snapshot` Full data <br/> `update` Incremental data                                        |
| data          | List&lt;Object&gt; | Subscribed data                                                                                                     |
| &gt; symbol   | String             | Trading pair name, e.g. `BTCUSDT`                                                                                   |
| &gt; fundingRate | String          | [Current funding rate](https://www.bitget.com/trade-info/funding_rate). In decimal form, e.g. `0.000088` represents 0.0088% |
| &gt; fundingRateInterval | String  | Funding rate settlement period, unit: hour <br/> `1` represents 1 hour, `2` represents 2 hours, and so on           |
| &gt; nextUpdate | String           | Next update time of the funding rate <br/> Unix millisecond timestamp                                              |
| &gt; minFundingRate | String       | Lower limit of funding rate <br/> Returned in decimal form, e.g. `0.025` represents 2.5%                           |
| &gt; maxFundingRate | String       | Upper limit of funding rate <br/> Returned in decimal form, e.g. `0.025` represents 2.5%                           |
| &gt; lastFundingRate | String      | Last funding rate <br/> In decimal form, e.g. `0.000088` represents 0.0088%                                        |
| &gt; nextFundingRate | String      | Next funding rate <br/> In decimal form, e.g. `0.000088` represents 0.0088%                                        |
| &gt; baseInterestRate | String     | Base interest rate <br/> In decimal form, e.g. `0.0001` represents 0.01%                                           |
| &gt; impactMarginNotional | String | Impact margin notional <br/> Unit: quote coin                                                                      |
| &gt; cashDividend | String          | Per-share cash dividend, unit: USDT. Only has a value when there is a cash dividend event <br/> Cash dividend paid by RWA stock contracts to eligible holders. For details, refer to [this article](https://www.bitget.com/support/articles/12560603884677) |
| &gt; cashDividendNextUpdate | String | Next update time of the cash dividend. Only has a value when there is a cash dividend event <br/> Unix millisecond timestamp |

</div>

---

# 资金费率

### 描述

订阅资金费率频道。订阅成功后会立即推送一次当前资金费率、下次费率、费率上下限与结算周期的全量快照。

此外，本频道还会在以下情况推送：
- 资金费率结算周期从 8h/4h 临时切换为 1h 时，推送含新周期的消息
- 结算周期从 1h 回调至原周期时，推送含回调后周期的消息
- 产生现金派息数据时
- 除上述条件触发推送外，本频道每 60 秒推送一次定时快照

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "funding-rate",
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
| &gt; topic    | String             | 是   | 频道名 <br/> `funding-rate` 资金费率频道                                                                              |
| &gt; symbol   | String             | 是   | 交易对名称 <br/> 如 `BTCUSDT`                                                                                         |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "funding-rate",
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
| &gt; topic    | String | 频道名 <br/> `funding-rate` 资金费率频道                                                                              |
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
      "fundingRate": "0.000071",
      "fundingRateInterval": "8",
      "nextUpdate": "1743062400000",
      "minFundingRate": "-0.003",
      "maxFundingRate": "0.003",
      "lastFundingRate": "0.000071",
      "nextFundingRate": "0.000088",
      "baseInterestRate": "0.0001",
      "impactMarginNotional": "20000",
      "cashDividend": null,
      "cashDividendNextUpdate": null
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "topic": "funding-rate",
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
| &gt; topic    | String             | 频道名 <br/> `funding-rate` 资金费率频道                                                                              |
| &gt; symbol   | String             | 交易对名称 <br/> 如 `BTCUSDT`                                                                                         |
| action        | String             | 推送数据的方式 <br/> `snapshot` 全量 <br/> `update` 增量                                                              |
| data          | List&lt;Object&gt; | 订阅的数据                                                                                                           |
| &gt; symbol   | String             | 币对名称，例如 `BTCUSDT`                                                                                              |
| &gt; fundingRate | String          | [当前资金费率](https://www.bitget.com/zh-CN/trade-info/funding_rate)。小数形式，`0.000088` 即代表 0.0088%            |
| &gt; fundingRateInterval | String  | 资金费率结算周期，单位为小时 <br/> 数字 `1` 代表 1 小时，`2` 代表 2 小时，以此类推                                      |
| &gt; nextUpdate | String           | 资金费率下次更新时间 <br/> Unix毫秒时间戳                                                                             |
| &gt; minFundingRate | String       | 资金费率下限 <br/> 以小数形式返回，例如 `0.025` 为 2.5%                                                               |
| &gt; maxFundingRate | String       | 资金费率上限 <br/> 以小数形式返回，例如 `0.025` 为 2.5%                                                               |
| &gt; lastFundingRate | String      | 上次资金费率 <br/> 小数形式返回，如 `0.000088` 表示 0.0088%                                                           |
| &gt; nextFundingRate | String      | 下次资金费率 <br/> 小数形式返回，如 `0.000088` 表示 0.0088%                                                           |
| &gt; baseInterestRate | String     | 基础利率 <br/> 小数形式返回，如 `0.0001` 表示 0.01%                                                                   |
| &gt; impactMarginNotional | String | 冲击保证金影响额 <br/> 单位：计价币                                                                                   |
| &gt; cashDividend | String          | 每股现金派息，单位为 USDT，只在有现金派息行为的时候有值 <br/> RWA 股票合约向符合条件的持有人支付的现金分红，具体请参考[这里](https://www.bitget.com/zh-CN/support/articles/12560603884677) |
| &gt; cashDividendNextUpdate | String | 现金派息下次更新时间，只在有现金派息行为的时候有值 <br/> Unix毫秒时间戳                                                 |

</div>