---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/Account-Channel
api_type: WebSocket
updated_at: 2026-11-28 18:59:56.712187
---

# Account Channel

### Description

Data will be pushed when the following events occurred:
1. Push on first-time subscription
2. Push when spot/margin/futures orders are filled in the unified trading account
3. Push when the fund settlement is done
4. Push when balance changes (transfers, airdrops, loans, etc.)

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "account"
        }
    ]
}
```

### Request Parameters

| Parameter    |  Type      | Required | Description                                          | 
|:-----------------|:--------------------|:---------|:-----------------------------------------------------|
| op               | String              | Yes      | Operation <br/> `subscribe`/`unsubscribe`            |
| args             | List&lt;Object&gt;  | Yes      | Subscribed channels                                  |
| &gt; instType    | String              | Yes      | Product Type <br/> `UTA` Unified trading account     |
| &gt; topic       | String              | Yes      | Topic<br/>`account`                                  |


</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "UTA",
        "topic": "account"
    },
    "connId": "xxxxxxxxxx"
}
```

### Response Parameters
| Parameter    |  Type | Description                                                                                         | 
|:----------------|:---------------|:----------------------------------------------------------------------------------------------------|
| event           | String         | Operation <br/> `subscribe` Subscribe <br/> `unsubscribe` Unsubscribe <br/> `error` Parameter Error |
| arg             | Object         | Subscribed Channel                                                                                  |
| &gt; instType  | String         | Product Type <br/> `UTA`                                                                            |
| &gt; topic     | String         | Topic <br/> `account`                                                                        |
| code            | String         | Error Code                                                                                          |
| msg             | String         | Error Message                                                                                       |
| connId          | String         | Connection ID                                                                                       |

</div>


<div className="api-br-10"></div>


<div className="api-aligning">

```json title="Push Data"
{
  "data": [{
    "unrealisedPnL": "-10116.55",
    "totalEquity": "4976919.05",
    "positionMgnRatio": "0",
    "mmr": "408.08",
    "effEquity": "4847952.35",
    "imr": "17795.97",
    "mgnRatio": "0",
    "coin": [{
      "debts": "0",
      "balance": "0.9992",
      "balanceOriginal": "0.9992",
      "available": "0.9992",
      "borrow": "0",
      "locked": "0",
      "equity": "0.9992",
      "coin": "ETH",
      "usdValue": "2488.667472",
      "bonus": "0",
      "collateralLimitStatus": "normal"
    }, {
      "debts": "0",
      "balance": "52.00819",
      "balanceOriginal": "52.00819",
      "available": "52.00819",
      "borrow": "0",
      "locked": "0",
      "equity": "52.00819",
      "coin": "BTC",
      "usdValue": "4630564.31304974",
      "bonus": "0",
      "collateralLimitStatus": "normal"
    }, {
      "debts": "0",
      "balance": "354411.45536458",
      "balanceOriginal": "354411.45536458",
      "available": "344282.65536458",
      "borrow": "0",
      "locked": "0",
      "equity": "344282.65536458",
      "coin": "USDT",
      "usdValue": "343866.07335159",
      "bonus": "10",
      "collateralLimitStatus": "normal"
    }]
  }],
  "arg": {
    "instType": "UTA",
    "topic": "account"
  },
  "action": "snapshot",
  "ts": 1740546523244
}
```

### Push Parameters

| Parameter            | Type   | Description                                                                                                                            |
|----------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------|
| action               | String | Action <br/>`snapshot` Full data <br/>`update` Incremental data                                                                        |
| ts                   | Number | Timestamp                                                                                                                              |
| arg                  | Object | Subscribe channel                                                                                                                      |
| &gt; instType        | String | Product type<br/> `UTA`                                                                                                                |
| &gt; topic           | String | Topic<br/>`account`                                                                                                                    |
| data                 | List   | Subscribed data                                                                                                                        |
| &gt; totalEquity     | String | Account equity (USD)                                                                                                                   |
| &gt; effEquity       | String | Effective margin (USD)<br/> The net value available for margin in spot and perpetual trades under cross-margin mode, converted to fiat |
| &gt; mmr             | String | Maintenance margin (USD) <br/>The minimum margin required to maintain the position, converted to fiat                                  |
| &gt; imr             | String | Initial margin (USD) Total initial margin of assets in base coin, converted to fiat                                                    |
| &gt; mgnRatio        | String | Margin ratio                                                                                                                           |
| &gt;positionMgnRatio | String | Hold position margin ratio                                                                                                             |
| &gt; unrealisedPnL   | String | Unrealised profit and loss                                                                                                             |
| &gt; coin            | List   | Coin list                                                                                                                              |
| &gt;&gt; coin        | String | Coin name                                                                                                                              |
| &gt;&gt; balance     | String | Coin balance (excluding borrowed amount)                                                                                                  |
| &gt;&gt; balanceOriginal | String | Coin balance (including borrowed amount)                                                                               |
| &gt;&gt; locked      | String | Locked amount <br/> _Only applicable for spot order placement_                                                                         |
| &gt;&gt; equity      | String | Coin equity (USD)                                                                                                                      |
| &gt;&gt; usdValue    | String | Coin value (USD)                                                                                                                       |
| &gt;&gt; available   | String | Available balance                                                                                                                      |
| &gt;&gt; borrow      | String | Borrowed amount                                                                                                                        |
| &gt;&gt; debts       | String | Debt <br/> _Only applicable for margin trading_                                                                                        |
| &gt;&gt; bonus       | String | USDT bonus amount                                                                                                                      |
| &gt;&gt; collateralLimitStatus | String | Platform collateral limit status <br/>`normal` Normal <br/>`user_warning` User limit warning: the limit has not been triggered, but this coin is approaching the user's collateral limit <br/>`platform_warning` Platform limit warning: the limit has not been triggered, but this coin is approaching the platform's collateral limit <br/>`user_limited` User limit triggered <br/>`platform_limited` Platform limit triggered <br/>Returns `normal` for coins not under collateral limit management |


</div>

---

# 账户

### 描述
实时接收账户相关的数据更新

以下事件发生时推送数据：
1. 首次订阅,推送
2. 统一账户现货/杠杆/合约委托单成交,推送
3. 资金结算时,推送
4. 改变balance时（划转、空投、借贷等），推送

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "account"
        }
    ]
}
```

### 请求参数说明

| 参数名           | 参数类型               | 是否必须   | 描述                                              | 
|:--------------|:-------------------|:-------|:------------------------------------------------|
| op            | String             | 是      | 操作 <br/> `subscribe` 订阅 <br/>`unsubscribe` 取消订阅 |
| args          | List&lt;Object&gt; | 是      | 请求订阅的频道列表                                       |
| &gt; instType | String             | 是      | 产品类型<br/>`UTA` 统一账户                             |
| &gt; topic    | String             | 是      | 频道名  `account`                                  |


</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "account"
  },
  "connId": "xxxxxxxxxx"
}
```

### 返回参数说明

| 返回字段          | 参数类型     | 字段说明                    | 
|:--------------|:---------|:------------------------|
| event         | String   | 操作  <br/>`subscribe` 订阅 <br/>`unsubscribe` 退订  <br/>`error` 参数错误                    |
| arg           | Object   | 订阅的频道                   |
| &gt; instType | String   | 产品类型<br/>`UTA` 统一账户     |
| &gt; topic    | String   | 频道名 <br/>`account` 账户频道 |
| code          | String   | 错误码                     |
| msg           | String   | 错误消息                    |
| connId        | String   | 连接ID                    |


</div>


<div className="api-br-10"></div>


<div className="api-aligning">

```json title="推送示例"
{
  "data": [{
    "unrealisedPnL": "-10116.55",
    "totalEquity": "4976919.05",
    "positionMgnRatio": "0",
    "mmr": "408.08",
    "effEquity": "4847952.35",
    "imr": "17795.97",
    "mgnRatio": "0",
    "coin": [{
      "debts": "0",
      "balance": "0.9992",
      "balanceOriginal": "0.9992",
      "available": "0.9992",
      "borrow": "0",
      "locked": "0",
      "equity": "0.9992",
      "coin": "ETH",
      "usdValue": "2488.667472",
      "bonus": "0",
      "collateralLimitStatus": "normal"
    }, {
      "debts": "0",
      "balance": "52.00819",
      "balanceOriginal": "52.00819",
      "available": "52.00819",
      "borrow": "0",
      "locked": "0",
      "equity": "52.00819",
      "coin": "BTC",
      "usdValue": "4630564.31304974",
      "bonus": "0",
      "collateralLimitStatus": "normal"
    }, {
      "debts": "0",
      "balance": "354411.45536458",
      "balanceOriginal": "354411.45536458",
      "available": "344282.65536458",
      "borrow": "0",
      "locked": "0",
      "equity": "344282.65536458",
      "coin": "USDT",
      "usdValue": "343866.07335159",
      "bonus": "10",
      "collateralLimitStatus": "normal"
    }]
  }],
  "arg": {
    "instType": "UTA",
    "topic": "account"
  },
  "action": "snapshot",
  "ts": 1740546523244
}
```

### 推送参数说明

| 属性名                  | 类型                 | 描述                                                       |
|----------------------|--------------------|----------------------------------------------------------|
| action               | String             | 推送数据动作<br/>`snapshot`全量 <br/> `update` 增量                |
| ts                   | Number             | 时间戳                                                      |
| arg                  | Object             | 订阅成功频道                                                   |
| &gt; instType        | String             | 产品线类型<br/>`UTA`统一账户                                      |
| &gt; topic           | String             | 频道名<br/>`account`账户频道                                    |
| data                 | List&lt;Object&gt; | 订阅的数据                                                    |
| &gt;totalEquity      | String             | 账户权益，单位为USD                                              |
| &gt;effEquity        | String             | 有效保证金，单位为USD <br/>账户中可为全仓模式下的现货、永续合约交易提供保证金的资产折合成法币价值的净值 |
| &gt;mmr              | String             | 维持保证金，单位为USD <br/>维持当前仓位所需的最低保证金                         |
| &gt;imr              | String             | 初始保证金，单位为USD <br/>账户中所有全仓持仓及挂单的保证金折合成法币价值的净值             |
| &gt;mgnRatio         | String             | 保证金比率                                                    |
| &gt;positionMgnRatio | String             | 持仓保证金比率                                                  |
| &gt;unrealisedPnL    | String             | 未实现盈亏                                                    |
| &gt;coin             | Array              | 资产币种列表                                                   |
| &gt;&gt;coin         | String             | 币种名称                                                     |
| &gt;&gt;balance      | String             | 币种余额（扣除借币）                                         |
| &gt;&gt;balanceOriginal | String          | 币种余额（不扣除借币）                                           |
| &gt;&gt;locked       | String             | 下单占用<br/>仅现货下单场景有值                                       |
| &gt;&gt;equity       | String             | 币种权益                                                     |
| &gt;&gt;usdValue     | String             | 币种美金价值                                                   |
| &gt;&gt;available    | String             | 币种可用                                                     |
| &gt;&gt;borrow       | String             | 借款                                                       |
| &gt;&gt;debts        | String             | 负债<br/>当前币种的已用借贷额度 (仅现货杠杆借贷时)                            |
| &gt;&gt;bonus        | String             | USDT 体验金金额                                                 |
| &gt;&gt;collateralLimitStatus | String   | 平台抵押品限额状态<br/>`normal`正常 <br/>`user_warning`用户限额预警。未触发限额，但该币种已接近用户抵押品限额 <br/>`platform_warning`平台限额预警。未触发限额，但该币种已接近平台抵押品限额 <br/>`user_limited`用户已触发限额 <br/>`platform_limited`平台已触发限额 <br/>未纳入抵押品限额管理的币种返回 `normal` |


</div>