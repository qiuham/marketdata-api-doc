---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-portfolio-margin-pro/user-data-streams
api_type: REST
updated_at: 2026-11-13 20:28:22.202983
---

# User Data Streams

## Connect

  * The websocket base url is: **wss://fstream.binance.com/pm-classic**
  * User Data Streams are accessed at **/ws/**
  * Example: `wss://fstream.binance.com/pm-classic/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`
  * The `listenKey` is generated using `POST /fapi/v1/listenKey`.



* * *

## Event: Risk Level Change

### Description

  * When the user's position risk ratio is too high, this stream will be pushed.
  * This message is only used as risk guidance information and is not recommended for investment strategies.
  * `riskLevelChange` includes following types: `NORMAL`, `MARGIN_CALL`, `REDUCE_ONLY`, `FORCE_LIQUIDATION`
  * In the case of a highly volatile market, there may be the possibility that the user's position has been liquidated at the same time when this stream is pushed out.



### Event Name

`riskLevelChange`

### Payload

> **Schema:** [`risklevelchange`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/ws-streams/~schemas#risklevelchange)

Loading schema...

* * *

## Event: PM Pro Account Update

### Description

  * The stream is pushed every 5 seconds with account asset status.



### Event Name

`PM_PRO_ACCOUNT_UPDATE`

### Payload

> **Schema:** [`pmProAccountUpdate`](/en/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/ws-streams/~schemas#pmproaccountupdate)

Loading schema...

Was this page helpful?

Last modified on November 12, 2026

[General Info](/en/docs/products/derivatives-trading-portfolio-margin-pro/general-info)[Error Codes](/en/docs/products/derivatives-trading-portfolio-margin-pro/error-code)

---

# 统一账户专业版账户信息推送

## 连接

  * Websocket的base url是: **wss://fstream.binance.com/pm-classic**
  * 订阅账户数据流的stream名称为 **/ws/**
  * 连接样例: `wss://fstream.binance.com/pm-classic/ws/XaEAKTsQSRLZAGH9tuIu37plSRsdjmlAVBoNYPUITlTAko1WI22PgmBMpI1rS8Yh`
  * `listenKey` 通过 `POST /fapi/v1/listenKey` 生成。



* * *

## 账户风险状态变动

### 事件描述

  * 当用户持仓风险过高，会推送此消息。
  * 此消息仅作为风险指导信息，不建议用于投资策略。
  * `riskLevelChange`包含如下事件：`NORMAL`, `MARGIN_CALL`, `REDUCE_ONLY`, `FORCE_LIQUIDATION`
  * 在大波动市场行情下，不排除此消息发出的同时用户仓位已被强平的可能。



### 事件类型

`riskLevelChange`

### Payload

> **Schema:** [`risklevelchange`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/ws-streams/~schemas#risklevelchange)

Loading schema...

* * *

## 账户资产状态变动

### 事件描述

  * 每 5 秒推送一次账户资产状态。



### 事件类型

`PM_PRO_ACCOUNT_UPDATE`

### Payload

> **Schema:** [`pmProAccountUpdate`](/zh-CN/docs/catalog/advanced-trading-derivatives-trading-portfolio-margin-pro/api/ws-streams/~schemas#pmproaccountupdate)

Loading schema...

此页面是否有帮助？

Last modified on November 12, 2026

[基本信息](/zh-CN/docs/products/derivatives-trading-portfolio-margin-pro/general-info)[错误代码](/zh-CN/docs/products/derivatives-trading-portfolio-margin-pro/error-code)