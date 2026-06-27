---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/demo-mode
api_type: REST
updated_at: 2026-05-27 18:53:42.136744
---

# CHANGELOG for Binance SPOT Demo Mode

**Last Updated: 2026-05-11**

### 2026-05-11[​](/docs/binance-spot-api-docs/demo-mode#2026-05-11 "Direct link to 2026-05-11")

The following rollout will occur at **approximately 07:00 UTC on 2026-05-12**.

  * Added WebSocket Stream support for [Block Trades](https://www.binance.info/en/support/faq/detail/557f95eaf8fb4460aed0a891d42a1425). 
    * New stream: 
      * `<symbol>@blockTrade`



* * *

### 2026-03-12[​](/docs/binance-spot-api-docs/demo-mode#2026-03-12 "Direct link to 2026-03-12")

**Notice:** FIX TLS Connectivity Update on **2026-06-08** , starting from **03:00 UTC** and will take about 1 hour to complete.

**Action Required:**

During the update window, existing FIX connections may drop intermittently. To ensure successful reconnections and new connections afterward, please verify before our update that your client sends SNI (Server Name Indication) during the TLS handshake and validates the certificate against the requested hostname.   
Clients without SNI may receive an error message during handshake related to incorrect certificate during or after the update window, leading to TLS handshake or hostname verification failures. This can occur with some Node.js clients if SNI is not explicitly configured.  
Please consult the [FIX API documentation](/docs/binance-spot-api-docs/fix-api#general-api-information) for full context.

* * *

### 2026-03-09[​](/docs/binance-spot-api-docs/demo-mode#2026-03-09 "Direct link to 2026-03-09")

Scheduled downtime maintenance will begin at **2026-03-13 06:00 UTC** and will last for approximately 4 hours.

* * *

### 2026-01-29[​](/docs/binance-spot-api-docs/demo-mode#2026-01-29 "Direct link to 2026-01-29")

This changelog will announce any scheduled downtime for maintenance for the SPOT Demo Mode environment.

For more information on how to use Demo Mode via API, please refer to the [General Info](/docs/binance-spot-api-docs/demo-mode/general-info) page.

---

# Binance 现货模拟交易 更新日志

**最近更新：2026-05-11**

### 2026-05-11[​](/docs/zh-CN/binance-spot-api-docs/demo-mode#2026-05-11 "2026-05-11的直接链接")

**注意：以下变更将于 2026 年 05 月 12 日 07:00 (UTC) 左右发生** 。

  * 新增对 [大宗交易](https://www.binance.info/zh-CN/support/faq/detail/557f95eaf8fb4460aed0a891d42a1425) 的 WebSocket 行情接口支持。 
    * 新 Stream: 
      * `<symbol>@blockTrade`



* * *

### 2026-03-12[​](/docs/zh-CN/binance-spot-api-docs/demo-mode#2026-03-12 "2026-03-12的直接链接")

**通知：** FIX TLS 连接更新将于 **2026-06-08** ，从 **03:00 UTC** 开始，预计耗时约 1 小时完成。

**请注意及时处理：**

  * 在更新期间，现有的 FIX 连接可能会间歇性断开。为确保更新后能够成功重新连接和建立新连接，请在我们更新之前确认您的客户端在 TLS 握手过程中发送了 SNI（服务器名称指示）并且对目标主机名进行了证书验证。
  * 未发送 SNI 的客户端可能会在更新期间或之后收到证书错误的消息，导致 TLS 握手或主机名验证失败。这种情况可能发生在某些未配置 SNI 的 Node.js 客户端上。
  * 请查阅 [FIX API 文档](/docs/zh-CN/binance-spot-api-docs/fix-api#general-api-information) 以获取完整信息。



* * *

### 2026-03-09[​](/docs/zh-CN/binance-spot-api-docs/demo-mode#2026-03-09 "2026-03-09的直接链接")

计划的停机维护将于 **2026-03-13 06:00 UTC** 开始，预计持续约4小时。

* * *

### 2026-01-29[​](/docs/zh-CN/binance-spot-api-docs/demo-mode#2026-01-29 "2026-01-29的直接链接")

本更新日志将公布现货模拟交易环境的所有计划维护停机时间。

有关如何通过 API 使用模拟交易的更多信息，请参阅 [常规信息](/docs/zh-CN/binance-spot-api-docs/demo-mode/general-info) 页面。