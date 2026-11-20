---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/private/Plan-Order-Channel
api_type: WebSocket
updated_at: 2026-11-20 19:00:50.338285
---

# Trigger Order Channel

### Description

Subscribe trigger order channel

Data will be pushed when the trigger plans are opened,cancelled,modified,triggered.

<div className="api-aligning">

```json title="Request Example"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "orders-algo",
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
| &gt; channel | String | Yes | Channel name:`orders-algo`                                                                                          |
| &gt; instType | String | Yes | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; instId | String | No | Trading pair                                                                                                        |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Response Example"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "orders-algo",
        "instId": "default"
    }
}
```

### Response Parameters

| Parameter | Type | Description                                                                                                         | 
| :---- | :---- |:--------------------------------------------------------------------------------------------------------------------|
| event | String | Event                                                                                                               |
| arg | Object | Subscribed channels                                                                                                 |
| &gt; channel | String | Channel name: orders-algo                                                                                           |
| &gt; instType | String | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures  |
| &gt; instId | String | Product ID                                                                                                          |
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
        "channel": "orders-algo",
        "instId": "default"
    },
    "data": [
        {
            "instId": "BTCUSDT",
            "orderId": "1",
            "clientOid": "1",
            "triggerPrice": "27000.000000000",
            "triggerType": "fill_price",
            "triggerTime": "1695719197612",
            "planType": "pl",
            "price": "27000.000000000",
            "executePrice": "27000.000000000",
            "size": "0.020000000",
            "actualSize": "0.000000000",
            "orderType": "market",
            "side": "buy",
            "tradeSide": "open",
            "posSide": "long",
            "marginCoin": "USDT",
            "status": "live",
            "posMode": "hedge_mode",
            "enterPointSource": "web",
            "stopSurplusTriggerType": "fill_price",
            "stopLossTriggerType": "fill_price",
            "stpMode": "cancel_taker",
            "cTime": "1695719197612",
            "uTime": "1695719197612"
        }
    ],
    "ts": 1695719197733
}
```

### Push Parameters

| Parameter | Type | Description                                                                                                                                                                                                                                                                                                                                    | 
| :---- | :---- |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| action | String | Push action                                                                                                                                                                                                                                                                                                                                    |
| arg | Object | Channels with successful subscription                                                                                                                                                                                                                                                                                                          |
| &gt; channel | String | Channel name: orders-algo                                                                                                                                                                                                                                                                                                                      |
| &gt; instType | String | Product type<br/>`USDT-FUTURES` USDT-M Futures<br/>`COIN-FUTURES` Coin-M Futures<br/>`USDC-FUTURES` USDC-M Futures                                                                                                                                                                                                                             |
| &gt; instId | String | Product ID<br/>delivery contract reference：https://www.bitget.com/api-doc/common/release-note                                                                                                                                                                                                                                                  |
| data | List&lt;Object&gt; | Subscription data                                                                                                                                                                                                                                                                                                                              |
| &gt; instId | String | Product ID<br/>delivery contract reference：https://www.bitget.com/api-doc/common/release-note                                                                                                                                                                                                                                                  |
| &gt; orderId | String | Bot order ID                                                                                                                                                                                                                                                                                                                                   |
| &gt; clientOid | String | Customized bot order ID                                                                                                                                                                                                                                                                                                                        |
| &gt; triggerPrice | String | Trigger price                                                                                                                                                                                                                                                                                                                                  |
| &gt; triggerType | String | Trigger type<br/>fill_price: filled price<br/>mark_price: mark price                                                                                                                                                                                                                                                                           |
| &gt; triggerTime | String | Trigger time, ms                                                                                                                                                                                                                                                                                                                               |
| &gt; planType | String | Websocket trigger order type. Data will be pushed when modify,cancel,open,triggered the plan types below<br/>`pl`:Default value, trigger order<br/>`tp`:Partial take profit<br/>`sl`:Partial stop loss<br/>`ptp`:Position take profit<br/>`psl`:Position stop loss<br/>`track`:Trailing stop<br/>`mtpsl`:Trailing TP/SL                        |
| &gt; price | String | Order price                                                                                                                                                                                                                                                                                                                                    |
| &gt; executePrice | String | Execute price                                                                                                                                                                                                                                                                                                                                  |
| &gt; size | String | Original order amount in coin                                                                                                                                                                                                                                                                                                                  |
| &gt; actualSize | String | Actual number of orders in coin                                                                                                                                                                                                                                                                                                                |
| &gt; orderType | String | Order type<br/>limit: limit order<br/>market                                                                                                                                                                                                                                                                                                   |
| &gt; side | String | Order direction,                                                                                                                                                                                                                                                                                                                               |
| &gt; tradeSide | String | Trade Side trading direction                                                                                                                                                                                                                                                                                                                   |
| &gt; posSide | String | Position direction;                                                                                                                                                                                                                                                                                                                            |
| &gt; marginCoin | String | Margin coin                                                                                                                                                                                                                                                                                                                                    |
| &gt; status | String | Order status<br/>`live`: plan order created<br/>`executed`: executed<br/>`fail_execute`: execute failed<br/>`cancelled`: cancelled<br/>`executing`: executing                                                                                                                                                                                  |
| &gt; posMode | String | Position mode<br/>`one_way_mode`: one-way position mode<br/>`hedge_mode`: hedge postion mode                                                                                                                                                                                                                                                   |
| &gt; enterPointSource | String | Order source<br/>WEB: Orders created on the website<br/>API: Orders created on API<br/>SYS: System managed orders, usually generated by forced liquidation logic<br/>ANDROID: Orders created on the Android app<br/>IOS: Orders created on the iOS app                                                                                         |
| &gt; stopSurplusPrice | String | Preset/Partial/Position position take-profit execution price;<br/> 1. When planType is pl, it represents the preset take-profit execution price.<br/>2. When planType is tp, it represents the partial take-profit execution price.<br/>3. When planType is ptp, it represents the position take-profit execution price.                       |
| &gt; stopSurplusTriggerPrice | String | Preset/Partial/Position take-profit trigger price;<br/> 1. When planType is pl, it represents the preset take-profit trigger price.<br/>2. When planType is tp, it represents the partial take-profit trigger price.<br/>3. When planType is ptp, it represents the position take-profit trigger price.<br/>It is empty when there is nothing. |
| &gt; stopSurplusTriggerType | String | Preset/Partial/Position take-profit trigger type;<br/> 1. When planType is pl, it represents the preset take-profit trigger type.<br/>2. When planType is tp, it represents the partial take-profit trigger type.<br/>3. When planType is ptp, it represents the position take-profit trigger type.<br/>It is empty when there is nothing.     |
| &gt; stopLossPrice | String | Preset/Partial/Position stop-loss execution price;<br/> 1. When planType is pl, it represents the preset stop-loss execution price.<br/>2. When planType is sl, it represents the partial stop-loss execution price.<br/>3. When planType is psl, it represents the position stop-loss execution price.<br/>It is empty when there is nothing. |
| &gt; stopLossTriggerPrice | String | Preset/Partial/Position stop-loss trigger price;<br/> 1. When planType is pl, it represents the preset stop-loss trigger price.<br/>2. When planType is sl, it represents the partial stop-loss trigger price.<br/>3. When planType is psl, it represents the position stop-loss trigger price.                                                |
| &gt; stopLossTriggerType | String | Preset/Partial/Position stop-loss trigger type;<br/> 1. When planType is pl, it represents the preset stop-loss trigger type.<br/> 2. When planType is sl, it represents the partial stop-loss trigger type.<br/>3. When planType is psl, it represents the position stop-loss trigger type.<br/>It is empty when there is nothing.            |
| &gt; uTime | String | Order update time, Milliseconds format of updated data timestamp Unix, e.g. 1597026383085                                                                                                                                                                                                                                                      |
| &gt; stpMode          | String             | STP Mode <br/> `none` not setting STP <br/> `cancel_taker` cancel taker order <br/>  `cancel_maker` cancel maker order <br/>  `cancel_both` cancel both of taker and maker orders                                                                                                                                                              |

</div>

---

# 计划委托频道

### 描述

订阅计划委托

当新增，修改，撤销，触发委托时，数据将会被推送。

<div className="api-aligning">

```json title="请求示例"
{
    "op": "subscribe",
    "args": [
        {
            "instType": "USDT-FUTURES",
            "channel": "orders-algo",
            "instId": "default"
        }
    ]
}
```

### 请求参数

| 参数名 | 参数类型 | 是否必须 | 描述                                                                                | 
| :---- | :---- | :---- |:----------------------------------------------------------------------------------|
| op | String | 是 | 操作, subscribe unsubscribe                                                         |
| args | List&lt;Object&gt; | 是 | 请求订阅的频道列表                                                                         |
| &gt; channel | String | 是 | 频道名:`orders-algo`                                                                 |
| &gt; instType | String | 是 | 产品类型<br/>`USDT-FUTURES` U本位合约<br/>`COIN-FUTURES` 币本位合约<br/>`USDC-FUTURES` USDC合约  |
| &gt; instId | String | 否 | 交易对，交割合约参考：https://www.bitget.com/zh-CN/api-doc/common/release-note               |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="订阅返回示例"
{
    "event": "subscribe",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "orders-algo",
        "instId": "default"
    }
}
```

### 返回参数

| 返回字段 | 参数类型 | 字段说明 | 
| :---- | :---- | :---- |
| event | String | 事件 |
| arg | Object | 订阅的频道 |
| &gt; channel | String | 频道名 |
| &gt; instType | String | 产品类型  |
| &gt; instId | String |产品ID |
| code | String | 错误码 |
| msg | String | 错误消息 |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="推送返回示例"
{
    "action": "snapshot",
    "arg": {
        "instType": "USDT-FUTURES",
        "channel": "orders-algo",
        "instId": "default"
    },
    "data": [
        {
            "instId": "BTCUSDT",
            "orderId": "1",
            "clientOid": "1",
            "triggerPrice": "27000.000000000",
            "triggerType": "fill_price",
            "triggerTime": "1695719197612",
            "planType": "pl",
            "price": "27000.000000000",
            "executePrice": "27000.000000000",
            "size": "0.020000000",
            "actualSize": "0.000000000",
            "orderType": "market",
            "side": "buy",
            "tradeSide": "open",
            "posSide": "long",
            "marginCoin": "USDT",
            "status": "live",
            "posMode": "hedge_mode",
            "enterPointSource": "web",
            "stopSurplusTriggerType": "fill_price",
            "stopLossTriggerType": "fill_price",
            "stpMode": "cancel_taker",
            "cTime": "1695719197612",
            "uTime": "1695719197612"
        }
    ],
    "ts": 1695719197733
}
```

### 推送数据参数

| 返回字段 | 参数类型 | 字段说明                                                                                                                                               | 
|:---- |:---- |:---------------------------------------------------------------------------------------------------------------------------------------------------|
| action | String | 推送动作                                                                                                                                               |
| arg | Object | 订阅成功的频道                                                                                                                                            |
| &gt; channel | String | 频道名                                                                                                                                                |
| &gt; instType | String | 产品类型                                                                                                                                               |
| &gt; instId | String | 产品ID                                                                                                                                               |
| data | List&lt;Object&gt; | 订阅的数据                                                                                                                                              |
| &gt; instId | String | 产品ID                                                                                                                                               |
| &gt; orderId | String | 策略订单ID                                                                                                                                             |
| &gt; clientOid | String | 自定义策略订单id                                                                                                                                          |
| &gt; triggerPrice | String | 触发价格                                                                                                                                               |
| &gt; triggerType | String | 触发类型<br/>fill_price成交价格<br/>mark_price标记价格                                                                                                         |
| &gt; triggerTime | String | 触发时间, ms                                                                                                                                           |
| &gt; planType | String | 委托类型。新增、修改、撤销、触发以下委托时，推送数据<br/>`pl`: 默认值, 计划委托订单<br/>`tp`: 部分止盈<br/>`sl`: 部分止损<br/>`ptp`: 仓位止盈<br/>`psl`: 仓位止损<br/>`track`:追踪委托<br/>`mtpsl`：移动止盈止损 |
| &gt; price | String | 委托价格                                                                                                                                               |
| &gt; executePrice | String | 执行价格                                                                                                                                               |
| &gt; size | String | 原始委托数量，以币为单位                                                                                                                                       |
| &gt; actualSize | String | 实际委托数量 以币为单位                                                                                                                                       |
| &gt; orderType | String | 订单类型<br/>limit 限价单，<br/>market 市价单                                                                                                                 |
| &gt; side | String | 订单方向，                                                                                                                                              |
| &gt; tradeSide | String | Trade Side 交易方向                                                                                                                                    |
| &gt; posSide | String | 持仓方向；                                                                                                                                              |
| &gt; marginCoin | String | 保证金币种                                                                                                                                              |
| &gt; status | String | 订单状态<br/>`live`：创建订单<br/>`executed`：已执行<br/>`fail_execute`：执行失败<br/>`cancelled`：取消<br/>`executing`：执行中                                             |
| &gt; posMode | String | 持仓模式<br/>one_way_mode 单向持仓<br/>hedge_mode 双向持仓                                                                                                     |
| &gt; enterPointSource | String | 客户端: WEB/API/SYS/ANDROID/IOS                                                                                                                       |
| &gt; stopSurplusPrice | String | 预设/部分/仓位 仓位止盈执行价<br/>1.planType为pl时，代表预设止盈执行价。<br/>2.planType为tp时，代表部分止盈执行价。<br/>3.planType为ptp时，代表仓位止盈执行价。                                        |
| &gt; stopSurplusTriggerPrice | String | 预设/部分/仓位 止盈触发价格<br/>1.planType为pl时，代表预设止盈触发价。<br/>2.planType为tp时，代表部分止盈触发价。<br/>3.planType为ptp时，代表仓位止盈触发价。<br/>没有时为空。                              |
| &gt; stopSurplusTriggerType | String | 预设/部分/仓位 止盈触发类型 <br/> 1.planType为pl时，代表预设止盈触发类型。<br/>2.planType为tp时，代表部分止盈触发类型。<br/>3.planType为ptp时，代表仓位止盈触发类型。<br/>没有时为空。                         |
| &gt; stopLossPrice | String | 预设/部分/仓位 止损执行价<br/>1.planType为pl时，代表预设止损执行价。<br/>2.planType为sl时，代表部分止损执行价。<br/>3.planType为psl时，代表仓位止损执行价。<br/>没有时为空。                               |
| &gt; stopLossTriggerPrice | String | 预设/部分/仓位 止损触发价格<br/>1.planType为pl时，代表预设止损触发价。<br/>2.planType为sl时，代表部分止损触发价。<br/>3.planType为psl时，代表仓位止损触发价。<br/>>stopLossTriggerType                |
| &gt; stopLossTriggerType | String | 预设/部分/仓位 止损触发类型<br/>1.planType为pl时，代表预设止盈触发类型。<br/>2.planType为tp时，代表部分止盈触发类型。<br/>3.planType为ptp时，代表仓位止盈触发类型。<br/>没有时为空。                           |
| &gt; uTime | String | 订单更新时间，Unix时间戳的毫秒数格式，如 1597026383085                                                                                                               |
| &gt; stpMode          | String             | STP模式 <br/> `none` 不设置STP <br/> `cancel_taker` 取消taker单 <br/>  `cancel_maker` 取消maker单 <br/>  `cancel_both` 两者都取消                                  |

</div>