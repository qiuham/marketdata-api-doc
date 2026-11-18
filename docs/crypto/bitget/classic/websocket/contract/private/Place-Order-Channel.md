---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/websocket/contract/private/Place-Order-Channel
api_type: WebSocket
updated_at: 2026-11-18 18:59:58.904319
---

# Place Order Channel

### Description

- Ignore the `tradeSide` parameter when position mode is in one-way-mode<br/>
- hedge position mode: Open long: `"side"=buy, "tradeSide"=open`; Close long: `"side"=buy, "tradeSide"=close`; Open short: `"side"=sell, "tradeSide"=open`; Close short: `"side"=sell, "tradeSide"=close`; one-way position mode: "side"=buy and sell, tradeSide: ignore；

<div className="api-aligning">

```json title="Request Example"
{
   "args":[
      {
         "channel":"place-order",
         "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
         "instId":"BTCUSDT",
         "instType":"USDT-FUTURES",
         "params":{
            "orderType":"limit",
            "side":"buy",
            "size":"2",
            "tradeSide":"open",
            "price":"501",
            "marginCoin":"USDT",
            "force":"gtc",
            "marginMode":"crossed",
            "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
         }
      }
   ],
   "op":"trade"
}
```

### Request Parameters

| Parameter                       | Type               | Required | Description                                                                                                                                                                                             | 
|:--------------------------------|:-------------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| op                              | String             | Yes        | "trade"                                                                                                                                                                                                 |
| apiCode                         | String             | No       | API rebate identifier                                                                                                                                                                                   |
| args                            | List&lt;Object&gt; | Yes      | List of channels to request subscription                                                                                                                                                                |
| &gt; id                         | String             | Yes      | Unique Identifier<br/>Length&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                                                                                                                     |
| &gt; instType                   | String             | Yes      | Product line type `USDT-FUTURES`                                                                                                                                                                        |
| &gt; instId                     | String             | Yes      | Product ID, e.g. `ETHUSDT`                                                                                                                                                                              |
| &gt; channel                    | String             | Yes      | Channel name, `place-order`                                                                                                                                                                             |
| &gt; params                     | Object             | Yes      |                                                                                                                                                                                                         |
| &gt;&gt; orderType              | String             | Yes        | Order type<br/>`limit`: Limit order<br/>`market`: Market order                                                                                                                                          |
| &gt;&gt; side                   | String             | Yes        | Trade side<br/>`buy`: Buy(one-way-mode); Long position direction(hedge-mode)<br/>`sell`: Sell(one-way-mode); Short position direction(hedge-mode)                                                       |
| &gt;&gt; size                   | String             | Yes        | Amount (base coin)<br/>To get the decimal places of size:Get Contract Config                                                                                                                            |
| &gt;&gt; force                  | String             | Yes        | Execution strategy(It will be invalid when orderType is market) <br/>`gtc`：Normal limit order, good till cancelled<br/>`post_only`：Post only<br/>`fok`：Fill or kill<br/>`ioc`：Immediate or cancel       |
| &gt;&gt; price                  | String             | No        | Limit price<br/>The decimal places of price and the price step can be returned by the Get Symbol Info interface                                                                                         |
| &gt;&gt; clientOid              | String             | No        | Custom order ID                                                                                                                                                                                         |
| &gt;&gt; marginCoin             | String             | Yes        | Margin coin(capitalized)                                                                                                                                                                                |
| &gt;&gt; marginMode             | String             | Yes        | Position mode<br/>`isolated`: isolated margin<br/>`crossed`: crossed margin                                                                                                                             |
| &gt;&gt; tradeSide              | String             | No        | Trade type<br/>Only required in hedge-mode<br/>`open`: Open position<br/>`close`: Close position                                                                                                        |
| &gt;&gt; reduceOnly             | String             | No        | Whether or not to just reduce the position: `YES, NO`<br/>Default: `NO`.<br/>Applicable only in one-way-position mode                                                                                   |
| &gt;&gt; presetStopSurplusPrice | String             | No        | Take-profit value<br/>No take-profit is set if the field is empty.                                                                                                                                      |
| &gt;&gt; presetStopLossPrice    | String             | No        | Stop-loss value<br/>No stop-loss is set if the field is empty.                                                                                                                                          |
| &gt;&gt; stpMode                | String             | No        | STP Mode(Self Trade Prevention)<br/>`none`：not setting STP(default)<br/>`cancel_taker`：cancel taker order<br/>`cancel_maker`：cancel maker order<br/>`cancel_both`：cancel both of taker and maker orders |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="Fail Response Example"
{
  "event":"trade",
  "arg":[
    {
      "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
      "instType":"USDT-FUTURES",
      "channel":"place-order",
      "instId":"BTCUSDT",
      "params":{
        "orderId":"xxxxxxxxxxx",
        "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
      }
    }
  ],
  "code":0,
  "msg":"Success"
}
```

### Response Parameters

| Parameter                       | Type           | Description                                                                                                                                                                                             | 
|:--------------------------------|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| event                           | String         | Event<br/>`trade` <br/>`error`                                                                                                                                                                          |
| arg                             | Object         | Channel                                                                                                                                                                                                 |
| &gt; id                         | String         | Unique Identifier<br/>Length&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                                                                                                                     |
| &gt; instType                   | String         | Product line type `USDT-FUTURES`                                                                                                                                                                        |
| &gt; instId                     | String         | Product ID, e.g. `ETHUSDT`                                                                                                                                                                              |
| &gt; channel                    | String         | Channel name, `place-order`                                                                                                                                                                             |
| &gt; params                     | Object         |                                                                                                                                                                                                         |
| &gt;&gt; orderType              | String         | Order type<br/>`limit`: Limit order<br/>`market`: Market order                                                                                                                                          |
| &gt;&gt; OrderId                | String         | Order ID.                                                                                                                                                                                               |
| &gt;&gt; side                   | String         | Trade side<br/>`buy`: Buy(one-way-mode); Long position direction(hedge-mode)<br/>`sell`: Sell(one-way-mode); Short position direction(hedge-mode)                                                       |
| &gt;&gt; size                   | String         | Amount (base coin)<br/>To get the decimal places of size:Get Contract Config                                                                                                                            |
| &gt;&gt; force                  | String         | Execution strategy(It will be invalid when orderType is market) <br/>`gtc`：Normal limit order, good till cancelled<br/>`post_only`：Post only<br/>`fok`：Fill or kill<br/>`ioc`：Immediate or cancel       |
| &gt;&gt; price                  | String         | Limit price<br/>The decimal places of price and the price step can be returned by the Get Symbol Info interface                                                                                         |
| &gt;&gt; clientOid              | String         | Custom order ID                                                                                                                                                                                         |
| &gt;&gt; marginCoin             | String         | Margin coin(capitalized)                                                                                                                                                                                |
| &gt;&gt; marginMode             | String         | Position mode<br/>`isolated`: isolated margin<br/>`crossed`: crossed margin                                                                                                                             |
| &gt;&gt; tradeSide              | String         | Trade type<br/>Only required in hedge-mode<br/>`open`: Open position<br/>`close`: Close position                                                                                                        |
| &gt;&gt; reduceOnly             | String         | Whether or not to just reduce the position: `YES, NO`<br/>Default: `NO`.<br/>Applicable only in one-way-position mode                                                                                   |
| &gt;&gt; presetStopSurplusPrice | String         | Take-profit value<br/>No take-profit is set if the field is empty.                                                                                                                                      |
| &gt;&gt; presetStopLossPrice    | String         | Stop-loss value<br/>No stop-loss is set if the field is empty.                                                                                                                                          |
| &gt;&gt; stpMode                | String         | STP Mode(Self Trade Prevention)<br/>`none`：not setting STP(default)<br/>`cancel_taker`：cancel taker order<br/>`cancel_maker`：cancel maker order<br/>`cancel_both`：cancel both of taker and maker orders |
| code                            | String         | code                                                                                                                                                                                                    |
| msg                             | String         | msg                                                                                                                                                                                                     |

</div>

---

# 下单频道

### 描述

- 单向持仓时，必须省略`tradeSide`参数；<br/>
- 双向持仓时，开多规则为：`side=buy,tradeSide=open`；开空规则为：`side=sell,tradeSide=open`；平多规则为：`side=buy,tradeSide=close`；平空规则为：`side=sell,tradeSide=close`；

<div className="api-aligning">

```json title="请求示例"
{
   "args":[
      {
         "channel":"place-order",
         "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
         "instId":"BTCUSDT",
         "instType":"USDT-FUTURES",
         "params":{
            "orderType":"limit",
            "side":"buy",
            "size":"2",
            "tradeSide":"open",
            "price":"501",
            "marginCoin":"USDT",
            "force":"gtc",
            "marginMode":"crossed",
            "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
         }
      }
   ],
   "op":"trade"
}
```

### 请求参数

| 参数名                             | 参数类型               | 是否必须 | 描述                                                                                                                                              | 
|:--------------------------------|:-------------------|:-----|:------------------------------------------------------------------------------------------------------------------------------------------------|
| op                              | String             | 是    | "trade"                                                                                                                                         |
| apiCode                         | String             | 否    | API返佣标识                                                                                                                                         |
| args                            | List&lt;Object&gt; | 是    | 请求参数列表                                                                                                                                          |
| &gt; id                         | String             | 是    | 用户标识请求与返回<br/>长度&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                                                                         |
| &gt; instType                   | String             | 是    | 产品类型 `USDT-FUTURES`                                                                                                                             |
| &gt; instId                     | String             | 是    | 产品ID, 例如：`ETHUSDT`                                                                                                                              |
| &gt; channel                    | String             | 是    | 频道名, `place-order`                                                                                                                              |
| &gt; params                     | Object             | 是    |                                                                                                                                                 |
| &gt;&gt; orderType              | String             | 是    | 订单类型<br/>`limit`: 限价<br/>`market`: 市价                                                                                                           |
| &gt;&gt; side                   | String             | 是    | 交易方向<br/>`buy`: 单向持仓时代表买入，双向持仓时代表多头方向<br/>`sell`: 单向持仓时代表卖出，双向持仓时代表空头方向                                                                         |
| &gt;&gt; size                   | String             | 是    | 下单数量(基础币)<br/>数量小数位可以通过获取合约信息 接口获取                                                                                                              |
| &gt;&gt; force                  | String             | 是    | 订单有效期<br/>`gtc`：普通限价单，一直有效直至取消<br/>`post_only`：只做 maker 订单<br/>`fok`：全部成交或立即取消<br/>`ioc`：立即成交并取消剩余 <br/> `orderType`为`limit`限价单时必填，若省略则默认为`gtc` |
| &gt;&gt; price                  | String             | 否    | 下单价格<br/>`orderType`为`limit`时必填<br/>价格小数位可以通过获取合约信息 接口获取                                                                                        |
| &gt;&gt; clientOid              | String             | 否    | 自定义订单ID                                                                                                                                         |
| &gt;&gt; marginCoin             | String             | 是    | 保证金币种(大写), 如:USDT                                                                                                                               |
| &gt;&gt; marginMode             | String             | 是    | 仓位模式<br/>`isolated`: 逐仓<br/>`crossed`: 全仓                                                                                                       |
| &gt;&gt; tradeSide              | String             | 否    | 交易类型(仅限双向持仓)<br/>双向持仓模式下必填，单向持仓时不要填，否则会报错<br/>`open`: 开仓<br/>`close`: 平仓                                                                        |
| &gt;&gt; reduceOnly             | String             | 否    | 只减仓(仅适用单向持仓模式下)<br/>`YES`<br/>`NO`(默认)                                                                                                          |
| &gt;&gt; presetStopSurplusPrice | String             | 否    | 预设止盈值<br/>为空则默认不设止盈                                                                                                                             |
| &gt;&gt; presetStopLossPrice    | String             | 否    | 预设止损值<br/>为空则默认不设止损                                                                                                                             |
| &gt;&gt; stpMode                | String             | 否    | STP（自成交预防）模式<br/>`none`：不设置STP（默认值）<br/>`cancel_taker`：取消taker单<br/>`cancel_maker`：取消maker单<br/>`cancel_both`：两者都取消                             |

</div>

<div className="api-br-10"></div>

<div className="api-aligning">

```json title="响应示例"
{
  "event":"trade",
  "arg":[
    {
      "id":"xxxxx-xxx-xxx-xxxx-xxxxxx",
      "instType":"USDT-FUTURES",
      "channel":"place-order",
      "instId":"BTCUSDT",
      "params":{
        "orderId":"xxxxxxxxxxx",
        "clientOid":"xxxxx-xxx-xxx-xxxx-xxxxxx"
      }
    }
  ],
  "code":0,
  "msg":"Success"
}
```

### 响应参数

| 返回字段                            | 参数类型        | 字段说明                                                                                                                                            | 
|:--------------------------------|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| event                           | String      | 事件<br/>`trade` 交易<br/>`error`参数错误                                                                                                               |
| arg                             | Object      | 订阅成功的频道                                                                                                                                         |
| &gt; id                         | String      | 用户标识请求与返回<br/>长度&lt;= 40<br/>("^[0-9A-Za-z_:#\\-+\\s]*$");                                                                                         |
| &gt; instType                   | String      | 产品类型 `USDT-FUTURES`                                                                                                                             |
| &gt; instId                     | String      | 产品ID, 例如：`ETHUSDT`                                                                                                                              |
| &gt; channel                    | String      | 频道名, `place-order`                                                                                                                              |
| &gt; params                     | Object      |                                                                                                                                                 |
| &gt;&gt; orderId                | String      | 订单ID                                                                                                                                            |
| &gt;&gt; clientOid              | String      | 自定义订单ID                                                                                                                                         |
| &gt;&gt; orderType              | String      | 订单类型<br/>`limit`: 限价<br/>`market`: 市价                                                                                                           |
| &gt;&gt; side                   | String      | 交易方向<br/>`buy`: 单向持仓时代表买入，双向持仓时代表多头方向<br/>`sell`: 单向持仓时代表卖出，双向持仓时代表空头方向                                                                         |
| &gt;&gt; size                   | String      | 下单数量(基础币)<br/>数量小数位可以通过获取合约信息 接口获取                                                                                                              |
| &gt;&gt; force                  | String      | 订单有效期<br/>`gtc`：普通限价单，一直有效直至取消<br/>`post_only`：只做 maker 订单<br/>`fok`：全部成交或立即取消<br/>`ioc`：立即成交并取消剩余 <br/> `orderType`为`limit`限价单时必填，若省略则默认为`gtc` |
| &gt;&gt; price                  | String      | 下单价格<br/>`orderType`为`limit`时必填<br/>价格小数位可以通过获取合约信息 接口获取                                                                                        |
| &gt;&gt; marginCoin             | String      | 保证金币种(大写), 如:USDT                                                                                                                               |
| &gt;&gt; marginMode             | String      | 仓位模式<br/>`isolated`: 逐仓<br/>`crossed`: 全仓                                                                                                       |
| &gt;&gt; tradeSide              | String      | 交易类型(仅限双向持仓)<br/>双向持仓模式下必填，单向持仓时不要填，否则会报错<br/>`open`: 开仓<br/>`close`: 平仓                                                                        |
| &gt;&gt; reduceOnly             | String      | 只减仓(仅适用单向持仓模式下)<br/>`YES`<br/>`NO`(默认)                                                                                                          |
| &gt;&gt; presetStopSurplusPrice | String      | 预设止盈值<br/>为空则默认不设止盈                                                                                                                             |
| &gt;&gt; presetStopLossPrice    | String      | 预设止损值<br/>为空则默认不设止损                                                                                                                             |
| &gt;&gt; stpMode                | String      | STP（自成交预防）模式<br/>`none`：不设置STP（默认值）<br/>`cancel_taker`：取消taker单<br/>`cancel_maker`：取消maker单<br/>`cancel_both`：两者都取消                             |
| code                            | String      | 状态码                                                                                                                                             |
| msg                             | String      | 状态消息                                                                                                                                            |

</div>