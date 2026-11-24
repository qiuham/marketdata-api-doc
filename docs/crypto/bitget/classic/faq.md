---
exchange: bitget
source_url: https://www.bitget.com/docs/classic/faq
api_type: Guide
updated_at: 2026-11-24 19:00:23.072692
---

# FAQ

**Q1: How to get API support?**

Join our official API support group and our admins will answer your questions: https://t.me/bitgetOpenapi

**Q2: What does the WebSocket parameter `instId` pass? For example, BTCUSDT_UMCBL or BTCUSDT?**

`BTCUSDT` or `default`. Please refer to the `symbol` value from Get Contract Config.

**Q3: How do I deposit demo coins in Demo Trading?**

First enter the official site for demo trading. On the right side under your Asset section, click the deposit button below it.

Note: you can only claim again 72 hours after your last claim.

**Q4: What are the differences between a Trader's minimum open count and a normal user's?**

Futures Trader's minimum open count: refer to the `minOpenCount` response parameter of Get Copy Trade Symbol Settings. Spot Trader's minimum open count: refer to the `minOpenCount` response parameter of Get Copytrade Configuration.

**Q5: How to get a future's maximum order numbers and position numbers?**

Refer to the `maxProductOrderNum` and `maxPositionNum` response parameters of Get Contract Config.

**Q6: How to know whether you are a trader?**

Refer to the `traderType` response parameter of `GET /api/v2/spot/account/info` (Get Account Information).

**Q7: I am using a third-party server/code and it is not working. How can I get help?**

Unfortunately, we do not provide troubleshooting support for third-party servers or tools. Please contact the third-party customer service for further assistance. In addition, providing your API keys to any other platform carries potential security risk, and it is up to you to decide whether to use their services. Please note that we do not provide coding-related help.

**Q8: If I forget the passphrase of my API key, what should I do?**

The passphrase of an API Key cannot be modified. Please recreate your API Key.

**Q9: What is the rate limit of the API?**

1. The rate limit of each API endpoint is marked on the doc page; 2. The rate limit of each API interface is calculated independently; 3. The overall rate limit is 8000/IP/Min. After the rate limit is triggered, it takes 5 minutes to recover.

**Q10: How can I find out the remaining rate limit per second for the API?**

Please refer to the `x-mbx-used-remain-limit` parameter in the response header.

**Q11: Is there any currency with a different name in the spot market and the futures market?**

Yes, currently there are three currencies with this situation: 1. Luna2 (Futures) — Luna (Spot); 2. ALT (Futures) — $ALT (Spot); 3. MEME (Futures) — MEMECOIN (Spot).

**Q12: Which characters are supported for clientOid?**

`clientOid` supports `[0-9]`, `[a-z]`, `[A-Z]` and `[-,+,_,#]`, with a length less than 50.

**Q13: Is there a fixed regular release date for the backend?**

Yes. The current fixed regular release date for the backend is **every Tuesday and Thursday from 14:00 PM to 18:00 PM (UTC +8)** (except for emergency upgrades). During the regular release time window, the REST API may return 45001, 40725, 40808 or 40015 error responses. Users can retry after receiving these error responses. WebSocket connections may be disconnected during the release period, so WebSocket users are advised to implement a reconnection mechanism in their code.

**Q14: Is it possible to lose messages when subscribing to private channels via WebSocket?**

Yes, there is a possibility of message loss. We recommend users always use the REST API as a fallback.

---

# FAQ

**Q1：如何获取 API 相关问题的技术支持？**

可以加入官方 API 技术支持群来反馈 API 问题，管理员会答复您：https://t.me/bitgetOpenapi

**Q2：WebSocket 订阅时 `instId` 传的是什么？**

`instId` 传的是合约信息接口的 `symbol`；有的频道也可以使用 `default` 订阅全部 symbol。

**Q3：模拟盘如何充值模拟币？**

进入官方网站模拟盘交易页面，右侧在资产下方点击充值按钮。

提示：每次资产领取后需间隔 72 小时才能再次领取。

**Q4：交易员最小开单数量跟普通用户有什么区别？**

合约交易员最小开单额：请在交易员获取带单交易对接口的返回参数 `minOpenCount` 获取。现货交易员最小开单额：请在交易员查询带单设置接口的返回参数 `minOpenCount` 获取。

**Q5：合约最大持有订单数、最大持有仓位数如何获取？**

请在合约信息接口的返回参数 `maxSymbolOrderNum`、`maxProductOrderNum`、`maxPositionNum` 获取。

**Q6：如何判断您的身份是否是交易员？**

请在获取账户信息接口的返回参数 `traderType` 获取。

**Q7：我使用的第三方服务器/外包服务器不工作了，可以给我提供帮助吗？**

很抱歉，我们不支持对第三方服务器或工具的帮助，请您联系三方服务供应商或开发商寻求进一步的帮助。除此之外，将您在 Bitget 平台的 API Key 提供给任何第三方平台是存在安全风险的，您需要自行决定是否使用这些服务。请注意，我们不提供与编程相关的帮助。

**Q8：如果我忘记了 API key 的 passphrase 怎么办？**

API key 的 passphrase 不支持更改，需要您重新创建 API key。

**Q9：API 接口的限频规则是什么？**

1. 各 API 端口频率限制规则在文档有标注；2. 各 API 接口的限频互相独立计算；3. 总体有 8000 次/IP/分钟的限频规则，限频触发后需要 5 分钟恢复。

**Q10：如何得知接口每秒剩余的限频次数？**

请参考响应头中的 `x-mbx-used-remain-limit` 参数。

**Q11：是否有币种在现货和合约交易对中的名称不同？**

是的，目前有三个币种有此情况，分别是：1. 合约 LUNA2 — 现货 LUNA；2. 合约 ALT — 现货 $ALT；3. 合约 MEME — 现货 MEMECOIN。

**Q12：clientOid 支持哪些格式？**

`clientOid` 支持 `[0-9]`、`[a-z]`、`[A-Z]` 以及 `[-,+,_,#]`，长度小于 50。

**Q13：Bitget 后端是否有固定的常规发布日？**

是的，当前后端固定的常规发布日为**每周二和周四的 14:00 - 18:00 pm (UTC +8)**（紧急发布除外）。在常规发布时间段内，REST API 可能会收到 45001、40725、40808、40015 报错响应，用户在收到报错响应后重试即可。WebSocket 可能会在发布、更新期间断连，请 WebSocket 用户在代码中添加重连机制。

**Q14：WebSocket 私有频道订阅是否有可能丢失消息？**

是的，存在消息丢失的可能性，建议用户始终使用 REST API 作为兜底措施。