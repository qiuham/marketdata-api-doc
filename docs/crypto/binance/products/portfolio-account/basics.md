---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/portfolio-account/basics
api_type: Guide
updated_at: 2026-11-27 18:30:13.738748
---

# Basics

## Base URLs

Production: `https://api.binance.com`. Also available on `api-gcp.binance.com` and
`api1`–`api4.binance.com`.

Portfolio Account endpoints are served through Binance SAPI.

## Endpoint summary

**Trading team endpoints** — API key on the Manager Parent Account with Portfolio Account permission

| Method | Endpoint                                                              | Weight | Description                                                |
| ------ | --------------------------------------------------------------------- | ------ | ---------------------------------------------------------- |
| GET    | `/sapi/v2/portfolio-account/trading-team/portfolio-basic-info`        | 1      | Portfolio basic info, one or all portfolios                |
| GET    | `/sapi/v2/portfolio-account/trading-team/portfolio-nav-info`          | 1      | Portfolio NAV history                                      |
| GET    | `/sapi/v2/portfolio-account/trading-team/investor-portfolio-his-info` | 1      | A specified investor's subscription and redemption history |
| GET    | `/sapi/v2/capital-connect/trading-team/redemption/calendar`           | 30000  | Upcoming redemption calendar (next 8 days)                 |
| POST   | `/sapi/v2/portfolio-account/trading-team/change-api-sharing-switch`   | 400    | Enable or disable investor API data sharing                |
| GET    | `/sapi/v2/portfolio-account/trading-team/api-sharing-status`          | 200    | Current API sharing status                                 |

**Investor endpoints** — API key on the investor's own account

| Method | Endpoint                                                             | Weight | Description                                            |
| ------ | -------------------------------------------------------------------- | ------ | ------------------------------------------------------ |
| GET    | `/sapi/v1/portfolio-account/investor/portfolio-nav-info`             | 600    | NAV per allocation series                              |
| GET    | `/sapi/v1/portfolio-account/investor/portfolio-history-info`         | 600    | The investor's own subscription and redemption history |
| GET    | `/sapi/v1/portfolio-account/investor/portfolio-realtime-asset-value` | 600    | Realtime NAV per allocation and investor equity        |

## Authentication and request signing

All Portfolio Account endpoints are `SIGNED` and require a valid API key.

- Send the API key in the `X-MBX-APIKEY` header
- Sign each request using HMAC SHA256 with your API secret, over the query string
- Include `timestamp` (Unix milliseconds, validated against the server clock) in every signed
  request
- Optionally include `recvWindow` (request validity window, milliseconds)

The key must be issued on the correct account:

| Endpoint group   | Required key                                                 |
| ---------------- | ------------------------------------------------------------ |
| `trading-team/*` | Manager Parent Account, Portfolio Account permission enabled |
| `investor/*`     | The investor's own account                                   |

GET endpoints take parameters in the query string. POST endpoints take parameters in the query
string or request body per standard SAPI conventions.

For full signing mechanics, parameter encoding and worked examples, see the standard Binance API
signing documentation.

## Rate limits

Portfolio Account endpoints consume UID-based request weight. Weights are listed per endpoint in the
endpoint summary above and in each API Reference entry.

Response headers `x-mbx-used-weight-1m` show current usage against the 1-minute UID limit. Pace
requests accordingly.

Recommended polling schedule:

| Data                         | Suggested frequency                            | Why                                     |
| ---------------------------- | ---------------------------------------------- | --------------------------------------- |
| NAV history                  | Once or twice daily, after 04:00 UTC           | NAV is struck once per day              |
| Investor transaction history | Daily, or on demand                            | Changes only on subscription/redemption |
| Redemption calendar          | Daily, before planning liquidity               | Covers the next 8 days                  |
| API sharing status           | On demand                                      | Changes rarely                          |
| Realtime asset value         | Per your monitoring need, within weight budget | Genuinely realtime                      |

## Numeric formats and precision

All decimal values are returned as strings, per Binance SAPI convention. Parse with a decimal type,
not a float.

- `navPerAllocation` is returned to 8 decimal places
- Allocations are returned to 8 decimal places
- Amounts are returned to the precision of the relevant asset

Using floating-point arithmetic on `navPerAllocation` × allocations will introduce rounding
differences against Binance's own figures.

## Error codes

Errors follow the standard Binance format: an HTTP status plus a JSON body containing `code` and
`msg`. See [Error Codes](./error-code.md) for the Portfolio Account business errors.

## Data freshness and polling

Portfolio Account has no callback or push notification mechanism. Clients must poll.

| Event                                                | Timing                                                                        |
| ---------------------------------------------------- | ----------------------------------------------------------------------------- |
| Daily NAV calculation                                | Between 00:00 and 04:00 UTC; latest available NAV is for the previous UTC day |
| Subscription funds arriving in the Portfolio Account | ~1 hour after trading team approval                                           |
| Redemption transfer attempts                         | Daily, from T+1 up to the settlement deadline                                 |
| New portfolio                                        | No NAV exists until the first daily calculation completes                     |

NAV history is limited to a trailing window (see each endpoint's reference entry). Capital Connect
displays since-inception returns and risk metrics computed from the full series, but the API exposes
only the trailing window. Persist each day's NAV locally from first integration — history beyond the
window is not retrievable through the API.

---

# 基础信息

## 基础 URL

生产环境：`https://api.binance.com`。也可使用 `api-gcp.binance.com` 以及 `api1`–`api4.binance.com`。

投资组合账户接口通过币安 SAPI 提供。

## 接口汇总

**交易团队接口** — 使用管理人母账户上开通了投资组合账户权限的 API Key

| 方法 | 接口                                                                  | 权重  | 说明                                 |
| ---- | --------------------------------------------------------------------- | ----- | ------------------------------------ |
| GET  | `/sapi/v2/portfolio-account/trading-team/portfolio-basic-info`        | 1     | 投资组合基本信息，单个或全部投资组合 |
| GET  | `/sapi/v2/portfolio-account/trading-team/portfolio-nav-info`          | 1     | 投资组合净值历史                     |
| GET  | `/sapi/v2/portfolio-account/trading-team/investor-portfolio-his-info` | 1     | 指定投资人的申购和赎回历史           |
| GET  | `/sapi/v2/capital-connect/trading-team/redemption/calendar`           | 30000 | 即将到来的赎回日历（未来 8 天）      |
| POST | `/sapi/v2/portfolio-account/trading-team/change-api-sharing-switch`   | 400   | 开启或关闭投资人 API 数据共享        |
| GET  | `/sapi/v2/portfolio-account/trading-team/api-sharing-status`          | 200   | 当前 API 共享状态                    |

**投资人接口** — 使用投资人自己账户的 API Key

| 方法 | 接口                                                                 | 权重 | 说明                       |
| ---- | -------------------------------------------------------------------- | ---- | -------------------------- |
| GET  | `/sapi/v1/portfolio-account/investor/portfolio-nav-info`             | 600  | 每份净值序列               |
| GET  | `/sapi/v1/portfolio-account/investor/portfolio-history-info`         | 600  | 投资人自身的申购和赎回历史 |
| GET  | `/sapi/v1/portfolio-account/investor/portfolio-realtime-asset-value` | 600  | 实时每份净值及投资人权益   |

## 认证与请求签名

所有投资组合账户接口均为 `SIGNED`，需要有效的 API Key。

- 在 `X-MBX-APIKEY` 请求头中发送 API Key
- 使用 API Secret 对查询字符串做 HMAC SHA256 签名
- 每个签名请求都要包含 `timestamp`（Unix 毫秒时间戳，与服务器时钟校验）
- 可选包含 `recvWindow`（请求有效窗口，毫秒）

Key 必须签发在正确的账户上：

| 接口分组         | 所需 Key                             |
| ---------------- | ------------------------------------ |
| `trading-team/*` | 管理人母账户，已开通投资组合账户权限 |
| `investor/*`     | 投资人自己的账户                     |

GET 接口的参数放在查询字符串中。POST 接口的参数按标准 SAPI 惯例放在查询字符串或请求体中。

完整的签名机制、参数编码和示例，请参阅币安 API 标准签名文档。

## 限频

投资组合账户接口消耗基于 UID 的请求权重。各接口权重见上方接口汇总以及 API 参考中的各接口条目。

响应头 `x-mbx-used-weight-1m` 显示当前相对于 1 分钟 UID 限额的使用量，请据此控制请求节奏。

推荐的轮询频率：

| 数据           | 建议频率                     | 原因                |
| -------------- | ---------------------------- | ------------------- |
| 净值历史       | 每天一到两次，UTC 04:00 之后 | 净值每天结算一次    |
| 投资人交易历史 | 每天一次，或按需             | 仅在申购/赎回时变化 |
| 赎回日历       | 每天一次，规划流动性之前     | 覆盖未来 8 天       |
| API 共享状态   | 按需                         | 很少变化            |
| 实时资产价值   | 按监控需求，在权重预算内     | 真正的实时数据      |

## 数值格式与精度

按币安 SAPI 惯例，所有小数均以字符串返回。请使用 decimal 类型解析，不要使用浮点数。

- `navPerAllocation` 精确到小数点后 8 位
- 份额精确到小数点后 8 位
- 金额精确到相应币种的精度

对 `navPerAllocation` × 份额使用浮点运算，会与币安自己的数值产生舍入差异。

## 错误码

错误遵循币安标准格式：HTTP 状态码加包含 `code` 和 `msg`
的 JSON 响应体。投资组合账户的业务错误请参阅[错误码](./error-code.md)。

## 数据时效与轮询

投资组合账户没有回调或推送通知机制，客户端必须轮询。

| 事件                     | 时点                                                     |
| ------------------------ | -------------------------------------------------------- |
| 每日净值计算             | UTC 00:00 至 04:00 之间；可获取的最新净值为前一个 UTC 日 |
| 申购资金到达投资组合账户 | 交易团队批准后约 1 小时                                  |
| 赎回划转尝试             | 每日，从 T+1 到结算截止日                                |
| 新建投资组合             | 首次每日计算完成前不存在净值                             |

净值历史仅限于一个滚动窗口（详见各接口的参考条目）。Capital
Connect 展示的是基于完整序列计算的成立以来收益和风险指标，但 API 只开放滚动窗口。请从首次对接起每天在本地保存当日净值 — 超出窗口的历史无法通过 API 获取。