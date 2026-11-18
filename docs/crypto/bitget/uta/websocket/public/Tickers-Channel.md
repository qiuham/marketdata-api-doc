---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/public/Tickers-Channel
api_type: WebSocket
updated_at: 2026-11-18 19:00:57.270726
---

# Tickers Channel

### Description

Push the latest transaction price, best bid, best ask, 24-hour trading volume, and other market data for the product. When the market changes (transactions, best bid/ask updates), the push frequency is 200ms.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "spot",
            "topic": "ticker",
            "symbol": "BTCUSDT"
        }
    ]
}
```

### Request Parameters

| Parameters    | Type               | Required | Description                                                                                                                                |
|---------------|--------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------|
| op            | String             | Yes      | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe                                                                      |
| args          | List&lt;Object&gt; | Yes      | Subscribed channel                                                                                                                         |
| &gt; instType | String             | Yes      | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String             | Yes      | Topic <br/> `ticker` Market data channel                                                                                                   |
| &gt; symbol   | String             | Yes      | Trading pair <br/> e.g. `BTCUSDT`                                                                                                          |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "spot",
    "topic": "ticker",
    "symbol": "BTCUSDT"
  },
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    | Type   | Description                                                                                                                                |
|---------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------|
| event         | String | Event                                                                                                                                      |
| arg           | Object | Subscribed channel                                                                                                                         |
| &gt; instType | String | Product type<br/>`spot` Spot trading<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures |
| &gt; topic    | String | Topic <br/> `ticker` Ticker channel                                                                                                        |
| &gt; symbol   | String | Trading pair <br/> e.g. `BTCUSDT`                                                                                                          |
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
      "bid1Price": "99999",
      "lowPrice24h": "98200",
      "ask1Size": "188.312553",
      "volume24h": "37.722858",
      "price24hPcnt": "0.01833",
      "highPrice24h": "100000",
      "turnover24h": "3750302.979626",
      "bid1Size": "186.183209",
      "ask1Price": "100000",
      "openPrice24h": "0",
      "lastPrice": "100000",
      "platformTurnover24h": "677732572.225658"
    }
  ],
  "arg": {
    "instType": "spot",
    "symbol": "BTCUSDT",
    "topic": "ticker"
  },
  "action": "snapshot",
  "ts": 1736371332162
}
```

### Push Parameters

#### Spot Push

| Parameters        | Parameter Type     | Description                                 |
|-------------------|--------------------|---------------------------------------------|
| arg               | Object             | Subscribed channel                          |
| &gt; instType     | String             | Product type <br/>`spot` Spot trading       |
| &gt; topic        | String             | Topic <br/> `ticker` Ticker channel         |
| &gt; symbol       | String             | Symbol name                                 |
| action            | String             | Data push action <br/> `snapshot` Full data |
| data              | List&lt;Object&gt; | Subscribed data                             |
| &gt; highPrice24h | String             | Highest price in the last 24 hours          |
| &gt; lowPrice24h  | String             | Lowest price in the last 24 hours           |
| &gt; openPrice24h | String             | Market price 24 hours ago                   |
| &gt; lastPrice    | String             | Latest price                                |
| &gt; turnover24h  | String             | 24-hour turnover                            |
| &gt; volume24h    | String             | 24-hour volume                              |
| &gt; bid1Price    | String             | Best bid price                              |
| &gt; ask1Price    | String             | Best ask price                              |
| &gt; bid1Size     | String             | Best bid quantity                           |
| &gt; ask1Size     | String             | Best ask quantity                           |
| &gt; price24hPcnt | String             | 24-hour price change percentage             |
| &gt; platformTurnover24h | String    | 24-hour platform turnover <br/> Only available for rtoken |

#### Futures Push

| Parameters             | Parameter Type     | Description                                                                                                                                                                                                                                                                                                         |
|------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| arg                    | Object             | Subscribed successful channel                                                                                                                                                                                                                                                                                       |
| &gt; instType          | String             | Product type<br/>`usdt-futures` USDT futures <br/> `coin-futures` Coin-M futures <br/> `usdc-futures` USDC futures                                                                                                                                                                                                  |
| &gt; topic             | String             | Topic <br/> `ticker` Ticker channel                                                                                                                                                                                                                                                                                 |
| action                 | String             | Data push action <br/> `snapshot` Full data                                                                                                                                                                                                                                                                         |
| data                   | List&lt;Object&gt; | Subscribed data                                                                                                                                                                                                                                                                                                     |
| &gt; highPrice24h      | String             | Highest price in the last 24 hours                                                                                                                                                                                                                                                                                  |
| &gt; lowPrice24h       | String             | Lowest price in the last 24 hours                                                                                                                                                                                                                                                                                   |
| &gt; openPrice24h      | String             | Market price 24 hours ago                                                                                                                                                                                                                                                                                           |
| &gt; lastPrice         | String             | Latest price                                                                                                                                                                                                                                                                                                        |
| &gt; turnover24h       | String             | 24-hour turnover                                                                                                                                                                                                                                                                                                    |
| &gt; volume24h         | String             | 24-hour volume                                                                                                                                                                                                                                                                                                      |
| &gt; bid1Price         | String             | Best bid price                                                                                                                                                                                                                                                                                                      |
| &gt; ask1Price         | String             | Best ask price                                                                                                                                                                                                                                                                                                      |
| &gt; bid1Size          | String             | Best bid quantity                                                                                                                                                                                                                                                                                                   |
| &gt; ask1Size          | String             | Best ask quantity                                                                                                                                                                                                                                                                                                   |
| &gt; price24hPcnt      | String             | 24-hour price change percentage                                                                                                                                                                                                                                                                                     |
| &gt; indexPrice        | String             | Index price <br/> Available only for futures                                                                                                                                                                                                                                                                        |
| &gt; markPrice         | String             | Mark price  <br/> Available only for futures                                                                                                                                                                                                                                                                        |
| &gt; fundingRate       | String             | Funding rate  <br/> Available only for futures                                                                                                                                                                                                                                                                      |
| &gt; nextFundingTime   | String             | Next funding rate settlement time                                                                                                                                                                                                                                                                                   |
| &gt; openInterest      | String             | Open interest  <br/> Available only for futures                                                                                                                                                                                                                                                                     |
| &gt; deliveryTime      | String             | Delivery time <br/> Available only for deliveries                                                                                                                                                                                                                                                                   |
| &gt; deliveryStartTime | String             | Delivery start time  <br/> Available only for deliveries                                                                                                                                                                                                                                                            |
| &gt; deliveryStatus    | String             | Delivery status  <br/> `delivery_config_period` New pair configuration <br/> `delivery_normal` Trading <br/> `delivery_before` 10 minutes before delivery, no new orders <br/> `delivery_period` During delivery, no opening or closing of positions, and no order cancellation <br/> Available only for deliveries |

</div>

---

# 行情

### 描述

推送产品的最新成交价、买一价、卖一价和24小时交易量等行情数据；当行情发生变化（成交、买一价或卖一价更新）时，推送频率为 200ms。

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "spot",
            "topic": "ticker",
            "symbol": "BTCUSDT"
        }
    ]
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                                                                                                  | 
|:--------------|:-------------------|:-----|:----------------------------------------------------------------------------------------------------|
| op            | String             | 是    | 操作<br/>`subscribe` 订阅 <br/>`unsubscribe` 退订                                                         |
| args          | List&lt;Object&gt; | 是    | 请求订阅的频道列表                                                                                           |
| &gt; instType | String             | 是    | 产品线类型<br/>`spot` 现货交易<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String             | 是    | 频道名<br/>`ticker`  行情频道                                                                              |
| &gt; symbol   | String             | 是    | 交易对名称<br/>例如`BTCUSDT`                                                                               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "spot",
    "topic": "ticker",
    "symbol": "BTCUSDT"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数

| 返回字段          | 参数类型   | 字段说明                                                                                                | 
|:--------------|:-------|:----------------------------------------------------------------------------------------------------|
| event         | String | 事件                                                                                                  |
| arg           | Object | 订阅的频道                                                                                               |
| &gt; instType | String | 产品线类型<br/>`spot` 现货交易<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约 |
| &gt; topic    | String | 频道名 <br/>`ticker`行情频道                                                                               |
| &gt; symbol   | String | 交易对名称                                                                                               |
| code          | String | 错误码                                                                                                 |
| msg           | String | 错误消息                                                                                                |
| connId        | String | 连接ID                                                                                                |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
  "data": [
    {
      "bid1Price": "99999",
      "lowPrice24h": "98200",
      "ask1Size": "188.312553",
      "volume24h": "37.722858",
      "price24hPcnt": "0.01833",
      "highPrice24h": "100000",
      "turnover24h": "3750302.979626",
      "bid1Size": "186.183209",
      "ask1Price": "100000",
      "openPrice24h": "0",
      "lastPrice": "100000",
      "platformTurnover24h": "677732572.225658"
    }
  ],
  "arg": {
    "instType": "spot",
    "symbol": "BTCUSDT",
    "topic": "ticker"
  },
  "action": "snapshot",
  "ts": 1736371332162
}
```

### 推送数据参数

#### 现货推送

| 返回字段             | 参数类型               | 字段说明                    | 
|:-----------------|:-------------------|:------------------------|
| arg              | Object             | 订阅频道                    |
| &gt; instType    | String             | 产品线类型<br/>`spot` 现货交易   |
| &gt; topic       | String             | 频道名<br/>`ticker`行情频道    |
| &gt; symbol      | String             | 交易对名称                   |
| action           | String             | 推送数据动作<br/>`snapshot`全量 |
| data             | List&lt;Object&gt; | 订阅的数据                   |
| &gt;highPrice24h | String             | 24小时最高价                 |
| &gt;lowPrice24h  | String             | 24小时最低价                 |
| &gt;openPrice24h | String             | 24小时前的市场价格              |
| &gt;lastPrice    | String             | 最新价                     |
| &gt;turnover24h  | String             | 24小时成交额                 |
| &gt;volume24h    | String             | 24小时成交量                 |
| &gt;bid1Price    | String             | 买一价                     |
| &gt;ask1Price    | String             | 卖一价                     |
| &gt;bid1Size     | String             | 买一量                     |
| &gt;ask1Size     | String             | 卖一量                     |
| &gt;price24hPcnt | String             | 24小时价格涨跌幅               |
| &gt;platformTurnover24h | String      | 24小时平台成交额<br/>仅rtoken有值  |

#### 合约推送

| 返回字段                  | 参数类型               | 字段说明                                                                                                                 | 
|:----------------------|:-------------------|:---------------------------------------------------------------------------------------------------------------------|
| arg                   | Object             | 订阅成功频道                                                                                                               |
| &gt; instType         | String             | 产品线类型<br/> `usdt-futures` USDT合约<br/>`coin-futures` 币本位合约<br/>`usdc-futures` USDC合约                                  |
| &gt; topic            | String             | 频道名<br/>`ticker`行情频道                                                                                                 |
| action                | String             | 推送数据动作<br/>`snapshot`全量                                                                                              |
| data                  | List&lt;Object&gt; | 订阅的数据                                                                                                                |
| &gt;highPrice24h      | String             | 24小时最高价                                                                                                              |
| &gt;lowPrice24h       | String             | 24小时最低价                                                                                                              |
| &gt;openPrice24h      | String             | 24小时前的市场价格                                                                                                           |
| &gt;lastPrice         | String             | 最新价                                                                                                                  |
| &gt;turnover24h       | String             | 24小时成交额                                                                                                              |
| &gt;volume24h         | String             | 24小时成交量                                                                                                              |
| &gt;bid1Price         | String             | 买一价                                                                                                                  |
| &gt;ask1Price         | String             | 卖一价                                                                                                                  |
| &gt;bid1Size          | String             | 买一量                                                                                                                  |
| &gt;ask1Size          | String             | 卖一量                                                                                                                  |
| &gt;price24hPcnt      | String             | 24小时价格涨跌幅                                                                                                            |
| &gt;indexPrice        | String             | 指数价格                                                                                                                 |
| &gt;markPrice         | String             | 标记价格                                                                                                                 |
| &gt;fundingRate       | String             | 当前资金费率                                                                                                               |
| &gt;nextFundingTime   | String             | 下次资金费率结算时间                                                                                                           |
| &gt;openInterest      | String             | 当前平台总持仓量                                                                                                             |
| &gt;deliveryTime      | String             | 交割时间                                                                                                                 |
| &gt;deliveryStartTime | String             | 交割开始时间                                                                                                               |
| &gt;deliveryStatus    | String             | 交割状态 <br/> `delivery_config_period`配置中 <br/>`delivery_normal`正常 <br/>`delivery_before`待交割 <br/> `delivery_period`交割中 |

</div>