---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/cfd-market
api_type: REST
updated_at: 2026-11-27 19:02:31.298424
---

# CFD Market

CFD market data APIs: instruments, tickers, and candlestick history.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/cfd/market/tickers` — Get Tickers
- `GET /api/v3/cfd/market/history-candlestick` — Get Kline/Candlestick History

## Get Tickers

`GET /api/v3/cfd/market/tickers`

Rate limit: 10/sec/UID <br/> Permission: UTA trade (read-only)

Query ticker information for a CFD trading pair.

Operation ID: `cfdMarketGetTickers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair name |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].quoteTime | string |  | Quote time |
| data[].askOpenPriceChange | string |  | Change in the ask opening price<br/>Shown as a decimal, e.g. 0.1 represents 10% |
| data[].bidOpenPriceChange | string |  | Change in the bid opening price<br/>Shown as a decimal, e.g. 0.1 represents 10% |
| data[].highPrice | string |  | Today's highest price |
| data[].lowPrice | string |  | Today's lowest price |
| data[].ask1 | string |  | Best ask price |
| data[].bid1 | string |  | Best bid price |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "symbol": "XAUUSD",
      "quoteTime": "1740000000000",
      "askOpenPriceChange": "0.001",
      "bidOpenPriceChange": "0.001",
      "highPrice": "2650.12",
      "lowPrice": "2610.34",
      "ask1": "2620.60",
      "bid1": "2620.50"
    }
  ]
}
```

## Get Kline/Candlestick History

`GET /api/v3/cfd/market/history-candlestick`

Rate limit: 10/sec/UID <br/> Permission: UTA trade (read-only)

Query historical candlestick data for a CFD trading pair.

Operation ID: `cfdMarketGetHistoryCandlestick`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | Trading pair, e.g. `XAUUSD` |
| interval | query | string | 是 | Granularity<br/>`1m`, `15m`, `1h`, `4h`, `1d` |
| side | query | string | 是 | Trade side<br/>`buy`: Buy side<br/>`sell`: Sell side |
| startTime | query | string |  | Start time; returns candlesticks after this time<br/>A Unix millisecond timestamp, e.g. `1672410780000`<br/>Maximum query range is 90 days |
| endTime | query | string |  | End time; returns candlesticks before this time<br/>A Unix millisecond timestamp, e.g. `1672410780000`<br/>Maximum query range is 90 days |
| limit | query | string |  | Number of entries per page<br/>Default: 100, maximum: 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | Each element is an array: [timestamp, open, high, low, close] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    [
      "1597026383085",
      "2610.34",
      "2650.12",
      "2605.10",
      "2620.55"
    ]
  ]
}
```


---

CFD 行情 API：产品信息、行情数据、K 线数据。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v3/cfd/market/tickers` — 获取行情数据
- `GET /api/v3/cfd/market/history-candlestick` — 获取 K 线数据

## 获取行情数据

`GET /api/v3/cfd/market/tickers`

限频：10次/秒/UID <br/> 权限：UTA 交易（只读）

查询 CFD 交易对的行情信息。

Operation ID: `cfdMarketGetTickers`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易对名称 |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 交易对名称 |
| data[].quoteTime | string |  | 报价时间 |
| data[].askOpenPriceChange | string |  | 卖盘开盘价格涨跌幅<br/>小数形式展示，如0.1代表10% |
| data[].bidOpenPriceChange | string |  | 买盘开盘价格涨跌幅<br/>小数形式展示，如0.1代表10% |
| data[].highPrice | string |  | 今日最高价 |
| data[].lowPrice | string |  | 今日最低价 |
| data[].ask1 | string |  | 卖一价 |
| data[].bid1 | string |  | 买一价 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    {
      "symbol": "XAUUSD",
      "quoteTime": "1740000000000",
      "askOpenPriceChange": "0.001",
      "bidOpenPriceChange": "0.001",
      "highPrice": "2650.12",
      "lowPrice": "2610.34",
      "ask1": "2620.60",
      "bid1": "2620.50"
    }
  ]
}
```

## 获取 K 线数据

`GET /api/v3/cfd/market/history-candlestick`

限频：10次/秒/UID <br/> 权限：UTA 交易（只读）

查询 CFD 交易对的历史 K 线数据。

Operation ID: `cfdMarketGetHistoryCandlestick`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string | 是 | 交易对，如 `XAUUSD` |
| interval | query | string | 是 | 时间粒度<br/>`1m`、`15m`、`1h`、`4h`、`1d` |
| side | query | string | 是 | 交易方向<br/>`buy`：买方<br/>`sell`：卖方 |
| startTime | query | string |  | 开始时间，Unix 毫秒时间戳，如 `1672410780000`<br/>单次查询范围不超过 90 天 |
| endTime | query | string |  | 结束时间，Unix 毫秒时间戳，如 `1672410780000`<br/>单次查询范围不超过 90 天 |
| limit | query | string |  | 每页条数，默认 100，最大 100 |

### 响应 200：成功响应

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | string[][] |  | 每个元素为数组：[时间戳, 开盘价, 最高价, 最低价, 收盘价] |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1740000000000.0,
  "data": [
    [
      "1597026383085",
      "2610.34",
      "2650.12",
      "2605.10",
      "2620.55"
    ]
  ]
}
```