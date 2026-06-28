---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/zh_CN
api_type: REST
updated_at: 2026-05-27 20:16:42.508670
---

# Gate API v4.106.88

v4.106.88 · Stable


欢迎使用 Gate API APIv4 接口提供了现货、杠杆、合约交易相关的操作，包括公共接口查询市场行情，以及需要认证的私有接口， 实现基于 API 的自动交易。

##  访问链接

**REST API BaseURL:**

  * 实盘交易: `https://api.gateio.ws/api/v4`
  * 模拟交易：`https://api-testnet.gateapi.io/api/v4`
  * 合约实盘交易备选入口（只适用合约 API）：`https://fx-api.gateio.ws/api/v4`

##  SDK

可用 SDK:

[PyPython](https://github.com/gate/gateapi-python)[JavaJava](https://github.com/gate/gateapi-java)[PHPPHP](https://github.com/gate/gateapi-php)[GoGo](https://github.com/gate/gateapi-go)[C#C#](https://github.com/gate/gateapi-csharp)[NodeNodeJS](https://github.com/gate/gateapi-nodejs)[JSJavascript](https://github.com/gate/gateapi-js)

  * [Python ](https://github.com/gate/gateapi-python)
  * [Java ](https://github.com/gate/gateapi-java)
  * [PHP ](https://github.com/gate/gateapi-php)
  * [Go ](https://github.com/gate/gateapi-go)
  * [C# ](https://github.com/gate/gateapi-csharp)
  * [NodeJS ](https://github.com/gate/gateapi-nodejs)
  * [Javascript ](https://github.com/gate/gateapi-js)

部分 SDK 除了各接口的示例文档以外，还额外提供了调用 SDK 的示例应用程序。 示例应用程序提供了一个相对更加丰富的 SDK 使用示例，可以完整构建运行， 具体使用方式参考各 SDK 的示例程序说明

  * [Python ](https://github.com/gate/gateapi-python/tree/master/example)
  * [Java ](https://github.com/gate/gateapi-java/tree/master/example)
  * [C# ](https://github.com/gate/gateapi-csharp/tree/master/example)
  * [Go ](https://github.com/gate/gateapi-go/tree/master/_example)

##  关于APIv4 Key升级

2020 年 4 月

APIv4 最开始合约的 Key 与现货的是分开管理的。不过从现在开始我们对 APIv4 的 Key 进行了升级改造。 用户现在可以创建多个 Key，而且可以为每个 Key 配置不同的操作权限。比如你可以创建一个 Key 同时拥有现货的读写和合约的读写权限，这样的话只需要一个 Key 就可以同时操作现货和合约交易。

用户原有的 Key 会无缝迁移到新的管理方案，原先的 Key 在新的管理模式下，对应一个 Key 只配置了现货的权限，另一个 Key 只配置了合约的权限，用户可以使用新的管理模式对迁移后的 Key 重新配置权限。

##  与 APIv2 的区别

APIv4 是一套全新的 HTTP REST API ，独立于 APIv2 。APIv4 提供了完整的交易功能，增强了 API 的认证鉴权。另外 APIv4 基于 [OpenAPI 标准 ](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md) 书写，SDK 和文档通过同一套 API 标准生成，确保文档和程序的完整一致。

APIv4 与 APIv2 在使用上有如下区别：

  1. 两者的 API Key 是独立的。 APIv2 在个人账户的 APIKeys 入口申请。而 APIv4 在个人账户的 APIv4Keys 页面申请。
  2. APIv2 在交易操作上只支持现货交易，APIv4 支持现货、杠杆和合约的完整交易操作

如何选择：

  1. 如果需要杠杆或合约交易，选择 APIv4
  2. 如果只需要现货交易或者钱包操作，则根据个人当前状况自行选择

##  市商申请

为进一步提高平台盘口深度和交易流动性，我们将通过公开透明的方式招募机构做市商，根据为平台流动性做出的贡献情况，为专业机构做市商提供专业的做市商手续费率方案。

  1. 提供 Gate UID
  2. 提供他所交易量截图或VIP等级等
  3. 简述做市方法及规模

提供以上内容提交至 [mm@gate.com](mailto:mm@gate.com) ，我们将在3个工作日内受理。

TIP

VIP11及以上需在个人中心开启GT抵扣，才可享有专业市商费率。

##  技术支持

使用过程中如有问题或者建议，您可以选择以下任意方式联系我们：

  * 提交工单反馈
  * 在线工单反馈
  * 将您的联系方式与问题发送至 [mm@gate.com](mailto:mm@gate.com) ，我们将为您分配技术专员为您服务

如您遇到API错误，建议您整理以下内容，方便我们为您快速分析问题：

  1. 问题描述
  2. Gate UID
  3. 请求的地址与参数
  4. 错误代码
  5. 返回结果

DANGER

即使是提交问题，也切勿将API key信息提交给客服及他人，否则会有严重的资产风险。如果已经不小心泄漏，请将已有API删除并重新生成。

#  Changelog

**v4.106.88**

2026-05-26

  * 统一账户：快捷还款相关参数补充必填字段约束 —— `QuickRepaymentInfo` 必填 **`debt_currencies`** 、**`available_currencies`** ；`QuickRepaymentResp` 必填 **`order_id`** 、**`repaid_infos`** 、**`used_infos`** ；`RepaidInfo` 必填 **`currency`** 、**`repaid`** 、**`left`** ；`UsedInfo` 必填 **`currency`** 、**`used`**

**v4.106.87**

2026-05-21

  * CrossEx API：交易所枚举 **`exchange_type`** 、划转路径账户类型等补充 **`KRAKEN`** 、**`CROSSEX_KRAKEN`** ；费率示例增加 Kraken 现货/合约档位；`**CrossexOrder.symbol`** 补充 **`KRAKEN_FUTURE_*`** 合约标识写法；产品与接口说明对齐 Kraken 侧暂不支持现货/杠杆单笔路径等限制

**v4.106.86**

2026-05-19

  * 合约新增可选字段 **`tpsl_tp_trigger_price`** 、**`tpsl_sl_trigger_price`** （string，止盈价 / 止损价），用于合约下单链路携带止盈止损触发价

**v4.106.85**

2026-05-19

  * TradFi API新增可选查询参数 **`page`** 、**`page_size`** ，支持历史仓位分页查询
  * TradFi API响应 `data` 增加 **`total`** （总数）、**`total_page`** （总页数）
  * 合约下单请求体新增可选字段 **`action_mode`** （string，处理模式），用于控制下单响应返回的字段粒度；取值 **`ACK`** （异步，仅关键字段）、**`RESULT`** （无清算信息）、**`FULL`** （完整模式，默认）
  * 合约API在 **`DELETE /futures/{settle}/orders`** （`cancelFuturesOrders`）与 **`DELETE /futures/{settle}/orders/{order_id}`** （`cancelFuturesOrder`）上增加可选查询参数 **`action_mode`** ，使撤销接口的响应字段与下单时的 `action_mode` 语义对齐

**v4.106.84**

2026-05-18

  * 双币投资计划模型新增 **`min_amount`** （string，最小投资金额）；计划在列表文档与示例载荷中同步体现该字段

**v4.106.83**

2026-05-18

  * **`PUT /futures/{settle}/price_orders/amend`** 不再使用路径参数 `order_id`，请在请求体 JSON 中使用 **`order_id`** 指定待修改的自动订单（其他语义不变）
  * 补充 **`pos_margin_mode`** （仓位保证金模式），取值 **`isolated`（逐仓）** / **`cross`（全仓）**；移除 enum 中无效的中文占位项
  * 现货限价单止盈/止损嵌套对象（单笔下单、单笔改单、批量下单、批量改单请求体）：在文档中分别以互斥的名称展示止盈/止损段落（文档展示名：`SpotOrderStopProfit` / `SpotOrderStopLoss`、`PatchSpotOrderStopProfit` / `PatchSpotOrderStopLoss`），与各语言 SDK 的生成类型保持一致；`stop_loss.order_price` 描述统一为「止损委托价」

**v4.106.82**

2026-05-14

  * 合约新增 **追逐限价单（Chase Limit Order）** 接口，均在 `/futures/{settle}/autoorder/v1/chase/*` 路径下： 
    * **`POST /futures/{settle}/autoorder/v1/chase/create`** （`createChaseOrder`）—— 创建追逐限价单，支持 `contract`、`amount`、`price_limit`（或 `offset_limit`）、可选 `reduce_only`、`text`、`is_dual_mode`、`price_type` / `price_gap_type` / `price_gap_value`、`pos_margin_mode`、`position_mode`
    * **`POST /futures/{settle}/autoorder/v1/chase/stop`** （`stopChaseOrder`）—— 终止指定追逐限价单，按 `id` 或 `text` 任一确定委托
    * **`POST /futures/{settle}/autoorder/v1/chase/stop_all`** （`stopAllChaseOrders`）—— 批量终止追逐限价单，可按 `contract`、`pos_margin_mode` 过滤
    * **`GET /futures/{settle}/autoorder/v1/chase/list`** （`getChaseOrders`）—— 获取追逐限价单列表，支持 `contract`、`is_finished`、`start_at` / `end_at`、`page_num` / `page_size`、必填 `sort_by`（1 `ORDER_SORT_CREATED_AT`，2 `ORDER_SORT_FINISHED_AT`）、`hide_cancel`、`reduce_only`、`side` 等筛选
    * **`GET /futures/{settle}/autoorder/v1/chase/detail`** （`getChaseOrderDetail`）—— 按 `id` 获取追逐限价单详情
  * REST 文档为追逐限价单补充结构化请求与响应说明：`CreateChaseOrderReq`、`CreateChaseOrderResp`、`StopChaseOrderReq`、`StopChaseOrderResp`、`StopAllChaseOrdersReq`、`StopAllChaseOrdersResp`、`GetChaseOrdersResp`、`GetChaseOrderDetailResp`，以及列表/详情条目 `ChaseOrder`（含 `chase_price`、`interval_sec`、`suborder_*`、`price_type`、`price_gap_type`、`price_gap_value` 等字段）

**v4.106.81**

2026-05-13

  * 现货下单相关文档增补 `stop_profit` / `stop_loss` 嵌套结构（章节展示标题为 `SpotOrderTPSL` / `PatchSpotOrderTPSL`），覆盖单笔下单、单笔改单、批量下单与批量改单；限价止盈/止损字段均包含 `trigger_price`、`order_price`；取消止盈/止损时传 `{}`，传 `null` 表示不修改对应侧；示例已刷新

**v4.106.80**

2026-05-10

  * 在 **`GET /crossex/history_orders`** （`listCrossexHistoryOrders`）上新增可选查询参数 **`attributes`** ，支持按订单属性多选过滤（`COMMON`、`LIQ`、`REDUCE`、`ADL`、`SETTLEMENT`，多个以英文逗号分隔）
  * 补充若干查询参数说明（如 `coin`、`symbol` 等）；`CrossexOrder.attribute` 的描述中增加 **下架清算（SETTLEMENT）** ；划转记录里 `to_account_type` 的文案风格与 `from_account_type` 对齐（字段说明统一用描述句式）；`exchange_type` 文案中的交易所枚举说明收窄为 **BINANCE / OKX / GATE / BYBIT** （若线上仍可能返回其他取值请与产品/后端核对）

**v4.106.78**

2026-05-04

  * `GET /crossex/coin_discount_rate`（`listCrossexCoinDiscountRate`）的 summary 由「查询币种折扣率（分所模式下，保证金币种的折扣率）」精简为「查询币种折扣率」，去掉括号内的「分所模式/保证金币种」说明性补充

**v4.106.75**

2026-04-28

  * P2P示例与演示数据脱敏刷新（商家/对手方场景、含 SWIFT 等支付方式）；示例字段命名与文档 schema 对齐（如 `seller_realname`、`currency_type`）；精简冗长历史示例块
  * 量化：`SpotGridStrategy.strategy_params_preview` 将扩展字段收窄为字符串键值映射；`SpotGridStrategyDetail` 的 `base_info`、`metrics`、`position` 改为松散字符串映射，不再挂载旧版 AI-hub 组合的 `AIHubPortfolio*` 子结构，`AIHubPortfolioBaseInfo`、`AIHubPortfolioMetrics`、`AIHubPortfolioPosition` 三组辅助模型从对外文档移除
  * 跨所API：杠杆映射类响应的英文描述；账单流水分页接口移除查询参数 `statement_type`；列表项字段由 `statement_type` 更名为 `type` 并更新说明；精简 `CrossexSymbol` 等字段的中英描述措辞
  * `GET /wallet/withdraw_status` 的 `page` 参数英文说明改为 “Page number”

**v4.106.73**

2026-04-27

  * **`Contract`** 模型：新增 `enable_circuit_breaker`，表示新上市合约是否启用标记价格熔断机制（平台若对某新开盘合约市场启用该机制以降低开盘后剧烈波动与爆仓风险，将提前公告）
  * **`ContractStat`** 模型：新增 `long_liq_usd_new`、`short_liq_usd_new`（USDT 结算下按 `long_liq_size` / `short_liq_size`、`multiplier` 与 `mark_price` 计算的计价币种爆仓量）；新增 `top_long_size`、`top_short_size`、`long_taker_size`、`short_taker_size`、`top_long_account`、`top_short_account`、`long_users`、`short_users` 等大户持仓、吃单量与用户数量类字段

**v4.106.72**

2026-04-27

  * 文档站点：按 Tag 拆分展示，各 Tag 页面仅聚合该分组下的路径与关联 schema；全站通用的 changelog 概览、REST 必读、认证、FAQ、错误码等章节不再在每个 Tag 着陆页全文重复挂载；同时为 **TradFi** 相关内容增加侧边栏分组标题

**v4.106.71**

2026-04-27

###  统一账户 — 快捷还款（新增接口）

  * **新增`GET /unified/estimated_quick_repayment`**（`getEstimatedQuickRepayment`）— 返回预估快捷还款信息（按币种负债与可用于还款的币种及余额等）。
  * **新增`POST /unified/quick_repayment`**（`createQuickRepayment`）— 执行快捷还款；请求体为 `debt_currencies`、`available_currencies` 字符串数组。上述接口仅适用于统一账户 **跨币种保证金模式** 或 **组合保证金模式** 。
  * 快捷还款文档的请求/响应体采用统一命名的结构段落：`QuickEstimatedRepayment`、`QuickRepaymentInfo`、`QuickRepaymentResp`；数组部分分别使用 `UnifiedDebtCurrencies`、`UnifiedAvailableCurrencies`、`RepaidInfo`、`UsedInfo` 作为容器，`UnifiedQuickRepayDebtItem`、`UnifiedQuickRepayAvailableItem`、`UnifiedQuickRepayRepaidInfo`、`UnifiedQuickRepayUsedInfo` 描述行项目；章节示例随之更新
  * 两个接口均补充典型 **`400`** / **`401`** / **`403`** 错误响应，遵循标准 Gate 错误包络（含 `label` / `message` 等语义）
  * 文案修正：去掉重复「模式」，统一为「跨币种保证金模式与组合保证金模式」。

###  其他变更

  * 子账户余额列表接口查询参数 `page` 的英文说明更新
  * 合约API从 `FuturesOrderAmendment` 移除内部字段 `contract`，并精简改单请求示例
  * 跨所API摘要与示例更新，示例字段对齐（`tif`、`fee_currency`、`avg_price` 等）；账户流水相关：去掉 `statement_type` 查询参数，响应字段更名为 `type`，及其他示例/文案调整
  * 量化/网格策略相关 schema 与字段说明调整
  * P2P 商家端接口路径与 schema 更新

**v4.106.70**

2026-04-21

  * 文档：BizType 参考表新增 5 个子账号内部资金划转 biz_id —— `150215`、`150216`、`150217`、`150218`、`150219`（均归类为「子账号资金划转」）
  * 资产互换：`GET /asset-swap/config` 与 `GET /asset-swap/orders/v1/{id}` 的响应 `data` 分别改用 `ConfigResp`、`OrderQueryV1Resp` 说明包裹结构（示例同步更新）
  * 量化API将 `additionalProperties` 由强制 `type: string` 放宽为任意类型（`{}`）；强类型 SDK 将由原本的 `Map<String, String>` 变为 `Map<String, Object>`

**v4.106.61**

2026-04-14

  * `SubAccountBalance` 模型，新增 `locking` 字段（币种锁定金额）
  * 为 `FuturesPriceTriggeredOrder`、`TriggerOrderResponse` 补充 `id_string` 字段说明：与数值 `id` 表示同一自动订单，为 `id` 的十进制字符串，避免 JavaScript 等环境下 int64 精度问题；展示或需要字符串唯一标识时建议使用；与 `futures.orders`、`futures.autoorders` 等推送中同名字段含义一致。覆盖合约价格触发相关 REST：`/futures/{settle}/price_orders`（创建、列表、批量撤销、查询、撤销、修改）。
  * `PartnerCommissionHistory`、`AgencyCommissionHistory` 中合伙人/代理商返佣列表项：将 `commission_amount`、`commission_asset` 字段说明由「交易金额」调整为「返佣金额」，与字段语义一致
  * `Contract` 模型：补充 `interest_rate` 字段说明（字符串形式的小数比率），适用于 `GET /futures/{settle}/contracts` 与 `GET /futures/{settle}/contracts/{contract}` 返回
  * 开发者文档：将 Agent 相关文档品牌由 **Gate for AI** 更名为 **Gate for AI Agent** （页面标题、正文与侧栏文案）；产品主页与帮助中心链接更新为 `gate-for-ai-agent` 路径

**v4.106.59**

2026-04-10

  * 新增 `GET /earn/dual/order-refund-preview`（`getDualOrderRefundPreview`）— 双币投资提前赎回预览
  * 新增 `POST /earn/dual/order-refund`（`placeDualOrderRefund`）— 双币订单提前赎回
  * 新增 `POST /earn/dual/modify-order-reinvest`（`modifyDualOrderReinvest`）— 双币订单复投修改
  * 新增 `GET /earn/dual/project-recommend`（`getDualProjectRecommend`）— 双币推荐项目
  * `GET /earn/dual/investment_plan`：新增可选查询参数 `coin`、`type`、`quote_currency`、`sort`、`page`、`page_size`
  * `GET /earn/dual/orders`：新增可选查询参数 `type`、`status`、`coin`
  * 双币理财相关新增模型 `DualOrderRefundPreview`、`DualOrderRefundParams`、`DualModifyOrderReinvestParams`、`DualProjectRecommend` 及对应示例

**v4.106.58**

2026-04-03

  * `Contract` 模型：新增 `contract_type` 字段 — 合约分类类型（如 stocks-股票、metals-金属、indices-指数、forex-外汇、commodities-大宗商品等）
  * `GET /wallet/sub_account_balances` 接口：新增 `page` 和 `limit` 查询参数，支持分页

**v4.106.57**

2026-04-01

  * `WithdrawalRecord` 模型：调整提现终态时间字段说明 — 当 `status = DONE` 时表示提现成功时间（不再与 `block_number > 0` 绑定）
  * `WithdrawalRecord`、`WithdrawalsDel` 模型：精简 `DONE` 状态枚举说明（移除「`block_number > 0` 时表示已完成上链」的表述）
  * `GET /crossex/rule/risk_limits` 返回：`CrossexRiskLimitTier` 新增必填字符串字段 `quick_cal_amount`（速算额）

**v4.106.56**

2026-03-31

  * 文档与翻译：修复英文 `messages.po` 重复条目与损坏的 `msgid`；对卡券中心两处超长 Markdown 说明清空不兼容的英文 `msgstr`（JSON 字面量中的 `%` 与 gettext 占位规则冲突，后续补全英文翻译）

**v4.106.55**

2026-03-30

  * 新增 `GET /api/v4/rebate/partner/data/aggregated` 接口（`getPartnerAgentDataAggregated`）— 合伙人代理数据聚合统计（返佣金额、交易量、净手续费、客户数；按业务类型可选返回交易人数）
  * 新增聚合返佣接口对应的 `PartnerDataAggregated`、`PartnerDataAggregatedResponse` 模型定义

**v4.106.54**

2026-03-20

  * 新增 `POST /api/v4/earn/autoinvest/plans/create` 接口 - 创建定投计划
  * 新增 `POST /api/v4/earn/autoinvest/plans/update` 接口 - 更新定投计划
  * 新增 `POST /api/v4/earn/autoinvest/plans/stop` 接口 - 停止定投计划
  * 新增 `POST /api/v4/earn/autoinvest/plans/add_position` 接口 - 立即加仓
  * 新增 `GET /api/v4/earn/autoinvest/coins` 接口 - 查询支持定投的币种
  * 新增 `POST /api/v4/earn/autoinvest/min_invest_amount` 接口 - 查询可投资的最小金额
  * 新增 `GET /api/v4/earn/autoinvest/plans/records` 接口 - 查询计划执行记录
  * 新增 `GET /api/v4/earn/autoinvest/orders` 接口 - 查询计划执行记录详情（订单明细）
  * 新增 `GET /api/v4/earn/autoinvest/config` 接口 - 查询投资币种配置
  * 新增 `GET /api/v4/earn/autoinvest/plans/detail` 接口 - 查询定投计划详情
  * 新增 `GET /api/v4/earn/autoinvest/plans/list_info` 接口 - 查询定投计划列表

**v4.106.52**

2026-03-29

  * `FuturesInitialOrder` 模型：新增可选 `amount` 字段（字符串），用于小数合约张数；与 `size` 同时存在时以 `amount` 为准
  * `FuturesUpdatePriceTriggeredOrder` 模型：新增可选 `amount` 字段（字符串），语义与 `size` 相同
  * `SpotPricePutOrder` 模型：将 `time_in_force` 列入必填字段

**v4.106.51**

2026-03-27

  * 文档站点新增 **Gate for AI 开发者指南** 菜单：全面指导 AI Agent 通过 MCP（Model Context Protocol）协议与 CLI 工具接入 Gate API
  * 文档包含：MCP 服务端点、AI Skills（40+ 预置工作流）、接入方式（Cursor、Claude、CLI）、鉴权方式、代码示例等

**v4.106.50**

2026-03-26

  * 下线理财 ETH2 质押相关接口：`POST /earn/staking/eth2/swap`（swapETH2）、`GET /earn/staking/eth2/rate_records`（rateListETH2）
  * 下线理财结构性产品相关接口：`GET /earn/structured/products`（listStructuredProducts）、`GET /earn/structured/orders`（listStructuredOrders）、`POST /earn/structured/orders`（placeStructuredOrder）
  * 随上述接口下线同步移除 Earn 侧的模型文档与示例载荷

**v4.106.49**

2026-03-25

  * 新增 `FuturesOrderTimerange` 模型；`GET /futures/{settle}/orders_timerange` 返回列表项数据结构由 `FuturesOrder` 调整为 `FuturesOrderTimerange`
  * `FuturesOrder` 模型的 `order_value`、`trade_value` 保持只读，并在轻量化 SDK 中默认隐藏以降低噪音
  * `GET /futures/{settle}/orders/{order_id}`：优化路径参数说明（按订单 ID / 自定义 `text` 查询的规则）

**v4.106.48**

2026-03-25

  * `Currency` 模型：新增 `category` 字段（字符串数组，币种分类，取值示例见字段说明：stocks/metals/indices/forex/commodities 等）

**v4.106.45**

2026-03-20

  * `BatchOrder` 模型：完善 `finish_as` 字段 `ioc` 和 `poc` 枚举值描述，准确反映基于 time_in_force 设置的订单撤销原因
  * `Order` 模型：完善 `finish_as` 字段 `ioc` 和 `poc` 枚举值描述，准确反映基于 time_in_force 设置的订单撤销原因
  * `UnifiedAccount` 模型：新增 `mode` 字段（统一账户模式：经典账户/跨币种保证金/组合保证金/单币种保证金）
  * `UnifiedAccount` 模型：新增 `balance_version` 字段（余额版本号）
  * `UnifiedAccount` 模型：优化 `available`、`freeze`、`equity`、`iso_balance` 等多个保证金相关字段的描述
  * 更新 `UidPushWithdrawalResp` 模型：`id` 字段类型从 `integer` (int64) 变更为 `string`
  * CrossEx API `GET /crossex/fee` 费率接口：响应结构调整为数组形式，支持返回多个交易所（BINANCE、OKX、GATE、BYBIT）的费率信息，新增 `exchange_type` 字段标识交易所类型
  * CrossEx API `POST /crossex/convert` 闪兑接口：响应新增 `order_id`（订单号）和 `text`（订单号文本）字段
  * CrossEx API 利率扣息类型说明优化：`interest_type` 字段新增 `PERIODIC_ISOLATED` 枚举值（整点负债收息）

**v4.106.44**

2026-03-20

  * 更新 TradFi API：`GET /tradfi/symbols/detail`（`querySymbolDetail`）改为需认证的私有接口（不再支持匿名读取）

**v4.106.43**

2026-03-19

  * 新增理财定期 API：`GET /earn/fixed-term/product`（listEarnFixedTermProducts）、`GET /earn/fixed-term/product/{asset}/list`（listEarnFixedTermProductsByAsset）、`POST /earn/fixed-term/user/lend`（createEarnFixedTermLend）、`GET /earn/fixed-term/user/lend`（listEarnFixedTermLends）、`POST /earn/fixed-term/user/pre-redeem`（createEarnFixedTermPreRedeem）、`GET /earn/fixed-term/user/history`（listEarnFixedTermHistory）
  * `FuturesUpdatePriceTriggeredOrder` 模型：`order_id` 字段新增 `format: int64`
  * 合约价格触发委托（期货自动下单）接口：文档中响应里的订单标识字段增补 **`format: int64`** 说明；全站复用的查询参数 **`pos_margin_mode`** 与 **`dual_side`** 在引用场景中改为必填要求

**v4.106.42**

2026-03-19

  * `UnifiedAccount` 模型：新增 `mode` 字段（统一账户模式：经典账户/跨币种保证金/组合保证金/单币种保证金）
  * `UnifiedAccount` 模型：新增 `balance_version` 字段（余额版本号）
  * `UnifiedAccount` 模型：优化 `available`、`freeze`、`equity`、`iso_balance` 等多个保证金相关字段的描述

**v4.106.38**

2026-03-14

  * 更新 `amendOptionsOrder` 请求体：新增必填字段 `contract`（期权合约名称）

**v4.106.36**

2026-03-13

  * 新增 `PUT /options/orders/{order_id}` 期权改单接口（amendOptionsOrder）
  * 更新 TradFi API：`GET /tradfi/users/mt5-account` 改为需认证的私有接口（不再支持匿名读取）

**v4.106.34**

2026-03-12

  * 更新 Alpha API `/alpha/orders` 查询订单接口：`currency`、`side`、`status` 参数从必填改为选填
  * CrossEx API 新增支持 BYBIT 交易所

**v4.106.33**

2026-03-10

  * `BrokerCommission`、`BrokerTransaction` 模型：`source` 字段新增 `TradFi` 类型（返佣交易类型：Spot、Futures、Options、Alpha、TradFi）

**v4.106.32**

2026-03-05

  * 更新 P2P Merchant API：请求内容类型从 `multipart/form-data` 改为 `application/json`，并在文档中以结构化 JSON 描述各请求体字段（无需再上传 multipart 表单）
  * 更新 P2P Merchant API：取消逐接口「匿名可调用」特例，与各业务线一致的 **API Key + 签名（`KEY` / `SIGN`）**流程对齐
  * 更新 P2P Merchant API：`complete_rate_month`、`orders_buy_rate_month`、`transactions_month`、`transactions_all` 字段类型从 `integer` 改为 `number`

**v4.106.31**

2026-03-03

  * `PUT /futures/{settle}/price_orders/{order_id}` 接口路径变更为 `PUT /futures/{settle}/price_orders/amend/{order_id}`
  * `FuturesUpdatePriceTriggeredOrder` 模型：`order_id` 字段类型从 `string` 变更为 `integer`
  * `BatchOrder` 模型：`finish_as` 字段新增枚举值：`liquidate_cancelled`（爆仓撤销）、`small`（数量太小）、`depth_not_enough`（深度不足）、`trader_not_enough`（对手方不足）、`poc`（未满足挂单策略）、`fok`（未完全成交）、`price_protect_cancelled`（价格保护撤单）、`unknown`（未知）
  * `Order` 模型：更新 `cancelled_reason` 字段中 `ioc` 枚举值的描述，明确该状态也适用于 poc/rvt/rat/rpi 类型订单被判定为 taker 而拒绝的场景

**v4.106.30**

2026-03-03

  * `PUT /futures/{settle}/price_orders/{order_id}` 接口路径变更为 `PUT /futures/{settle}/price_orders/amend/{order_id}`
  * `FuturesUpdatePriceTriggeredOrder` 模型：`order_id` 字段类型从 `string` 变更为 `integer`

**v4.106.29**

2026-03-02

  * CrossEx API 所有接口路径新增 `/crossex` 前缀
  * `POST /crossex/orders` 接口：限频描述新增最大挂单数限制（1,000 个）
  * `GET /crossex/positions/leverage` 接口：响应结构从数组改为 Map
  * `GET /crossex/margin_positions/leverage` 接口：响应结构从数组改为 Map
  * 平仓接口从 `DELETE /position` 变更为 `POST /crossex/position`
  * `POST /unified/portfolio_calculator` 接口：更新描述，支持所有已开放期权交易的标的物币种
  * `MockSpotBalance` 模型：`equity` 字段描述移除币种限制
  * `MockSpotOrder` 模型：`count` 字段描述移除币种限制
  * `MockFuturesPosition`、`MockFuturesOrder` 模型：`contract` 字段描述更新为支持所有已开放期权交易的标的物的USDT永续合约
  * `MockOptionsPosition`、`MockOptionsOrder` 模型：`options_name` 字段描述更新为支持所有期权合约市场

**v4.106.28**

2026-02-28

  * 更新翻译内容，优化TradFi文档描述

**v4.106.27**

2026-02-26

  * 新增闪兑相关错误码文档
  * 新增币种 `total_supply`（总供应量）和 `market_cap`（市值）字段描述
  * `Contract` 模型：新增 `funding_impact_value` 字段（资金费用深度影响额）
  * `FuturesBBOOrder` 模型：删除 `limit_vip` 字段

**v4.106.26**

2026-02-12

  * 新增 P2P Merchant API 接口：`POST /p2p/merchant/books/ads_list`（获取广告列表）

**v4.106.25**

2026-02-11

  * `POST /earn/dual/orders`：拆分展示下单请求载荷与返回值结构
  * 双币申购参数 `PlaceDualInvestmentOrderParams` 与成交返回 `PlaceDualInvestmentOrder`（补充 `id`、`copies`、`invest_amount`、`settlement_amount`、`create_time`、`complete_time`、`status`、`invest_currency`、`exercise_currency`、`exercise_price`、`settlement_price`、`settlement_currency`、`apy_display`、`apy_settlement`、`delivery_time` 等字段）在文档中分别描述
  * **`GET /earn/dual/investment_plan`** ：计划项中的 `per_value` 标记为废弃字段

**v4.106.24**

2026-02-09

  * 新增 OTC API 接口：`POST /otc/quote`（法币和稳定币询价）、`POST /otc/order/create`（法币下单）、`POST /otc/stable_coin/order/create`（稳定币下单）、`GET /otc/get_user_def_bank`（获取用户默认银行卡信息）、`GET /otc/bank_list`（获取用户银行卡列表）、`POST /otc/order/paid`（法币订单设置已付款）、`POST /otc/order/cancel`（法币订单取消）、`GET /otc/order/list`（法币订单列表）、`GET /otc/stable_coin/order/list`（稳定币订单列表）、`GET /otc/order/detail`（法币订单详情）

**v4.106.23**

2026-02-06

  * `OptionsOrder`：`id` 字段按大整型语义书写，文档补充 JavaScript/TypeScript bigint 场景的解析说明

**v4.106.22**

2026-02-03

  * `Order` 模型：新增 `price_protect_cancelled` 状态，表示因价格保护导致撤单的订单

**v4.106.21**

2026-02-03

  * 更新子账户划转及划转记录相关 `amount` 字段描述

**v4.106.20**

2026-02-02

  * 新增合约追踪委托接口：`POST /futures/{settle}/autoorder/v1/trail/create`、`POST /futures/{settle}/autoorder/v1/trail/stop`、`POST /futures/{settle}/autoorder/v1/trail/stop_all`、`GET /futures/{settle}/autoorder/v1/trail/list`、`GET /futures/{settle}/autoorder/v1/trail/detail`、`POST /futures/{settle}/autoorder/v1/trail/update`、`GET /futures/{settle}/autoorder/v1/trail/change_log`
  * 新增 `TrailOrder`、`TrailChangeLog` 模型（追踪委托及改单记录）
  * `SwapCoin` 模型：`side` 字段类型改为 integer（0-质押、1-赎回），移除 `pid` 的 int32 格式限制
  * 新增 `BatchFundingRatesRequest`、`BatchFundingRatesResponse` 模型（批量查询资金费率的请求/响应结构）
  * `FuturesAccount` 模型：删除 `cross_settle` 字段
  * `TotalBalance` 模型：新增账户类型（`meme_box`、`options`、`payment`）
  * `UnifiedMarginTiers` 模型：修复描述格式
  * `GET /futures/{settle}/funding_rate` 接口：时间间隔枚举新增 `10s` 选项

**v4.106.19**

2026-01-27

  * `Contract` 模型，新增 `enable_decimal` 字段，用于标识是否支持小数字符串类型合约张数。当该字段为 `true` 时，表示该合约支持小数张数（即 `size` 字段可以使用小数字符串类型）；当为 `false` 时，表示该合约不支持小数张数（即 `size` 字段只能使用整数类型）

**v4.106.18**

2026-01-26

  * 更新 API 文档：添加现货限频规则说明章节，包括现有限频规则、新增限频规则和成交率计算公式
  * 新增 P2P Merchant API 接口：`POST /p2p/merchant/account/get_user_info`（获取账户信息）、`POST /p2p/merchant/account/get_counterparty_user_info`（获取对手方信息）、`POST /p2p/merchant/account/get_myself_payment`（获取支付方式列表）、`POST /p2p/merchant/transaction/get_pending_transaction_list`（获取进行中订单）、`POST /p2p/merchant/transaction/get_completed_transaction_list`（获取所有/历史订单）、`POST /p2p/merchant/transaction/get_transaction_details`（查询订单详情）、`POST /p2p/merchant/transaction/confirm-payment`（确认付款）、`POST /p2p/merchant/transaction/confirm-receipt`（确认收款）、`POST /p2p/merchant/transaction/cancel`（取消订单）、`POST /p2p/merchant/books/place_biz_push_order`（发布广告挂单）、`POST /p2p/merchant/books/ads_update_status`（广告单状态更新）、`POST /p2p/merchant/books/ads_detail`（查询广告详情）、`POST /p2p/merchant/books/my_ads_list`（获取我的广告列表）、`POST /p2p/merchant/chat/get_chats_list`（获取聊天记录）、`POST /p2p/merchant/chat/send_chat_message`（发送文本消息）、`POST /p2p/merchant/chat/upload_chat_file`（上传聊天文件）

**v4.106.17**

2026-01-22

  * `GET /loan/multi_collateral/currency_quota` 接口，`CurrencyQuota` 模型新增两个返回字段：`left_quota_fixed`（定期币种剩余`可借/质押`限额）和 `left_quote_usdt_fixed`（定期币种换算成USDT的剩余币种限额）
  * 下线：移除单币抵押借币 API 接口（`/loan/collateral/**`）。这些接口已不再可用。
  * `FuturesUpdatePriceTriggeredOrder` 模型：`order_id` 字段类型修改为字符串，新增 `close` 字段
  * `SpotPriceTrigger` 模型：`expiration` 字段从必填项中移除

**v4.106.16**

2026-01-20

  * 更新订单状态文案：标准化订单对象（涵盖 `BatchOrder`、`InternalOrder`、`Order`、`OrderCancel` 以及组合保证金场景的 `PortfolioSpotOrders`）中 `closed` 含义，由「全部成交」调整为更贴近语义的「已结束的订单」，避免误以为必须完全成交才算 closed

**v4.106.15**

  * 添加crossex菜单、其子菜单websocket和rest页
  * 新增完整的crossex API端点，支持跨交易所交易，包括订单管理、仓位管理、账户管理和历史数据查询
  * 实现crossex WebSocket支持，提供实时市场数据和订单更新

**v4.106.14**

  * `Order` 模型，`text` 字段描述更新，补充强平订单场景说明（`pm_liquidate`、`comb_margin_liquidate`、`scm_liquidate` 这三种场景代表全仓强平订单，`liquidate` 代表逐仓强平订单）
  * `Trade` 模型，`text` 字段描述更新，补充强平订单场景说明（`pm_liquidate`、`comb_margin_liquidate`、`scm_liquidate` 这三种场景代表全仓强平订单，`liquidate` 代表逐仓强平订单）

**v4.106.13**

  * 新增 OTC API 接口：`POST /otc/quote`（法币和稳定币询价）、`POST /otc/order/create`（法币下单）、`POST /otc/stable_coin/order/create`（稳定币下单）、`GET /otc/get_user_def_bank`（获取用户默认银行卡信息）、`POST /otc/order/paid`（法币订单设置已付款）、`POST /otc/order/cancel`（法币订单取消）、`GET /otc/order/list`（法币订单列表）、`GET /otc/stable_coin/order/list`（稳定币订单列表）、`GET /otc/order/detail`（法币订单详情）、`GET /otc/stable_coin/order/detail`（稳定币订单详情）、`GET /otc/get_api_order_uid`（获取通过api/v4接口下单的用户）
  * OTC REST 文档：请求体一律使用 JSON（`application/json`，替代 `multipart/form-data`），补充常见成功/失败的说明段落，强调需在登录状态下调用并更新基础域名与签名指引，与新列出的 OTC 路由配套阅读

**v4.106.12**

  * 新增 `GET /earn/dual/balance` 接口，查询双币理财资产
  * 新增 `GET /futures/{settle}/get_leverage/{contract}` 接口，获取指定模式的杠杆信息
  * 新增 `POST /futures/{settle}/positions/{contract}/set_leverage` 接口，更新指定模式的杠杆，简化leverage接口复杂逻辑
  * 新增 `POST /futures/{settle}/set_position_mode` 接口，设置持仓模式，替换dual_mode接口
  * `POST /futures/{settle}/positions/{contract}/reverse` 接口，新增 `pos_margin_mode` 参数（仓位保证金模式，分仓模式必传，取值isolated/cross）
  * `FuturesAccount` 模型，新增 `enable_dual_plus` 字段，表示是否支持分仓模式
  * `FuturesAccount` 模型，`position_mode` 字段描述更新，明确持仓模式：single-单向持仓，dual-双向持仓，dual_plus-分仓
  * `FuturesOrder` 模型，新增 `pos_margin_mode` 字段，表示仓位保证金模式（isolated - 逐仓, cross - 全仓，只在简易分仓模式下传递）
  * `Position` 模型，新增 `pos_margin_mode` 字段，表示仓位保证金模式（isolated - 逐仓, cross - 全仓）
  * `Position` 模型，新增 `lever` 字段，表示仓位当前杠杆，逐仓和全仓都可以该字段表示，逐步替换当前的leverage和cross_leverage_limit
  * 新增 `FuturesLeverage` 模型定义，用于杠杆查询响应

**v4.106.11**

  * `BatchOrder`、`CurrencyPair`、`Order` 模型中 `slippage` 字段描述更新，明确为现货市价下单支持的最大滑点比率，以下单时的市场最新价格为基准计算（示例：0.03即3%）
  * `POST /spot/batch_orders` 接口，响应描述更新，说明响应包含多个订单对象，订单对象具体结构参考 `/spot/orders` 下单接口的结构

**v4.106.10**

  * `GET /account/rate_limit` 接口，新增描述说明该接口暂未开放使用
  * `GET /wallet/order_status` 接口，更新接口说明和描述，明确为查询主子账户划转状态

**v4.106.9**

  * `PUT /futures/{settle}/price_orders/{order_id}` 接口，修复请求体模型 `FuturesUpdatePriceTriggeredOrder` 字段名错误：`contact` 字段改为 `order_id`，并将 `order_id` 字段标记为必填
  * `POST /loan/collateral/orders` 接口标记为已废弃/下线

**v4.106.8**

  * `Contract` 模型，新增 `market_order_slip_ratio` 字段，表示合约市价下单支持的最大滑点比率，比率计算以市场最新价格为基准
  * `Contract` 模型，新增 `market_order_size_max` 字段，表示合约市价下单支持的最大张数，默认值为0，为默认值时取`order_size_max`字段作为最大张数限制
  * `FuturesOrder` 模型，新增 `market_order_slip_ratio` 字段，表示市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置
  * `BatchFuturesOrder` 模型，新增 `market_order_slip_ratio` 字段，表示订单响应中返回的最大滑点比率

**v4.106.7**

  * `Contract` 模型，新增 `market_order_slip_ratio` 字段，表示合约市价下单支持的最大滑点比率，比率计算以市场最新价格为基准
  * `Contract` 模型，新增 `market_order_size_max` 字段，表示合约市价下单支持的最大张数，默认值为0，为默认值时取`order_size_max`字段作为最大张数限制
  * `FuturesOrder` 模型，新增 `market_order_slip_ratio` 字段，表示市价下单自定义最大滑点比率，不传和未返回表示使用合约默认配置
  * `BatchFuturesOrder` 模型，新增 `market_order_slip_ratio` 字段，表示订单响应中返回的最大滑点比率
  * `GET /unified/batch_borrowable` 接口，`currencies` 参数添加 `style: form` 和 `explode: false`，优化数组参数格式
  * `GET /unified/estimate_rate` 接口，`currencies` 参数添加 `style: form` 和 `explode: false`，优化数组参数格式
  * `GET /loan/multi_collateral/current_rate` 接口，`currencies` 参数添加 `style: form` 和 `explode: false`，优化数组参数格式
  * 更新限频规则文档：在钱包私有接口限频规则中新增 `POST /withdrawals/push` 接口限频说明（1r/10s）

**v4.106.6**

  * `GET /options/order_book` 接口响应模型从 `FuturesOrderBook` 更新为 `OptionsOrderBook`，实现期权与合约 API 的更好分离
  * `GET /options/trades` 接口响应模型从 `FuturesTrade` 更新为 `OptionsTrade`，实现期权与合约 API 的更好分离
  * `GET /options/candlesticks` 接口响应模型从 `FuturesCandlestick` 更新为 `OptionsCandlestick`，实现期权与合约 API 的更好分离
  * 新增 `OptionsOrderBook` 和 `OptionsTrade` 模型定义，为期权 API 响应提供专门的模型

**v4.106.5**

  * 新增资产流水编码：`150102`（币种回购-扣款）、`150101`（币种回购-加款）、`143`（币种更名扣款）、`144`（币种更名加款）、`707`（现货同币种结算-转出）、`708`（现货同币种结算-转入）

**v4.106.4**

  * `CurrencyPair` 模型，新增 `up_rate` 和 `down_rate` 字段，展示报价最大涨跌幅百分比
  * `Contract` 模型，新增 `funding_rate_limit` 字段，表示资金费率上限值

**v4.106.3**

  * `GET /futures/{settle}/accounts` 接口说明更新，支持查询经典合约账户和统一账户
  * `PUT /futures/{settle}/accounts` 接口，`enable_evolved_classic` 字段标记为已废弃
  * `GET /futures/{settle}/positions/{contract}` 接口说明更新，明确在同一合约市场下持有双向仓位时的查询方式
  * `POST /futures/{settle}/positions/{contract}/margin` 接口说明更新，附加新风险限额规则链接，说明应使用杠杆调整接口而非直接修改保证金
  * `POST /futures/{settle}/positions/{contract}/leverage` 接口参数说明更新，明确 `leverage` 参数（用于逐仓，需要 `cross_leverage_limit` 为空）和 `cross_leverage_limit` 参数（用于全仓，需要 `leverage` 设为 0）
  * `POST /futures/{settle}/dual_comp/positions/{contract}/risk_limit` 接口说明更新，附加风险限额规则链接
  * `GET /options/accounts` 接口说明更新，支持查询经典期权账户和统一账户
  * `Position` 模型字段描述更新，优化杠杆和风险管理相关说明：`leverage`（逐仓杠杆倍数，0 表示全仓模式）、`leverage_max`（基于当前仓位规模的最大杠杆）、`maintenance_rate`（梯度式维持保证金率计算）、`liq_price`（预估强平价，仅供参考）、`initial_margin` 和 `maintenance_margin`（扩大适用范围说明）、`realised_pnl`（详细说明包含平仓结算、资金费和手续费）、`pnl_pnl`（平仓结算盈亏）、`pnl_fund`（资金费盈亏）、`pnl_fee`（总手续费）、`history_pnl`（所有历史平仓结算盈亏）、`cross_leverage_limit`（简化说明）
  * `FuturesAccount` 和 `DeliveryAccount` 模型更新：`total` 字段更新说明"仅适用于经典合约账户"，`position_margin` 标记为已废弃，`order_margin` 更新为"所有未完成订单的起始保证金"，`enable_evolved_classic` 和 `enable_new_dual_mode` 标记为已废弃，`margin_mode` 枚举值扩展新增值 3（单币种保证金模式）
  * `OptionsAccount` 模型更新：`total` 和 `equity` 字段添加统一账户限制说明，`liq_triggered` 描述更新为"账户是否处于强平状态"，`margin_mode` 枚举值扩展新增值 3，`unrealised_pnl` 描述增强附带计算公式
  * `MarginAccount` 模型更新：`account_type` 描述更新删除"risk"选项，`risk` 字段标记为已废弃，`mmr` 描述优化
  * `Contract` 和 `DeliveryContract` 模型更新：`quanto_multiplier` 概念更新为"合约乘数"，`maintenance_rate` 明确为"第一档维持保证金率要求"，`mark_type` 和 `funding_cap_ratio` 标记为已废弃，`mark_price_round` 简化为"标记价格的最小单位"
  * `OptionsContract` 模型更新：`tag` 更新为"到期周期，有 day、week、month"，`multiplier` 更新为"期权合约乘数"，`underlying_price` 更新为"对应交割日期的远期期货价格"，`mark_price_round` 简化说明，`order_price_deviate` 和 `trade_id` 标记为已废弃，`orders_limit` 优化为"每个用户在该盘口最多可挂的订单数量"
  * `FuturesTicker` 和 `DeliveryTicker` 模型更新：`quanto_base_rate` 字段标记为已废弃
  * `OptionsTicker` 模型更新：`leverage` 计算公式更新并添加参考说明
  * `FuturesTrade` 和 `DeliveryTrade` 模型更新：`is_internal` 字段标记为已废弃
  * `OptionsMyTrade` 和 `OptionsPosition` 模型更新：`underlying_price` 字段更新为"对应交割日期的远期期货价格"
  * `PositionTimerange` 模型更新：`leverage_max` 和 `maintenance_rate` 描述优化
  * `FuturesAutoDeleverage` 模型更新：`leverage` 和 `cross_leverage_limit` 描述明确，更好理解保证金模式
  * 风险限额梯度模型更新（`FuturesRiskLimitTier`、`FuturesLimitRiskTiers`、`DeliveryLimitRiskTiers`）：统一 `maintenance_rate` 描述为"第一档维持保证金率要求"
  * `MarginLeverageTier` 模型更新：优化 `upper_limit`（基于杠杆的最大借币限额）、`mmr`（梯度保证金要求下的综合维持保证金率）和 `leverage`（基于当前负债规模的最大杠杆倍数）描述
  * `CreateUniLoan` 和 `UniLoanInterestRecord` 模型更新：`type` 字段描述更新为"借贷类型，margin 表示为杠杆借币"

**v4.106.2**

  * 新增 `GET /wallet/getLowCapExchangeList` 接口，获取低价值币种列表

**v4.106.1**

  * `Position` 和 `FuturesAutoDeleverage` 模型中 `leverage` 和 `cross_leverage_limit` 字段描述更新，明确全仓/逐仓模式下的使用说明
  * `POST /futures/{settle}/positions/{contract}/leverage` 接口中 `leverage` 和 `cross_leverage_limit` 参数描述更新，明确使用要求
  * `PUT /sub_accounts/{user_id}/keys/{key}` 接口说明更新，提示此接口无法修改 `mode` 账户类型属性

**v4.106.0**

  * 为解决支持小数下单问题，将所有 Futures 相关接口中的 size、数量相关字段从 `integer` 类型统一改为 `string` 类型。受影响的模型包括：`FuturesOrder`（`size`、`iceberg`、`left`）、`BatchFuturesOrder`（`size`、`iceberg`、`left`）、`Position`（`size`、`trade_long_size`、`trade_short_size`）、`PositionTimerange`（`size`）、`MyFuturesTrade`（`size`、`close_size`）、`MyFuturesTradeTimeRange`（`size`、`close_size`）、`FuturesTrade`（`size`）、`FuturesOrderBook`（`asks` 和 `bids` 中的 `size`）、`FuturesCandlestick`（`v`）、`FuturesLiquidate`（`size`、`order_size`）、`FuturesLiqOrder`（`position_size`、`size`、`order_size`）、`FuturesAutoDeleverage`（`size`、`entry_size`）、`FuturesCollusionOrder`（`size`、`left`）、`FuturesBatchAmendOrderRequest`（`size`）、`Contract`（`order_size_min`、`order_size_max`、`trade_size`、`position_size`）、`ContractStat`（`long_liq_size`、`short_liq_size`、`open_interest`）
  * `Position` 模型中新增 `pid` 字段，用于分仓仓位 ID
  * 所有语言 SDK（Go、C#、Java、Python、PHP、TypeScript）统一添加 `X-Gate-Size-Decimal: 1` 默认请求头，确保服务端正确处理 size 字段
  * 新建 12 个独立的 Delivery Schema 文件，用于分离 Delivery 和 Futures 对象：`DeliveryAccount`、`DeliveryAccountBook`、`DeliveryOrder`、`DeliveryOrderBook`、`DeliveryPosition`、`DeliveryPositionClose`、`DeliveryTrade`、`DeliveryMyTrade`、`DeliveryLiquidate`、`DeliveryInsuranceRecord`、`DeliveryLimitRiskTiers`、`DeliveryCloseAllPositionsResponse`

**v4.105.32**

  * `POST /futures/{settle}/positions/{contract}/leverage` 接口描述更新，新增仓位模式切换规则详解、使用示例和风险警告，提升接口使用的安全性和清晰度

**v4.105.31**

  * `TradeFee` 模型中 `taker_fee` 和 `maker_fee` 字段描述更新，明确为现货交易费率

**v4.105.29**

  * `GET /spot/my_trades` 接口响应中新增 `deal` 字段，显示本次成交总额
  * `GET /unified/accounts` 接口响应中新增 `options_order_loss` 字段，显示期权挂单损失（单位USDT），在组合保证金模式下有效，接口响应中 `spot_order_loss` 字段描述更新，明确表示现货挂单损失，在跨币种模式和组合保证金模式下有效， `cross_balance` 和 `iso_balance` 字段描述更新，现在在单币种保证金模式、跨币种保证金模式下均有效

**v4.105.28**

  * `DELETE /withdrawals/{withdrawal_id}` 接口响应中新增 `block_number` 字段，显示区块编号
  * `GET /unified/accounts` 接口响应中 `cross_balance` 和 `iso_balance` 字段描述更新，现在在单币种保证金模式、跨币种保证金模式下均有效

**v4.105.27**

  * 更新 `DepositRecord`、`WithdrawalRecord` 和 `WithdrawalsDel` 模型中 `status` 字段的描述，使其更加清晰
  * 充值状态枚举中移除 `FINAL` 状态，优化 `DONE` 状态描述

**v4.105.24**

  * `GET /wallet/currency_chains` 接口描述更新，流通性或者价值极低的币种不支持api操作，请通过Web或App页面进行查询以及处理
  * `GET /wallet/withdraw_status` 接口描述更新，流通性或者价值极低的币种不支持api操作，请通过Web或App页面进行查询以及处理

**v4.105.20**

  * `DELETE /withdrawals/{withdrawal_id}` 接口响应模型更新为使用 `WithdrawalsDel` 结构
  * `GET /wallet/deposits` 接口响应中新增 `BLOCKED`、`DEP_CREDITED`、`FINAL` 状态值
  * `GET /wallet/currency_chains` 接口响应中新增 `is_deposit_disabled` 字段

**v4.105.19**

  * `GET /spot/currency_pairs` 和 `GET /spot/currency_pairs/{currency_pair}` 接口，`fee` 字段标记为已废弃
  * `POST /earn/staking/eth2/swap` 接口描述从"ETH2兑换"更新为"ETH兑换"，ETH2更名为GTETH
  * `GET /earn/staking/eth2/rate_records` 接口描述更新为查询GTETH历史收益率

**v4.105.18**

  * 新增 `PUT /futures/{settle}/price_orders` 接口，用于修改单个价格触发订单
  * 修改价格触发订单请求中新增 `settle`、`order_id`、`size`、`price`、`trigger_price`、`price_type` 和 `auto_size` 参数

**v4.105.11**

  * 新增 `GET /account/main_keys` 接口，查询主账户所有API Key信息
  * `GET /spot/currency_pairs` 和 `GET /spot/currency_pairs/{currency_pair}` 接口，`fee` 字段标记为已废弃

**v4.105.10**

  * 新增 `POST /futures/{settle}/bbo_orders` 接口，档位BBO合约下单功能
  * `POST /futures/{settle}/price_orders` 接口，合约价格触发单中的 `price` 和 `rule` 字段更新为必填

**v4.105.9**

  * `GET /futures/{settle}/positions` 接口，返回值增加 `settlement_currency` 字段，支持多结算币种
  * `POST /earn/uni/lends` 接口，请求参数新增 `auto_renew` 字段，支持自动续借功能
  * `GET /spot/trades` 接口，查询参数新增 `trade_type` 字段，支持按交易类型过滤

**v4.105.8**

  * `GET /unified/accounts` 接口，返回值增加 `margin_mode` 字段，标识账户保证金模式
  * `GET /spot/my_trades` 接口，返回值增加 `fee_currency` 字段，显示手续费币种

**v4.105.7**

  * `GET /futures/{settle}/positions` 接口，返回值增加 `liquidation_price` 字段，用于风险管理
  * `POST /spot/orders` 接口，请求参数新增 `stop_loss` 和 `take_profit` 字段，支持高级订单类型
  * `GET /unified/accounts` 接口，返回值增加 `total_balance` 字段，显示总余额

**v4.105.6**

  * 新增 `GET /wallet/saved_address` 接口，查询已保存的提现地址
  * `GET /wallet/withdrawals` 接口，返回值增加 `network_fee` 字段，显示网络手续费
  * `GET /spot/currency_pairs` 接口，返回值增加 `min_amount` 和 `max_amount` 字段，显示交易限额

**v4.105.5**

  * `GET /futures/{settle}/orders` 接口，返回值增加 `order_type` 字段，区分订单类型
  * `GET /spot/candlesticks` 接口，`interval` 参数新增支持 `30s` 时间间隔
  * `GET /margin/accounts` 接口，返回值增加 `available_balance` 字段，显示可用余额

**v4.105.4**

  * `GET /futures/{settle}/tickers` 接口，返回值增加 `funding_rate_next` 字段，显示下期资金费率
  * `GET /unified/accounts` 接口，返回值增加 `cross_leverage` 字段，显示全仓杠杆倍数

**v4.105.3**

  * `GET /futures/{settle}/positions` 接口，查询参数新增 `position_side` 字段，支持对冲模式
  * `GET /earn/dual/orders` 接口，查询参数新增 `investment_type` 字段，按投资类型过滤
  * `GET /futures/{settle}/accounts` 接口，返回值增加 `unrealized_pnl` 字段，显示未实现盈亏

**v4.105.2**

  * `GET /spot/fee` 接口，返回值增加 `maker_fee_rate` 和 `taker_fee_rate` 字段，显示手续费率
  * `GET /futures/{settle}/contracts` 接口，返回值增加 `settle_currency` 字段，显示结算币种

**v4.105.1**

  * `POST /futures/{settle}/orders` 接口，请求参数新增 `time_in_force` 字段，设置订单有效期类型
  * `GET /wallet/deposits` 接口，查询参数新增 `network` 字段，按网络过滤充值记录

**v4.105.0**

  * `GET /unified/accounts` 接口，返回值增加 `portfolio_margin` 字段，显示组合保证金信息
  * `POST /futures/{settle}/positions/mode` 接口，请求参数新增 `position_mode` 字段，设置持仓模式

**v4.104.9**

  * `POST /futures/{settle}/orders` 接口，请求参数新增 `reduce_only` 字段，支持只减仓订单
  * `GET /spot/orders` 接口，查询参数新增 `account_type` 字段，按账户类型过滤
  * `GET /futures/{settle}/accounts` 接口，返回值增加 `funding_balance` 字段，显示资金余额

**v4.104.8**

  * `GET /earn/uni/currencies` 接口，返回值增加 `apr` 字段，显示年化收益率
  * `GET /earn/dual/investment_plan` 接口，返回值增加 `lock_period` 字段，显示锁定期

**v4.104.7**

  * `GET /spot/order_book` 接口，返回值增加 `order_book_id` 字段，用于订单簿版本控制
  * `POST /wallet/transfers` 接口，请求参数新增 `client_order_id` 字段，支持客户端订单ID
  * `GET /spot/accounts` 接口，返回值增加 `trading_fee_rate` 字段，显示交易手续费率

**v4.104.6**

  * `GET /futures/{settle}/tickers` 接口，返回值增加 `mark_price` 字段，显示标记价格
  * 新增 `GET /futures/{settle}/insurance` 接口，查询保险基金信息
  * `GET /futures/{settle}/positions` 接口，返回值增加 `isolated_margin` 字段，显示逐仓保证金

**v4.104.5**

  * `GET /spot/my_trades` 接口，返回值增加 `order_id` 字段，用于交易与订单关联
  * `GET /unified/loans` 接口，查询参数新增 `currency` 字段，按币种过滤借贷记录
  * `GET /unified/accounts` 接口，返回值增加 `borrow_amount` 字段，显示借贷金额

**v4.104.4**

  * `GET /spot/price_orders` 接口，返回值增加 `trigger_price` 字段，显示触发价格
  * `GET /futures/{settle}/contracts` 接口，返回值增加 `maintenance_rate` 字段，显示维持保证金率

**v4.104.3**

  * `GET /futures/{settle}/positions` 接口，查询参数新增 `hedge_mode` 字段，支持对冲模式查询
  * `GET /earn/dual/orders` 接口，查询参数新增 `status` 字段，按状态过滤订单
  * `GET /unified/accounts` 接口，返回值增加 `cross_margin_leverage` 字段，显示全仓杠杆倍数

**v4.104.2**

  * `GET /futures/{settle}/my_trades` 接口，返回值增加 `settlement_size` 字段，显示结算数量
  * 新增 `GET /wallet/total_balance` 接口，查询账户总余额
  * `GET /margin/accounts` 接口，返回值增加 `available_margin` 字段，显示可用保证金

**v4.104.1**

  * `POST /spot/orders` 接口，请求参数新增 `post_only` 字段，支持只做maker订单
  * `GET /futures/{settle}/orders` 接口，查询参数新增 `contract` 字段，按合约过滤订单
  * `GET /futures/{settle}/funding_rate` 接口，返回值增加 `funding_time` 字段，显示资金费率时间

**v4.104.0**

  * 新增 `GET /unified/risk_units` 接口，统一账户风险单位计算
  * `GET /unified/accounts` 接口，返回值增加 `risk_level` 字段，显示风险等级
  * `POST /unified/orders` 接口，请求参数新增 `auto_borrow` 字段，支持自动借贷

**v4.103.0**

  * `GET /spot/account_book` 接口新增 `code` 查询参数和响应字段，支持按特定编码过滤账户流水记录
  * `closeAllPositions` 操作新增 `text` 参数，支持在一键平仓时添加订单备注
  * 新增资产流水编码详细文档，包含超过300个交易编码的详细说明

**v4.102.6**

  * 优化赚币兑换响应结构 `SwapCoinStruct`，新增 `pid`、`subtype`、`exchange_amount`、`updateStamp`、`protocol_type`、`client_order_id`、`source` 字段

**v4.102.0**

  * `GET /unified/accounts`接口, 返回值增加`is_all_collateral`（是否所有币种均作为保证金）、balances下新增字段`enabled_collateral`（币种开启作为保证金）
  * 新增 `POST /unified/collateral_currencies` 接口，跨币种下可设置抵押币种

**v4.101.9**

  * 新增 `GET /futures/{settle}/risk_limit_table` 接口，根据table_id查询风险限额梯度表
  * 合约账户模型新增 `enable_tiered_mm` 字段，支持梯度式维持保证金计算
  * 持仓模型新增 `risk_limit_table`（风险限额表）和 `average_maintenance_rate`（平均维持保证金率）字段，增强风险管理
  * 合约风险限额梯度新增 `deduction` 字段，用于维持保证金速算扣减额
  * 新增模型：`FuturesRiskLimitTier`（风险限额梯度档位）和 `FuturesRiskLimitTierList`（风险限额梯度表列表）
  * 优化 `POST /earn/staking/swap` 接口响应结构，增强兑换订单详情信息

**v4.100.0**

  * 新增alpha账户查询和账户流水查询功能
  * 优化alpha API币种和ticker查询接口描述，参数使用说明
  * 新增 `GET /earn/staking/coins` 接口，查询链上赚币币种
  * 新增 `POST /earn/staking/swap` 接口，链上赚币兑换
  * 经纪商佣金和交易API新增 `sub_broker_info` 子经纪商信息对象字段

**v4.99.0**

  * `GET /spot/accounts` 接口, 返回值增加`refresh_time`字段
  * 移除 `PUT /earn/uni/interest_reinvest` 接口

**v4.98.0**

  * 新增 `/earn/uni/rate` 接口, 币种预估年化利率
  * `GET /spot/currency_pairs`、`GET /spot/currency_pairs/{currency_pair}`接口, 返回值增加`delisting_time`、`trade_url` 字段

**v4.97.0**

  * 新增 `GET /unified/batch_borrowable` 接口, 批量查询统一账户最多可借
  * `GET /spot/candlesticks` 接口, `interval`支持`1s`粒度
  * 新增 `GET /earn/uni/chart` 接口, 余币宝币种年化走势图
  * 新增 `POST /futures/{settle}/positions/cross_mode` 接口, 切换全逐仓模式

**v4.96.0**

  * `GET /futures/{settle}/accounts` 接口, 返回值新增`cross_margin_balance`,`cross_mmr`,`cross_imr`字段

**v4.95.0**

  * `GET /spot/account_book` 接口, 查询参数新增 `code` 字段,返回值增加 `code` 字段
  * 新增 `GET /unified/transferables` 接口, 批量查询统一账户最多可转出
  * 新增 `GET /margin/user/loan_margin_tiers` 接口, 查询当前市场下用户自身杠杆借贷梯度
  * 新增 `GET /margin/loan_margin_tiers` 接口, 查询当前市场杠杆借贷梯度
  * 新增 `POST /margin/leverage/user_market_setting` 接口, 设置用户市场杠杆倍数
  * 新增 `GET /margin/user/account` 接口, 查询用户逐仓杠杆账户列表

**v4.94.0**

  * 新增 `GET /unified/currencies` 接口, 统一账户支持的借贷币种列表
  * `GET /unified/accounts` 接口, 查询参数新增 `sub_uid` 字段

**v4.93.0**

  * `GET /earn/dual/investment_plan` 接口, 查询参数新增 `plan_id` 字段
  * `GET /earn/dual/orders` 接口, 查询参数新增 `from`、`to`、`page`、`limit` 字段;
  * `GET /earn/dual/orders` 接口, 返回值增加 `text` 字段
  * `POST /earn/dual/orders` 接口, 返回值增加 `text` 字段
  * 新增 `GET /earn/staking/eth2/rate_records` 接口, GTETH历史收益率查询

**v4.92.1**

2025-02-27

  * `GET /spot/currencies` 接口，返回值增加 `chains` 字段
  * `GET /spot/currencies/{currency}` 接口，返回值增加 `chains` 字段
  * `GET /spot/currencies` 接口，返回值废弃 `withdraw_disabled`、`withdraw_delayed`、`deposit_disabled` 字段
  * `GET /spot/currencies/{currency}` 接口，返回值废弃 `withdraw_disabled`、`withdraw_delayed`、`deposit_disabled` 字段

**v4.92.0**

2025-02-24

  * `GET /spot/currencies` 接口，返回值增加 `name` 字段
  * `GET /spot/currency_pairs` 接口，返回值增加 `base_name`、`quote_name` 字段
  * `GET /spot/price_orders` 接口, 查询参数新增 `unified` 类型
  * `GET /unified/accounts` 接口, 查询参数新增 `sub_uid` 字段

**v4.91.0**

2025-02-10

`2025-04-01` 之后我们将移除以下接口，请尽快迁移至新接口

**v4.90.0**

2025-01-20

  * `GET /wallet/push` 接口, 查询参数新增`transaction_type`
  * 新增 `GET /rebate/user/sub_relation` 接口, 查询指定用户是否在体系内
  * `GET /futures/{settle}/liq_orders` 接口, 返回值新增`order_size`字段
  * `GET /spot/currency_pairs` 接口，返回值增加 `type` 字段

**v4.88.0**

2024-12-24

  * 新增 `GET /spot/insurance_history` 接口, 查询现货保险基金历史数据
  * `GET /unified/accounts` 接口，返回值增加 `cross_balance`、`iso_balance`、`im`、`mm`、`imr`、`mmr`、`margin_balance`、`available_margin`
  * `PUT /unified/unified_mode` 接口，新增单币种保证金模式

**v4.87.0**

  * 新增 `GET /unified/history_loan_rate` 接口, 获取历史借币利率

**v4.86.0**

2024-12-02

  * 新增 `GET /wallet/order_status` 划转状态查询
  * `GET /futures/{settle}/positions` 接口,返回值增加 `update_id`

**v4.85.0**

2024-11-11

  * `POST /futures/{settle}/orders`、`POST /spot/batch_order` 接口，请求头新增 `x-gate-exptime`字段
  * `POST /futures/{settle}/dual_mode` 接口，返回增加 `cross_order_margin`、`cross_initial_margin`、`cross_maintenance_margin`、`cross_unrealised_pnl`、`cross_available`、`isolated_position_margin` 字段

**v4.84.0**

2024-11-04

  * 新增 `GET /loan/multi_collateral/current_rate` 接口, 查询币种活期利率
  * `GET /spot/tickers` 接口, 返回值增加 `lowest_size`、`highest_size` 字段
  * `POST /earn/dual/orders` 接口, 请求体新增 `amount` 字段

**v4.83.0**

2024-10-28

  * 新增 `GET /unified/leverage/user_currency_config` 接口, 查询用户最大、最小可设置币种杠杆倍数
  * 新增 `GET /unified/leverage/user_currency_setting` 接口, 获取用户币种杠杆倍数
  * 新增 `POST /unified/leverage/user_currency_setting` 接口, 设置币种杠杆倍数
  * `GET /futures/{settle}/account_book` 接口，返回值增加 `id` 字段
  * `GET /unified/currency_discount_tiers` 接口，返回值增加 `leverage` 字段

**v4.82.0**

2024-10-14

  * 新增 `GET /account/rate_limit` 接口, 获取用户限流信息. 详情请见成交比率限频
  * `GET /account/detail` 接口, 返回值增加 `copy_trading_role` 字段

**v4.81.0**

2024-09-30

  * 新增 `POST /options/countdown_cancel_all` 接口, 倒计时取消订单
  * `GET /wallet/push` 接口, 返回值增加 `message` 字段
  * `GET /futures/{settle}/funding_rate` 接口, 新增 `from`、`to` 查询字段
  * `POST /earn/dual/orders` 接口, 返回值增加 `is_max` 字段

**v4.80.0**

2024-09-09

  * 新增 `GET /options/mmp` 接口, MMP查询
  * 新增 `POST /options/mmp` 接口, MMP设置
  * 新增 `POST /options/mmp/reset` 接口, MMP重置
  * `GET /wallet/withdrawals`接口, 返回值增加 `block_number` 字段

**v4.79.0**

2024-09-02

  * `GET /unified/interest_records` 接口，新增 `from`、`to` 查询字段
  * `GET /unified/unified_mode` 接口，返回值增加 `options` 字段
  * `PUT /unified/unified_mode` 接口，新增 `options` 字段

**v4.78.0**

2024-08-19

  * 新增 `GET /wallet/push` 接口, 获取记录
  * 新增 `POST /withdrawals/push` 接口, 现货主账号之间划转,划转双方不可为子账号
  * 新增 `GET /futures/{settle}/batch_amend_orders` 接口, 批量修改指定 ID 的订单
  * `GET /futures/{settle}/my_trades` 接口, 返回增加 `close_size` 字段
  * `POST /wallet/transfers` 接口, 返回增加 `tx_id` 字段

**v4.77.0**

2024-08-05

  * 新增 `GET /sub_accounts/unified_mode` 接口，获取子帐号模式
  * `GET /rebate/broker/commission_history` 接口，新增 `from`、`to` 查询字段
  * `GET /rebate/broker/transaction_history` 接口，新增 `from`、`to` 查询字段

**v4.76.0**

2024-07-22

  * 新增 `GET /rebate/partner/sub_list` 接口，伙人下级列表
  * `GET /flash_swap/currency_pairs` 接口，新增 `page`、`limit` 查询字段
  * `PATCH /spot/orders/{order_id}` 接口，新增 `order_id`、`currency_pair`、`account` 字段
  * `DELETE /spot/orders/{order_id}` 接口，新增 `order_id`、`currency_pair`、`account` 字段

**v4.75.1**

2024-07-08

  * 新增 `GET /delivery/{settle}/risk_limit_tiers` 接口，查询风险限额等级
  * 新增 `GET /rebate/partner/transaction_history` 接口，合伙人获取推荐用户的交易记录
  * `GET /unified/loan_records` 接口，返回值增加 `borrow_type` 字段
  * `GET /futures/{settle}/position_close` 接口，返回值增加 `accum_size` 字段

**v4.75.0**

2024-06-24

  * 新增 `GET /account/debit_fee` 接口，查询GT抵扣配置
  * 新增 `POST /account/debit_fee` 接口，设定GT抵扣

**v4.74.1**

2024-06-11

  * 针对移动端可视区域DOM优化

**v4.74.0**

2024-05-29

  * 新增 `GET /unified/loan_margin_tiers` 接口， 查询统一账户借贷梯度保证金

**v4.73.0**

2024-05-27

  * `POST /wallet/small_balance`接口，新增 `is_all` 字段
  * `POST /spot/cancel_batch_orders`接口，返回值增加 `text`字段
  * `GET /unified/accounts`接口，返回值增加 `funding`、`funding_version`、`use_funding`字段

**v4.72.0**

2024-05-13

  * `GET /sub_accounts/{user_id}/keys`接口，返回值增加 `last_access`字段
  * `GET /futures/{settle}/risk_limit_tiers`接口，返回值增加 `contract`字段

**v4.71.0**

2024-04-23

  * `GET /wallet/saved_address`接口，新增 `page` 查询字段
  * 新增 `GET /api/v4/rebate/user/info` 接口， 获取用户返佣信息
  * 新增 `POST /unified/portfolio_calculator` 接口，组合保证金计算器计算
  * 新增 `GET /unified/risk_units` 接口， 获取用户风险单元详情
  * 新增 `PUT /unified/unified_mode` 接口， 设置统一账户模式
  * 新增 `GET /unified/unified_mode` 接口， 查询统一账户模式

**v4.70.0**

2024-04-08

  * `GET /futures/{settle}/positions`接口，返回值增加 `pnl_pnl`、`pnl_fund`、`pnl_fee`字段
  * `GET /futures/{settle}/position_close`接口，返回值增加 `pnl_pnl`、`pnl_fund`、`pnl_fee`字段

**v4.69.0**

2024-03-25

  * `POST /delivery/{settle}/price_orders`接口，返回值增加 `text` 字段

**v4.68.0**

2024-03-18

  * 新增 `GET /unified/currency_discount_tiers` 接口，查询统一账户梯度式discount
  * `GET /unified/loans`接口，新增 `type` 查询字段，返回值增加 `type` 字段
  * `GET /unified/interest_records`接口，新增 `type` 查询字段，返回值增加 `type` 字段

**v4.67.0**

2024-03-11

  * `POST /spot/orders`,`POST /spot/batch_orders`接口，返回值增加 `filled_amount` 字段
  * 限频规则中,钱包提现接口限速描述，由`10r/10s`更正为`1r/3s`(并无修改原本限流行为)

**v4.66.1**

2024-02-19

  * 新增 `GET /wallet/small_balance` 接口，获取可兑换的小额币种清单
  * 新增 `GET /wallet/small_balance_history` 接口，获取可兑换的小额币种历史纪录
  * 新增 `GET /unified/estimate_rate` 接口，查询统一账户的预估利率

**v4.65.0**

2024-01-29

  * `GET /spot/batch_fee` 接口，返回值增加 `debit_fee` 字段
  * `DELETE /account/stp_groups/{stp_id}/users` 接口，新增 `user_id` 请求字段
  * 现货API下单增加异步支持模式，`ACK`,`RESULT`,`FULL`，详情请见SPOT API

**v4.64.0**

2024-01-22

  * `GET /loan/multi_collateral/orders` 接口，新增 `order_type` 查询字段
  * `GET /loan/multi_collateral/orders` 接口，返回值增加 `order_type`,`fixed_type`,`fixed_rate`,`expire_time`,`auto_renew`,`auto_repay` 字段
  * `GET /loan/multi_collateral/repay` 接口，返回值增加`before_ltv`,`after_ltv` 字段
  * 新增 `GET /loan/multi_collateral/fixed_rate` 接口，查询币种7日固定利率和30日固定利率
  * `GET /wallet/total_balance` 接口，返回值增加`unrealised_pnl`,`borrowed` 字段

**v4.63.0**

2024-01-15

  * `GET /wallet/currency_chains` 接口，返回值增加 `decimal` 字段
  * 新增 `GET /futures/{settle}/risk_limit_tiers` 接口，查询风险限额等级

**v4.62.0**

2024-01-02

  * 新增 `POST /futures/{settle}/batch_cancel_orders` 接口，用户可批量撤销订单
  * 新增多币质押API (`/loan/multi_collateral/**`)

**v4.61.0**

2023-12-18

  * `GET /rebate/broker/commission_history` 和 `GET /rebate/broker/commission_history` 接口，新增经纪商获取返佣记录

**v4.60.0**

2023-12-01

  * 新的 Unified API 已经上线, 旧的 `/portfoli/*` 接口已被弃用 (2023-12-31 移除)
  * 新增理财产品 API (`/earn/**`)
  * `GET /futures/{settle}/account_book` 接口，返回值增加 `trade_id` 字段

**v4.59.0**

2023-11-22

  * `GET /futures/{settle}/contracts` 接口，返回值增加 `funding_cap_ratio` 字段
  * `GET /delivery/{settle}/account_book` 接口，返回值增加 `contract` 字段
  * `GET /wallet/withdraw_status` 接口，返回值增加 `withdraw_percent_on_chains` 字段
  * `GET /portfolio/accounts` 接口，返回值增加 `leverage` 字段

**v4.58.0**

2023-11-03

  * `GET /account/detail` 接口, 返回值新增 `tier` 字段
  * `GET /spot/currency_pairs` 接口, 返回值新增 `max_base_amount`、`max_quote_amount` 字段

**v4.57.0**

2023-10-20

  * 新增进出网关时间记录，详情参考网关入出站时间
  * `POST /spot/orders` 接口，新增支持保证金帐户类型
  * `GET /spot/trades` 接口，返回值新增 `sequence_id` 字段
  * `GET /spot/account_book` 接口，返回值新增 `text` 字段
  * `GET /spot/my_trades` 接口，返回值新增 `text` 字段
  * 新增 `POST /spot/amend_batch_orders` 接口，用户可以批量修改订单
  * 新增 `PUT /earn/uni/interest_reinvest` 接口，用户可以设置利息复投开关
  * `GET /portfolio/spot/orders`、 `GET /portfolio/spot/orders`、`GET /portfolio/spot/orders/{order_id}`、`DELETE /portfolio/spot/orders/{order_id}` and `PATCH /portfolio/spot/orders/{order_id}` 这些接口将被弃用, 我们预计在十月底移除这些接口的支持, 用户可以转用 `/spot/orders` 相关接口来替代

**v4.56.0**

2023-09-25

  * `GET /portfolio/loan_records` 接口，新增 `repayment_type` 字段
  * `GET /futures/{settle}/positions` 接口, 请求参数新增 `holding` 字段
  * `GET /futures/{settle}/my_trades_timerange` 接口, 请求参数新增 `role` 字段
  * `GET /futures/{settle}/position_close` 接口, 请求参数新增 `side` and `pnl` 字段

**v4.55.0**

2023-09-12

  * 新增 `POST /portfolio/account_mode` 接口，新增模式切换

**v4.54.0**

2023-08-28

  * `GET /wallet/currency_chains` 接口，新增 `contract_address` 字段
  * `GET /portfolio/spot/currency_pairs` 与 `GET /portfolio/spot/currency_pairs/{currency_pair}`，新增查询保证金现货市场列表

**v4.53.0**

2023-08-14

  * `DELETE /account/stp_groups/{stp_id}/users`，新增删除 STP Group 用户接口

**v4.52.0**

2023-08-07

  * 新增抵押借币相关 API

**v4.51.0**

2023-07-29

  * 调整优化资产流水类型
  * `GET /account/detail` 接口，新增 `mode` 字段

**v4.50.0**

2023-07-14

  * 新增保证金账户体系相关的API，目前服务只对白名单用户开放，有兴趣的用户可以聯繫機構部門
  * 新增 `GET /flash_swap/currency_pairs` 接口，查询支持闪兑的所有交易对列表

**v4.49.0**

2023-07-03

  * 新增新版限频规则 ，新版预计于 2023-07-10 (utc+8) 开始生效
  * `GET /futures/{settle}/orders`接口，调整请求字段 `contract` 改为非必填

**v4.48.0**

2023-06-16

  * `GET /wallet/sub_account_transfers`接口，新增 `client_order_id` 请求字段

**v4.47.0**

2023-05-23

  * `GET /margin/uni/estimate_rate`，新增逐仓借贷利率查询接口
  * `GET /futures/{settle}/orders_timerange`，新增查询合约历史订单列表(时间区间)接口
  * `GET /options/positions/{contract}`接口，新增 `underlying`、`underlying_price`、`mark_iv`、`delta`、`gamma`、`vega`、`theta` 等字段
  * 新增 STP Group 管理 API 接口

**v4.46.0**

2023-05-08

  * `GET /spot/account_book`，新增查询现货账户变动历史接口
  * `GET /futures/{settle}/fee`，新增查询合约市场交易费率接口

**v4.45.0**

2023-04-21

  * 逐仓借贷迁移到余币宝，详细资讯可参考逐仓迁移说明
  * `POST /futures/{settle}/batch_orders` 接口，新增 STP 功能

**v4.44.0**

2023-04-07

  * 新增 `ORDER_BOOK_NOT_FOUND`、`FAILED_RETRIEVE_ASSETS` 错误信息

**v4.43.0**

2023-03-27

  * 现货下单接口，新增 `Self-Trade Prevention` 功能，详细资讯可参考STP介绍
  * `GET /account/detail`，新增查询 API Key 的 IP 白名单接口
  * `PATCH /spot/orders/{order_id}` 接口，新增 `amend_text` 字段

**v4.42.0**

2023-03-13

  * 新增余币宝接口
  * 合约下单接口，新增 `Self-Trade Prevention` 功能，详细资讯可参考STP介绍
  * `POST /wallet/sub_account_transfers` 接口，新增 `交割合约账户` 类型支持

**v4.40.0**

2023-02-24

  * `GET /futures/{settle}/candlesticks` 接口，新增 `sum` 字段
  * `GET /futures/{settle}/auto_deleverages` 接口，新增查询ADL自动减仓订单信息

**v4.39.0**

2023-02-09

  * `GET /spot/batch_fee` 接口，新增批量查询账户费率接口
  * `GET /futures/{settle}/contracts` 接口，新增 `enable_bonus`、`enable_credit` 字段

**v4.38.0**

2023-02-04

  * `GET /futures/{settle}/my_trades_timerange` 接口，新增时间范围查询合約成交记录接口
  * `POST /withdrawals` 接口，新增 `withdraw_order_id` 字段

**v4.37.0**

2023-01-20

  * 新增查询反佣相关接口

**v4.36.0**

2022-12-23

  * `POST /spot/orders` 和 `POST /spot/batch_orders` 接口，下单的时候 `iceberg` 字段不再支持全部订单隐藏

**v4.35.0**

2022-12-09

  * `GET /spot/orders` 接口, 新增订单平均价格字段
  * `PATCH /spot/orders/{order_id}` 接口, 新增订单修改单
  * `POST /spot/batch_orders` 接口, 新增现货市价单类型

**v4.34.0**

2022-11-25

  * `POST /spot/orders` 接口, 现货下单增加市价单

**v4.33.0**

2022-11-11

  * K 线图接口 `GET /futures/{settle}/premium_index`
  * 创建子帐号的时候可以指定密码与 Eamil

**v4.32.0**

2022-10-28

  * 优化期权API文档

**v4.31.0**

2022-10-14

  * `POST /wallet/sub_account_to_sub_account` 子帐号划转接口，新增合约与全仓杠杆划转

**v4.30.0**

2022-09-23

  * 新增管理子帐号 API Key 接口
  * 新增子帐号冻结与解冻接口
  * `POST /wallet/sub_account_to_sub_account` 接口，新增子帐号与子帐号划转

**v4.29.0**

2022-09-09

  * 新增创建、查询子帐号功能
  * `GET /wallet/fee` 接口，新增 `settle` 查询字段
  * 期权订单新增 `refr` 字段
  * 创建 API Key 数量上限调整至 20

**v4.28.0**

2022-08-12

  * `GET /futures/{settle}/trades` 接口，新增 `offset` 查询字段
  * 新增现货与合约的定时取消订单接口

**v4.27.0**

2022-07-29

  * 新增 `X-Client-Request-Id` 请求 ID header，可以用来追踪请求
  * 新增合约批量下单接口，`POST /futures/{settle}/batch_orders`
  * 新增合约交易下单FOK订单类型

**v4.26.0**

2022-07-15

  * 现货自动单支持统一帐户
  * 新增 `GET /wallet/saved_address` 接口，获取提币白名单地址
  * `POST /wallet/transfers` 接口，支援操作单号返回
  * 新增 `GET /wallet/sub_account_cross_margin_balances` 接口，查询子账号全仓杠杆账户余额信息
  * `GET /margin/currency_pairs` 接口、新增 `status` 字段

**v4.25.1**

2022-07-06

  * 新增 `GET /spot/time` 获取服务器当前时间接口
  * 获取交易对 ticker 信息 `GET /spot/tickers`，新增 `change_utc0`, `change_utc8` 字段
  * 新增 `GET /options/my_settlements` 查询期权个人结算记录接口

**v4.25.0**

2022-06-24

  * 支持统一帐户 API
  * 全仓账户增加多个返回字段，详细请查看接口描述
  * 现货交易增加接口`POST /spot/cross_liquidate_orders`，处理全仓币种禁用时平仓买入下单
  * 获取合约账号接口新增 `bonus` 理财金字段和 `history` 累计统计数据字段
  * 合约个人成交记录新增 `text` 订单的自定义信息,`fee` 成交手续费,`point_fee`成交点卡手续费等字段
  * 订正撤销单个自动单名称
  * `POST /wallet/sub_account_transfers` 支持划转到全仓杠杆账户

**v4.24.0**

2022-05-20

  * 新增 `/flash_swap` 闪兑 API ，支持直接通过 API 方式进行闪兑操作，接口组关联现货权限
  * 钱包新增 `GET /wallet/sub_account_margin_balances` , `GET /wallet/sub_account_futures_balances` 接口，方便主账号查询子账号的逐仓杠杆账户和永续合约账户的余额信息
  * 永续合约新增 API `GET /futures/{settle}/index_constituents/{index}` 查询指数来源信息
  * 修复合约自动订单 `FuturesPriceTriggeredOrder` 缺少 `order_type` 等字段的定义

**v4.23.4**

2022-04-25

  * 现货 K 线查询支持 `30d` 粒度

**v4.23.3**

2022-04-01

  1. 现货 K 线增加基础货币成交量返回
  2. 现货币种信息返回增加该币所在链的信息
  3. 钱包接口 `GET /wallet/currency_chains` 增加币种的充提状态返回
  4. 永续合约双仓模式下增加缺失的全仓杠杆 `cross_leverage_limit` 参数
  5. 永续、交割合约查询 K 线新增多个时间粒度的支持

**v4.23.2**

2022-01-21

  1. 提现充值历史增加 `fee` 字段返回
  2. 现货 `Currency` 币种模型增加固定费率

**v4.23.1**

2021-12-23

  1. 现货下单 `time_in_force` 增加新类型 `FOK`
  2. 新增错误代码 `FOK_NOT_FILL`

**v4.23.0**

2021-12-09

  1. 新增期权 API
  2. 新增详细的限速规则说明
  3. 新增 `GET /wallet/currency_chains` 查询币种支持的链
  4. 提现充值历史增加新的 status 可选值

**v4.22.4**

2021-11-01

  1. `SpotPriceTriggeredOrder` 字段 `ctime` 和 `ftime` 更正为 `int64`

**v4.22.3**

2021-10-27

  1. `GET /spot/trades` 支持指定 `from` 和 `to` 按时间范围筛选的查询

**v4.22.2**

2021-09-29

  1. 提现充值记录新增 `status` 字段的可选值
  2. 合约下单新增 `auto_size` 只写字段用于双向持仓模式的平仓操作

**v4.22.1**

2021-09-07

  1. 新增钱包接口 `GET /wallet/total_balance` 获取用户总资产
  2. 逐仓杠杆账户返回增加`locked` 和 `risk` 字段
  3. 逐仓和全仓杠杆借入支持输入自定义 text

**v4.22.0**

2021-08-13

  1. 交割合约支持 BTC 结算
  2. 现货 API `GET /spot/orders` 和 `GET /spot/my_trades` 支持按时间范围筛选
  3. 逐仓和全仓支持查询用户最大借入额度

**v4.21.6**

2021-08-12

  1. 修复 `GET /wallet/deposit_address` 地址链字段错误名称

**v4.21.5**

2021-06-30

  * 针对已结束的单子， `GET /spot/orders`, `GET /spot/orders/{order_id}` 以及 `GET /spot/my_trades` 接口可以不用指定 `currency_pair` 参数
  * `GET /wallet/withdraw_status` 返回增加多链的固定提现手续费返回
  * 新增 `GET /margin/transferable` API 查询逐仓和全仓账户允许的最大转出额度
  * 合约平仓历史 API 新增 `from` 和 `to` 的时间范围查询参数

**v4.21.4**

2021-06-23

  * 逐仓账户历史 `GET /margin/account_book` 返回增加毫秒时间戳

**v4.21.3**

2021-06-17

  * 现货、合约深度增加时间戳返回

**v4.21.2**

2021-06-07

  * 合约 API 新增对全仓杠杆调整的支持
  * 新增 `/margin/cross` 全仓杠杆 API
  * 新增现货下单对全仓杠杆账户的支持
  * 逐仓杠杆账户查询返回新增账户未还利息
  * 现货订单信息新增 `create_time_ms` 和 `update_time_ms` 毫秒时间返回
  * 新增取消提现接口 `DELETE /withdrawals/{withdrawal_id}`

**v4.20.1**

2021-04-14

  * 更新文档部分链接

**v4.20.0**

2021-03-25

  * 增加现货自动订单接口组 `/spot/price_orders`

**v4.19.6**

2021-03-22

  * 现货交易对查询增加开盘时间返回

**v4.19.5**

2021-03-18

  * 指定订单 ID 的现货、永续合约操作支持使用用户自定义 ID（只在订单创建后的 30 分钟内有效）。

**v4.19.4**

2021-03-10

  * `/wallet/sub_account_transfers` 接口支持转账到子账户的合约账户

**v4.19.3**

2021-03-04

  * 新增杠杆借贷自动还款设置和查询接口 `/margin/auto_repay`
  * `/wallet/deposit_address` 接口新增 `multichain_address` 字段，返回某些币种的多充值地址
  * 优化部分文档内容

**v4.19.2**

2021-03-01

  * 新增 `/wallet/fee` 接口用于查询交易费率，原有 `/spot/fee` 接口废弃
  * 提现操作增加 `chain` 字段
  * 合约深度查询 `/futures/{settle}/order_book` 增加 `with_id` 字段的说明，返回内容增加深度 ID 的说明
  * 合约个人平仓历史查询 `/futures/{settle}/position_close` 增加 `offset` 参数，用于翻页获取历史平仓记录
  * 增加合约价值的计算方法说明，具体参考 `Contract` 模型的描述
  * 修复合约统计数据字段类型错误

**v4.18.4**

2021-01-22

  * 现货 `Trade` 模型新增 `create_time_ms` 字段
  * ETF 交易对 Ticker 增加净值等相关信息返回

**v4.18.1**

2021-01-07

  * 现货下单新增冰山委托支持
  * 修复 `/futures/{settle}/contract_stats` 返回数据的错误字段类型

**v4.18.0**

2020-12-21

  * 现货新增 `/spot/currencies` 和 `/spot/currencies/{currency}` 查询币种信息
  * 合约 `ContractStat` 返回新增 `top_lsr_account` 和 `top_lsr_size` 等多个字段

**v4.17.1**

2020-12-16

  * `/spot/order_book` 接口 `limit` 字段最大值增加到 100

**v4.17.0**

2020-12-15

  * 新增子账号余额查询接口 `/wallet/sub_account_balances`

**v4.16.1**

2020-12-10

  * 修复 Position 模型定义里的错误字段名称 `dual_mode` 。正确应该是 `mode`

**v4.16.0**

2020-12-09

_现货_

  * `POST /spot/batch_orders` 每个交易对可以创建的 order 数量提高到 10 个
  * 现货 `GET /spot/trades` 新增 `reverse` 参数支持时间逆序查询历史记录

_合约_

  * 永续合约新增双仓支持 API ，`/futures/{settle}/dual_mode` 接口设置是否开启双仓。 双仓相关的仓位操作参照 `/futures/{settle}/dual_comp/positions` 接口组
  * 永续合约账户返回新增 `in_dual_mode` ，仓位返回新增 `dual_mode`
  * 永续合约新增 `/futures/{settle}/liq_orders` 支持查询市场强平记录

**v4.15.5**

2020-11-04

  * 新增 API `/futures/{settle}/contract_stats` 获取合约统计信息
  * 新增 API `/margin/{currency_pair}` 获取单个杠杆交易对详情

**v4.15.4**

2020-09-01

  * `GET /spot/fee` 接口返回新增 `point_type` 字段
  * 新增 API `GET /wallet/withdraw_status`
  * 新增了 C# SDK 入口

**v4.15.2**

2020-08-12

  * 新增 `GET /spot/fee` 获取个人现货交易费率

**v4.15.1**

2020-08-04

  * 新增获取现货市场所有当前委托 `GET /spot/open_orders`
  * 新增杠杆账户余额变更历史 `GET /margin/account_book`

**v4.14.1**

2020-07-08

  * 订单里的 `text` 字段最大允许长度提高到了 28 个字节（不包括前缀）

**v4.14.0**

2020-07-06

  * 交割合约引擎 API `/delivery` 上线

**v4.13.1**

2020-06-28

  * 新增 `GET /wallet/sub_account_transfers` 接口查询主子账号划转历史

**v4.13.0**

2020-05-20

  * 增加了对提现操作的支持，详情关注 `POST /withdrawals` 接口和“认证”一节
  * 账户划转 `POST /wallet/transfers` 支持现货到合约了。
  * 钱包接口新增了提现充值历史记录查询
  * 合约订单和个人成交列表支持传入 `offset` 参数
  * 合约 `Contract` 模型添加新字段 `in_delisting`

**v4.12.0**

2020-04-08

  * 升级 APIv4 的 Key ，不再按功能独立 Key，每个 Key 都可以独立配置多个功能的权限， 详细说明参考 “关于 APIv4 Key 升级” 一节
  * 新增接口 `POST /wallet/sub_account_transfers` 支持主子账号余额划转
  * `GET /spot/candlesticks` 增加请求参数 `from` 和 `to` ，方便获取历史数据

**v4.11.2**

2020-03-29

  * `Order` 模型增加字段 `filled_total` 替换命名容易引起误解的 `fill_price`
  * 添加新的错误码标识 `POC_FILL_IMMEDIATELY`

**v4.11.1**

2020-03-23

  * 个人成交记录 `GET /spot/my_trades` 返回增加 `role` 交易角色信息
  * 修复查询币币理财账户 `GET /margin/funding_accounts` 缺少未使用过理财的币种的问题

**v4.11.0**

2020-03-20

  * 现货下单支持 GT 抵扣费率折扣
  * 现货下单 Time in force 支持传入 `poc`

**v4.10.1**

2020-02-24

  * 现货交易对新增字段 `trade_status`

**v4.10.0**

2020-02-17

  * 杠杆下单支持传入 `auto_borrow` 字段（只写），在余额不足时由系统自动借入不足部分
  * 增加指定订单 ID 的批量撤单接口 `POST /spot/cancel_batch_orders`
  * 补充“错误处理”和“与 APIv2 的区别”文档

**v4.9.1**

2020-01-07

  * `Order` 和 `BatchOrder` 新增订单最近修改时间、成交费率的返回
  * `GET /spot/my_trades` 增加成交费率返回

**v4.9.0**

2019-12-17

  * `GET /futures/{settle}/trades` 不再支持 `last_id` 参数，改用 `from` 和 `to` 来获取历史成交

**v4.8.2**

2019-12-02

  * 新增 `/spot/batch_orders` 支持现货和杠杆的批量下单操作
  * 杠杆还款产生的手续费率支持用户等级折扣
  * `Loan` 模型里增加了 `fee_rate` 字段标识杠杆借出单的手续费率，`orig_id` 标识续借单的原始借出单 ID

**v4.8.1**

2019-11-27

  * 修复 `GET /futures/{settle}/positions` 文档和代码示例缺少 `settle` 字段的说明和使用

**v4.8.0**

2019-11-07

  * 合约 API 支持以 USDT 结算
  * 原有的以 `/futures` 为前缀的所有接口前缀统一调整为 `/futures/{settle}` ，以支持基于多种结算货币的合约操作。
  * `/futures/{settle}/accounts` 返回的账户信息里 `currency` 增加 `USDT` 的返回 `volume_24h_settle` 字段，取代原有 `volume_24h_btc` 和 `volume_24h_usd` 的使用。 后两个字段为了兼容依然保留，但是新的操作不推荐继续使用。

将 `/futures` 替换成 `/futures/usdt` 就可以使用 USDT 结算的合约操作, 例如 `GET /futures/usdt/accounts` 能够获取 USDT 的合约账户，而 `GET /futures/btc/accounts` 则是用来获取 BTC 的合约账户。

为了保持兼容, 原有的 `GET /futures/xxx` 的 API 都会默认为 BTC `GET /futures/btc/xxx` 。如 `GET /futures/accounts` 会被服务默认按 `GET /futures/btc/accounts` 请求来处理

**v4.7.3**

2019-07-18

  * 现货、合约下单增加 `text` ，支持用户自定义信息

**v4.6.3**

2019-06-11

  * 合约账户和仓位信息里增加点卡相关信息

**v4.7.2**

2019-05-29

  * 理财借出 `Loan` 的 `rate` 字段调整为非必选

**v4.7.1**

2019-04-17

  * 新增 wallet v4 API ，目前仅支持现货与杠杆账户转账操作
  * `GET /margin/loans` 接口支持按 `rate` 排序，支持可选 `currency_pair` 输入
  * 修复各种文档问题

**v4.6.2**

2019-04-24

  * 修复合约价格单文档覆盖了普通合约单接口 `GET /futures/orders/{order_id}` 和 `DELETE /futures/orders/{order_id}` 的文档

**v4.6.1**

2019-04-02

  * 合约 Ticker 返回新增字段 `high_24h` 、 `low_24h` 和 `funding_rate_indicative`

**v4.6.0**

2019-03-21

_只影响 SDK_

  * 修改合约相关的下单函数名，防止在 Go SDK 中与现货下单冲突
  * 修复验签时没有对请求参数做 decode 的问题

**v4.5.2**

2019-03-14

  * `/spot/order_book` 的参数 `currency_pair` 应为必选
  * 优化代码示例

**v4.5.1**

2019-03-11

  * 修复缺少 URL 参数的说明

**v4.5.0**

为了避免引起版本混乱，APIv4 此后的版本统一以 `4` 作为大版本号开头（包括文档和 SDK）

2019-03-05

  * 新增现货 v4 API，在原有 API 基础之上提供更多功能
  * 新增杠杆 v4 API，提供杠杆借贷功能；杠杆交易API 复用现货 v4 交易API
  * 提供合约止盈止损自动单 API 支持，详情见 `/futures/price_orders` 一组接口
  * 实盘交易统一 APIv4 统一 Base URL 到 `https://api.gateio.ws/api/v4`

**v1.3.0**

2019-02-13

_重要更新_

  * base URLs 域名更新为 `fx-api.gateio.ws` 和 `fx-api-testnet.gateio.ws` 原有 `*.gateio.io` 已废弃

**v1.2.1**

2019-02-13

  * 合约 Ticker 接口返回增加 `volumn_24h_usd` 和 `volume_24h_btc`

**v1.2.0**

2019-01-17

  * 新增 `GET /futures/contracts/{contract}` 查询单个合约
  * 新增 `GET /futures/positions/{contract}` 查询单个合约的仓位
  * 新增 `GET /futures/account_book` 查询用户合约账户历史
  * `Contract` 模型新增 `config_change_time` 字段
  * 修复各种文档问题

**v1.1.0**

2019-01-08

  * `Contract`, `Position`, `FuturesOrder` 模型增加更多参数
  * 新增 API `GET /futures/position_close` 获取平仓记录
  * API `GET /futures/my_trades` 增加可选参数 `order_id` 支持
  * `DELETE /futures/orders` 和 `DELETE /futures/orders/{order_id}` 返回状态码从 204 改为 200, 并在请求成功后返回撤销的订单列表
  * `DELETE /futures/orders/{order_id}` 对无效订单不忽略错误，改为返回 404
  * `POST /futures/orders` 支持 POC 和冰山委托

**v1.0.0**

2018-12-30

  * 初次发布

#  General

##  匹配机制

###  匹配优先级

Gate 订单匹配遵循 价格优先 > 时间优先 的原则

假设订单簿情况如下：

匹配优先级订单 | 下单时间 | Ask/卖价  
---|---|---  
A | 10:00 | 100  
B | 10:00 | 102  
C | 10:01 | 100  
  
如果 10:02 分 的现价买单 102，最终成交顺序为： A、C、B

###  订单生命周期

发送到匹配引擎的有效订单会立即被接受，并跟已有挂单进行匹配，然后将匹配结果返回给客户端。

匹配结果若是完全执行，则订单结束。若结果是不执行或部分执行，TimeInForce 为 IOC 的订单会立即结束； 其他情况的订单，则被挂在相应价格订单队尾，等待被匹配或者被撤销。

##  数据中心

Gate 数据中心位于 AWS 日本东京 (ap-northeast-1) 地区。

##  接口概览

接口概览接口分类 | 分类链接 | 概述  
---|---|---  
host + `/api/v4/spot/*` | 现货交易 | 包含币种状态、行情信息、下单、成交记录等功能  
host + `/api/v4/margin/*` | 杠杆交易 | 杠杆账户管理、借贷、还款等  
host + `/api/v4/futures/*` | 永续合约交易 | 永续合约账户管理、行情信息、下单、成交记录等功能  
host + `/api/v4/delivery/*` | 交割合约交易 | 交割合约账户管理、行情信息、下单、成交记录等功能  
host + `/api/v4/options/*` | 期权交易 | 期权账户管理、行情信息、下单、成交记录等功能  
host + `/api/v4/wallet/*` | 钱包管理 | 充提记录、查询余额、资金划转等  
host + `/api/v4/withdrawals/*` | 提现 | 数字货币提现  
  
##  逐仓迁移说明

平台于 2023 年 4 月 13 日 14:00（UTC+8）到 2023 年 4 月 23 日 14:00（UTC+8）期间陆续对币币理财市场中未被借贷的资产进行系统自动迁移，迁移至余币宝市场，同时也会对已经被借贷出去的资产进行取消自动放贷处理，迁移完成后您可到余币宝市场中，查看您的理财详情。在此期间将暂停通过币币理财借出资金，您也可以手动将资产从币币理财转到余币宝市场，提前获得理财收益。  
自动迁移后老版本的借贷接口将被弃用，新版借贷使用`/margin/uni`接口组，详细的接口迁移可以参考下表

逐仓杠杆账户相关接口:

逐仓迁移说明接口名称 | 路径 | 接口是否下线 | 新路径  
---|---|---|---  
杠杆账户列表 | GET /margin/accounts | 否 | `-`  
查询杠杆账户变动历史 | GET /margin/account_book | 否 | `-`  
理财账户列表 | GET /margin/funding_accounts | 否 | `-`  
修改用户自动还款设置 | POST /margin/auto_repay | 否 | `-`  
查询用户自动还款设置 | GET /margin/auto_repay | 否 | `-`  
逐仓杠杆允许的最大转出 | GET /margin/transferable | 否 | `-`  
  
逐仓杠杆借贷相关接口（迁移至`/margin/uni`接口组）:

逐仓迁移说明接口名称 | 路径 | 接口是否下线 | 新路径  
---|---|---|---  
查询支持杠杆交易的所有交易对 | GET /margin/currency_pairs | 是 | GET /margin/uni/currency_pairs  
查询单个杠杆交易对 | GET /margin/currency_pairs/{currency_pair} | 是 | GET /margin/uni/currency_pairs/{currency_pair}  
借入或借出 | POST /margin/loans | 是 | POST /margin/uni/loans  
查询借贷订单详情 | GET /margin/loans/{loan_id} | 是 | `-`  
查询借贷订单列表 | GET /margin/loans | 是 | GET /margin/uni/loans  
归还借贷 | POST /margin/loans/{loan_id}/repayment | 是 | POST /margin/uni/loans  
查询借贷归还记录 | GET /margin/loans/{loan_id}/repayment | 是 | GET /margin/uni/loan_records  
逐仓杠杆用户最多可借入 | GET /margin/borrowable | 是 | GET /margin/uni/borrowable  
查询扣息记录 | `-` | `-` | GET /margin/uni/interest_records  
  
理财相关接口(迁移至`/earn/uni`接口组）:

逐仓迁移说明接口名称 | 路径 | 接口是否下线 | 新路径  
---|---|---|---  
查询支持杠杆交易的所有交易对 | GET /margin/currency_pairs | 是 | GET /earn/uni/currencies  
查询单个杠杆交易对 | GET /margin/currency_pairs/{currency_pair} | 是 | GET /earn/uni/currencies/{currency}  
借入或借出 | POST /margin/loans | 是 | POST /earn/uni/lends  
查询借贷订单列表 | GET /margin/loans | 是 | GET /earn/uni/lends  
借出市场的深度 | GET /margin/funding_book | 是 | -  
合并多个借贷订单 | POST /margin/merged_loans | 是 | -  
修改借贷订单 | PATCH /margin/loans/{loan_id} | 是 | PATCH /earn/uni/lends  
撤销借出贷款订单 | DELETE /margin/loans/{loan_id} | 是 | POST /earn/uni/lends  
查看某个借贷订单的借出记录 | GET /margin/loan_records | 是 | GET /earn/uni/lend_records  
查看单个借出记录 | GET /margin/loan_records/{loan_record_id} | 是 | `-`  
修改单个借出记录 | PATCH /margin/loan_records/{loan_record_id} | 是 | `-`  
查询用户派息记录 | `-` | `-` | GET /earn/uni/interest_records  
  
#  API

##  HTTP 通用格式

  * 所有读操作都是 `GET` 方法，只接受请求参数，不读取任何请求体。
  * `DELETE` 方法移除指定资源（如委托），但因为 `DELETE` 方法也不读取任何请求体， 并不是所有移除操作都是用 `DELETE` 方法。复杂的移除操作通过 `POST` 方法配合请求体来实现。
  * 更新操作使用 `POST`, `PUT` 或 `PATCH` 方法，不同的请求有不同的参数传递方式， 但是他们要么是通过请求体，要么是请求参数，不会二者混用。
  * 所有操作成功时都会返回 HTTP 状态码 `2xx` 。`401` 说明认证有问题。其他 `4xx` 状态码说明请求无效。 如果是 `5xx` 错误，则是服务端处理请求时遇上了未知的严重错误，碰到的话请第一时间反馈。

##  时间

所有时间字段，如果没有额外说明，格式都是**秒** 级的 Unix 时间戳，但是返回的格式可能不同 `int64`, `number` 或者 `string` ），示例值如：

  * 1596531048
  * "1596531048"
  * 1596531048.285
  * "1596531048.285"

最佳方式是按有小数点的 `number` 去解析 (`string` 需要实现转换）。 如果不需要高精度， 再强转成整数（或长整形）。上面的 SDK 会对不同格式的时间字段按照相应格式做好反序列化处理。

##  网关入出站时间

每次请求API响应头(response header)中都会包含如下字段：

  * `X-In-Time`: API网关**接收请求** 时的时间戳，格式:Unix的时间戳,单位**微秒** 。

  * `X-Out-Time`: API网关**返回响应** 时的时间戳，格式:Unix的时间戳,单位**微秒**

例如：
    
    
    X-In-Time: 1695715091540163
    X-Out-Time: 1695715091551905
    

##  分页

分页的实现有如下两种方式：

  * `page`, `limit` 方式
  * `limit`, `offset` 方式

这两种方式里，`limit` 字段都是用来限制单次请求里列表返回的最大数量。没有特殊说明的情况下， 它的默认值是 `100` ，最大允许 `1000` 。

`page` 方式类似于网页的翻页，从 1 开始计数。遍历完整列表的方法是使用同一个 `limit`，每次请求将 `page` 加 1，直到返回的列表长度小于 `limit`

`offset` 方式类似于数据库检索，遍历完整列表的方式是每次累加 `limit` 到 `offset` 上， 直到返回的列表长度小于 `limit`

举例说明，如果订单总数是 201 个。使用 page-limit 方式，请求参数可以按照如下发送：

  1. `page=1&limit=100`
  2. `page=2&limit=100`
  3. `page=3&limit=100`

如果使用 limit-offset 方法，则是：

  1. `limit=100&offset=0`
  2. `limit=100&offset=100`
  3. `limit=100&offset=200`

有一些请求可能会返回额外的分页元数据信息。这些元数据信息都存储在返回头部。以 `GET /futures/{settle}/orders` 为例，这个请求会在返回头部追加如下分页元数据信息：

  * `X-Pagination-Limit`: 请求指定的 limit 参数
  * `X-Pagination-Offset`: 请求指定的 `offset` 参数
  * `X-Pagination-Total`: 满足条件的所有条目总数

##  限频规则

限频规则市场 | 入口 | 限速 | 依据 | 包含  
---|---|---|---|---  
公共接口 | 公共接口 | 单个接口 200r/10s | IP | 深度、K线、交易对信息等  
钱包 | 私有接口 |  提现接口(POST /withdrawals) 1r/3s  
提现uid转账接口(POST /withdrawals/push) 1r/10s  
交易账户互转接口 (POST /wallet/transfers) 80r/10s  
主子账号互转 (POST /wallet/sub_account_transfers) 80r/10s  
子账号与子帐号互转 (POST /wallet/sub_account_to_sub_account) 80r/10s  
查询个人账户总额 (GET /wallet/total_balance) 80r/10s  
查询子账号余额信息 (GET /wallet/sub_account_balances) 80r/10s  
查询子账号逐仓杠杆账户余额信息 (GET /wallet/sub_account_margin_balances) 80r/10s  
查询子账号永续合约账户余额信息 (GET /wallet/sub_account_futures_balances) 80r/10s  
查询子账号全仓杠杆账户余额信息 (GET /wallet/sub_account_cross_margin_balances) 80r/10s  
钱包其他单个接口 200r/10s  
| UID |  提现  
个人账户余额查询  
子账户余额查询  
  
现货 | 私有接口 |  现货批量/单个下单/单个修改接口一共订单数 10r/s (uid+市场)  
现货批量/单个撤单接口一共 200r/s  
现货其他单个接口 200r/10s  
| UID |  现货下单、撤单  
成交历史、费率查询等  
  
永续合约 | 私有接口 |  合约批量/单个下单/修改单个订单接口一共 100r/s  
合约批量/单个撤单接口一共 200r/s  
永续合约其他单个接口 200r/10s  
| UID |  合约下单、撤单  
成交历史、费率查询等  
  
交割合约 | 私有接口 |  单个下单接口 500r/10s  
单个撤单接口 500r/10s  
交割其他单个接口 200r/10s  
| UID |  下单、撤单  
  
期权合约 | 私有接口 |  单个下单接口 200r/s  
单个撤单接口 200r/s  
期权其他单个接口 200r/10s  
| UID |  下单、撤单  
  
子账户 | 私有接口 |  单个子账户相关接口 80r/10s  | UID |  创建普通子账户  
查询子账户列表  
禁用、启用子账户APIKEY  
  
保证金 | 私有接口 |  借入或还款 15/10s  | UID |  借入或还款(POST /unified/loans)  
  
其他私有接口 | 私有接口 |  单个接口 150r/10s  | UID |  理财、抵押借币等   
  
> 限速是每个子账号或主账号单独计算的

**限流字段**

每次请求API响应头(response header)中都会包含如下字段：

  * X-Gate-RateLimit-Requests-Remain - 该接口当前时间窗口剩余可用请求数
  * X-Gate-RateLimit-Limit - 该接口当前频率限制上限
  * X-Gate-RateLimit-Reset-Timestamp - 如果您已超过该接口当前窗口频率限制，该字段表示下个可用时间窗口的时间戳（秒），即什么时候可以恢复访问；如果您未超过该接口当前窗口频率限制，该字段表示返回的是当前服务器时间（秒).

WebSocket:

  * 现货: 现货批量/单个下单/单个改单一共 10r/s
  * 合约: 合约批量/单个下单/单个改单/单个撤单/批量撤单s一共 100r/s
  * 其他：无限制
  * 每个 IP 最大连接数: ≤ 300

##  成交比率限频

为提升交易效率，我们决定为成交比率较高的用户实施更为优越的子账户频率限制。该评估将依据过去七天的交易数据，于每日 00:00 UTC 进行计算。请注意，此项规则仅适用于 **VIP14 及以上的用户** 。

###  1\. 术语介绍

####  1.1 交易产品系数

为了更为精细化管理不同交易产品对成交比率的影响，我们引入了交易产品系数的概念。这一系数的设定允许我们根据产品的特性调整其对于总体成交量的影响。对于那些系数小于1的产品，它们通常涉及较小的合约规模，因此需要更多的交易指令来达到相同的交易量。通常情况下，所有交易产品都配备了一个默认系数，然而，部分产品根据其特性被赋予了独立的系数。相关产品的具体系数信息，请参考所提供的表格资料。

1.1 交易产品系数业务线 | 基于 | 独立系数 | 默认系数  
---|---|---|---  
USDT 永续合约 | 合约市场 |  1  
合约市场：  
BTC-USDT  
ETH-USDT  | 0.4  
现货 | 现货市场 |  1  
合约市场：  
BTC-USDT  
ETH-USDT  | 0.4  
  
> 请注意：现货本期暂时不会上线

####  1.2 交易量权重定义

我们会根据市场来波动，评估 maker 和 taker的行为模式，并据此设计 maker 与 taker 的交易量比例权重。此外，我们将定期对这些权重进行评估，并在必要时进行同步调整。

**本次 maker交易量占比权重：100%， taker交易量占比权重：90%**

####  1.3 成交比例计算公式

系统将在每日 08:00 UTC，依据 00:00 UTC 的数据快照，从子账户成交比率和母账户综合成交比率中选取较高的值，以确定子账户的未来限频。对于独立经纪商，系统将仅考虑其子账户的成交比率。需要注意的是，母账户也会被视作一个“子账户”。

  1. 子账户成交比率：该比率的计算方式为（子账户 永续合约Taker 的 USDT 成交量 × 0.9 + 永续合约Maker 的 USDT 成交量 × 1）/（各交易产品的新增和修改请求总数 × 交易产品系数总和）。
  2. 母账户综合成交比率：此比率的计算方式为（母账户的 永续合约Taker USDT 成交量 × 0.9 + 永续合约Maker USDT 成交量 × 1）/（所有子账户的各交易产品新增和修改请求总数 × 交易产品系数总和）。

###  2\. 现货下单频率限制规则

####  2.1 现有限频规则

现货批量/单个下单/单个修改接口一共订单数 10r/s (市场)

  * 同一个UID在不同的市场限速均为10r/s，在不同现货市场的限速相互独立

####  2.2 新增限频规则

平台将对在短期内频繁进行下单、撤单或修改订单操作，但成交率较低的交易行为实施限速，具体规则内容如下：

**1\. 统计周期**

  * 统计周期：统计最近24小时的数据，每小时进行一次统计。

**2\. 请求类型**

  * 统计项：统计所有请求，包括下单、撤单和修改订单中成功请求和失败请求（如被动委托成交、资金不足等）。

**3\. 限频标准**

  * 对下单（POST /spot/orders）和修改订单（PATCH /spot/orders/{order_id}）两个API接口进行限速。基于UID降至每10秒不超过10次请求，建议客户保持自己的成交率在0.1以上。

**4\. 解锁机制**

  * 系统将对用户的交易行为进行动态评估，在每小时一次的检测中，一旦检测到用户策略调整并符合我们的效率标准，将会解除限制。

**说明：**

  * 系统每小时统计最近24小时成交率，至少限制一个小时。如果用户在当前小时被限制，按照每个小时统计一次成交率，若当前小时成交率大于阈值时，下一个小时则限制解除。

####  2.3 成交率计算公式

成交率 = USDT成交金额 / （下单&撤单&修改订单请求数之和）

###  3\. 合约下单频率限制规则

3\. 合约下单频率限制规则合约限频规则  
---  
Tier | ratio | rate limit (uid)  
Tier 1 | [0,1) | 100r/s  
Tier 2 | [1,3) | 150r/s  
Tier 3 | [3,5) | 200r/s  
Tier 4 | [5,10) | 250r/s  
Tier 5 | [10,20) | 300r/s  
Tier 6 | [20,50) | 350r/s  
Tier 7 | >= 50 | 400r/s  
  
> 现货敬请期待

###  4\. 成交比例详细规则

  1. 面向客户群体：VIP≥ 14
  2. 计算周期：7天
  3. 更新时间：每日08:00 (UTC)，系统将根据UTC时间 00:00 的数据，更新成交比例的数据。 
     1. 若成交比率和预期限速有所改善，则提升将于 08:00 (UTC) 立即生效。
     2. 但若成交比率下降，则将会立即进行降低限频。
     3. 若用户的VIP等级下降级为 VIP14以下，其限速将降低为最低档位，立即生效。
     4. 若用户的VIP等级上升为VIP14以上，其根据目前所在等级立刻调整。
  4. 若子账户7日交易量低于1,000,000 USDT，则按照母账户的合计成交比率实施限速。
  5. 对于新创建的子账户，创建时将应用最低档位限速，在 T+1 08:00 (UTC) 进行计算，开始应用上述限速规则。
  6. WebSocket和REST 同时适用该规则

###  5\. 示例

假设用户拥有三个账户，交易永续合约产品 BTC-USDT 和 SOL-USDT 的系数分别为 1 和 0.4。

  1. 账户 A（主账户）：

  * BTC-USDT Maker 交易量为 100 USDT，订单请求数为 10，Taker 交易量为 200 USDT，订单请求数为 20。
  * SOL-USDT Maker 交易量为 20 USDT，订单请求数为 15，Taker 交易量为 20 USDT，订单请求数为 20。
  * 子账户成交比率 = ((100+20)*1 + (200+20)*0.9) / ((10+20) * 1 + (15+20) * 0.4) = 7.23

  2. 账户 B (子账户)：

  * BTC-USDT Maker 交易量为 200 USDT，订单请求数为 20，Taker 交易量为 200 USDT，订单请求数为 30。
  * SOL-USDT Maker 交易量为 20 USDT，订单请求数为 5，Taker 交易量为 30 USDT，订单请求数为 5。
  * 子账户成交比率 = ((200+20)*1 + (200+30)*0.9) / ((20+30) * 1 + (5+5) * 0.4) = 7.91

  3. 账户 C (子账户)：

  * BTC-USDT Maker 交易量为 50 USDT，订单请求数为 5，Taker 交易量为 60 USDT，订单请求数为 8。
  * SOL-USDT Maker 交易量为 100 USDT，订单请求数为 20，Taker 交易量为 120 USDT，订单请求数为 25。
  * 子账户成交比率 = ((50+100)*1 + (60+120)*0.9) / ((5+8) * 1 + (20+25) * 0.4) = 10.06

  4. 母账户综合成交比率 = ((100+20+200+20+50+100)*1 + (200+20+200+30+60+120)*0.9) / ((10+20+20+30+5+8)*1 + (15+20+5+5+20+25)*0.4) = 8.19
  5. 账户限频：

  * 账户 A = max(7.23, 8.19) = 8.19 -> 250r/s
  * 账户 B = max(7.91, 8.19) = 8.19 -> 250r/s
  * 账户 C = max(10.06, 8.19) = 10.06 -> 300r/s

###  6\. 备注

  1. 永续合约成交比例限频发布时间后续将会公布，敬请期待。
  2. 原有永续合约滥用限频规则依然存在，即： 
     1. 成交率 = USDT成交金额 / （下单&撤单&修改订单请求数之和）
     2. 24小时内请求次数超过86,400次请求，并且24小时内无任何订单成交，在下一小时内，永续合约下单限频被限制10r/10s；
     3. 24小时内请求次数超过86,400次请求，并且成交阈值低于1%，在下一小时内，永续合约下单限频为被限制20r/10s。
  3. **现货的成交比例限频，敬请期待。**

##  返回格式

所有的接口返回都是 JSON 格式，需要用户自行转换提取数据。 所有操作成功时都会返回 HTTP 状态码 2xx 。401 说明认证有问题。其他 4xx 状态码说明请求无效。 如果是 5xx 错误，则是服务端处理请求时遇上了未知的严重错误，碰到的话请第一时间反馈。

**返回状态**

返回格式状态码 | 说明  
---|---  
200/201 | 请求执行成功  
202 | 请求已被服务端接受，但是仍在处理中  
204 | 请求成功，服务端没有提供返回体  
400 | 无效请求  
401 | 认证失败  
404 | 未找到  
429 | 请求过于频繁  
5xx | 服务器错误  
  
##  数据类型

数据类型类型 | 说明  
---|---  
`string` | 字符串类型，以双引号表示，涉及金额和价格也会使用字符串标识  
`integer` | 32位整数，主要涉及到状态码、大小、次数等  
`integer(int64)` | 64位整数，主要涉及到ID和高精度时间戳  
`number` | 浮点数，部分时间或统计数据会以浮点形式返回  
`object` | 对象，包含一个子对象{}  
`array` | 数组，包含多组内容  
`boolean` | true 为真，false 为假  
  
##  统一帐户（旧）

TIP

统一账户旧版已不再维护，新版统一账户请查询统一账户

我们从 `4.25.0` 版本之后开始引入对统一账户的支持 。统一账户是Gate新⼀代的交易系统，主要功能在于打破经典账户 (Classic Account) 内各个账户之间的资金隔离，实现多产品业务线之间的多币种保证金共享，用户无需各类交易之间进行资金划转，不同交易产品之间仓位盈亏可以互相抵消，有效提升用户的资金利用率。统一帐户（旧）更详细介绍可以查看 [ 帮助中心](/zh/help/trade/portfolio) 。

用户在使用统一账户（旧） API 功能之前需要先在官网 API 管理页面创建统一账号（旧）的 API Key ， 目前统一账户（旧）只支持现货全仓杠杆和永续合约交易。

> 如果创建 API Key 的权限选项无法选择，首先确保现货全仓账户已经开通并且有初始资金。

###  资金划转

经典帐户与统一帐户是两个不同的帐户，如果想实现多产品业务线之间的多币种保证金共享则必须使用统一帐户。

统一账户（旧）的资金来源于经典账户，由于涉及到经典账户的资金变动，资金的转入转出操作都只能使用经典账户的 API Key 来执行。

统一账户（旧）基于原有经典账户的全仓杠杆账户升级，因此经典账户只需要将自己的现货资金划转到现货全仓杠杆账户，即可为统一账户（旧）充值。 同理资金的转出操作也必须由经典账户从全仓杠杆账户划转到自己的现货账户。

统一账户（旧）的 API Key 只能在自己的多个账户之间划转， 由于保证金共享，统一账户（旧）也无需将全仓账户的资金划转到合约账户 （我们也限制了向合约账户的转入功能）。 但是如果合约账户有资金需要提取，必须由统一账户（旧）划转到自己的现货全仓杠杆账户，才可以交给经典账户执行资金转出动作。

###  现货交易

统一账户（旧）的现货交易与经典账户几乎完全一致，除了在订单操作中需要指定 `account` 的地方必须要指定 `cross_margin` ， 比如想挂 `BTC_USDT` 交易对的买单，下单请求会类似于
    
    
    POST /spot/orders
    
    {
      "currency_pair": "BTC_USDT",
      "account": "cross_margin",
      "side": "buy",
      ...
    }
    

其他订单相关限制请直接参考各接口说明。

TIP

需要特别说明的是，统一账户（旧）升级自经典账户的现货全仓杠杆账户，经典账户的 API Key 原先就支持操作现货全仓杠杆账户， 为了不影响经典账户已有的操作，我们依然保留了经典账户的这个功能。所以不管是经典账户还是统一账户（旧）的 API Key 都可以操作同一个现货全仓杠杆账户（注意合约账户是分开的）

###  永续合约交易

统一账户（旧）永续合约的 API 操作与经典账户完全相同，不过当前只支持 USD 结算

TIP

需要留意一下在合约交易的部份，并没有像现货交易在使用经典帐户 API Key 的时候有做对全仓杠杆帐户的兼容性处理，所以当使用经典帐户 API Key 进行合约交易的时候，资产是保留在 `经典帐户-合约` 下面，而使用统一帐户 API Key 进行合约交易的时候，资产是保留在 `统一帐户-合约` 下面，这两个是不同的合约帐号。另外在 `经典帐户-现货` 下的资金, 是无法与 `经典帐户-合约` 共享保证金的。

##  Trace ID

API响应会携带header: X-Gate-Trace-ID 。这个header用于链路追踪。

##  Self-Trade Prevention(STP)

###  名词解释

**Self-Trade Prevention** : 自成交保护机制，后文中都简称为`STP`

**CN** : Cancel new,取消新订单，保留老订单

**CO** : Cancel old,取消⽼订单，保留新订单

**CB** : Cancel both,新旧订单都取消

###  成交策略

目前支持三种自成交保护策略，分别是`CN`、`CO`、`CB`。

我们实现了`STP用户组`来提供给用户，被添加到同一个组内的多个用户账户ID，自成交或彼此成交会受到限制，限制策略取决于用户账户以`taker` 角色下单时指定的`stp_act`参数。

当用户的账户ID添加到指定`STP用户组`后，下单时可以自定义`stp_act`参数，系统会按照用户传入的策略进行`STP用户组` 内撮合成交的限制；如果下单时没有指定`stp_act`策略，成交时默认按照`CN`策略执行。

当下单用户的账户ID没有进入任何`STP用户组`，同时下单又指定了`stp_act`参数，此时系统会报错，无法下单。用户需要去掉`stp_act` 参数，此时用户成交不受任何自成交策略限制。

###  接口参数调整

以合约下单为例，有如下调整：
    
    
    POST /futures/{settle}/orders
    

新增请求参数

接口参数调整名称 | 位置 | 类型 | 必选 | 描述  
---|---|---|---|---  
stp_act | body | string | 否 | stp策略，包括：  
\- cn 取消新订单，保留旧订单  
\- co 取消老订单，保留新订单  
\- cb 取消老订单和新订单  
  
新增返回参数（查询订单列表接口同理）

接口参数调整名称 | 类型 | 必选 | 限制 | 描述  
---|---|---|---|---  
stp_act | string | 否 | none | STP策略，包括：  
\- `cn` 取消新订单，保留旧订单  
\- `co` 取消老订单，保留新订单  
\- `cb` 取消老订单和新订单  
stp_id | integer(int64) | 否 | 只读 | 用户所在`STP用户组`的id，是引擎判断用户之间订单是否可以成交的依据。如果账户没有进入`STP用户组`，`stp_id`不返回。  
finish_as | string | 否 | 只读 | 结束方式：  
\- **stp: 订单发生自成交限制而被撤销**  
  
###  使用场景

`组织A`下有多个账户，其中几个账户id分别为`101`,`102`,`103`。

为了防止组织内部账户下单发生自成交，管理员创建了一个`STP用户组`，用户组id为`100`，将账户`101`和`102`加入到该`STP用户组` 中，此时组内成员为`[101,102]`

T1: `STP`策略版本上线。

T2: `组织A`账户`101`下做空单后，市场订单深度没有与之匹配的订单可以撮合成交，此时下单角色是`maker`，订单状态是`open` 。返回参数会增加如下信息返回
    
    
    {
    	"status":"open",
    	"stp_act":"cn",
    	"stp_id":100
    }
    

T3: `组织A`账户`101`/`102`下做多单后，市场深度匹配到`101`账户下的做空订单可以撮合成交，当前角色是`taker` ，系统判断到两个订单的`stp_id`均为100，此时会限制成交，限制策略以`taker`为准。

  * 如果选择了`cn`，`taker`下的订单会被取消，订单会结束，返回关键参数为：

    
    
    {
    	"status":"finished",
    	"stp_act":"cn",
    	"stp_id":100,
    	"finish_as":"stp"
    }
    

  * 如果选择了`co`，`taker`下的订单会被保留，订单状态为`open`，系统默认会取消`maker`的订单（`maker`可以通过查询订单列表，订单状态会跟上一种情况一致。）

  * 如果选择了`cb`，`taker`下的订单会被取消，订单会结束。系统默认会取消`maker`的订单（`maker` 可以通过查询订单列表）。两者的订单结束原因都为`stp`

    
    
    {
    	"status":"finished",
    	"stp_act":"cb",
    	"stp_id":100,
    	"finish_as":"stp"
    }
    

T3': `组织A`账户`103`下做多单后，市场深度匹配到`101`账户下的做空订单可以撮合成交，由于`103`用户没有被添加到组里，`stp_id` 为0，系统判断两边的`stp_id`不一致，可以成交。订单信息为：
    
    
    {
    	"status":"finished",
    	"stp_id":0,
    	"finish_as":"filled"
    }
    

##  统一账户

###  说明

用户开通统一账户后，可以使用现货账户中的资产作为交易的保证金， 账户内的各币种资产将会根据其流动性，定义相应的调整系数，再统一折算为USD，来统一计算账户的资产及持仓价值。

统一账户最大可借贷额度是用户对于当前交易市场的最大借贷额度。平台将根据用户的可用保证金数量以及平台风控规则等限制，计算用户当前的最大借贷额度。统一账户产生自动借款后，平台即时对所借数字资产开始计息。

目前统一账户支持开通`多币种保证金`模式，后续将推出`组合保证金`模式，可根据自身需求进行账户模式切换，敬请期待。

相关的接口请查看统一账户文挡，开通统一账户后可进行调用。更详细介绍可以查看 [ 帮助中心](https://www.gate.com/zh-tw/unified-trading-account) 。

###  API接入流程

  * 创建新 `API KEY` 或者更新已有 `API KEY` 权限，勾选 `unified` 权限
  * 使用经典账户 `API KEY` 调用 `PUT /unified/unified_mode` 接口，或者 `WEB` 页面升级新版统一账户
  * 使用 `/api/v4/spot/**` 接口进行现货相关操作（下单、修改订单、查询订单等）， `account` 类型增加 `unified` 选项
  * 使用 `/api/v4/futures/**` 接口进行永续合约相关操作（下单、修改订单、查询订单等）
  * 使用 `/api/v4/unified/**` 接口进行统一账户相关操作（账户查询、借贷查询）

###  现货交易

统一账户的现货交易与经典账户一致，在订单操作中指定 `account=unified`，或者指定`account=spot`系统检测账户为统一账户时会自动处理为统一账户订单， 比如想挂 `BTC_USDT` 交易对的买单，下单请求会类似于
    
    
    POST /spot/orders
    
    {
      "currency_pair": "BTC_USDT",
      "account": "unified",
      "side": "buy",
      ...
    }
    

其他订单相关限制请直接参考各接口说明。

###  永续合约交易

统一账户永续合约的 API 操作与经典账户完全相同，当前只支持 USDT 结算

###  保证金公式

保证金公式详情见：[ 保证金公式](https://www.gate.com/zh/help/unified-account/risk_control_mechanism/33018)

##  资产流水类型

###  通用

  * unknown : 未知
  * login : 登陆
  * withdraw : 提现
  * ch_pass : 修改密码
  * ch_fund_pass : 修改资金密码
  * login_failed : 登录失败
  * axs_account : 访问账号
  * req_pass_ch : 修改密码请求
  * req_fund_pass_ch : 修改资金密码请求
  * fund_pass_ent : 输入交易密码
  * bank_card_add : 绑定银行卡
  * frw : 提现人脸验证

###  订单

  * new_order : 下单
  * cancel_order : 取消订单
  * order_fill : 成交
  * order_rej : 订单退回
  * order_fee : 成交手续费
  * system_fee : 系统成交手续费

###  充提

  * withdraw : 提现
  * deposit : 充值
  * deposit_rej : 充值退回
  * withdraw_rej : 提现退回
  * cancel_withdraw : 取消提现
  * withdraw_gatecode : 充值码提现
  * withdraw_fireblock : Fireblock提现
  * withdraw_copper : Copper提现
  * startup_withdraw : Startup项目提现
  * deposit_gatecode : 充值码充值
  * deposit_fireblock : Fireblock充值
  * deposit_copper : Copper充值
  * buy_cl : 法币入金 Legend
  * buy_cc : 法币入金 Cabital
  * deposit_finmo : Finmo充值

###  Startup

  * startup_prtcp : 参加Startup
  * startup_refund : 退回Startup
  * startup_sale : Startup认购
  * startup_sale_rb : Startup认购退回

###  返佣

  * referral_rebate : 推荐奖励
  * sec_rebate_out : 二级返佣系统账户转出
  * sec_rebate_in : 用户获得二级返佣
  * ab_rebate : API Broker返佣上级收入
  * eb_rebate : Exchange Broker返佣上级收入
  * u_rebate : 普通邀请返佣用户收入
  * ads_rebate : 代理商直接上级返佣收入
  * au_rebate : 代理商返佣用户收入
  * pis_rebate : 合伙人间接上级返佣收入
  * pds_rebate : 合伙人直接上级返佣收入
  * pu_rebate : 合伙人用户返佣收入

###  兑换

  * eth_swap : ETH分叉兑换
  * dust_swap_dctd : 小额资产兑换
  * dust_swap_gt_add : 小额资产GT增加
  * dust_swap_fee : 小额币种手续费扣除
  * cv_buy : 闪兑买入
  * cv_sell : 闪兑卖出

###  C2C

  * c2c_mop : C2C商家下单
  * c2c_moc : C2C取消商家单
  * c2c_rop : C2C用户下单
  * c2c_roc : C2C取消用户单
  * c2c_om : C2C成交
  * c2c_or : C2C退回
  * c2c_fee : C2C手续费

###  奖励

  * deposit_bonus : 充值奖励
  * trading_rewards : 交易奖励
  * purchase_bonus : 买入奖励
  * airdrop : 空投奖励
  * award : 限时奖励
  * mining_rewards : 挖矿奖励

###  账户出入金

  * margin_in : 逐仓杠杆转入
  * margin_out : 逐仓杠杆转出
  * spot_settle_out: 现货同币种结算转出
  * spot_settle_in: 现货同币种结算转入
  * lending_in : 理财转入
  * lending_out : 理财转出
  * cross_in : 统一账户转入
  * cross_out : 统一账户转出
  * perp_in : 永续合约转入
  * perp_out : 永续合约转出
  * perp_settle_in: 永续合约多币种结算转入
  * perp_settle_out: 永续合约多币种结算转出
  * delivery_in : 交割合约转入
  * delivery_out : 交割合约转出
  * ai_in : 定投转入
  * ai_out : 定投转出
  * e_options_in : 短时期权转入
  * e_options_out : 短时期权转出
  * options_in : 期权转入
  * options_out : 期权转出
  * cbbc_in : 牛熊证转入
  * cbbc_out : 牛熊证转出
  * warrant_in : 窝轮转入
  * warrant_out : 窝轮转出
  * subaccount_trf : 子账户资金划转
  * quant_in : 量化交易转入
  * quant_out : 量化交易转出
  * pay_in : 支付账户转入
  * pay_out : 支付账户转出
  * fct_in : 合约跟单交易转入
  * fct_out : 合约跟单交易转出

###  点卡

  * points_purchase : 购买点卡
  * points_expiration : 限时点卡
  * points_trf : 点卡转让
  * points_trf_rej : 点卡转让退回

###  金融

  * lending_lent : 理财借出
  * collected : 收款
  * interest_in : 利息收入
  * lending_fee : 理财手续费抵扣
  * hodl_int : PoS利息收益
  * redeem : 赎回
  * lend : 借出
  * dual_purchased : 双币理财申购
  * dual_settled : 双币理财结算
  * liq_add : 流动性添加
  * liq_rm : 流动性赎回
  * liq_rebalanced : 流动性调仓
  * slot_int_in : 插槽解锁利息收益
  * str_int_in : 结构性理财利息收益

###  借贷

  * borrow : 借款
  * repay : 还款
  * margin_borrow : 逐仓杠杆借入
  * margin_repay : 逐仓杠杆还款
  * margin_interest_out : 逐仓杠杆扣息
  * cl_borrow : 抵押借入
  * cl_repay : 抵押还款
  * cl_dctd : 抵押扣除
  * cl_rtd : 抵押退还
  * cross_borrow : 统一账户借入
  * cross_repay : 统一账户还款
  * interest_out : 利息

###  币圈

  * donation : 捐款
  * rp_sent : 发送红包
  * rp_rcvd : 收取红包
  * rp_rej : 红包退回
  * ls_offered : 直播打赏
  * ls_rcvd : 直播被打赏
  * pt_offered : 币圈打赏
  * pt_rcvd : 币圈被打赏
  * subs_deduct : 订阅扣费
  * subs_in : 订阅费入账
  * subs_refund : 订阅费退回
  * subs_in_rcvd : 订阅费用退回入账

###  PUSH交易

  * push_dctd : push扣除
  * push_rcvd_dctd : push接收扣除
  * push_canceled : push撤单
  * push_rej : push拒绝
  * push_sent : push转让
  * push_rcvd : push接收

###  量化跟单

  * quant_return : 量化交易退回
  * quant_cmn_in : 量化复制分红转入
  * quant_cmn_out : 量化复制分红转出
  * quant_cmn_rtd : 量化复制分红退回
  * fct_refund : 合约跟单交易资金退回
  * fct_rcvd : 合约带单分红转入
  * fct_fee : 合约跟单分红转出
  * fct_fee_refund : 合约跟单分红资金退回

###  NFT

  * nft_mp : 拍卖支付保证金
  * nft_bm : 拍卖购买
  * nft_om : 拍卖出售
  * ntf_mr : 拍卖保证金退回
  * nft_amr : 拍卖流拍获得保证金
  * nft_ocb : 订单取消退回
  * nft_fb : 一口价购买
  * nft_fs : 一口价出售
  * nft_ob : 报价购买
  * nft_os : 报价出售
  * nft_cr : 取消报价退款
  * nft_ir : 报价失效退款
  * nft_wf : 提现服务费
  * nft_wfr : 提现手续费退回
  * ntf_mf : 多副本创作服务费
  * ntf_mfr : 多副本创作服务费退回
  * ntf_royalty : 用户版税收入
  * nft_cd : 订单取消扣款
  * nft_crd : 交易撤销版税扣款
  * nft_cf : 众筹差额扣款
  * nft_cfr : 众筹差额退款
  * nft_ammf : 流动性池充值冻结
  * nft_ammw : 流动性池提现
  * nft_ammdf : 流动性池手续费
  * nft_ammd : 流动性池交易成功打款

##  资产流水编码

###  资产

####  C2C

  * 301 : C2C商家下单
  * 302 : C2C 取消商家单
  * 303 : C2C用户卖出
  * 304 : C2C取消用户单
  * 305 : C2C用户买入
  * 308 : C2C手续费
  * 309 : C2C 保证金冻结
  * 310 : C2C 保证金退回
  * 311 : C2C 保证金赔付
  * 312 : C2C共享资产退回
  * 313 : C2C申诉冻结
  * 314 : C2C 申诉解冻
  * 315 : C2C 快捷闪兑买入
  * 110106 : C2C 商家保证金理财利息

####  充值

  * 110 : 链上充值
  * 121 : 充值码
  * 122 : Fireblocks充值
  * 123 : Wrongdeposit Fee
  * 124 : Copper 充值
  * 125 : 资产寻回手续费退回
  * 1907 : push转让
  * 1908 : 手机/邮箱/UID 充值
  * 2650 : Bitgo 充值
  * 5107 :

####  兑换

  * 1301 : 小额资产兑换
  * 1302 : 小额资产GT增加
  * 1307 : 小额资产兑换
  * 1310 : 小额资产兑换
  * 1322 : 小额资产兑换（USDT）
  * 1323 : 小额兑换USDT增加
  * 2601 : 闪兑买入
  * 2602 : 闪兑卖出
  * 2603 : 一键还款出账
  * 2604 : 一键还款入账
  * 2605 : 闪兑买入
  * 2606 : 闪兑卖出
  * 2612 : 闪兑买入
  * 2613 : 闪兑卖出
  * 2615 : OTC-订单成交
  * 2616 : OTC-订单成交

####  其他

  * 106 : 捐款
  * 115 : 快照
  * 118 : 币种基数调整
  * 131 : 集合竞价冻结
  * 132 : 集合竞价解冻
  * 141 : ETF资产合并-扣款
  * 142 : ETF资产合并-加款
  * 143 : 币种更名扣款
  * 144 : 币种更名加款
  * 181 : ETH分叉兑换
  * 182 : ETH2兑换
  * 329 : Gate Connect-退款
  * 330 : Gate Connect-购买
  * 331 : Gate Connect-卖出
  * 501 : 领取分叉币
  * 502 : 返还分叉币
  * 801 : 发送红包
  * 802 : 收取红包
  * 803 : 红包退回
  * 804 : 直播打赏
  * 805 : 直播被打赏
  * 806 : 币圈打赏
  * 807 : 币圈被打赏
  * 903 : 限时点卡
  * 913 : 点卡兑换商品
  * 915 : 点卡兑换商品退回
  * 917 : 点卡过期回收
  * 1001 : 法币借贷发布广告单
  * 1002 : 法币借贷撤销广告单
  * 1003 : 法币借贷下单
  * 1004 : 法币借贷完成还款
  * 1005 : 法币借贷撤单
  * 1006 : 法币借贷手续费
  * 1007 : 法币借贷平仓
  * 1008 : 法币借贷补仓
  * 1311 : 小额资产兑换
  * 1312 : 小额资产USDT增加
  * 1501 : 订阅扣费
  * 1502 : 订阅费入账
  * 1503 : 订阅费退回
  * 1504 : 订阅费用退回入账
  * 2950 : BUGSFUNDED 报名费
  * 2951 : BUGSFUNDED 报名费退款
  * 2952 : BUGSFUNDED 实盘资金-扣款
  * 2953 : BUGSFUNDED 利润划出
  * 2954 : BUGSFUNDED 利润划入
  * 2956 : BUGSFUNDED 实盘资金-划入
  * 2970 : PUMP售卖活动-退回购买金额
  * 2971 : PUMP售卖活动-发放代币
  * 2972 : PUMP售卖活动-扣除购买金额
  * 3701 : OTC交易-买入
  * 3702 : OTC交易-卖出
  * 3703 : OTC交易-取消
  * 5104 : Fireblocks手续费退回
  * 5105 : 预扣 Gas 费
  * 5106 : 回滚预扣 Gas 费
  * 100101 : 平仓尾差转出
  * 100102 : 平仓尾差转入
  * 110101 : 低流通币种提现手续费退回
  * 110102 : 低流通币种提现手续费
  * 130101 : 创建代币
  * 130102 : 创建代币失败退回
  * 130111 : KOL 代币未上市退款
  * 130112 : KOL 代币超额认购退款
  * 130113 : KOL 代币赎回
  * 130114 : KOL 代币认购
  * 130115 : KOL 代币链上手续费
  * 130118 : KOL 代币链上手续费退款
  * 130119 : KOL 代币认购失败退款
  * 150101 : 币种回购-加款
  * 150102 : 货币回购-借记
  * 150201 : 借入映射资金
  * 150202 : 归还映射资金
  * 150203 : 转入资金
  * 150204 : 转出资金
  * 150208 :
  * 180101 : Alpha 代币下架退款

####  划转

  * 601 : 转出至杠杆账户
  * 602 : 从杠杆账户转入
  * 701 : 转出至永续合约账户
  * 702 : 从永续合约账户转入
  * 703 : 转出至交割合约账户
  * 704 : 从交割合约账户转入
  * 1401 : 子账号资金划转
  * 150215 : 子账号资金划转
  * 150216 : 子账号资金划转
  * 150217 : 子账号资金划转
  * 150218 : 子账号资金划转
  * 150219 : 子账号资金划转
  * 1603 : 转出至期权账户
  * 1604 : 从期权账户转入
  * 3001 : 转出至支付账户
  * 3008 : 从支付账户转入
  * 3028 : 支付账户划转（退款）
  * 100202 : 转出至 TradFi 账户
  * 170201 : 从跨所账户转入
  * 170204 : 转出至跨所账户

####  奖励

  * 120102 : 合约积分空投

####  提现

  * 4 : 链上提现
  * 17 : 充值码提现
  * 18 : Fireblocks提现
  * 19 : Copper 提现
  * 104 : 取消链上提现
  * 1901 : 手机/邮箱/UID 提现
  * 1903 : push接收扣除
  * 1905 : 手机/邮箱/UID 取消提现
  * 1906 : 手机/邮箱/UID 提现退回
  * 2651 : Bitgo 提现

####  支付

  * 2609 : 闪兑买入
  * 2610 : 闪兑卖出
  * 2611 : 闪兑退款
  * 3001 : 转出至支付账户
  * 3017 :
  * 3018 : 划转（下发）
  * 3019 : 提现法币
  * 3020 : 提现法币退款
  * 3024 :
  * 3026 : 收款
  * 3027 : 退款
  * 3519 : 礼品卡 - 创建
  * 3520 : 礼品卡 - 兑换
  * 190101 : 结算 - 增加
  * 190301 : 待接收
  * 190305 : 转账成功
  * 190306 : 超时退回
  * 190307 : 已撤销

####  活动&奖励

  * 401 : 充值奖励
  * 402 : 交易奖励
  * 403 : 买入奖励
  * 404 : 空投奖励
  * 405 : 反馈奖励
  * 3101 : 卡券中心点卡兑换
  * 3104 : 现货代币空投
  * 3105 : 卡券手续费返现
  * 3120 : Candydrop 奖励
  * 3150 : 活动代币发放失败
  * 3801 : 体验券盈利结转
  * 120101 : 合约积分奖励
  * 140203 : 现金券奖励兑换
  * 140204 : 激励空投
  * 140205 : 激励空投解锁
  * 140206 : 激励空投回收
  * 140207 : 锁仓扣除

####  现货大宗交易

  * 3401 : 现货大宗交易转入
  * 3402 : 现货大宗交易转出

####  返佣

  * 109 : 普通邀请上级推荐返佣
  * 162 : 代理商间接上级返佣收入
  * 164 : 代理商直接上级返佣收入
  * 166 : 代理商返佣用户收入
  * 191 : 普通邀请返佣用户收入
  * 3301 : 超级代理商直接上级返佣
  * 3321 : Affiliate Ultra Indirect Superior Rebate
  * 3341 : 超级代理商自返佣
  * 3381 : 观察期返佣
  * 3390 : API Broker返佣上级收入
  * 3410 : Exchange Broker返佣上级收入
  * 4002 : 佣金提取收入
  * 4009 : 用户奖励自提
  * 4011 : 扣除负maker

###  交易

####  期权

  * dnw : 转入转出
  * fee : 交易手续费
  * prem : 权利金
  * refr : 推荐人返佣
  * set : 结算盈利

####  永续

  * bonus_dnw : 体验金充提
  * bonus_offset : 体验金抵扣
  * dnw : 转入转出
  * fee : 交易手续费
  * fund : 资金费用
  * pnl : 减仓盈亏
  * point_convert : 点卡转化
  * point_dnw : 点卡转入转出
  * point_fee : 点卡交易手续费
  * point_refr : 点卡推荐人返佣
  * pv_dnw : 体验仓位赠金充值与回收
  * refr : 推荐人返佣

####  交割

  * dnw : 转入转出
  * fee : 交易手续费
  * pnl : 减仓盈亏
  * point_dnw : 点卡转入转出
  * point_fee : 点卡交易手续费
  * point_refr : 点卡推荐人返佣
  * refr : 推荐人返佣
  * settle : 结算
  * settle_fee : 结算手续费

####  Alpha

  * 6001 : Alpha 下单
  * 6002 : Alpha 下单
  * 6003 : Alpha 成交
  * 6004 : Alpha 成交
  * 6005 : Alpha 交易失败
  * 6006 : Alpha 交易失败
  * 6007 : MemeBox 交易手续费
  * 6010 : Alpha 空投
  * 6011 : Alpha 买入订单撤销
  * 6012 : Alpha 买入订单撤销
  * 130103 : Alpha 闪兑卖出
  * 130104 : Alpha 闪兑买入
  * 130105 : Alpha 闪兑失败退回
  * 130106 : Alpha 闪兑卖出
  * 130107 : Alpha 闪兑买入
  * 130108 : Alpha 闪兑失败退回

####  交易机器人

  * 1701 : 机器人交易转入
  * 1702 : 机器人交易转出
  * 1703 : 机器人交易退回
  * 2401 : 机器人复制分红转入
  * 2402 : 机器人复制分红转出
  * 2403 : 机器人复制分红退回
  * 150210 : 期权机器人交易转入
  * 150211 : 期权机器人交易转出

####  保证金交易

  * 659 : 异币种还款入账
  * 660 : 异币种还款出账
  * 670 : 保证金交易借入
  * 671 : 保证金交易还款
  * 672 : 保证金交易扣息
  * 682 : 补充保险基金
  * 683 : 保险基金填补损失
  * 685 : 平台借币扣息

####  现货

  * 101 : 卖出
  * 102 : 买入
  * 151 : 成交手续费

####  跟单

  * 3151 : 跟单无忧金赔付
  * 3201 : 合约跟单交易转入
  * 3202 : 合约跟单交易转出
  * 3203 : 合约跟单交易资金退回
  * 3204 : 合约带单分红转入
  * 3205 : 合约跟单分红转出
  * 3206 : 合约跟单分红资金退回
  * 3601 : 现货带单交易转入
  * 3602 : 现货带单交易转出
  * 3603 : 现货带单交易退回
  * 3604 : 现货跟单交易转入
  * 3605 : 现货跟单交易转出
  * 3606 : 现货跟单交易资金退回
  * 3607 : 现货带单分红转入
  * 3608 : 现货跟单分红转出
  * 3609 : 现货跟单分红资金退回
  * 210101 : 跟单体验金回收
  * 210102 : 跟单体验金发放

####  逐仓杠杆

  * 601 : 转出至杠杆账户
  * 602 : 从杠杆账户转入
  * 605 : 逐仓杠杆借入
  * 606 : 逐仓杠杆还款
  * 616 : 强平手续费
  * 675 : 逐仓杠杆计息
  * 676 : 逐仓杠杆扣息

###  理财

####  HODLer Airdrop

  * 2614 : HODLer Airdrop

####  Launchpad

  * 1134 : Launchpad 扣款
  * 1135 : Launchpad 退回
  * 1136 : Launchpad 分发
  * 1203 : Launchpad 锁仓

####  Launchpool

  * 1174 : 邀请奖励
  * 1251 : 质押
  * 1253 : 主动赎回
  * 1255 : 派息奖励
  * 1258 : 自动赎回

####  余币宝

  * 661 : 赎回-活期
  * 662 : 申购-活期
  * 669 : 利息收益-活期
  * 681 : 额外奖励-活期
  * 686 : 申购-定期
  * 687 : 赎回-定期
  * 688 : 利息收益-定期
  * 689 : 额外奖励-定期
  * 160301 : 定期理财利息收益
  * 160302 : 定期理财额外奖励
  * 160303 : 定期理财赎回
  * 160304 : 定期理财申购
  * 160401 : 加息收益-定期
  * 160402 : 定期理财加息收益
  * 160406 : Boost 奖励-定期

####  双币宝

  * 2001 : 双币投资申购
  * 2004 : 双币投资结算
  * 2011 : 申购抄底宝产品
  * 2012 : 抄底宝产品到期回款
  * 2021 : 申购逃顶宝产品
  * 2022 : 逃顶宝产品到期回款
  * 160201 : 双币投资到期回款
  * 160202 : 双币投资申购

####  定投理财

  * 911 : 定投转出
  * 912 : 定投转入

####  抵押借币

  * 635 : 固定利率抵押利息
  * 640 : 活期扺押借入
  * 641 : 活期抵押还款
  * 642 : 活期平仓还款
  * 643 : 活期平仓利息
  * 644 : 活期抵押利息
  * 645 : 抵押扣除
  * 646 : 抵押退还
  * 647 : 抵押调整
  * 648 : 平仓退还
  * 649 : 平仓手续费
  * 655 : 固定利率抵押借入
  * 656 : 固定利率抵押还款
  * 657 : 固定利率平仓还款
  * 658 : 固定利率平仓利息
  * 696 : 提前还款违约金
  * 697 : 提前还款违约金退还
  * 160601 : 平仓赎回余币宝保证金扣款
  * 160602 : 平仓剩余余币宝保证金退还

####  持币生息

  * 120103 : 合约持币生息
  * 160501 : 现货持币生息

####  杠杆无忧

  * 160608 : 杠杆无忧到期回款
  * 160609 : 杠杆无忧申购

####  私募基金

  * 160101 : 私募基金到期回款
  * 160102 : 私募基金申购
  * 160103 : 私募基金手动赎回回款
  * 160104 : 私募基金收益

####  第三方基金

  * 170101 : 第三方基金申购款
  * 170111 : 第三方基金赎回款
  * 170112 : 第三方基金清算款
  * 170113 : 第三方基金申购失败退款
  * 170206 : 第三方基金现金分红款

####  量化基金

  * 739 : 财富管理返佣
  * 751 : 量化基金锁仓
  * 753 : 量化基金解锁
  * 754 : 量化基金解锁收益

####  链上赚币

  * 1171 : 额外奖励
  * 1173 : 额外奖励
  * 1181 : 质押
  * 1184 : 赎回
  * 1186 : 利息派发
  * 1191 : 质押
  * 1194 : 赎回
  * 1196 : 利息派发
  * 160607 : 撤销赎回

##  异常处理

APIv4 对于所有的异常请求，会设置状态码为非 2xx ，同时返回一个 JSON 格式的返回体来描述具体的错误信息。

返回体的格式通常如下所示：
    
    
    {
      "label": "INVALID_PARAM_VALUE",
      "message": "Invalid parameter `text` with value: abc"
    }
    

  * `label` 用于标识某种错误的类型，格式 `string` ，它的值是一个固定的列表（见下方）。程序处理可以使用 `label` 字段的内容来设定和捕获异常
  * `message` (或 `detail`) 表示详细的错误信息，方便 API 对接时，理解具体是因为什么样的参数设置导致请求出现了异常。 该字段内容不建议用于异常的捕获或识别。

以 Python [requests ](https://requests.readthedocs.io/zh_CN/latest/) 为例，异常的处理流程可以参考如下所示：

> 以下示例的异常捕获流程只涉及到业务相关的异常，网络连接超时等其他非业务相关的异常还需要自行处理。
    
    
    import requests
    
    r = requests.get("https://api.gateio.ws/api/v4/futures/btc/contracts/BTC_USD")
    try:
        r.raise_for_status()
    except requests.HTTPError:
        # 捕获非 2xx 错误，尝试解析 body 里返回的错误消息，并根据不同 label 做不同的异常处理
        if r.json()['label'] == 'xxx':
            print(r.json())
    

以 [Python SDK ](https://github.com/gate/gateapi-python) 为示例：
    
    
    import json
    from gate_api import FuturesApi
    from gate_api.rest import ApiException
    
    api = FuturesApi()
    try:
        api.get_futures_contract(settle='btc', contract="BTC_USD")
    except ApiException as e:  # ApiException 封装了异常的各种信息，详情可参看类定义
        detail = json.loads(e.value.body)
        if detail['label'] == 'xxx':
            print(detail)
    

##  异常 `label` 列表

  * 请求参数或格式问题

异常 label 列表`label` | 含义  
---|---  
INVALID_PARAM_VALUE | 参数输入值无效  
INVALID_PROTOCOL | 参数输入值无效  
INVALID_ARGUMENT | 参数无效  
INVALID_REQUEST_BODY | 无效请求体  
MISSING_REQUIRED_PARAM | 缺少必选参数  
BAD_REQUEST | 无效请求  
INVALID_CONTENT_TYPE | 无效的 Content-Type 头部格式  
NOT_ACCEPTABLE | Accept 头部无法满足  
METHOD_NOT_ALLOWED | 请求方法不接受  
NOT_FOUND | 资源 URL 不存在  
  
  * 认证相关

异常 label 列表`label` | 含义  
---|---  
INVALID_CREDENTIALS | 认证接口缺少用户认证信息  
INVALID_KEY | 无效的 API Key  
IP_FORBIDDEN | 请求 IP 不在白名单  
READ_ONLY | 请求账户只读，不可执行写操作  
INVALID_SIGNATURE | 无效签名  
MISSING_REQUIRED_HEADER | 缺少必要的认证头部  
REQUEST_EXPIRED | 客户端时间与服务端时间相差过大  
ACCOUNT_LOCKED | 账户被锁定  
FORBIDDEN | 账户无权执行该操作  
API_WITHDRAW_DISABLED | API提现操作临时禁用  
INVALID_WITHDRAW_ID | 无效的提现ID  
INVALID_WITHDRAW_CANCEL_STATUS | 当前提现状态无法取消  
  
  * 钱包相关

异常 label 列表`label` | 含义  
---|---  
SUB_ACCOUNT_NOT_FOUND | 子账户不存在  
SUB_ACCOUNT_LOCKED | 子账号被冻结  
MARGIN_BALANCE_EXCEPTION | 杠杆账户异常  
MARGIN_TRANSFER_FAILED | 杠杆资金划转失败  
TOO_MUCH_FUTURES_AVAILABLE | 合约账户总资产达到上限  
FUTURES_BALANCE_NOT_ENOUGH | 合约账户余额不足  
ACCOUNT_EXCEPTION | 账户异常  
SUB_ACCOUNT_TRANSFER_FAILED | 子账户资金划转失败  
ADDRESS_NOT_USED | 指定的钱包地址未在网页执行过划转  
TOO_FAST | 提现频率过快  
WITHDRAWAL_OVER_LIMIT | 超出提现额度  
DUPLICATE_REQUEST | 重复请求  
ORDER_EXISTS | 订单已存在  
INVALID_CLIENT_ORDER_ID | 无效的client_order_id  
RISK_ERROR | 触发风控  
NEGATIVE_ASSETS | 安全提现检查存在负资产  
RECEIVE_ERROR | 接收失败  
DEDUCTION_ERROR | 转账人扣款失败  
FINANCE_ERROR | 财务账户扣款失败  
BALANCE_NOT_ENOUGH | 余额不足  
  
  * 现货和杠杆相关

异常 label 列表`label` | 含义  
---|---  
INVALID_PRECISION | 无效的精度  
INVALID_CURRENCY | 无效的币种信息  
INVALID_CURRENCY_PAIR | 无效的交易对  
POC_FILL_IMMEDIATELY | 被动委托会立即成交  
ORDER_NOT_FOUND | 订单不存在  
ORDER_CLOSED | 订单已结束  
ORDER_CANCELLED | 订单已撤销  
QUANTITY_NOT_ENOUGH | 数量不足  
BALANCE_NOT_ENOUGH | 余额不足  
MARGIN_NOT_SUPPORTED | 该交易对不支持杠杆交易  
MARGIN_BALANCE_NOT_ENOUGH | 杠杆账户余额不足  
AMOUNT_TOO_LITTLE | 数额小于最低值  
AMOUNT_TOO_MUCH | 数额过大  
REPEATED_CREATION | 重复创建  
LOAN_NOT_FOUND | 借贷订单不存在  
LOAN_RECORD_NOT_FOUND | 借贷记录不存在  
NO_MATCHED_LOAN | 没有借贷记录能满足借入需求  
NOT_MERGEABLE | 借贷单不可合并  
NO_CHANGE | 修改的参数与当前状态无区别  
REPAY_TOO_MUCH | 还款数额超出借款数额  
TOO_MANY_CURRENCY_PAIRS | 批量下单指定了过多交易对  
TOO_MANY_ORDERS | 批量下单的单个交易对下单数过多  
MIXED_ACCOUNT_TYPE | 批量下单中使用了多个账户类型  
AUTO_BORROW_TOO_MUCH | 自动借入超出最多可借  
TRADE_RESTRICTED | 高负债率导致交易操作被限制  
FOK_NOT_FILL | FOK 订单无法全部成交  
INITIAL_MARGIN_TOO_LOW | 用户总初始保证金率太低  
NO_MERGEABLE_ORDERS | 找不到能够合并的借贷订单  
ORDER_BOOK_NOT_FOUND | 市场深度不足  
FAILED_RETRIEVE_ASSETS | 获取账户资产失败  
CANCEL_FAIL | 订单撤销失败  
PRICE_THRESHOLD_EXCEEDED | 触发限价保护  
  
  * 合约相关

异常 label 列表`label` | 含义  
---|---  
USER_NOT_FOUND | 用户无合约账户  
CONTRACT_NO_COUNTER | 没有匹配的对手单  
CONTRACT_NOT_FOUND | 合约未找到  
NOT_FOUND | 请求路径不存在  
RISK_LIMIT_EXCEEDED | 委托超出风险限额  
INSUFFICIENT_AVAILABLE | 余额不足  
LIQUIDATE_IMMEDIATELY | 操作可能导致爆仓  
LEVERAGE_TOO_HIGH | 杠杆倍数设置过高  
LEVERAGE_TOO_LOW | 杠杆倍数设置过低  
ORDER_NOT_FOUND | 委托不存在  
ORDER_NOT_OWNED | 委托不存在  
ORDER_FINISHED | 委托已结束  
TOO_MANY_ORDERS | 过多未完成的委托  
POSITION_CROSS_MARGIN | 全仓不支持更新保证金  
POSITION_IN_LIQUIDATION | 仓位在强制平仓中  
POSITION_IN_CLOSE | 仓位正在平仓中  
POSITION_EMPTY | 仓位为空  
REMOVE_TOO_MUCH | 保证金超过可调范围  
RISK_LIMIT_NOT_MULTIPLE | 风险限额未按照步长调整  
RISK_LIMIT_TOO_HIGH | 超出最大风险限额  
RISK_LIMIT_TOO_lOW | 风险限额设置过低  
PRICE_TOO_DEVIATED | 下单价与标记价格相差过大  
SIZE_TOO_LARGE | 下单数量超过上限  
SIZE_TOO_SMALL | 下单数量不足下限  
PRICE_OVER_LIQUIDATION | 增加仓位时价格不能超过平仓价  
PRICE_OVER_BANKRUPT | 减少仓位时价格不能超过破产价  
ORDER_POC_IMMEDIATE | 被动委托会立即成交  
INCREASE_POSITION | 只减仓委托会增加仓位  
CONTRACT_IN_DELISTING | 当前合约市场处于下线过渡期，只允许创建只减仓委托或者平仓委托  
POSITION_NOT_FOUND | 仓位不存在  
POSITION_DUAL_MODE | 双向持仓模式不允许此操作  
ORDER_PENDING | 有委托存在则不允许此操作  
POSITION_HOLDING | 有持仓则不允许此操作  
REDUCE_EXCEEDED | 双向持仓模式下，减仓单超过仓位大小  
NO_CHANGE | 没有改变发生  
AMEND_WITH_STOP | 有止盈止损单时不能修改委托  
ORDER_FOK | FOK 订单无法全部成交  
  
  * 抵押借币相关

异常 label 列表`label` | 含义  
---|---  
COL_NOT_ENOUGH | 质押物余额不足  
COL_TOO_MUCH | 超过质押币种质押额度  
INIT_LTV_TOO_HIGH | 初始质押率过高  
REDEEMED_LTV_TOO_HIGH | 提取后质押率过高  
BORROWABLE_NOT_ENOUGH | 剩余可借余额不足  
ORDER_TOO_MANY_TOTAL | 超过平台每天下单数量  
ORDER_TOO_MANY_DAILY | 超过单一用户每天下单数量  
ORDER_TOO_MANY_USER | 超过单一用户总下单数量  
ORDER_NOT_EXIST | 订单不存在  
ORDER_FINISHED | 订单已结束  
ORDER_NO_PAY | 订单待还金额为0  
ORDER_EXIST | 订单已存在  
ORDER_HISTORY_EXIST | 订单历史记录已存在  
ORDER_REPAYING | 订单已在还款中  
ORDER_LIQUIDATING | 订单已在平仓中  
BORROW_TOO_LITTLE | 小于币种最小可借  
BORROW_TOO_LARGE | 借款金额超过最大剩余可借  
REPAY_AMOUNT_INVALID | 还款金额无效  
REPAY_GREATER_THAN_AVAILABLE | 还款数额大于剩余可用  
POOL_BALANCE_NOT_ENOUGH | 资金池余额不足  
CURRENCY_SETTLING | 币种结算中，不允许还款  
RISK_REJECT | 风控检查中，请稍后再试  
LOAN_FAILED | 放款失败，可以再次发起借款  
  
  * 现货保证金相关

异常 label 列表`label` | 含义  
---|---  
USER_LIAB | 用户存在负债  
USER_PENDING_ORDERS | 用户存在挂单  
MODE_SET | 保证金模式已设置  
  
  * 理财相关

异常 label 列表`label` | 含义  
---|---  
ERR_BALANCE_NOT_ENOUGH | 余额不足  
ERR_PRODUCT_SELL_OUT | 项目售罄  
ERR_PRODUCT_BUY | 项目未开始  
ERR_CREATE_ORDER | 下单失败  
ERR_QUOTA_LOWER_LIMIT | 不满足最小下单金额  
ERR_QUOTA_SUPERIOR_LIMIT | 已达最大下单额度  
ERR_ORDER_NUMBER_LIMIT | 已达最大下单数量  
ERR_PRODUCT_CLOSE | 项目已结束  
COPIES_NOT_ENOUGH | 可申购仓位不足  
COPIES_TOO_SMALL | 投资份额不足  
COPIES_TOO_BIG | 投资份额超过最大购买限制  
TOTAL_AMOUNT_24 | 24小时内质押与赎回总量超限  
TOTAL_BUYCOUNT_24 | 24小时内质押与赎回次数超限  
REDEEM_24_LIMIT | 质押后24小时内不能赎回  
  
  * 服务异常

异常 label 列表`label` | 含义  
---|---  
INTERNAL | 内部错误  
SERVER_ERROR | 内部错误  
INTERNAL_SERVER_ERROR | 操作失败，请稍后重试（等同于 SERVER_ERROR）  
TOO_BUSY | 服务当前忙  
  
  * 闪兑相关

异常 label 列表`label` | 含义  
---|---  
INVALID_PARAM_VALUE | 参数不合法  
INVALID_CURRENCY | 不支持的币种  
INVALID_CURRENCY_PAIR | 无效交易对  
PRICE_OBSOLETE | 价格已失效/过期/作废  
ORDER_NOT_FOUND | 订单不存在  
ORDER_BOOK_NOT_FOUND | 订单簿不存在  
BALANCE_NOT_ENOUGH | 余额不足，划转失败  
TOO_MANY_REQUESTS | 请求过于频繁  
QUOTA_NOT_ENOUGH | 额度不足  
SERVER_TIMEOUT | 服务超时  
MISSING_REQUIRED_PARAM | 缺失必要参数  
REQUEST_FORBIDDEN | 资管账户访问限制  
CONVERT_PREVIEW_EXPIRED | 预览缓存过期  
CONVERT_PREVIEW_NOT_MATCH | 预览数据不一致  
AMOUNT_TOO_LITTLE | 金额太小  
AMOUNT_TOO_MUCH | 金额太大  
  
#  认证

##  生成 API key

在调用私有API接口前，需要生成账户的API key来验证身份。 您可以在网页端登录成功后，在【账户管理】-> 【APIv4 Keys】中生成， 或点击 [这里](/myaccount/apiv4keys) 生成 API keys

每个账户最多可以创建 20 个 API key，每个 Key 的权限配置都是相互独立的。 建议给每个 Key 设置能够标明用途的备注名

**`Key`** 访问密钥  
**`Secret Key`** 签名认证加密所使用的密钥

除此之外，还可以配置 IP 白名单，只允许服务端接收来自 IP 白名单里的客户端请求。每个 Key 最多可配置 20 个 IP 地址，IP 地址按照 IPv4 配置， 不支持 IP 地址段。若不设置 IP 白名单，服务端不会验证客户端 IP 来源。

TIP

注：如果发现 Key 的名字是 `spot` 或者 `futures` ，该 Key 很有可能是迁移之后系统的默认命名， 详情参考 “关于 APIv4 Key 升级” 一节。

创建的 Key 还可以更新和删除，不过需要注意的是 Key 的更新和删除，最多需要 5 分钟才能生效。

另外模拟合约与实盘合约属于两套不同的环境，实盘合约的 API Key 不可用于模拟合约。 如果需要使用模拟合约做 API 接口联调测试，需要在个人账户 APIv4Keys 页面的模拟合约入口单独申请。 模拟合约与实盘合约的接口请求方式完全相同，区别只是在 API 的 Base URL 和使用的 API Key

##  APIv4 权限

创建 Key 的时候，可以为该 Key 配置是否开启现货杠杆、合约、钱包或者提现的权限， 开启的权限可以配置读写或者只读。

APIv4 权限产品 | 权限  
---|---  
`现货/杠杆` | `只读`查询订单 `读写`查询订单&下单  
`永续合约` | `只读`查询订单 `读写`查询订单&下单  
`交割合约` | `只读`查询订单 `读写`查询订单&下单  
`钱包` | `只读`查询充提划转记录 `读写` 查询账户记录&资金划转  
`提现` | `只读`查询提现记录 `读写` 查询提现记录&提现  
  
所有请求方法为 `GET` 的都是读操作，其他的则是写请求。每个权限组可以设置为禁用、只读或读写。

值得注意的一点是，尽管提现操作组只有一个 API （即 `POST /withdrawals` ），考虑到一般使用情况， 还是将其从钱包操作里独立成一个权限组，而包括了提现记录的账户转出流水记录查询（即 `GET /wallet/withdrawals` ）还是保留在钱包 API 权限组了。

##  APIv4 验签请求接口发送要求

  1. 在官网个人中心申请 APIv4 Key ，并确保该 Key 拥有对应操作的读写权限。
  2. 在发送请求头部传入 `KEY` ，即 APIv4 密钥对的 Key
  3. 在发送请求头部传入 `Timestamp` ，即请求发送的时间，格式是秒级精度的 Unix 时间戳。 同时该时间不能与当前时间差距超过 60 秒。
  4. 在发送请求头部传入 `SIGN` ，即将请求生成签名字符串并用 APIv4 Secret 加密后生成的签名。 签名字符串生成方法参看下节，加密算法为 `HexEncode(HMAC_SHA512(secret, signature_string))` ， 即通过 HMAC-SHA512 加密算法，将 APIv4 Secret 作为加密密钥，签名字符串作为加密消息， 生成加密结果的 16 进制输出。
  5. 确保发送请求的客户端 IP 地址在所使用的密钥的 IP 地址白名单里。

##  APIv4 签名字符串生成方式

APIv4 中签名字符串按照如下方式拼接生成：

`Request Method + "\n" + Request URL + "\n" + Query String + "\n" + HexEncode(SHA512(Request Payload)) + "\n" + Timestamp`

###  Request Method

请求方法，全大写, 如 `POST`, `GET`

###  Request URL

请求 URL，不包括服务地址和端口，如 `/api/v4/futures/orders`

###  Query String

_没有_ 使用 URL 编码的请求参数，请求参数在参与计算签名时的顺序一定要保证和实际请求里的顺序一致。 如 `status=finished&limit=50` 。

如果没有请求参数，使用空字符串 ("")

###  HexEncode(SHA512(Request Payload))

将请求体字符串使用 SHA512 哈希之后的结果。如果没有请求体，使用空字符串的哈希结果，即 `cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e`

###  Timestamp

设置在请求头部 `Timestamp` 里的值

示例

注：示例中所有的换行都是为了方便显示人为添加的，实际只有示例中的一个 `\n` 保留

假设使用的 Key 为 `key` ，Secret 为 `secret`

  1. 查询所有合约订单

    
    
    	GET /api/v4/futures/orders?contract=BTC_USD&status=finished&limit=50 HTTP/1.1
    

签名字符串:
    
    
    	GET\n
    	/api/v4/futures/orders\n
    	contract=BTC_USD&status=finished&limit=50\n
    	cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e\n
    	1541993715
    

说明

  * `/api/v4/futures/orders`: 请求 URL
  * `contract=BTC_USD&status=finished&limit=50`: 请求参数，与实际请求的顺序完全一致
  * 请求体为空，使用空字符串的哈希输出
  * `1541993715`: Unix 时间戳

签名结果

`55f84ea195d6fe57ce62464daaa7c3c02fa9d1dde954e4c898289c9a2407a3d6fb3faf24deff16790d726b66ac9f74526668b13bd01029199cc4fcc522418b8a`

  2. 创建合约委托

    
    
    	POST /api/v4/futures/orders HTTP/1.1
    
    	{"contract":"BTC_USD","type":"limit","size":100,"price":6800,"time_in_force":"gtc"}
    

签名字符串:
    
    
    	POST\n
    	/api/v4/futures/orders\n
    	\n
    	ad3c169203dc3026558f01b4df307641fa1fa361f086b2306658886d5708767b1854797c68d9e62fef2f991645aa82673622ebf417e091d0bd22bafe5d956cca\n
    	1541993715
    

说明

  * 请求参数为空，使用空字符串
  * 使用 JSON 序列化之后的字符串的哈希输出

签名结果

`eae42da914a590ddf727473aff25fc87d50b64783941061f47a3fdb92742541fc4c2c14017581b4199a1418d54471c269c03a38d788d802e2c306c37636389f0`
    
    
    # coding: utf-8
    
    # Python 示例验签代码
    
    """
    本示例仅作为演示签名计算方式使用，推荐使用各语言的 SDK ，因为已经集成了验签规则
    """
    
    # coding: utf-8
    import time
    import hashlib
    import hmac
    import requests
    import json
    
    def gen_sign(method, url, query_string=None, payload_string=None):
        key = ''        # api_key
        secret = ''     # api_secret
    
        t = time.time()
        m = hashlib.sha512()
        m.update((payload_string or "").encode('utf-8'))
        hashed_payload = m.hexdigest()
        s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
        sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}
    
    if __name__ == "__main__":
        host = "https://api.gateio.ws"
        prefix = "/api/v4"
        common_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
        url = '/futures/orders'
        body = {"contract": "BTC_USD", "size": 100, "price": "30", "tif": "gtc"}
        request_content = json.dumps(body)
        sign_headers = gen_sign('POST', prefix + url, "", request_content)
        sign_headers.update(common_headers)
        print('signature headers: %s' % sign_headers)
        res = requests.post(host + prefix + url, headers=sign_headers, data=request_content)
        print(res.status_code)
        print(res.content)
    

#  常见问题

  * `POST /wallet/transfers` 的操作记录怎么查询？

通过 `POST /wallet/transfers` 执行的转账操作，按不同的账户类型，查询入口分在不同的服务地址，包括：

    * `GET /margin/account_book` 查询杠杆账户的转入转入历史
    * `GET /futures/{settle}/account_book?type=dnw` 查询永续合约账户的转入转出历史
    * `GET /delivery/{settle}/account_book?type=dnw` 查询交割合约账户的转入转出历史
  * 杠杆下单怎么操作？

杠杆下单复用了现货下单接口，只需要在 `POST /spot/orders` 或 `POST /spot/batch_orders` 时将请求体里的 `account` 参数设置为 `margin` 即可

  * 合约操作返回 `USER_NOT_FOUND`

原因是因为合约账户没有开户，只需要执行一笔账户划转操作即可。注意不同结算币种有不同的合约账户

  * 合约提示 `CONTRACT_NOT_FOUND`

不同结算币种的合约也是不同的，请确认指定的合约名称是否在对应结算币种支持的合约列表中。即

`GET /futures/{settle}/contracts` 和 `GET /delivery/{settle}/contracts`

  * 主子账号的区别

    * 子账号 API Key 不能操作主子账户互转API， 即 `POST /wallet/sub_account_transfers`
    * 子账号 API Key 不能使用API进行提现，即 `POST /withdrawals`
    * 如果创建子账号时没有开启对应业务的权限，即时子账号 API key 开启了权限，请求也一样会被拒绝
  * 上面没有我的问题

联系客服咨询具体问题。如果有使用到某一个语言的 SDK ，也可以在相应 SDK 的 github 项目中提交 issue

提交问题的时候，建议至少包含以下信息，可以更快速定位问题：

    * 用户 ID
    * 原始的请求 URL、请求参数和请求体内容 
      * 使用的 API Key 是实盘还是模拟的，具体的 Key 是什么（不需要提供 Secret）
      * 编程语言，最好提供一段发送请求的代码片段
      * 是否使用了 SDK ，如果使用了 SDK ，具体是调用哪个方法

Last Updated: 4/27/2026, 10:15:14 AM