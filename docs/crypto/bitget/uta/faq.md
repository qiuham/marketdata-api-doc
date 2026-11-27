---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/faq
api_type: Guide
updated_at: 2026-11-27 19:02:03.164944
---

# FAQ

**Q1: How to get API support?**

Join our official API support group and our admins will answer your questions: https://t.me/bitgetOpenapi

**Q2: How do I specify the trading pair when subscribing via WebSocket?**

In UTA V3 WebSocket subscription messages, pass the `symbol` parameter (e.g. `BTCUSDT`). Note: V3 no longer uses the V2 field name `instId`.

**Q3: How do I deposit demo coins in Demo Trading?**

Go to the demo trading page on the official website and click the deposit button below the Assets section on the right. After each claim, you must wait 72 hours before claiming again.

**Q4: How do I get the maximum number of open orders and positions for futures?**

Refer to the response parameters of Get Instruments (`GET /api/v3/market/instruments`):

- `maxProductOrderNum`: maximum number of open orders within the same product type (e.g. USDT-FUTURES).
- `maxPositionNum`: maximum number of positions per symbol (returned for futures/margin only).
- For per-order quantity limits, use `minOrderQty` (minimum order quantity) and `maxOrderQty` (maximum order quantity; `0` means no limit).

**Q5: How do I know whether I am a trader?**

Refer to the `traderType` response parameter of Get Account Information.

**Q6: I am using a third-party server/code and it is not working. How can I get help?**

Unfortunately, Bitget does not provide support for third-party servers or tools. Please contact your service provider or developer directly. Providing your API Key to any third-party platform carries security risks, which you bear yourself. Please note that we do not provide coding-related help.

**Q7: If I forget the passphrase of my API key, what should I do?**

The passphrase of an API key cannot be modified or recovered. You can only create a new API key.

**Q8: What is the rate limit of the API?**

- If requests are too frequent, the system automatically throttles them and returns the `429 Too Many Requests` status code;
- The rate limit of each API endpoint is marked on its doc page;
- The rate limit of each API endpoint is calculated independently;
- REST and WebSocket share the same rate limit quota;
- The overall rate limit for the general domain is 8,000 requests/IP/minute (it takes 5 minutes to recover after being triggered);
- Rate limits increase automatically with VIP/MM/PRO level. For details, see [VIP Rate Limit Rules](/docs/uta/rate-limit/rate-limit) and [Institutional Rate Limit](/docs/uta/rate-limit/institutional/institutional-rate-limit).

**Q9: How can I find out the remaining rate limit per second?**

REST API: refer to the `x-mbx-used-remain-limit` parameter in the HTTP response header.

WebSocket: when sending trading requests (e.g. place or cancel orders), the `remaining` field (String) in the response indicates the number of requests currently remaining.

**Q10: Which formats are supported for `clientOid`?**

In UTA V3 order placement endpoints, a custom `clientOid` must match the regular expression `^[0-9A-Za-z_:#\-+\s]{1,32}$`, i.e. 1–32 characters consisting of upper/lower-case letters, digits, and `_`, `:`, `#`, `-`, `+` or whitespace.

**Q11: Is there a fixed regular release date for the backend?**

Yes. The current fixed regular release window is **every Tuesday and Thursday, 14:00 - 18:00 (UTC+8)** (except for emergency releases). During the release window, the REST API may return 45001, 40725, 40808 or 40015 errors; simply retry after receiving them. WebSocket connections may be disconnected during the release, so please implement a reconnection mechanism in your code.

**Q12: Is it possible to lose messages when subscribing to private channels via WebSocket?**

Yes, message loss is possible. WebSocket only provides real-time push; the gateway neither caches nor replays historical events, and events generated while the connection is down will not be re-sent after reconnecting. We recommend always using the REST API as a fallback and actively querying the latest state after reconnecting.

---

# FAQ

**Q1：如何获取 API 相关问题的技术支持？**

可以加入官方 API 技术支持群来反馈 API 问题，管理员会答复您：https://t.me/bitgetOpenapi

**Q2：WebSocket 订阅时，如何指定交易对？**

在 UTA V3 的 WebSocket 订阅报文中，请传入 `symbol` 参数（如 `BTCUSDT`）。注：V3 已不再使用 V2 的 `instId` 命名。

**Q3：模拟盘如何充值模拟币？**

进入官方网站模拟盘交易页面，在右侧资产下方点击充值按钮。每次领取后需间隔 72 小时才能再次领取。

**Q4：合约最大持有订单数、最大持有仓位数如何获取？**

请在合约信息接口（`GET /api/v3/market/instruments`）的返回参数中获取：

- `maxProductOrderNum`：同一业务线（如 USDT-FUTURES）下的最大委托数量。
- `maxPositionNum`：单个交易对的最大持有仓位数量（仅合约/杠杆返回）。
- 单笔订单数量限制请使用 `minOrderQty`（最小开单数量）与 `maxOrderQty`（最大下单数量，为 `0` 表示不限制）。

**Q5：如何判断您的身份是否是交易员？**

请在获取账户信息接口的返回参数 `traderType` 中查看。

**Q6：我使用的第三方服务器/外包服务器不工作了，可以给我提供帮助吗？**

很抱歉，Bitget 不支持对第三方服务器或工具提供帮助，请直接联系您的服务供应商或开发商。将 API Key 提供给任何第三方平台都存在安全风险，需自行承担；我们也不提供与编程相关的帮助。

**Q7：如果我忘记了 API key 的 passphrase 怎么办？**

API key 的 passphrase 不支持修改或找回，您只能重新创建一个新的 API key。

**Q8：API 接口的限频规则是什么？**

- 如果请求过于频繁，系统会自动限制请求并返回 `429 Too Many Requests` 状态码；
- 各 API 接口的限频规则在各自文档页面中有标注；
- 各 API 接口的限频互相独立计算；
- REST 与 WebSocket 共享限频额度；
- 普通域名总体有 8,000 次/IP/分钟的限频规则（触发后需 5 分钟恢复）；
- 限频会随 VIP/MM/PRO 等级提升而自动提升，详情请参考 [VIP 限频规则](/zh-CN/docs/uta/rate-limit/rate-limit) 与 [机构限频规则](/zh-CN/docs/uta/rate-limit/institutional/institutional-rate-limit)。

**Q9：如何得知接口每秒剩余的限频次数？**

REST API：请参考 HTTP 响应头中的 `x-mbx-used-remain-limit` 参数。

WebSocket：发送交易指令（如下单、撤单）时，响应报文中的 `remaining` 字段（String 类型）代表当前剩余的可用请求次数。

**Q10：`clientOid` 支持哪些格式？**

UTA V3 下单接口中，`clientOid` 的自定义格式必须满足正则表达式 `^[0-9A-Za-z_:#\-+\s]{1,32}$`，即长度为 1～32 个字符，允许大小写字母、数字及 `_`、`:`、`#`、`-`、`+`、空白字符。

**Q11：Bitget 后端是否有固定的常规发布日？**

是的，当前固定常规发布日为**每周二和周四的 14:00 - 18:00（UTC+8）**（紧急发布除外）。在常规发布时间段内，REST API 可能会返回 45001、40725、40808、40015 报错响应，收到后重试即可。WebSocket 可能会在发布期间断连，请在代码中添加重连机制。

**Q12：WebSocket 私有频道订阅是否有可能丢失消息？**

是的，存在消息丢失的可能性。WebSocket 仅提供实时推送，网关不缓存也不重放历史事件；连接断开期间产生的事件，重连后不会补发。建议始终使用 REST API 作为兜底措施，在断线重连后主动查询最新状态。