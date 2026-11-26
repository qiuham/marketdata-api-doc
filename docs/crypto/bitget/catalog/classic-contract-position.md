---
exchange: bitget
source_url: https://www.bitget.com/docs/catalog/classic-contract-position
api_type: REST
updated_at: 2026-11-26 19:03:47.846822
---

# Classic Contract Position API

Classic account — futures position queries.

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/mix/market/query-position-lever` — Get Position Tier
- `GET /api/v2/mix/position/single-position` — Get Single Position
- `GET /api/v2/mix/position/history-position` — Get Historical Position
- `GET /api/v2/mix/position/adlRank` — Get Position Adl Rank
- `GET /api/v2/mix/position/all-position` — Get All Positions

## Get Position Tier

`GET /api/v2/mix/market/query-position-lever`

Frequency limit: 10 times/1s (IP)

Get the position gradient configuration of a certain trading pair

Operation ID: `classicContractPositionGetQueryPositionLever`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| symbol | query | string | 是 | Trading pair |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].level | string |  | Tier |
| data[].startUnit | string |  | Minimum value |
| data[].endUnit | string |  | Maximum value |
| data[].leverage | string |  | Leverage |
| data[].keepMarginRate | string |  | Maintenance margin rate: The margin amount corresponds to the position quantity tier. When the margin rate of a position is less than the maintenance margin rate, it will trigger a forced partial liquidation or full liquidation. |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695796884470,
  "data": [
    {
      "symbol": "BTCUSDT",
      "level": "1",
      "startUnit": "0",
      "endUnit": "50000",
      "leverage": "125",
      "keepMarginRate": "0.004"
    },
    {
      "symbol": "BTCUSDT",
      "level": "2",
      "startUnit": "50000",
      "endUnit": "200000",
      "leverage": "100",
      "keepMarginRate": "0.005"
    }
  ]
}
```

## Get Single Position

`GET /api/v2/mix/position/single-position`

Rate limit: 10 requests/sec/UID

Returns position information of a single symbol, response including estimated liquidation price.

Operation ID: `classicContractPositionGetSinglePosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| symbol | query | string | 是 | Trading pair, e.g. BTCUSDT |
| marginCoin | query | string | 是 | Margin coin, capitalized, e.g. USDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].marginCoin | string |  | Margin coin |
| data[].holdSide | string |  | Position direction<br><br>`long`: long position<br><br>`short`: short position |
| data[].openDelegateSize | string |  | Amount to be filled of the current order (base coin) |
| data[].marginSize | string |  | Margin amount (margin coin) |
| data[].available | string |  | Available amount for positions (base currency) |
| data[].locked | string |  | Frozen amount in the position (base currency) |
| data[].total | string |  | Total amount of all positions (available amount + locked amount) |
| data[].leverage | string |  | Leverage |
| data[].achievedProfits | string |  | Realized PnL(exclude funding fee and transaction fee) |
| data[].openPriceAvg | string |  | Average entry price |
| data[].marginMode | string |  | Margin mode<br><br>`isolated`: isolated margin<br><br>`crossed`: cross margin |
| data[].posMode | string |  | Position mode<br><br>`one_way_mode`: positions in one-way mode<br><br>`hedge_mode`: positions in hedge-mode |
| data[].unrealizedPL | string |  | Unrealized PnL |
| data[].liquidationPrice | string |  | Estimated liquidation price<br><br>If the value <= 0, it means the position is at low risk and there is no liquidation price at this time |
| data[].keepMarginRate | string |  | Tiered maintenance margin rate |
| data[].markPrice | string |  | Mark price |
| data[].marginRatio | string |  | Maintenance margin rate (MMR), 0.1 represents 10% |
| data[].breakEvenPrice | string |  | Position breakeven price |
| data[].totalFee | string |  | Funding fee, the accumulated value of funding fee during the position,The initial value is empty, indicating that no funding fee has been charged yet. |
| data[].deductedFee | string |  | Deducted transaction fees: transaction fees deducted during the position |
| data[].cashDividend | string |  | Cash dividend<br><br>The unit is USDT |
| data[].cTime | string |  | Creation time, timestamp, milliseconds |
| data[].assetMode | string |  | `single` : single asset mode  <br><br>`union` multi-Assets mode |
| data[].uTime | string |  | Last updated time, timestamp, milliseconds |
| data[].autoMargin | string |  | Auto Margin <br><br>  `on` Auto Margin Call <br><br> `off` No Auto Margin Call |
| data[].grant | string |  | Futures Airdrop Voucher Amount |
| data[].takeProfit | string |  | Take profit price |
| data[].stopLoss | string |  | Stop loss price |
| data[].takeProfitId | string |  | Take profit order ID |
| data[].stopLossId | string |  | Stop loss order ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1768195413808,
  "data": [
    {
      "marginCoin": "USDT",
      "symbol": "BTCUSDT",
      "holdSide": "short",
      "openDelegateSize": "0",
      "marginSize": "32.9182142857142858",
      "available": "0.005",
      "locked": "0",
      "total": "0.005",
      "leverage": "14",
      "achievedProfits": "-48.1989666666666705",
      "openPriceAvg": "88505.233333333333",
      "marginMode": "crossed",
      "posMode": "hedge_mode",
      "unrealizedPL": "-18.328833333333335",
      "liquidationPrice": "17288450.450983311758416",
      "keepMarginRate": "0.004",
      "markPrice": "92171",
      "marginRatio": "0.0030244464835655",
      "breakEvenPrice": "67274.9159193683778732",
      "totalFee": "-56.2349883554",
      "deductedFee": "1.5158073",
      "cashDividend": "0",
      "grant": "",
      "assetMode": "union",
      "autoMargin": "off",
      "takeProfit": null,
      "stopLoss": null,
      "takeProfitId": null,
      "stopLossId": null,
      "cTime": "1766103799183",
      "uTime": "1768194000530"
    }
  ]
}
```

## Get Historical Position

`GET /api/v2/mix/position/history-position`

20times/S （uid）

Check position history

(Only check the data within 3 months)

Operation ID: `classicContractPositionGetHistoryPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | Trading pair |
| productType | query | string |  | Product type, default:`USDT-FUTURES`, if symbol parameter reuqest, then this parameter will not take effect <br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| idLessThan | query | string |  | Requests the content on the page before this ID (older data), the value input should be the endId of the corresponding interface. |
| startTime | query | string |  | Start time(timestamp in milliseconds)  <br><br>timestampis Unix time in milliseconds，for example 1597026383085<br><br>（Wildest time range is 3 months，if this field is empty then the default time range is 3 months.） |
| endTime | query | string |  | Start time (timestamp in milliseconds) <br><br>timestampis Unix time in milliseconds，for example 1597026383085<br><br>（Wildest time range is 3 months，if this field is empty then the default time range is 3 months.） |
| limit | query | string |  | Default 20 Max 100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | Historical Position Data |
| data.list[].positionId | string |  | History position ID |
| data.list[].symbol | string |  | Trading pair |
| data.list[].marginCoin | string |  | Margin coin |
| data.list[].holdSide | string |  | Position direction<br><br>long: long position <br><br>short: short position |
| data.list[].posMode | string |  | Position mode<br><br>`one_way_mode`: positions in one-way mode<br><br>`hedge_mode`: positions in hedge-mode |
| data.list[].openAvgPrice | string |  | Average price of opening position |
| data.list[].closeAvgPrice | string |  | Average price of closing position |
| data.list[].marginMode | string |  | Margin Mode <br><br>`isolated`: Isolated margin    <br><br>`crossed`: Cross margin |
| data.list[].openTotalPos | string |  | Accumulated amount of long positions |
| data.list[].closeTotalPos | string |  | Accumulated amount of short positions |
| data.list[].pnl | string |  | realized profit and loss |
| data.list[].netProfit | string |  | net profit<br><br>netProfit = pnl + totalFunding + openFee + closeFee |
| data.list[].totalFunding | string |  | Accumulated funding costs |
| data.list[].openFee | string |  | Total handling fee for position opening |
| data.list[].closeFee | string |  | Total handling fee for position closing |
| data.list[].cashDividend | string |  | Cash dividend<br><br>The unit is USDT |
| data.list[].utime | string |  | Last update time Timestamp milliseconds |
| data.list[].ctime | string |  | Create time Timestamp milliseconds |
| data.endId | string |  | ID of the last data。id value is tracking No and use it to check based on idLessThan |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1312312312321,
  "data": {
    "list": [
      {
        "positionId": "xxxxxxxxxxx",
        "marginCoin": "USDT",
        "symbol": "BTCUSDT",
        "holdSide": "long",
        "openAvgPrice": "32000",
        "closeAvgPrice": "32500",
        "marginMode": "isolated",
        "openTotalPos": "0.01",
        "closeTotalPos": "0.01",
        "pnl": "14.1",
        "netProfit": "12.1",
        "totalFunding": "0.1",
        "openFee": "0.01",
        "closeFee": "0.01",
        "cashDividend": "0",
        "posMode": "one_way_mode",
        "ctime": "1988824171000",
        "utime": "1988824171000"
      }
    ],
    "endId": "23423432423423234"
  }
}
```

## Get Position Adl Rank

`GET /api/v2/mix/position/adlRank`

5times/S （uid）

Query Account Position ADL Rank

Operation ID: `classicContractPositionGetPositionAdl`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | Product type, default:`USDT-FUTURES`,  <br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair |
| data[].marginCoin | string |  | Margin coin |
| data[].adlRank (Deprecated) | string |  | This indicator shows your position in the ADL queue. the further ahead you are in the queue, the higher the possibility that your position may be reduced in the event of an auto-deleveraging |
| data[].rank | string |  | Current position's ADL sequence rank. Closer to 1, more prone to ADL during market events. |
| data[].holdSide | string |  | Position direction<br><br>long: long position <br><br>short: short position |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753775486724,
  "data": [
    {
      "symbol": "MOVEUSDT",
      "marginCoin": "USDT",
      "adlRank": "0.2248",
      "rank": "0.7752",
      "holdSide": "long"
    }
  ]
}
```

## Get All Positions

`GET /api/v2/mix/position/all-position`

Rate limit: 5 requests/sec/UID

Returns information about all current positions with the given `productType`

Operation ID: `classicContractPositionGetAllPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | Product type<br><br>`USDT-FUTURES` USDT-M Futures<br><br>`COIN-FUTURES` Coin-M Futures<br><br>`USDC-FUTURES` USDC-M Futures |
| marginCoin | query | string |  | Margin coin, capitalized. e.g. USDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | Trading pair name |
| data[].marginCoin | string |  | Margin coin |
| data[].holdSide | string |  | Position direction<br><br>`long`: long position<br><br>`short`: short position |
| data[].openDelegateSize | string |  | Amount to be filled of the current order (base coin) |
| data[].marginSize | string |  | Margin amount (margin coin) |
| data[].available | string |  | Available amount for positions (base currency) |
| data[].locked | string |  | Frozen amount in the position (base currency) |
| data[].total | string |  | Total amount of all positions (available amount + locked amount) |
| data[].leverage | string |  | Leverage |
| data[].achievedProfits | string |  | Realized PnL(exclude the funding fee and transaction fee) |
| data[].openPriceAvg | string |  | Average entry price |
| data[].marginMode | string |  | Margin mode<br><br>`isolated`: isolated margin<br><br>`crossed`: cross margin |
| data[].posMode | string |  | Position mode<br><br>`one_way_mode` positions in one-way mode<br><br>`hedge_mode` positions in hedge-mode |
| data[].unrealizedPL | string |  | Unrealized PnL |
| data[].liquidationPrice | string |  | Estimated liquidation price<br><br>If the value <= 0, it means the position is at low risk and there is no liquidation price at this time |
| data[].keepMarginRate | string |  | Tiered maintenance margin rate |
| data[].markPrice | string |  | Mark price |
| data[].marginRatio | string |  | Maintenance margin rate (MMR), 0.1 represents 10% |
| data[].breakEvenPrice | string |  | Position breakeven price |
| data[].totalFee | string |  | Funding fee, the accumulated value of funding fee during the position,The initial value is empty, indicating that no funding fee has been charged yet. |
| data[].takeProfit | string |  | Take profit price |
| data[].stopLoss | string |  | Stop loss price |
| data[].takeProfitId | string |  | Take profit order ID |
| data[].stopLossId | string |  | Stop loss order ID |
| data[].deductedFee | string |  | Deducted transaction fees: transaction fees deducted during the position |
| data[].cashDividend | string |  | Cash dividend<br><br>The unit is USDT |
| data[].cTime | string |  | Creation time, timestamp, milliseconds <br><br>The set is in descending order from the latest time. |
| data[].assetMode | string |  | `single` : single asset mode  <br><br>`union` multi-Assets mode |
| data[].autoMargin | string |  | Auto Margin <br><br>  `on` Auto Margin Call <br><br> `off` No Auto Margin Call |
| data[].uTime | string |  | Last updated time, timestamp, milliseconds |
| data[].grant | string |  | Futures Airdrop Voucher Amount |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767685381615,
  "data": [
    {
      "marginCoin": "USDT",
      "symbol": "BTCUSDT",
      "holdSide": "short",
      "openDelegateSize": "0",
      "marginSize": "103.1894785714285715",
      "available": "0.0155",
      "locked": "0",
      "total": "0.0155",
      "leverage": "14",
      "achievedProfits": "8.605233333333333",
      "openPriceAvg": "88505.233333333333",
      "marginMode": "crossed",
      "posMode": "hedge_mode",
      "unrealizedPL": "-72.8215833333333385",
      "liquidationPrice": "5737867.8639926850760812",
      "keepMarginRate": "0.004",
      "markPrice": "93203.4",
      "marginRatio": "0.0028541392311979",
      "breakEvenPrice": "85283.0669339944416898",
      "totalFee": "-56.8315381906",
      "deductedFee": "0.92414181",
      "cashDividend": "0",
      "grant": "",
      "assetMode": "union",
      "autoMargin": "off",
      "takeProfit": "",
      "stopLoss": "",
      "takeProfitId": "",
      "stopLossId": "",
      "cTime": "1766103799183",
      "uTime": "1767682800537"
    }
  ]
}
```


---

经典账户 — 合约持仓查询。

版本: 1.0.0

## 服务地址

- `https://api.bitget.com`

## 接口列表

- `GET /api/v2/mix/market/query-position-lever` — 获取仓位档位梯度配置
- `GET /api/v2/mix/position/single-position` — 获取单个合约仓位信息
- `GET /api/v2/mix/position/history-position` — 获取合约历史持仓列表
- `GET /api/v2/mix/position/adlRank` — 获取合约仓位ADL排名列表
- `GET /api/v2/mix/position/all-position` — 获取全部合约仓位信息

## 获取仓位档位梯度配置

`GET /api/v2/mix/market/query-position-lever`

限速规则: 10次/1s (IP)

获取某交易对的仓位档位梯度配置

Operation ID: `classicContractPositionGetQueryPositionLever`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string | 是 | 交易币对 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名 |
| data[].level | string |  | 阶梯档位 |
| data[].startUnit | string |  | 价值下限 |
| data[].endUnit | string |  | 价值上限 |
| data[].leverage | string |  | 杠杆倍数 |
| data[].keepMarginRate | string |  | 维持保证金率，持仓档位对应的数值，当仓位的保证金率小于维持保证金率时，将会触发强制减仓或爆仓 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1695867562585,
  "data": [
    {
      "symbol": "BTCUSDT",
      "level": "1",
      "startUnit": "0",
      "endUnit": "50000",
      "leverage": "125",
      "keepMarginRate": "0.004"
    },
    {
      "symbol": "BTCUSDT",
      "level": "2",
      "startUnit": "50000",
      "endUnit": "200000",
      "leverage": "100",
      "keepMarginRate": "0.005"
    }
  ]
}
```

## 获取单个合约仓位信息

`GET /api/v2/mix/position/single-position`

限频规则：10次/秒/UID

返回单个合约的仓位信息，包括预估强平价。

Operation ID: `classicContractPositionGetSinglePosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| symbol | query | string | 是 | 交易币对，例如：BTCUSDT |
| marginCoin | query | string | 是 | 保证金币种，必须大写，例如：USDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名称 |
| data[].marginCoin | string |  | 保证金币种 |
| data[].holdSide | string |  | 持仓方向<br><br>`long`: 多仓<br><br>`short`: 空仓 |
| data[].openDelegateSize | string |  | 当前委托待成交的数量(基础币) |
| data[].marginSize | string |  | 保证金数量 (保证金币种) |
| data[].available | string |  | 仓位可用(基础币) |
| data[].locked | string |  | 仓位冻结(基础币) |
| data[].total | string |  | 仓位总数量(available + locked) |
| data[].leverage | string |  | 杠杆倍数 |
| data[].achievedProfits | string |  | 已实现盈亏（不包含手续费和资金费用） |
| data[].openPriceAvg | string |  | 平均开仓价 |
| data[].marginMode | string |  | 保证金模式<br><br>`crossed`:全仓<br><br>`isolated`: 逐仓 |
| data[].posMode | string |  | 持仓模式<br><br>`one_way_mode` 单向持仓<br><br>`hedge_mode` 双向持仓 |
| data[].unrealizedPL | string |  | 未实现盈亏 |
| data[].liquidationPrice | string |  | 预估强平价<br><br>小于等于0，代表永不爆仓 |
| data[].keepMarginRate | string |  | 仓位档位维持保证金率 |
| data[].markPrice | string |  | 标记价格 |
| data[].marginRatio | string |  | 维持保证金率（0.1代表10%） |
| data[].breakEvenPrice | string |  | 仓位盈亏平衡价 |
| data[].totalFee | string |  | 资金费用，仓位存续期间，资金费用的累加值,初始值为空，表示还没收取过资金费 |
| data[].deductedFee | string |  | 已扣手续费，仓位存续期间扣除的交易手续费 |
| data[].cashDividend | string |  | 现金派息<br><br>单位为USDT |
| data[].cTime | string |  | 创建时间 时间戳, 毫秒 |
| data[].assetMode | string |  | `single` : 单币种保证金  <br><br>`union` 多币种联合保证金 |
| data[].uTime | string |  | 最近更新时间，时间戳，毫秒 |
| data[].autoMargin | string |  | 自动追加保证金 <br><br>  `on` 自动追加 <br><br> `off` 不自动追加 |
| data[].grant | string |  | 合约空投券金额 |
| data[].takeProfit | string |  | 止盈价格 |
| data[].stopLoss | string |  | 止损价格 |
| data[].takeProfitId | string |  | 止盈订单ID |
| data[].stopLossId | string |  | 止损订单ID |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1768195413808,
  "data": [
    {
      "marginCoin": "USDT",
      "symbol": "BTCUSDT",
      "holdSide": "short",
      "openDelegateSize": "0",
      "marginSize": "32.9182142857142858",
      "available": "0.005",
      "locked": "0",
      "total": "0.005",
      "leverage": "14",
      "achievedProfits": "-48.1989666666666705",
      "openPriceAvg": "88505.233333333333",
      "marginMode": "crossed",
      "posMode": "hedge_mode",
      "unrealizedPL": "-18.328833333333335",
      "liquidationPrice": "17288450.450983311758416",
      "keepMarginRate": "0.004",
      "markPrice": "92171",
      "marginRatio": "0.0030244464835655",
      "breakEvenPrice": "67274.9159193683778732",
      "totalFee": "-56.2349883554",
      "deductedFee": "1.5158073",
      "cashDividend": "0",
      "grant": "",
      "assetMode": "union",
      "autoMargin": "off",
      "takeProfit": null,
      "stopLoss": null,
      "takeProfitId": null,
      "stopLossId": null,
      "cTime": "1766103799183",
      "uTime": "1768194000530"
    }
  ]
}
```

## 获取合约历史持仓列表

`GET /api/v2/mix/position/history-position`

20次/S 根据uid限频

查询历史持仓列表

(只能查询最近3个月的历史持仓数据)

Operation ID: `classicContractPositionGetHistoryPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| symbol | query | string |  | 交易币对 |
| productType | query | string |  | 产品类型，默认`USDT-FUTURES`， 如果传了symbol，则此字段失效<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| idLessThan | query | string |  | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的 endId。 |
| startTime | query | string |  | 开始时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传结束时间，则默认结束时间为三个月。） |
| endTime | query | string |  | 结束时间戳 <br><br>Unix时间戳的毫秒数格式，如 1597026383085<br><br>（时间跨度最大支持三个月，若不传开始时间，则默认开始时间为三个月。） |
| limit | query | string |  | 查询条数 默认20，最大100 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object |  |  |
| data.list | object[] |  | 历史持仓数据 |
| data.list[].positionId | string |  | ID |
| data.list[].symbol | string |  | 币对名称 |
| data.list[].marginCoin | string |  | 保证金币种 |
| data.list[].holdSide | string |  | 持仓方向<br><br>long: 多仓 <br><br>short: 空仓 |
| data.list[].posMode | string |  | 持仓模式<br><br>one_way_mode: 单向持仓 <br><br>hedge_mode: 双向持仓 |
| data.list[].openAvgPrice | string |  | 开仓均价 |
| data.list[].closeAvgPrice | string |  | 平仓均价 |
| data.list[].marginMode | string |  | 保证金模式 <br><br>isolated: 逐仓    <br><br>crossed: 全仓 |
| data.list[].openTotalPos | string |  | 累计开仓数量 |
| data.list[].closeTotalPos | string |  | 累计已平仓数量 |
| data.list[].pnl | string |  | 已实现盈亏 |
| data.list[].netProfit | string |  | 净盈亏<br><br>netProfit = pnl + totalFunding + openFee + closeFee |
| data.list[].totalFunding | string |  | 累计资金费用 |
| data.list[].openFee | string |  | 仓位开仓总手续费 |
| data.list[].closeFee | string |  | 仓位平仓总手续费 |
| data.list[].cashDividend | string |  | 现金派息<br><br>单位为USDT |
| data.list[].utime | string |  | 最近更新时间 |
| data.list[].ctime | string |  | 创建时间 时间戳 毫秒 <br><br>集合中从最新时间开始降序。 |
| data.endId | string |  | 最后的数据id。id值为跟踪单号，用于根据idLessThan查询 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1312312312321,
  "data": {
    "list": [
      {
        "positionId": "xxxxxxxxxxx",
        "marginCoin": "USDT",
        "symbol": "BTCUSDT",
        "holdSide": "long",
        "openAvgPrice": "32000",
        "closeAvgPrice": "32500",
        "marginMode": "isolated",
        "openTotalPos": "0.01",
        "closeTotalPos": "0.01",
        "pnl": "14.1",
        "netProfit": "12.1",
        "totalFunding": "0.1",
        "openFee": "0.01",
        "closeFee": "0.01",
        "cashDividend": "0",
        "posMode": "one_way_mode",
        "ctime": "1988824171000",
        "utime": "1988824171000"
      }
    ],
    "endId": "23423432423423234"
  }
}
```

## 获取合约仓位ADL排名列表

`GET /api/v2/mix/position/adlRank`

5次/S 根据uid限频

查询合约持仓的当前仓位的ADL排名列表

Operation ID: `classicContractPositionGetPositionAdl`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | 产品类型，默认`USDT-FUTURES`， <br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名称 |
| data[].marginCoin | string |  | 保证金币种 |
| data[].adlRank (已过时) | string |  | 当前仓位在自动减仓序列中的排序。当市场发生自动减仓事件时，值越靠前，您的持仓被减少的概率越大。 |
| data[].rank | string |  | 当前仓位在自动减仓序列中的排序。当市场发生自动减仓事件时，值越接近1 越容易被adl。 |
| data[].holdSide | string |  | 持仓方向<br><br>long: 多仓 <br><br>short: 空仓 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1753775486724,
  "data": [
    {
      "symbol": "MOVEUSDT",
      "marginCoin": "USDT",
      "adlRank": "0.2248",
      "rank": "0.7752",
      "holdSide": "long"
    }
  ]
}
```

## 获取全部合约仓位信息

`GET /api/v2/mix/position/all-position`

限频规则：5次/秒/UID

返回指定productType当前全部的持仓信息

Operation ID: `classicContractPositionGetAllPosition`

### 参数

| 名称 | 位置 | 类型 | 必填 | 说明 |
|---|---|---|---|---|
| productType | query | string | 是 | 产品类型<br><br>`USDT-FUTURES` U本位合约<br><br>`COIN-FUTURES` 币本位合约<br><br>`USDC-FUTURES` USDC合约 |
| marginCoin | query | string |  | 保证金币种，必须大写，例如USDT |

### 响应 200：Successful response

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| code | string |  |  |
| msg | string |  |  |
| requestTime | integer |  |  |
| data | object[] |  |  |
| data[].symbol | string |  | 币对名称 |
| data[].marginCoin | string |  | 保证金币种 |
| data[].holdSide | string |  | 持仓方向<br><br>`long`: 多仓<br><br>`short`: 空仓 |
| data[].openDelegateSize | string |  | 当前委托待成交的数量(基础币) |
| data[].marginSize | string |  | 保证金数量 (保证金币种) |
| data[].available | string |  | 仓位可用(基础币) |
| data[].locked | string |  | 仓位冻结(基础币) |
| data[].total | string |  | 仓位总数量(available + locked) |
| data[].leverage | string |  | 杠杆倍数 |
| data[].achievedProfits | string |  | 已实现盈亏（不包含资金费用和手续费） |
| data[].openPriceAvg | string |  | 平均开仓价 |
| data[].marginMode | string |  | 保证金模式<br><br>`crossed`:全仓<br><br>`isolated`: 逐仓 |
| data[].posMode | string |  | 持仓模式<br><br>`one_way_mode` 单向持仓<br><br>`hedge_mode` 双向持仓 |
| data[].unrealizedPL | string |  | 未实现盈亏 |
| data[].liquidationPrice | string |  | 预估强平价<br><br>小于等于0，代表永不爆仓 |
| data[].keepMarginRate | string |  | 仓位档位维持保证金率 |
| data[].markPrice | string |  | 标记价格 |
| data[].marginRatio | string |  | 维持保证金率（0.1代表10%） |
| data[].breakEvenPrice | string |  | 仓位盈亏平衡价 |
| data[].totalFee | string |  | 资金费用，仓位存续期间，资金费用的累加值,初始值为空，表示还没收取过资金费 |
| data[].takeProfit | string |  | 止盈价格 |
| data[].stopLoss | string |  | 止损价格 |
| data[].takeProfitId | string |  | 止盈订单ID |
| data[].stopLossId | string |  | 止损订单ID |
| data[].deductedFee | string |  | 已扣手续费，仓位存续期间扣除的交易手续费 |
| data[].cashDividend | string |  | 现金派息<br><br>单位为USDT |
| data[].cTime | string |  | 创建时间 时间戳 毫秒 <br><br>集合中从最新时间开始降序。 |
| data[].assetMode | string |  | `single` : 单币种保证金  <br><br>`union`：多币种联合保证金 |
| data[].autoMargin | string |  | 自动追加保证金 <br><br>`on` 开启自动追加保证金 <br><br>`off` 关闭自动追加保证金 |
| data[].uTime | string |  | 最近更新时间 时间戳 毫秒 |
| data[].grant | string |  | 合约空投券金额 |

```json
{
  "code": "00000",
  "msg": "success",
  "requestTime": 1767685381615,
  "data": [
    {
      "marginCoin": "USDT",
      "symbol": "BTCUSDT",
      "holdSide": "short",
      "openDelegateSize": "0",
      "marginSize": "103.1894785714285715",
      "available": "0.0155",
      "locked": "0",
      "total": "0.0155",
      "leverage": "14",
      "achievedProfits": "8.605233333333333",
      "openPriceAvg": "88505.233333333333",
      "marginMode": "crossed",
      "posMode": "hedge_mode",
      "unrealizedPL": "-72.8215833333333385",
      "liquidationPrice": "5737867.8639926850760812",
      "keepMarginRate": "0.004",
      "markPrice": "93203.4",
      "marginRatio": "0.0028541392311979",
      "breakEvenPrice": "85283.0669339944416898",
      "totalFee": "-56.8315381906",
      "deductedFee": "0.92414181",
      "cashDividend": "0",
      "grant": "",
      "assetMode": "union",
      "autoMargin": "off",
      "takeProfit": "",
      "stopLoss": "",
      "takeProfitId": "",
      "stopLossId": "",
      "cTime": "1766103799183",
      "uTime": "1767682800537"
    }
  ]
}
```