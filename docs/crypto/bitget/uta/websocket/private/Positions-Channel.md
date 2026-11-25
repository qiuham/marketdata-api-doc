---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/websocket/private/Positions-Channel
api_type: WebSocket
updated_at: 2026-11-25 19:02:11.967462
---

# Positions Channel

### Description

Data will be pushed when the following events occur:
1. Push on the first-time subscription
2. Push incremental data when close-position orders are placed in the unified trading account
3. Push incremental data when futures positions are opened in the unified trading account
4. Push incremental data when futures positions are closed in the unified trading account
5. Push incremental data when futures close-position orders are modified in the unified trading account
6. Push incremental data when futures close-position orders are cancelled in the unified trading account


<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "position"
        }
    ]
}
```

### Request Parameters

| Parameters    |  Type         | Description                                                          | 
|:--------------|:-----------------------|:---------------------------------------------------------------------|
| op            | String                 | Operation <br/> `subscribe` Subscribe <br/>`unsubscribe` Unsubscribe |
| args          | List&lt;Object&gt;     | Subscribed channel                                                   |
| &gt; instType | String                 | Product type <br/>`UTA` Unified trading account                      |
| &gt; topic    | String                 | Topic `position` Position                                            |


</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "position"
  },
  "code": "",
  "msg": "",
  "connId": "xxxxxxxxxx"
}
```

### Response Parameters

| Parameters    |  Type   | Description                                                                                            | 
|:--------------|:-----------------|:-------------------------------------------------------------------------------------------------------|
| event         | String           | Operation <br/>`subscribe` Subscription <br/>`unsubscribe` Unsubscription <br/>`error` Parameter error |
| arg           | Object           | Subscribed channel                                                                                     |
| &gt; instType | String           | Product type <br/>`UTA` Unified trading account                                                        |
| &gt; topic    | String           | Topic <br/>`position` Position                                                                         |
| code          | String           | Error code                                                                                             |
| msg           | String           | Error message                                                                                          |
| connId        | String           | Connection ID                                                                                          |

</div>


<div className="api-br-10"></div>

<div className="api-aligning">


```json title="Push Data"
{
  "data": [
    {
      "symbol": "BTCUSDT",
      "leverage": "20",
      "openFeeTotal": "",
      "mmr": "",
      "breakEvenPrice": "",
      "available": "0",
      "liqPrice": "",
      "marginMode": "crossed",
      "unrealisedPnl": "0",
      "markPrice": "94987.1",
      "createdTime": "1736378720620",
      "avgPrice": "0",
      "totalFundingFee": "0",
      "cashDividend": "0",
      "updatedTime": "1736378720620",
      "marginCoin": "USDT",
      "frozen": "0",
      "profitRate": "",
      "closeFeeTotal": "",
      "marginSize": "0",
      "curRealisedPnl": "0",
      "size": "0",
      "positionStatus": "ended",
      "posSide": "long",
      "holdMode": "hedge_mode"
    }
  ],
  "arg": {
    "instType": "UTA",
    "topic": "position"
  },
  "action": "snapshot",
  "ts": 1730711666652
}
```


### Push Parameters

| Parameter            | Type               | Description                                                                                                                                                    |
|----------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| arg                  | Object             | Subscribed channel                                                                                                                                             |
| &gt; instType        | String             | Product type <br/>`UTA` Unified Account                                                                                                                        |
| &gt; topic           | String             | Topic <br/>`position` Position channel                                                                                                                         |
| action               | String             | Action <br/>`snapshot` Full data <br/>`update` Incremental data                                                                                                |
| data                 | List&lt;Object&gt; | Subscribed data                                                                                                                                                |
| &gt; symbol          | String             | Symbol name                                                                                                                                                    |
| &gt; marginCoin      | String             | Margin coin                                                                                                                                                    |
| &gt; marginSize      | String             | Margin size                                                                                                                                                    |
| &gt; marginMode      | String             | Margin mode<br/>`crossed` Cross margin<br/>`isolated` Isolated margin                                                                                          |
| &gt; posSide         | String             | Position side <br/>`long`/`short`                                                                                                                              |
| &gt; holdMode        | String             | Holding mode <br/> `one_way_mode`/`hedge_mode`                                                                                                                 |
| &gt; positionStatus  | String             | Position status <br/> `opening` Ongoing <br/> `ended` Completed                                                                                                |
| &gt; size            | String             | Position size <br/>`size` = `available` + `frozen`                                                                                                             |
| &gt; available       | String             | Available position size                                                                                                                                        |
| &gt; frozen          | String             | Frozen position size                                                                                                                                           |
| &gt; avgPrice        | String             | Average open price                                                                                                                                             |
| &gt; leverage        | String             | Leverage multiple                                                                                                                                              |
| &gt; curRealisedPnl  | String             | Realised PnL                                                                                                                                                   |
| &gt; unrealisedPnl   | String             | Unrealised PnL                                                                                                                                                 |
| &gt; liqPrice        | String             | Estimated liquidation price                                                                                                                                    |
| &gt; mmr             | String             | Maintain margin rate                                                                                                                                           |
| &gt; marginRate      | String             | Margin rate                                                                                                                                                    |
| &gt; markPrice       | String             | Mark Price                                                                                                                                                     |
| &gt; openFeeTotal    | String             | Total opening fee                                                                                                                                              |
| &gt; closeFeeTotal   | String             | Total closing fee                                                                                                                                              |
| &gt; breakEvenPrice  | String             | Break-even price                                                                                                                                               |
| &gt; profitRate      | String             | Profit rate<br/>_Profit rate = Unrealized PnL ÷ Initial margin_<br/>_Initial margin = Average open price × Position size ÷ Leverage ÷ Margin coin index price_ |
| &gt; totalFundingFee | String             | Total funding fee over the position's lifetime<br/> `0` indicates that no funding fee has been charged yet                                                     |
| &gt; cashDividend    | String             | Cash dividend, unit: USDT                                                                                                                                      |
| &gt; createdTime     | String             | Position creation time<br/>A Unix timestamp in milliseconds. e.g.,`1597026383085`                                                                              |
| &gt; updatedTime     | String             | Latest position update time<br/>A Unix timestamp in milliseconds. e.g.,`1597026383085`                                                                         |

## Profit Rate Calculation

**Profit Rate = Unrealized PnL / Initial Margin**

### Initial Margin
**Initial Margin = (Average Open Price × Position Size) / Leverage / Margin Coin Index Price**

</div>

---

# 持仓

### 描述
实时推送用户持仓数据

以下事件发生时推送数据：
1. 首次订阅，推送，全量
2. 统一账户合约平仓委托单下单，推送，增量
3. 统一账户合约开仓委托成交，推送，增量
4. 统一账户合约平仓委托成交，推送，增量
5. 统一账户合约平仓委托单改单，推送，增量
6. 统一账户合约平仓委托单撤单，推送，增量


<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "UTA",
            "topic": "position"
        }
    ]
}
```

### 请求参数

| 参数名           | 参数类型               | 是否必须 | 描述                                               | 
|:--------------|:-------------------|-----|:-------------------------------------------------|
| op            | String             | 是   | 操作: <br/> `subscribe` 订阅 <br/>`unsubscribe` 取消订阅 |
| args          | List&lt;Object&gt; | 是   | 请求订阅的频道列表                                        |
| &gt; instType | String             | 是   | 产品类型<br/>`UTA` 统一账户                                       |
| &gt; topic    | String             | 是   | 频道名: `position` 仓位                               |


</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
  "event": "subscribe",
  "arg": {
    "instType": "UTA",
    "topic": "position"
  },
  "code": "",
  "msg": "",
  "connId": "xxxxxxxxxx"
}
```

### 返回参数说明

| 返回字段          | 参数类型     | 字段说明                                                            | 
|:--------------|:---------|:----------------------------------------------------------------|
| event         | String   | 操作 <br/>`subscribe` 订阅 <br/>`unsubscribe` 退订  <br/>`error` 参数错误 |
| arg           | Object   | 订阅的频道                                                           |
| &gt; instType | String   | 产品类型<br/>`UTA` 统一账户                                             |
| &gt; topic    | String   | 频道名 <br/>`position` 仓位                                          |
| code          | String   | 错误码                                                             |
| msg           | String   | 错误消息                                                            |
| connId        | String   | 连接ID                                                            |


</div>


<div className="api-br-10"></div>

<div className="api-aligning">


```json title="推送示例"
{
  "data": [
    {
      "symbol": "BTCUSDT",
      "leverage": "20",
      "openFeeTotal": "",
      "mmr": "",
      "breakEvenPrice": "",
      "available": "0",
      "liqPrice": "",
      "marginMode": "crossed",
      "unrealisedPnl": "0",
      "markPrice": "94987.1",
      "createdTime": "1736378720620",
      "avgPrice": "0",
      "totalFundingFee": "0",
      "cashDividend": "0",
      "updatedTime": "1736378720620",
      "marginCoin": "USDT",
      "frozen": "0",
      "profitRate": "",
      "closeFeeTotal": "",
      "marginSize": "0",
      "curRealisedPnl": "0",
      "size": "0",
      "positionStatus": "ended",
      "posSide": "long",
      "holdMode": "hedge_mode"
    }
  ],
  "arg": {
    "instType": "UTA",
    "topic": "position"
  },
  "action": "update",
  "ts": 1736378720624
}
```


### 参数说明

| 参数                  | 类型                 | 描述                                                   |
|---------------------|--------------------|------------------------------------------------------|
| arg                 | Object             | 订阅成功频道                                               |
| &gt; instType       | String             | 产品线类型<br/>`UTA`统一账户                                  |
| &gt; topic          | String             | 频道名<br/>`position`仓位频道                               |
| action              | String             | 推送数据动作<br/>`snapshot`全量 <br/> `update` 增量            |
| data                | List&lt;Object&gt; | 订阅的数据                                                |
| &gt;symbol          | String             | 交易对名称                                                |
| &gt;marginCoin      | String             | 保证金币种                                                |
| &gt;marginSize      | String             | 保证金数量                                                |
| &gt;marginMode      | String             | 保证金模式<br/>`crossed` 全仓<br/>`isolated` 逐仓          |
| &gt;posSide         | String             | 持仓方向 <br/>`long` 多 <br/> `short`空                    |
| &gt;holdMode        | String             | 持仓模式 <br/> `one_way_mode`单向持仓 <br/> `hedge_mode`双向持仓 |
| &gt;positionStatus  | String             | 仓位状态 <br/> `opening`进行中 <br/> `ended`完结              |
| &gt;size            | String             | 持仓数量 <br/> `size` = `available` + `frozen`           |
| &gt;available       | String             | 可平仓数量                                                |
| &gt;frozen          | String             | 冻结数量                                                 |
| &gt;avgPrice        | String             | 开仓平均价                                                |
| &gt;leverage        | String             | 杠杆倍数                                                 |
| &gt;curRealisedPnl  | String             | 已实现盈亏 (不包含手续费和资金费用)                                  |
| &gt;unrealisedPnl   | String             | 未实现盈亏                                                |
| &gt;liqPrice        | String             | 预估强平价                                                |
| &gt;mmr             | String             | 维持保证金率                                               |
| &gt;marginRate      | String             | 保证金率                                                 |
| &gt;markPrice       | String             | 标记价格                                                 |
| &gt;openFeeTotal    | String             | 开仓总计手续费                                              |
| &gt;closeFeeTotal   | String             | 平仓总计手续费                                              |
| &gt;breakEvenPrice  | String             | 仓位盈亏平衡价                                              |
| &gt;profitRate      | String             | 收益率                                                  |
| &gt;totalFundingFee | String             | 资金费用  仓位存续期间，资金费用的累加值，初始值为空，表示还没收取过资金费               |
| &gt;cashDividend    | String             | 现金派息，单位：USDT                                         |
| &gt;createdTime     | String             | 持仓创建时间 Unix时间戳的毫秒数格式，如 1597026383085                 |
| &gt;updatedTime     | String             | 最近一次持仓更新时间 Unix时间戳的毫秒数格式，如 1597026383085             |

## 收益率计算公式

收益率的计算公式为：<br/>
回报率=未实现盈亏÷初始保证金，<br/>
初始保证金=开仓均价x持仓数量÷杠杆÷保证金币指数价格


</div>