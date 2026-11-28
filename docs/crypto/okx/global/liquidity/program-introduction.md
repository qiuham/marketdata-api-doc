---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#global-liquidity-program-introduction
anchor_id: global-liquidity-program-introduction
api_type: API
updated_at: 2026-11-28 18:57:22.844922
---

# Introduction

The OKX Global Liquidity Program (GLP) offers fee benefits to eligible market makers based on trading or quoting performance.  
  
  * **GLP-A** : Type A (top) pairs. Assessed weekly on unadjusted trading market share, separately for Maker and Taker. Benefit: VIP 9 + Colo.
  * **GLP-B** : Type B pairs (most other pairs). Assessed weekly on adjusted trading market share, separately for Maker and Taker. Benefit: VIP 6–9, with Colo at VIP 9. Expiry Futures & Nitro Spreads are assessed across all pairs on unadjusted share.
  * **GLP-C** : Liquidity-incentive pairs (Spot and Perpetuals). Assessed hourly on bilateral weighted quoting share. Benefit: VIP 6–9 Maker fees from the next hour.

Participants must meet AUM and organic VIP tier requirements; see the [OKX Liquidity Program page](https://www.okx.com/fees/liquidity-program) for details. Where more than one program applies, the most favorable fee applies. Program participants are not eligible for other VIP-related or volume-related promotions or rebates.

Only enrolled accounts can access the user endpoints in this section. A sub-account API key returns the master account's data.

[Program details](https://www.okx.com/help/introducing-the-okx-global-liquidity-program) · [GLP Workspace](https://www.okx.com/glp-workspace) · To apply, contact your Relationship Manager or email `institutional@okx.com`.

**Common error codes**

Error code | HTTP status code | Error message  
---|---|---  
50001 | 503 | Service temporarily unavailable. Please try again later.  
50014 | 200 | Parameter {param0} can not be empty  
50016 | 200 | Parameter {param0} does not match parameter {param1}  
50026 | 500 | System error. Try again later  
50030 | 200 | You don't have permission to use this API endpoint  
51000 | 200 | Parameter error

---

# 介绍

OKX 全球流动性计划（GLP）根据交易或报价表现，为符合条件的做市商提供费率优惠。  
  
  * **GLP-A** ：Type A（头部）交易对。按未加权的交易市场份额进行周度考核，Maker 和 Taker 分开考核。权益为 VIP 9 + Colo。
  * **GLP-B** ：Type B 交易对（大多数其他交易对）。按调整后的交易市场份额进行周度考核，Maker 和 Taker 分开考核。权益为 VIP 6–9，VIP 9 可享 Colo。交割合约和 Nitro Spreads 不区分交易对类型，所有交易对一起按未加权份额考核。
  * **GLP-C** ：流动性激励交易对（现货和永续合约）。按双边加权报价份额进行小时考核，从下一小时起享受 VIP 6–9 Maker 费率。

参与者须满足 AUM 和原生 VIP 等级要求，详情参见 [OKX 流动性计划页面](https://www.okx.com/fees/liquidity-program)。同时适用多个计划时，采用最优惠的费率。计划参与者不享受其他 VIP 相关或交易量相关的优惠活动或返佣。

本节用户接口仅限已报名账户调用。子账户 API key 返回主账户的数据。

[计划详情](https://www.okx.com/help/introducing-the-okx-global-liquidity-program) · [GLP 工作台](https://www.okx.com/glp-workspace) · 如需申请，请联系客户经理或发送邮件至 `institutional@okx.com`。

**通用错误码**

错误码 | HTTP 状态码 | 错误提示  
---|---|---  
50001 | 503 | 服务暂时不可用，请稍后重试  
50014 | 200 | 参数 {param0} 不能为空  
50016 | 200 | 参数 {param0} 与参数 {param1} 不匹配  
50026 | 500 | 系统错误，请稍后重试  
50030 | 200 | 您无权使用此 API 端点  
51000 | 200 | 参数错误