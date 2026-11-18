---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/Instruments-Channel
api_type: WebSocket
updated_at: 2026-11-18 08:37:05.022640
---

# Instruments Channel

### Description

Push trading parameter and trading pair status changes for a product. When trading parameters change (e.g. limit price ratio, price protection, order price/quantity precision, etc.) or the trading pair status changes (e.g. listed, online, maintenance, etc.), this channel pushes a message containing the new values.

After subscribing, messages are pushed only when trading parameters change. It is recommended to first fetch the full information via REST, then subscribe to this channel to receive subsequent changes.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "instruments"
        }
    ]
}
```

### Request Parameters

| Parameters    | Type               | Required | Description                                                                                                                                |
|---------------|--------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| op            | String             | Yes      | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe                                                                      |
| args          | List&lt;Object&gt; | Yes      | Subscribed channel                                                                                                                         |
| &gt; instType | String             | Yes      | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String             | Yes      | Topic <br/> `instruments` Instruments channel                                                                                              |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "instruments"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    | Type   | Description                                                                                                                                |
|---------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------|
| event         | String | Event                                                                                                                                      |
| arg           | Object | Subscribed channel                                                                                                                         |
| &gt; instType | String | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String | Topic <br/> `instruments` Instruments channel                                                                                              |
| code          | String | Error code                                                                                                                                 |
| msg           | String | Error message                                                                                                                              |
| connId        | String | Connection ID                                                                                                                              |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Push Data"
{
  "data": [
    {
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "buyLimitPriceRatio": "0.05",
      "sellLimitPriceRatio": "0.05",
      "marketPriceRatio": "0.05",
      "priceProtectThreshold": "0.1",
      "feeRateUpRatio": "0.01",
      "openCostUpRatio": "0.01",
      "minOrderQty": "0.001",
      "maxOrderQty": "1000",
      "minOrderAmount": "5",
      "maxMarketOrderQty": "500",
      "pricePrecision": "2",
      "quantityPrecision": "3",
      "quotePrecision": "4",
      "priceMultiplier": "0.01",
      "quantityMultiplier": "0.001",
      "type": "perpetual",
      "status": "online",
      "openTime": "1700000000000",
      "offTime": "",
      "limitOpenTime": ""
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "topic": "instruments"
  },
  "action": "snapshot",
  "ts": 1736371332162
}
```

### Push Parameters

| Parameters    | Parameter Type     | Description                                                                                                                                |
|---------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| arg           | Object             | Subscribed channel                                                                                                                         |
| &gt; instType | String             | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String             | Topic <br/> `instruments` Instruments channel                                                                                              |
| action        | String             | Data push action <br/> `snapshot` Full data <br/> `update` Incremental data                                                                 |
| data          | List&lt;Object&gt; | Subscribed data                                                                                                                            |
| &gt; baseCoin | String             | Base coin <br/> e.g. `BTC` in `BTCUSDT`                                                                                                   |
| &gt; quoteCoin | String            | Quote coin <br/> e.g. `USDT` in `BTCUSDT`                                                                                                  |
| &gt; buyLimitPriceRatio | String  | Buy limit price ratio <br/> The ratio of the buy limit price to the market price, determining the highest allowed price for a buy order  |
| &gt; sellLimitPriceRatio | String | Sell limit price ratio <br/> The ratio of the sell limit price to the market price, determining the lowest allowed price for a sell order |
| &gt; marketPriceRatio | String     | Market order price ratio <br/> The ratio of the buy/sell market order price to the market price, determining the price range for market orders |
| &gt; priceProtectThreshold | String | Take-profit/stop-loss price protection threshold <br/> The maximum allowed deviation between the TP/SL trigger price and the latest/mark price <br/> Returned in decimal form, e.g. `0.1` represents 10% |
| &gt; feeRateUpRatio | String       | Fee rate markup ratio <br/> The percentage increase of the actual fee relative to the base fee                                           |
| &gt; openCostUpRatio | String      | Opening cost markup ratio <br/> The percentage increase of the position opening cost relative to the base/standard cost                  |
| &gt; minOrderQty | String          | Minimum limit order quantity <br/> The minimum order quantity allowed, denominated in the base coin                                      |
| &gt; maxOrderQty | String          | Maximum limit order quantity <br/> The maximum order quantity allowed, denominated in the base coin <br/> `0` means no limit              |
| &gt; minOrderAmount | String       | Minimum limit order amount <br/> The minimum order amount allowed, denominated in the quote coin                                         |
| &gt; maxMarketOrderQty | String    | Maximum market order quantity <br/> The maximum order quantity allowed for market orders, denominated in the base coin                   |
| &gt; pricePrecision | String       | Price precision <br/> The number of decimal places allowed for price <br/> The order price must be an integer multiple of the price precision |
| &gt; quantityPrecision | String     | Quantity precision <br/> The number of decimal places allowed for quantity <br/> The order quantity must be an integer multiple of the quantity precision |
| &gt; quotePrecision | String       | Quote order precision <br/> The number of decimal places allowed for the quote coin price                                               |
| &gt; priceMultiplier | String      | Price multiplier <br/> Used together with `pricePrecision`. For example, if `pricePrecision=2` and `priceMultiplier=0.01`, the order price must be a multiple of `priceMultiplier` with 2 decimal places |
| &gt; quantityMultiplier | String   | Quantity multiplier <br/> Used for futures orders together with `quantityPrecision`. For example, if `quantityPrecision=2` and `quantityMultiplier=0.01`, the order quantity must be a multiple of `quantityMultiplier` with 2 decimal places |
| &gt; type       | String          | Contract type <br/> `perpetual` Perpetual <br/> `delivery` Delivery                                                                       |
| &gt; status     | String          | Trading pair status <br/> `listed` Listed (not yet open) <br/> `online` Trading normally/open <br/> `limit_open` Opening disabled <br/> `limit_close` Closing disabled for futures, trading halted for spot <br/> `offline` Delisted/under maintenance |
| &gt; openTime   | String          | Opening time <br/> Unix millisecond timestamp                                                                                             |
| &gt; offTime    | String          | Trading halt time <br/> Returns `""` when not configured <br/> Futures only                                                              |
| &gt; limitOpenTime | String       | Opening restriction time <br/> A non-empty value indicates the symbol is or will be under maintenance, and trading will be disabled after this time <br/> Returns `""` when not configured |

</div>

---

# 产品信息

### 描述

推送交易对的交易参数与状态变更。当交易参数发生变化（如限价比例、价差保护、下单价格/数量精度等）或交易对状态发生变化（如上线、下线、维护等）时，本频道会推送含新值的消息。

订阅后，交易参数变化后推送，建议用户先通过REST获取全量信息后订阅该频道接收变化信息；

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "usdt-futures",
            "topic": "instruments"
        }
    ]
}
```

### 请求参数

| 参数名        | 类型               | 是否必传 | 描述                                                                                                                 |
|---------------|--------------------|------|----------------------------------------------------------------------------------------------------------------------|
| op            | String             | 是   | 操作 <br/> `subscribe` 订阅 <br/> `unsubscribe` 取消订阅                                                              |
| args          | List&lt;Object&gt; | 是   | 请求订阅的频道列表                                                                                                     |
| &gt; instType | String             | 是   | 产品线类型<br/>`spot` 现货交易<br/>`usdt-futures` USDT合约 <br/> `coin-futures` 币本位合约 <br/> `usdc-futures` USDC合约 |
| &gt; topic    | String             | 是   | 频道名 <br/> `instruments` 产品信息频道                                                                               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "usdt-futures",
    "topic": "instruments"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数

| 参数名        | 类型   | 描述                                                                                                                 |
|---------------|--------|------------------------------------------------------------------------------------------------------------------------|
| event         | String | 事件                                                                                                                 |
| arg           | Object | 请求订阅的频道列表                                                                                                   |
| &gt; instType | String | 产品线类型<br/>`spot` 现货交易<br/>`usdt-futures` USDT合约 <br/> `coin-futures` 币本位合约 <br/> `usdc-futures` USDC合约 |
| &gt; topic    | String | 频道名 <br/> `instruments` 产品信息频道                                                                               |
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
      "baseCoin": "BTC",
      "quoteCoin": "USDT",
      "buyLimitPriceRatio": "0.05",
      "sellLimitPriceRatio": "0.05",
      "marketPriceRatio": "0.05",
      "priceProtectThreshold": "0.1",
      "feeRateUpRatio": "0.01",
      "openCostUpRatio": "0.01",
      "minOrderQty": "0.001",
      "maxOrderQty": "1000",
      "minOrderAmount": "5",
      "maxMarketOrderQty": "500",
      "pricePrecision": "2",
      "quantityPrecision": "3",
      "quotePrecision": "4",
      "priceMultiplier": "0.01",
      "quantityMultiplier": "0.001",
      "type": "perpetual",
      "status": "online",
      "openTime": "1700000000000",
      "offTime": "",
      "limitOpenTime": ""
    }
  ],
  "arg": {
    "instType": "usdt-futures",
    "topic": "instruments"
  },
  "action": "snapshot",
  "ts": 1736371332162
}
```

### 推送参数

| 参数名        | 参数类型           | 描述                                                                                                                 |
|---------------|--------------------|------------------------------------------------------------------------------------------------------------------------|
| arg           | Object             | 请求订阅成功的频道列表                                                                                                 |
| &gt; instType | String             | 产品线类型<br/>`spot` 现货交易<br/>`usdt-futures` USDT合约 <br/> `coin-futures` 币本位合约 <br/> `usdc-futures` USDC合约 |
| &gt; topic    | String             | 频道名 <br/> `instruments` 产品信息频道                                                                               |
| action        | String             | 推送数据的方式 <br/> `snapshot` 全量 <br/> `update` 增量                                                              |
| data          | List&lt;Object&gt; | 订阅的数据                                                                                                           |
| &gt; baseCoin | String             | 交易币种 <br/> 如 `BTCUSDT` 中的 `BTC`                                                                                |
| &gt; quoteCoin | String            | 计价币种 <br/> 如 `BTCUSDT` 中的 `USDT`                                                                               |
| &gt; buyLimitPriceRatio | String  | 买价限价比例 <br/> 买入限价与市场价格的比率，决定买单下单时的最高价格                                                    |
| &gt; sellLimitPriceRatio | String | 卖价限价比例 <br/> 卖出限价与市场价格的比率，决定卖单下单时的最低价格                                                   |
| &gt; marketPriceRatio | String     | 市价比例 <br/> 买卖市价与市场价格的比率，决定下单时的价格范围                                                           |
| &gt; priceProtectThreshold | String | 止盈止损价差保护阈值 <br/> 止盈止损触发价与最新/标记价格的最大允许偏差比例 <br/> 小数形式，如 `0.1` 代表 10%             |
| &gt; feeRateUpRatio | String       | 手续费上浮比例 <br/> 实际费用相对于基础费用增加的百分比                                                                 |
| &gt; openCostUpRatio | String      | 开仓成本上浮比例 <br/> 开仓的成本相对于基础或标准成本增加的百分比                                                       |
| &gt; minOrderQty | String          | 限价最小下单数量 <br/> 以基础币种下单时允许的最小数量                                                                   |
| &gt; maxOrderQty | String          | 限价最大下单数量 <br/> 以基础币种下单时允许的最大数量 <br/> 为 `0` 表示不限制                                            |
| &gt; minOrderAmount | String       | 限价最小下单金额 <br/> 以计价币种下单时允许的最小数量                                                                   |
| &gt; maxMarketOrderQty | String    | 市价最大下单数量 <br/> 以基础币种下单时允许的最大数量                                                                   |
| &gt; pricePrecision | String       | 价格精度 <br/> 价格允许的小数位数 <br/> 下单时，填写的价格必须是价格精度的整数倍                                        |
| &gt; quantityPrecision | String     | 数量精度 <br/> 数量允许的小数位数 <br/> 下单时，填写的数量必须是数量精度的整数倍                                        |
| &gt; quotePrecision | String       | 市价下单精度 <br/> 计价币价格允许的小数位数                                                                             |
| &gt; priceMultiplier | String      | 价格乘数 <br/> 配合 `pricePrecision`。如 `pricePrecision=2`、`priceMultiplier=0.01`，则委托价格要满足 `priceMultiplier` 的倍数，并且小数位是 2 |
| &gt; quantityMultiplier | String   | 数量乘数 <br/> 合约下单使用，配合 `quantityPrecision`。如 `quantityPrecision=2`、`quantityMultiplier=0.01`，则委托数量要满足 `quantityMultiplier` 的倍数，并且小数位是 2 |
| &gt; type       | String          | 合约类型 <br/> `perpetual` 永续 <br/> `delivery` 交割                                                                  |
| &gt; status     | String          | 交易对状态 <br/> `listed` 上架(未开盘) <br/> `online` 正常交易/开盘 <br/> `limit_open` 合约禁止开仓 <br/> `limit_close` 合约禁止平仓，现货停盘 <br/> `offline` 下架/维护 |
| &gt; openTime   | String          | 开盘时间 <br/> Unix毫秒时间戳                                                                                          |
| &gt; offTime    | String          | 停盘时间 <br/> 未配置则返回 `""` <br/> 只支持合约                                                                     |
| &gt; limitOpenTime | String       | 限制开仓时间 <br/> 其它值表示 symbol 正在/计划维护，指定时间后禁止交易 <br/> 未配置则返回 `""`                           |

</div>