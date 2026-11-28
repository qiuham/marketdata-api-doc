---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-glp-c-glp-c-api
anchor_id: global-liquidity-program-glp-c-glp-c-api
api_type: API
updated_at: 2026-11-28 18:57:22.936298
---

# GLP-C API

GLP-C (Global Liquidity Program - C) APIs let eligible market makers discover and enroll instruments, and query their quote assessment results.

**Category** | **Endpoint**  
---|---  
Enrollment | Get eligible instruments · Enroll instruments · Get enrollment statistics  
Quote assessment | Get minute assessment · Get hourly instrument assessment · Get hourly assessment summary  
  
**Program rules**

Instruments are grouped into G1 / G2 / G3 with required bilateral weighted quoting share of 5% / 10% / 15%. Top 3 price levels are weighted 2 / 1 / 0.5. An instrument qualifies for an hour when it qualifies in at least 70% of minutes. Spot and Perpetuals are assessed separately. The tier is based directly on the number of qualified instruments, without a multiplier: Tier 1 ≥ 40 → VIP 9 Maker; Tier 2 30–39 → VIP 8; Tier 3 20–29 → VIP 7; Tier 4 10–19 → VIP 6. Taker fees follow the organic VIP tier.

During the public beta (24 Nov – 1 Dec 2026), the hourly uptime requirement is 50%, and `requiredUptime` / `requiredHourlyUptime` return `"0.5"`. From 1 Dec 2026, the requirement is 70% (`"0.7"`).

**General notes**

  * In requests, use `PERP` for perpetuals (including X-Perp). The hourly assessment summary returns `SWAP` for the same category.

  * Only accounts whitelisted for GLP-C can call these endpoints. Results are returned for the participant of the authenticated account. No user ID parameter is accepted.

  * An instrument is identified by `instType` \+ `instId`. The same `instId` can exist under different `instType`.

  * Timestamps use Unix timestamp format in milliseconds (UTC), e.g. `1795154400000`. Query ranges are inclusive. Assessment data is available for the last 72 hours.

  * Quote assessment endpoints return all values as strings. Unavailable values are returned as `""`. Empty results are returned as `[]`.

#### Assessment reason codes

**Reason code** | **Description**  
---|---  
QUALIFIED | The minute meets the qualification requirements  
BELOW_THRESHOLD | Share is below the threshold  
NO_CUSTOMER_QUOTE | No quotes from the account in this minute  
MARKET_DENOMINATOR_ZERO | No market quotes in this minute  
SOURCE_DATA_MISSING | Market snapshot is missing  
SOURCE_DATA_INVALID | Market snapshot is unusable

---

# GLP-C API

GLP-C（Global Liquidity Program - C）API 供符合条件的做市商查询及注册产品，并查询其报价考核结果。

**类别** | **接口**  
---|---  
注册 | 获取可参与产品 · 注册产品 · 获取注册统计  
报价考核 | 获取分钟考核 · 获取产品小时考核 · 获取小时考核汇总  
  
**计划规则**

产品分为 G1 / G2 / G3，双边加权报价份额门槛分别为 5% / 10% / 15%。前三档价格权重分别为 2 / 1 / 0.5。一个小时内至少 70% 的分钟达标，该产品才在该小时达标。现货和永续合约分开考核。等级直接按达标产品数量计算，不使用 multiplier 加权：Tier 1 ≥ 40 → VIP 9 Maker；Tier 2 为 30–39 → VIP 8；Tier 3 为 20–29 → VIP 7；Tier 4 为 10–19 → VIP 6。Taker 费率按原生 VIP 等级执行。

公测期间（2026 年 11 月 24 日至 12 月 1 日），小时在线率要求为 50%，`requiredUptime` / `requiredHourlyUptime` 返回 `"0.5"`。自 2026 年 12 月 1 日起，要求为 70%（`"0.7"`）。

**通用说明**

  * 请求中使用 `PERP` 表示永续合约（含 X-Perp）；小时考核汇总响应使用 `SWAP` 表示相同类别。

  * 仅 GLP-C 白名单账户可调用这些接口。返回结果为当前鉴权账户所属 participant 的数据。不支持传入用户 ID 参数。

  * 产品由 `instType` \+ `instId` 唯一确定。同一 `instId` 可能存在于不同的 `instType` 下。

  * 时间戳均为 Unix 毫秒时间戳（UTC），如 `1795154400000`。查询时间范围为闭区间。考核数据保留最近 72 小时。

  * 报价考核接口的所有数值均以字符串返回。不可用的值返回 `""`。无结果时返回 `[]`。

#### 考核原因码

**原因码** | **描述**  
---|---  
QUALIFIED | 该分钟满足达标要求  
BELOW_THRESHOLD | 份额低于门槛  
NO_CUSTOMER_QUOTE | 该分钟内账户无报价  
MARKET_DENOMINATOR_ZERO | 该分钟内市场无报价  
SOURCE_DATA_MISSING | 市场快照缺失  
SOURCE_DATA_INVALID | 市场快照不可用