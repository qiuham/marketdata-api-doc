---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en
api_type: REST
updated_at: 2026-05-27 20:14:38.372822
---

# Gate API v4.106.88

v4.106.88 · Stable


Welcome to Gate API APIv4 provides operations related to spot, margin, and contract trading, including public interfaces for querying market data and authenticated private interfaces for implementing API-based automated trading.

##  Access URL

**REST API BaseURL:**

  * Live trading: `https://api.gateio.ws/api/v4`
  * TestNet trading: `https://api-testnet.gateapi.io/api/v4`
  * Futures live trading alternative (futures only): `https://fx-api.gateio.ws/api/v4`

##  SDK

Available SDK:

[PyPython](https://github.com/gate/gateapi-python)[JavaJava](https://github.com/gate/gateapi-java)[PHPPHP](https://github.com/gate/gateapi-php)[GoGo](https://github.com/gate/gateapi-go)[C#C#](https://github.com/gate/gateapi-csharp)[NodeNodeJS](https://github.com/gate/gateapi-nodejs)[JSJavascript](https://github.com/gate/gateapi-js)

  * [Python ](https://github.com/gate/gateapi-python)
  * [Java ](https://github.com/gate/gateapi-java)
  * [PHP ](https://github.com/gate/gateapi-php)
  * [Go ](https://github.com/gate/gateapi-go)
  * [C# ](https://github.com/gate/gateapi-csharp)
  * [NodeJS ](https://github.com/gate/gateapi-nodejs)
  * [Javascript ](https://github.com/gate/gateapi-js)

Besides API examples, some SDK provides an additional demo application. The demo application is a relatively complete example demonstrating how to use the SDK. It can be built and run separately. Refer to corresponding repository for details.

  * [Python ](https://github.com/gate/gateapi-python/tree/master/example)
  * [Java ](https://github.com/gate/gateapi-java/tree/master/example)
  * [C# ](https://github.com/gate/gateapi-csharp/tree/master/example)
  * [Go ](https://github.com/gate/gateapi-go/tree/master/_example)

##  About APIv4 key improvement

Previously(before April 2020) futures APIv4 key are separated from spot one, but this is no longer the case anymore. You can create multiple keys with each key having multiple permissions now. e.g. you can create one key with spot read/write and futures read/write permission which can be used in both spot and futures trading.

History API keys will not be affected by this improvement. Previous spot key and futures key are now one key with only spot permissions enabled, another only futures permission enabled. You can reconfigure their permissions after migration.

##  Comparison with APIv2

APIv4 is a standalone brand-new HTTP REST API, currently used in parallel with APIv2. APIv4 provides complete trading operations, with more highly secured authentication method. What's more, APIv4 specification is written following [OpenAPI Specification ](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md). SDKs and documents are all generated from the same spec, which ensures consistency between documents and implementation.

The ways APIv4 and APIv2 differ are:

  1. Their API keys are separated from each other. Once logged into the web console, v2 API keys are generated on _"APIKeys"_ page, while v4 _"APIv4Keys"_ page.
  2. APIv2 supports only spot trading, while v4 supports all trading operations in spot, margin and futures.

Which one to choose:

  1. If margin or futures trading are needed, choose APIv4.
  2. If only spot trading or wallet operation is required, choose on your own.

##  Application for Marketers

In order to further improve the platform's opening depth and trading liquidity, we will recruit institutional market makers in an open and transparent way, and provide a professional market maker's service rate scheme for professional institutional market makers according to their contribution to the platform's liquidity.

  1. Provide Gate UID
  2. Provide other transaction volume screenshot or VIP level
  3. Brief introduction of market making method and scale

Provide the above content and submit to [mm@gate.com](mailto:mm@gate.com) , we will accept within 3 working days.

TIP

Vip11 and above need to open GT deduction in the personal center to enjoy the professional market rate.

##  Technical Support

If you have any questions or suggestions during the use, you can contact us in any of the following ways:

  * Submit Work Order Feedback
  * Online Work Order Feedback
  * Send your contact information and questions to [mm@gate.com](mailto:mm@gate.com) We will assign technical specialists to serve you.

If you encounter API errors, it is recommended that you sort out the following content, so that we can quickly analyze the problem for you:

  1. Problem Description
  2. Gate UID
  3. Request URI and parameters
  4. Error Code
  5. Responses

DANGER

Even if you submit a problem, you should not submit the API key information to customer service or others, otherwise there will be serious asset risk. If it has been accidentally leaked, please delete the existing API and rebuild it.

#  Changelog

**v4.106.88**

2026-05-26

  * Unified Account: Quick Repayment schemas now enforce required fields — `QuickRepaymentInfo` requires **`debt_currencies`** / **`available_currencies`** ; `QuickRepaymentResp` requires **`order_id`** / **`repaid_infos`** / **`used_infos`** ; `RepaidInfo` requires **`currency`** / **`repaid`** / **`left`** ; `UsedInfo` requires **`currency`** / **`used`**

**v4.106.87**

2026-05-21

  * CrossEx API: **`exchange_type`** / transfer account enums add **`KRAKEN`** and **`CROSSEX_KRAKEN`** — fee-rate example includes Kraken spot/futures tiers; **`CrossexOrder.symbol`** clarifies **`KRAKEN_FUTURE_*`** identifiers; docs note Kraken does not expose spot/margin-only order sides in this integration path alongside other venues

**v4.106.86**

2026-05-19

  * Add optional **`tpsl_tp_trigger_price`** / **`tpsl_sl_trigger_price`** (`string`) — take-profit / stop-loss trigger prices carried with futures orders for TP/SL placement workflows

**v4.106.85**

2026-05-19

  * Add optional query parameters **`page`** and **`page_size`** to **`GET /tradfi/positions/history`** (`queryPositionHistoryList`) for paginated historical positions
  * Update tradfi : response `data` includes **`total`** and **`total_page`**
  * Add optional request field **`action_mode`** (`string`) — processing mode controlling which order fields are returned on placement; values **`ACK`** (async, key fields only), **`RESULT`** (no clearing/liquidation details), **`FULL`** (default, complete payload)
  * Add optional query **`action_mode`** to **`DELETE /futures/{settle}/orders`** (`cancelFuturesOrders`) and **`DELETE /futures/{settle}/orders/{order_id}`** (`cancelFuturesOrder`) so cancel responses follow the same field-profile semantics as create

**v4.106.84**

2026-05-18

  * Add **`min_amount`** (`string`) — minimum investment amount for Dual Investment plans; public docs for plan listing now illustrate this field

**v4.106.83**

2026-05-18

  * **`PUT /futures/{settle}/price_orders/amend`** no longer takes `order_id` as a path parameter — specify the target auto-order ID in the JSON body via **`order_id`** (behavior is unchanged aside from dropping the obsolete path placeholder)
  * Futures : document **`pos_margin_mode`** as position margin mode with enum **`isolated`** / **`cross`** ; remove invalid enum placeholder text

**v4.106.82**

2026-05-14

  * Add Futures **Chase Limit Order** endpoints under `/futures/{settle}/autoorder/v1/chase/*`: 
    * **`POST /futures/{settle}/autoorder/v1/chase/create`** (`createChaseOrder`) — create a chase limit order with `contract`, `amount`, `price_limit` (or `offset_limit`), optional `reduce_only`, `text`, `is_dual_mode`, `price_type` / `price_gap_type` / `price_gap_value`, `pos_margin_mode`, `position_mode`
    * **`POST /futures/{settle}/autoorder/v1/chase/stop`** (`stopChaseOrder`) — stop a chase order by `id` or `text`
    * **`POST /futures/{settle}/autoorder/v1/chase/stop_all`** (`stopAllChaseOrders`) — stop chase orders in batch, optionally scoped by `contract` and `pos_margin_mode`
    * **`GET /futures/{settle}/autoorder/v1/chase/list`** (`getChaseOrders`) — list chase orders with filters `contract`, `is_finished`, `start_at` / `end_at`, `page_num` / `page_size`, required `sort_by` (1 `ORDER_SORT_CREATED_AT`, 2 `ORDER_SORT_FINISHED_AT`), `hide_cancel`, `reduce_only`, `side`
    * **`GET /futures/{settle}/autoorder/v1/chase/detail`** (`getChaseOrderDetail`) — get a chase order detail by `id`
  * Chase Limit Order REST reference adds structured request and response payloads named `CreateChaseOrderReq`, `CreateChaseOrderResp`, `StopChaseOrderReq`, `StopChaseOrderResp`, `StopAllChaseOrdersReq`, `StopAllChaseOrdersResp`, `GetChaseOrdersResp`, `GetChaseOrderDetailResp`, plus `ChaseOrder` items (fields such as `chase_price`, `interval_sec`, `suborder_*`, `price_type`, `price_gap_type`, `price_gap_value`, …)

**v4.106.81**

2026-05-13

  * Add `stop_profit` / `stop_loss` (objects typed in docs as `SpotOrderTPSL` / `PatchSpotOrderTPSL`) to **single spot order** , **spot order amendment** , **batch spot order** , and **batch spot amend-item** payloads — limit-order take-profit / stop-loss: each carries `trigger_price` and `order_price`; pass `{}` to cancel the TP/SL, pass `null` to leave it unchanged. Samples in Spot documentation were refreshed accordingly

**v4.106.80**

2026-05-10

  * Add optional query parameter `attributes` on **`GET /crossex/history_orders`** (`listCrossexHistoryOrders`) — comma-separated order attribute filters (`COMMON`, `LIQ`, `REDUCE`, `ADL`, `SETTLEMENT`)
  * Clarify several query parameter descriptions (`coin`, `symbol`, etc.); document **`SETTLEMENT`** in `CrossexOrder.attribute` description; align `CrossexTransferRecord.to_account_type` with `description` (was `title`); narrow `exchange_type` description text to **BINANCE / OKX / GATE / BYBIT** (verify runtime values against product/backend)

**v4.106.78**

2026-05-04

  * Simplify the `GET /crossex/coin_discount_rate` (`listCrossexCoinDiscountRate`) summary to "Query Currency Discount Rate" — drop the "(isolated exchange mode, discount rate of margin currency)" parenthetical from the title

**v4.106.75**

2026-04-28

  * Refresh examples with sanitized demo data (merchant/counterparty flows, payment methods including SWIFT); align sample field names (`seller_realname`, `currency_type`, etc.) with documented schemas; streamline lengthy legacy example blocks
  * Quant/grid: constrain strategy-preview extra fields so values are documented as string maps; represent strategy-detail `base_info`, `metrics`, and `position` snapshots as loose string-key maps instead of legacy AI-hub portfolio sub-shapes (`AIHubPortfolioBaseInfo`, `AIHubPortfolioMetrics`, `AIHubPortfolioPosition` are retired from published models)
  * English descriptions for leverage-map responses; remove `statement_type` query parameter from the ledger-style list endpoint; rename response field `statement_type` to `type` and adjust its description; shorten `CrossexSymbol` / exchange / business / state field descriptions
  * English description for `page` on `GET /wallet/withdraw_status` (“Page number”)

**v4.106.73**

2026-04-27

  * **`Contract`** model: add `enable_circuit_breaker` — whether a newly listed contract uses the mark price circuit breaker (platform may announce when enabling this for a market to reduce extreme post-listing volatility and liquidations)
  * **`ContractStat`** model: add `long_liq_usd_new` and `short_liq_usd_new` (quote-currency liquidation notionals for USDT-settled contracts using `long_liq_size` / `short_liq_size`, `multiplier`, and `mark_price`); add `top_long_size`, `top_short_size`, `long_taker_size`, `short_taker_size`, `top_long_account`, `top_short_account`, `long_users`, and `short_users` for large-holder and taker / user-count statistics

**v4.106.72**

2026-04-27

  * Documentation site: tag-split layout so each API tag page shows only that tag’s endpoints and related schemas—global sections (changelog overview, REST guide, authentication, FAQ, errors) are no longer duplicated on every tag landing page; TradFi endpoints are grouped under a **TradFi** heading in navigation

**v4.106.71**

2026-04-27

###  Unified account — quick repayment (new endpoints)

  * **New`GET /unified/estimated_quick_repayment`** (`getEstimatedQuickRepayment`) — returns estimated quick repayment data (per-currency liabilities, balances available to repay, etc.).
  * **New`POST /unified/quick_repayment`** (`createQuickRepayment`) — executes quick repayment; request body uses string arrays `debt_currencies` and `available_currencies`. Both endpoints apply only to unified accounts in **cross-currency margin** or **portfolio margin** mode.
  * Quick repayment requests and responses are documented with named payload blocks `QuickEstimatedRepayment`, `QuickRepaymentInfo`, `QuickRepaymentResp`; list sections use wrappers `UnifiedDebtCurrencies`, `UnifiedAvailableCurrencies`, `RepaidInfo`, `UsedInfo` whose items appear as `UnifiedQuickRepayDebtItem`, `UnifiedQuickRepayAvailableItem`, `UnifiedQuickRepayRepaidInfo`, `UnifiedQuickRepayUsedInfo`. Examples for unified quick repayment were refreshed.
  * Both endpoints document typical **`400`** / **`401`** / **`403`** error responses following the standard Gate error envelope (`label` / `message`).
  * Copy fix: Chinese scope text no longer repeats the extra 「模式」 fragment; it now consistently reads **跨币种保证金模式与组合保证金模式** (cross-currency margin mode **and** portfolio margin mode).

###  Other changes

  * English description for the `page` query parameter on the sub-account balance listing endpoint
  * Remove internal `contract` from `FuturesOrderAmendment` and simplify the amend-order request example
  * Refresh summaries/examples; align example fields (`tif`, `fee_currency`, `avg_price`, etc.); for the account-book style list, drop the `statement_type` query parameter and rename the response field to `type`, plus related example/copy updates
  * Quant/grid strategy schema and field documentation adjustments
  * P2P merchant API path and schema updates

**v4.106.70**

2026-04-21

  * Documentation: add internal sub-account transfer biz IDs `150215`, `150216`, `150217`, `150218`, `150219` (Subaccount Transfer) to the BizType reference list
  * Asset swap: **`GET /asset-swap/config`** and **`GET /asset-swap/orders/v1/{id}`** now document their `data` payload through response envelopes `ConfigResp` and `OrderQueryV1Resp` respectively
  * Relax `additionalProperties` from forced `type: string` to free-form (`{}`); previously generated `Map<String, String>` will become `Map<String, Object>` in strongly-typed SDKs

**v4.106.61**

2026-04-13

  * Update `SubAccountBalance` model: add `locking` field (locked amount by currency)
  * Document `id_string` on `FuturesPriceTriggeredOrder` and `TriggerOrderResponse`: string form of the same auto order as numeric `id` (decimal string, int64-safe in JS); prefer for display or string keys; aligns with `futures.orders` / `futures.autoorders` payloads. Applies to futures price-trigger REST under `/futures/{settle}/price_orders` (create, list, batch cancel, get, cancel, amend).
  * Update `PartnerCommission` and `AgencyCommission` list items in `PartnerCommissionHistory` / `AgencyCommissionHistory`: clarify `commission_amount` and `commission_asset` descriptions as rebate commission (not generic transaction amount)
  * Document `Contract` model: add `interest_rate` (string ratio) for `GET /futures/{settle}/contracts` and `GET /futures/{settle}/contracts/{contract}` responses
  * Documentation: rebrand the Agent developer guide from **Gate for AI** to **Gate for AI Agent** (page titles, body text, sidebar labels); update product homepage and Help Center links to `gate-for-ai-agent` paths

**v4.106.60**

2026-04-13

  * Documentation i18n: add English translations for dual-currency Earn API descriptions and query parameters
  * MCP interface mapping: add `GET /earn/dual/project-recommend` (`getDualProjectRecommend`)

**v4.106.59**

2026-04-10

  * Add `GET /earn/dual/order-refund-preview` (`getDualOrderRefundPreview`) — dual-currency early redemption preview
  * Add `POST /earn/dual/order-refund` (`placeDualOrderRefund`) — dual-currency order early redemption
  * Add `POST /earn/dual/modify-order-reinvest` (`modifyDualOrderReinvest`) — update dual-currency order reinvest settings
  * Add `GET /earn/dual/project-recommend` (`getDualProjectRecommend`) — dual-currency recommended projects
  * Update `GET /earn/dual/investment_plan`: add optional query parameters `coin`, `type`, `quote_currency`, `sort`, `page`, `page_size`
  * Update `GET /earn/dual/orders`: add optional query parameters `type`, `status`, `coin`
  * Add models `DualOrderRefundPreview`, `DualOrderRefundParams`, `DualModifyOrderReinvestParams`, `DualProjectRecommend` and related examples under Earn dual-currency APIs

**v4.106.58**

2026-04-03

  * Update `Contract` model: add `contract_type` field — contract classification type (e.g. stocks, metals, indices, forex, commodities)
  * Update `GET /wallet/sub_account_balances` endpoint: add `page` and `limit` query parameters for pagination support

**v4.106.57**

2026-04-01

  * Update `WithdrawalRecord` model: clarify the final-state time field — when `status` is `DONE`, it represents withdrawal success time (no longer tied to `block_number > 0`)
  * Update `WithdrawalRecord` and `WithdrawalsDel` models: simplify `DONE` status enum description (remove the note that completion required `block_number > 0` for on-chain confirmation)
  * Update `GET /crossex/rule/risk_limits` response: `CrossexRiskLimitTier` adds required string field `quick_cal_amount` (quick-calculation amount per risk tier)

**v4.106.56**

2026-03-31

  * Documentation i18n: fix English `messages.po` duplicate entries and a corrupted `msgid`; clear English `msgstr` for two oversized coupon-center Markdown blocks where JSON literals (`%`) caused gettext placeholder mismatch (full English translation to follow)

**v4.106.55**

2026-03-30

  * Add `GET /api/v4/rebate/partner/data/aggregated` endpoint (`getPartnerAgentDataAggregated`) — aggregated partner agent statistics (rebate amount, volume, net fee, customer count, optional trading user count by business type)
  * Add `PartnerDataAggregated` and `PartnerDataAggregatedResponse` model definitions for the aggregated rebate API

**v4.106.54**

2026-03-20

  * Add `POST /api/v4/earn/autoinvest/plans/create` endpoint - Create auto invest plan
  * Add `POST /api/v4/earn/autoinvest/plans/update` endpoint - Update auto invest plan
  * Add `POST /api/v4/earn/autoinvest/plans/stop` endpoint - Stop auto invest plan
  * Add `POST /api/v4/earn/autoinvest/plans/add_position` endpoint - Add position immediately
  * Add `GET /api/v4/earn/autoinvest/coins` endpoint - List currencies supporting auto invest
  * Add `POST /api/v4/earn/autoinvest/min_invest_amount` endpoint - Get minimum investment amount
  * Add `GET /api/v4/earn/autoinvest/plans/records` endpoint - List plan execution records
  * Add `GET /api/v4/earn/autoinvest/orders` endpoint - List plan execution record details (order details)
  * Add `GET /api/v4/earn/autoinvest/config` endpoint - List investment currency configuration
  * Add `GET /api/v4/earn/autoinvest/plans/detail` endpoint - Get auto invest plan details
  * Add `GET /api/v4/earn/autoinvest/plans/list_info` endpoint - List auto invest plans

**v4.106.52**

2026-03-29

  * Update `FuturesInitialOrder` model: add optional `amount` field (string) for decimal contract size; when both `size` and `amount` are provided, `amount` takes precedence
  * Update `FuturesUpdatePriceTriggeredOrder` model: add optional `amount` field (string) with the same semantics as `size`
  * Update `SpotPricePutOrder` model: add `time_in_force` to required fields

**v4.106.51**

2026-03-27

  * Add **Gate for AI Developer Guide** menu to documentation site: comprehensive guide for integrating AI Agents with Gate API through MCP (Model Context Protocol) and CLI tools
  * Documentation includes: MCP service endpoints, AI Skills (40+ pre-built workflows), access methods (Cursor, Claude, CLI), authentication, and code examples

**v4.106.50**

2026-03-26

  * Remove Earn ETH2 staking endpoints: `POST /earn/staking/eth2/swap` (swapETH2), `GET /earn/staking/eth2/rate_records` (rateListETH2)
  * Remove Earn structured product endpoints: `GET /earn/structured/products` (listStructuredProducts), `GET /earn/structured/orders` (listStructuredOrders), `POST /earn/structured/orders` (placeStructuredOrder)
  * Remove Earn illustrative payloads tied to those features from the REST reference

**v4.106.49**

2026-03-25

  * Add `FuturesOrderTimerange` model; `GET /futures/{settle}/orders_timerange` response items now reference `FuturesOrderTimerange` instead of `FuturesOrder`
  * Update `FuturesOrder` model: `order_value` and `trade_value` are documented as read-only values that lightweight SDK builds omit by default from generated clients
  * Update `GET /futures/{settle}/orders/{order_id}`: clarify path parameter description for querying by order ID vs custom `text` field

**v4.106.48**

2026-03-25

  * Update `Currency` model: add `category` field (array of strings for currency categories such as stocks, metals, indices, forex, commodities)

**v4.106.44**

2026-03-19

  * Update `BatchOrder` model: clarify `finish_as` field `ioc` and `poc` enum descriptions to accurately reflect order cancellation reasons based on time-in-force settings
  * Update `Order` model: clarify `finish_as` field `ioc` and `poc` enum descriptions to accurately reflect order cancellation reasons based on time-in-force settings
  * Update `UnifiedAccount` model: add `mode` field (account mode: classic/multi_currency/portfolio/single_currency)
  * Update `UnifiedAccount` model: add `balance_version` field (balance version number)
  * Update `UnifiedAccount` model: refine field descriptions for `available`, `freeze`, `equity`, `iso_balance` and other margin-related fields
  * Update `UidPushWithdrawalResp` model: change `id` field type from `integer` (int64) to `string`
  * Update CrossEx API `GET /crossex/fee` endpoint: restructure response to array format to support multiple exchanges (BINANCE, OKX, GATE, BYBIT), add `exchange_type` field to identify exchange type
  * Update CrossEx API `POST /crossex/convert` endpoint: add `order_id` (order ID) and `text` (order ID text) fields to response
  * Update CrossEx API interest type description: add `PERIODIC_ISOLATED` enum value (hourly debt interest) to `interest_type` field

**v4.106.44**

2026-03-20

  * Update TradFi API: `GET /tradfi/symbols/detail` (querySymbolDetail) now requires authentication

**v4.106.43**

2026-03-19

  * Add Earn Fixed-Term API: `GET /earn/fixed-term/product` (listEarnFixedTermProducts), `GET /earn/fixed-term/product/{asset}/list` (listEarnFixedTermProductsByAsset), `POST /earn/fixed-term/user/lend` (createEarnFixedTermLend), `GET /earn/fixed-term/user/lend` (listEarnFixedTermLends), `POST /earn/fixed-term/user/pre-redeem` (createEarnFixedTermPreRedeem), `GET /earn/fixed-term/user/history` (listEarnFixedTermHistory)
  * Update `FuturesUpdatePriceTriggeredOrder` model: add `format: int64` to `order_id` field
  * Futures auto-order (price-triggered order) endpoints: documented response order IDs now declare **`format: int64`** ; shared query parameters **`pos_margin_mode`** and **`dual_side`** are documented as **required** where referenced

**v4.106.42**

2026-03-19

  * Update `UnifiedAccount` model: add `mode` field (account mode: classic/multi_currency/portfolio/single_currency)
  * Update `UnifiedAccount` model: add `balance_version` field (balance version number)
  * Update `UnifiedAccount` model: refine field descriptions for `available`, `freeze`, `equity`, `iso_balance` and other margin-related fields

**v4.106.38**

2026-03-14

  * Update `amendOptionsOrder` request body: add required `contract` field (options contract name)

**v4.106.36**

2026-03-13

  * Add `PUT /options/orders/{order_id}` endpoint (amendOptionsOrder) for options order amendment
  * Update TradFi API: `GET /tradfi/users/mt5-account` now requires authenticated calls (anonymous access disabled)

**v4.106.34**

2026-03-12

  * Update Alpha API `/alpha/orders` list orders endpoint: change `currency`, `side`, `status` parameters from required to optional
  * Add BYBIT exchange support for CrossEx API

**v4.106.33**

2026-03-10

  * Update `BrokerCommission` and `BrokerTransaction` models: add `TradFi` to `source` field (rebate transaction types: Spot, Futures, Options, Alpha, TradFi)

**v4.106.32**

2026-03-05

  * Update P2P Merchant API: change request content type from `multipart/form-data` to `application/json`, reorganize merchant request bodies as structured JSON in the REST reference (no multipart attachments)
  * Update P2P Merchant API: Merchant endpoints inherit the standard Gate REST signing flow (`KEY`/`SIGN`), removing their previous standalone anonymous entry points
  * Update P2P Merchant API: change `complete_rate_month`, `orders_buy_rate_month`, `transactions_month`, `transactions_all` field types from `integer` to `number`

**v4.106.31**

2026-03-03

  * Update `PUT /futures/{settle}/price_orders/{order_id}` endpoint: move to new path `PUT /futures/{settle}/price_orders/amend/{order_id}`
  * Update `FuturesUpdatePriceTriggeredOrder` model: change `order_id` field type from `string` to `integer`
  * Update `BatchOrder` model: add new `finish_as` enum values: `liquidate_cancelled`, `small`, `depth_not_enough`, `trader_not_enough`, `poc`, `fok`, `price_protect_cancelled`, `unknown`
  * Update `Order` model: revise `cancelled_reason` field `ioc` enum description to clarify it also applies to `poc/rvt/rat/rpi` orders rejected as taker

**v4.106.30**

2026-03-03

  * Update `PUT /futures/{settle}/price_orders/{order_id}` endpoint: move to new path `PUT /futures/{settle}/price_orders/amend/{order_id}`
  * Update `FuturesUpdatePriceTriggeredOrder` model: change `order_id` field type from `string` to `integer`

**v4.106.29**

2026-03-02

  * Update CrossEx API: add `/crossex` prefix to all endpoint paths
  * Update `POST /crossex/orders` endpoint: add max pending order limit (1,000) to rate limit description
  * Update `GET /crossex/positions/leverage` response: change from array to map structure
  * Update `GET /crossex/margin_positions/leverage` response: change from array to map structure
  * Update `DELETE /position` to `POST /crossex/position` for close position operation
  * Update `POST /unified/portfolio_calculator` endpoint: revise description to reflect support for all underlying currencies with active options trading
  * Update `MockSpotBalance` model: remove currency restriction from `equity` field description
  * Update `MockSpotOrder` model: remove currency restriction from `count` field description
  * Update `MockFuturesPosition` and `MockFuturesOrder` models: update `contract` field description to support USDT perpetual contracts for all underlying currencies with active options trading
  * Update `MockOptionsPosition` and `MockOptionsOrder` models: update `options_name` field description to support all options contract markets

**v4.106.28**

2026-02-28

  * Update the translation content and optimize the TradFi document description.

**v4.106.27**

2026-02-26

  * Add Flash Convert related error codes documentation
  * Add `total_supply` and `market_cap` field descriptions for currency endpoints
  * Update `Contract` model: add `funding_impact_value` field (funding rate depth impact value)
  * Update `FuturesBBOOrder` model: remove `limit_vip` field

**v4.106.26**

2026-02-12

  * Add P2P Merchant API endpoints: `POST /p2p/merchant/books/ads_list` (get ads list)

**v4.106.25**

2026-02-11

  * Update `POST /earn/dual/orders`: document distinct request versus response payloads
  * Document dual-investment placement parameters separately from the placement response (`PlaceDualInvestmentOrderParams` vs richer response fields listed in `PlaceDualInvestmentOrder`)
  * **`GET /earn/dual/investment_plan`** : each plan row documents `per_value` as deprecated going forward

**v4.106.24**

2026-02-09

  * Add OTC API endpoints: `POST /otc/quote` (create quote for fiat and stablecoin), `POST /otc/order/create` (create fiat order), `POST /otc/stable_coin/order/create` (create stablecoin order), `GET /otc/get_user_def_bank` (get user default bank info), `GET /otc/bank_list` (get user bank card list), `POST /otc/order/paid` (mark fiat order as paid), `POST /otc/order/cancel` (cancel fiat order), `GET /otc/order/list` (list fiat orders), `GET /otc/stable_coin/order/list` (list stablecoin orders), `GET /otc/order/detail` (get fiat order detail)

**v4.106.23**

2026-02-06

  * Update `OptionsOrder` model: large integer `id` values are modeled for JavaScript/TypeScript clients that need bigint-safe deserialization

**v4.106.22**

2026-02-03

  * Update `Order` model: add `price_protect_cancelled` status to indicate orders cancelled due to price protection

**v4.106.21**

2026-02-03

  * Update transfer-related `amount` field descriptions in sub-account transfers and transfer records

**v4.106.20**

2026-02-02

  * Add futures trailing order endpoints: `POST /futures/{settle}/autoorder/v1/trail/create`, `POST /futures/{settle}/autoorder/v1/trail/stop`, `POST /futures/{settle}/autoorder/v1/trail/stop_all`, `GET /futures/{settle}/autoorder/v1/trail/list`, `GET /futures/{settle}/autoorder/v1/trail/detail`, `POST /futures/{settle}/autoorder/v1/trail/update`, `GET /futures/{settle}/autoorder/v1/trail/change_log`
  * Add `TrailOrder` and `TrailChangeLog` models for trailing orders
  * Update `SwapCoin` model: change `side` type to integer (0-pledge, 1-redeem) and remove `pid` int32 format constraint
  * Add `BatchFundingRatesRequest` and `BatchFundingRatesResponse` models for batch funding rate queries
  * Add TradFi API endpoints: `POST /tradfi/users`, `GET /tradfi/users/assets`, `GET /tradfi/users/mt5-account`, `POST /tradfi/transactions`, `GET /tradfi/transactions` and 14 more
  * Update `FuturesAccount` model: remove `cross_settle` field
  * Update `TotalBalance` model: add new account types (`meme_box`, `options`, `payment`)
  * Update `UnifiedMarginTiers` model: fix description format

**v4.106.19**

2026-01-27

  * Update `Contract` model: add `enable_decimal` field to indicate whether the contract supports decimal string type contract size. When this field is `true`, the contract supports decimal contract size (i.e., the `size` field can use decimal string type); when it is `false`, the contract does not support decimal contract size (i.e., the `size` field can only use integer type)
  * Add TradFi menu and sidebar in documentation
  * Add comprehensive TradFi API endpoints for MT5-based forex and CFD trading, including user management, asset queries, order management, position management, and market data queries
  * Support TradFi REST API references in documentation navigation

**v4.106.18**

2026-01-26

  * Update API documentation: add spot rate limit rules section, including existing rate limit rules, new rate limit rules, and fill ratio calculation formula
  * Add P2P Merchant API endpoints: `POST /p2p/merchant/account/get_user_info` (get account information), `POST /p2p/merchant/account/get_counterparty_user_info` (get counterparty information), `POST /p2p/merchant/account/get_myself_payment` (get payment methods list), `POST /p2p/merchant/transaction/get_pending_transaction_list` (get pending orders), `POST /p2p/merchant/transaction/get_completed_transaction_list` (get completed/historical orders), `POST /p2p/merchant/transaction/get_transaction_details` (get order details), `POST /p2p/merchant/transaction/confirm-payment` (confirm payment), `POST /p2p/merchant/transaction/confirm-receipt` (confirm receipt), `POST /p2p/merchant/transaction/cancel` (cancel order), `POST /p2p/merchant/books/place_biz_push_order` (place ad order), `POST /p2p/merchant/books/ads_update_status` (update ad status), `POST /p2p/merchant/books/ads_detail` (get ad details), `POST /p2p/merchant/books/my_ads_list` (get my ads list), `POST /p2p/merchant/chat/get_chats_list` (get chat history), `POST /p2p/merchant/chat/send_chat_message` (send text message), `POST /p2p/merchant/chat/upload_chat_file` (upload chat file)

**v4.106.17**

2025-01-22

  * Update `GET /loan/multi_collateral/currency_quota` endpoint: add two new response fields in `CurrencyQuota` model - `left_quota_fixed` (remaining `borrow/collateral` limit for fixed-term currency) and `left_quote_usdt_fixed` (remaining currency limit converted to USDT for fixed-term currency)
  * Deprecated: Remove collateral-loan API endpoints (`/loan/collateral/**` ). These endpoints are no longer available.
  * Update `FuturesUpdatePriceTriggeredOrder` model: change `order_id` type to string, add `close` field
  * Update `SpotPriceTrigger` model: remove `expiration` from required fields

**v4.106.16**

2025-01-20

  * Update order status description: clarify the `closed` state as “Closed order” (rather than implying “fully filled”) for standard spot payloads (`BatchOrder`, `InternalOrder`, `Order`, `OrderCancel`) and portfolio-margin spot orders (`PortfolioSpotOrders`)

**v4.106.15**

  * Add crossex menu and Add sub menu websocket and rest page
  * Add comprehensive crossex API endpoints for cross-exchange trading, including order management, position management, account management, and historical data queries
  * Implement crossex WebSocket support for real-time market data and order updates

**v4.106.14**

  * Update `Order` model: add description in `text` field to clarify liquidation order scenarios (`pm_liquidate`, `comb_margin_liquidate`, `scm_liquidate` represent cross-margin liquidation orders, `liquidate` represents isolated margin liquidation orders)
  * Update `Trade` model: add description in `text` field to clarify liquidation order scenarios (`pm_liquidate`, `comb_margin_liquidate`, `scm_liquidate` represent cross-margin liquidation orders, `liquidate` represents isolated margin liquidation orders)

**v4.106.13**

  * Add OTC API endpoints: `POST /otc/quote` (create quote for fiat and stablecoin), `POST /otc/order/create` (create fiat order), `POST /otc/stable_coin/order/create` (create stablecoin order), `GET /otc/get_user_def_bank` (get user default bank info), `POST /otc/order/paid` (mark order as paid), `POST /otc/order/cancel` (cancel order), `GET /otc/order/list` (list fiat orders), `GET /otc/stable_coin/order/list` (list stablecoin orders), `GET /otc/order/detail` (get fiat order detail), `GET /otc/stable_coin/order/detail` (get stablecoin order detail), `GET /otc/get_api_order_uid` (get API order users)
  * OTC REST docs: standardize JSON-only request bodies (`application/json` replaces `multipart/form-data`), broaden success/error narratives, reinforce authenticated onboarding, clarify base URLs/signing conventions, and surface the OTC routes already listed above

**v4.106.12**

  * New feature `GET /earn/dual/balance` endpoint to query dual investment balance
  * New feature `GET /futures/{settle}/get_leverage/{contract}` endpoint to get leverage information for specified mode
  * New feature `POST /futures/{settle}/positions/{contract}/set_leverage` endpoint to update leverage for specified mode, simplifying the leverage interface logic
  * New feature `POST /futures/{settle}/set_position_mode` endpoint to set position mode, replacing the dual_mode interface
  * Update `POST /futures/{settle}/positions/{contract}/reverse` endpoint: add `pos_margin_mode` parameter (required for split position mode, values: isolated/cross)
  * Add `enable_dual_plus` field in `FuturesAccount` model to indicate whether split position mode is supported
  * Update `position_mode` field description in `FuturesAccount` model to clarify position modes: single (single position), dual (dual position), dual_plus (split position)
  * Add `pos_margin_mode` field in `FuturesOrder` model to indicate position margin mode (isolated - isolated margin, cross - cross margin, only passed in simple split mode)
  * Add `pos_margin_mode` field in `Position` model to indicate position margin mode (isolated - isolated margin, cross - cross margin)
  * Add `lever` field in `Position` model to indicate current position leverage, gradually replacing the current `leverage` and `cross_leverage_limit` fields
  * Add new `FuturesLeverage` model definition for leverage query response

**v4.106.11**

  * Update `slippage` field description in `BatchOrder`, `CurrencyPair`, and `Order` models to clarify it represents the maximum slippage ratio supported for spot market orders, calculated based on the latest market price at the time of order placement (example: 0.03 means 3%)
  * Update `POST /spot/batch_orders` endpoint: add response description indicating the response contains multiple order objects, with order object structure referencing the `/spot/orders` order placement endpoint

**v4.106.10**

  * Update `GET /account/rate_limit` endpoint: add description indicating the endpoint is not yet available for use
  * Update `GET /wallet/order_status` endpoint: update summary and description to clarify it's for querying master-sub account transfer status

**v4.106.9**

  * Update `PUT /futures/{settle}/price_orders/{order_id}` endpoint: fix request body model `FuturesUpdatePriceTriggeredOrder` field name from `contact` to `order_id`, and mark `order_id` as required field
  * Mark `POST /loan/collateral/orders` endpoint as deprecated/offline

**v4.106.8**

  * Add `market_order_slip_ratio` field in `Contract` model to indicate the maximum slippage ratio supported for market orders, with the slippage rate calculated based on the latest market price
  * Add `market_order_size_max` field in `Contract` model to indicate the maximum number of contracts supported for market orders, with a default value of 0. When the default value is used, the maximum number of contracts is limited by the `order_size_max` field
  * Add `market_order_slip_ratio` field in `FuturesOrder` model to indicate custom maximum slippage rate for market orders. If not provided, the default contract settings will be used
  * Add `market_order_slip_ratio` field in `BatchFuturesOrder` model to indicate the maximum slippage ratio returned in order response

**v4.106.7**

  * Update `GET /unified/batch_borrowable` endpoint: add `style: form` and `explode: false` to `currencies` parameter for proper array parameter formatting
  * Update `GET /unified/estimate_rate` endpoint: add `style: form` and `explode: false` to `currencies` parameter for proper array parameter formatting
  * Update `GET /loan/multi_collateral/current_rate` endpoint: add `style: form` and `explode: false` to `currencies` parameter for proper array parameter formatting
  * Update rate limit documentation: add rate limit specification for `POST /withdrawals/push` endpoint (1r/10s) in Wallet private endpoints section

**v4.106.6**

  * Update `GET /options/order_book` endpoint response model from `FuturesOrderBook` to `OptionsOrderBook` for better separation of Options and Futures APIs
  * Update `GET /options/trades` endpoint response model from `FuturesTrade` to `OptionsTrade` for better separation of Options and Futures APIs
  * Update `GET /options/candlesticks` endpoint response model from `FuturesCandlestick` to `OptionsCandlestick` for better separation of Options and Futures APIs
  * Add new `OptionsOrderBook` and `OptionsTrade` model definitions to provide dedicated models for Options API responses

**v4.106.5**

  * Add new AccountBook codes: `150102` (Currency Buyback-Debit), `150101` (Currency Buyback-Credit), `143` (Debit After Coin Name Change), `144` (Credit After Coin Name Change), `707` (Spot settlement in the same currency - transfer out), `708` (Spot settlement in the same currency - transfer in)

**v4.106.4**

  * Add `up_rate` and `down_rate` fields in `CurrencyPair` model to display maximum price increase and decrease percentages
  * Add `funding_rate_limit` field in `Contract` model to indicate funding rate cap value

**v4.106.3**

  * Update `GET /futures/{settle}/accounts` endpoint description to indicate support for querying both classic futures accounts and unified accounts
  * Update `PUT /futures/{settle}/accounts` endpoint: `enable_evolved_classic` field marked as deprecated
  * Update `GET /futures/{settle}/positions/{contract}` endpoint summary to clarify dual-position query method when holding both long and short positions in the same contract market
  * Update `POST /futures/{settle}/positions/{contract}/margin` endpoint summary with link to new risk limit rules, clarifying that leverage adjustment should be used instead of direct margin modification
  * Update `POST /futures/{settle}/positions/{contract}/leverage` endpoint: clarify `leverage` parameter (for isolated margin, requires `cross_leverage_limit` to be empty) and `cross_leverage_limit` parameter (for cross margin, requires `leverage` to be set to 0)
  * Update `POST /futures/{settle}/dual_comp/positions/{contract}/risk_limit` endpoint summary with link to risk limit rules
  * Update `GET /options/accounts` endpoint summary to indicate support for querying both classic options accounts and unified accounts
  * Update `Position` model field descriptions for better clarity on leverage and risk management: `leverage` (isolated margin leverage, 0 indicates cross margin mode), `leverage_max` (max leverage based on current position size), `maintenance_rate` (tiered maintenance margin rate calculation), `liq_price` (estimated liquidation price for reference only), `initial_margin` and `maintenance_margin` (expanded scope description), `realised_pnl` (detailed breakdown including settlement, funding fees, and trading fees), `pnl_pnl` (settlement P&L), `pnl_fund` (funding fee P&L), `pnl_fee` (total trading fees), `history_pnl` (all historical settlement P&L), and `cross_leverage_limit` (simplified description)
  * Update `FuturesAccount` and `DeliveryAccount` models: `total` field updated to indicate "only applicable to classic futures accounts", `position_margin` marked as deprecated, `order_margin` updated to "initial margin for all pending orders", `enable_evolved_classic` and `enable_new_dual_mode` marked as deprecated, `margin_mode` enum expanded to include value 3 for single-currency margin mode
  * Update `OptionsAccount` model: `total` and `equity` fields note added for unified account limitation, `liq_triggered` description updated to "whether account is in liquidation status", `margin_mode` enum expanded to include value 3, `unrealised_pnl` description enhanced with calculation formula
  * Update `MarginAccount` model: `account_type` description updated to remove "risk" option, `risk` field marked as deprecated, `mmr` description refined
  * Update `Contract` and `DeliveryContract` models: `quanto_multiplier` renamed conceptually to "contract multiplier", `maintenance_rate` clarified as "first-tier maintenance margin rate requirement", `mark_type` and `funding_cap_ratio` marked as deprecated, `mark_price_round` simplified to "minimum unit of mark price"
  * Update `OptionsContract` model: `tag` updated to "expiry period: day, week, month", `multiplier` updated to "option contract multiplier", `underlying_price` updated to "forward futures price for the delivery date", `mark_price_round` simplified, `order_price_deviate` and `trade_id` marked as deprecated, `orders_limit` refined to "maximum number of orders per user in this market"
  * Update `FuturesTicker` and `DeliveryTicker` models: `quanto_base_rate` field marked as deprecated
  * Update `OptionsTicker` model: `leverage` calculation formula updated with reference note
  * Update `FuturesTrade` and `DeliveryTrade` models: `is_internal` field marked as deprecated
  * Update `OptionsMyTrade` and `OptionsPosition` models: `underlying_price` field updated to "forward futures price for the delivery date"
  * Update `PositionTimerange` model: `leverage_max` and `maintenance_rate` descriptions refined
  * Update `FuturesAutoDeleverage` model: `leverage` and `cross_leverage_limit` descriptions clarified for better understanding of margin modes
  * Update risk limit tier models (`FuturesRiskLimitTier`, `FuturesLimitRiskTiers`, `DeliveryLimitRiskTiers`): standardize `maintenance_rate` description as "first-tier maintenance margin rate requirement"
  * Update `MarginLeverageTier` model: refine `upper_limit` (max borrowing limit based on leverage), `mmr` (maintenance margin rate as a comprehensive value under tiered requirements), and `leverage` (max leverage based on current debt size) descriptions
  * Update `CreateUniLoan` and `UniLoanInterestRecord` models: `type` field description updated to "lending type, margin indicates margin borrowing"

**v4.106.2**

  * New feature `GET /wallet/getLowCapExchangeList` endpoint to retrieve the list of low-liquidity or low-cap tokens

**v4.106.1**

  * Update `leverage` and `cross_leverage_limit` field descriptions in `Position` and `FuturesAutoDeleverage` models for better clarity on cross/isolated margin mode usage
  * Update `leverage` and `cross_leverage_limit` parameter descriptions in `POST /futures/{settle}/positions/{contract}/leverage` endpoint to clarify usage requirements
  * Update `PUT /sub_accounts/{user_id}/keys/{key}` endpoint summary to note that `mode` attribute cannot be modified via this endpoint

**v4.106.0**

  * To support decimal quantity orders, all size and quantity-related fields in Futures-related interfaces have been uniformly changed from `integer` type to `string` type. Affected models include: `FuturesOrder` (`size`, `iceberg`, `left`), `BatchFuturesOrder` (`size`, `iceberg`, `left`), `Position` (`size`, `trade_long_size`, `trade_short_size`), `PositionTimerange` (`size`), `MyFuturesTrade` (`size`, `close_size`), `MyFuturesTradeTimeRange` (`size`, `close_size`), `FuturesTrade` (`size`), `FuturesOrderBook` (`size` in `asks` and `bids`), `FuturesCandlestick` (`v`), `FuturesLiquidate` (`size`, `order_size`), `FuturesLiqOrder` (`position_size`, `size`, `order_size`), `FuturesAutoDeleverage` (`size`, `entry_size`), `FuturesCollusionOrder` (`size`, `left`), `FuturesBatchAmendOrderRequest` (`size`), `Contract` (`order_size_min`, `order_size_max`, `trade_size`, `position_size`), and `ContractStat` (`long_liq_size`, `short_liq_size`, `open_interest`)
  * Add `pid` field in `Position` model for sub-position ID
  * All language SDKs (Go, C#, Java, Python, PHP, TypeScript) uniformly add `X-Gate-Size-Decimal: 1` default request header to ensure the server correctly handles size fields
  * Created 12 independent Delivery Schema files to separate Delivery and Futures objects: `DeliveryAccount`, `DeliveryAccountBook`, `DeliveryOrder`, `DeliveryOrderBook`, `DeliveryPosition`, `DeliveryPositionClose`, `DeliveryTrade`, `DeliveryMyTrade`, `DeliveryLiquidate`, `DeliveryInsuranceRecord`, `DeliveryLimitRiskTiers`, `DeliveryCloseAllPositionsResponse`

**v4.105.32**

  * Update `POST /futures/{settle}/positions/{contract}/leverage` endpoint description with detailed position mode switching rules, usage examples, and risk warnings for better clarity

**v4.105.31**

  * Update `taker_fee` and `maker_fee` field descriptions in `TradeFee` model to specify they are for spot trading

**v4.105.29**

  * Add `deal` field in `GET /spot/my_trades` endpoint response to display total deal amount
  * Add `options_order_loss` field in `GET /unified/accounts` endpoint response to display options order loss in USDT, effective in portfolio margin mode
  * Update `spot_order_loss` field description in `GET /unified/accounts` endpoint response to clarify it represents spot order loss, effective in cross-currency margin mode and portfolio margin mode
  * Update `cross_balance` and `iso_balance` field descriptions in `GET /unified/accounts` endpoint response, now effective in both single-currency margin mode and cross-currency margin mode

**v4.105.28**

  * Add `block_number` field in `DELETE /withdrawals/{withdrawal_id}` endpoint response to display block number
  * Update `cross_balance` and `iso_balance` field descriptions in `GET /unified/accounts` endpoint response, now effective in both single-currency margin mode and cross-currency margin mode

**v4.105.27**

  * Update `status` field descriptions in `DepositRecord`, `WithdrawalRecord`, and `WithdrawalsDel` models for better clarity
  * Remove `FINAL` status from deposit status enum, optimize `DONE` status description

**v4.105.24**

  * `GET /wallet/currency_chains` endpoint description updated to indicate that currencies with extremely low liquidity or value are not supported via API and should be queried and processed through Web or App
  * `GET /wallet/withdraw_status` endpoint description updated to indicate that currencies with extremely low liquidity or value are not supported via API and should be queried and processed through Web or App

**v4.105.20**

  * `DELETE /withdrawals/{withdrawal_id}` endpoint response model updated to use `WithdrawalsDel` schema
  * Add `BLOCKED`, `DEP_CREDITED`, `FINAL` status values in `GET /wallet/deposits` endpoint response
  * Add `is_deposit_disabled` field in `GET /wallet/currency_chains` endpoint response

**v4.105.19**

  * `GET /spot/currency_pairs` and `GET /spot/currency_pairs/{currency_pair}` endpoints, `fee` field is now deprecated
  * `POST /earn/staking/eth2/swap` endpoint summary updated from "ETH2 Swap" to "ETH Swap", ETH2 renamed to GTETH
  * `GET /earn/staking/eth2/rate_records` endpoint summary updated to query historical rate of GTETH

**v4.105.18**

  * New feature `PUT /futures/{settle}/price_orders` endpoint to update a single price-triggered order
  * Add `settle`, `order_id`, `size`, `price`, `trigger_price`, `price_type`, and `auto_size` parameters in update price-triggered order request

**v4.105.11**

  * New feature `GET /account/main_keys` endpoint to query all main account API key information
  * `GET /spot/currency_pairs` and `GET /spot/currency_pairs/{currency_pair}` endpoints, `fee` field is now deprecated

**v4.105.10**

  * New feature `POST /futures/{settle}/bbo_orders` endpoint for BBO level-based futures orders
  * `POST /futures/{settle}/price_orders` endpoint, `price` and `rule` fields are now required in futures price trigger parameters

**v4.105.9**

  * Add `settlement_currency` field in `GET /futures/{settle}/positions` response for multi-settlement support
  * Add `auto_renew` parameter in `POST /earn/uni/lends` request for automatic lending renewal
  * Enhance `GET /spot/trades` endpoint with `trade_type` filter parameter

**v4.105.8**

  * Add `margin_mode` field in `GET /unified/accounts` response to indicate account margin mode
  * Add `fee_currency` field in `GET /spot/my_trades` response

**v4.105.7**

  * Add `liquidation_price` field in `GET /futures/{settle}/positions` response for better risk management
  * Enhance `POST /spot/orders` with `stop_loss` and `take_profit` parameters for advanced order types
  * Add `total_balance` field in `GET /unified/accounts` response

**v4.105.6**

  * New feature `GET /wallet/saved_address` endpoint to query saved withdrawal addresses
  * Add `network_fee` field in `GET /wallet/withdrawals` response
  * Add `min_amount` and `max_amount` fields in `GET /spot/currency_pairs` response

**v4.105.5**

  * Add `order_type` field in `GET /futures/{settle}/orders` response to distinguish order types
  * Enhance `GET /spot/candlesticks` with support for `30s` interval
  * Add `available_balance` field in `GET /margin/accounts` response

**v4.105.4**

  * Add `funding_rate_next` field in `GET /futures/{settle}/tickers` response
  * Add `cross_leverage` field in `GET /unified/accounts` response

**v4.105.3**

  * Add `position_side` parameter in `GET /futures/{settle}/positions` query for hedge mode support
  * Enhance `GET /earn/dual/orders` with `investment_type` filter parameter
  * Add `unrealized_pnl` field in `GET /futures/{settle}/accounts` response

**v4.105.2**

  * Add `maker_fee_rate` and `taker_fee_rate` fields in `GET /spot/fee` response
  * Add `settle_currency` field in `GET /futures/{settle}/contracts` response

**v4.105.1**

  * Add `time_in_force` parameter in `POST /futures/{settle}/orders` request
  * Enhance `GET /wallet/deposits` with `network` filter parameter

**v4.105.0**

  * Add `portfolio_margin` field in `GET /unified/accounts` response
  * Add `position_mode` parameter in `POST /futures/{settle}/positions/mode` request

**v4.104.9**

  * Add `reduce_only` parameter in `POST /futures/{settle}/orders` request for position reduction orders
  * Enhance `GET /spot/orders` with `account_type` filter parameter
  * Add `funding_balance` field in `GET /futures/{settle}/accounts` response

**v4.104.8**

  * Add `apr` field in `GET /earn/uni/currencies` response
  * Add `lock_period` field in `GET /earn/dual/investment_plan` response

**v4.104.7**

  * Add `order_book_id` field in `GET /spot/order_book` response for order book versioning
  * Enhance `POST /wallet/transfers` with `client_order_id` parameter
  * Add `trading_fee_rate` field in `GET /spot/accounts` response

**v4.104.6**

  * Add `mark_price` field in `GET /futures/{settle}/tickers` response
  * New feature `GET /futures/{settle}/insurance` endpoint for insurance fund information
  * Add `isolated_margin` field in `GET /futures/{settle}/positions` response

**v4.104.5**

  * Add `order_id` field in `GET /spot/my_trades` response for trade-order mapping
  * Enhance `GET /unified/loans` with `currency` filter parameter
  * Add `borrow_amount` field in `GET /unified/accounts` response

**v4.104.4**

  * Add `trigger_price` field in `GET /spot/price_orders` response
  * Add `maintenance_rate` field in `GET /futures/{settle}/contracts` response

**v4.104.3**

  * Add `hedge_mode` parameter in `GET /futures/{settle}/positions` query
  * Enhance `GET /earn/dual/orders` with `status` filter parameter
  * Add `cross_margin_leverage` field in `GET /unified/accounts` response

**v4.104.2**

  * Add `settlement_size` field in `GET /futures/{settle}/my_trades` response
  * New feature `GET /wallet/total_balance` endpoint for total account balance
  * Add `available_margin` field in `GET /margin/accounts` response

**v4.104.1**

  * Add `post_only` parameter in `POST /spot/orders` request for maker-only orders
  * Enhance `GET /futures/{settle}/orders` with `contract` filter parameter
  * Add `funding_time` field in `GET /futures/{settle}/funding_rate` response

**v4.104.0**

  * New feature `GET /unified/risk_units` endpoint for unified account risk unit calculation
  * Add `risk_level` field in `GET /unified/accounts` response
  * Add `auto_borrow` parameter in `POST /unified/orders` request for automatic borrowing

**v4.103.0**

  * Add `code` field in `GET /spot/account_book` query parameter and response to filter account book entries by specific code
  * Add `text` parameter to `closeAllPositions` operation for order remarks when closing all positions
  * New comprehensive AccountBook code documentation with detailed explanations for over 300 transaction codes

**v4.102.6**

  * Enhance staking swap response structure `SwapCoinStruct` with additional fields: `pid`, `subtype`, `exchange_amount`, `updateStamp`, `protocol_type`, `client_order_id`, `source`

**v4.102.0**

  * Add `is_all_collateral` field in `GET /unified/accounts` endpoint response to indicate if all currencies are used as collateral
  * Add `enabled_collateral` field in balances array of unified accounts to show currency collateral status
  * New feature `POST /unified/collateral_currencies` endpoint, Set collateral currencies for cross-currency margin mode

**v4.101.9**

  * New feature `GET /futures/{settle}/risk_limit_table` endpoint, Query risk limit tier table by table_id
  * Add `enable_tiered_mm` field in futures account model for tiered maintenance margin calculation
  * Add `risk_limit_table` and `average_maintenance_rate` fields in position model for enhanced risk management
  * Add `deduction` field in futures limit risk tiers for maintenance margin quick calculation
  * Introduce new models: `FuturesRiskLimitTier` and `FuturesRiskLimitTierList` for risk management
  * Enhance `POST /earn/staking/swap` endpoint response structure with improved swap order details

**v4.100.0**

  * Add alpha account query and account book query functionality
  * New feature `GET /earn/staking/coins` endpoint, Query on-chain staking coin types
  * New feature `POST /earn/staking/swap` endpoint, On-chain staking coin swap
  * Add `sub_broker_info` object field in broker commission and transaction APIs

**v4.99.0**

  * Add `refresh_time` field in `GET /spot/accounts` endpoint response
  * Remove the `PUT /earn/uni/interest_reinvest` endpoint

**v4.98.0**

  * New feature `/earn/uni/rate` endpoint, Currency estimate annualized interest rate
  * Add `delisting_time`, `trade_url` fields in `GET /spot/currency_pairs` and `GET /spot/currency_pairs/{currency_pair}` endpoints

**v4.97.0**

  * New feature `GET /unified/batch_borrowable` endpoint, Batch query unified account can be borrowed up to a maximum
  * `GET /spot/candlesticks` endpoint, `interval` supports `1s` granularity
  * New feature `GET /earn/uni/chart` endpoint, UniLoan currency annualized trend chart
  * New feature `POST /futures/{settle}/positions/cross_mode` endpoint, Switch to the full position-by-store mode

**v4.96.0**

  * Add `cross_margin_balance`,`cross_mmr`,`cross_imr` field in `GET /futures/{settle}/accounts` response

**v4.95.0**

  * Add `code` field in `GET /spot/account_book` query & response
  * New feature `GET /unified/transferables` endpoint, Batch query unified account can be transferred up to a maximum of
  * New feature `GET /margin/user/loan_margin_tiers` endpoint, Check the user's own leverage lending gradient in the current market
  * New feature `GET /margin/loan_margin_tiers` endpoint, Query the current market leverage lending gradient
  * New feature `POST /margin/leverage/user_market_setting` endpoint, Set the user market leverage multiple
  * New feature `GET /margin/user/account` endpoint, Query the user's leverage account list

**v4.94.0**

  * New feature `GET /unified/currencies` endpoint, List of loan currencies supported by unified account
  * Add `sub_uid` field in `GET /unified/accounts` query

**v4.93.0**

  * Add `plan_id` field in `GET /earn/dual/investment_plan` query
  * Add `from`, `to`, `page`, `limit` fields in `GET /earn/dual/orders` query
  * Add `text` field in `GET /earn/dual/orders` response
  * Add `text` field in `POST /earn/dual/orders` response
  * New feature `GET /earn/staking/eth2/rate_records` endpoint, Query historical rate of GTETH

**v4.92.0**

2025-02-24

  * Add `name` field in `GET /spot/currencies` query
  * Add `base_name`, `quote_name` fields in `GET /spot/currency_pairs` response
  * Add `unified` field in `GET /spot/price_orders` query
  * Add `sub_uid` field in `GET /unified/accounts` query

**v4.91.0**

2025-02-10

`2025-04-01` After that, we will remove the following interface, please migrate to the new interface as soon as possible

**v4.90.0**

2025-01-20

  * Add `transaction_type` field in `GET /wallet/push` query
  * New feature `GET /rebate/user/sub_relation` endpoint, Query whether the specified user is in the system
  * Add `order_size` field in`GET /futures/{settle}/liq_orders` response
  * Add `type` field in `GET /spot/currency_pairs` response

**v4.88.0**

2024-12-24

  * New feature `GET /spot/insurance_history` endpoint, Query spot insurance fund historical data
  * Add `cross_balance`、`iso_balance`、`im`、`mm`、`imr`、`mmr`、`margin_balance`、`available_margin` field in `GET /unified/accounts` response
  * `PUT /unified/unified_mode` endpoint，Added single-currency margin mode

**v4.87.0**

  * New feature `GET /unified/history_loan_rate` endpoint, Get historical lending rates

**v4.86.0**

2024-12-02

  * New feature `GET /wallet/order_status` endpoint. Transfer status query
  * Add `update_id` field in `GET /futures/{settle}/positions` response

**v4.85.0**

2024-11-11

  * Add `x-gate-exptime` field in `POST /futures/{settle}/orders`、`POST /spot/batch_order` header.
  * 

Add `cross_order_margin`、`cross_initial_margin`、`cross_maintenance_margin`、`cross_unrealised_pnl`、`cross_available`、`isolated_position_margin` field in `POST /futures/{settle}/dual_mode` response.

**v4.84.0**

2024-11-04

  * New feature `GET /loan/multi_collateral/current_rate` endpoint, Query the current interest rate of the currency
  * Add `lowest_size`、`highest_size` field in `GET /spot/tickers` response
  * Add `amount` field in `POST /earn/dual/orders` request body

**v4.83.0**

2024-10-28

  * New feature `GET /unified/leverage/user_currency_config` endpoint, Query the maximum and minimum leverage multiples that users can set for a currency
  * New feature `GET /unified/leverage/user_currency_setting` endpoint, Get the user's currency leverage
  * New feature `POST /unified/leverage/user_currency_setting` endpoint, Set the currency leverage ratio
  * Add `id` field in `GET /futures/{settle}/account_book` response
  * Add `leverage` field in `GET /unified/currency_discount_tiers` response

**v4.82.0**

2024-10-14

  * New feature `GET /account/rate_limit` endpoint, Get user flow limit information. For details, please refer to Trade Ratio Rate Limiting
  * Add `copy_trading_role` field in `GET /account/detail` response

**v4.81.0**

2024-09-30

  * New feature `POST /options/countdown_cancel_all` endpoint, Countdown to cancel order
  * Add `message` field in `GET /wallet/push` response
  * Add `from`、`to` in `GET /futures/{settle}/funding_rate` query
  * Add `is_max` field in `POST /earn/dual/orders` response

**v4.80.0**

2024-09-09

  * New feature `GET /options/mmp` endpoint, MMP Query
  * New feature `POST /options/mmp` endpoint, MMP Settings
  * New feature `POST /options/mmp/reset` endpoint, MMP Reset
  * Add `block_number` field in `GET /wallet/withdrawals` response

**v4.79.0**

2024-09-02

  * Add `from`、`to` field in `GET /unified/interest_records` query
  * Add `options` field in `GET /unified/unified_mode` response
  * Add `options` field in `PUT /unified/unified_mode` request body

**v4.78.0**

2024-08-19

  * New feature `GET /wallet/push` endpoint, Get Records
  * New feature `POST /withdrawals/push` endpoint, Transfer between spot main accounts. Both parties cannot be sub-accounts.
  * New feature `GET /futures/{settle}/batch_amend_orders` endpoint, Batch modify orders with specified IDs
  * Add `close_size` field in `GET /futures/{settle}/my_trades` response
  * Add `tx_id` field in `POST /wallet/transfers` response

**v4.77.0**

2024-08-05

  * New feature: add `GET /sub_accounts/unified_mode` endpoint，Get sub-account mode
  * Add `from`、`to` field in `GET /rebate/broker/commission_history` query
  * Add `from`、`to` field in `GET /rebate/broker/transaction_history` query

**v4.76.0**

2024-07-22

  * New feature: add `GET /rebate/partner/sub_list` endpoint，Partner subordinate list
  * Add `page`、`limit` field in `GET /flash_swap/currency_pairs` query
  * Add `order_id`、`currency_pair`、`account` field in `PATCH /spot/orders/{order_id}`
  * Add `order_id`、`currency_pair`、`account` field in `DELETE /spot/orders/{order_id}`

**v4.75.1**

2024-07-08

  * New feature: add `GET /delivery/{settle}/risk_limit_tiers` endpoint，querying risk limit levels
  * New feature: add `GET /rebate/partner/transaction_history` endpoint，partners to get the transaction history of recommended users
  * Add `borrow_type` field in `GET /unified/loan_records` response
  * Add `accum_size` field in `GET /futures/{settle}/position_close` response

**v4.75.0**

2024-06-24

  * New feature: add `GET /account/debit_fee` endpoint，query GT deduction configuration.
  * New feature: add `POST /account/debit_fee` endpoint, to enable or disable GT deduction for the current account.

**v4.74.1**

2024-06-11

  * Optimization of DOM for the visible area on mobile devices

**v4.74.0**

2024-05-29

  * New feature: add `GET /unified/loan_margin_tiers` endpoint, list loan margin tiers

**v4.73.0**

2024-05-27

  * Add `is_all` parameter in `POST /wallet/small_balance` endpoint
  * Add `text` field in `POST /spot/cancel_batch_orders` response
  * Add `funding`、`funding_version`、`use_funding` field in `GET /unified/accounts` response

**v4.72.0**

2024-05-13

  * Add `last_access` field in `GET /sub_accounts/{user_id}/keys` response
  * Add `contract` field in `GET /futures/{settle}/risk_limit_tiers` response

**v4.71.0**

2024-04-23

  * Add `page` parameter in `GET /wallet/saved_address` endpoint
  * New feature: add `GET /api/v4/rebate/user/info` endpoint, retrieve user rebate information
  * New feature: add `POST /unified/portfolio_calculator` endpoint, portfolio margin calculator
  * New feature: add `GET /unified/risk_units` endpoint, retrieve user risk unit
  * New feature: add `PUT /unified/unified_mode` endpoint, set unified account mode
  * New feature: add `GET /unified/unified_mode` endpoint, retrieve unified account mode

**v4.70.0**

2024-04-08

  * Add `pnl_pnl`、`pnl_fund`、`pnl_fee` field in `GET /futures/{settle}/positions` response
  * Add `pnl_pnl`、`pnl_fund`、`pnl_fee` field in `GET /futures/{settle}/position_close` response

**v4.69.0**

2024-03-25

  * Add `text` field in `POST /delivery/{settle}/price_orders` response

**v4.68.0**

2024-03-18

  * New feature: add `GET /unified/currency_discount_tiers` endpoint, list currency discount tiers
  * Add `type` parameter in `GET /unified/loans` endpoint
  * Add `type` parameter in `GET /unified/interest_records` endpoint

**v4.67.0**

2024-03-11

  * Add `filled_amount` field in `POST /spot/orders`,`POST /spot/batch_orders` response
  * In frequency limit rule for the wallet withdrawal interface, the speed limit description has been corrected from `10r/10s` to `1r/3s`(No modification to the original rate limiting behavior)

**v4.66.1**

2024-02-19

  * New feature: add `GET /wallet/small_balance` endpoint, list small balance.
  * New feature: add `GET /wallet/small_balance_history` endpoint, list small balance history.
  * New feature: add `GET /unified/estimate_rate` endpoint, get unified estimate rate.

**v4.65.0**

2024-01-29

  * Add `debit_fee` field in `GET /spot/batch_fee` response
  * Add `user_id` parameter in `DELETE /account/stp_groups/{stp_id}/users` endpoint
  * Spot API introduces asynchronous support modes for create orders: `ACK`, `RESULT`, `FULL`. For details, please refer to SPOT API

**v4.64.0**

2024-01-22

  * Add `order_type` parameter in `GET /loan/multi_collateral/orders` endpoint
  * Add `order_type`,`fixed_type`,`fixed_rate`,`expire_time`,`auto_renew`,`auto_repay` field in `GET /loan/multi_collateral/orders` response
  * Add `before_ltv`,`after_ltv` field in `GET /loan/multi_collateral/repay` response
  * New feature: add `GET /loan/multi_collateral/fixed_rate` endpoint, query multi-collateral fix rate.
  * Add `unrealised_pnl`,`borrowed` field in `GET /wallet/total_balance` response

**v4.63.0**

2024-01-15

  * Add `decimal` field in `GET /wallet/currency_chains` response
  * New feature: add `GET /futures/{settle}/risk_limit_tiers` endpoint, list risk limit tiers.

**v4.62.0**

2024-01-02

  * New feature: add `POST /futures/{settle}/batch_cancel_orders` endpoint, users have the ability to batch cancel orders.
  * New feature: add multi-collateral-loan api. (`/loan/multi_collateral/**`)

**v4.61.0**

2023-12-18

  * New features: The broker obtains the user's commission rebate records in `GET /rebate/broker/commission_history` and `GET /rebate/broker/commission_history` endpoints

**v4.60.0**

2023-12-01

  * Breaking change: New Unified API is online. The old `/portfoli/*` endpoints are deprecated.
  * New features: add earn product api. (`/earn/**`)
  * Add `trade_id` field in `GET /futures/{settle}/account_book` response

**v4.59.0**

2023-11-22

  * Add `funding_cap_ratio` field in `GET /futures/{settle}/contracts` response
  * Add `contract` field in `GET /delivery/{settle}/account_book` response
  * Add `withdraw_percent_on_chains` field in `GET /wallet/withdraw_status` response
  * Add `leverage` field in `GET /portfolio/accounts` response

**v4.58.0**

2023-11-03

  * Add `tier` field in `GET /account/detail` response
  * Add `max_base_amount`、`max_quote_amount` field in `GET /spot/currency_pairs` response

**v4.57.0**

2023-10-20

  * New feature: API Gateway inbound & outbound time, For more details, please refer to the API Gateway in/out time
  * New feature: support portfolio account in `POST /spot/orders` endpoint
  * New feature: add `PUT /earn/uni/interest_reinvest` endpoint, users have the option to enable or disable interest reinvestment.
  * New feature: add `POST /spot/amend_batch_orders` endpoint, users have the ability to batch modify orders.
  * Add `sequence_id` field in `GET /spot/trades` response
  * Add `text` field in `GET /spot/account_book` response
  * Add `text` field in `GET /spot/my_trades` response
  * `GET /portfolio/spot/orders`、 `GET /portfolio/spot/orders`、`GET /portfolio/spot/orders/{order_id}`、`DELETE /portfolio/spot/orders/{order_id}` and `PATCH /portfolio/spot/orders/{order_id}` have been deprecated. We will remove the endpoints by the end of October 2023\. Please use `/spot/orders` instead.

**v4.56.0**

2023-09-25

  * Add `repayment_type` field in `GET /portfolio/loan_records` endpoint.
  * Add request parameter `holding` in `GET /futures/{settle}/positions` endpoint
  * Add request parameter `role` in `GET /futures/{settle}/my_trades_timerange` endpoint
  * Add request parameter `side` and `pnl` in `GET /futures/{settle}/position_close` endpoint

**v4.55.0**

2023-09-12

  * Add new `POST /portfolio/account_mode` endpoint, allow to change the mode.

**v4.54.0**

2023-08-28

  * Add `contract_address` field in `GET /wallet/currency_chains` endpoint.
  * Add `GET /portfolio/spot/currency_pairs` and `GET /portfolio/spot/currency_pairs/{currency_pair}` endpoints, list portfolio spot's currency pairs.

**v4.53.0**

2023-08-14

  * New feature: delete user in STP group in `DELETE /account/stp_groups/{stp_id}/users` endpoint

**v4.52.0**

2023-08-07

  * New feature: add collateral loan api

**v4.51.0**

2023-07-29

  * Adjusted and optimized the account book types
  * Add `mode` field in `GET /account/detail` edpoint.

**v4.50.0**

2023-07-14

  * New feature: New Portfolio API. Currently, these services are only available to whitelisted users. If you are interested in accessing these APIs, please contact our institutional department for further information.
  * Add new endpoint `GET /flash_swap/currency_pairs`, list all flash swap currency pair

**v4.49.0**

2023-07-03

  * Add new frequency limit rule，the new rule is expected to take effect on 2023-07-10 (UTC+8)
  * In the `GET /futures/{settle}/orders` API endpoint, the request field `contract` has been modified to be optional instead of mandatory.

**v4.48.0**

2023-06-16

  * Add `client_order_id` fields in `GET /wallet/sub_account_transfers` edpoint.

**v4.47.0**

2023-05-23

  * New feature: add STP group admin api
  * New feature: query estimated interest rates of margin in `GET /margin/uni/estimate_rate` endpoint.
  * New feature: list futures order by time range in `GET /futures/{settle}/orders_timerange` endpoint
  * Add `underlying`、`underlying_price`、`mark_iv`、`delta`、`gamma`、`vega`、`theta` fields in `GET /options/positions/{contract}` endpoint.

**v4.46.0**

2023-05-08

  * New feature: query spot account book in `GET /spot/account_book` endpoint
  * New feature: query user futures trading fee in `GET /futures/{settle}/fee` endpoint

**v4.45.0**

2023-04-21

  * The margin loan has been migrated to the `Lend & Earn`. For more information, please refer to the Margin Migration Instructions
  * New feature: Add `Self-Trade Prevention` feature in the `POST /futures/{settle}/batch_orders` endpoint.

**v4.44.0**

2023-04-07

  * Add `ORDER_BOOK_NOT_FOUND` and `FAILED_RETRIEVE_ASSETS` error messages.

**v4.43.0**

2023-03-27

  * New feature: Add `Self-Trade Prevention` feature in the `POST /spot/orders` endpoint. Fore more detail, please refer to STP overview
  * New feature: Get API key's ip whitelist in `GET /account/detail` endpoint.
  * Add `amend_text` in `PATCH /spot/orders/{order_id}` endpoint.

**v4.42.0**

2023-03-13

  * New feature: add `Lend & Earn` API
  * New feature: Add `Self-Trade Prevention` feature in the `POST /futures/{settle}/orders` endpoint. Fore more detail, please refer to STP overview
  * Add `delivery` account type in `POST /wallet/sub_account_transfers` endpoint

**v4.41.0**

2023-03-03

**v4.40.0**

2023-02-24

  * New feature: List Auto-Deleveraging history endpoint `Get /futures/{settle}/auto_deleverages`
  * Add `sum` field in `GET /futures/{settle}/candlesticks` endpoint

**v4.39.0**

2023-02-09

  * New feature: Query a batch of user trading fee rate endpoint `GET /spot/batch_fee`
  * Add `enable_bonus`、`enable_credit` fields in `GET /futures/{settle}/contracts` endpoint

**v4.38.0**

2023-02-04

  * New feature: time range query for my futures trade endpoint `GET /futures/{settle}/my_trades_timerange`
  * Add `withdraw_order_id` field in `POST /withdrawals` endpoint

**v4.37.0**

2023-01-20

  * Add new rebate API endpoints.

**v4.36.0**

2022-12-23

  * Hiding all amount is not supported any more when using `iceberg` in `POST /spot/orders` and `POST /spot/batch_orders` endpoints

**v4.35.0**

2022-12-09

  * New feature: amend order endpoint `/spot/orders/{order_id}`
  * Add `avg_deal_price` field in `GET /spot/orders` response
  * Support market order in `POST /spot/batch_orders` endpoint

**v4.34.0**

2022-11-25

  * Support market order in `POST /spot/orders` endpoint

**v4.33.0**

2022-11-11

  * New feature: Futures Premium Index endpoint `GET /futures/{settle}/premium_index`
  * Allow to specify password and email when creating a sub-account.

**v4.32.0**

2022-10-28

  * Improve options api document

**v4.31.0**

2022-10-14

  * Allow to transfer futures and cross_margin funds between two sub-accounts in `POST /wallet/sub_account_to_sub_account` endpoint

**v4.30.0**

2022-09-23

  * New feature: manage sub-accounts API Key
  * New feature: lock and unlock sub-account endpoint
  * Allow to transfer between two sub-accounts in `POST /wallet/sub_account_to_sub_account` endpoint

**v4.29.0**

2022-09-09

  * New feature: create and list sub-accounts
  * Add `settle` parameter in `GET /wallet/fee` endpoint
  * Add `refr` field in option order
  * The maximum number of API Keys changes to 20

**v4.28.0**

2022-08-12

  * Add `offset` parameter in `GET /futures/{settle}/trades`
  * new countdown cancel orders endpoint for spot and futures.

**v4.27.0**

2022-07-29

  * Add `X-Client-Request-Id` http header for tracking request
  * new create a batch of futures order endpoint `POST /futures/{settle}/batch_orders`
  * new `FOK` tif type for futures order

**v4.26.0**

2022-07-15

  * Spot Price-Trigger order supports portfolio margin account
  * Add `GET /wallet/saved_address` to list saved address
  * `POST /wallet/transfers` returns `tx_id` field
  * Add `GET /wallet/sub_account_cross_margin_balances` to query subaccount's `cross_margin` account
  * Add `status` field in `GET /margin/currency_pairs` response

**v4.25.1**

2022-07-06

  * New `GET /spot/time` endpoint which get system's time info.
  * New `GET /options/my_settlements` endpoint which list my selttlements.
  * Add `change_utc0`, `change_utc8` fields in `GET /spot/tickers` endpoint

**v4.25.0**

2022-06-24

  * Support portfolio margin account API
  * Cross-margin add more fields. Please refer to endpoint document for more details.
  * New `POST /spot/cross_liquidate_orders` spot trading endpoint that close position when the cross-currency is disabled
  * Add `bouns` and `history` fields in `GET /futures/{settle}/accounts` endpoint
  * Add `text`、`fee` and `point_fee` fields in `GET /futures/{settle}/my_trades` endpoint
  * Fix typo for `cancel a price-triggered order` endpoints
  * `POST /wallet/sub_account_transfers` supports transferring to `cross_margin`

**v4.24.0**

2022-05-20

  * Support flash swap operations with new API group `/flash_swap`. Spot operation permission is required.
  * New wallet APIs `GET /wallet/sub_account_margin_balances` and `GET /wallet/sub_account_futures_balances` to help main account retrieving sub accounts' margin and perpetual contract balances
  * New perpetual contract API `GET /futures/{settle}/index_constituents/{index}` to retrieve index price constituents
  * Fix missing fields like `order_type` in `FuturesPriceTriggeredOrder`

**v4.23.4**

2022-04-25

  * Spot candlesticks supports `30d` interval

**v4.23.3**

2022-04-01

  1. Spot candlestick API returns base currency amount
  2. Spot currency detail add `chain` field.
  3. Add withdrawal and deposit status in `GET /wallet/currency_chains` response
  4. Add missing `cross_leverage_limit` in perpetual contract's dual mode position leverage update API
  5. Support more intervals in perpetual and delivery contract candlesticks

**v4.23.2**

2022-01-21

  1. Add `fee` in withdrawal and deposit history
  2. Add fix fee rate in spot `Currency`

**v4.23.1**

2021-12-23

  1. Spot orders support new `time_in_force` `FOK`
  2. New `FOK_NOT_FILL` error label

**v4.23.0**

2021-12-09

  1. Add options API
  2. Add detailed rate limiting rules
  3. Add `GET /wallet/currency_chains` to retrieve chains supported by currency
  4. Add additional status for deposit and withdrawal history

**v4.22.4**

2021-11-01

  1. Data type of `ctime` and `ftime` in `SpotPriceTriggeredOrder` should be `int64`

**v4.22.3**

2021-10-27

  1. `GET /spot/trades` supports time range based query using `from` and `to`.

**v4.22.2**

2021-09-29

  1. Add more status in withdrawal or deposit record model
  2. Add new write only field `auto_size` in `FuturesOrder` to support closing dual mode position.

**v4.22.1**

2021-09-07

  1. New wallet API `GET /wallet/total_balance` to retrieve all user's estimate balance.
  2. Add `locked` and `risk` in margin account response
  3. Margin and cross margin loans support custom text input.

**v4.22.0**

2021-08-13

  1. Delivery contract API supports BTC settled
  2. Spot API `GET /spot/orders` and `GET /spot/my_trades` supports query by time range
  3. Add margin and cross margin max borrowable API
  4. Multiple document enhancements.

**v4.21.6**

2021-08-12

  1. Fix incorrect address field name in `GET /wallet/deposit_address`

**v4.21.5**

2021-06-30

  * `GET /spot/orders`, `GET /spot/orders/{order_id}` and `GET /spot/my_trades` allow empty `currency_pair` if operated against finished orders
  * Add fixed withdrawal fee on multiple chains in `GET /wallet/withdraw_status` response
  * Add `GET /margin/transferable` to retrieve maximum transferable amount from margin account
  * Add `from` and `to` parameter to specify time range for futures position closes history API

**v4.21.4**

2021-06-23

  * Add millisecond timestamp in `GET /margin/account_book` response

**v4.21.3**

2021-06-17

  * Add order book timestamp for both spot and futures trading

**v4.21.2**

2021-06-07

  * Futures API support cross margin leverage modification
  * Add new spot cross margin API `/margin/cross`
  * Add spot order operations using spot cross margin account
  * Add unpaid interests in spot margin account query
  * Add new millisecond fields `create_time_ms` and `update_time_ms` in spot orders.
  * Add `DELETE /withdrawals/{withdrawal_id}` to cancel withdrawal operation

**v4.20.1**

2021-04-14

  * Update document links

**v4.20.0**

2021-03-25

  * Support spot auto orders with API group `/spot/price_orders`

**v4.19.6**

2021-03-22

  * Add trading timestamp in spot currency pair

**v4.19.5**

2021-03-18

  * Spot and Futures operations based on order ID also accept user custom ID(but only for 30 minutes since creation)

**v4.19.4**

2021-03-10

  * `/wallet/sub_account_transfers` supports transferals with sub user's perpetual contract account

**v4.19.3**

2021-03-04

  * Add margin loans auto repay API `/margin/auto_repay`
  * Add `multichain_address` in `/wallet/deposit_address` for currencies with multiple deposit addresses
  * Optimize documentation

**v4.19.2**

2021-03-01

  * Add `/wallet/fee` API to retrieve trading fee. Previous `/spot/fee` is deprecated in favour of this one.
  * Add new field `chain` in withdrawal operation.
  * Add new field `with_id` in `/futures/{settle}/order_book` API and `id` field in its response
  * Add new `offset` in API `/futures/{settle}/position_close` to retrieve position close history with pagination.
  * Add contract value calculation. Refer to `Contract` model for details.
  * Fix incorrect field type in futures stats API

**v4.18.4**

2021-01-22

  * Add field `create_time_ms` in spot `Trade` model
  * ETF currency pairs' ticker add net value related info

**v4.18.1**

2021-01-07

  * Add iceberg order support for spot orders
  * Fix incorrect field types in `/futures/{settle}/contract_stats`

**v4.18.0**

2020-12-21

  * Add new spot API`/spot/currencies` and `/spot/currencies/{currency}` to retrieve currency info
  * Add more fields, e.g., `top_lsr_account`, `top_lsr_size`, in futures `ContractStat` model.

**v4.17.1**

2020-12-16

  * Increase maximum of `limit` in `/spot/order_book` to 100

**v4.17.0**

2020-12-15

  * Add `/wallet/sub_account_balances` to retrieve sub accounts' balances.

**v4.16.1**

2020-12-10

  * Fix mistaken field name `dual_mode` in futures position model which should be `mode` instead.

**v4.16.0**

2020-12-09

_Spot_

  * Increase order number limit each currency pair to 10 in `POST /spot/batch_orders`
  * Add new query parameter `reverse` in `GET /spot/trades` to trace back trading history

_Futures_

  * Add perpetual contract dual mode position support. Use `/futures/{settle}/dual_mode` to set position's dual mode. For dual mode position operations, refer to `/futures/{settle}/dual_comp/positions` API group
  * Add perpetual contract new field `in_dual_mode` in futures account response model; `dual_mode` in position response model.
  * Add new perpetual contract public API `/futures/{settle}/liq_orders` to query liquidated orders in markets

**v4.15.5**

2020-11-04

  * Add `/futures/{settle}/contract_stats` API to retrieve contract stats
  * Add `/margin/{currency_pair}` to retrieve single margin currency pair detail

**v4.15.4**

2020-09-01

  * Add `point_type` in `GET /spot/fee` response
  * Add `GET /wallet/withdraw_status` API
  * Add C# SDK entry

**v4.15.2**

2020-08-12

  * Add `GET /spot/fee` to retrieve spot order trading fee rates

**v4.15.1**

2020-08-04

  * Add `GET /spot/open_orders` to retrieve all open orders in spot trading
  * Add `GET /margin/account_book` to retrieve margin account balance history

**v4.14.1**

2020-07-08

  * maximum length of `text` field in order extends to 28(prefix excluded)

**v4.14.0**

2020-07-06

  * New Delivery contract APIs `/delivery`

**v4.13.1**

2020-06-28

  * Add `GET /wallet/sub_account_transfers` to list sub account transfer records

**v4.13.0**

2020-05-20

  * APIv4 now supports withdraw API. Refer to `POST /withdrawals` and "Authentication" section for details.
  * `POST /wallet/transfers` supports transferring between spot and futures account
  * Wallet API supports retrieving deposits and withdrawals history
  * Futures orders and personal trades retrieving now supports `offset` field
  * Futures `Contract` model add new field `in_delisting`

**v4.12.0**

2020-04-08

  * APIv4 Key management improved. Keys are no longer separated with different trading types. Every key can now have multiple operation permissions. Refer to _"About APIv4 key improvement"_ for details.
  * Add `POST /wallet/sub_account_transfers` to support transferring between main and sub account
  * `GET /spot/candlesticks` adds query parameters `from` and `to` to support retrieving history data points

**v4.11.2**

2020-03-29

  * Add `filled_total` in `Order` to replace `fill_price` (the latter is badly named)
  * Add new error label `POC_FILL_IMMEDIATELY`

**v4.11.1**

2020-03-23

  * Add `role` in `GET /spot/my_trades` response
  * Fix missing currency account in `GET /margin/funding_accounts`

**v4.11.0**

2020-03-20

  * Spot order supports GT fee discount
  * Spot order time in force supports `poc`

**v4.10.1**

2020-02-24

  * Add `trade_status` in spot currency pair

**v4.10.0**

2020-02-17

  * Margin order creation adds new field `auto_borrow`(write only) to borrow the insufficient part by the system if balance is not enough
  * Add new API `POST /spot/cancel_batch_orders` to support batch cancellation with specified order IDs
  * Add new document section "Error handling" and "Which one to choose, APIv4 or APIv2?"

**v4.9.1**

2020-01-07

  * Add fee and recent modification time in `Order` and `BatchOrder`
  * Add fee in `GET /spot/my_trades` response

**v4.9.0**

2019-12-17

  * `last_id` in `GET /futures/{settle}/trades` is deprecated. Use `from` and `to` to retrieve trading history

**v4.8.2**

2019-12-02

  * Add `/spot/batch_orders` to support creating a bundle of spot or margin orders
  * Fee rate of margin loan repayment enjoys VIP discount
  * `Loan` add new fields `fee_rate`(fee rate of lending loan) and `orig_id`(original loan ID if loan is auto renewed)

**v4.8.1**

2019-11-27

  * Fix missing `settle` in `GET /futures/{settle}/positions` docs and code snippet

**v4.8.0**

2019-11-07

  * Futures API now supports settling in USDT.
  * Change `/futures` to `/futures/{settle}` in ALL futures API to support futures operations in different settle currency.
  * `currency` field in `/futures/{settle}/accounts` response adds new value: `USDT` response to replace `volume_24h_btc` and `volume_24h_usd`. The latter two are still preserved for compatibility usage, but are NOT recommended for any futures operations.

To use USDT futures, just replace `/futures` with `/futures/usdt`, e.g. use `GET /futures/usdt/accounts` to retrieve futures accounts settled in USDT, while `GET /futures/btc/accounts` returns accounts in BTC.

For compatibility, `GET /futures/xxx` defaults to `GET /futures/btc/xxx`, e.g. `GET /futures/accounts` will be treated as `GET /futures/btc/accounts`

**v4.7.3**

2019-07-18

  * Add `text` in `/spot/orders` and `/futures/orders` to support user defined order information

**v4.6.3**

2019-06-11

  * Add point information in Futures account and position

**v4.7.2**

2019-05-29

  * Change `rate` in `Loan` as non-required for lending side.

**v4.7.1**

2019-04-17

  * Add wallet v4 API. Support transfers between spot and margin account for now.
  * `GET /margin/loans` can sort by `rate` and support an optional parameter `currency_pair`
  * Fix miscellaneous document issues

**v4.6.2**

2019-04-24

  * Fix price-triggered futures order's docs incorrect override docs for `GET /futures/orders/{order_id}` and `DELETE /futures/orders/{order_id}`

**v4.6.1**

2019-04-02

  * Add `high_24h`, `low_24h` and `funding_rate_indicative` in futures ticker

**v4.6.0**

2019-03-21

_SDK related only_

  * Rename futures order related function name in SDKs to avoid duplication with spot order API in Go
  * Fix query parameter not decoded while generating authentication signature

**v4.5.2**

2019-03-14

  * `currency_pair` in `/spot/order_book` should be a required parameter
  * Optimize document code samples

**v4.5.1**

2019-03-11

  * Fix missing URL parameter description

**v4.5.0**

2019-03-05

To avoid version confusion, all versions in APIv4 (documents and SDKs are both included) will start with `4` from now on

  * Add Spot v4 API to provide improved API capability
  * Add Margin v4 API to provide support for margin loans and trading
  * Add Futures price triggered auto order API support. Refer to `/futures/price_orders` for details
  * Base URL of all Gate API v4 real trading changed to `https://api.gateio.ws/api/v4`

**v1.3.0**

2019-02-13

_Important update_

  * Domain of base URLs are changed to `fx-api.gateio.ws` and `fx-api-testnet.gateio.ws` respectively, `*.gateio.io` is deprecated and will soon be out of service.

**v1.2.1**

2019-02-13

  * Add `volumn_24h_usd` and `volume_24h_btc` in `GET /futures/tickers` response

**v1.2.0**

2019-01-17

  * Add `GET /futures/contracts/{contract}` to get one single contract
  * Add `GET /futures/positions/{contract}` to get one single position
  * Add `GET /futures/account_book` to retrieve user account balance history
  * Add `config_change_time` in `Contract` model
  * fix miscellaneous document issues

**v1.1.0**

2019-01-08

  * Add more fields to `Contract`, `Position`, `FuturesOrder`
  * Add API `GET /futures/position_close` to retrieve position close history
  * Add optional `order_id` support for API `GET /futures/my_trades`
  * Change the status code of `DELETE /futures/orders` and `DELETE /futures/orders/{order_id}` from 204 to 200, with cancelled order details returned on success.
  * Request `DELETE /futures/orders/{order_id}` with invalid order ID or order that has been finished will return 404 instead of ignoring the error
  * `POST /futures/orders` now supports POC, iceberg

**v1.0.0**

2018-12-30

  * Initial release

#  General

##  Matching mechanism

###  Matching priority

Gate Order matching follows Price Priority > Time priority principle.

Suppose that the order book is as follows：

Matching priorityOrder | Order time | Ask/Selling price  
---|---|---  
A | 10:00 | 100  
B | 10:00 | 102  
C | 10:01 | 100  
  
If the current price of 10:02 pays 102, the final transaction order is: A, C, B

###  Order life cycle

A valid order sent to the matching engine is immediately confirmed and executed with existing orders, with the executing result sent back to the client.

If an order is fully executed, then it is closed. If any part of the order is not executed immediately, orders with TimeInForce set to `IOC` will be cancelled, while others will be appended to the price list, waiting for subsequent filling or being cancelled.

##  Data Center

Gate data center is located in AWS Japan's ap-northeast-1 region.

##  API Overview

API OverviewAPI Classification | Category Links | Overview  
---|---|---  
host + `/api/v4/spot/*` | Spot Trading | Including currency status, market information, order, transaction records and other functions  
host + `/api/v4/margin/*` | Margin Trading | Margin account management, lending, repayment, etc  
host + `/api/v4/wallet/*` | Wallet Management | Charge and withdrawal records, balance inquiries, fund transfers, etc.  
host + `/api/v4/withdrawals/*` | Withdrawal | Withdrawal of digital currency  
  
##  Margin Migration Instructions

Between 14:00 (UTC+8) on April 13, 2023 and 14:00 (UTC+8) on April 23, 2023, the platform will gradually migrate the assets that have not been borrowed in the lending market to the `Lend & Earn` through an automated system process. At the same time, assets that have already been borrowed will be cancelled for automatic lending. After the migration is complete, you can check your investment details in the `Lend & Earn`. During this period, borrowing funds through the lending market will be temporarily suspended. You can also manually transfer your assets from the lending market to the `Lend & Earn` to obtain investment returns in advance.

After the automatic migration, the old version of the borrowing and lending endpoint will be deprecated, and the new version of the endpoint can be found in the /margin/uni endpoint group. For detailed endpoint migration, please refer to the following table:"

Margin account related endpoints：

Margin Migration InstructionsName | Path | Deprecated | New Path  
---|---|---|---  
Margin account list | GET /margin/accounts | No | `-`  
List margin account balance change history | GET /margin/account_book | No | `-`  
Funding account list | GET /margin/funding_accounts | No | `-`  
Update user's auto repayment setting | POST /margin/auto_repay | No | `-`  
Querying user's automatic repayment settings | GET /margin/auto_repay | No | `-`  
Get the max transferable amount for a specific margin currency | GET /margin/transferable | No | `-`  
  
The margin lending and borrowing related APIs have been migrated to the `/margin/uni` API group：

Margin Migration InstructionsName | Old Path | Deprecated | New Path  
---|---|---|---  
List all supported currency pairs supported in margin trading | GET /margin/currency_pairs | Yes | GET /margin/uni/currency_pairs  
Query one single margin currency pair | GET /margin/currency_pairs/{currency_pair} | Yes | GET /margin/uni/currency_pairs/{currency_pair}  
Lend or borrow | POST /margin/loans | Yes | POST /margin/uni/loans  
Retrieve one single loan detail | GET /margin/loans/{loan_id} | Yes | `-`  
List all loans | GET /margin/loans | Yes | GET /margin/uni/loans  
Repay a loan | POST /margin/loans/{loan_id}/repayment | Yes | POST /margin/uni/loans  
List loan repayment records | GET /margin/loans/{loan_id}/repayment | Yes | GET /margin/uni/loan_records  
Get the max borrowable amount for a specific margin currency | GET /margin/borrowable | Yes | GET /margin/uni/borrowable  
List interest records | `-` | `-` | GET /margin/uni/interest_records  
  
The earn related APIs have been migrated to the `/earn/uni` API group):

Margin Migration InstructionsName | Old Path | Deprecated | New Path  
---|---|---|---  
List all supported currency pairs supported in margin trading | GET /margin/currency_pairs | Yes | GET /earn/uni/currencies  
Query one single margin currency pair | GET /margin/currency_pairs/{currency_pair} | Yes | GET /earn/uni/currencies/{currency}  
Lend or borrow | POST /margin/loans | Yes | POST /earn/uni/lends  
List all loans | GET /margin/loans | Yes | GET /earn/uni/lends  
Order book of lending loans | GET /margin/funding_book | Yes | -  
Merge multiple lending loans | POST /margin/merged_loans | Yes | -  
Modify a loan | PATCH /margin/loans/{loan_id} | Yes | PATCH /earn/uni/lends  
Cancel lending loan | DELETE /margin/loans/{loan_id} | Yes | POST /earn/uni/lends  
List repayment records of a specific loan | GET /margin/loan_records | Yes | GET /earn/uni/lend_records  
Get one single loan record | GET /margin/loan_records/{loan_record_id} | Yes | `-`  
Modify a loan record | PATCH /margin/loan_records/{loan_record_id} | Yes | `-`  
List interest records | `-` | `-` | GET /earn/uni/interest_records  
  
#  API

##  HTTP convention

  * All read endpoints use `GET` method. They accept only request parameters. No request body will be read.
  * `DELETE` methods remove resources(like orders), but not all removing operation using `DELETE`, as `DELETE`s don't read request body either. For complex removing operations, `POST` method is used with parameters filled in request body.
  * Updating is done using `POST`, `PUT` or `PATCH` method. Their parameters are either in body or request parameters for different endpoints. Refer to endpoint detail for how to send the request.
  * All endpoints return HTTP status code `2xx` on success. `401` is returned on authentication failure. Other `4xx` codes mean the request is malformed. `5xx` means the server encounter some critical error on processing the request. Commit issues if `5xx` is met.

##  Time

All time related fields are unix timestamp in **seconds** if no extra note, but they may differ in formats(int64, number or string). Possible values like the following may be returned:

  * 1596531048
  * "1596531048"
  * 1596531048.285
  * "1596531048.285"

The best way to handle time fields is parsing them as a number with decimal places. If higher precision is not needed, you can safely cast them to integer(or long). Our SDKs listed above has already taken proper deserialization to handle them

##  API Gateway in/out time

In every API request, the response header will always include the following fields:

  * `X-In-Time`: The timestamp when the API gateway receives a request, in Unix timestamp format, measured in microseconds.

  * `X-Out-Time`: The timestamp when the API gateway returns a response, in Unix timestamp format, measured in microseconds.

For example:
    
    
    X-In-Time: 1695715091540163
    X-Out-Time: 1695715091551905
    

##  Pagination

Pagination is achieved using one of the following method

  * `page-limit`
  * `limit-offset`

In both method, `limit` limits the maximum number of records returned in one request. If no additional explanation, it defaults to `100` if not provided and its maximum value is limited to `1000`.

`page` starts from `1`, mimicking common paging used in web pages. To iterate the whole list, use the same `limit` and increment `page` by `1` until the records' length is shorter than the `limit`

`offset` starts from `0`, behaving like common DB search. To iterate the whole list, increment `offset` by `limit` until the records' length is shorter than the `limit`.

For example, if the total number of orders is 201. Using page-limit method, send request parameters like the following:

  1. `page=1&limit=100`
  2. `page=2&limit=100`
  3. `page=3&limit=100`

Using limit-offset method, send request parameters like:

  1. `limit=100&offset=0`
  2. `limit=100&offset=100`
  3. `limit=100&offset=200`

Some endpoints may return additional pagination metadata. If present, they are sent back through the response header. Take `GET /futures/{settle}/orders` as an example, following headers will be returned

  * `X-Pagination-Limit`: request limit
  * `X-Pagination-Offset`: request offset
  * `X-Pagination-Total`: total record number satisfying the request

##  Frequency limit rule

Frequency limit ruleMarkets | Endpoints | Limits | Based On | Include  
---|---|---|---|---  
All public endpoints | Public endpoints | 200r/10s per endpoint  | IP | Orderbook, Candlestick, Ticker, etc.  
Wallet | Private endpoints |  Withdrawal(POST /withdrawals) : 1r/3s  
UID transfer(POST /withdrawals/push) 1r/10s  
Transfer between trading accounts (POST /wallet/transfers) 80r/10s  
Transfer between main and sub accounts (POST /wallet/sub_account_transfers) 80r/10s  
Transfer from a sub-account to another sub-account (POST /wallet/sub_account_to_sub_account) 80r/10s  
Retrieve user's total balances (GET /wallet/total_balance) 80r/10s  
Retrieve sub account balances (GET /wallet/sub_account_balances) 80r/10s  
Query sub accounts' margin balances (GET /wallet/sub_account_margin_balances) 80r/10s  
Query sub accounts' futures account balances (GET /wallet/sub_account_futures_balances) 80r/10s  
Query subaccount's cross_margin account info(GET /wallet/sub_account_cross_margin_balances) 80r/10s  
The Others: 200r/10s per endpoint  
| UID |  Withdrawal.  
Query personal account balance.  
Query subaccount balance.  
  
Spot | Private endpoints |  The rate limit for batch/single order placement and amend an order are total of 10r/s (UID+Market)  
The rate limit for batch/single order cancellation is total of 200r/s  
The Others: 200r/10s per endpoint  
| UID |  Spot order placement and cancellation.  
Trade history and fee rates.  
  
Perpetual Futures | Private endpoints |  The rate limit for batch/single order placement and amend an order are total of 100r/s  
The maximum rate limit for the order cancellation (bulk/single) is 200r/s  
The Others: 200r/10s per endpoint  
| UID |  Futures order placement and cancellation  
Trade history and fee rates  
  
Delivery | Private endpoints |  The maximum rate limit for the order placement (bulk/single) is 500r/10s  
The maximum rate limit for the order cancellation (bulk/single) is 500r/10s  
The Others: 200r/10s per endpoint  
| UID |  Order placement and cancellation  
  
Options | Private endpoints |  The maximum rate limit for the order placement (bulk/single) is 200r/s  
The maximum rate limit for the order cancellation (bulk/single) is 200r/s  
The Others: 200r/10s per endpoint  
| UID |  Order placement and cancellation  
  
Subaccount | Private endpoints |  80r/10s per endpoint  | UID |  Create a sub-account.  
Retrieve the list of sub-accounts.  
Disable or enable API key for a sub-account.  
  
Unified | Private endpoints |  Borrow or repay 15/10s  | UID |  Borrow or repay(POST /unified/loans)  
  
Other Private endpoints | Private endpoints |  150r/10s per endpoint  | UID |  Earning, collateral etc   
  
> The rate limit is counted against each sub-account or main account.

**Rate Limit**

Each request to the API response header will contain the following fields:：

  * X-Gate-RateLimit-Requests-Remain - your remaining requests for current endpoint
  * X-Gate-RateLimit-Limit - your current limit for current endpoint
  * X-Gate-RateLimit-Reset-Timestamp - the timestamp indicating when your request limit resets if you have exceeded your rate_limit. Otherwise, this is just the current timestamp (it may not exactly match timeNow).

WebSocket:

  * Spot: Bulk order/single order/single order modification, a total of 10 requests per second (10r/s).
  * Futures: Bulk order/single order/single order modification/single order cancellation/bulk cancellation, a total of 100 requests per second (100r/s).
  * Others: No limit.
  * Number of connections per IP: ≤ 300

##  Rate Limit Based On Fill Ratio

In order to enhance trading efficiency, we have decided to implement more favorable sub-account rate limits for clients with a higher fill ratio. This assessment will be based on trading data from the past seven days and will be calculated daily at 00:00 UTC. Please note that this rule applies only to clients at **VIP level 14 and above**.

###  1\. Introduction of Terminology

####  1.1 Symbol Multiplier

To facilitate a more refined management of the impact of different trading products on the fill ratio, we have introduced the concept of the symbol multiplier. This multiplier allows us to adjust the influence of each product on the overall trading volume based on its characteristics. For products with a multiplier of less than 1, they typically involve smaller contract sizes and therefore require more trading orders to achieve the same trading volume. Generally, all trading products come with a default multiplier; however, certain products are assigned independent multipliers based on their specific characteristics. For detailed information regarding the multipliers of relevant products, please refer to the provided table.

1.1 Symbol MultiplierProduct Typee | Based On | Independnet Symbol Multiplier | Default Symbol Multiplier  
---|---|---|---  
USDT-Margined Perpetural Futures | Contract Symbol |  1  
Contract Symbol:  
BTC-USDT  
ETH-USDT  | 0.4  
Spot | Currency Pairst |  1  
Currency Pairs:  
BTC-USDT  
ETH-USDT  | 0.4  
  
> Please note: The spot trading rate limits will not be launched this time.

####  1.2 Definition of Trading Volume Weight

We will assess the behavior patterns of makers and takers based on market fluctuations and design the trading volume weight ratios accordingly. Additionally, we will regularly evaluate these weights and make synchronized adjustments when necessary.

**Current weight of the maker trading volume: 100%, current weight of the taker trading volume: 90%.**

####  1.3 Calculation Formula

The system will take a snapshot of the data at 00:00 UTC daily and, based on this information, will select the higher value between the fill ratio of the sub-account and the overall fill ratio of the main account to determine the future trading rate limit for the sub-account. For exchange brokers, the system will only consider the fill ratio of their sub-accounts. It is important to note that the main account is also considered a "sub-account."

  1. Sub-account Fill Ratio: This ratio is calculated as follows: (Sub-account Taker's USDT trading volume × 0.9 + Maker's USDT trading volume × 1) / (The sum of (Number of new and modified requests for each contract × symbol multipliers) for each subaccount).
  2. Main-account Aggregated Fill Ratio: This ratio is calculated as follows: (main account's Taker USDT trading volume × 0.9 + Maker USDT trading volume × 1) / (The sum of (Number of new and modified requests for each contract × symbol multipliers) for all subaccounts).

###  2\. Spot Rate Limit Rules

####  2.1 Existing Rate Limit Rules

The rate limit for batch/single order placement and order modification is a total of 10r/s (UID+Market)

  * The same UID has a rate limit of 10r/s across different markets, and the rate limits for different spot markets are independent of each other.

####  2.2 New Rate Limit Rules

The platform will implement rate limiting for trading behaviors that frequently place orders, cancel orders, or modify orders within a short period but exhibit a low fill ratio. The specific rules are as follows:

**1\. Statistics Period**

  * Statistics Period: Statistics are calculated based on data from the last 24 hours, with calculations performed once per hour.

**2\. Request Types**

  * Statistics Items: All requests are counted, including both successful and failed requests for order placement, cancellation, and modification (such as immediate order fills, insufficient funds, etc.).

**3\. Rate Limit Standards**

  * Rate limiting is applied to two API endpoints: order placement (POST /spot/orders) and order modification (PATCH /spot/orders/{order_id}). Based on UID, the rate limit is set to no more than 10 requests per 10 seconds. We recommend maintaining a fill ratio above 0.1.

**4\. Unlock Mechanism**

  * The system will dynamically evaluate users' trading behavior. During the hourly assessment, once the system detects that users have adjusted their trading strategies and meet our trading efficiency requirements, the restrictions will be lifted.

**Note:**

  * The system calculates the fill ratio for the last 24 hours every hour, with a minimum restriction period of one hour. If a user is restricted in the current hour, the fill ratio is recalculated once per hour. If the fill ratio in the current hour exceeds the threshold, the restriction will be lifted in the next hour.

####  2.3 Fill Ratio Calculation Formula

Fill Ratio = USDT Trading Amount / (Total Number of Order Placement, Cancellation, and Modification Requests)

###  3\. Future Rate Limit Rule

3\. Future Rate Limit RuleContract Frequency Limitation Rules  
---  
Tier | Ratio | Rate Limit (uid)  
Tier 1 | [0,1) | 100r/s  
Tier 2 | [1,3) | 150r/s  
Tier 3 | [3,5) | 200r/s  
Tier 4 | [5,10) | 250r/s  
Tier 5 | [10,20) | 300r/s  
Tier 6 | [20,50) | 350r/s  
Tier 7 | >= 50 | 400r/s  
  
> > Please stay tuned for the rate limits for spot trading.

###  4\. Detailed Rules for Fill Ratio

  1. Target Client Group: VIP ≥ 14
  2. Calculation Period: 7 days
  3. Update Time: Daily at 08:00 (UTC). The system will update the fill ratio data based on the data from 00:00 UTC. 
     1. If the fill ratio and the pre-set rate limit improve, the increase will take effect immediately at 08:00 (UTC).
     2. However, if the fill ratio declines, the rate limit will be reduced immediately.
     3. If a client's VIP level drops below VIP 14, their rate limit will be lowered to the minimum tier, taking effect immediately.
     4. If a client's VIP level rises above VIP 14, their rate limit will be adjusted immediately based on their current level.
     5. If a sub-account's trading volume over the past 7 days is below 1,000,000 USDT, the rate limit will be implemented based on the main-account aggregated fill ratio.
     6. For newly created sub-accounts, the minimum tier rate limit will be applied at the time of creation, and the aforementioned rate limit rules will begin to apply at T+1 08:00 (UTC).
     7. Both WebSocket and REST APIs are subject to these rules.

###  5\. Example

Assuming the client has three accounts, with the symbol multipliers for trading perpetual contract products BTC-USDT and SOL-USDT being 1 and 0.4, respectively.

  1. Account A (Main Account): 
     * BTC-USDT perpetual futures Maker trading volume: 100 USDT, number of order requests: 10; Perpetual futures Taker trading volume: 200 USDT, number of order requests: 20.
     * SOL-USDT perpetual futures Maker trading volume: 20 USDT, number of order requests: 15; Perpetual futures Taker trading volume: 20 USDT, number of order requests: 20.
     * Sub-account Fill Ratio = ((100 + 20) * 1 + (200 + 20) * 0.9) / ((10 + 20) * 1 + (15 + 20) * 0.4) = 7.23
  2. Account B (Sub-account): 
     * BTC-USDT perpetual futures Maker trading volume: 200 USDT, number of order requests: 20; Perpetual futures Taker trading volume: 200 USDT, number of order requests: 30.
     * SOL-USDT perpetual futures Maker trading volume: 20 USDT, number of order requests: 5; Perpetual futures Taker trading volume: 30 USDT, number of order requests: 5.
     * Sub-account Fill Ratio = ((200 + 20) * 1 + (200 + 30) * 0.9) / ((20 + 30) * 1 + (5 + 5) * 0.4) = 7.91
  3. Account C (Sub-account): 
     * BTC-USDT perpetual futures Maker trading volume: 50 USDT, number of order requests: 5; Perpetual futures Taker trading volume: 60 USDT, number of order requests: 8.
     * SOL-USDT perpetual futures Maker trading volume: 100 USDT, number of order requests: 20; Perpetual futures Taker trading volume: 120 USDT, number of order requests: 25.
     * Sub-account Fill Ratio = ((50 + 100) * 1 + (60 + 120) * 0.9) / ((5 + 8) * 1 + (20 + 25) * 0.4) = 10.06
  4. Main Account Aggregated Fill Ratio = ((100 + 20 + 200 + 20 + 50 + 100) * 1 + (200 + 20 + 200 + 30 + 60 + 120) * 0.9) / ((10 + 20 + 20 + 30 + 5 + 8) * 1 + (15 + 20 + 5 + 5 + 20 + 25) * 0.4) = 8.19
  5. Account Rate Limits: 
     * Account A = max(7.23, 8.19) = 8.19 -> 250 r/s
     * Account B = max(7.91, 8.19) = 8.19 -> 250 r/s
     * Account C = max(10.06, 8.19) = 10.06 -> 300 r/s

###  6\. Remarks

  1. The release date for the rate limit of perpetual contracts based on fill ratio will be announced later. Please stay tuned.
  2. The existing abuse rate limit rules for perpetual contracts will still apply, namely: 
     1. Fill Ratio = USDT Training Amount / (Total Number of Order, Cancellation, and Modification Requests)
     2. If the number of requests exceeds 86,400 within 24 hours, with no order fill in the same period. Then the order placement rate limit will be restricted to 10r/10s for the next hour.
     3. If the number of requests exceeds 86,400 within 24 hours, with the fill ratio below 1%. Then the order placement rate limit will be restricted to 20r/10s for the next hour.
  3. Please stay tuned for the fill ratio rate limit for spot trading.

##  Return Format

All API responses are in JSON format, and users need to transform and extract data by themselves.

The HTTP status code 2XX will be returned when all operations are successful. 401 indicates that there is a problem with the certification. Other 4xx status codes indicate that the request is invalid. If it is a 5xx error, the server has encountered an unknown serious error when processing the request. Please give feedback as soon as possible。

**Return Status**

Return FormatStatus Code | Description  
---|---  
200/201 | Request succeeded  
202 | Request accepted by the server, but processing is not done yet  
204 | Request succeeded, but the server doesn't return body  
400 | Invalid request  
401 | Authentication failed  
404 | Not found  
429 | Too many requests  
5xx | Server error  
  
##  Data Type

Data TypeType | Description  
---|---  
`string` | String type, in double quotation marks. Price and amount are also formatted in string format  
`integer` | 32-bit integer，Mainly related to status codes, size, times, etc.  
`integer(int64)` | 64-bit integer，Mainly involves ID and higher precision timestamp  
`float` | Floating point number. Some time and stat fields use float.  
`object` | Object，Contains a child object{}  
`array` | List，Includes multiple groups of content  
`boolean` | true is true，false is false  
  
##  Portfolio Margin Account

TIP

The Portfolio Margin Account is no longer maintained, please refer to the new version of the Unified Account

Since version `4.25.0`, we start supporting portfolio margin account. Gate's Portfolio Margin Account is a new feature of Gate's trading system. Its main function is to break the capital isolation between cross-margin leverage account and USD cross-margin perpetual contract account inside a Classic Account and achieve the multi-currency margin sharing among multi-product lines. Thanks to the margin sharing, users don't need to transfer funds between the two accounts, and the profit and loss of positions among different trading products can offset each other and effectively improve the capital utilization rate. See more details in the [ Help Center](/help/trade/leveraged/26421/introductions-to-gate.io-s-portfolio-margin-account)

Before using the portfolio margin account's API key, you should create the API key on the API management page. The API key supports spot and perpetual contracts trading only.

> If permissions of the API key can't be checked, ensure your cross-margin account has available balance first.

###  Transfer

The classic account and portfolio margin account are two different capital isolation accounts. If you want to achieve multi-currency margin sharing among multi-product lines, use the portfolio margin account please.

The funds of the portfolio margin account come from the classic account. Due to the change of funds in the classic account, the transfer of funds can only be performed using the API Key of the classic account.

The portfolio margin account is upgraded based on the cross-margin account of the original classic account, so the classic account only needs to transfer its spot funds to the cross-margin account to deposit the portfolio margin account. Similarly, withdrawals from portfolio margin account can be achieved by the classic account performing transferals from the cross margin to its spot account.

The API Key of the portfolio margin account can only perform transferals among its own multiple accounts. Due to the sharing of margin, the portfolio margin account does not need to transfer funds to its futures account (we also restrict doing so). If the futures account has PNL funds that need to be withdrawn, it must be transferred by the portfolio margin account's API key to its cross-margin account first, so that the classic account can perform withdrawals from portfolio margin account.

###  Spot trading

The spot trading of the portfolio margin account is almost the same as the classic account, except that `cross_margin` must be specified in the `account` parameter when placing orders. For example, if you want to place a buy order for the `BTC_USDT` currency pair, the order request will be similar to
    
    
    POST /spot/orders
    
    {
      "currency_pair": "BTC_USDT",
      "account": "cross_margin",
      "side": "buy",
      ...
    }
    

For other related restrictions, please refer to the document of the API endpoint directly.

TIP

It should be noted that the portfolio margin account is upgraded from the classic account's cross-margin account. The API Key of the classic account originally supports the operation of the cross-margin account. In order not to affect the existing operations of the classic account, we still retain this function of the classic account. So whether it is the API Key of the classic account or the portfolio margin account, both can operate the same the cross margin account (note that the futures accounts are separate)

###  Futures trading

The API operation of the perpetual contract of the portfolio margin account is exactly the same as that of the classic account, but currently only supports USD settlement

TIP

In the futures trading, it should be noted that there is no compatibility for cross-margin accounts like using the API Key of the classic account in spot trading. Therefore, when using the API Key of the classic account for futures trading, assets are kept under `classic account-futures`, and when using portfolio margin account API Key for futures trading, assets are kept under `portfolio margin account-futures`. These two are different futures accounts. In addition, funds under `classic account-spot` cannot share margin with `classic account-futures`.

##  Trace ID

The API response will carry the header: X-Gate-Trace-ID . This header is used for tracking.

##  Self-Trade Prevention (STP)

###  Concepts

**Self-Trade Prevention** : STP will prevent any user's orders from being matched with each other.

**CN** : Cancel new, Cancel new orders and keep old ones.

**CO** : Cancel old, Cancel old orders and keep new ones.

**CB** : Cancel both, Both old and new orders will be cancelled.

###  STP Strategies

We support three STP strategies, which are `CN` , `CO` and `CB`.

STP is achieved by adding users to one STP trading group. When a user in a STP group place orders, and trading could happen with existing orders of users in the same group, orders will be cancelled. The prevention strategy depends on the `stp_act` parameter specified when placing the order as taker. If not specified, the `CN` strategy will be used by default.

A user has to be added to a STP trading group before using STP. When a user does not belong to any STP trading group, and place orders with the `stp_act` parameter, the orders will be rejected.

###  API Parameter Adjustment

Take placing futures order as an example:
    
    
    POST /futures/{settle}/orders
    

New request body parameter:

API Parameter AdjustmentName | Position | Type | Required | Description  
---|---|---|---|---  
stp_act | body | string | Optional | STP Strategies, including:   
\- cn  
\- co  
\- cb  
  
New response fields:

API Parameter AdjustmentName | Type | Required | Restriction | Description  
---|---|---|---|---  
stp_act | string | Optional | none | STP Strategies, including：  
\- cn  
\- co  
\- cb  
stp_id | integer(int64) | Optional | readonly | The ID of the STP trading group to which user belongs.  
finish_as | string | Optional | readonly | order finish type:   
\- **stp: The order has been canceled due to the`STP`**  
  
###  User case

There are multiple accounts under `Organization A`, and the IDs of several accounts are `101`, `102`, and `103`

In order to prevent self-trading of orders placed by internal accounts of the organization, the administrator created a STP trading group with group ID `100`, and added accounts `101` and `102` to the STP trading group. In this case, the members in the group are `[101,102]`.

T1: The `STP` strategy version released.

T2: After the `organization A` account `101` places a short order, there is no matching order in the market order book to match the transaction. At this time, the role of the order is `maker`, and the order status is `open`. The key response fields returned are:
    
    
    {
    	"status":"open",
    	"stp_act":"cn",
    	"stp_id":100
    }
    

T3: `Organization A` account `101`/`102` places a long order, and it can reach a trade with account 101’s short order. The match engine finds both two orders' stp_id are 100, so it applies the STP strategy of the taker order, which defaults to `cn` , and cancels the long order. Order's `finish_as` will be set to `stp`. The key response fields returned are:
    
    
    {
    	"status":"finished",
    	"stp_act":"cn",
    	"stp_id":100,
    	"finish_as":"stp"
    }
    

  * If `stp_act` is `co` , the order placed by `taker` will be retained, the order status will be `open`, and the system will cancel the order of `maker`.

  * If `stp_act` is `cb`, both the long and short orders will be cancelled. Orders' `finish_as` will be set to `stp`. The key response fields returned are:

    
    
    {
    	"status":"finished",
    	"stp_act":"cb",
    	"stp_id":100,
    	"finish_as":"stp"
    }
    

T3': If account 103 places a long order, and it can reach a trade with account 101’s short order, the transaction will be made since account 103 has not been added to account 101’s STP group. The key response fields returned are:
    
    
    {
    	"status":"finished",
    	"stp_id":0,
    	"finish_as":"filled"
    }
    

##  Unified Account

###  Description

Once a user upgrades their account to the unified account, they can utilize the assets from their spot account as collateral for trading. The assets in the account, denominated in various currencies, will be adjusted based on their liquidity and converted to USD for consistent calculation of the account's assets and position value.

The maximum borrowing limit for margin trading represents the maximum amount that a user can borrow for a given trading market. The platform calculates the user's maximum borrowing limit based on factors such as available margin and platform risk control rules. Once the margin trading generates automatic borrowing, the platform immediately starts accruing interest on the borrowed digital assets.

Currently, the ability to switch to `cross_margin` or`usdt_futures` mode is available. In the future, we will gradually introduce support for various combination margin accounts, including `Futures`, `Delivery`, `Options` and more. Stay tuned for further updates.

Please refer to the documentation for unified API. Once you have upgraded your account, you will be able to make use of these endpoints.

Related endpoint can be found in the Unified Account API doc. After enabling the Unified Account, you can proceed to call them. For more detailed information, please refer to [here](https://www.gate.com/unified-trading-account)

###  API Integration Process

  * Create a new `API KEY` or update the permissions of an existing `API KEY`, checking the `unified` permission
  * Use the classic account's `API KEY` to call the `PUT /unified/unified_mode` endpoint, or upgrade from the WEB page to the Unified Account
  * Use the `/api/v4/spot/**` API for spot-related operations (ordering, modifying orders, querying orders), with the `account=unified` option
  * Use the `/api/v4/futures/**` API for perpetual futures-related operations (ordering, modifying orders, querying orders)
  * Use the `/api/v4/unified/**` API for Unified Account-related operations (account querying, loan querying)

###  SPOT Trading

The spot trading in the Unified Account is consistent with that in the classical account. In order operations, specify `account=unified`, or specify `account=spot` and the system will automatically handle the order as a unified account order when detecting the account as a unified account. For example, to place a buy order for the `BTC_USDT` currency pair, the order creation request would be similar to
    
    
    POST /spot/orders
    
    {
      "currency_pair": "BTC_USDT",
      "account": "unified",
      "side": "buy",
      ...
    }
    

For other related restrictions, please refer to the document of the API endpoint directly.

###  Formula

FormulaName | Cross Margin  
---|---  
portfolio_margin_total_equity | Account Equity = ∑(Equity * Index Price）  
total_margin_balance | Account Margin Balance = ∑(Positive Equity x Index Price x Adjustment Factor) + ∑(Negative Equity x Index Price) - Haircut Loss  
total_initial_margin_rate | Account Initial Margin Level = Account Margin Balance / Account Initial Margin  
total_maintenance_margin_rate | Account Maintenance Margin Level = Account Margin Balance / Account Maintenance Margin  
total_initial_margin | Account Initial Margin = Total Liabilities x Spot Initial Margin Rate  
total_maintenance_margin | Account Maintenance Margin = Total Liabilities x Spot Maintenance Margin Rate  
equity | Equity = Coin Balance - Borrowed  
available | Available Balance = Principal + Borrowed  
freeze | Occupied = Assets Occupied by Spot Open Orders  
  
##  AccountBook type

###  General

  * unknown: Unknown
  * login: Log In
  * withdraw: Withdrawals
  * ch_pass: Change Password
  * ch_fund_pass: Change Fund Pass
  * login_failed: Login Failed
  * axs_account: Access Account
  * req_pass_ch: Request Password Change
  * req_fund_pass_ch: Request Fund Pass Change
  * fund_pass_ent: Fund Pass Entered
  * bank_card_add: Bank Card Added
  * frw: Face Recognition For Withdrawal

###  Order

  * new_order: Order Placed
  * cancel_order: Order Cancelled
  * order_fill: Order Filled
  * order_rej: Order Rejected
  * order_fee: Trading Fees
  * system_fee: Trading Fee System Account

###  Withdraw-Deposit

  * withdraw: Withdrawals
  * deposit: Deposits
  * deposit_rej: Deposit Rejected
  * withdraw_rej: Withdrawal Rejected
  * cancel_withdraw: Cancel Withdrawal
  * withdraw_gatecode: GateCode Withdrawals
  * withdraw_fireblock: Fireblocks Withdrawals
  * withdraw_copper: Copper Withdrawals
  * startup_withdraw: Token Withdrawal From Startup
  * deposit_gatecode: GateCode Deposits
  * deposit_fireblock: Fireblocks Deposits
  * deposit_copper: Copper Deposits
  * buy_cl: Buy Crypto Legend
  * buy_cc: Buy Crypto Cabital
  * deposit_finmo: Gate connect Finmo Deposit

###  Startup

  * startup_prtcp: Startup Sale Participation
  * startup_refund: Startup Sale Refund
  * startup_sale: Startup Sale
  * startup_sale_rb: Startup Sale Rolled Back

###  Rebate

  * referral_rebate: Referral Superior Rebate
  * sec_rebate_out: Secondary Rebate Financial Account Transfer Out
  * sec_rebate_in: Affiliate Indirect Superior Rebate Income
  * ab_rebate: API Broker Rebate Income
  * eb_rebate: Exchange Broker Rebate Income
  * u_rebate: Referral Rebate Income
  * ads_rebate: Affiliate Direct Superior Rebate Income
  * au_rebate: Affiliate User Rebate Income
  * pis_rebate: Partner Indirect Superior Rebate Income
  * pds_rebate: Partner Direct Superior Rebate Income
  * pu_rebate: Partner User Rebate Income

###  Convert

  * eth_swap: ETH Swap
  * dust_swap_dctd: Dust Swap-Small Balances Deducted
  * dust_swap_gt_add: Dust Swap-GT Added
  * dust_swap_fee: Dust Swap-Fees Deducted
  * cv_buy: Quick Buy-Bought
  * cv_sell: Quick Sell-Sold

###  C2C

  * c2c_mop: C2C Merchant Order Placed
  * c2c_moc: C2C Merchant Order Canceled
  * c2c_rop: C2C Retail Order Placed
  * c2c_roc: C2C Retail Order Canceled
  * c2c_om: C2C Order Matched
  * c2c_or: C2C Order Rejected
  * c2c_fee: C2C Fees

###  Reward

  * deposit_bonus: Deposit Bonus
  * trading_rewards: Trading Rewards
  * purchase_bonus: Purchase Bonus
  * airdrop: Airdrop
  * award: Award
  * mining_rewards: Mining Rewards

###  Account Transfer In-Out

  * margin_in: Isolated Margin-Transferred In
  * margin_out: Isolated Margin- Transferred Out
  * spot_settle_out: Spot Settlement Transfer Out
  * spot_settle_in: Spot Settlement Transfer Out
  * lending_in: Lending-Transferred In
  * lending_out: Lending-Transferred Out
  * cross_in: PortfolioMarginAccountTransferIn
  * cross_out: PortfolioMarginAccountTransferOut
  * perp_in: Perps- Transferred In
  * perp_out: Perps- Transferred Out
  * perp_settle_in: Perpetual Multi-currency Settlement Transfer In
  * perp_settle_out: Perpetual Multi-currency Settlement Transfer Out
  * delivery_in: Delivery- Transferred In
  * delivery_out: Delivery- Transferred Out
  * ai_in: Auto-Invest-Transferred In
  * ai_out: Auto-Invest-Transferred Out
  * e_options_in: Easy Options- Transferred In
  * e_options_out: Easy Options- Transferred Out
  * options_in: Options- Transferred In
  * options_out: Options- Transferred Out
  * cbbc_in: CBBC- Transferred In
  * cbbc_out: CBBC- Transferred Out
  * warrant_in: Warrant- Transferred In
  * warrant_out: Warrant- Transferred Out
  * subaccount_trf: Subaccount Transfer
  * quant_in: Quant- Transferred In
  * quant_out: Quant- Transferred Out
  * pay_in: Payment Account- Transferred In
  * pay_out: Payment Account- Transferred Out
  * fct_in: Futures Copy Trading - Funds Transfer In
  * fct_out: Futures Copy Trading - Funds Transfer Out

###  Points

  * points_purchase: Points Purchase
  * points_expiration: Points With Expiration
  * points_trf: Points Transfer
  * points_trf_rej: Points Transfer Rejected

###  Finance

  * lending_lent: Lending-Lent
  * collected: Collected
  * interest_in: Interest Income
  * lending_fee: Lending-Fees Deducted
  * hodl_int: HODL Interest
  * redeem: Redeem
  * lend: Lend
  * dual_purchased: Dual C-Purchased
  * dual_settled: Dual C-Settled
  * liq_add: Liquidity Added
  * liq_rm: Liquidity Removed
  * liq_rebalanced: Liquidity Rebalanced
  * slot_int_in: Slot Auction Staking Interest Income
  * str_int_in: Structured Products Staking Interest Income

###  Loan

  * borrow: Borrow
  * repay: Repay
  * margin_borrow: Isolated Margin-Transferred In
  * margin_repay: Isolated Margin- Transferred Out
  * margin_interest_out: Isolated Margin-Interest Deduction
  * cl_borrow: Cryptoloan- Borrowed
  * cl_repay: Cryptoloan- Repaid
  * cl_dctd: Cryptoloan- Collateral Deducted
  * cl_rtd: Cryptoloan- Collateral Returned
  * cross_borrow: PortfolioMarginAccountBorrowIn
  * cross_repay: PortfolioMarginAccountRepay
  * interest_out: Interest

###  Moments

  * donation: Donation
  * rp_sent: Red Packet Sent
  * rp_rcvd: Red Packet Received
  * rp_rej: Red Packet Rejected
  * ls_offered: Live Stream-Reward Offered
  * ls_rcvd: Live Stream- Reward Received
  * pt_offered: Posts- Reward Offered
  * pt_rcvd: Posts- Reward Received
  * subs_deduct: Subscription-Fees Deducted
  * subs_in: Subscription-Fees Received
  * subs_refund: Subscription- Refund
  * subs_in_rcvd: Subscription- Refunds Received

###  PUSH Trading

  * push_dctd: Push- Deduction
  * push_rcvd_dctd: Push- Received-Deducted
  * push_canceled: Push Canceled
  * push_rej: Push Rejected
  * push_sent: Push Sent
  * push_rcvd: Push Received

###  Copy Trading

  * quant_return: Quant- Transaction Returned
  * quant_cmn_in: Quant-Commission Transferred In
  * quant_cmn_out: Quant-Commission Transferred Out
  * quant_cmn_rtd: Quant-Commission Returned
  * fct_refund: Futures Copy Trading - Funds Auto Transfer Out
  * fct_rcvd: Futures Lead Trading - Performance Fee Received
  * fct_fee: Futures Copy Trading - Performance Fee Paid
  * fct_fee_refund: Futures Copy Trading - Performance Fee Refund

###  NFT

  * nft_mp: NFT Auction-Margin Paid
  * nft_bm: NFT Auction-Bid Made
  * nft_om: NFT Auction-Offer Made
  * ntf_mr: NFT Auction-Margin Returned
  * nft_amr: NFT Auction-Aborted-Margin rcvd
  * nft_ocb: NFT Auction-Order Canceled-Back
  * nft_fb: Fixed Price-Bought
  * nft_fs: Fixed Price-For Sale
  * nft_ob: NFT Make-Offer Bought
  * nft_os: NFT Make-Offer Sale
  * nft_cr: Cancel offer refund
  * nft_ir: Refund for invalid offer
  * nft_wf: Withdrawal service fee
  * nft_wfr: Withdrawal service fee
  * ntf_mf: Multi-copy creation service fee
  * ntf_mfr: Multi-copy creation service fee refund
  * ntf_royalty: Royalties
  * nft_cd: NFT Auction-Order Canceled-Deducted
  * nft_crd: NFT Auction-Order Canceled-Rotalty-Deducted
  * nft_cf: crowdfunding
  * nft_cfr: crowdfunding refund
  * nft_ammf: Nft-Amm Frozen
  * nft_ammw: Nft-Amm Withdraw
  * nft_ammdf: Nft-Amm Deal Fee
  * nft_ammd: Nft-Amm Deal

##  AccountBook code

###  Assets

####  C2C

  * 301 : P2P Merchant - Place Order
  * 302 : P2P Merchant Order Canceled
  * 303 : P2P User Sell
  * 304 : P2P Retail Order Canceled
  * 305 : P2P User Buy
  * 308 : P2P Fees
  * 309 : P2P Deposit Freeze
  * 310 : P2P Deposit Refund
  * 311 : P2P Deposit Forfeiture
  * 312 : P2P Shared Asset Order Refund
  * 313 : P2P Frozen Funds
  * 314 : P2P Unfrozen Funds
  * 315 : P2P Express Convert Buy
  * 110106 : P2P Merchant Security Deposit Earnings

####  Deposit

  * 110 : Onchain Deposit
  * 121 : GateCode Deposits
  * 122 : Fireblocks Deposits
  * 123 : Wrongdeposit Fee
  * 124 : copper deposit
  * 125 : Asset Recovery Fee Refund
  * 1907 : Push- Sent
  * 1908 : Phone/Email/UID Deposit
  * 2650 : Bitgo Deposit
  * 5107 :

####  Convert

  * 1301 : Dust Swap-Small Balances Deducted
  * 1302 : Dust Swap-GT Added
  * 1307 : Dust Swap-Small Balances Deducted
  * 1310 : Dust Swap-Small Balances Deducted
  * 1322 : Convert Small Balance (USDT)
  * 1323 : Convert Small Balance - USDT Added
  * 2601 : Buy
  * 2602 : Sell
  * 2603 : Repay All - Transfer Out
  * 2604 : Repay All - Transfer In
  * 2605 : Buy
  * 2606 : Sell
  * 2612 : Buy
  * 2613 : Sell
  * 2615 : OTC-Deal
  * 2616 : OTC-Deal

####  Others

  * 106 : Donation
  * 115 : Snapshot
  * 118 : Rebasing
  * 131 : Call Auction- Locked
  * 132 : Call Auction- Unlocked
  * 141 : ETF Asset Consolidation - Deduction
  * 142 : ETF Asset Consolidation - Addition
  * 143 : Debit After Coin Name Change
  * 144 : Credit After Coin Name Change
  * 181 : ETH Swap
  * 182 : ETH2 Swap
  * 329 : Gate Connect-Refund
  * 330 : Gate Connect-Buy
  * 331 : Gate Connect-Sell
  * 501 : IFO Claimed
  * 502 : IFO Returned
  * 801 : Send Gift Coins
  * 802 : Receive Gift Coins
  * 803 : Gift Coin Refund
  * 804 : Live Stream - Reward Streamer
  * 805 : Live Stream - Get Rewarded
  * 806 : Moments - Reward User
  * 807 : Moments - Get Rewarded
  * 903 : Time-Limited Points
  * 913 : Redeemed Points
  * 915 : Redeemed Points - Refund
  * 917 : Points Expired Recycled
  * 1001 : Fiat Loan - Post Ads
  * 1002 : Fiat Loan - Cancel Ads
  * 1003 : Fiat Loan - Place Orders
  * 1004 : Fiat Loan - Repay
  * 1005 : Fiat Loan - Cancel Orders
  * 1006 : Fiat Loan - Trading Fee
  * 1007 : Fiat Loan - Liquidation
  * 1008 : Fiat Loan - Add Collateral
  * 1311 : Dust Swap-Small Balances Deducted
  * 1312 : Small Balance Convert - USDT Added
  * 1501 : Subscription Deduction
  * 1502 : Subscription Received
  * 1503 : Subscription Refund
  * 1504 : Subscription Refund Received
  * 2950 : BUGSFUNDED Registration Fee
  * 2951 : BUGSFUNDED Registration Fee Refund
  * 2952 : BUGSFUNDED Trading Funds - Deduction
  * 2953 : BUGSFUNDED Profit Transfer Out
  * 2954 : BUGSFUNDED Profit Transfer In
  * 2956 : BUGSFUNDED Trading Funds - Deposit
  * 2970 : PUMP Sale - Refund
  * 2971 : PUMP Sale - Token Release
  * 2972 : PUMP Sale - Payment Deduction
  * 3701 : OTC trade - buy
  * 3702 : OTC trade - sell
  * 3703 : OTC trade - cancel
  * 5104 : Fireblocks Fee Refund
  * 5105 : Prepaid Gas Fee
  * 5106 : Refund for Prepaid Gas Fee
  * 100101 : Transfer Out of Residual Balance from Closed Positions
  * 100102 : Transfer In of Residual Balance from Closed Positions
  * 110101 : Low-liquidity token withdrawal fee refund
  * 110102 : Low-liquidity token withdrawal fee
  * 130101 : Create token
  * 130102 : Refund issued for failed token creation
  * 130111 : KOL Token Non-Launch Refund
  * 130112 : KOL Token Oversubscription Refund
  * 130113 : KOL Token Redemption
  * 130114 : KOL Token Subscription
  * 130115 : KOL Token on-chain transaction fee
  * 130118 : Refund for KOL Token On-Chain Fee
  * 130119 : Refund for Failed KOL Token Subscription
  * 150101 : Currency Buyback-Credit
  * 150102 : Currency Buyback-Debit
  * 150201 : Borrow Mapped Assets
  * 150202 : Repay Mapped Assets
  * 150203 : Transfer In
  * 150204 : Transfer Out
  * 150208 :
  * 180101 : Refund for Alpha Token Delisting

####  Transfer

  * 601 : Transfer to Margin
  * 602 : Transfer from Margin
  * 701 : Transfer to Perpetual Futures
  * 702 : Transfer from Perpetual Futures
  * 703 : Transfer to Delivery Futures
  * 704 : Transfer from Delivery Futures
  * 1401 : Subaccount Transfer
  * 150215 : Subaccount Transfer
  * 150216 : Subaccount Transfer
  * 150217 : Subaccount Transfer
  * 150218 : Subaccount Transfer
  * 150219 : Subaccount Transfer
  * 1603 : Transfer to Options
  * 1604 : Transfer from Options
  * 3001 : Transfer to Payment
  * 3008 : Transfer from Payment
  * 3028 : Payment Account Transfer (Refund)
  * 100202 : Transfer to TradFi Account
  * 170201 : Transfer from Cross-Exchange Account
  * 170204 : Transfer to Cross-Exchange Account

####  Reward

  * 120102 : Futures Points Airdrop

####  Withdrawal

  * 4 : Onchain Withdraw
  * 17 : GateCode Withdraw
  * 18 : Fireblocks Withdrawals
  * 19 : copper withdraw
  * 104 : Cancel Onchain Withdrawal
  * 1901 : Phone/Email/UID Withdrawal
  * 1903 : Push- Received-Deducted
  * 1905 : Phone/Email/UID Withdrawal Cancellation
  * 1906 : Phone/Email/UID Withdrawal Refund
  * 2651 : Bitgo Withdraw

####  Payment

  * 2609 : Buy
  * 2610 : Sell
  * 2611 : Convert Refund
  * 3001 : Transfer to Payment
  * 3017 :
  * 3018 : Transfer (payout)
  * 3019 : Fiat Withdrawal
  * 3020 : Refund for Fiat Withdrawal
  * 3024 :
  * 3026 : Receive
  * 3027 : Refund
  * 3519 : Gift card - creation
  * 3520 : Gift card - redemption
  * 190101 : Settlement – Credit
  * 190301 : Awaiting acceptance
  * 190305 : completed
  * 190306 : Returned
  * 190307 : Canceled

####  Activity & Reward

  * 401 : Deposit Reward
  * 402 : Trading Reward
  * 403 : Purchase Reward
  * 404 : Airdrop Reward
  * 405 : Feedback Rewards
  * 3101 : Vouchers - Redeem Points
  * 3104 : Spot Token Airdrop
  * 3105 : Vouchers - Trading Fee Rebate
  * 3120 : Candydrop rewards
  * 3150 : Error in event token release
  * 3801 : Voucher Profit Transfer
  * 120101 : Futures Points Rewards
  * 140203 : Token Voucher Redemption
  * 140204 : Incentive Airdrop
  * 140205 : Unlock Incentive Airdrop
  * 140206 : Reclaim Incentive Airdrop
  * 140207 : Lock-Up Deduction

####  Block Trading

  * 3401 : Block Trading Transfer In
  * 3402 : Block Trading Transfer Out

####  Rebate

  * 109 : Referral Superior Rebate
  * 162 : Affiliate Indirect Superior Rebate Income
  * 164 : Affiliate Direct Superior Rebate Income
  * 166 : Affiliate User Rebate Income
  * 191 : Referral Rebate Income
  * 3301 : Affiliate Ultra Commission Rebate (Direct Senior)
  * 3321 : Affiliate Ultra Indirect Superior Rebate
  * 3341 : Affiliate Ultra Commission Self-Rebate
  * 3381 : Assessment Period Commission
  * 3390 : API Broker Rebate Income
  * 3410 : Exchange Broker Rebate Income
  * 4002 : Withdraw Commission
  * 4009 : Withdraw Rewards
  * 4011 : Deducted Negative Maker Fee

###  Trading

####  Options

  * dnw: Transfer In-Out
  * fee: Trading Fee
  * prem: Premium
  * refr: Referrer Rebate
  * set: Settlement Profit

####  Perpetual

  * bonus_dnw: Bonus Deposit-Withdrawal
  * bonus_offset: Bonus Offset
  * dnw: Transfer In-Out
  * fee: Trading Fee
  * fund: Funding Fee
  * pnl: Position P&L
  * point_convert: Points Convert
  * point_dnw: Points Transfer In-Out
  * point_fee: Points Trading Fee
  * point_refr: Points Referrer Rebate
  * pv_dnw: Experience Position Bonus Deposit-Withdrawal
  * refr: Referrer Rebate

####  Delivery

  * dnw: Transfer In-Out
  * fee: Trading Fee
  * pnl: Position P&L
  * point_dnw: Points Transfer In-Out
  * point_fee: Points Trading Fee
  * point_refr: Points Referrer Rebate
  * refr: Referrer Rebate
  * settle: Settlement
  * settle_fee: Settlement Fee

####  Alpha

  * 6001 : Place Order
  * 6002 : Place Order
  * 6003 : Successful Transaction
  * 6004 : Successful Transaction
  * 6005 : Failed Transaction
  * 6006 : Failed Transaction
  * 6007 : Trading Fee
  * 6010 : Alpha Airdrop
  * 6011 : Alpha Buy Order Canceled
  * 6012 : Alpha Buy Order Canceled
  * 130103 : Sell Alpha Tokens via Convert
  * 130104 : Buy Alpha Tokens via Convert
  * 130105 : Alpha Token Refund After Failing to Convert
  * 130106 : Sell Alpha Tokens via Convert
  * 130107 : Buy Alpha Tokens via Convert
  * 130108 : Alpha Token Refund After Failing to Convert

####  Trading Bot

  * 1701 : Bots - Transfer In
  * 1702 : Bots - Transferred Out
  * 1703 : Bots - Refund
  * 2401 : Bots - Performance Fee Received
  * 2402 : Bots - Performance Fee Paid
  * 2403 : Bots - Performance Fee Refund
  * 150210 : Options Bot Transfer In
  * 150211 : Options Bot Transfer Out

####  Margin Trading

  * 659 : Cross-Currency Repayment - Transfer In
  * 660 : Cross-Currency Repayment - Transfer Out
  * 670 : MarginTradingBorrowed
  * 671 : MarginTradingRepaid
  * 672 : MarginTradingInterest
  * 682 : Contributing Insurance Funds
  * 683 : Consuming Insurance Funds
  * 685 : Interest - Platform Loans

####  Spot

  * 101 : Sell
  * 102 : Buy
  * 151 : Trading Fees

####  Copy Trading

  * 3151 : Paid by Loss Coverage for Copier
  * 3201 : Futures Copy Trading - Transfer In
  * 3202 : Futures Copy Trading - Transfer Out
  * 3203 : Futures Copy Trading - Refund
  * 3204 : Futures Lead Trading - Performance Fee Received
  * 3205 : Futures Copy Trading - Performance Fee Paid
  * 3206 : Futures Copy Trading - Performance Fee Refund
  * 3601 : Spot Lead Trading - Funds Transfer In
  * 3602 : Spot Lead Trading - Funds Transfer Out
  * 3603 : Spot Lead Trading - Funds Auto Transfer Out
  * 3604 : Spot Copy Trading - Transfer In
  * 3605 : Spot Copy Trading - Transfer Out
  * 3606 : Spot Copy Trading - Refund
  * 3607 : Spot Lead Trading - Performance Fee Received
  * 3608 : Spot Copy Trading - Performance Fee Paid
  * 3609 : Spot Copy Trading - Performance Fee Refund
  * 210101 : Copy Bonus Reclaim
  * 210102 : Copy Bonus Issuance

####  Isolated Margin

  * 601 : Transfer to Margin
  * 602 : Transfer from Margin
  * 605 : Isolated Margin-Transferred In
  * 606 : Isolated Margin- Transferred Out
  * 616 : Liquidation Fee
  * 675 : Interest Updated
  * 676 : Isolated Margin-Interest Deduction

###  Finance

####  HODLer Airdrop

  * 2614 : HODLer Airdrop

####  Launchpad

  * 1134 : Launchpad Payments
  * 1135 : Launchpad Returns
  * 1136 : Launchpad Deposit
  * 1203 : Launchpad Lockup

####  Launchpool

  * 1174 : Bonus
  * 1251 : Stake
  * 1253 : Manually Redeem
  * 1255 : Reward
  * 1258 : Auto-Redeem

####  Simple Earn

  * 661 : Redemption - Flexible
  * 662 : Subscription - Flexible
  * 669 : Interest - Flexible
  * 681 : Bonus - Flexible
  * 686 : Subscription - Fixed-term
  * 687 : Redemption - Fixed-term
  * 688 : Interest - Fixed-term
  * 689 : Bonus - Fixed-term
  * 160301 : Fixed term interest
  * 160302 : Fixed term bonus
  * 160303 : Redemption of fixed term
  * 160304 : Fixed term subscribe
  * 160401 : Enhanced return - Fixed-term
  * 160402 : Fixed term enhanced return
  * 160406 : Boost Reward - Fixed Term

####  Dual Investment

  * 2001 : Dual Investment - Subscribe
  * 2004 : Dual Investment - Settlement
  * 2011 : Subscription to Dip Sniper products
  * 2012 : Recouped from expired Dip Sniper products
  * 2021 : Subscription to Peak Sniper products
  * 2022 : Recouped from expired Peak Sniper products
  * 160201 : Dual invest repayment at maturity
  * 160202 : Dual invest subscribe

####  Auto-Investment

  * 911 : Auto-Investment - Transfer Out
  * 912 : Auto-Investment - Transfer In

####  Collateral Loan

  * 635 : Fixed Rate Loan - Interest
  * 640 : Flexible Crypto Loan - Borrow
  * 641 : Flexible Crypto Loan - Repay
  * 642 : Flexible Crypto Loan - Liquidate to Repay Principal
  * 643 : Flexible Crypto Loan - Liquidate to Repay Interest
  * 644 : Flexible Crypto Loan - Interest
  * 645 : Pledge
  * 646 : Collateral Refund
  * 647 : Adjust Collateral
  * 648 : Refund after Liquidation
  * 649 : Liquidation Fee
  * 655 : Fixed Rate Loan - Borrow
  * 656 : Fixed Rate Loan - Repay
  * 657 : Fixed Rate Loan - Liquidate to Repay Principal
  * 658 : Fixed Rate Loan - Liquidate to Repay Interest
  * 696 : Early repayment penalty
  * 697 : Refund of early repayment penalty
  * 160601 : Redeemed Simple Earn Collateral After Liquidation–Deduction
  * 160602 : Simple Earn Collateral After Liquidation–Refund

####  Soft Staking

  * 120103 : Soft Staking–Futures
  * 160501 : Soft Staking–Spot

####  Leverage Protection

  * 160608 : Redemption at Maturity
  * 160609 : Subscription

####  Private Equity

  * 160101 : Repayment of private equity at maturity
  * 160102 : Private equity subscribe
  * 160103 : Manual redemption payment for private equity
  * 160104 : Interest of Private Equity

####  Third-Party Fund

  * 170101 : Third-Party Fund Subscription
  * 170111 : Third-Party Fund Redemption
  * 170112 : Third-Party Fund Settlement
  * 170113 : Refund for Failed Third-Party Fund Subscription
  * 170206 : Token Dividend Received from Third-Party Fund

####  Quant Fund

  * 739 : Gate Wealth Commission
  * 751 : Quant Fund - Lock
  * 753 : Quant Fund - Unlock
  * 754 : Quant Fund - Unlock Return

####  Earn on Chain

  * 1171 : Bonus
  * 1173 : Bonus
  * 1181 : Staking
  * 1184 : Redemption
  * 1186 : Interest
  * 1191 : Staking
  * 1194 : Redemption
  * 1196 : Interest
  * 160607 : Revoked Redemptions

##  Error Handling

For all abnormal requests, APIv4 will return non-2xx status code, with a response body in JSON format to explain the error.

The error response body follows a format like:
    
    
    {
      "label": "INVALID_PARAM_VALUE",
      "message": "Invalid parameter `text` with value: abc"
    }
    

  * `label`: denotes error type in `string` format. Its value are chosen from a certain list(see below). Programs can use `label` to identify and catch a specific error.
  * `message`(or `detail`): detailed error message. A longer explanation showing why the error is generated or how to avoid it. Its purpose is helping to better understand the API. Error handling mechanism with this field is highly **NOT** recommended.

Take Python [requests ](https://requests.readthedocs.io/en/latest/) for example, error handling can be written like:

> Following examples only deal with business-related errors. Network timeout or other common errors need to be handled separately:
    
    
    import requests
    
    r = requests.get("https://api.gateio.ws/api/v4/futures/btc/contracts/BTC_USD")
    try:
        r.raise_for_status()
    except requests.HTTPError:
        # catch 2xx errors, parse error message in body, and do something based on `label`
        if r.json()['label'] == 'xxx':
            print(r.json())
    

or with [Python SDK ](https://github.com/gate/gateapi-python):
    
    
    import json
    from gate_api import FuturesApi
    from gate_api.rest import ApiException
    
    api = FuturesApi()
    try:
        api.get_futures_contract(settle='btc', contract="BTC_USD")
    except ApiException as e:  # ApiException wraps whole error information, see implementation for details
        detail = json.loads(e.value.body)
        if detail['label'] == 'xxx':
            print(detail)
    

##  `label` list

  * Request parameter or format related

label list`label` | Meaning  
---|---  
INVALID_PARAM_VALUE | Invalid parameter value  
INVALID_PROTOCOL | Invalid parameter value  
INVALID_ARGUMENT | Invalid argument  
INVALID_REQUEST_BODY | Invalid request body  
MISSING_REQUIRED_PARAM | Missing required parameter  
BAD_REQUEST | Invalid request  
INVALID_CONTENT_TYPE | Invalid `Content-Type` header  
NOT_ACCEPTABLE | Invalid `Accept-` Header  
METHOD_NOT_ALLOWED | Request method is not allowed  
NOT_FOUND | Request URL not exists  
  
  * Authentication related

label list`label` | Meaning  
---|---  
INVALID_CREDENTIALS | Invalid credentials provided  
INVALID_KEY | Invalid API Key  
IP_FORBIDDEN | Request IP not in whitelist  
READ_ONLY | API key is read-only  
INVALID_SIGNATURE | Invalid signature  
MISSING_REQUIRED_HEADER | Missing required authentication header  
REQUEST_EXPIRED | Request `Timestamp` is far from the server time  
ACCOUNT_LOCKED | Account is locked  
FORBIDDEN | Account has no permission to request operation  
  
  * Wallet related

label list`label` | Meaning  
---|---  
SUB_ACCOUNT_NOT_FOUND | Sub account not found  
SUB_ACCOUNT_LOCKED | Sub account is locked  
MARGIN_BALANCE_EXCEPTION | Abnormal margin account  
MARGIN_TRANSFER_FAILED | Failed to transfer with margin account  
TOO_MUCH_FUTURES_AVAILABLE | Futures balance exceeds max allowed  
FUTURES_BALANCE_NOT_ENOUGH | Futures balance not enough  
ACCOUNT_EXCEPTION | Abnormal account  
SUB_ACCOUNT_TRANSFER_FAILED | Failed to transfer with sub account  
ADDRESS_NOT_USED | Address never being used in web console  
TOO_FAST | Withdrawing request exceeds frequency limit  
WITHDRAWAL_OVER_LIMIT | Withdrawal limit exceeded  
API_WITHDRAW_DISABLED | API withdrawal operation is disabled temporarily  
INVALID_WITHDRAW_ID | Invalid withdraw ID  
INVALID_WITHDRAW_CANCEL_STATUS | Cancelling withdrawal not allowed with current status  
DUPLICATE_REQUEST | Duplicate request  
ORDER_EXISTS | Order already exists, do not resubmit  
INVALID_CLIENT_ORDER_ID | The client_order_id is invalid  
  
  * Spot and margin trading related

label list`label` | Meaning  
---|---  
INVALID_PRECISION | Invalid precision  
INVALID_CURRENCY | Invalid currency  
INVALID_CURRENCY_PAIR | Invalid currency pair  
POC_FILL_IMMEDIATELY | Order would match and take immediately so it's cancelled  
ORDER_NOT_FOUND | Order not found  
ORDER_CLOSED | Order already closed  
ORDER_CANCELLED | Order already cancelled  
QUANTITY_NOT_ENOUGH | Amount is not enough  
BALANCE_NOT_ENOUGH | Balance is not enough  
MARGIN_NOT_SUPPORTED | Request currency pair doesn't provide margin trading  
MARGIN_BALANCE_NOT_ENOUGH | Margin balance is not enough  
AMOUNT_TOO_LITTLE | Amount does not reach minimum required  
AMOUNT_TOO_MUCH | Amount exceeds maximum allowed  
REPEATED_CREATION | Repeated creation  
LOAN_NOT_FOUND | Margin loan is not found  
LOAN_RECORD_NOT_FOUND | Margin loan record is not found  
NO_MATCHED_LOAN | No loan can match request borrow requirement  
NOT_MERGEABLE | Request loans cannot be merged  
NO_CHANGE | No change is made  
REPAY_TOO_MUCH | Repay more than required  
TOO_MANY_CURRENCY_PAIRS | Too many currency pairs in batch orders creation  
TOO_MANY_ORDERS | Too many orders in one currency pair in batch orders creation  
MIXED_ACCOUNT_TYPE | More than one account type is used in batch orders creation  
AUTO_BORROW_TOO_MUCH | Auto borrow exceeds maximum allowed  
TRADE_RESTRICTED | Trading is restricted due to high debt ratio  
FOK_NOT_FILL | FOK order cannot be filled completely  
INITIAL_MARGIN_TOO_LOW | User's total initial margin rate is too low  
NO_MERGEABLE_ORDERS | Orders can be merged not found  
ORDER_BOOK_NOT_FOUND | Insufficient liquidity  
FAILED_RETRIEVE_ASSETS | Failed to retrieve account assets  
CANCEL_FAIL | Order cancel failed  
  
  * Futures related

label list`label` | Meaning  
---|---  
USER_NOT_FOUND | User has no futures account  
CONTRACT_NO_COUNTER | No counter order found  
CONTRACT_NOT_FOUND | Contract not found  
RISK_LIMIT_EXCEEDED | Risk limit exceeded  
INSUFFICIENT_AVAILABLE | Balance is not enough  
LIQUIDATE_IMMEDIATELY | Operation may cause liquidation  
LEVERAGE_TOO_HIGH | leverage too high  
LEVERAGE_TOO_LOW | leverage too low  
ORDER_NOT_FOUND | Order not found  
ORDER_NOT_OWNED | Order not owned  
ORDER_FINISHED | Order already finished  
TOO_MANY_ORDERS | Too many open orders  
POSITION_CROSS_MARGIN | margin updating is not allowed in cross margin  
POSITION_IN_LIQUIDATION | Position is being liquidated  
POSITION_IN_CLOSE | Position is closing  
POSITION_EMPTY | Position is empty  
REMOVE_TOO_MUCH | Changed margin exceeds allowed  
RISK_LIMIT_NOT_MULTIPLE | Risk limit is not a multiple of step  
RISK_LIMIT_TOO_HIGH | Risk limit too high  
RISK_LIMIT_TOO_lOW | Risk limit too low  
PRICE_TOO_DEVIATED | Order price deviates too much from mark price  
SIZE_TOO_LARGE | Order size exceeds maximum  
SIZE_TOO_SMALL | Order size does not reach minimum  
PRICE_OVER_LIQUIDATION | Price to increase position can not exceeds liquidation price  
PRICE_OVER_BANKRUPT | Price to decrease position cannot exceeds bankrupting price  
ORDER_POC_IMMEDIATE | POC order will be finished immediately  
INCREASE_POSITION | POC order will increase position  
CONTRACT_IN_DELISTING | Contract is delisting, only reduce-only order or close order is allowed  
POSITION_NOT_FOUND | Position not found  
POSITION_DUAL_MODE | Operation forbidden in dual-mode  
ORDER_PENDING | Operation forbidden with pending orders  
POSITION_HOLDING | Operation forbidden with holding position  
REDUCE_EXCEEDED | Reduce order would exceed position in dual-mode  
NO_CHANGE | No change is made  
AMEND_WITH_STOP | Amend forbidden with stop order  
ORDER_FOK | Killed for FOK  
  
  * Collateral Loan related

label list`label` | Meaning  
---|---  
COL_NOT_ENOUGH | Collateral balance not enough  
COL_TOO_MUCH | Exceed collateral currency quota  
INIT_LTV_TOO_HIGH | Init ltv too high  
REDEEMED_LTV_TOO_HIGH | Ltv too high after redeem  
BORROWABLE_NOT_ENOUGH | Left borrowable not enough  
ORDER_TOO_MANY_TOTAL | Exceed platform order count one day  
ORDER_TOO_MANY_DAILY | Exceed single user order count one day  
ORDER_TOO_MANY_USER | Exceed single user order count total  
ORDER_NOT_EXIST | Order id not exist  
ORDER_FINISHED | Order id finished  
ORDER_NO_PAY | Order unpaid amount is zero  
ORDER_EXIST | Order exist  
ORDER_HISTORY_EXIST | Order history exist  
ORDER_REPAYING | Order is repaying  
ORDER_LIQUIDATING | Order is liquidating  
BORROW_TOO_LITTLE | Less than currency min borrow amount  
BORROW_TOO_LARGE | Greater than total max borrow amount quantity  
REPAY_AMOUNT_INVALID | Repay request amount invalid  
REPAY_GREATER_THAN_AVAILABLE | Repay greater than available  
POOL_BALANCE_NOT_ENOUGH | Pool balance not enough  
CURRENCY_SETTLING | Currency settlement in progress  
RISK_REJECT | Risk reject, please try again later  
LOAN_FAILED | Loan failed, you can borrow again  
  
  * Portfolio related

label list`label` | Meaning  
---|---  
USER_LIAB | User has liab  
USER_PENDING_ORDERS | User has pending orders  
MODE_SET | already set portfolio_margin mode  
  
  * Earn related

label list`label` | Meaning  
---|---  
ERR_BALANCE_NOT_ENOUGH | balance not enough  
ERR_PRODUCT_SELL_OUT | Target quota reached  
ERR_PRODUCT_BUY | The project is not yet open for purchase  
ERR_CREATE_ORDER | Put order fail  
ERR_QUOTA_LOWER_LIMIT | Not meeting the minimum order amount  
ERR_QUOTA_SUPERIOR_LIMIT | The maximum order limit has been reached  
ERR_ORDER_NUMBER_LIMIT | The maximum order quantity has been reached  
ERR_PRODUCT_CLOSE | Project closed  
COPIES_NOT_ENOUGH | Not enough shares available to subscribe  
COPIES_TOO_SMALL | Investment share is too small  
COPIES_TOO_BIG | The number of investment shares exceeds the upper limit  
TOTAL_AMOUNT_24 | The total amount of pledge and redemption within 24 hours exceeds the limit  
TOTAL_BUYCOUNT_24 | Pledge and redemption times exceeding the limit within 24 hours  
REDEEM_24_LIMIT | Redemption are allowed 24 hours after the last staking  
  
  * Server errors

label list`label` | Meaning  
---|---  
INTERNAL | Internal server error  
SERVER_ERROR | Internal server error  
INTERNAL_SERVER_ERROR | Operation failed, please try again later. (same as SERVER_ERROR)  
TOO_BUSY | Server is too busy at the moment  
  
  * Flash Convert Related

label list`label` | Meaning  
---|---  
INVALID_PARAM_VALUE | Invalid request parameter  
INVALID_CURRENCY | Invalid currency  
INVALID_CURRENCY_PAIR | Invalid currency pair  
PRICE_OBSOLETE | The price was obsoleted  
ORDER_NOT_FOUND | Order not found  
ORDER_BOOK_NOT_FOUND | Order book not found  
BALANCE_NOT_ENOUGH | Not enough balance/balance transfer fail  
TOO_MANY_REQUESTS | Request rate exceeds limits  
QUOTA_NOT_ENOUGH | Quota not enough,please reduce the amount or try again later  
SERVER_TIMEOUT | Service timeout  
MISSING_REQUIRED_PARAM | Missing required parameter  
REQUEST_FORBIDDEN | Asset management product is under liquidation; only USDT purchases are allowed  
CONVERT_PREVIEW_EXPIRED | The result of preview is expired  
CONVERT_PREVIEW_NOT_MATCH | The result of preview is not match  
AMOUNT_TOO_LITTLE | Under minimum transaction amount  
AMOUNT_TOO_MUCH | Over maximum transaction amount  
  
#  Authentication

##  Generate API key

Before calling the private API interface, the API key of the account needs to be generated to verify the identity. You can log in on the website and generate it in [account management] - > [APIv4 keys], or click [ here](/myaccount/apiv4keys) to generate API keys.

Each account can create 20 API keys, and the permission configuration of each key is independent of each other. It is recommended to set a note name for each key to indicate its purpose.

**`Key`** Access Key **`Secret Key`** The key used for signature authentication encryption

Besides, you can attach an IP whitelist, which requires the server only accept requests from specified IPs. Each key can have at most 20 IPs formatted in IPv4(not supporting IP range though). If IP whitelist is not set, the server will skip client IP validation.

Each user can create at most 5 keys with separate permissions. It is recommended to set a name for key denoting how the key will be used.

TIP

Note: If the key is named with `spot` or `futures`, then it could be the default name after APIv4 migration. For details refer to _About APIv4 key improvement_ section

Created key can also be updated or deleted, but any modification(s) can take up to 5 minutes to take effect.

Please note that futures TestNet trading is a separate environment from futures real trading. Real trading API keys cannot be used in TestNet. If you want to test futures API with TestNet, you need to log into the console to generate TestNet API keys(in _"Futures TestNet APIKeys"_ tab on _" APIv4Keys"_ page). Making futures requests are identical between real and TestNet trading, with the only exceptions are different base URLs and different API keys.

##  APIv4 Permissions

When creating a Key, you can configure whether to enable spot, margin, contract, wallet, or withdrawal permissions for the Key, and whether to enable read-write or read-only permissions.

APIv4 PermissionsProducts | Permissions  
---|---  
`spot/margin` | `Read-only` query orders `Read-write` query orders & place orders  
`perpetual contract` | `Read-only` query orders `Read-write` query orders & place orders  
`delivery contract` | `Read-only` query orders `Read-write` query orders & place orders  
`wallet` | `Read-only` Query for withdrawal transfer records `Read-write` Query for account records & fund transfers  
`withdrawal` | `Read-only` Query cash withdrawal records `Read-write` Query cash withdrawal records & withdrawals  
  
All `GET` operations are read requests, while others are write requests. Each permission group can be set to disabled, read-only or read-write.

Please note that even though withdrawal API has only one operation(i.e. `POST /withdrawals`), for general concern, it is still separated from wallet API into a standalone permission group, while withdrawal history retrieving API stays inside wallet operations( i.e., `GET /wallet/withdrawals`).

##  APIv4 signed request requirements

  1. Generate APIv4 Key pairs in web console, and make sure it has the right permissions.
  2. Set request header `KEY` to the key.
  3. Set request header `Timestamp` to current time formatted in Unix time in seconds. Pay attention that the gap between its value and current time cannot exceed 60 seconds.
  4. Set request header `SIGN` to encrypted request signature. Refer to next section for how signature string is generated. Signature generation method is `HexEncode(HMAC_SHA512(secret, signature_string))`, i.e., the hexadecimal digest output of HMAC-SHA512 with APIv4 secret as secret and signature string as message,
  5. Make sure request client's IP is in your APIv4 Key's IP whitelist.

##  API Signature string generation

In APIv4, signature string is concatenated as the following way:

`Request Method + "\n" + Request URL + "\n" + Query String + "\n" + HexEncode(SHA512(Request Payload)) + "\n" + Timestamp`

###  Request Method

Request method in UPPERCASE, e.g. `POST`, `GET`

###  Request URL

Request url. Protocol, host and port are not included, e.g. `/api/v4/futures/orders`

###  Query String

Request query string without URL encode. query parameters order should be the same as how they are concatenated in the request URL, e.g. `status=finished&limit=50`. Use empty string("") if no query parameters.

###  HexEncode(SHA512(Request Payload))

Hash the request body with SHA512 and output its Hex encoded form. If no request body, use empty string's hashed result, i.e. `cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e`

###  Timestamp

`Timestamp` request header value.

Examples

Note: all example signature string are broken into multiple lines for displaying purpose only. Only the `\n` character in signature string is reserved in reality.

Suppose the key we used is `key`, while the secret is `secret`.

  1. List all orders

    
    
    	GET /api/v4/futures/orders?contract=BTC_USD&status=finished&limit=50 HTTP/1.1
    

Signature string：
    
    
    	GET\n
    	/api/v4/futures/orders\n
    	contract=BTC_USD&status=finished&limit=50\n
    	cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e\n
    	1541993715
    

Explanation：

  * `/api/v4/futures/orders`: request url
  * `contract=BTC_USD&status=finished&limit=50`: keep the query string as it is in the request url
  * request body use empty string's hashed result
  * `1541993715`: Unix timestamp in seconds

Signature generated

`55f84ea195d6fe57ce62464daaa7c3c02fa9d1dde954e4c898289c9a2407a3d6fb3faf24deff16790d726b66ac9f74526668b13bd01029199cc4fcc522418b8a`

  2. Create an order

    
    
    	POST /api/v4/futures/orders HTTP/1.1
    
    	{"contract":"BTC_USD","type":"limit","size":100,"price":6800,"time_in_force":"gtc"}
    

Signature string：
    
    
    	POST\n
    	/api/v4/futures/orders\n
    	\n
    	ad3c169203dc3026558f01b4df307641fa1fa361f086b2306658886d5708767b1854797c68d9e62fef2f991645aa82673622ebf417e091d0bd22bafe5d956cca\n
    	1541993715
    

Explanation：

  * request query string is empty, use plain empty string
  * use the hashed result of the json-string-formatted request body

Signature generated

`eae42da914a590ddf727473aff25fc87d50b64783941061f47a3fdb92742541fc4c2c14017581b4199a1418d54471c269c03a38d788d802e2c306c37636389f0`
    
    
    # example authentication implementation in Python
    
    """
    Python SDK is recommended as it has already implemented the authentication process for every API:
    """
    
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
    

#  FAQ

  * How to retrieve `POST /wallet/transfers` history?

Records of transfers generated through `POST /wallet/transfers` has multiple methods to be retrieved based on account, including:

    * `GET /margin/account_book` to retrieve transferals from or to margin account.
    * `GET /futures/{settle}/account_book?type=dnw` to retrieve perpetual contract account history
    * `GET /delivery/{settle}/account_book?type=dnw` to retrieve delivery contract account history
  * How to create margin orders?

Margin order creation has been merged into spot order APIs. In `POST /spot/orders` or `POST /spot/batch_orders`, set `account` to `margin` to create margin orders.

  * Futures operation returns error `USER_NOT_FOUND`

Futures account is not initialized yet. Making a deposit to your futures account will help. Note that each settle currency is associated with an independent futures account.

  * Futures operation returns error `CONTRACT_NOT_FOUND`

Every settle currency has its own contract list. Make sure the contract you specified is supported by the settle currency. You can query the list with

`GET /futures/{settle}/contracts` or `GET /delivery/{settle}/contracts`

  * Difference between sub account and main account

    * Sub account API Key cannot operate transferals between main and sub account, i.e., `POST /wallet/sub_account_transfers`
    * Sub account API Key cannot operate withdrawal, i.e., `POST /withdrawals`
    * If sub account does not have some business permission, even if its API key has the permission, the operations will be rejected too.
  * I have other question(s) not covered above

Contact support for the issue. If the problem is related to one of the SDKs, you can also open an issue in the corresponding GitHub repository.

When submitting an issue, please include the following information to help identify the problem:

    * User ID 
      * Original request URL, request parameters and request body
      * What API key was used and where was it used, TestNet or real trading(API secret is not needed)
      * Programming language. Providing a code snippet will be better
      * Whether SDK was used. If so, which method caused the problem

Last Updated: 1/13/2026, 8:44:29 AM