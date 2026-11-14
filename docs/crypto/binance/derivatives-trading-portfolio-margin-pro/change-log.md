---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/derivatives-trading-portfolio-margin-pro/change-log
api_type: REST
updated_at: 2026-11-13 20:28:21.003680
---

# Change Log

## 2026-10-23

**Effective Date: 2026-10-23**

USDⓈ-M Futures

  * `POST /fapi/v1/algoOrder` (New Algo Order): the maximum value of `callbackRate` for `TRAILING_STOP_MARKET` orders is updated from 10 to 20.
  * WebSocket API `algoOrder.place` (New Algo Order): the maximum value of `callbackRate` for `TRAILING_STOP_MARKET` orders is updated from 10 to 20.



Portfolio Margin

  * `POST /papi/v1/um/algo/order` (New UM Algo Order): the maximum value of `callbackRate` for `TRAILING_STOP_MARKET` orders is updated from 10 to 20.



* * *

## 2026-10-21

**Effective Date: 2026-10-28**

Portfolio Margin

  * `GET /papi/v1/um/income` (Get UM Income History): the `page` parameter is no longer supported. Use `startTime` and `endTime` to locate records.
  * `GET /papi/v1/cm/income` (Get CM Income History): the `page` parameter is no longer supported. Use `startTime` and `endTime` to locate records.



* * *

## 2026-10-20

**Effective Date: 2026-10-20**

USDⓈ-M Futures

  * `GET /fapi/v1/income/asyn` (Get Download Id For Futures Transaction History): the request limit is now 100 times per month, shared across the front end download page and rest api, as well as between USDⓈ-M and COIN-M contracts.



COIN-M Futures

  * `GET /dapi/v1/income/asyn` (Get Download Id For Futures Transaction History): the request limit is now 100 times per month, shared across the front end download page and rest api, as well as between USDⓈ-M and COIN-M contracts.



* * *

## 2026-10-15

**Effective Date: 2026-10-15**

Portfolio Margin and Portfolio Margin Pro

  * `POST /sapi/v1/portfolio/asset-collection` (Fund Collection by Asset) and `POST /papi/v1/asset-collection` (Fund Collection by Asset): added two optional request parameters, `amount` (DECIMAL) and `futureType` (STRING; enum `UM` / `CM` / `OPTION`, `OPTION` for SPAN only). When both are provided, the collection is routed to the specified wallet. `amount` and `futureType` must be supplied together. When neither is provided, behavior is unchanged.



**Effective Date: 2026-10-16**

USDⓈ-M Futures

  * `GET /fapi/v1/income` (Get Income History): the `page` parameter is no longer supported. Use `startTime` and `endTime` to locate records.



COIN-M Futures

  * `GET /dapi/v1/income` (Get Income History): the `page` parameter is no longer supported. Use `startTime` and `endTime` to locate records.



* * *

## 2026-10-09

**Effective Date: 2026-10-09**

USDⓈ-M Futures

  * `POST /fapi/v1/leverage` (Change Initial Leverage): removed the documented fixed maximum of 125 on `leverage`. The maximum is symbol-specific and equals `initialLeverage` of bracket 1 from `GET /fapi/v1/leverageBracket` (e.g. 150 for BTCUSDT and ETHUSDT). Documentation correction only, reflecting current backend behavior.



Portfolio Margin

  * `POST /papi/v1/um/leverage` (Change UM Initial Leverage): removed the documented fixed maximum of 125 on `leverage`. The maximum is symbol-specific and equals `initialLeverage` of bracket 1 from `GET /papi/v1/um/leverageBracket`. Documentation correction only, reflecting current backend behavior.



* * *

## 2026-10-08

**Effective Date: 2026-10-08**

European Options

  * `GET /eapi/v1/bill` (Account Funding Flow)
    * Response now includes a `symbol` field on contract-related records (e.g. `CONTRACT`, `FEE`, `EXERCISE_PNL`, `EXERCISE_FEE`), identifying the option symbol. It is not returned for other types such as `TRANSFER`, and older records may not include it.



* * *

## 2026-09-28

**Effective Date: 2026-09-28**

USDⓈ-M Futures

  * Added new error code `-4425` `JOINT_MARGIN_REJECT_WITH_SIGNAL_LEAD`: "Cannot switch to multi-asset mode due to active signal lead portfolio."



* * *

## 2026-09-21

**Effective Date: 2026-09-14**

USDⓈ-M Futures

  * `GET /fapi/v1/tradingSchedule` (Trading Schedule) and the Trading Session Stream now cover the FX market (`FX` / `FXUpdate`), with session types "REGULAR" and "NO_TRADING".



* * *

## 2026-09-15

**Effective Date: 2026-09-15**

USDⓈ-M Futures

  * Modified `order.modify` (WebSocket API — Modify Order): added optional parameter `reduceOnly` (STRING). When `true`, the endpoint skips `min_notional` validation on the modified order if and only if the original order was also placed as reduce-only; otherwise the request is rejected with `-5047` "The original order is not a reduce-only order".
  * Modified `PUT /fapi/v1/order` (REST API — Modify Order): added the same optional parameter `reduceOnly` (STRING), with identical behavior to the `order.modify` change above.
  * Note: the `reduceOnly` parameter is used purely for order validation (min_notional bypass + RO attribute consistency check). Passing `reduceOnly=true` does NOT change the original order's reduce-only attribute — the order's RO flag remains whatever it was set to at placement time.



* * *

## 2026-09-10

**Effective Date: 2026-09-10**

USDⓈ-M Futures

  * `GET /fapi/v1/income` (Get Income History): added a new `incomeType` enum value `SPECIAL_FUNDING_FEE`, used for Tradfi Dividend funding fee.



* * *

## 2026-08-26

**Effective Date: 2026-08-26**

USDⓈ-M Futures

  * `GET /fapi/v1/userTrades` (Account Trade List): the historical data availability note is updated from "Only support querying trade in the past 6 months" to **"Only support querying trade in the past 3 months"** , reflecting current backend behavior.



COIN-M Futures

  * `GET /dapi/v1/userTrades` (Account Trade List): added a historical data availability note, **"Only support querying trade in the past 3 months"** , reflecting current backend behavior.



* * *

## 2026-08-25

**Effective Date: 2026-08-25**

USDⓈ-M Futures

  * `GET /fapi/v1/allOrders` (All Orders): the `symbol` parameter changed from mandatory to optional. All other behavior unchanged — the endpoint still returns up to 1000 records per request.



**Effective Date: 2026-08-26**

Portfolio Margin

  * `POST /papi/v1/um/algo/order` (New UM Algo Order): added optional `closePosition` parameter (`true`/`false`; Close-All, used with `STOP_MARKET` or `TAKE_PROFIT_MARKET`; mutually exclusive with `quantity`/`reduceOnly`; in Hedge Mode, cannot be used with `BUY` orders in `LONG` position side or `SELL` orders in `SHORT` position side); `quantity` changes from mandatory to optional; response now includes `closePosition`.



* * *

## 2026-08-21

**Effective Date: 2026-08-21**

USDⓈ-M Futures

  * `ALGO_UPDATE` (Algo Order Update)
    * The `ia` field (introduced in the [2026-08-07](/en/docs/products/derivatives-trading-portfolio-margin-pro/change-log#2026-08-07) entry) is now fully active — no longer a placeholder. For trailing stop orders, before the order triggers (Algo Status `X` remains `NEW`), you may receive two separate `ALGO_UPDATE` `NEW` push events: one with `ia:false`, followed by another with `ia:true` once the order is activated.



Portfolio Margin

  * `ALGO_UPDATE` (Algo Order Update)
    * The `ia` field (introduced in the [2026-08-07](/en/docs/products/derivatives-trading-portfolio-margin-pro/change-log#2026-08-07) entry) is now fully active — no longer a placeholder. For trailing stop orders, before the order triggers (Algo Status `X` remains `NEW`), you may receive two separate `ALGO_UPDATE` `NEW` push events: one with `ia:false`, followed by another with `ia:true` once the order is activated.



* * *

## 2026-08-17

**Effective Date: 2026-08-17**

USDⓈ-M Futures

  * `GET /fapi/v1/tradingSchedule` (Trading Schedule) and the Trading Session Stream now cover the China equity market (`CN_EQUITY` / `CN_EquityUpdate`), with session types "REGULAR" and "NO_TRADING".



* * *

## 2026-08-14

COIN-M Futures

  * `GET /futures/data/topLongShortAccountRatio` (Top Trader Long/Short Ratio (Accounts)): fixed request parameter `symbol` → `pair`; added optional `contractType` parameter (`PERPETUAL` / `CURRENT_QUARTER` / `NEXT_QUARTER`; omit for aggregated data across all contract types).
  * `GET /futures/data/globalLongShortAccountRatio` (Long/Short Ratio): added optional `contractType` parameter (`PERPETUAL` / `CURRENT_QUARTER` / `NEXT_QUARTER`; omit for aggregated data across all contract types).
  * `GET /futures/data/openInterestHist` (Open Interest Statistics): corrected `contractType` from documented-as-required to optional (`PERPETUAL` / `CURRENT_QUARTER` / `NEXT_QUARTER`; omit for aggregated data across all contract types; server behavior unchanged).
  * `GET /futures/data/topLongShortPositionRatio` (Top Trader Long/Short Ratio (Positions)): added optional `contractType` parameter (`PERPETUAL` / `CURRENT_QUARTER` / `NEXT_QUARTER`; omit for aggregated data across all contract types).



* * *

## 2026-08-11

**Effective Date: 2026-08-13**

USDⓈ-M Futures

  * `GET /fapi/v1/aggTrades` (Compressed/Aggregate Trades List): the maximum queryable trade history lookback (counted from now) is extended from 24 hours to 48 hours.



* * *

## 2026-08-07

**Effective Date: 2026-08-07**

USDⓈ-M Futures

  * `ACCOUNT_UPDATE` (Balance and Position Update)
    * The `a` object now includes a new field `S` (STRING): the symbol associated with the event. Only pushed when the event reason type `m` is `FUNDING_FEE`.
  * `ALGO_UPDATE` (Algo Order Update)
    * The `o` object now includes a new field `ia` (BOOLEAN): whether the algo order has been activated. Only meaningful for trailing stop orders.
    * Note: `ia` is currently a placeholder field and will always return `false`. It will be fully functional in a future release.



COIN-M Futures

  * `ACCOUNT_UPDATE` (Balance and Position Update)
    * The `a` object now includes a new field `S` (STRING): the symbol associated with the event. Only pushed when the event reason type `m` is `FUNDING_FEE`.



Portfolio Margin

  * `ACCOUNT_UPDATE` (Futures Balance and Position Update)
    * The `a` object now includes a new field `S` (STRING): the symbol associated with the event. Only pushed when the event reason type `m` is `FUNDING_FEE`.
  * `ALGO_UPDATE` (Algo Order Update)
    * The `ao` object now includes a new field `ia` (BOOLEAN): whether the algo order has been activated. Only meaningful for trailing stop orders.
    * Note: `ia` is currently a placeholder field and will always return `false`. It will be fully functional in a future release.



* * *

## 2026-08-05

**Effective Date: 2026-08-05**

The order/trade-history query endpoints (`forceOrders` / `allOrders` / `userTrades`, both `/fapi/v1/*` UM and `/dapi/v1/*` CM) support returning both UM and CM futures data.

USDⓈ-M Futures

  * The following endpoints now include additional fields in their responses:
    * `GET /fapi/v1/forceOrders` (User's Force Orders): added `cumBase` and `pair`.
    * `GET /fapi/v1/allOrders` (All Orders): added `cumBase` and `pair`.
    * `GET /fapi/v1/userTrades` (Account Trade List): added `pair`, `baseQty` and `marginAsset`.



COIN-M Futures

  * The following endpoints now include additional fields in their responses:
    * `GET /dapi/v1/forceOrders` (User's Force Orders): added `cumQuote` and `goodTillDate`.
    * `GET /dapi/v1/allOrders` (All Orders): added `cumQuote` and `goodTillDate`.
    * `GET /dapi/v1/userTrades` (Account Trade List): added `quoteQty`.



* * *

## 2026-08-03

**Effective Date: 2026-08-03**

Portfolio Margin

  * The `avgPrice` field, along with `cumQuote` (UM) / `cumBase` (CM), has been removed from the responses of the following endpoints:
    * PUT `/papi/v1/um/order` (Modify UM Order)
    * PUT `/papi/v1/cm/order` (Modify CM Order)



* * *

## 2026-07-29

**Effective Date: 2026-07-29**

USDⓈ-M Futures

  * `GET /fapi/v1/historicalTrades` (Old Trades Lookup)
    * Request Weight updated from `20` to `200`.



COIN-M Futures

  * `GET /dapi/v1/historicalTrades` (Old Trades Lookup)
    * Request Weight updated from `20` to `200`.



* * *

## 2026-07-23

**Effective Date: 2026-07-23**

USDⓈ-M Futures

  * `GET /fapi/v1/fundingRate` (Get Funding Rate History)
    * The response now includes a new field `rateType` (STRING): the funding rate type. `Regular` for the normal funding rate; `Special` for the additional funding rate generated by stock dividends.



* * *

## 2026-07-21

**Effective Date: 2026-07-30**

USDⓈ-M Futures

  * `PUT /fapi/v1/order` (Modify Order), `PUT /fapi/v1/batchOrders` (Modify Multiple Orders), and the WebSocket API `order.modify`
    * New optional request parameter `modifyId` (INT): a user-defined modification identifier that the server passes through as-is; not validated for uniqueness. If omitted, it is not returned.
    * The response now returns `modifyId` when it was provided in the request.
  * `GET /fapi/v1/orderAmendment` (Get Order Modify History)
    * The response now includes `modifyId` for each modification that was submitted with one.
  * User Data Stream `ORDER_TRADE_UPDATE` event (`"x": "AMENDMENT"`)
    * New field `M` (STRING): the `modifyId` from the corresponding modify request; only pushed when a `modifyId` was provided.



COIN-M Futures

  * `PUT /dapi/v1/order` (Modify Order), `PUT /dapi/v1/batchOrders` (Modify Multiple Orders), and the WebSocket API `order.modify`
    * New optional request parameter `modifyId` (INT): a user-defined modification identifier that the server passes through as-is; not validated for uniqueness. If omitted, it is not returned.
    * The response now returns `modifyId` when it was provided in the request.
  * `GET /dapi/v1/orderAmendment` (Get Order Modify History)
    * The response now includes `modifyId` for each modification that was submitted with one.
  * User Data Stream `ORDER_TRADE_UPDATE` event (`"x": "AMENDMENT"`)
    * New field `M` (STRING): the `modifyId` from the corresponding modify request; only pushed when a `modifyId` was provided.



Portfolio Margin

  * `PUT /papi/v1/um/order` and `PUT /papi/v1/cm/order` (Modify Order)
    * New optional request parameter `modifyId` (INT): a user-defined modification identifier that the server passes through as-is; not validated for uniqueness. If omitted, it is not returned.
    * The response now returns `modifyId` when it was provided in the request.
  * `GET /papi/v1/um/orderAmendment` and `GET /papi/v1/cm/orderAmendment` (Query Order Modify History)
    * The response now includes `modifyId` for each modification that was submitted with one.
  * User Data Stream `ORDER_TRADE_UPDATE` event (`"x": "AMENDMENT"`)
    * New field `M` (STRING): the `modifyId` from the corresponding modify request; only pushed when a `modifyId` was provided.



* * *

## 2026-07-16

**Effective Date: 2026-07-16**

USDⓈ-M Futures

  * `GET /fapi/v1/tradingSchedule` (Trading Schedule)
    * Now covers the Hong Kong equity market (`HK_EQUITY`), with session types `REGULAR` and `NO_TRADING`.
  * WebSocket Trading Session Stream (`tradingSession`)
    * New event type `HK_EquityUpdate` for the Hong Kong equity market, with session types `REGULAR` and `NO_TRADING`.



* * *

## 2026-07-13

**Effective Date: 2026-07-14**

Portfolio Margin

  * The `cumBase`, `cumQuote` and `avgPrice` fields will be removed from the responses of the following endpoints:
    * POST `/papi/v1/um/order`
    * POST `/papi/v1/cm/order`
    * DELETE `/papi/v1/um/order`
    * DELETE `/papi/v1/cm/order`



* * *

## 2026-07-09

Options

  * New REST API:
    * `POST /eapi/v1/stock/contract`: sign TradFi Options agreement contract



European Options

  * `GET /eapi/v1/exchangeInfo` (Exchange Information)
    * Response `optionSymbols` now includes `contractType` and `underlyingType` fields for each option symbol, indicating the contract type and underlying type.



* * *

## 2026-06-30

COIN-M Futures

  * `GET /dapi/v1/constituents` (Index Constituents)
    * Response now includes `weight` and `price` fields for each constituent, consistent with the USDⓈ-M Futures endpoint (`GET /fapi/v1/constituents`).
  * `GET /dapi/v1/pmAccountInfo` (Classic Portfolio Margin Account Information) is no longer in use. Please use `GET /fapi/v1/pmAccountInfo` instead.
  * WebSocket Stream `<pair>@indexPrice` (Index Price Stream)
    * The pair field in the response payload has been renamed from `"i"` to `"s"`.
    * The `<pair>@indexPrice@1s` (1000ms) variant has been removed. The stream is now available as `<pair>@indexPrice` only, with an update speed of 1000ms.



* * *

## 2026-06-29

**Time-sensitive Notice**

  * `POST /dapi/v1/countdownCancelAll` (COIN-M Auto-Cancel All Open Orders / Countdown)
    * The COIN-M countdown (auto-cancel) feature will be **suspended on 2026-06-29 at 09:00 UTC (17:00 UTC+8)** for the CM migration maintenance, and will be **restored after CM resumes**.
    * Any countdown set before the suspension remains effective in the matching engine up until the snapshot is taken at maintenance shutdown.
    * If the countdown timer set by the user is scheduled to fire after the maintenance snapshot, the countdown for those symbols will **not** take effect.



* * *

## 2026-06-20

USDⓈ-M Futures

  * `POST /fapi/v1/algoOrder` (New Algo Order)
    * Request Weight now follows the order rate limits: `1` on 10s order rate limit (`X-MBX-ORDER-COUNT-10S`) and `1` on 1min order rate limit (`X-MBX-ORDER-COUNT-1M`). IP weight remains `0`.



* * *

## 2026-06-16

**Time-sensitive Notice**

  * Please note the Futures COIN-M demo trading will be unavailable from 2026-06-16 02:00 till 10:00 UTC.
  * **Update:** The Futures COIN-M demo trading maintenance window is extended. The new window is from 2026-06-16 02:00:00 till 2026-06-23 10:00:00 (UTC). We appreciate your patience and understanding.



* * *

## 2026-06-10

**Effective Date: 2026-06-30**

COIN-M Futures architecture integration with USDⓈ-M Futures — REST endpoints, WebSocket streams, and account-level behavior changes. See [Important CM-UM Integration Notice](/en/docs/products/derivatives-trading-coin-futures/Important-CM-UM-Integration-Notice) for the full list of affected endpoints and the action items. For the detailed timeline, please refer to the [announcement](https://www.binance.com/en/support/announcement/detail/2a84dfd7643f4dc18084e45e8691b69e).

* * *

## 2026-06-02

**Effective Date: 2026-06-02**

USDⓈ-M Futures

  * `GET /fapi/v1/tradingSchedule` (Trading Schedule)
    * Extended time range from 7 days forward to **7 days backward and 7 days forward** starting from the day prior to the query time.
    * Added Korean equity market (`KR_EQUITY`) support. Korean equity market session types: `REGULAR` and `NO_TRADING`.
  * WebSocket Stream `tradingSession` (Trading Session Stream)
    * Added Korean equity market support.
    * Added new event type `KR_EquityUpdate`. Korean equity market session types: `REGULAR` and `NO_TRADING`.



* * *

## 2026-05-11

**Effective Date: 2026-05-13**

USDⓈ-M Futures

  * `POST /fapi/v1/positionSide/dual`
    * New error code `-4531`: When changing UM `dualSidePosition`, the system will automatically sync CM `dualSidePosition`. If the CM account has any open position or open order, the sync cannot proceed and the UM position mode change will be rejected with error code `-4531`.

    * Error payload:
          
          Code
          
          {
            "code": -4531,
            "msg": "Position mode change requires syncing UM and CM. Please close any open positions or orders in CM and try again."
          }

    * **Note** : This error code is temporary and will only be active until CM enters Guard (approximately 1 month). After CM enters Guard, this error will no longer occur.




* * *

## 2026-04-17

Portfolio Margin Pro

  * User Data Stream:
    * Add new event `PM_PRO_ACCOUNT_UPDATE`, which pushes account asset status every 5 seconds.



* * *

## 2026-04-15

European Options

  * Trade
    * Cancel Multiple Option Orders - Corrected request weight from 1 to 5.



* * *

## 2026-04-14

Portfolio Margin

  * The following REST Endpoints and WebSocket User Data Streams will be enabled from 2026-04-28:

    * REST:
      * POST `/papi/v1/um/algo/order`
      * DELETE `/papi/v1/um/algo/order`
      * DELETE `/papi/v1/um/algo/allOpenOrders`
      * GET `/papi/v1/um/algo/algoOrder`
      * GET `/papi/v1/um/algo/openAlgoOrders`
      * GET `/papi/v1/um/algo/allAlgoOrders`
    * Websocket:
      * `ALGO_UPDATE`: algo order update event
  * The following REST Endpoints will be deprecated from 2026-04-28

    * REST:
      * POST `/papi/v1/um/conditional/order`
      * DELETE `/papi/v1/um/conditional/order`
      * DELETE `/papi/v1/um/conditional/allOpenOrders`
      * GET `/papi/v1/um/conditional/allOrders`
      * GET `/papi/v1/um/conditional/openOrders`
      * GET `/papi/v1/um/conditional/openOrder`
      * GET `/papi/v1/um/conditional/orderHistory`



Please refer to [announcement](https://www.binance.com/en/support/announcement/detail/13980e4145ee41259d32f985161d81b6) for API replacement

* * *

## 2026-04-13

Portfolio Margin and Portfolio Margin Pro

New REST APIs:

  * `POST /sapi/v1/portfolio/margin-call-level` : Set the margin call level for a Portfolio Margin account. When the account's uniMMR drops to the specified level, a notification will be sent via email and SMS.
  * `GET /sapi/v1/portfolio/margin-call-level` : Get the margin call level for a Portfolio Margin account.
  * `DELETE /sapi/v1/portfolio/margin-call-level` : Delete the margin call level for a Portfolio Margin account.



* * *

## 2026-04-10

**Effective Date: 2026-04-14**

COIN-M Futures / Portfolio Margin and Portfolio Margin Pro

  * `POST /dapi/v1/positionSide/dual` and `POST /papi/v1/cm/positionSide/dual`
    * CM `dualSidePosition` must now stay consistent with UM. If CM `dualSidePosition` is already the same as UM, changing it will be rejected.



USDⓈ-M Futures

  * Liquidation Order Streams (`<symbol>@forceOrder`) and All Market Liquidation Order Streams (`!forceOrder@arr`)
    * Updated description: changed "only the latest one liquidation order" to "only the largest one liquidation order" within 1000ms.



* * *

## 2026-04-09

Portfolio Margin

  * User Data Stream
    * [Event: Margin Order Update](/en/docs/products/derivatives-trading-portfolio-margin/user-data-streams#event-margin-order-update) \- Added new fields to the `executionReport` event payload: `Cs`, `pl`, `pL`, `pY`, `eR`.



* * *

## 2026-04-08

Portfolio Margin

New REST APIs:

  * `POST /papi/v1/um/stock/contract` : sign TradFi-Perps agreement contract



* * *

## 2026-04-06

USDⓈ-M Futures / COIN-M Futures / Portfolio Margin and Portfolio Margin Pro

  * `GET /fapi/v1/forceOrders`, `GET /dapi/v1/forceOrders`, `GET /papi/v1/um/forceOrders` and `GET /papi/v1/cm/forceOrders`
    * Added note: Only support querying data in the past 90 days.



* * *

## 2026-04-02

USDⓈ-M Futures

  * WebSocket
    * Updated [important websocket change notice](/en/docs/products/derivatives-trading-usds-futures/websocket-market-streams/Important-WebSocket-Change-Notice) with legacy URL decommissioning date: **2026-04-23**.



* * *

## 2026-03-19

USDⓈ-M Futures / COIN-M Futures

  * `GET /fapi/v1/historicalTrades` and `GET /dapi/v1/historicalTrades`
    * Updated data availability from the last 3 months to the last 1 month.



## 2026-03-16

USDⓈ-M Futures

  * Websocket Market Streams
    * Add new field `ap` in `Mark-Price-Stream` and `Mark-Price-Stream-for-All-market` to show mark price moving average.



## 2026-03-11

Option

  * Effective on 2026-03-19
  * Self-Trade Prevention:
    * Similar to USDⓈ-M Futures, Self-Trade Prevention (aka STP) is added to the system. This prevents orders from matching with orders from the same account, or accounts under the same tradeGroupId
    * User can set selfTradePreventionMode when placing new orders. All option symbols support the following STP mode:
      * EXPIRE_MAKER: expire maker order when STP trigger
      * EXPIRE_TAKER: expire taker order when STP trigger
      * EXPIRE_BOTH: expire taker and maker order when STP trigger
  * REST Update:
    * New order status EXPIRED_IN_MATCH \- This means that the order expired due to STP being triggered.
    * Add optional parameter selfTradePreventionMode in the endpoints below to set order's STP mode:
      * POST /eapi/v1/order
      * POST /eapi/v1/batchOrders
    * Add new field selfTradePreventionMode in response of the endpoints below to show order's STP mode:
      * POST /eapi/v1/order
      * POST /eapi/v1/batchOrders
      * GET /eapi/v1/order
      * GET /eapi/v1/openOrders
      * PUT /eapi/v1/order
      * PUT /eapi/v1/batchOrders
      * DELETE /eapi/v1/order
      * DELETE /eapi/v1/batchOrders
  * WEBSOCKET User Data Stream:
    * Add new field V in ORDER_TRADE_UPDATE to order STP mode.



## 2026-03-05

USDⓈ-M Futures

  * WebSocket
    * Add [important websocket change notice](/en/docs/products/derivatives-trading-usds-futures/websocket-market-streams/Important-WebSocket-Change-Notice).
    * Added `URL PATH` section to all websocket market stream pages indicating the new base URL path (`/public`, `/market`).
    * Added `URL PATH` section to all user data stream event pages indicating the new base URL path (`/private`).



## 2026-01-09

Portfolio Margin and Portfolio Margin Pro

  * New endpoints for switch to Delta Mode:
    * `POST /sapi/v1/portfolio/delta-mode`: Switch the Delta Mode for existing PM PRO / PM RETAIL accounts.
    * `GET /sapi/v1/portfolio/delta-mode`: Query the Delta mode status of current account.



## 2026-01-07

Option

  * New REST APIs:
    * `GET /eapi/v1/commission`: query user commission rate



## 2025-12-29

USDⓈ-M Futures

  * The parameter "filterType": "MAX_NUM_ALGO_ORDERS" has been removed from the endpoint `GET /fapi/v1/exchangeInfo`. The condtional order limits is 200 across all symbols.
  * Effective on 2025-12-31, field `nq` will be available in `<symbol>@aggTrade` stream. For this new field, only normal market trades will be aggregated， which means the trades involving RPI orders won't be aggregated.



## 2025-12-11

USDⓈ-M Futures

  * New REST APIs:
    * `GET /fapi/v1/tradingSchedule`: query trading session schedules for a one-week period
    * `POST /fapi/v1/stock/contract`: sign TradFi-Perps agreement contract
  * New Websocket API:
    * `tradingSession`: query current trading session information



## 2025-12-10

  * Since conditional orders have been migrated to the Algo Service, the event `CONDITIONAL_ORDER_TRIGGER_REJECT` will be deprecated effective December 15, 2025. Any conditional order rejection reasons are provided within the `ALGO_UPDATE` event.



## 2025-12-09

COIN-M Futures

  * Effective on 2025-12-10, Order expire reason field `er` will be available in `ORDER_TRADE_UPDATE` stream.



## 2025-11-25

USDⓈ-M Futures

  * Effective on **2025-11-26** , RPI commisson fee is available in the response of User Commission Rate endpoint
    * REST
      * `GET /fapi/v1/commissionRate`
  * New endpoints to fetch RPI order book
    * REST
      * `GET /fapi/v1/rpiDepth`
    * WebSocket
      * `<symbol>@rpiDepth@500ms`



## 2025-11-19

USDⓈ-M Futures

  * REST API
    * `GET /fapi/v1/symbolAdlRisk`: New endpoints to query ADL risk rating



## 2025-11-18

USDⓈ-M Futures

  * The RPI order is introduced to USDⓈ-M Futures
    * New time-in-force ENUM value - RPI is supported in
      * REST
        * `POST /fapi/v1/order`
        * `POST /fapi/v1/batchOrders`
      * WebSocket
        * `order.place`
    * New fields in the market data response - Boolean "IsRPITrade" available in
      * REST
        * `GET /fapi/v1/trades`
        * `GET /fapi/v1/historicalTrades`
    * Order Book Exclusion - RPI orders don't appear in
      * REST
        * `GET /fapi/v1/depth`
        * `GET /fapi/v1/ticker/bookTicker`
      * WebSocket
        * `ticker.book`
        * `<symbol>@bookTicker`
        * `!bookTicker`
        * `<symbol>@depth<levels>`
        * `<symbol>@depth`
  * For more details, please refer to <https://www.binance.com/en/support/faq/92c83c53173947c4a44f9a7277c3b9ce>



## 2025-11-12

Binance Derivative is rebuilding the Options system to enhance overall stability, performance, and scalability, while also introducing new features.

As the first step, a new Options Demo API environment has been launched to help existing users adapt their code to the updated system. Documentation is available under the "Options Demo Trading" tab.

To get started, please visit <https://demo.binance.com/zh-CN/my/settings/api-management> to create a new API key. This key can be used to access the new Options Demo Trading environment.

## 2025-11-10

  * As BFUSD has been migrated to Binance Earn on 2025-08-13. The following endpoints is deprecated:
    * `POST sapi/v1/portfolio/mint`
    * `POST sapi/v1/portfolio/redeem`



## 2025-11-06

  * Effective on **2025-12-09** , USDⓈ-M Futures will migrate conditional orders to the Algo Service, which will affect the following order types: `STOP_MARKET`/`TAKE_PROFIT_MARKET`/`STOP`/`TAKE_PROFIT`/`TRAILING_STOP_MARKET`.

  * The new endpoints for conditional orders of REST API :

    * `POST fapi/v1/algoOrder`: Place an algo order
    * `DELETE /fapi/v1/algoOrder`: Cancel an algo order
    * `DELETE fapi/v1/algoOpenOrders`: Cancel all open algo orders
    * `GET /fapi/v1/algoOrder`: Query an algo order
    * `GET /fapi/v1/openAlgoOrders`: Query algo open order(s)
    * `GET /fapi/v1/allAlgoOrders`: Query algo order(s)
  * The following enpoints will block the requests for order types after the migration: `STOP_MARKET`/`TAKE_PROFIT_MARKET`/`STOP`/`TAKE_PROFIT`/`TRAILING_STOP_MARKET`. The error code `-4120` STOP_ORDER_SWITCH_ALGO will be encountered.

    * `POST /fapi/v1/order`
    * `POST /fapi/v1/batchOrders`
  * Websocket User Stream Update

    * New algo order event: `ALGO_UPDATE`
  * Websocket API Update

    * New algo order : `algoOrder.place`
    * Cancel algo order: `algoOrder.cancel`
  * Please note that after the migration:

    * No margin check before the conditional order gets triggered.
    * GTE_GTC orders no longer depend on open orders of the opposite side, but rather on positions only.
    * There should be no latency increase in order triggering.
    * Modification of untriggered conditional orders is not supported.



## 2025-10-21

  * Effective **2025-10-23** , the `priceMatch` enum values **`OPPONENT_10`** and **`OPPONENT_20`** are temporarily removed from **place/amend** flows, other enums are not impacted. Affected endpoints:

**USDT-M Futures (`/fapi`)**

    * `POST /fapi/v1/order`
    * `POST /fapi/v1/batchOrders`
    * `PUT /fapi/v1/order`
    * `PUT /fapi/v1/batchOrders`

**COIN-M Futures (`/dapi`)**

    * `POST /dapi/v1/order`
    * `POST /dapi/v1/batchOrders`
    * `PUT /dapi/v1/order`
    * `PUT /dapi/v1/batchOrders`

**Portfolio Margin (`/papi`)**

    * `POST /papi/v1/um/order`
    * `PUT /papi/v1/um/order`
    * `POST /papi/v1/um/conditional/order`
    * `POST /papi/v1/cm/order`
    * `PUT /papi/v1/cm/order`
    * `POST /papi/v1/cm/conditional/order`



## 2025-10-20

USDⓈ-M Futures

  * Effective 2025-10-23, Order expire reason field `er` will be available in `ORDER_TRADE_UPDATE` stream.



## 2025-10-14

  * Effective 2025-10-23, the error message for the code below will be updated:


    
    
    Code
    
    {
        "code": -1008,
        "msg": "Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again."
    }

## 2025-10-09

  * Futures now supports trading pair symbols in Chinese. Example from `exchangeInfo`: `"symbol": "测试USDT"`.
  * When placing orders via API, if `symbol` contains Chinese characters, it **must** be URL-encoded (UTF-8 percent-encoding). Example:  
`https://fapi.binance.com/fapi/v1/order?symbol=%E6%B5%8B%E8%AF%95USDT&side=BUY&type=TAKE_PROFIT_MARKET&timeInForce=GTC&quantity=1&stopPrice=30&timestamp=1760000007980`
  * The `symbol` field in push messages (WebSocket/User Data Stream) may also contain Chinese. Ensure clients/downstream systems handle decoding and rendering properly.
  * Requests with unencoded Chinese `symbol` may fail or return parameter parsing errors.



## 2025-08-11

  * BFUSD will be migrated to Binance Earn on 2025-08-13. The following endpoints will be deprecated after the migration:
    * `POST sapi/v1/portfolio/mint`
    * `POST sapi/v1/portfolio/redeem`
  * Error code `-21015` ENDPOINT_GONE will be encountered.
  * Portfolio Margin and Portfolio Margin Pro users can switch to Binance Earn for BFUSD minting and redeeming. After the migration, the existing BFUSD under the Portfolio Margin wallet can use the aggregate balance function(`POST /sapi/v1/portfolio/asset-collection`) first, and transfer from Portfolio Margin wallet to Spot wallet for redemption.



## 2025-07-25

  * Added new error code in fapi:
    * `-4109`: _This account is inactive. Please activate it before trading._  
This indicates the account has been archived due to inactivity. To activate it, transfer any amount of asset to the USDM Futures account.



## 2025-07-02

USDⓈ-M Futures

  * REST API

    * `GET /futures/data/openInterestHist`: add response field `CMCCirculatingSupply`
  * Websocket Market Streams

    * A single connection of maximum streams change from 200 to 1024.



## 2025-04-23

USDⓈ-M Futures

  * REST API
    * `GET /fapi/v1/insuranceBalance`: New endpoints to query insurance fund balance snapshot
    * `GET /fapi/v1/constituents`: add response field `price` and `weight`



## 2025-04-15

Portfolio Margin and Portfolio Margin Pro

  * New endpoints for Earn Asset transfer as collateral:
    * `POST /sapi/v1/portfolio/earn-asset-transfer`: Transfer LDUSDT for Portfolio Margin
    * `GET /sapi/v1/portfolio/earn-asset-balance`: Get Transferable Earn Asset Balance for Portfolio Margin



## 2025-02-28

Portfolio Margin

  * New endpoints to query user pmloan repay record(Release on 2025-02-28):
    * `GET /sapi/v1/portfolio/pmloan-history`



## 2025-02-20

COIN-M Futures

WEBSOCKET API

  * Websocket API will be available on 2025-02-25 and can be accessed through this URL: `wss://ws-dapi.binance.com/ws-dapi/v1`
  * WebSocket API allows placing orders, canceling orders, etc. through a WebSocket connection.
  * WebSocket API is a separate service from WebSocket Market Data streams. I.e., placing orders and listening to market data requires two separate WebSocket connections.
  * WebSocket API is subject to the same Filter and Rate Limit rules as REST API.
  * WebSocket API and REST API are functionally equivalent: they provide the same features, accept the same parameters, return the same status and error codes.



## 2025-01-20

Portfolio Margin

  * New endpoints to query user negative balance auto exchange record(Release on 2025-01-22):
    * `GET /papi/v1/portfolio/negative-balance-exchange-record`



## 2025-01-13

USDⓈ-M Futures & COIN-M Futures

  * The following endpoints will be updated at 2024-01-14:

    * `GET /fapi/v1/historicalTrades`
    * `GET /dapi/v1/historicalTrades`

Changes to the request parameter `limit`:

    * Maximum value changed from 1000 to 500
    * Default value changed from 500 to 100



## 2025-01-06

Portfolio Margin

  * New endpoints to query user rate limit:
    * `GET papi/v1/rateLimit/order`



## 2024-12-19

Portfolio Margin Pro & Portfolio Margin

  * New endpoints for BFUSD mint and redeem(Release on 2024-12-20):
    * `POST sapi/v1/portfolio/mint`
    * `POST sapi/v1/portfolio/redeem`



## 2024-12-17

Options

  * REST API: Added new endpoint `GET /eapi/v1/blockTrades` to get recent block trades

  * Websocket Market Streams: Add field `X` in streams `<symbol>@trade` and `<underlyingAsset>@trade` to show trade type




## 2024-12-02

USDⓈ-M Futures

  * The following error code will be added on 2024-12-03:
    * `-4116`: ClientOrderId is duplicated.
    * `-4117`: Stop order is in triggering process. Please try again later.



## 2024-11-04

USDⓈ-M Futures & COIN-M Futures

  * `GET /fapi/v1/pmExchangeInfo` and `GET /dapi/v1/pmExchangeInfo` will be deprecated on 2024-11-15



## 2024-11-01

Options

  * Add block trade endpoints:
    * `POST eapi/v1/block/order/create`
    * `PUT eapi/v1/block/order/create`
    * `DELETE eapi/v1/block/order/create`
    * `GET eapi/v1/block/order/orders`
    * `POST eapi/v1/block/order/execute`
    * `GET eapi/v1/block/order/execute`
    * `GET eapi/v1/block/user-trades`



## 2024-10-29

Portfolio Margin Pro

  * The following REST endpoints will be adjusted:
    * `POST /sapi/v1/portfolio/repay-futures-switch`: Effective on 2024-11-01, rate limit will be adjusted to 20/day.



Portfolio Margin

  * The following REST endpoints will be adjusted:
    * `POST /papi/v1/repay-futures-switch`: Effective on 2024-11-01, rate limit will be adjusted to 20/day.



## 2024-10-24

Options

  * API Field Removal(Effective 2024-10-28):
    * In the `GET /eapi/v1/exchangeInfo` endpoint, the `id` field will be removed from `optionContracts`, the `id` field will been removed from `optionAssets`, and both the `contractId` and `id` fields have been removed from `optionSymbols`.
    * The `id` and `cid` fields will been removed from the `option_pair` websocket stream



## 2024-10-21

USDⓈ-M Futures & COIN-M Futures

  * Effective from 2024-10-30 00:00 (UTC), the endpoints will only support querying futures trade histories within the most recent 6 months:
    * `GET /fapi/v1/userTrades`
    * `GET /dapi/v1/userTrades`



COIN-M Futures

  * Add new historical data download endpoint:
    * `GET /dapi/v1/order/asyn`: to get Download Id For Futures Order History
    * `GET /dapi/v1/order/asyn/id`: to get Futures Order History Download Link by Id
    * `GET /dapi/v1/trade/asyn`: to get Download Id For Futures Trade History
    * `GET /dapi/v1/trade/asyn/id`: to get Futures Trade History Download Link by Id



## 2024-10-15

Portfolio Margin Pro(Release date 2024-10-18)

  * New endpoint to get Portfolio Margin Pro SPAN Account Info(For Portfolio Margin Pro SPAN users only):
    * `GET /sapi/v2/portfolio/account`
  * New endpoint to get Portfolio Margin Pro Account Balance Info:
    * `GET /sapi/v1/portfolio/balance`



Portfolio Margin

  * New endpoint to get download id for UM futures trade history:
    * `GET /papi/v1/um/trade/asyn`
  * New endpoint to get UM futures trade download link by Id:
    * `GET /papi/v1/um/trade/asyn/id`
  * New endpoint to get download id for UM futures order history:
    * `GET /papi/v1/um/order/asyn`
  * New endpoint to get UM futures order download link by Id:
    * `GET /papi/v1/um/order/asyn/id`
  * New endpoint to get download id for UM futures transaction history:
    * `GET /papi/v1/um/income/asyn`
  * New endpoint to get UM futures transaction download link by Id:
    * `GET /papi/v1/um/income/asyn/id`



## 2024-10-14

USDⓈ-M Futures

  * The following REST endpoints will be adjusted:
    * `POST /fapi/v1/convert/getQuote`: Effective on 2024-10-19, rate limit will be adjusted to 360/hour, 500/day.
    * `POST /fapi/v1/convert/getQuote`: `validTime` can only be set to `10s`



## 2024-10-11

COIN-M Futures

  * **Self-Trade Prevention** :

  * Self-Trade Prevention (aka STP) is added to the system. This prevents orders from matching with orders from the same account, or accounts under the same `tradeGroupId`(currently only support same account). For more detail, please check [FAQ](https://www.binance.com/zh-CN/support/faq/what-is-self-trade-prevention-0941126f6413485b9a3df964a9aa2306)

  * User can set `selfTradePreventionMode` when placing new orders. All symbols support the following STP mode:

    * NONE: No Self-Trade Prevention
    * EXPIRE_TAKER: expire taker order when STP trigger
    * EXPIRE_BOTH: expire taker and maker order when STP trigger
    * EXPIRE_MAKER: expire maker order when STP trigger
  * REST Update:

    * New order status `EXPIRED_IN_MATCH` \- This means that the order expired due to STP being triggered.
    * Add optional parameter `selfTradePreventionMode` in the endpoints below to set order's STP mode:
      * `POST /dapi/v1/order`
      * `POST /dapi/v1/batchOrders`
    * Add new field `selfTradePreventionMode` in response of the endpoints below to show order's STP mode:
      * `POST /dapi/v1/order`
      * `POST /dapi/v1/batchOrders`
      * `GET /dapi/v1/order`
      * `GET /dapi/v1/openOrders`
      * `GET /dapi/v1/allOrders`
      * `PUT /dapi/v1/order`
      * `PUT /dapi/v1/batchOrders`
      * `DELETE /dapi/v1/order`
      * `DELETE /dapi/v1/batchOrders`
  * WEBSOCKET User Data Stream:

    * Add new field `V` in `ORDER_TRADE_UPDATE` to order STP mode.
  * **Price Match**

  * Coin margin future supports order price match function. This feature allows users' LIMIT/STOP/TAKE_PROFIT orders to be placed without entering a price. The price match function will automatically determine the order price in real-time based on the price match mode and the order book.

  * The following priceMatch modes are supported on order level:

    * NONE: no price match
    * OPPONENT: counterparty best price
    * OPPONENT_5: counterparty 5th best price
    * OPPONENT_10: counterparty 10th best price
    * OPPONENT_20: counterparty 20th best price
    * QUEUE: the best price on the same side of the order book
    * QUEUE_5: the 5th best price on the same side of the order book
    * QUEUE_10: the 10th best price on the same side of the order book
    * QUEUE_20: the 20th best price on the same side of the order book
  * Example:

    * User places buy order and set priceMatch as QUEUE_5, the order price will be 5th best bid price of the orderbook
    * User places buy order and set priceMatch as OPPONENT, the order price will be best ask price of the orderbook
  * REST Update:

  * Add optional parameter priceMatch in the endpoints below to set order's priceMatch mode:

    * `POST /dapi/v1/order`
    * `POST /dapi/v1/batchOrders`
  * Add new field priceMatch in response of the endpoints below to show order's priceMatch mode:

    * `POST /dapi/v1/order`
    * `POST /dapi/v1/batchOrders`
    * `GET /dapi/v1/order`
    * `GET /dapi/v1/openOrders`
    * `GET /dapi/v1/allOrders`
    * `PUT /dapi/v1/order`
    * `PUT /dapi/v1/batchOrders`
    * `DELETE /dapi/v1/order`
    * `DELETE /dapi/v1/batchOrders`
  * WEBSOCKET User Data Stream:

    * Add new field `pm` in `ORDER_TRADE_UPDATE` to show price match mode.



## 2024-10-10

USDⓈ-M Futures

  * Binance will update the following endpoints, estimated to be in force on 2024-10-17 03:00 (UTC). After 2024-10-17 03:00 (UTC), the endpoints will support querying futures trade histories that are not older than one year:

    * `GET /fapi/v1/aggTrades`
    * `GET /dapi/v1/aggTrades`
  * Binance will update the following endpoints, estimated to be in force on 2024-10-16 03:00 (UTC). After 2024-10-16 03:00 (UTC), the endpoint will support querying future histories that are not older than 30 days:

    * `GET /fapi/v1/positionMargin/history`



## 2024-10-08

COIN-M Futures

  * The most recent 7-days data is returned by default when requesting the following endpoints. The query time period for these endpoints must be less than 7 days:

    * `GET /dapi/v1/allOrders`
    * `GET /dapi/v1/userTrades`
  * The following endpoints will be adjusted to keep only recent three month data:

    * `GET /dapi/v1/order`
    * `GET /dapi/v1/allOrders`



## 2024-09-27

USDⓈ-M Futures

  * The following websocket user data requests are deprecated:
    * `listenkey@account`
    * `listenkey@balance`
    * `listenkey@position`



COIN-M Futures

  * The following websocket user data requests are deprecated:
    * `listenkey@account`
    * `listenkey@balance`
    * `listenkey@position`



## 2024-09-19

Portfolio Margin

  * New endpoint to repay debt for Margin:
    * `POST /papi/v1/margin/repay-debt`: Repay debt for a margin loan.



## 2024-09-06

Portfolio Margin

  * Update endpoint for Portfolio Margin/Trade(Release date 2024-09-06):

    * `POST /papi/v1/um/order`: add parameter `priceMatch` to support priceMatch for place order
    * `POST/papi/v1/um/conditional/order`: add parameter `priceMatch` to support priceMatch for plac conditional order
    * `PUT /papi/v1/um/order`: add parameter `priceMatch` to ssupport priceMatch for order modification
  * Add new field `priceMatch` in response of the endpoints below to show order's priceMatch:

    * `POST /papi/v1/um/order`
    * `POST/papi/v1/um/conditional/order`
    * `PUT /papi/v1/um/order`
    * `GET /papi/v1/um/orderAmendment`
    * `GET /papi/v1/um/order`
    * `GET /papi/v1/um/openOrder`
    * `GET /papi/v1/um/openOrders`
    * `GET /papi/v1/um/allOrders`
    * `GET /papi/v1/um/conditional/openOrder`
    * `GET /papi/v1/um/conditional/openOrders`
    * `GET /papi/v1/um/conditional/orderHistory`
    * `GET /papi/v1/um/conditional/allOrders`
    * `DELETE /papi/v1/um/order`
    * `DELETE /papi/v1/um/conditional/order`
  * WEBSOCKET

    * Add new field `pm` in `ORDER_TRADE_UPDATE` and `CONDITIONAL_ORDER_TRADE_UPDATE`, which represents priceMatch .



## 2024-09-05

Portfolio Margin Pro

  * New endpoint to query Portfolio Margin Pro Tiered Collateral Rate:
    * `GET /sapi/v2/portfolio/collateralRate`: Query Portfolio Margin Pro Tiered Collateral Rate.



## 2024-09-03

USDⓈ-M Futures

  * User data stream will add `TRADE_LITE` event. `TRADE_LITE` event designed to reduce user data latency by focusing solely on ‘TRADE’ execution type and minimizing the number of user data fields, providing a faster and more efficient experience compared to the original `ORDER_TRADE_UPDATE` user data stream.



## 2024-08-26

USDⓈ-M Futures

  * New endpoint to Future Convert:
    * `GET /fapi/v1/convert/exchangeInfo`
    * `POST /fapi/v1/convert/getQuote`
    * `POST /fapi/v1/convert/acceptQuote`
    * `GET /fapi/v1/convert/orderStatus`



## 2024-08-23

Portfolio Margin

  * New endpoint to toggle UM Futures BNB Burn:
    * `POST /papi/v1/um/feeBurn`: Toggle BNB Burn on UM Futures Trade.
    * `GET /papi/v1/um/feeBurn`: Get UM Futures BNB Burn status.
  * New Endpoints to Query Account Information:
    * `GET /papi/v1/um/accountConfig`: Query user UM account configuration.
    * `GET /papi/v1/um/symbolConfig`: Query user symbol configuration.
    * `GET /papi/v2/um/account`: Compared to `GET /papi/v1/um/account`, this endpoint only returns symbols that the user has positions or open orders in. Configuration-related fields have been removed and can now be queried from `GET /papi/v1/um/symbolConfig` and `GET /papi/v1/um/accountConfig`. The V2 endpoint also offers better performance.



## 2024-08-07

USDⓈ-M Futures

  * The following endpoints IP weight limit will be adjusted from 2024-09-03:

    * REST API:
      * `GET /fapi/v2/balance`: 5->10
      * `GET /fapi/v2/account`: 5->10
      * `GET /fapi/v2/positionRisk`: 5->10
    * Websocket API:
      * `account.status`: 5->10
      * `account.balance`: 5->10
      * `account.position`: 5->10
  * The following WebSocket User Data Requests will be deprecated from 2024-09-03

    * <listenKey>@account
    * <listenKey>@balance
    * <listenKey>@position



Please refer to [annoucement](https://www.binance.com/en/support/announcement/notice-on-upcoming-binance-api-update-2024-09-03-19d4e3cd0758426584dd9686eb56ec64) for api replacement

## 2024-08-06

COIN-M Futures

`GET /dapi/v1/pmExchangeInfo` will be deprecated on August 6,2024 due to removing `notionalLimit` restriction.

## 2024-07-24

USDⓈ-M Futures

#### REST API

  * New Endpoints to Query Account Information:

    * `GET /fapi/v1/symbolConfig`: Query user symbol configuration.
    * `GET /fapi/v1/accountConfig`: Query user account configuration.
    * `GET /fapi/v3/account`: Compared to `GET /fapi/v2/account`, this endpoint only returns symbols that the user has positions or open orders in. Configuration-related fields have been removed and can now be queried from `GET /fapi/v1/symbolConfig` and `GET /fapi/v1/accountConfig`. The V3 endpoint also offers better performance.
    * `GET /fapi/v3/balance`: Query user account balance.
  * New Endpoints to Query Trade Information:

    * `GET /fapi/v3/positionRisk`: Compared to `GET /fapi/v2/positionRisk`, this endpoint only returns symbols that the user has positions or open orders in. Configuration-related fields have been removed and can now be queried from `GET /fapi/v1/symbolConfig`. The V3 endpoint also offers better performance.



#### WebSocket API

  * New Endpoints to Query Account Information:
    * `v2/account.status`: Compared to `account.status`, this endpoint only returns symbols that the user has positions or open orders in. Configuration-related fields have been removed and can now be queried from `GET /fapi/v1/symbolConfig` and `GET /fapi/v1/accountConfig`. The V2 endpoint also offers better performance.
    * `v2/account.balance`: Query user account balance.
    * `v2/account.position`: Compared to `account.position`, this endpoint only returns symbols that the user has positions or open orders in. Configuration-related fields have been removed and can now be queried from `GET /fapi/v1/symbolConfig`. The V2 endpoint also offers better performance.



**Deprecation Notice:**

  * The following endpoints will be deprecated in the coming months (exact date to be announced later). Please switch to the new endpoints listed above:
    * REST API:
      * `GET /fapi/v2/balance`
      * `GET /fapi/v2/account`
      * `GET /fapi/v2/positionRisk`
    * Websocket API:
      * `account.status`
      * `account.balance`
      * `account.position`



* * *

## 2024-07-17

Portfolio Margin

REST API

  * The response field `marginAsset` in `GET /papi/v1/um/userTrades` will be removed on 2024-07-17.



* * *

## 2024-06-19

USDⓈ-M Futures

REST API

  * The response field `marginAsset` in `GET /fapi/v1/userTrades` will be removed on 2024-06-25.



* * *

## 2024-05-22

USDⓈ-M Futures

REST API & Websocket API

  * New endpoint to toggle BNB Burn:
    * `POST /fapi/v1/feeBurn` to toggle BNB Burn on Futures Trade.
    * `GET /fapi/v1/feeBurn` to get BNB Burn status.



* * *

## 2024-04-19

USDⓈ-M Futures

REST API & Websocket API

  * The new field listenKey will be integrated into the response received from the `PUT /fapi/v1/listenKey` endpoint and WebSocket api `userDataStream.ping`. This enhancement will allow users to view the key that has been kept alive. This update is scheduled to take effect on 2024-04-25.


    
    
    Code
    
    {
        "listenKey": "3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg"
    }

* * *

## 2024-04-09

USDⓈ-M Futures/ COIN-M Futures / Portfolio Margin

WEBSOCKET API

  * Good-Till-Cancel (GTC) timeInForce will have a one-year validity period after order placement. GTC orders longer than one-year will be automatically canceled. This applies to all order types including reduceOnly but does not affect part-filled orders or strategy trading or copy-trading orders.



* * *

## 2024-04-01

USDⓈ-M Futures

WEBSOCKET API

  * Websocket API is now available and can be accessed through this URL: `wss://ws-fapi.binance.com/ws-fapi/v1`
  * WebSocket API allows placing orders, canceling orders, etc. through a WebSocket connection.
  * WebSocket API is a separate service from WebSocket Market Data streams. I.e., placing orders and listening to market data requires two separate WebSocket connections.
  * WebSocket API is subject to the same Filter and Rate Limit rules as REST API.
  * WebSocket API and REST API are functionally equivalent: they provide the same features, accept the same parameters, return the same status and error codes.



* * *

## 2024-03-11

USDⓈ-M Futures

REST

  * Add new Account Endpoints:
    * `GET /fapi/v1/rateLimit/order`: query user order rate limits



* * *

## 2024-02-09

USDⓈ-M Futures

Binance Future is doing Websocket Service upgrade and the upgrade impacts the following：

  * Before upgrade:

    * The websocket server will send a ping frame every 3 minutes. If the websocket server does not receive a pong frame back from the connection within a 10 minute period, the connection will be disconnected. Unsolicited pong frames are allowed.
  * After upgrade:

    * Websocket server will send a `ping frame` every 3 minutes.
      * If the websocket server does not receive a `pong frame` back from the connection within a 10 minute period, the connection will be disconnected.
      * When you receive a ping, you must send a pong with a copy of ping's payload as soon as possible.
      * Unsolicited `pong frames` are allowed, but will not prevent disconnection. **It is recommended that the payload for these pong frames are empty.**



* * *

## 2024-01-24

USDⓈ-M Futures

Testnet WEBSOCKET

  * The Websocket baseurl for **testnet** is updated to "wss://fstream.binancefuture.com"



* * *

## 2024-01-19

Portfolio Margin

  * REST
    * New endpoints `PUT /papi/v1/um/order` and `PUT /papi/v1/cm/order` to support UM/CM limit order modify
    * New endpoints `GET /papi/v1/um/orderAmendment` and `GET /papi/v1/cm/orderAmendment` to get UM/CM order modify history



* * *

## 2024-01-11

Portfolio Margin

  * **Self-Trade Prevention(Released):**

  * Self-Trade Prevention (aka STP) will be added to the system. This will prevent orders from matching with orders from the same account, or accounts under the same `tradeGroupId`. For more detail, please check [FAQ](https://www.binance.com/en/support/faq/what-is-self-trade-prevention-stp-0941126f6413485b9a3df964a9aa2306)

  * User can set `selfTradePreventionMode` when placing new orders. All symbols support the following STP mode:

    * NONE: No Self-Trade Prevention
    * EXPIRE_TAKER: expire taker order when STP trigger
    * EXPIRE_BOTH: expire taker and maker order when STP trigger
    * EXPIRE_MAKER: expire maker order when STP trigger
  * REST Update:

    * New order status `EXPIRED_IN_MATCH` \- This means that the order expired due to STP being triggered.

    * GET /papi/v1/um/account: Add new field `tradeGroupId` in response to show user's tradeGroupId

    * Add optional parameter `selfTradePreventionMode` in the endpoints below to set order's STP mode:

      * POST /papi/v1/um/order
      * POST/papi/v1/um/conditional/order
      * POST /papi/v1/margin/order
      * POST /papi/v1/margin/order/oco
    * Add new field `selfTradePreventionMode` in response of the endpoints below to show order's STP mode:

      * POST /papi/v1/um/order

      * POST/papi/v1/um/conditional/order

      * GET /papi/v1/um/order

      * GET /papi/v1/um/openOrder

      * GET /papi/v1/um/openOrders

      * GET /papi/v1/um/allOrders

      * GET /papi/v1/um/conditional/openOrder

      * GET /papi/v1/um/conditional/openOrders

      * GET /papi/v1/um/conditional/orderHistory

      * GET /papi/v1/um/conditional/allOrders

      * DELETE /papi/v1/um/order

      * DELETE /papi/v1/um/conditional/order

      * DELETE /papi/v1/margin/order

      * DELETE /papi/v1/margin/allOpenOrders

      * DELETE /papi/v1/margin/orderList

      * GET /papi/v1/margin/order

      * GET /papi/v1/margin/allOrders

      * GET /papi/v1/margin/orderList

      * GET /papi/v1/margin/allOrderList

      * GET /papi/v1/margin/openOrderList

  * WEBSOCKET User Data Stream:

    * Add new field `V` in `ORDER_TRADE_UPDATE` and `CONDITIONAL_ORDER_TRADE_UPDATE` to order STP mode.
    * New fields for `executionReport` (These fields will only appear if the order has expired due to STP trigger)
      * `u` \- `tradeGroupId`
      * `v` \- `preventedMatchId`
      * `U` \- `counterOrderId`
      * `A` \- `preventedQuantity`
      * `B` \- `lastPreventedQuantity`
  * **Good Till Date TIF(Released)**

  * USDⓈ margin future will support Good To Date TIF. Orders with the TIF set to GTD will be automatically canceled by the `goodTillDate` time.

  * REST Update:

    * Add optional parameter `goodTillDate` in the endpoints below to set order's `goodTillDate` :

      * POST /papi/v1/um/order
      * POST/papi/v1/um/conditional/order
    * Add new field `goodTillDate` in response of the endpoints below to show order's `goodTillDate`:

      * POST /papi/v1/um/order
      * POST/papi/v1/um/conditional/order
      * GET /papi/v1/um/order
      * GET /papi/v1/um/openOrder
      * GET /papi/v1/um/openOrders
      * GET /papi/v1/um/allOrders
      * GET /papi/v1/um/conditional/openOrder
      * GET /papi/v1/um/conditional/openOrders
      * GET /papi/v1/um/conditional/orderHistory
      * GET /papi/v1/um/conditional/allOrders
      * DELETE /papi/v1/um/order
      * DELETE /papi/v1/um/conditional/order
  * WEBSOCKET User Data Stream:

    * Add new field `gtd` in `ORDER_TRADE_UPDATE` and `CONDITIONAL_ORDER_TRADE_UPDATE` to order good till date.
  * **Breakeven Price(Released)**

  * REST Update

    * Add new field `breakEvenPrice` in The following endpoint
      * GET /papi/v1/um/account
      * GET /papi/v1/um/positionRisk
      * GET /papi/v1/cm/account
      * GET /papi/v1/cm/positionRisk
  * WEBSOCKET

    * New field `bep` represents Break-Even Price in position `P` of payload to event: Balance and Position Update – "e": "ACCOUNT_UPDATE"



* * *

## 2024-01-08

USDⓈ-M Futures

REST

  * Update endpoint for Account/Trade(Release date 2023-01-11):
    * `PUT /fapi/v1/order`: add parameter `priceMatch` to support priceMatch for order modification
    * `PUT /fapi/v1/batchOrders`: add parameter `priceMatch` to support priceMatch for order modification
    * Order modification will preserve the original `selfTradePreventionMode` of the order



* * *

## 2023-12-12

USDⓈ-M Futures

WEBSOCKET

  * Update speed for stream `!bookTicker` will be modified from real-time to every 5 seconds on starting December 20, 2023. Individual Symbol Book Ticker Streams `<symbol>@bookticker` will remain unaffected by this update



* * *

## 2023-11-15

USDⓈ-M Futures

REST

  * Add new Market Data Endpoints:
    * `GET /fapi/v2/ticker/price`: this is v2 endpoint for querying latest price. It has same parameters and response as the `GET /fapi/v1/ticker/price`, and it offers lower latency and consume less of the IP rate limit. Please note that the `GET /fapi/v1/ticker/price` will be deprecated in the future, with the exact timing to be determined.



WEBSOCKET

  * Binance Futures will retire the `wss://fstream-auth.binance.com` domain at 2023-12-15 06:00. API users are advised to establish a new WebSocket connection to `wss://fstream.binance.com`. Please note that the connection method for `wss://fstream.binance.com` is different from that of `wss://fstream-auth.binance.com`. For instance:
    * `wss://fstream-auth.binance.com/ws/<ListenKey>?listenKey=<ListenKey>` should change to `wss://fstream.binance.com/ws/<ListenKey>`



* * *

## 2023-11-01

COIN-M Futures

REST

  * Update on `GET dapi/v1/fundingRate`:
    * add response field `markPrice` to display mark price associated with a particular funding fee charge



* * *

## 2023-11-01

USDⓈ-M Futures

REST

  * Add new Market Data Endpoints:

    * `GET /futures/data/basis`: query basis data
  * Update on `GET /fapi/v1/fundingRate`:

    * add response field `markPrice` to display mark price associated with a particular funding fee charge



* * *

## 2023-10-19

COIN-M Futures

REST

  * New Market Data Endpoints
    * `GET /futures/data/delivery-price`: query quarterly contract settlement price
  * Update Rate Limit to 1000/5min/IP on Market Data Endpoints below:
    * `GET /futures/data/openInterestHist`
    * `GET /futures/data/topLongShortAccountRatio`
    * `GET /futures/data/topLongShortPositionRatio`
    * `GET /futures/data/globalLongShortAccountRatio`
    * `GET /futures/data/takerlongshortRatio`



* * *

## 2023-10-19

European Options

Binance Option is doing Websocket Service upgrade and the upgrade impacts the following：

  * Before upgrade:

    * The websocket server will send a ping frame every 5 minutes. If the websocket server does not receive a pong frame back from the connection within a 15 minute period, the connection will be disconnected. Unsolicited pong frames are allowed.
    * To connect websocket server without subscription, user can connect by using
      * `wss://nbstream.binance.com/eoptions/ws`
      * `wss://nbstream.binance.com/eoptions/stream`
      * `wss://nbstream.binance.com/eoptions/ws/`
      * `wss://nbstream.binance.com/eoptions/stream/`
  * After upgrade:

    * The websocket server will send a ping frame every 3 minutes. If the websocket server does not receive a pong frame back from the connection within a 10 minute period, the connection will be disconnected. Unsolicited pong frames are allowed.
    * To connect websocket server without subscription:
    * Connect websocket server with subscription:
      * `wss://nbstream.binance.com/eoptions/ws`
      * `wss://nbstream.binance.com/eoptions/stream`
      * `/` at the end is no longer supported
    * Raw stream like `wss://nbstream.binance.com/eoptions/illegal_parameter/stream?steams=<streamName>` or `wss://fstream.binance.com/illegal_parameter/ws/<streamName>`is not supported, please use remove `illegal_parameter/` before `/ws` and `/stream`.



* * *

## 2023-10-19

USDⓈ-M Futures

REST

  * New Market Data Endpoints
    * `GET /futures/data/delivery-price`: query quarterly contract settlement price
  * Update Rate Limit to 1000/5min/IP on Market Data Endpoints below:
    * `GET /futures/data/openInterestHist`
    * `GET /futures/data/topLongShortAccountRatio`
    * `GET /futures/data/topLongShortPositionRatio`
    * `GET /futures/data/globalLongShortAccountRatio`
    * `GET /futures/data/takerlongshortRatio`
  * Update Rate Limit to 500/5min/IP on Market Data Endpoints below:
    * `GET /fapi/v1/fundingRate`
    * `GET /fapi/v1/fundingInfo`



* * *

## 2023-10-16

COIN-M Futures

REST

  * New Market Data Endpoints
    * `GET /dapi/v1/constituents`: query index constituents



* * *

## 2023-10-16

USDⓈ-M Futures

REST

  * New Market Data Endpoints
    * `GET /fapi/v1/constituents`: query index constituents



* * *

## 2023-10-11

USDⓈ-M Futures

REST

  * Account Endpoints IP Weight Update:
    * `GET /fapi/v1/income/asyn`: 5->1000
    * `GET /fapi/v1/order/asyn`: 5->1000
    * `GET /fapi/v1/trade/asyn`: 5->1000
    * `GET /fapi/v1/income/asyn/id`: 5->10
    * `GET /fapi/v1/order/asyn/id`: 5->10
    * `GET /fapi/v1/trade/asyn/id`: 5->10



* * *

## 2023-09-25

COIN-M Futures

REST

  * New Market Data Endpoints Update
    * `GET /dapi/v1/fundingInfo`: query adjusted funding info



* * *

## 2023-09-25

USDⓈ-M Futures

REST

  * New Market Data Endpoints Update
    * `GET /fapi/v1/fundingInfo`: query adjusted funding info



* * *

## 2023-09-22

Portfolio Margin

  * Update on endpoints:

    * `GET /papi/v1/um/positionRisk`: add response field `liquidationPrice`
    * `GET /papi/v1/cm/positionRisk`: add response field `liquidationPrice`
    * `GET /papi/v1/um/leverageBracket`: add response field `notionalCoef`
    * `GET /papi/v1/cm/leverageBracket`: add response field `notionalCoef`
  * Websocket User Data Streams Update:

    * `outboundAccountPosition` event add new field updateId `U`
    * `balanceUpdate` event add new field updateId `U`



* * *

## 2023-09-20

COIN-M Futures

REST

  * Update on `GET /dapi/v1/ticker/bookTicker`:

    * add response field `lastUpdateId`
  * Update on `GET /dapi/v1/account`:

    * add response field `updateTime` in `assets`



* * *

## 2023-09-20

USDⓈ-M Futures

REST

  * Update on `GET /fapi/v1/ticker/bookTicker`:
    * add response field `lastUpdateId`



* * *

## 2023-09-19

USDⓈ-M Futures
    
    
    Code
    
    {
        "code": -1008,
        "msg": "Server is currently overloaded with other requests. Please try again in a few minutes."
    }

  * New error code message for http `503` return code, endpoints below might have this response during high traffic:
    * `POST /fapi/v1/order`
    * `PUT /fapi/v1/order`
    * `DELETE /fapi/v1/order`
    * `POST /fapi/v1/batchOrder`
    * `PUT /fapi/v1/batchOrder`
    * `DELETE /fapi/v1/batchOrder`
    * `POST /fapi/v1/order/test`
    * `DELETE /fapi/v1/allOpenOrders`
  * This is a failure API operation and you can resend your request if you need.



* * *

## 2023-09-07

COIN-M Futures

REST

  * New endpoint`GET /dapi/v1/income/asyn`to get Download Id For Futures Transaction History
  * New endpoint`GET /dapi/v1/income/asyn/id`to get Futures Transaction History Download Link by Id



* * *

## 2023-09-05

USDⓈ-M Futures

  * As per the [announcement](https://www.binance.com/en/support/announcement/binance-futures-launches-self-trade-prevention-stp-function-for-usd%E2%93%A2-margined-futures-on-api-32916877372243d69154c345200e34b8), Self Trade Prevention is enabled at **2023-09-05**.
  * Price Match/ Good Till Date TIF/ Breakeven Price(detail in 2023-08-29 changelog) are released at **2023-09-05**



* * *

## 2023-09-04

Portfolio Margin

**Expect 2023-09-07 Release**

  * Overall papi order ratelimit change from 2400 orders/min to 1200 orders/min, impacted endpoints are:
    * POST `/papi/v1/um/order`
    * POST `/papi/v1/cm/order`
    * POST `/papi/v1/margin/order`
    * POST `/papi/v1/margin/order/oco`
    * POST `/papi/v1/um/conditional/order`
    * POST `/papi/v1/cm/conditional/order`



* * *

## 2023-08-31

COIN-M Futures

Binance Future is doing Websocket Service upgrade and the upgrade impacts the following：

  * Before upgrade:

    * The websocket server will send a ping frame every 5 minutes. If the websocket server does not receive a pong frame back from the connection within a 15 minute period, the connection will be disconnected. Unsolicited pong frames are allowed.
  * After upgrade:

    * The websocket server will send a ping frame every 3 minutes. If the websocket server does not receive a pong frame back from the connection within a 10 minute period, the connection will be disconnected. Unsolicited pong frames are allowed.



* * *

## 2023-08-31

USDⓈ-M Futures

Binance Future is doing Websocket Service upgrade and the upgrade impacts the following：

  * Before upgrade:

    * The websocket server will send a ping frame every 5 minutes. If the websocket server does not receive a pong frame back from the connection within a 15 minute period, the connection will be disconnected. Unsolicited pong frames are allowed.
  * After upgrade:

    * The websocket server will send a ping frame every 3 minutes. If the websocket server does not receive a pong frame back from the connection within a 10 minute period, the connection will be disconnected. Unsolicited pong frames are allowed.



* * *

## 2023-08-29

European Options

REST

  * `GET /eapi/v1/account`: add new field `riskLevel` to show account risk level
  * `GET /eapi/v1/marginAccount`: add new field`riskLevel` to show account risk level



Websocket User Data Stream

  * Add new event `RISK_LEVEL_CHANGE` to show account riskLevel change



* * *

## 2023-08-29

USDⓈ-M Futures

  * **Self-Trade Prevention(Release Date TBD)** :

  * Self-Trade Prevention (aka STP) will be added to the system. This will prevent orders from matching with orders from the same account, or accounts under the same `tradeGroupId`. For more detail, please check [FAQ](https://www.binance.com/zh-CN/support/faq/what-is-self-trade-prevention-0941126f6413485b9a3df964a9aa2306)

  * User can set `selfTradePreventionMode` when placing new orders. All symbols support the following STP mode:

    * NONE: No Self-Trade Prevention
    * EXPIRE_TAKER: expire taker order when STP trigger
    * EXPIRE_BOTH: expire taker and maker order when STP trigger
    * EXPIRE_MAKER: expire maker order when STP trigger
  * REST Update:

    * New order status `EXPIRED_IN_MATCH` \- This means that the order expired due to STP being triggered.
    * `GET /fapi/v2/account`: Add new field `tradeGroupId` in response to show user's tradeGroupId
    * Add optional parameter `selfTradePreventionMode` in the endpoints below to set order's STP mode:
      * `POST /fapi/v1/order`
      * `POST /fapi/v1/batchOrders`
    * Add new field `selfTradePreventionMode` in response of the endpoints below to show order's STP mode:
      * `POST /fapi/v1/order`
      * `POST /fapi/v1/batchOrders`
      * `POST /fapi/v1/order`
      * `POST /fapi/v1/order`
      * `GET /fapi/v1/order`
      * `GET /fapi/v1/openOrders`
      * `GET /fapi/v1/allOrders`
      * `PUT /fapi/v1/order`
      * `PUT /fapi/v1/batchOrders`
      * `DELETE /fapi/v1/order`
      * `DELETE /fapi/v1/batchOrders`
  * WEBSOCKET User Data Stream:

    * Add new field `V` in `ORDER_TRADE_UPDATE` to order STP mode.



* * *

## 2023-08-25

COIN-M Futures

  * Binance Future is doing Websocket Service upgrade and the upgrade impacts the following：
    * Connect websocket server without subscription:
      * Before upgrade, user can connect by using:
        * `wss://dstream.binance.com/ws`
        * `wss://dstream.binance.com/stream`
        * `wss://dstream.binance.com/ws/`
        * `wss://dstream.binance.com/stream/`
      * After upgrade, user can connect by using:
        * `wss://dstream.binance.com/ws`
        * `wss://dstream.binance.com/stream`
        * `/` at the end is no longer supported
    * Connect websocket server with subscription:
      * Raw stream like `wss://dstream.binance.com/illegal_parameter/stream?steams=<streamName>` or `wss://dstream.binance.com/illegal_parameter/ws/<streamName>`is not supported, please use remove `illegal_parameter/` before `/ws` and `/stream`.



* * *

## 2023-08-19

USDⓈ-M Futures

  * Binance Future is doing Websocket Service upgrade and the upgrade impacts the following：
    * Connect websocket server without subscription:
      * Before upgrade, user can connect by using:
        * `wss://fstream.binance.com/ws`
        * `wss://fstream.binance.com/stream`
        * `wss://fstream.binance.com/ws/`
        * `wss://fstream.binance.com/stream/`
      * After upgrade, user can connect by using:
        * `wss://fstream.binance.com/ws`
        * `wss://fstream.binance.com/stream`
        * `/` at the end is no longer supported
    * Connect websocket server with subscription:
      * Raw stream like `wss://fstream.binance.com/illegal_parameter/stream?steams=<streamName>` or `wss://fstream.binance.com/illegal_parameter/ws/<streamName>`is not supported, please use remove `illegal_parameter/` before `/ws` and `/stream`.



* * *

## 2023-08-18

Portfolio Margin

  * New endpoints for Query Order:
    * `GET /papi/v1/margin/order`: Query Margin Account Order
    * `GET /papi/v1/margin/openOrders`: Query Current Margin Open Order
    * `GET /papi/v1/margin/allOrders`: Query All Margin Account Orders
    * `GET /papi/v1/margin/orderList`: Query Margin Account's OCO
    * `GET /papi/v1/margin/allOrderList`: Query Margin Account's all OCO
    * `GET /papi/v1/margin/openOrderList`: Query Margin Account's Open OCO
    * `GET /papi/v1/margin/myTrades`: Query Margin Account's Trade List



* * *

## 2023-08-14

COIN-M Futures

  * Update endpoint for Account/Trade:
    * `GET /dapi/v1/income`: Add parameter `page` for pagination



* * *

## 2023-08-14

USDⓈ-M Futures

  * Update endpoint for Account/Trade:
    * `GET /fapi/v1/income`: Add parameter `page` for pagination



* * *

## 2023-07-28

Portfolio Margin

  * New endpoints for account:
    * `POST /papi/v1/asset-collection`: Fund Collection by Asset



* * *

## 2023-07-21

European Options

REST

  * New endpoint`GET /eapi/v1/income/asyn`to get Download Id For Option Transaction History
  * New endpoint`GET /eapi/v1/income/asyn/id`to get Option Transaction History Download Link by Id



* * *

## 2023-07-20

Portfolio Margin

  * New endpoints for account:
    * `GET /papi/v1/um/adlQuantile`: UM Position ADL Quantile Estimation
    * `GET /papi/v1/cm/adlQuantile`: CM Position ADL Quantile Estimation



* * *

## 2023-07-19

COIN-M Futures

REST

  * Add field `notionalCoef` in `GET /dapi/v2/leverageBracket` to show the bracket multiplier comparing to default leverage bracket



* * *

## 2023-07-18

Portfolio Margin

  * New endpoints for account:
    * `POST /papi/v1/repay-futures-switch`: Change Auto-repay-futures Status
    * `GET /papi/v1/repay-futures-switch`: Get Auto-repay-futures Status
    * `POST /papi/v1/repay-futures-negative-balance`: Repay futures Negative Balance



* * *

## 2023-07-18

USDⓈ-M Futures

REST

  * Add field `notionalCoef` in `GET /fapi/v1/leverageBracket` to show the bracket multiplier comparing to default leverage bracket



* * *

## 2023-07-13

European Options

Websocket Market Streams

  * These change will be effective from 2023-07-14:
    * Add field `T` in streams `<symbol>@ticker` and `<underlyingAsset>@ticker@<expirationDate>` to show transaction time
    * Add field `E` in stream `<symbol>@depth<levels>` to show event time



* * *

## 2023-07-13

Portfolio Margin

  * New USER DATA STREAM event `riskLevelChange`（effective 2023-07-14）



* * *

## 2023-07-12

COIN-M Futures

REST

  * New field `breakEvenPrice` represents Break-Even Price in position of response to:
    * GET /dapi/v1/account (HMAC SHA256)
    * GET /dapi/v1/positionRisk (HMAC SHA256)



WEBSOCKET

  * New field `bep` represents Break-Even Price in position `P` of payload to event: Balance and Position Update – "e": "ACCOUNT_UPDATE"



* * *

## 2023-07-11

Portfolio Margin

REST

  * Add new endpoint `POST /papi/v1/ping` for connectivity test



* * *

## 2023-07-04

USDⓈ-M Futures

REST

  * The following endpoints will be adjust to keep only recent three month data：
    * `GET /fapi/v1/order`(effective 2023-07-27)
    * `GET /fapi/v1/allOrders`(effective 2023-07-27)
    * `GET /fapi/v1/userTrades`(exact time TBD)
  * Please maintain and record old order/trade infomation or switch querying historical order/trade using new endpoint below:
    * New endpoint`GET /fapi/v1/order/asyn`to get Download Id For Futures Order History
    * New endpoint`GET /fapi/v1/order/asyn/id`to get Futures Order History Download Link by Id
    * New endpoint`GET /fapi/v1/trade/asyn`to get Download Id For Futures Trade History
    * New endpoint`GET /fapi/v1/trade/asyn/id`to get Futures Trade History Download Link by Id



* * *

## 2023-06-28

USDⓈ-M Futures

**Notice:**

REST

  * The following endpoints will no longer be supported from 2023-07-15:
    * `GET /fapi/v1/account`
    * `GET /fapi/v1/balance`
    * `GET /fapi/v1/positionRisk`
  * Please switch to corresponding v2 endpoints:
    * `GET /fapi/v2/account`
    * `GET /fapi/v2/balance`
    * `GET /fapi/v2/positionRisk`



* * *

## 2023-06-22

COIN-M Futures

**Notice:**

WEBSOCKET

  * Raw stream like **/ws? <streamName>** is not supported, for example `wss://dstream.binance.com/ws?btcusd@depth` is invalid.
  * Sending websocket message with invalid JSON format will cause disconnection now, returning this error `{"error":{"code":3,"msg":"Invalid JSON: expected value at line 1 column 1"}}`



* * *

## 2023-06-22

USDⓈ-M Futures

**Notice:**

WEBSOCKET

  * Raw stream like **/ws? <streamName>** is not supported, for example `wss://fstream.binance.com/ws?btcusdt@depth` is invalid.
  * Sending websocket message with invalid JSON format will cause disconnection now, returning this error `{"error":{"code":3,"msg":"Invalid JSON: expected value at line 1 column 1"}}`



* * *

## 2023-06-19

Portfolio Margin

REST

  * Add fields `CONTRACT_PRICE`，`priceProtect` in endpoints `POST /papi/v1/um/conditional/order` and `POST/papi/v1/cm/conditional/order`



* * *

## 2023-06-16

USDⓈ-M Futures

**Notice:**

  * It is recommended to use standard HTTP request formats, non-standard request formats will not be supported in fapi, below are some examples for correct code practice:
    * Escaping (") with '\x22' is no longer supported, please use the standard '%22' instead. It is necessary to URL encode the square brackets [] and the double quotes（"）inside the square brackets.
          
          Code
          
          DELETE /fapi/v1/batchOrders?origClientOrderIdList=
          
          Unsupported:

[\x229151944646313025900\x22]
          
          Code
          
          Suggest:

["9151944646313025900"]
          
          Code
          
          --After URL encode--

DELETE /fapi/v1/batchOrders?origClientOrderIdList=%5B%229151944646313025900%22%5D

    * Non-standard nested JSON formats are not supported,
          
          Code
          
          POST /fapi/v1/batchOrders?batchOrders=
          
          Unsupported:

["{\"type\":\"LIMIT\",\"timeInForce\":\"GTC\"}"]
          
          Code
          
          Suggest:

[{"type":"LIMIT","timeInForce":"GTC"}]
          
          Code
          
          --After URL encode--

POST /fapi/v1/batchOrders?batchOrders=%5B%7B%22type%22%3A%22LIMIT%22%2C%22timeInForce%22%3A%22GTC%22%7D%5D

    * Using incorrect data type is not supported
          
          Code
          
          DELETE /fapi/v1/batchOrders?orderIdList=
          
          As the data type of the 'orderIdList' parameter is LIST\<LONG\>
          Unsupported:

["159856286502","159856313662"]
          
          Code
          
          Suggest:

[159856286502,159856313662]
          
          Code
          
          --After URL encode--

DELETE /fapi/v1/batchOrders?orderIdList=%5B159856286502%2C159856313662%5D

    * Invalid whitespace characters from the request parameters are not supported
          
          Code
          
          Unsupported:

POST symbol=BTCUSDT& price= 40000.0 & signature=2d24a314
          
          Code
          
          Suggest:

POST symbol=BTCUSDT&&price=40000.0&signature=2d24a314

    * Passing empty values in request parameters is not supported
          
          Code
          
          Unsupported:

GET symbol=BTCUSDT&orderId=&signature=2d24a314

Suggest:

GET symbol=BTCUSDT&signature=2d24a314




* * *

## 2023-06-14

COIN-M Futures

WEBSOCKET

  * New field `i` for quote asset and index price added in streams `<symbol>@markPrice` and `<pair>@markPrice`



* * *

## 2023-06-14

USDⓈ-M Futures

WEBSOCKET

  * New WebSocket stream `!assetIndex@arr`OR`<assetSymbol>@assetIndex` for multi-assets mode asset index update



* * *

## 2023-06-01

Portfolio Margin

REST

  * The endpoints below will be deployed on 2023-06-02:
    * New endpoints `GET /papi/v1/um/income` and `GET /papi/v1/cm/income` to query portfolio margin UM/CM income history
    * New endpoints `GET /papi/v1/um/account` and `GET /papi/v1/cm/account` to query portfolio margin UM/CM account history



* * *

## 2023-05-31

USDⓈ-M Futures

WEBSOCKET

  * Add user data stream:
    * new event `CONDITIONAL_ORDER_TRIGGER_REJECT` to the order reject reason for triggered TP/SL order



* * *

## 2023-05-30

European Options

General Information on Endpoints

  * For `GET` endpoints, parameters must be sent as a `query string` without setting content type in the http headers.



* * *

## 2023-05-05

USDⓈ-M Futures

REST

  * New endpoints `PUT /fapi/v1/order` and `PUT /fapi/v1/batchOrders` to support limit order modify
  * New endpoint `GET /fapi/v1/orderAmendment` to get order modify history



WEBSOCKET

  * New type "AMENDMENT" as order modify in Execution Type `x` of Order Update event `ORDER_TRADE_UPDATE`



* * *

## 2023-05-04

Portfolio Margin

  * API doc for portfolio margin



* * *

## 2023-04-17

COIN-M Futures

**RELEASE DATE TBD**

The `recvWindow` check will also be performed when orders reach matching engine. The `recvWindow` will be checked more precisely on order placing endpoints.
    
    
    Code
    
    {
        "code": -4188,
        "msg": "Timestamp for this request is outside of the ME recvWindow"
    }

**recvWindow Logic Before Release:**

  * The order placing requests are valid if `recvWindow` \+ `timestamp` => REST API service server `timestamp`



**recvWindow Logic After Release:**

  * Add new recwWindow check: the order placing requests are valid if `recvWindow` \+ `timestamp` => matching engine `timestamp`

  * Impacted Endpoints:

    * POST /dapi/v1/order (HMAC SHA256)
    * PUT /dapi/v1/order (HMAC SHA256)
    * POST /dapi/v1/batchOrders (HMAC SHA256)
    * PUT /dapi/v1/batchOrders (HMAC SHA256)



* * *

## 2023-04-17

USDⓈ-M Futures

**RELEASE DATE 2023-04-18**

The `recvWindow` check will also be performed when orders reach matching engine. The `recvWindow` will be checked more precisely on order placing endpoints.
    
    
    Code
    
    {
        "code": -5028,
        "msg": "Timestamp for this request is outside of the ME recvWindow"
    }

**recvWindow Logic Before Release:**

  * The order placing requests are valid if `recvWindow` \+ `timestamp` => REST API service server `timestamp`



**recvWindow Logic After Release:**

  * Add new recwWindow check: the order placing requests are valid if `recvWindow` \+ `timestamp` => matching engine `timestamp`

  * Impacted Endpoints:

    * POST /fapi/v1/order
    * PUT /fapi/v1/order
    * POST /fapi/v1/batchOrders
    * PUT /fapi/v1/batchOrders



* * *

## 2023-03-28

USDⓈ-M Futures

**Referal Rebate Logic Before Release**

  * For every trade，the referal rebate balance change will be reflected in `ACCOUNT_UPDATE` event of USER-DATA-STREAM in real time：


    
    
    Code
    
    {
      "e": "ACCOUNT_UPDATE",
      "T": 1679974782150,
      "E": 1679974782155,
      "a": {
        "B": [
       {
           "a": "USDT",
           "wb": "685.31478079",
           "cw": "677.17212454",
           "bc": "0.00258637"
          }
     ],
        "P": [],
        "m": "ADMIN_DEPOSIT"
      }
    }

**Referal Rebate Logic After Release**

  * Referral rebates are aggregated every 20 minutes and reflected as a single push in the `ACCOUNT_UPDATE` event of the USER-DATA-STREAM, showing the total sum of rebates earned from multiple referrals.



* * *

## 2023-03-08

USDⓈ-M Futures

**RELEASE DATE 2023-03-22**

**Order Logic Before Release:**

  * When placing order with `timeInForce` `FOK` or `GTX`(Post-only), user will get order response with `status` = “NEW“ and corresponding `order_trade_update` with `x` = “NEW”, `X` = “NEW”. If the orders can't meet execution criteria, user will receive another websocket `order_trade_update` message `x` = “EXPIRED”, `X` = “EXPIRED”. The order can be found in `GET /fapi/v1/order` or `GET /fapi/v1/allOrders`.


    
    
    Code
    
    {
        "code": -5021,
        "msg": "Due to the order could not be filled immediately, the FOK order has been rejected. The order will not be recorded in the order history"
    }

**Order Logic After Release:**

  * When placing order with `timeInForce` `FOK` or `GTX`(Post-only), if the order can't meet execution criteria, order will get rejected directly and receive error response, no `order_trade_update` message in websocket. The order can't be found in `GET /fapi/v1/order` or `GET /fapi/v1/allOrders`.


    
    
    Code
    
    {
        "code": -5022,
        "msg": "Due to the order could not be executed as maker, the Post Only order will be rejected. The order will not be recorded in the order history"
    }

  * Impacted Endpoints:
    * POST /fapi/v1/order
    * POST /fapi/v1/batchOrders
    * GET /fapi/v1/order
    * GET /fapi/v1/allOrders



* * *

## 2023-02-02

European Options

REST

  * Endpoint `POST /eapi/v1/transfer` is disabled.



* * *

## 2023-01-11

European Options

REST

  * Add endpoint `GET /eapi/v1/order` to check order status.



* * *

## 2023-01-04

USDⓈ-M Futures

WEBSOCKET

  * Delete Order Status `NEW_INSURANCE` and `NEW_ADL` in Order Update Event



* * *

## 2022-12-16

COIN-M Futures

WEBSOCKET

  * New WebSocket stream `!contractInfo` for symbol information update



* * *

## 2022-12-16

USDⓈ-M Futures

WEBSOCKET

  * New WebSocket stream `!contractInfo` for symbol information update



* * *

## 2022-12-13

European Options

WEBSOCKET

  * Add `u` and `pu` in stream`<symbol>@depth1000` to get diff orderbook update.



* * *

## 2022-12-09

European Options

REST

  * Add updateId field `u` in `GET /eapi/v1/depth`
  * Add parameter `underlying` in `GET /eapi/v1/exerciseHistory` to query exercise histroy by underlying



* * *

## 2022-11-29

COIN-M Futures

WEB SOCKET USER DATA STREAM

  * New WebSocket stream `STRATEGY_UPDATE` in USER-DATA-STREAM: update when a strategy is created/cancelled/expired, ...etc.
  * New WebSocket stream `GRID_UPDATE` in USER-DATA-STREAM: update when a sub order of a grid is filled or partially filled.



* * *

## 2022-11-29

USDⓈ-M Futures

WEB SOCKET USER DATA STREAM

  * New WebSocket stream `STRATEGY_UPDATE` in USER-DATA-STREAM: update when a strategy is created/cancelled/expired, ...etc.
  * New WebSocket stream `GRID_UPDATE` in USER-DATA-STREAM: update when a sub order of a grid is filled or partially filled.



* * *

## 2022-11-18

European Options

REST

  * New endpoint `GET /eapi/v1/openInterest` is added to get options open interest for specific underlying on certain expiration date.



WEBSOCKET

  * New stream `<underlyingAsset>@openInterest@<expirationDate>` is added for real-time option open interest feed.



* * *

## 2022-11-16

European Options

WEBSOCKET

  * New trade stream `<underlyingAsset>@trade` is added for all option trades on specific underlying asset.
  * Adjust format in stream `option_pair`.



* * *

## 2022-11-03

European Options

REST

  * New endpoint for Auto-Cancel All Open Orders will be added on 2022-11-07:
    * `POST /eapi/v1/countdownCancelAll`：Set Auto-Cancel All Open Orders (Kill-Switch) Config
    * `GET /eapi/v1/countdownCancelAll`：Get Auto-Cancel All Open Orders (Kill-Switch) Config
    * `POST /eapi/v1/countdownCancelAllHeartBeat`：Auto-Cancel All Open Orders (Kill-Switch) Heartbeat



* * *

## 2022-10-13

COIN-M Futures

**Note:** This change will be effictive on 2022-10-17

REST RATE LIMIT WEIGHT

Endpoint `GET /dapi/v1/ticker/bookTicker`

**Weight Update:**

**2** for a single symbol;  
**5** when the symbol parameter is omitted

* * *

## 2022-10-13

USDⓈ-M Futures

**Note:** This change will be effictive on 2022-10-17

REST RATE LIMIT WEIGHT

Endpoint `GET /fapi/v1/ticker/bookTicker`

**Weight Update:**

**2** for a single symbol;  
**5** when the symbol parameter is omitted

* * *

## 2022-09-22

COIN-M Futures

  * Add new endpoint for Portfolio Margin:
    * `GET /dapi/v1/pmAccountInfo`: Get Portfolio Margin current account information.



* * *

## 2022-09-22

USDⓈ-M Futures

  * Update endpoint for Account/Trade:
    * `GET /fapi/v1/income`: Support more incomeType
  * Add new endpoint for Portfolio Margin:
    * `GET /fapi/v1/pmAccountInfo`: Get Portfolio Margin current account information.



* * *

## 2022-09-20

European Options

WEBSOCKET

  * New streams `<underlyingAsset>@markPrice` and `<underlyingAsset>@ticker@<expirationDate>` are added.
  * Streams `<!miniTicker@arr>` will be deprecated on 2022/10/30.



* * *

## 2022-09-14

European Options

REST

  * Adjust endpoint field `strikePrice`,`makerFeeRate`,`takerFeeRate`,`minQty`,`maxQty`,`initialMargin`,`maintenanceMargin`,`minInitialMargin`,`minMaintenanceMargin` to string in endpoint `GET /eapi/v1/exchangeInfo`
  * Only finished orders within 5 days can be queried in `GET /eapi/v1/historyOrders`



* * *

## 2022-09-05

European Options

REST

  * Adjust response result in endpoint `DELETE /eapi/v1/allOpenOrdersByUnderlying`



* * *

## 2022-08-22

European Options

REST

  * Add `rateLimits` information in endpoint `GET /eapi/v1/exchangeInfo`
  * Parameters `symbol` set to not mandatory in `GET /eapi/v1/userTrades`



* * *

## 2022-07-27

COIN-M Futures

REST RATE LIMIT WEIGHT

  * The weight of endpoint `GET /dapi/v1/trades` is updated to 5



* * *

## 2022-07-27

USDⓈ-M Futures

REST RATE LIMIT WEIGHT

  * The weight of endpoint `GET /fapi/v1/trades` is updated to 5



* * *

## 2022-06-28

COIN-M Futures

REST

  * New endpoint `GET /dapi/v1/pmExchangeInfo` to get current Portfolio Margin exchange trading rules.



* * *

## 2022-06-28

USDⓈ-M Futures

REST

  * New endpoint `GET /fapi/v1/pmExchangeInfo` to get current Portfolio Margin exchange trading rules.



* * *

## 2022-04-28

COIN-M Futures

REST

  * New endpoints `PUT /dapi/v1/order` and `PUT /dapi/v1/batchOrders` to support limit order modify
  * New endpoint `GET /dapi/v1/orderAmendment` to get order modify history



WEBSOCKET

  * New type "AMENDMENT" as order modify in Execution Type `x` of Order Update event `ORDER_TRADE_UPDATE`



* * *

## 2022-04-14

COIN-M Futures

WEB SOCKET USER DATA STREAM

  * New WebSocket stream `ACCOUNT_CONFIG_UPDATE` in USER-DATA-STREAM for leverage changed update



* * *

## 2022-03-01

USDⓈ-M Futures

REST

  * New endpoint`GET /fapi/v1/income/asyn`to get Download Id For Futures Transaction History
  * New endpoint`GET /fapi/v1/income/asyn/id`to get Futures Transaction History Download Link by Id



* * *

## 2022-02-18

COIN-M Futures

REST

  * The maximum value of `limit` in `GET /dapi/v1/userTrades` is adjusted to 1000



* * *

## 2022-02-10

USDⓈ-M Futures

REST

  * Update `GET /fapi/v2/account` endpoints:
    * If user is in multiAssetsMargin mode, all assets will be included in calculation for fields `totalInitialMargin``totalMaintMargin``totalWalletBalance``totalUnrealizedProfit``totalMarginBalance``totalPositionInitialMargin``totalOpenOrderInitialMargin``totalCrossWalletBalance``totalCrossUnPnl``availableBalance``maxWithdrawAmount` and the results will be show as value in USD
    * If user is in singleAssetsMargin mode, only USDT assets are included in the calculation(same as before)



* * *

## 2021-12-30

USDⓈ-M Futures

WEBSOCKET

  * New connection method for WEBSOCKET.
    * Base Url is `wss://fstream-auth.binance.com`
    * Streams can be access either in a single raw stream or a combined stream
    * Raw streams are accessed at `/ws/<streamName>?listenKey=<validateListenKey>`
    * Combined streams are accessed at `/stream?streams=<streamName1>/<streamName2>/<streamName3>&listenKey=<validateListenKey>`
    * `<validateListenKey>` must be a valid listenKey when you establish a connection.
  * More details: [Websocket Market Streams](/en/docs/products/derivatives-trading-usds-futures/websocket-market-streams/Connect) and [User Data Streams](/en/docs/products/derivatives-trading-usds-futures/user-data-streams)



* * *

## 2021-11-02

USDⓈ-M Futures

REST

  * New endpoint`GET /fapi/v1/assetIndex`to get asset index for Multi-Assets mode margin asset



* * *

## 2021-08-18

COIN-M Futures

REST

  * New field `positionAmt` as position amount in response of `GET /dapi/v1/account`



* * *

## 2021-08-17

COIN-M Futures

REST

  * New endpoints `PUT /dapi/v1/order` and `PUT /dapi/v1/batchOrders` to support limit order modify
  * New endpoint `GET /dapi/v1/orderAmendment` to get order modify history



WEBSOCKET

  * New type "AMENDMENT" as order modify in Execution Type `x` of Order Update event `ORDER_TRADE_UPDATE`



* * *

## 2021-07-23

COIN-M Futures

REST

  * New field `updateTime` as last update time of asset and position in response of `GET /dapi/v1/account` and `GET /dapi/v1/positionRisk`



* * *

## 2021-07-06

COIN-M Futures

REST

  * New fields in the response of `GET /dapi/v1/exchangeInfo`:
    * "liquidationFee" for liquidation fee rate
    * "marketTakeBound" for he max price difference rate( from mark price) a market order can make



* * *

## 2021-07-06

USDⓈ-M Futures

REST

  * New field `updateTime` as last update time of asset and position in response of `GET /fapi/v2/account` and `GET /fapi/v2/positionRisk`
  * New fields in the response of `GET /fapi/v1/exchangeInfo`:
    * "liquidationFee" for liquidation fee rate
    * "marketTakeBound" for he max price difference rate( from mark price) a market order can make



* * *

## 2021-06-15

USDⓈ-M Futures

WEBSOCKET

  * New fields "q" and "i" for quote asset and index price added in stream `<symbol>@compositeIndex`



REST

  * Update endpoints:
    * New fields `component` and `quoteAsset` as component asset and quote asset added in response of `GET /fapi/v1/indexInfo`



* * *

## 2021-05-06

COIN-M Futures

WEBSOCKET

  * New field "bc" for balance change in event "ACCOUNT_UPDATE"



* * *

## 2021-05-06

USDⓈ-M Futures

WEBSOCKET

  * Update streams:
    * Previous Leverage Update event `ACCOUNT_CONFIG_UPDATE` expanded as account configuration update event, including leverage update and Multi-Assets margin status update.
    * Balance and Position Update event `ACCOUNT_UPDATE` add new event reason type `m` as `AUTO_EXCHANGE`to represent Multi-Assets margin auto-exchange event



REST

  * New endpoints:

    * `POST /fapi/v1/multiAssetsMargin` to change Multi-Assets margin mode
    * `GET /fapi/v1/multiAssetsMargin` to check Multi-Assets margin mode
  * Update endpoints:

    * New object `assets` as asset information in response of `GET /fapi/v1/exchangeInfo`.
    * New field `marginAvailable` in response of `GET /fapi/v2/balance` and `GET /fapi/v2/account` to indicate whether the asset can be used as margin in Multi-Assets mode.



* * *

## 2021-04-27

COIN-M Futures

WEBSOCKET

  * The following liquidation orders streams do not push realtime order data anymore. Instead, they push snapshot order data at a maximum frequency of 1 order push per second.:
    * `<symbol>@forceOrder`
    * `!forceOrder@arr`



REST

  * The endpoint `GET /dapi/v1/allForceOrders` stop being maintained and no longer accepts request.



* * *

## 2021-04-27

USDⓈ-M Futures

WEBSOCKET

  * The following liquidation orders streams do not push realtime order data anymore. Instead, they push snapshot order data at a maximum frequency of 1 order push per second.:
    * `<symbol>@forceOrder`
    * `!forceOrder@arr`



REST

  * The endpoint `GET /fapi/v1/allForceOrders` stop being maintained and no longer accepts request.



* * *

## 2021-04-22

USDⓈ-M Futures

WEBSOCKET

  * New field "bc" for balance change in event "ACCOUNT_UPDATE"



* * *

## 2021-03-10

COIN-M Futures

REST

  * The query time period for endpoint `GET /dapi/v1/allForceOrders` must be less than 7 days (default as the recent 7 days).



* * *

## 2021-03-02

USDⓈ-M Futures

  * New endpoint `GET /fapi/v1/indexPriceKlines` to get index price kline/candlestick data.

  * New endpoint `GET /fapi/v1/markPriceKlines` to get mark price kline/candlestick data.




* * *

## 2021-02-24

USDⓈ-M Futures

REST RATE LIMIT WEIGHT

  * The weight of endpoint `GET /fapi/v2/balance` is updated to 5
  * The weight of endpoint `GET /fapi/v2/positionRisk` is updated to 5



* * *

## 2021-02-22

USDⓈ-M Futures

REST RATE LIMIT WEIGHT

  * The weight of endpoint `GET /fapi/v1/income` is updated to 30



REST

  * The query time period for endpoint `GET /fapi/v1/allOrders` must be less than 7 days.
  * The query time period for endpoint `GET /fapi/v1/allForceOrders` must be within the recent 7 days.



* * *

## 2021-01-26

COIN-M Futures

REST RATE LIMIT WEIGHT

  * Following endpoints' weights will be updated to 20 with symbol and 50 without symbol:
    * `GET /dapi/v1/allForceOrders`
    * `GET /dapi/v1/forceOrders`



* * *

## 2021-01-26

USDⓈ-M Futures

WEB SOCKET USER DATA STREAM

  * New WebSocket stream `ACCOUNT_CONFIG_UPDATE` in USER-DATA-STREAM for leverage changed update



REST RATE LIMIT WEIGHT

  * Following endpoints' weights will be updated to 20 with symbol and 50 without symbol:
    * `GET /fapi/v1/allForceOrders`
    * `GET /fapi/v1/forceOrders`



REST

  * New filter "MIN_NOTIONAL" whicht defines the minimum notional value allowed for an order on a symbol, and shown in the `/fapi/v1/exchangeInfo`



* * *

## 2021-01-21

COIN-M Futures

The regular expression rule for `newClientOrderId` updated as `^[\.A-Z\:/a-z0-9_-]{1,36}$`

* * *

## 2021-01-21

USDⓈ-M Futures

The regular expression rule for `newClientOrderId` updated as `^[\.A-Z\:/a-z0-9_-]{1,36}$`

* * *

## 2021-01-04

USDⓈ-M Futures

REST RATE LIMIT WEIGHT

  * Following endpoints will use new weight rule based on the paremeter "LIMIT" in the request:

    * `GET /fapi/v1/klines`
    * `GET /fapi/v1/continuousKlines`
  * Following endpoints' weights will be updated to 20:

    * `GET /fapi/v1/historicalTrades`
    * `GET /fapi/v1/allForceOrders`
    * `GET /fapi/v1/forceOrders`
    * `GET /fapi/v1/aggTrades`



* * *

## 2020-12-30

COIN-M Futures

REST

  * Following DAPI endpoints will use new weight rule based on the parameter "LIMIT" in the request:

    * `GET /dapi/v1/klines`
    * `GET /dapi/v1/continuousKlines`
    * `GET /dapi/v1/indexPriceKlines`
    * `GET /dapi/v1/markPriceKlines`
  * Following DAPI endpoints' weights will be updated to 20:

    * `GET /dapi/v1/historicalTrades`
    * `GET /dapi/v1/allForceOrders`
    * `GET /dapi/v1/forceOrders`
    * `GET /dapi/v1/aggTrades`



* * *

## 2020-12-08

USDⓈ-M Futures

WEBSOCKET

  * New field `e` for event type in payload of streams `<symbol>@bookTicker` and `!bookTicker`
  * New field `P` for estimated settle price in payload of streams `<symbol>@markPrice`, `<symbol>@markPrice@1s`, `!markPrice@arr`, and `!markPrice@arr@1s`.
  * New stream `<pair>_<contractType>@continuousKline_<interval>` for continuous contract kline



REST API

  * New field "estimatedSettlePrice" in response to `GET /fapi/v1/premiumIndex`

  * New fields in response to `GET /fapi/v1/exchangeInfo`:

    * "pair"
    * "contractType"
    * "deliveryDate"
    * "onboardDate"
  * New endpoint `GET /fapi/v1/continuousKlines` to get continuous contract kline data




ENUM

  * Contract types:
    * PERPETUAL
    * CURRENT_MONTH
    * NEXT_MONTH
    * CURRENT_QUARTER
    * NEXT_QUARTER



* * *

## 2020-11-27

COIN-M Futures

  * New endpoint `GET /dapi/v1/commissionRate` to get user commission rate.



* * *

## 2020-11-27

USDⓈ-M Futures

  * New endpoint `GET /fapi/v1/commissionRate` to get user commission rate.



* * *

## 2020-11-13

USDⓈ-M Futures

WEB SOCKET STREAM

  * In order to provide users with more secure and stable services, the update time of `<symbol>depth@0ms` and `<symbol>@depth<level>@0ms` is dynamically adjusted according to the total amount of data traffic and other objective conditions.



* * *

## 2020-11-10

USDⓈ-M Futures

  * New field "marginAsset" for margin asset in the response to `GET /fapi/v1/exchangeInfo`.
  * New field "positionAmt" for position amount in the response to `GET /fapi/v2/account`.



* * *

## 2020-11-09

USDⓈ-M Futures

WEB SOCKET USER DATA STREAM

Please notice: new streamlined and optimized push rules on event `ACCOUNT_UPDATE` in USER-DATA-STREAM

  * When an asset of a user is changed:

    * Only this asset and its balance information will be pushed
    * Other assets and information will no longer be pushed even the balances may not be 0
    * If none of the open positions change, the position "P" will only return an empty `[]`
  * When a position or the margin type of a symbol is changed:

    * "P" will push the details in the "BOTH" position of this symbol
    * If the change happens in "LONG" or "SHORT" position, the changed "LONG" or "SHORT" position of this symbol will be pushed
    * Initialized "LONG" or "SHORT" isolated position of this symbol will also be pushed
    * Position information of other symbols will no longer be pushed, even their positions may not be 0
  * In short, the **full** information of assets and positions should be obtained via the related RESTful endpoints(`GET /fapi/v2/account` and `GET /fapi/v2/positionRisk`), and the locally cached asset or position data can be updated via the event `ACCOUNT_UPDATE` in Websocket USER-DATA-STREAM with the information of **changed** asset or position.

  * Please visit [here](https://dev.binance.vision/t/838) to get examples for helping to understand the upgrade.




* * *

## 2020-10-27

USDⓈ-M Futures

WEB SOCKET STREAM

  * The maximum stream number that a single connection can listen to changes as 200.



* * *

## 2020-10-10

USDⓈ-M Futures

WEBSOCKET

  * New WebSocket streams `<symbol>@compositeIndex` for composite index symbol information.



* * *

## 2020-10-09

USDⓈ-M Futures

  * New endpoint `GET /fapi/v1/indexInfo` to get information of composite index.



* * *

## 2020-09-18

USDⓈ-M Futures

  * New endpoint `GET /fapi/v1/apiTradingStatus` to get futures API trading quantitative rules indicators



* * *

## 2020-09-16

USDⓈ-M Futures

  * New endpoint `GET /fapi/v1/lvtKlines` to get gistorical BLVT Kline.  
The BLVT NAV system is working relatively with Binance Futures, so the endpoint is based on fapi.



WEBSOCKET

  * New WebSocket streams for BLVT  
The BLVT NAV system is working relatively with Binance Futures, so the endpoint is based on futures websocket service.  
_`<tokenName>@tokenNav` for BLVT Info streams_ `<tokenName>@nav_kline_<interval>` for BLVT NAV Kline streams



* * *

## 2020-09-09

USDⓈ-M Futures

  * Some orders that were cancelled/expired will be removed gradually from API endpoints.
    * Orders that meet criteria
      * order status is `CANCELED` or `EXPIRED`, **AND**
      * order has NO filled trade, **AND**
      * created time + 7 days < current time
    * These endpoints are affected:
      * `GET /fapi/v1/order`
      * `GET /fapi/v1/allOrders`



* * *

## 2020-08-16

COIN-M Futures

WEBSOCKET

  * Websocket Request for user data:
    * `<listenKey>@account` request for user's account information
    * `<listenKey>@balance` request for user's account balance
    * `<listenKey>@balance` request for user's position information



REST

  * New endpoint `GET /dapi/v1/adlQuantile` to get the positions' ADL quantile estimation values



* * *

## 2020-08-14

USDⓈ-M Futures

  * New field "indexPrice" in response to endpoint `GET /fapi/v1/premiumIndex`.
  * New field "i" for indexPrice in payload of ws streams:
    * `<symbol>@markPrice`,
    * `<symbol>@markPrice@1s`,
    * `!markPrice@arr`,
    * `!markPrice@arr@1s`



* * *

## 2020-08-12

COIN-M Futures

  * New endpoint `GET /dapi/v1/forceOrders` to get the user's force orderes.



* * *

## 2020-08-12

USDⓈ-M Futures

  * New endpoint `GET /fapi/v1/forceOrders` to get the user's force orderes.



* * *

## 2020-08-11

COIN-M Futures

COIN MARGINED PERPETUAL FUTURES

  * New contract type ("contractType") `PERPETUAL` for coin margined perpetual futures countract.

  * New fields in the reponse to endpoint `GET /dapi/v1/premiumIndex`:

    * `lastFundingRate` for the lasted funding rate of the perpetual futures contract
    * `nextFundingTime` for the next funding time of the perpetual futures contract
  * New endpoint `GET /dapi/v1/fundingRate` to get funding rate history of perpetual futures

  * New fields in the payload of WSS `<symbol>@markPrice`, `<symbol>@markPrice@1s`, `<pair>@markPrice`, and `<pair>@markPrice@1s`:

    * `r` for the lasted funding rate of the perpetual futures contract
    * `T` for the next funding time of the perpetual futures contract



* * *

## 2020-07-30

USDⓈ-M Futures

  * New endpoint `GET /fapi/v1/adlQuantile` to get the positions' ADL quantile estimation values



* * *

## 2020-07-22

COIN-M Futures

  * New endpoints of coin margined futures trading data:
    * `GET /futures/data/openInterestHist`
    * `GET /futures/data/topLongShortAccountRatio`
    * `GET /futures/data/topLongShortPositionRatio`
    * `GET /futures/data/globalLongShortAccountRatio`
    * `GET /futures/data/takerBuySellVol`
    * `GET /futures/data/basis`



* * *

## 2020-07-17

USDⓈ-M Futures

  * Weights of endpoint `GET /fapi/v1/income` has been changed as 20



* * *

## 2020-07-02

USDⓈ-M Futures

WEBSOCKET

  * New field "m" for event reason type in event "ACCOUNT_UPDATE"
  * New field "rp" for the realized profit of the trade in event "ORDER_TRADE_UPDATE"



* * *

## 2020-06-15

USDⓈ-M Futures

  * New fields in responses to `GET /fapi/v2/account` and `GET /fapi/v2/balance`:
    * `availableBalance`
    * `maxWithdrawAmount`



* * *

## 2020-06-04

USDⓈ-M Futures

  * New endpoints of version 2 of fapi, having better performance than the v1 endpoints:
    * `GET /fapi/v2/account`
    * `GET /fapi/v2/balance`



* * *

## 2020-06-02

USDⓈ-M Futures

  * New endpoint `GET /fapi/v2/positionRisk` in version 2 of fapi:
    * User can choose to send specific "symbol".
    * All symbols in the market can be returned.
    * Different responses for "One-way" or "Hedge" position mode.
    * Better performance than the v1 endpoint.



* * *

## 2020-05-18

USDⓈ-M Futures

  * New parameter `closePosition` for endpoint `POST /fapi/v1/order`:  
If a `STOP_MARKET` or `TAKE_PROFIT_MARKET` order with `closePosition=true` is triggered，all of the current long position( if `SELL` order) or current short position( if `BUY` order) will be closed.
  * New field `closePosition` in response to endpoints:
    * `POST /fapi/v1/order`
    * `POST /fapi/v1/batchOrders`
    * `GET /fapi/v1/order`
    * `DELETE /fapi/v1/order`
    * `DELETE /fapi/v1/batchOrders`
    * `GET /fapi/v1/openOrder`
    * `GET /fapi/v1/openOrders`
    * `GET /fapi/v1/allOrders`



* * *

## 2020-05-18

USDⓈ-M Futures

  * Some orders that were cancelled/expired will be removed gradually from API endpoints, but they are still available from Web UI.
    * Orders that meet criteria
      * order status is `CANCELED` or `EXPIRED`, **AND**
      * order has NO filled trade, **AND**
      * created time + 30 days < current time
    * These endpoints are affected:
      * `GET /fapi/v1/order`
      * `GET /fapi/v1/allOrders`



* * *

## 2020-05-15

USDⓈ-M Futures

  * New fields in payloads of `<symbol>@bookTicker` and `!bookTicker`:
    * `E` for event time
    * `T` for transaction time



* * *

## 2020-05-14

USDⓈ-M Futures

  * New field `time` for transaction time in response to endpoints：
    * `GET /fapi/v1/ticker/price`
    * `GET /fapi/v1/ticker/bookTicker`
    * `GET /fapi/v1/openInterest`



* * *

## 2020-05-11

USDⓈ-M Futures

  * New endpoint `POST /fapi/v1/countdownCancelAll` to cancel all open orders of the specified symbol at the end of the specified countdown.  
This rest endpoint means to ensure your open orders are canceled in case of an outage. The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled and repalced by a new one.



* * *

## 2020-05-06

USDⓈ-M Futures

REST

  * Endpoint `GET /fapi/v1/leverageBracket` is changed as "USER-DATA". It need to be signed, and timestamp is needed.



WEB SOCKET USER DATA STREAM

  * Please notice: event `ACCOUNT_UPDATE` in USER-DATA-STREAM will be pushed with only account balance or relative position when "FUNDING FEE" occurs.
    * When "FUNDING FEE" occurs in a **crossed position** , `ACCOUNT_UPDATE` will be pushed with only the balance `B`(including the "FUNDING FEE" asset only), without any position `P` message.
    * When "FUNDING FEE" occurs in an **isolated position** , `ACCOUNT_UPDATE` will be pushed with only the balance `B`(including the "FUNDING FEE" asset only) and the relative position message `P`( including the isolated position on which the "FUNDING FEE" occurs only, without any other position message).



* * *

## 2020-04-25

USDⓈ-M Futures

  * New fields in USER DATA STREAM event `ORDER_TRADE_UPDATE`:

    * `cp` stands for Close-All conditional order
    * `AP` for Activation Price with `TRAILING_STOP_MARKET` order
    * `cr` for Callback Rate with `TRAILING_STOP_MARKET` order
  * New USER DATA STREAM event `MARGIN_CALL`.




* * *

## 2020-04-17

USDⓈ-M Futures

  * New parameter `newOrderRespType` for response type in endpoint `POST /fapi/v1/order`.  
`ACK` and `RESULT` are supported. And for `newOrderRespType= RESULT`: _`MARKET` order: the final FILLED result of the order will be return directly._ `LIMIT` order with special `timeInForce`: the final status result of the order(FILLED or EXPIRED) will be returned directly.



* * *

## 2020-04-14

USDⓈ-M Futures

WEB SOCKET STREAM

  * WebSocket connections have a limit of 10 incoming messages per second. A message is considered:
    * A PING frame
    * A PONG frame
    * A JSON control message (e.g. subscribe, unsubscribe)
  * A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.
  * A single connection can listen to a maximum of 200 streams.



* * *

## 2020-04-09

USDⓈ-M Futures

  * New endpoint of futures trading data: `GET /futures/data/takerlongshortRatio`



* * *

## 2020-04-08

USDⓈ-M Futures

  * New endpoint `GET /fapi/v1/positionSide/dual` to get current position mode.
  * New endpoint `POST /fapi/v1/batchOrders` to place multiple orders.



* * *

## 2020-04-06

USDⓈ-M Futures

  * Please notice: event `ACCOUNT_UPDATE` in USER-DATA-STREAM will not be pushed without update of account balances or positions.

    * `ACCOUNT_UPDATE` will be pushed only when update happens on user's account, including changes on balances, positions, or margin type.
    * Unfilled orders or cancelled orders will not make the event `ACCOUNT_UPDATE` pushed, since there's no change on positions.
    * Only positions of symbols with non-zero isolatd wallet or non-zero position amount will be pushed in the "position" part of the event `ACCOUNT_UPDATE`.
  * New endpoint `POST /fapi/v1/positionSide/dual` to change position mode: Hedge Mode or One-way Mode.

  * New parameter `positionSide` in the following endpoints：

    * `POST /fapi/v1/order`
    * `POST /fapi/v1/positionMargin`
  * New field `positionSide` in the responses to the following endpoints：

    * `POST /fapi/v1/order`
    * `GET /fapi/v1/order`
    * `DELETE /fapi/v1/order`
    * `DELETE /fapi/v1/batchOrders`
    * `GET /fapi/v1/openOrder`
    * `GET /fapi/v1/openOrders`
    * `GET /fapi/v1/allOrders`
    * `GET /fapi/v1/account`
    * `GET /fapi/v1/positionMargin/history`
    * `GET /fapi/v1/positionRisk`
    * `GET /fapi/v1/userTrades`
  * New field `ps` for "position side"in USER_DATA_STREAM events `ACCOUNT_UPDATE` and `ORDER_TRADE_UPDATE`.




* * *

## 2020-03-30

USDⓈ-M Futures

  * New endpoints of futures trading data:
    * `GET /futures/data/openInterestHist`
    * `GET /futures/data/topLongShortAccountRatio`
    * `GET /futures/data/topLongShortPositionRatio`
    * `GET /futures/data/globalLongShortAccountRatio`



## 2020-02-26

  * New order type: `TRAILING_STOP_MARKET`



* * *

## 2020-02-20

USDⓈ-M Futures

  * New endpoint to query specific current open order: `GET /fapi/v1/openOrder`



* * *

## 2020-02-17

USDⓈ-M Futures

  * Update time changed as 1000ms for streams `<symbol>@ticker` and `!ticker@arr`
  * New diff depth data with 500ms updates: `<symbol>@depth@500ms`
  * New partial depth data with 500ms updates: `<symbol>@depth<level>@500ms`



* * *

## 2020-02-12

USDⓈ-M Futures

  * New [SDK and Code Demonstration](/en/docs/sdks-tools/overview) on Java

  * Faster mark price websocket data with 1s updates: `<symbol>@markPrice@1s` and `!markPrice@arr@1s`




* * *

## 2020-02-05

USDⓈ-M Futures

  * New market data endpoint`GET /fapi/v1/leverageBracket` to check notional and leverage brackets.



* * *

## 2020-01-19

USDⓈ-M Futures

  * "cumQty" is going to be removed from the responses to `DELETE /fapi/v1/order`, `DELETE /fapi/v1/batchOrders` and other `order` relatived endpoints in the coming weeks.  
Please use "executedQty" instead.



* * *

## 2020-01-17

USDⓈ-M Futures

  * New [SDK and Code Demonstration](/en/docs/sdks-tools/overview) on Python



* * *

## 2020-01-06

USDⓈ-M Futures

  * Faster diff data with real time updates: `<symbol>@depth@0ms`



* * *

## 2020-01-03

USDⓈ-M Futures

  * New endpoints related to isolated position：

    * `POST /fapi/v1/marginType`
    * `POST /fapi/v1/positionMargin`
    * `GET /fapi/v1/positionMargin/history`
  * New field in response to `GET /fapi/v1/positionRisk` related to isolated position:

    * `marginType`
    * `isolatedMargin`
  * New field in response to `GET /fapi/v1/account`related to isolated position: `isolated`

  * New field in event `ACCOUNT_UPDATE`:

    * "cw" for cross wallet
    * "mt" for margin type
    * "iw" for isolated wallet (if isolated)



* * *

## 2019-12-19

USDⓈ-M Futures

  * New endpoint `GET /fapi/v1/openInterest` to get present open interest of a specific symbol.



* * *

## 2019-12-18

USDⓈ-M Futures

  * New event type in user data stream：`listenKeyExpired`.



* * *

## 2019-12-12

USDⓈ-M Futures

  * New endpoint `DELETE /fapi/v1/allOpenOrders` to cancel all open orders of a specific symbol.
  * New endpoint`DELETE /fapi/v1/batchOrders` to cancel a list of open orders.
  * `reduceOnly` has been supported in orders with type:
    * `TAKE_PROFIT`
    * `TAKE_PROFIT_MARKET`
    * `STOP`
    * `STOP_MARKET`



* * *

## 2019-11-29

USDⓈ-M Futures

  * New endpoint `GET /fapi/v1/allForceOrders` to get all liquidation orders.
  * New websocket streams:
    * `<symbol>@forceOrder`for liquidation order streams
    * `!forceOrder@arr` for all market liquidation order streams



* * *

## 2019-11-25

USDⓈ-M Futures

  * `GET /fapi/v1/account` has new field: `positions`
  * Added new field `time` for order creation time in:
    * `GET /fapi/v1/openOrders`
    * `GET /fapi/v1/order`
    * `GET /fapi/v1/allOrders`



* * *

## 2019-11-15

USDⓈ-M Futures

  * New websocket streams：
    * `!miniTicker@arr`: All market 24hr mini-tickers stream.
    * `!ticker@arr`: : All market 24hr tickers stream.



* * *

## 2019-11-12

USDⓈ-M Futures

  * WSS now supports live subscribing/unsubscribing to streams.



* * *

## 2019-11-05

USDⓈ-M Futures

  * New order type:
    * `STOP_MARKET`，
    * `TAKE_PROFIT_MARKET`.
  * New parameter `workingType` in `POST /fapi/v1/order`:  
order with stop price can be triggered by "CONTRACT_PRICE" or "MARK_PRICE"
  * New keys in USER-DATA-STREAMS：
    * in `ORDER_TRADE_UPDATE`:
      * "T" as transaction time
      * "wt" as workingType
    * in `ACCOUNT_UPDATE`:
      * "T" as transaction time



* * *

## 2019-10-28

USDⓈ-M Futures

  * New rest endpoint for income flow history `GET /fapi/v1/income`



* * *

## 2019-10-25

USDⓈ-M Futures

  * Added "up" in event `ACCOUNT_UPDATE` in user data stream: the unrealized PnL of the position.
  * Added "R" in event `ORDER_TRADE_UPDATE` in user data stream, showing if the trade is reduce only.



* * *

## 2019-10-24

USDⓈ-M Futures

  * New WebSocket streams for booktickers added: `<symbol>@bookTicker` and `!bookTicker`.
  * New WebSocket streams for partial orderbook added: `<symbol>@depth<levels>` and `<symbol>@depth<levels>@100ms`
  * Faster diff data with 100ms updates: `<symbol>@depth@100ms`
  * Added `Update Speed`: to `Websocket Market Streams`



* * *

## 2019-10-18

USDⓈ-M Futures

  * New endpoint `POST /fapi/v1/leverage` for changing user's initial leverage in specific symbol market.
  * Added "leverage" for current initial leverage and "maxNotionalValue" for notional value limit of current initial leverage in response to `GET /fapi/v1/positionRisk`.
  * `reduceOnly` now is supported in the `MARKET` orders.



* * *

## 2019-10-14

USDⓈ-M Futures

  * Added `GET /fapi/v1/fundingRate` for getting funding fee rate history.



* * *

## 2019-10-11

USDⓈ-M Futures

  * Added "m" in event `ORDER_TRADE_UPDATE` in user data stream, showing if the trade is the maker side.



* * *

## 2019-10-08

USDⓈ-M Futures

  * New order parameter `reduceOnly` for `LIMIT` orders.
  * New order type `TAKE_PROFIT`.



* * *

Was this page helpful?

Last modified on November 12, 2026

[Quick Start](/en/docs/products/derivatives-trading-portfolio-margin-pro/quick-start)[General Info](/en/docs/products/derivatives-trading-portfolio-margin-pro/general-info)

---

# 更新日志

## 2026-10-23

**生效时间: 2026-10-23**

U 本位合约

  * `POST /fapi/v1/algoOrder`（下条件单）：`TRAILING_STOP_MARKET` 订单的 `callbackRate` 最大值由 10 调整为 20。
  * WebSocket API `algoOrder.place`（条件单下单）：`TRAILING_STOP_MARKET` 订单的 `callbackRate` 最大值由 10 调整为 20。



统一账户

  * `POST /papi/v1/um/algo/order`（UM条件单下单）：`TRAILING_STOP_MARKET` 订单的 `callbackRate` 最大值由 10 调整为 20。



* * *

## 2026-10-21

**生效时间: 2026-10-28**

统一账户

  * `GET /papi/v1/um/income`（获取UM损益资金流水）：不再支持 `page` 参数。请使用 `startTime` 和 `endTime` 定位记录。
  * `GET /papi/v1/cm/income`（获取CM损益资金流水）：不再支持 `page` 参数。请使用 `startTime` 和 `endTime` 定位记录。



* * *

## 2026-10-20

**生效时间: 2026-10-20**

U 本位合约

  * `GET /fapi/v1/income/asyn`（获取合约资金流水下载Id）：请求限制现调整为每月100次，该限制在网页端下载页面与Rest接口之间共用，并且在U本位合约与币本位合约之间共用。



币本位合约

  * `GET /dapi/v1/income/asyn`（获取合约资金流水下载Id）：请求限制现调整为每月100次，该限制在网页端下载页面与Rest接口之间共用，并且在U本位合约与币本位合约之间共用。



* * *

## 2026-10-15

**生效时间: 2026-10-15**

统一账户和统一账户Pro

  * `POST /sapi/v1/portfolio/asset-collection`（特定资产资金归集）和 `POST /papi/v1/asset-collection`（特定资产资金归集）：新增两个可选请求参数 `amount`（DECIMAL）和 `futureType`（STRING，枚举 `UM` / `CM` / `OPTION`，`OPTION` 仅支持 SPAN）。两者同时传入时，资金归集将被路由到指定钱包。`amount` 和 `futureType` 必须同时传入。均不传入时行为不变。



**生效时间: 2026-10-16**

U 本位合约

  * `GET /fapi/v1/income`（获取账户损益资金流水）：不再支持 `page` 参数。请使用 `startTime` 和 `endTime` 定位记录。



币本位合约

  * `GET /dapi/v1/income`（获取账户损益资金流水）：不再支持 `page` 参数。请使用 `startTime` 和 `endTime` 定位记录。



* * *

## 2026-10-09

**生效时间: 2026-10-09**

U 本位合约

  * `POST /fapi/v1/leverage`（调整开仓杠杆）：移除 `leverage` 参数文档中固定的最大值 125。最大值因交易对而异，以 `GET /fapi/v1/leverageBracket` 返回的第 1 档 `initialLeverage` 为准（如 BTCUSDT、ETHUSDT 为 150）。仅为文档更正，与当前后端实际行为保持一致。



统一账户

  * `POST /papi/v1/um/leverage`（调整UM开仓杠杆）：移除 `leverage` 参数文档中固定的最大值 125。最大值因交易对而异，以 `GET /papi/v1/um/leverageBracket` 返回的第 1 档 `initialLeverage` 为准。仅为文档更正，与当前后端实际行为保持一致。



* * *

## 2026-10-08

**生效时间: 2026-10-08**

欧式期权

  * `GET /eapi/v1/bill`（获取账户资金流水）
    * 响应新增 `symbol` 字段，标识合约相关记录（如 `CONTRACT`、`FEE`、`EXERCISE_PNL`、`EXERCISE_FEE`）对应的期权交易对。其他类型（如 `TRANSFER`）不返回该字段；较早的记录可能不包含该字段。



* * *

## 2026-09-28

**生效时间: 2026-09-28**

U 本位合约

  * 新增错误码 `-4425` `JOINT_MARGIN_REJECT_WITH_SIGNAL_LEAD`："因存在活跃的信号带单组合，无法切换至多资产模式。"



* * *

## 2026-09-21

**生效时间: 2026-09-14**

U 本位合约

  * `GET /fapi/v1/tradingSchedule`（交易时段）以及当前交易时段数据流新增外汇市场（`FX` / `FXUpdate`）支持，时段类型为 "REGULAR" 和 "NO_TRADING"。



* * *

## 2026-09-15

**生效时间: 2026-09-15**

U 本位合约

  * 修改 `order.modify`（WebSocket API — 修改订单）：新增可选参数 `reduceOnly`（STRING）。当传 `true` 时，仅当原订单亦为 reduce-only 时跳过修改后订单的 `min_notional` 校验；否则拒绝请求并返回 `-5047` "The original order is not a reduce-only order"。
  * 修改 `PUT /fapi/v1/order`（REST API — 修改订单）：新增相同的可选参数 `reduceOnly`（STRING），行为与上述 `order.modify` 的改动一致。
  * 备注：`reduceOnly` 参数仅用于订单校验（min_notional 跳过 + RO 属性一致性检查）。传 `reduceOnly=true` 并不会改变原订单的 reduce-only 属性——订单的 RO 标记仍维持下单时设定的值。



* * *

## 2026-09-10

**生效时间: 2026-09-10**

U 本位合约

  * `GET /fapi/v1/income`（获取账户损益资金流水）：新增 `incomeType` 枚举值 `SPECIAL_FUNDING_FEE`，用于传统金融(Tradfi)分红资金费用。



* * *

## 2026-08-26

**生效时间: 2026-08-26**

U 本位合约

  * `GET /fapi/v1/userTrades`（账户成交历史）：历史数据可查询范围说明由"仅支持最近6个月历史交易的查询"更新为 **"仅支持最近3个月历史交易的查询"** ，与当前后端实际行为保持一致。



币本位合约

  * `GET /dapi/v1/userTrades`（账户成交历史）：补充历史数据可查询范围说明 **"本接口仅支持最近3个月历史交易的查询"** ，与当前后端实际行为保持一致。



* * *

## 2026-08-25

**生效时间: 2026-08-25**

U 本位合约

  * `GET /fapi/v1/allOrders`（查询所有订单）：`symbol` 参数由必填变更为选填。其他行为不变，接口单次请求最多仍返回 1000 条记录。



**生效时间: 2026-08-26**

统一账户

  * `POST /papi/v1/um/algo/order`（UM条件单下单）：新增可选参数 `closePosition`（`true`/`false`；触发后全部平仓，仅支持 `STOP_MARKET` 和 `TAKE_PROFIT_MARKET`；不与 `quantity`/`reduceOnly` 合用；双开模式下 `LONG` 方向不支持 `BUY`，`SHORT` 方向不支持 `SELL`）；`quantity` 由必填变更为选填；响应新增 `closePosition` 字段。



* * *

## 2026-08-21

**生效时间: 2026-08-21**

U 本位合约

  * `ALGO_UPDATE`（条件订单交易更新推送）
    * [2026-08-07](/zh-CN/docs/products/derivatives-trading-portfolio-margin-pro/change-log#2026-08-07) 版本中新增的 `ia` 字段现已正式生效，不再是占位字段。对于追踪止损单（trailing stop order），在订单实际触发前（Algo Status `X` 仍为 `NEW`），可能会收到两次独立的 `ALGO_UPDATE` `NEW` 推送：一次 `ia:false`，激活后再收到一次 `ia:true`。



统一账户

  * `ALGO_UPDATE`（条件订单交易更新推送）
    * [2026-08-07](/zh-CN/docs/products/derivatives-trading-portfolio-margin-pro/change-log#2026-08-07) 版本中新增的 `ia` 字段现已正式生效，不再是占位字段。对于追踪止损单（trailing stop order），在订单实际触发前（Algo Status `X` 仍为 `NEW`），可能会收到两次独立的 `ALGO_UPDATE` `NEW` 推送：一次 `ia:false`，激活后再收到一次 `ia:true`。



* * *

## 2026-08-17

**生效时间: 2026-08-17**

U 本位合约

  * `GET /fapi/v1/tradingSchedule`（交易时段）以及当前交易时段数据流新增中国股票市场（`CN_EQUITY` / `CN_EquityUpdate`）支持，时段类型为 "REGULAR" 和 "NO_TRADING"。



* * *

## 2026-08-14

币本位合约

  * `GET /futures/data/topLongShortAccountRatio`（大户账户数多空比）：修正请求参数 `symbol` → `pair`；新增可选参数 `contractType`（`PERPETUAL` / `CURRENT_QUARTER` / `NEXT_QUARTER`，不填则返回所有合约类型的汇总数据）。
  * `GET /futures/data/globalLongShortAccountRatio`（多空持仓人数比）：新增可选参数 `contractType`（`PERPETUAL` / `CURRENT_QUARTER` / `NEXT_QUARTER`，不填则返回所有合约类型的汇总数据）。
  * `GET /futures/data/openInterestHist`（合约持仓量）：修正文档中 `contractType` 参数从"必填"到"可选"（`PERPETUAL` / `CURRENT_QUARTER` / `NEXT_QUARTER`，不填则返回所有合约类型的汇总数据；服务端行为不变）。
  * `GET /futures/data/topLongShortPositionRatio`（大户持仓量多空比）：新增可选参数 `contractType`（`PERPETUAL` / `CURRENT_QUARTER` / `NEXT_QUARTER`，不填则返回所有合约类型的汇总数据）。



* * *

## 2026-08-11

**生效时间: 2026-08-13**

U 本位合约

  * `GET /fapi/v1/aggTrades`（近期成交/归集交易）：可查询交易历史的最大回溯时长（以当前时间为准）从24小时延长至48小时。



* * *

## 2026-08-07

**生效时间: 2026-08-07**

U 本位合约

  * `ACCOUNT_UPDATE`（Balance 和 Position 更新推送）
    * `a` 对象中新增字段 `S`（STRING）：本次事件对应的交易对。仅当事件推出原因 `m` 为 `FUNDING_FEE` 时推送。
  * `ALGO_UPDATE`（条件订单交易更新推送）
    * `o` 对象中新增字段 `ia`（BOOLEAN）：条件单是否已激活，仅对追踪止损单有意义。
    * 注意：`ia` 当前为占位字段，始终返回 `false`，将在后续版本中正式启用。



币本位合约

  * `ACCOUNT_UPDATE`（Balance 和 Position 更新推送）
    * `a` 对象中新增字段 `S`（STRING）：本次事件对应的交易对。仅当事件推出原因 `m` 为 `FUNDING_FEE` 时推送。



统一账户

  * `ACCOUNT_UPDATE`（合约 Balance 和 Position 更新推送）
    * `a` 对象中新增字段 `S`（STRING）：本次事件对应的交易对。仅当事件推出原因 `m` 为 `FUNDING_FEE` 时推送。
  * `ALGO_UPDATE`（条件订单交易更新推送）
    * `ao` 对象中新增字段 `ia`（BOOLEAN）：条件单是否已激活，仅对追踪止损单有意义。
    * 注意：`ia` 当前为占位字段，始终返回 `false`，将在后续版本中正式启用。



* * *

## 2026-08-05

**生效时间: 2026-08-05**

订单/成交历史查询接口（`forceOrders` / `allOrders` / `userTrades`，同时包含 U 本位合约 `/fapi/v1/*` 和币本位合约 `/dapi/v1/*`）均支持返回 U 本位合约和币本位合约的数据。

U 本位合约

  * 以下接口的响应中新增了字段：
    * `GET /fapi/v1/forceOrders`（用户强平单历史）：新增 `cumBase` 和 `pair`。
    * `GET /fapi/v1/allOrders`（查询所有订单）：新增 `cumBase` 和 `pair`。
    * `GET /fapi/v1/userTrades`（账户成交历史）：新增 `pair`、`baseQty` 和 `marginAsset`。



币本位合约

  * 以下接口的响应中新增了字段：
    * `GET /dapi/v1/forceOrders`（用户强平单历史）：新增 `cumQuote` 和 `goodTillDate`。
    * `GET /dapi/v1/allOrders`（查询所有订单）：新增 `cumQuote` 和 `goodTillDate`。
    * `GET /dapi/v1/userTrades`（账户成交历史）：新增 `quoteQty`。



* * *

## 2026-08-03

**生效时间: 2026-08-03**

统一账户

  * 以下接口的响应中移除了 `avgPrice` 字段，以及 `cumQuote`（UM）/ `cumBase`（CM）字段：
    * PUT `/papi/v1/um/order`（修改 UM 订单）
    * PUT `/papi/v1/cm/order`（修改 CM 订单）



* * *

## 2026-07-29

**生效时间: 2026-07-29**

U 本位合约

  * `GET /fapi/v1/historicalTrades` (查询订单簿历史成交)
    * 请求权重由 `20` 调整为 `200`。



币本位合约

  * `GET /dapi/v1/historicalTrades` (查询订单簿历史成交)
    * 请求权重由 `20` 调整为 `200`。



* * *

## 2026-07-23

**生效日期：2026-07-23**

U 本位合约

  * `GET /fapi/v1/fundingRate`（查询资金费率历史）
    * 响应新增字段 `rateType`（STRING）：资金费率类型。`Regular` 为正常资金费率；`Special` 为股票分红产生的额外资金费率。



* * *

## 2026-07-21

**生效日期：2026-07-30**

U 本位合约

  * `PUT /fapi/v1/order`（修改订单）、`PUT /fapi/v1/batchOrders`（批量修改订单）及 WebSocket API `order.modify`
    * 新增可选请求参数 `modifyId`（INT）：用户自定义的改单标识，服务端原样透传且不校验唯一性；不传时不返回。
    * 响应在请求传入该参数时原样返回 `modifyId`。
  * `GET /fapi/v1/orderAmendment`（查询订单修改历史）
    * 响应中为每条携带 `modifyId` 的修改记录返回该字段。
  * 用户数据流 `ORDER_TRADE_UPDATE` 事件（`"x": "AMENDMENT"`）
    * 新增字段 `M`（STRING）：对应改单请求传入的 `modifyId`，仅在请求传入时推送。



币本位合约

  * `PUT /dapi/v1/order`（修改订单）、`PUT /dapi/v1/batchOrders`（批量修改订单）及 WebSocket API `order.modify`
    * 新增可选请求参数 `modifyId`（INT）：用户自定义的改单标识，服务端原样透传且不校验唯一性；不传时不返回。
    * 响应在请求传入该参数时原样返回 `modifyId`。
  * `GET /dapi/v1/orderAmendment`（查询订单修改历史）
    * 响应中为每条携带 `modifyId` 的修改记录返回该字段。
  * 用户数据流 `ORDER_TRADE_UPDATE` 事件（`"x": "AMENDMENT"`）
    * 新增字段 `M`（STRING）：对应改单请求传入的 `modifyId`，仅在请求传入时推送。



统一账户

  * `PUT /papi/v1/um/order` 与 `PUT /papi/v1/cm/order`（修改订单）
    * 新增可选请求参数 `modifyId`（INT）：用户自定义的改单标识，服务端原样透传且不校验唯一性；不传时不返回。
    * 响应在请求传入该参数时原样返回 `modifyId`。
  * `GET /papi/v1/um/orderAmendment` 与 `GET /papi/v1/cm/orderAmendment`（查询订单修改历史）
    * 响应中为每条携带 `modifyId` 的修改记录返回该字段。
  * 用户数据流 `ORDER_TRADE_UPDATE` 事件（`"x": "AMENDMENT"`）
    * 新增字段 `M`（STRING）：对应改单请求传入的 `modifyId`，仅在请求传入时推送。



* * *

## 2026-07-16

**生效日期：2026-07-16**

U 本位合约

  * `GET /fapi/v1/tradingSchedule`（交易时段）
    * 新增覆盖香港股票市场（`HK_EQUITY`），时段类型包括 `REGULAR` 和 `NO_TRADING`。
  * WebSocket 当前交易时段（`tradingSession`）
    * 新增香港股票市场事件类型 `HK_EquityUpdate`，时段类型包括 `REGULAR` 和 `NO_TRADING`。



* * *

## 2026-07-13

**生效日期：2026-07-14**

统一账户

  * 以下接口的响应中将移除 `cumBase`、`cumQuote` 和 `avgPrice` 字段：
    * POST `/papi/v1/um/order`
    * POST `/papi/v1/cm/order`
    * DELETE `/papi/v1/um/order`
    * DELETE `/papi/v1/cm/order`



* * *

## 2026-07-09

期权

  * REST API新增:
    * `POST /eapi/v1/stock/contract`: 签署传统金融期权协议



欧式期权

  * `GET /eapi/v1/exchangeInfo`（获取交易规则和交易对）
    * 响应 `optionSymbols` 中每个期权交易对新增 `contractType` 和 `underlyingType` 字段，分别表示合约类型和标的类型。



* * *

## 2026-06-30

币本位合约

  * `GET /dapi/v1/constituents`（查询指数价格成分）
    * 响应新增 `weight` 和 `price` 字段，与 U 本位合约接口（`GET /fapi/v1/constituents`）保持一致。
  * `GET /dapi/v1/pmAccountInfo`（查询经典统一账户账户信息）已不再使用，请改用 `GET /fapi/v1/pmAccountInfo`。
  * WebSocket Stream `<pair>@indexPrice`（最新现货指数价格）
    * 响应中的标的交易对字段由 `"i"` 改为 `"s"`。
    * 移除 `<pair>@indexPrice@1s`（1000ms）变体。该 Stream 现仅提供 `<pair>@indexPrice`，更新速度为1000ms。



* * *

## 2026-06-29

**时效性通知**

  * `POST /dapi/v1/countdownCancelAll`（币本位倒计时撤销所有挂单 / Countdown）
    * 币本位倒计时（自动撤单）功能将于 **2026-06-29 09:00 UTC（17:00 UTC+8）** 因币本位迁移维护而**暂停** ，并在**币本位恢复后重新启用** 。
    * 在暂停前设置的倒计时,在撮合引擎中仍然有效,直至停机打快照为止。
    * 如果用户设置的倒计时触发时间在维护快照之后,则这些交易对的倒计时将**不会** 生效。



* * *

## 2026-06-20

U 本位合约

  * `POST /fapi/v1/algoOrder`（下条件单）
    * 请求权重调整为下单限频：10s order rate limit(`X-MBX-ORDER-COUNT-10S`) 为 `1`；1min order rate limit(`X-MBX-ORDER-COUNT-1M`) 为 `1`。IP 权重维持为 `0`。



* * *

## 2026-06-16

**时效性通知**

  * 请注意,币本位合约 demo 交易将于 2026-06-16 02:00 至 10:00 UTC 期间不可用。
  * **更新：** 币本位合约 demo 交易停机维护窗口延长。新的窗口为 2026-06-16 02:00:00 至 2026-06-23 10:00:00 (UTC)。感谢您的耐心与理解。



* * *

## 2026-06-10

**生效日期: 2026-06-30**

币本位合约与 U 本位合约架构整合 — 涉及 REST 接口、WebSocket Stream、以及账户层行为的变更。完整的受影响接口清单与行动项请见 [币本位/U本位整合迁移公告](/zh-CN/docs/products/derivatives-trading-coin-futures/Important-CM-UM-Integration-Notice)。详细的时间线请参考[公告](https://www.binance.com/zh-CN/support/announcement/detail/2a84dfd7643f4dc18084e45e8691b69e)。

* * *

## 2026-06-02

**生效日期: 2026-06-02**

U 本位合约

  * `GET /fapi/v1/tradingSchedule`（交易时段）
    * 时间范围从查询时间前一日起算的“往后 7 天”扩展为**“往前 7 天 + 往后 7 天”**。
    * 新增韩国股票市场（`KR_EQUITY`）支持。韩国股票市场时段类型：`REGULAR` 和 `NO_TRADING`。
  * WebSocket Stream `tradingSession`（当前交易时段）
    * 新增韩国股票市场支持。
    * 新增事件类型 `KR_EquityUpdate`。韩国股票市场时段类型：`REGULAR` 和 `NO_TRADING`。



* * *

## 2026-05-11

**生效日期: 2026-05-13**

USDⓈ-M期货

  * `POST /fapi/v1/positionSide/dual`
    * 新增错误码 `-4531`：在修改 UM 的 `dualSidePosition` 时,系统会自动同步 CM 的 `dualSidePosition`。如果 CM 账户有任何持仓或挂单,则无法进行同步,UM 持仓模式的修改将被拒绝并返回错误码 `-4531`。

    * 错误信息:
          
          Code
          
          {
            "code": -4531,
            "msg": "Position mode change requires syncing UM and CM. Please close any open positions or orders in CM and try again."
          }

    * **注意** : 此错误码是临时的,仅在 CM 进入 Guard 之前有效(约 1 个月)。CM 进入 Guard 后,将不再出现此错误。




* * *

## 2026-04-17

统一账户Pro

  * Websocket账户信息推送更新:
    * 新增 `PM_PRO_ACCOUNT_UPDATE` 消息，每 5 秒推送一次账户资产状态。



* * *

## 2026-04-15

欧式期权

  * 交易接口
    * 批量撤销订单 - 修正请求权重，从 1 更正为 5。



* * *

## 2026-04-14

统一账户

  * 将在2026-04-28启用以下REST接口和WebSocket用户数据推送：

    * REST:
      * POST `/papi/v1/um/algo/order`
      * DELETE `/papi/v1/um/algo/order`
      * DELETE `/papi/v1/um/algo/allOpenOrders`
      * GET `/papi/v1/um/algo/algoOrder`
      * GET `/papi/v1/um/algo/openAlgoOrders`
      * GET `/papi/v1/um/algo/allAlgoOrders`
    * Websocket:
      * `ALGO_UPDATE`: 条件订单交易更新推送
  * 将在2026-04-28弃用以下REST接口：

    * REST:
      * POST `/papi/v1/um/conditional/order`
      * DELETE `/papi/v1/um/conditional/order`
      * DELETE `/papi/v1/um/conditional/allOpenOrders`
      * GET `/papi/v1/um/conditional/allOrders`
      * GET `/papi/v1/um/conditional/openOrders`
      * GET `/papi/v1/um/conditional/openOrder`
      * GET `/papi/v1/um/conditional/orderHistory`



请参考以下[公告](https://www.binance.com/en/support/announcement/detail/13980e4145ee41259d32f985161d81b6)进行接口替换和调整

* * *

## 2026-04-13

统一账户和统一账户Pro

REST API新增:

  * `POST /sapi/v1/portfolio/margin-call-level` : 设置统一保证金账户的强平预警线。当账户的 uniMMR 降至指定水平时，系统将通过邮件和短信发送通知。
  * `GET /sapi/v1/portfolio/margin-call-level` : 查询统一保证金账户的强平预警线。
  * `DELETE /sapi/v1/portfolio/margin-call-level` : 删除统一保证金账户的强平预警线。



* * *

## 2026-04-10

**生效日期: 2026-04-14**

COIN-M期货 / 统一账户和统一账户Pro

  * `POST /dapi/v1/positionSide/dual` 和 `POST /papi/v1/cm/positionSide/dual`
    * CM 的 `dualSidePosition` 必须与 UM 保持一致。如果 CM 的 `dualSidePosition` 已经与 UM 相同，则修改会被拒绝。



USDⓈ-M期货

  * 强平订单 (`<symbol>@forceOrder`) 和全市场强平订单 (`!forceOrder@arr`)
    * 更新描述：将"最近的强平订单"改为"最大的强平订单"。



* * *

## 2026-04-09

统一账户

  * User Data Stream
    * [杠杆账户订单事件](/zh-CN/docs/products/derivatives-trading-portfolio-margin/user-data-streams#%E6%9D%A0%E6%9D%86%E8%B4%A6%E6%88%B7%E8%AE%A2%E5%8D%95%E4%BA%8B%E4%BB%B6) \- `executionReport` 事件新增字段: `Cs`, `pl`, `pL`, `pY`, `eR`。



* * *

## 2026-04-08

统一账户

REST API新增:

  * `POST /papi/v1/um/stock/contract` : 签署传统金融合约协议



* * *

## 2026-04-06

USDⓈ-M期货 / COIN-M期货 / 统一账户和统一账户Pro

  * `GET /fapi/v1/forceOrders`、`GET /dapi/v1/forceOrders`、`GET /papi/v1/um/forceOrders` 和 `GET /papi/v1/cm/forceOrders`
    * 新增说明：本接口仅支持最近90天数据的查询。



* * *

## 2026-04-02

USDⓈ-M期货

  * Websocket
    * 更新 [WebSocket Base URL 迁移公告](/zh-CN/docs/products/derivatives-trading-usds-futures/websocket-market-streams/Important-WebSocket-Change-Notice)，新增旧 URL 下线日期：**2026-04-23** 。



* * *

## 2026-03-19

USDⓈ-M期货 / COIN-M期货

  * `GET /fapi/v1/historicalTrades` 和 `GET /dapi/v1/historicalTrades`
    * 数据查询范围从最近3个月调整为最近1个月。



## 2026-03-16

USDⓈ-M期货

  * 市场数据连接
    * `Mark-Price-Stream`和`Mark-Price-Stream-for-All-market`中新增字段`ap`显示标记价格移动平均



## 2026-03-11

欧式期权

  * 自2026-03-19起
  * 自成交保护
    * 和USDⓈ-M期货一样，期权已经支持 Self-Trade Prevention（STP）自成交保护。此功能将阻止订单与来自同一账户或者同一tradeGroupId 账户的订单交易(当前仅支持同一账户)。
    * 期权所有交易对支持通过下单时设置selfTradePreventionMode为下面之一的 STP 模式：
      * EXPIRE_MAKER: 自成交过期 maker 订单
      * EXPIRE_TAKER: 自成交过期 taker 订单
      * EXPIRE_BOTH: 自成交过期 taker 和 maker 订单
  * REST 更新:
    * 新的订单状态：EXPIRED_IN_MATCH \- 订单由于 STP 触发而过期
    * 以下接口新增可选参数selfTradePreventionMode以设置该订单的自成交保护模式：
      * POST /eapi/v1/order
      * POST /eapi/v1/batchOrders
    * 以下接口新增响应字段selfTradePreventionMode以显示订单的自成交保护模式：
      * POST /eapi/v1/order
      * POST /eapi/v1/batchOrders
      * GET /eapi/v1/order
      * GET /eapi/v1/openOrders
      * PUT /eapi/v1/order
      * PUT /eapi/v1/batchOrders
      * DELETE /eapi/v1/order
      * DELETE /eapi/v1/batchOrders
  * WEBSOCKET 账户信息推送更新:
    * ORDER_TRADE_UPDATE中新增字段V显示用户订单的自成交保护模式



## 2026-03-05

USDⓈ-M期货

  * Websocket
    * [WebSocket Base URL 迁移公告](/zh-CN/docs/products/derivatives-trading-usds-futures/websocket-market-streams/Important-WebSocket-Change-Notice)
    * 所有 WebSocket 行情推送页面新增 `URL PATH` 字段，标注新的 Base URL 路径（`/public`、`/market`）。
    * 所有用户数据推送事件页面新增 `URL PATH` 字段，标注新的 Base URL 路径（`/private`）。



## 2026-01-09

统一账户：

  * Rest API新增Delta中性账户新接口:
    * `POST /sapi/v1/portfolio/delta-mode`: 切换当前统一账户到Delta中性账户
    * `GET /sapi/v1/portfolio/delta-mode`: 查询当前账户到Delta中性状态



## 2026-01-07

期权

  * REST API新增:
    * `GET /eapi/v1/commission`: 获取用户手续费率



## 2025-12-29

USDⓈ-M期货

  * "filterType": "MAX_NUM_ALGO_ORDERS" 返回已从接口 `GET /fapi/v1/exchangeInfo`移除。所有币对的未平仓条件单上限为 200 笔。
  * 自2025-12-31起，归集交易数据流`<symbol>@aggTrade`增加字段`nq`，其聚合普通订单成交量，不包含RPI订单数据。



## 2025-12-11

USDⓈ-M期货

  * REST API新增:
    * `GET /fapi/v1/tradingSchedule`: 获取一周交易时段信息
    * `POST /fapi/v1/stock/contract`: 签署传统金融合约协议
  * Websocket API新增:
    * `tradingSession`: 获取当前交易时段信息



## 2025-12-10

  * 由于条件订单已迁移至Algo服务，事件 `CONDITIONAL_ORDER_TRIGGER_REJECT` 将于2025年12月15日起废止。所有条件订单的拒绝原因已通过 `ALGO_UPDATE` 事件提供。



## 2025-12-09

COIN-M期货

  * 自2025-12-10起，订单交易更新推送事件`ORDER_TRADE_UPDATE`增加订单过期原因字段`er`。



## 2025-11-25

USDⓈ-M期货

  * 自 **2025-11-26** 起，用户手续费率接口支持查询RPI手续费率
    * REST
      * `GET /fapi/v1/commissionRate`
  * 提供如下新接口，获取RPI深度信息
    * REST
      * `GET /fapi/v1/rpiDepth`
    * WebSocket
      * `<symbol>@rpiDepth@500ms`



## 2025-11-19

USDⓈ-M期货

  * REST API更新:
    * `GET /fapi/v1/symbolAdlRisk`: 查询自动减仓风险评级



## 2025-11-18

USDⓈ-M期货

  * 支持RPI订单
    * 有效方式 (timeInForce)新增“RPI”枚举值
      * REST
        * `POST /fapi/v1/order`
        * `POST /fapi/v1/batchOrders`
      * WebSocket
        * `order.place`
    * 新响应字段"IsRPITrade"(布尔)
      * REST
        * `GET /fapi/v1/trades`
        * `GET /fapi/v1/historicalTrades`
    * RPI订单不包含在订单簿
      * REST
        * `GET /fapi/v1/depth`
        * `GET /fapi/v1/ticker/bookTicker`
      * WebSocket
        * `ticker.book`
        * `<symbol>@bookTicker`
        * `!bookTicker`
        * `<symbol>@depth<levels>`
        * `<symbol>@depth`
  * 更多详细信息，请阅读 - <https://www.binance.com/en/support/faq/92c83c53173947c4a44f9a7277c3b9ce>



## 2025-11-12

币安衍生品正在重建期权系统，以提升整体的稳定性、性能与可扩展性，并引入更多新功能。

作为第一步，我们已上线全新的期权 Demo API 环境，以便现有用户能够提前调整代码，适配新系统。相关文档可在 “Options Demo Trading” 标签页中查看。

请前往 <https://demo.binance.com/zh-CN/my/settings/api-management> 创建新的 API Key，该 Key 可用于访问全新的期权 Demo 交易环境。

## 2025-11-10

  * BFUSD 已于 2025-08-13 迁移至 Binance Earn，以下接口已被废弃：
    * `POST sapi/v1/portfolio/mint`
    * `POST sapi/v1/portfolio/redeem`



## 2025-11-06

  * USDT-M合约将在 **2025-12-09** 起将条件订单迁移到Algo服务, 以下订单类型将会受到影响： `STOP_MARKET`/`TAKE_PROFIT_MARKET`/`STOP`/`TAKE_PROFIT`/`TRAILING_STOP_MARKET`.

  * REST API 将提供如下新接口进行条件订单的下单、撤单和查询:

    * `POST fapi/v1/algoOrder`: 条件单下单
    * `DELETE /fapi/v1/algoOrder`: 条件单撤单
    * `DELETE fapi/v1/algoOpenOrders`: 撤销所有条件单
    * `GET /fapi/v1/algoOrder`: 查询条件订单
    * `GET /fapi/v1/openAlgoOrders`: 查询条件订单挂单
    * `GET /fapi/v1/allAlgoOrders`: 查询所有条件单
  * 切换后以下接口下 `STOP_MARKET`/`TAKE_PROFIT_MARKET`/`STOP`/`TAKE_PROFIT`/`TRAILING_STOP_MARKET`类型订单会被拦截。请求接口会遇到错误码 `-4120` STOP_ORDER_SWITCH_ALGO 。

    * `POST /fapi/v1/order`
    * `POST /fapi/v1/batchOrders`
  * 用户数据更新

    * 条件单新增事件: `ALGO_UPDATE`
  * Websocket API 更新

    * 条件单下单 : `algoOrder.place`
    * 条件单撤单: `algoOrder.cancel`
  * 本次迁移的影响点如下：

    * 条件单在触发前不会进行保证金校验
    * GTE_GTC 订单不再依赖于对手方的未平仓订单，而仅依赖于持仓情况
    * 订单触发不会增加延迟
    * 条件单暂不支持改单



## 2025-10-21

  * 自 **2025-10-23** 起，下单/改单接口中的 `priceMatch` 枚举 **`OPPONENT_10`** 、**`OPPONENT_20`** 暂时移除，其余枚举不受影响。影响接口如下：

**USDT-M 合约 (`/fapi`)**

    * `POST /fapi/v1/order`
    * `POST /fapi/v1/batchOrders`
    * `PUT /fapi/v1/order`
    * `PUT /fapi/v1/batchOrders`

**COIN-M 合约 (`/dapi`)**

    * `POST /dapi/v1/order`
    * `POST /dapi/v1/batchOrders`
    * `PUT /dapi/v1/order`
    * `PUT /dapi/v1/batchOrders`

**Portfolio Margin (`/papi`)**

    * `POST /papi/v1/um/order`
    * `PUT /papi/v1/um/order`
    * `POST /papi/v1/um/conditional/order`
    * `POST /papi/v1/cm/order`
    * `PUT /papi/v1/cm/order`
    * `POST /papi/v1/cm/conditional/order`



## 2025-10-20

USDⓈ-M期货

  * 自2025-10-23起，订单交易更新推送事件`ORDER_TRADE_UPDATE`增加订单过期原因字段`er`。



## 2025-10-14

  * 自 2025-10-23 起，下列错误码的提示信息将更新：


    
    
    Code
    
    {
        "code": -1008,
        "msg": "Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again."
    }

## 2025-10-09

  * 合约系统新增：支持中文交易对名称（`symbol` 可为中文）。`exchangeInfo` 返回示例：`"symbol": "测试USDT"`。
  * 通过 API 下单时，若 `symbol` 含中文，必须进行 URL 编码（UTF-8 百分号编码）。示例：  
`https://fapi.binance.com/fapi/v1/order?symbol=%E6%B5%8B%E8%AF%95USDT&side=BUY&type=TAKE_PROFIT_MARKET&timeInForce=GTC&quantity=1&stopPrice=30&timestamp=1760000007980`
  * 推送消息（WebSocket/用户数据流）中的 `symbol` 也可能为中文，请确保客户端/下游系统对中文解析、解码与显示的兼容性。
  * 未对中文 `symbol` 进行编码可能导致请求失败或参数解析错误。



## 2025-08-11

  * BFUSD 将于 2025-08-13 迁移至 Binance Earn。迁移完成后，以下接口将被废弃：
    * `POST sapi/v1/portfolio/mint`
    * `POST sapi/v1/portfolio/redeem`
  * 调用上述接口可能会遇到错误码 `-21015`（ENDPOINT_GONE）。
  * Portfolio Margin 和 Portfolio Margin Pro 用户可切换至 Binance Earn 进行 BFUSD 的铸造和赎回。迁移后，Portfolio Margin 钱包中的现有 BFUSD 可先通过资产归集接口（`POST /sapi/v1/portfolio/asset-collection`）进行资金归集，然后将BFUSD资产从 Portfolio Margin 钱包转至现货钱包进行赎回。



## 2025-07-25

  * fapi新增下列错误码:
    * `-4109`: _This account is inactive, please activate the account first._ 这表示该账户因长期未使用而被归档。要激活账户，请向USDM合约账户转入任意金额的资产。



## 2025-07-02

USDⓈ-M期货

  * REST API更新:

    * `GET /futures/data/openInterestHist`: 响应增加`CMCCirculatingSupply`
  * 市场数据连接:

    * 单个连接最多可以订阅Streams个数从200增加到1024。



## 2025-04-23

USDⓈ-M期货

  * REST API更新:
    * `GET /fapi/v1/insuranceBalance`: 查询保险基金余额快照
    * `GET /fapi/v1/constituents`: 响应增加`price`和`weight`



## 2025-04-15

Portfolio Margin and Portfolio Margin Pro

  * 统一账户支持Earn资产作为抵押物相关接口:
    * `POST /sapi/v1/portfolio/earn-asset-transfer`: 统一账户转入LDUSDT资产
    * `GET /sapi/v1/portfolio/earn-asset-balance`: 查询统一账户LDUSDT可转金额



## 2025-02-28

Portfolio Margin Pro

  * 统一账户专业版新增穿仓借贷偿还记录查询（将于2025-02-28生效）:
    * `GET /sapi/v1/portfolio/pmloan-history`



## 2025-02-20

币本位合约

WEBSOCKET API

  * Websocket API 将于2025-02-25，可通过以下 URL 访问：“wss://ws-dapi.binance.com/ws-dapi/v1”
  * WebSocket API 允许通过 WebSocket 连接下单、取消订单等。
  * WebSocket API 是独立于 WebSocket 市场数据流的服务。也就是说，下订单和收听市场数据需要两个独立的 WebSocket 连接。
  * WebSocket API 受与 REST API 相同的过滤器和速率限制规则的约束。
  * WebSocket API 和 REST API 在功能上是等效的：它们提供相同的功能，接受相同的参数，返回相同的状态和错误代码。



## 2025-01-20

Portfolio Margin

  * 统一账户新增查询用户负余额自动兑换记录（将于2025-01-22生效）:
    * `GET /papi/v1/portfolio/negative-balance-exchange-record`



## 2025-01-13

USDⓈ-M Futures & COIN-M Futures

  * 下列接口将在2024-01-14被调整：

    * `GET /fapi/v1/historicalTrades`
    * `GET /dapi/v1/historicalTrades`

接口请求参数`limit`调整内容为:

    * 最大值从1000改为500
    * 默认值从500改为100



## 2025-01-06

Portfolio Margin

  * 统一账户新增查询用户下单限频接口:
    * `GET papi/v1/rateLimit/order`



## 2024-12-19

Portfolio Margin Pro & Portfolio Margin

  * 统一账户新增BFUSD申购和赎回接口（将于2024-12-20生效）:
    * `POST sapi/v1/portfolio/mint`
    * `POST sapi/v1/portfolio/redeem`



## 2024-12-17

期权

  * REST API: 新增 `GET /eapi/v1/blockTrades`以查询最近的大宗交易

  * Websocket行情推送: 在消息`<symbol>@trade`和 `<underlyingAsset>@trade`增加字段`X`显示交易类型




## 2024-12-02

USDⓈ-M Futures

  * 将于2024-12-03增加下列错误码:
    * `-4116`: ClientOrderId is duplicated.
    * `-4117`: Stop order is in triggering process. Please try again later.



## 2024-11-04

USDⓈ-M期货和币本位合约

  * `GET /fapi/v1/pmExchangeInfo` 和 `GET /dapi/v1/pmExchangeInfo` 将于2024-11-15停用



## 2024-11-01

期权

  * 新增做市商大宗交易接口：
    * `POST eapi/v1/block/order/create`
    * `PUT eapi/v1/block/order/create`
    * `DELETE eapi/v1/block/order/create`
    * `GET eapi/v1/block/order/orders`
    * `POST eapi/v1/block/order/execute`
    * `GET eapi/v1/block/order/execute`
    * `GET eapi/v1/block/user-trades`



## 2024-10-29

Portfolio Margin Pro

  * 下列REST接口被调整：
    * `POST /sapi/v1/portfolio/repay-futures-switch`: 从2024-11-01开始, 接口限频为每天20次。



Portfolio Margin

  * T下列REST接口被调整：
    * `POST /papi/v1/repay-futures-switch`: 从2024-11-01开始, 接口限频为每天20次。



## 2024-10-24

欧式期权

  * 接口字段删除(2024-10-28生效)：
    * `GET /eapi/v1/exchangeInfo`接口移除`optionContracts`中的`id`字段，移除`optionAssets`中的`id`字段，移除`optionSymbols`中的`contractId`和`id`字段
    * 推送`option_pair`中移除`id`和`cid`字段



## 2024-10-21

USDⓈ-M期货和币本位合约

  * 币安合约预计于2024年10月30日08:00（东八区时间）更新以下接口。自2024年10月30日08:00（东八区时间）之后，以下接口仅支持查询不超过最近6个月的合约交易数据：
    * `GET /fapi/v1/userTrades`
    * `GET /dapi/v1/userTrades`



币本位合约

  * 新增历史数据下载接口：
    * `GET /dapi/v1/order/asyn`: 获取合约订单历史下载id
    * `GET /dapi/v1/order/asyn/id`: 通过下载id获取合约订单历史下载链接
    * `GET /dapi/v1/trade/asyn`: 获取合约交易历史下载id
    * `GET /dapi/v1/trade/asyn/id`: 通过下载id获取合约交易历史下载链接



## 2024-10-15

Portfolio Margin Pro(Release date 2024-10-18)

  * 新增查询统一账户专业版SPAN账户信息接口(仅统一账户专业版SPAN可查):
    * `GET /sapi/v2/portfolio/account`
  * 新增查询统一账户专业版账户资产信息接口:
    * `GET /sapi/v1/portfolio/balance`



Portfolio Margin

  * 新增获取统一账户UM合约交易历史下载Id:
    * `GET /papi/v1/um/trade/asyn`
  * 新增通过下载Id获取统一账户UM合约交易历史下载链接:
    * `GET /papi/v1/um/trade/asyn/id`
  * 新增获取统一账户UM合约订单历史下载Id:
    * `GET /papi/v1/um/order/asyn`
  * 新增通过下载Id获取统一账户UM合约订单历史下载链接:
    * `GET /papi/v1/um/order/asyn/id`
  * 新增获取统一账户UM合约资金流水历史下载Id:
    * `GET /papi/v1/um/income/asyn`
  * 新增通过下载Id获取统一账户UM合约资金流水历史下载链接:
    * `GET /papi/v1/um/income/asyn/id`



## 2024-10-14

USDⓈ-M 期货

  * 下列REST接口被调整：
    * `POST /fapi/v1/convert/getQuote`: 从2024-10-19开始，接口限频为每小时360次，每天500次。
    * `POST /fapi/v1/convert/getQuote`: `validTime`的枚举值调整为仅支持`10s`



## 2024-10-11

币本位合约

  * **自成交保护**

  * 币本位合约系统中已经支持 Self-Trade Prevention（STP）自成交保护。此功能将阻止订单与来自同一账户或者同一`tradeGroupId` 账户的订单交易(当前仅支持同一账户)。详情请参考 [FAQ](https://www.binance.com/cn/support/faq/0941126f6413485b9a3df964a9aa2306)

  * 合约所有交易对支持通过下单时设置`selfTradePreventionMode`为下面之一的 STP 模式：

    * NONE: 不设置自成交保护
    * EXPIRE_TAKER: 自成交过期 taker 订单
    * EXPIRE_MAKER: 自成交过期 maker 订单
    * EXPIRE_BOTH: 自成交过期 taker 和 maker 订单
  * REST 更新:

    * 新的订单状态：`EXPIRED_IN_MATCH` \- 订单由于 STP 触发而过期
    * 以下接口新增可选参数`selfTradePreventionMode`以设置该订单的自成交保护模式：
      * `POST /dapi/v1/order`
      * `POST /dapi/v1/batchOrders`
    * 以下接口新增响应字段`selfTradePreventionMode`以显示订单的自成交保护模式：
      * `POST /dapi/v1/order`
      * `POST /dapi/v1/batchOrders`
      * `GET /dapi/v1/order`
      * `GET /dapi/v1/openOrders`
      * `GET /dapi/v1/allOrders`
      * `PUT /dapi/v1/order`
      * `PUT /dapi/v1/batchOrders`
      * `DELETE /dapi/v1/order`
      * `DELETE /dapi/v1/batchOrders`
  * WEBSOCKET 账户信息推送更新:

    * `ORDER_TRADE_UPDATE`中新增字段`V`显示用户订单的自成交保护模式
  * **价格匹配**

  * 币本位合约系统中已经支持价格匹配功能（priceMatch）。此功能将允许用户的LIMIT/STOP/TAKE_PROFIT订单无需输入价格，价格匹配功能将根据订单的价格匹配模式和订单簿实时自动确定订单价格。

  * 合约LIMIT/STOP/TAKE_PROFIT订单支持设置priceMatch以价格匹配模式：

    * NONE: 设置价格匹配
    * OPPONENT: 盘口对手价
    * OPPONENT_5: 盘口对手5档价
    * OPPONENT_10: 盘口对手10档价
    * OPPONENT_20: 盘口对手20档价
    * QUEUE: 盘口同向价
    * QUEUE_5: 盘口同向排队5档价
    * QUEUE_10: 盘口同向排队10档价
    * QUEUE_20: 盘口同向排队20档价
  * 例子:

    * 用户下买单，设置priceMatch为QUEUE_5，则订单价格为订单薄买方向（盘口同向）第五档价格
    * 用户下买单，设置priceMatch为OPPONENT，则订单价格为订单薄卖方向（盘口对手）第一档价格
  * REST更新:

    * 以下接口新增可选参数priceMatch以设置价格匹配类型：
      * `POST /dapi/v1/order`
      * `POST /dapi/v1/batchOrders`
    * 以下接口新增响应字段priceMatch以显示订单的价格匹配模式：
      * `POST /dapi/v1/order`
      * `POST /dapi/v1/batchOrders`
      * `GET /dapi/v1/order`
      * `GET /dapi/v1/openOrders`
      * `GET /dapi/v1/allOrders`
      * `PUT /dapi/v1/order`
      * `PUT /dapi/v1/batchOrders`
      * `DELETE /dapi/v1/order`
      * `DELETE /dapi/v1/batchOrders`
  * Websocket账户信息推送更新:

    * ORDER_TRADE_UPDATE中新增字段`pm`显示用户订单的价格匹配模式



## 2024-10-10

USDⓈ-M 期货

  * 预计于2024年10月17日11:00（东八区时间）更新以下接口。自2024年10月17日11:00（东八区时间）后，以下接口将支持查询不超过1年的合约交易数据：

    * `GET /fapi/v1/aggTrades`
    * `GET /dapi/v1/aggTrades`
  * 预计于2024年10月16日11:00（东八区时间）更新以下接口。自2024年10月16日11:00（东八区时间）后，以下接口将支持查询不超过1个月的合约数据：

    * `GET /fapi/v1/positionMargin/history`



## 2024-10-08

COIN-M 期货

  * 请求以下接口时，默认返回最近7天的数据。这些接口的查询时间段必须小于7天：

    * `获取 /dapi/v1/allOrders`
    * `获取 /dapi/v1/userTrades`
  * 以下接口将进行调整，仅保留最近三个月的数据：

    * `获取 /dapi/v1/order`
    * `获取 /dapi/v1/allOrders`



## 2024-09-27

USDⓈ-M 期货

  * 下列websocket用户信息请求被停止使用:
    * `listenkey@account`
    * `listenkey@balance`
    * `listenkey@position`



COIN-M 期货

  * 下列websocket用户信息请求被停止使用:
    * `listenkey@account`
    * `listenkey@balance`
    * `listenkey@position`



## 2024-09-19

Portfolio Margin

  * 新增杠杆账户还款接口: `POST /papi/v1/margin/repay-debt`



## 2024-09-06

Portfolio Margin

  * Portfolio Margin/Trade接口更新(Release date 2024-09-06):

    * `POST /papi/v1/um/order`: 新增入参`priceMatch`以支持下单
    * `POST/papi/v1/um/conditional/order`: 新增入参`priceMatch`以支持条件单下单
    * `PUT /papi/v1/um/order`: 新增入参`priceMatch`以支持改单
  * 以下接口新增返回 `priceMatch`:

    * `POST /papi/v1/um/order`
    * `POST/papi/v1/um/conditional/order`
    * `PUT /papi/v1/um/order`
    * `GET /papi/v1/um/orderAmendment`
    * `GET /papi/v1/um/order`
    * `GET /papi/v1/um/openOrder`
    * `GET /papi/v1/um/openOrders`
    * `GET /papi/v1/um/allOrders`
    * `GET /papi/v1/um/conditional/openOrder`
    * `GET /papi/v1/um/conditional/openOrders`
    * `GET /papi/v1/um/conditional/orderHistory`
    * `GET /papi/v1/um/conditional/allOrders`
    * `DELETE /papi/v1/um/order`
    * `DELETE /papi/v1/um/conditional/order`
  * WEBSOCKET

    * `ORDER_TRADE_UPDATE` 和 `CONDITIONAL_ORDER_TRADE_UPDATE` 新增`pm`推送以支持priceMatch



## 2024-09-05

Portfolio Margin Pro

  * 新增查询统一账户专业版资产阶梯质押率信息的接口：
    * `GET /sapi/v2/portfolio/collateralRate`



## 2024-09-03

USDⓈ-M 期货

  * 账户信息推送中新增新增`TRADE_LITE`事件类型。`TRADE_LITE`旨在通过精简用户信息数据和仅推送用户已成交的TRADE数据流，从而降低用户数据推送的延迟。相比于现有的`ORDER_TRADE_UPDATE`事件类型，`TRADE_LITE`将提供更加敏捷和高效的用户体验。



## 2024-08-26

USDⓈ-M 期货

  * 新增账户内资产转换接口:
    * `GET /fapi/v1/convert/exchangeInfo`
    * `POST /fapi/v1/convert/getQuote`
    * `POST /fapi/v1/convert/acceptQuote`
    * `GET /fapi/v1/convert/orderStatus`



## 2024-08-23

Portfolio Margin

  * 新增查询账户信息的接口：
    * `POST /papi/v1/um/feeBurn`: BNB UM合约交易抵扣开关。
    * `GET /papi/v1/um/feeBurn`: 获取UM合约交易 BNB 抵扣开关状态。
  * 新增查询交易信息的接口：
    * `GET /papi/v1/um/accountConfig`: 查询用户UM账户配置。
    * `GET /papi/v1/um/symbolConfig`: 查询用户UM交易对配置。
    * `GET /papi/v2/um/account`: 相较于`GET /papi/v1/um/account`，此接口仅返回用户有持仓或挂单的交易对。账户/交易对配置相关字段已被移除，现在可以通过 `GET /papi/v1/um/symbolConfig` 和 `GET /papi/v1/um/accountConfig` 查询。V2接口还提供了更好的性能。



## 2024-08-07

USDⓈ-M 期货

  * 以下接口将在2024-09-03进行权重调整：

    * REST API:
      * `GET /fapi/v2/balance`: 5->10
      * `GET /fapi/v2/account`: 5->10
      * `GET /fapi/v2/positionRisk`: 5->10
    * Websocket API:
      * `account.status`: 5->10
      * `account.balance`: 5->10
      * `account.position`: 5->10
  * 将弃用以下WebSocket用户数据请求：

    * <listenKey>@account
    * <listenKey>@balance
    * <listenKey>@position



请参考以下[公告](https://www.binance.com/zh-CN/support/announcement/%E5%85%B3%E4%BA%8E%E5%B0%86%E6%9B%B4%E6%96%B0%E5%B8%81%E5%AE%89api%E7%9A%84%E5%85%AC%E5%91%8A-2024-09-03-19d4e3cd0758426584dd9686eb56ec64)进行接口替换和调整

## 2024-08-06

COIN-M 期货

因统一账户专业版移除`notionalLimit`限制，`GET /dapi/v1/pmExchangeInfo` 将于8月6日停用

## 2024-07-24

USDⓈ-M 期货

#### REST API

  * 新增查询账户信息的接口：

    * `GET /fapi/v1/symbolConfig`: 查询用户交易对配置。
    * `GET /fapi/v1/accountConfig`: 查询用户账户配置。
    * `GET /fapi/v3/account`: 相较于 `GET /fapi/v2/account`，此接口仅返回用户有持仓或挂单的交易对。账户/交易对配置相关字段已被移除，现在可以通过 `GET /fapi/v1/symbolConfig` 和 `GET /fapi/v1/accountConfig` 查询。V3接口还提供了更好的性能。
    * `GET /fapi/v3/balance`: 查询用户账户余额。
  * 新增查询交易信息的接口：

    * `GET /fapi/v3/positionRisk`: 相较于 `GET /fapi/v2/positionRisk`，此接口仅返回用户有持仓或挂单的交易对。交易对配置相关字段已被移除，现在可以通过 `GET /fapi/v1/symbolConfig` 查询。V3接口还提供了更好的性能。



#### WebSocket API

  * 新增查询账户信息的接口：
    * `v2/account.status`: 相较于 `account.status`，此接口仅返回用户有持仓或挂单的交易对。配置相关字段已被移除，现在可以通过 `GET /fapi/v1/symbolConfig` 和 `GET /fapi/v1/accountConfig` 查询。V2接口还提供了更好的性能。
    * `v2/account.balance`: 查询用户账户余额。
    * `v2/account.position`: 相较于 `account.position`，此接口仅返回用户有持仓或挂单的接口。配置相关字段已被移除，现在可以通过 `GET /fapi/v1/symbolConfig` 查询。V2接口还提供了更好的性能。



**弃用通知：**

  * 以下接口将在未来几个月内弃用（具体日期待定）。请切换到上述新接口：
    * REST API:
      * `GET /fapi/v2/balance`
      * `GET /fapi/v2/account`
      * `GET /fapi/v2/positionRisk`
    * Websocket API:
      * `account.status`
      * `account.balance`
      * `account.position`



* * *

## 2024-07-17

统一账户

#### REST API

  * `GET /papi/v1/um/userTrades`的响应字段`marginAsset`将在2024-07-17被移除



* * *

## 2024-06-19

U本位合约

#### REST API

  * `GET /fapi/v1/userTrades`的响应字段`marginAsset`将在2024-07-17被移除



* * *

## 2024-05-22

U本位合约

REST API & Websocket API

  * 新增BNB抵扣开关接口:
    * `POST /fapi/v1/feeBurn` BNB 合约交易抵扣开关。
    * `GET /fapi/v1/feeBurn` 获取 BNB 抵扣开关状态。



* * *

## 2024-04-19

U本位合约

REST API & Websocket API

  * 调用`PUT /fapi/v1/listenKey`或WebSocket api `userDataStream.ping`时会增加新的返回字段listenKey以显示有效期被延长的listenkey，改动将于2024-04-25生效。


    
    
    Code
    
    {
        "listenKey": "3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg"
    }

* * *

## 2024-04-09

U本位合约/币本位合约/统一账户

WEBSOCKET API

  * Good-Till-Cancel(GTC)订单变为仅有一年的有效期。 超过一年的GTC订单将被自动取消。改动适用于所有订单类型，包括仅减仓订单（reduceOnly），但不影响部分成交订单或策略交易或跟单交易订单。



* * *

## 2024-04-01

U本位合约

WEBSOCKET API

  * Websocket API 现已推出，可通过以下 URL 访问：“wss://ws-fapi.binance.com/ws-fapi/v1”
  * WebSocket API 允许通过 WebSocket 连接下单、取消订单等。
  * WebSocket API 是独立于 WebSocket 市场数据流的服务。也就是说，下订单和收听市场数据需要两个独立的 WebSocket 连接。
  * WebSocket API 受与 REST API 相同的过滤器和速率限制规则的约束。
  * WebSocket API 和 REST API 在功能上是等效的：它们提供相同的功能，接受相同的参数，返回相同的状态和错误代码。



* * *

## 2024-03-11

U本位合约

REST

  * 新增账户接口:
    * `GET /fapi/v1/rateLimit/order`: 查询用户下单频率限制



* * *

## 2024-02-09

U本位合约

币安合约在进行 Websocket 服务升级，升级影响以下逻辑：

  * 升级前：

    * 服务端每 3 分钟会发送 ping 帧，客户端应当在 10 分钟内回复 pong 帧，否则服务端会主动断开链接。允许客户端发送不成对的 pong 帧(即客户端可以以高于 10 分钟每次的频率发送 pong 帧保持链接)
  * 升级后

    * Websocket 服务器每 3 分钟发送 Ping 消息。
      * 如果 Websocket 服务器在 10 分钟之内没有收到 Pong 消息应答，连接会被断开。
      * 当客户收到 ping 消息，必需尽快回复 pong 消息，同时 payload 需要和 ping 消息一致。
      * 未经请求的 pong 消息是被允许的，但是不会保证连接不断开。**对于这些 pong 消息，建议 payload 为空**



* * *

## 2024-01-24

U本位合约

测试网 WEBSOCKET

  * **testnet** 的 Websocket baseurl 更新为 "wss://fstream.binancefuture.com"



* * *

## 2024-01-19

统一账户

  * REST
    * 新增 `PUT /papi/v1/um/order` 和 `PUT /papi/v1/cm/order` 接口以支持合约限价订单修改功能
    * 新增 `GET /papi/v1/um/orderAmendment` 和 `GET /papi/v1/cm/orderAmendment` 接口以查询合约订单修改历史



* * *

## 2024-01-11

统一账户

  * **自成交保护(已发布)**

  * U 本位合约系统中将支持 Self-Trade Prevention（STP）自成交保护。此功能将阻止订单与来自同一账户或者同一 tradeGroupId 账户的订单交易。详情请参考 [FAQ](https://www.binance.com/en/support/faq/what-is-self-trade-prevention-stp-0941126f6413485b9a3df964a9aa2306)

  * 合约所有交易对支持通过下单时设置`selfTradePreventionMode`为下面之一的 STP 模式：

    * NONE: 不设置自成交保护
    * EXPIRE_TAKER: 自成交过期 taker 订单
    * EXPIRE_MAKER: 自成交过期 maker 订单
    * EXPIRE_BOTH: 自成交过期 taker 和 maker 订单
  * REST 更新:

    * 新的订单状态：`EXPIRED_IN_MATCH` \- 订单由于 STP 触发而过期

    * /papi/v1/um/account 中响应新增字段`tradeGroupId`显示用户的 tradeGroupId

    * 以下接口新增可选参数`selfTradePreventionMode`以设置该订单的自成交保护模式：

      * POST /papi/v1/um/order
      * POST/papi/v1/um/conditional/order
      * POST /papi/v1/margin/order
      * POST /papi/v1/margin/order/oco
    * 以下接口新增响应字段`selfTradePreventionMode`以显示订单的自成交保护模式：

      * POST /papi/v1/um/order

      * POST/papi/v1/um/conditional/order

      * GET /papi/v1/um/order

      * GET /papi/v1/um/openOrder

      * GET /papi/v1/um/openOrders

      * GET /papi/v1/um/allOrders

      * GET /papi/v1/um/conditional/openOrder

      * GET /papi/v1/um/conditional/openOrders

      * GET /papi/v1/um/conditional/orderHistory

      * GET /papi/v1/um/conditional/allOrders

      * DELETE /papi/v1/um/order

      * DELETE /papi/v1/um/conditional/order

      * DELETE /papi/v1/margin/order

      * DELETE /papi/v1/margin/allOpenOrders

      * DELETE /papi/v1/margin/orderList

      * GET /papi/v1/margin/order

      * GET /papi/v1/margin/allOrders

      * GET /papi/v1/margin/orderList

      * GET /papi/v1/margin/allOrderList

      * GET /papi/v1/margin/openOrderList

  * WEBSOCKET 账户信息推送更新:

    * `ORDER_TRADE_UPDATE`和`CONDITIONAL_ORDER_TRADE_UPDATE`中新增字段`V`显示用户订单的自成交保护模式
    * `executionReport`中新增以下字段
      * `u` \- `tradeGroupId`
      * `v` \- `preventedMatchId`
      * `U` \- `counterOrderId`
      * `A` \- `preventedQuantity`
      * `B` \- `lastPreventedQuantity`
  * **有效方式 GTD(已发布)**

  * U 本位合约系统中将支持有效方式 GTD(Good Till Date)。有效方式(TIF)为 GTD 的订单到`goodTillDate`时间仍未完结会被自动取消

  * REST 更新:

    * 以下接口新增响应字段`goodTillDate`以配置 GTD 订单过期时间： _POST /papi/v1/um/order_ POST/papi/v1/um/conditional/order
    * 以下接口新增响应字段`goodTillDate`以显示 GTD 订单过期时间： _POST /papi/v1/um/order_ POST/papi/v1/um/conditional/order _GET /papi/v1/um/order_ GET /papi/v1/um/openOrder _GET /papi/v1/um/openOrders_ GET /papi/v1/um/allOrders _GET /papi/v1/um/conditional/openOrder_ GET /papi/v1/um/conditional/openOrders _GET /papi/v1/um/conditional/orderHistory_ GET /papi/v1/um/conditional/allOrders _DELETE /papi/v1/um/order_ DELETE /papi/v1/um/conditional/order
  * Websocket 账户信息推送更新:

`ORDER_TRADE_UPDATE`和 `CONDITIONAL_ORDER_TRADE_UPDATE`中新增字段 `goodTillDate`` 显示用户 GTD 订单的自动取消时间

  * **盈亏平衡价(已发布)**

  * REST 更新

    * 以下接口返回新增`breakEvenPrice`字段代表仓位盈亏平衡价： _GET /papi/v1/um/account_ GET /papi/v1/um/positionRisk _GET /papi/v1/cm/account_ GET /papi/v1/cm/positionRisk
  * WEBSOCKET 更新

    * Position 更新推送 payloadACCOUNT_UPDATE 中 P 新增 bep 字段代表仓位盈亏平衡价



* * *

## 2024-01-08

U本位合约

REST

  * 账号与交易接口更新(将于 2023-01-11 更新)：
    * `PUT /fapi/v1/order`: 新增入参`priceMatch`以支持改单价格保护
    * `PUT /fapi/v1/batchOrders`: 新增入参`priceMatch`以支持改单价格保护
    * 改单会保留该订单原有的`selfTradePreventionMode`



* * *

## 2023-12-12

U本位合约

WEBSOCKET

  * 行情推送`!bookTicker`的更新速度将从实时更改为每 5 秒一次，该更改将从 2023 年 12 月 20 日开始。单个交易对的 Book Ticker 流`<symbol>@bookticker`不会受到此次更新的影响。



* * *

## 2023-11-15

U本位合约

REST

  * 新增市场数据接口:
    * `GET /fapi/v2/ticker/price`: 查询最新价格 v2 接口。与`GET /fapi/v1/ticker/price`相比，v2 接口入参和响应相同，但接口延迟更低且占用限频更少。`GET /fapi/v1/ticker/price`将在未来被弃用，时间待定



WEBSOCKET

  * 币安合约将于 2023-12-15 06:00 停用`wss://fstream-auth.binance.com`域名，建议 API 用户在此时间前迁移 websocket 连接到`wss://fstream.binance.com`。需要特别注意的是，`wss://fstream.binance.com`的连接方法与`wss://fstream-auth.binance.com`不同，例如：
    * `wss://fstream-auth.binance.com/ws/<ListenKey>?listenKey=<ListenKey>` should change to `wss://fstream.binance.com/ws/<ListenKey>`



* * *

## 2023-11-01

币本位合约

REST

  * `GET dapi/v1/fundingRate`更新:
    * 增加返回字段`markPrice`以显示特定资金费对应的标记价格



* * *

## 2023-11-01

U本位合约

REST

  * 新增市场数据接口:
    * `GET /futures/data/basis`: 查询基差
  * `GET /fapi/v1/fundingRate`更新:
    * 增加返回字段`markPrice`以显示特定资金费对应的标记价格



* * *

## 2023-10-19

币本位合约

REST

  * 新增行情接口：
    * `GET /futures/data/delivery-price`: 查询季度合约历史交割价格
  * 调整下列接口限频为 1000/5min/IP:
    * `GET /futures/data/openInterestHist`
    * `GET /futures/data/topLongShortAccountRatio`
    * `GET /futures/data/topLongShortPositionRatio`
    * `GET /futures/data/globalLongShortAccountRatio`
    * `GET /futures/data/takerlongshortRatio`



* * *

## 2023-10-19

欧式期权

币安期权在进行 Websocket 服务升级，升级影响以下逻辑：

  * 升级前：

    * 服务端每 5 分钟会发送 ping 帧，客户端应当在 15 分钟内回复 pong 帧，否则服务端会主动断开链接。允许客户端发送不成对的 pong 帧(即客户端可以以高于 15 分钟每次的频率发送 pong 帧保持链接)
    * 无信息流订阅连接 Websocket 服务：
    * 升级前， 用户可以用以下方式连接:
      * `wss://nbstream.binance.com/eoptions/ws`
      * `wss://nbstream.binance.com/eoptions/stream`
      * `wss://nbstream.binance.com/eoptions/ws/`
      * `wss://nbstream.binance.com/eoptions/stream/`
  * 升级后

    * 服务端每 3 分钟会发送 ping 帧，客户端应当在 10 分钟内回复 pong 帧，否则服务端会主动断开链接。允许客户端发送不成对的 pong 帧(即客户端可以以高于 10 分钟每次的频率发送 pong 帧保持链接)
    * 无信息流订阅连接 Websocket 服务：
    * 升级后，用户可以用以下方式连接:
      * `wss://nbstream.binance.com/eoptions/ws`
      * `wss://nbstream.binance.com/eoptions/stream`
      * `/` 在 url 结尾不再支持
    * 带信息流订阅连接 Websocket 服务:
      * 不支持如下类型的 stream:`wss://nbstream.binance.com/eoptions/illegal_parameter/stream?steams=<streamName>`或`wss://nbstream.binance.com/eoptions/illegal_parameter/ws/<streamName>`，请移除 `/ws` 和 `/stream`前的`illegal_parameter/`



* * *

## 2023-10-19

U本位合约

REST

  * 新增行情接口：
    * `GET /futures/data/delivery-price`: 查询季度合约历史交割价格
  * 调整下列接口限频为 1000/5min/IP:
    * `GET /futures/data/openInterestHist`
    * `GET /futures/data/topLongShortAccountRatio`
    * `GET /futures/data/topLongShortPositionRatio`
    * `GET /futures/data/globalLongShortAccountRatio`
    * `GET /futures/data/takerlongshortRatio`
  * 调整下列接口限频为 500/5min/IP:
    * `GET /fapi/v1/fundingRate`
    * `GET /fapi/v1/fundingInfo`



* * *

## 2023-10-16

币本位合约

REST

  * 新增行情接口：
    * `GET /dapi/v1/constituents`: 查询指数成分



* * *

## 2023-10-16

U本位合约

REST

  * 新增行情接口：
    * `GET /fapi/v1/constituents`: 查询指数成分



* * *

## 2023-10-11

U本位合约

REST

  * 账户接口 IP 权重调整：
    * `GET /fapi/v1/income/asyn`: 5->1000
    * `GET /fapi/v1/order/asyn`: 5->1000
    * `GET /fapi/v1/trade/asyn`: 5->1000
    * `GET /fapi/v1/income/asyn/id`: 5->10
    * `GET /fapi/v1/order/asyn/id`: 5->10
    * `GET /fapi/v1/trade/asyn/id`: 5->10



* * *

## 2023-09-25

币本位合约

REST

  * 新增行情接口：
    * `GET /dapi/v1/fundingInfo`: 查询有调整的资金费率信息



* * *

## 2023-09-25

U本位合约

REST

  * 新增行情接口：
    * `GET /fapi/v1/fundingInfo`: 查询有调整的资金费率信息



* * *

## 2023-09-20

币本位合约

REST

  * `GET /dapi/v1/ticker/bookTicker`更新:

    * 增加返回字段`lastUpdateId`
  * `GET /dapi/v1/account`更新:

    * 在`assets`中增加返回字段`updateTime`



* * *

## 2023-09-20

U本位合约

REST

  * `GET /fapi/v1/ticker/bookTicker`更新:
    * 增加返回字段`lastUpdateId`



* * *

## 2023-09-19

U本位合约
    
    
    Code
    
    {
        "code": -1008,
        "msg": "Server is currently overloaded with other requests. Please try again in a few minutes."
    }

  * 新增 HTTP`503`可能的错误响应及错误码，下列接口在请求高峰期可能出现此响应:
    * `POST /fapi/v1/order`
    * `PUT /fapi/v1/order`
    * `DELETE /fapi/v1/order`
    * `POST /fapi/v1/batchOrder`
    * `PUT /fapi/v1/batchOrder`
    * `DELETE /fapi/v1/batchOrder`
    * `POST /fapi/v1/order/test`
    * `DELETE /fapi/v1/allOpenOrders`
  * 此响应表示本次 API 请求失败。这种情况下您如果需要的话可以选择立即重试。



* * *

## 2023-09-07

币本位合约

REST

  * 新增接口`GET /dapi/v1/income/asyn` 获取合约资金流水下载 id
  * 新增接口`GET /dapi/v1/income/asyn/id` 通过下载 id 获取合约资金流水下载链接



* * *

## 2023-09-05

U本位合约

  * 根据此[公告](https://www.binance.com/zh-CN/support/announcement/%E5%B8%81%E5%AE%89%E5%90%88%E7%BA%A6%E6%8E%A8%E5%87%BAapi-u%E6%9C%AC%E4%BD%8D%E5%90%88%E7%BA%A6%E8%87%AA%E6%88%90%E4%BA%A4%E9%A2%84%E9%98%B2-stp-%E5%8A%9F%E8%83%BD-32916877372243d69154c345200e34b8)，自成交保护（Self-Trade Prevention）已于 **2023-09-05** 发布。
  * 价格匹配/有效方式 GTD/盈亏平衡价等功能（详情见 2023-08-29 更新日志）已于**2023-09-05** 发布。



* * *

## 2023-09-04

统一账户

  * 接口字段更新:

    * `GET /papi/v1/um/positionRisk`: 新增响应字段`liquidationPrice`
    * `GET /papi/v1/cm/positionRisk`: 新增响应字段 `liquidationPrice`
    * `GET /papi/v1/um/leverageBracket`: 新增响应字段 `notionalCoef`
    * `GET /papi/v1/cm/leverageBracket`: 新增响应字段 `notionalCoef`
  * Websocket 账户信息推送字段更新:

    * `outboundAccountPosition`事件新增字段更新 Id`U`
    * `balanceUpdate`事件新增字段更新 Id`U`



* * *

## 2023-09-04

统一账户

**2023-09-07 发布**

  * papi 的 order ratelimit 从 2400 orders/min 降低为 1200 orders/min，受影响的接口：
    * POST `/papi/v1/um/order`
    * POST `/papi/v1/cm/order`
    * POST `/papi/v1/margin/order`
    * POST `/papi/v1/margin/order/oco`
    * POST `/papi/v1/um/conditional/order`
    * POST `/papi/v1/cm/conditional/order`



* * *

## 2023-08-31

币本位合约

币安合约在进行 Websocket 服务升级，升级影响以下逻辑：

  * 升级前：

    * 服务端每 5 分钟会发送 ping 帧，客户端应当在 15 分钟内回复 pong 帧，否则服务端会主动断开链接。允许客户端发送不成对的 pong 帧(即客户端可以以高于 15 分钟每次的频率发送 pong 帧保持链接)
  * 升级后

    * 服务端每 3 分钟会发送 ping 帧，客户端应当在 10 分钟内回复 pong 帧，否则服务端会主动断开链接。允许客户端发送不成对的 pong 帧(即客户端可以以高于 10 分钟每次的频率发送 pong 帧保持链接)



* * *

## 2023-08-31

U本位合约

币安合约在进行 Websocket 服务升级，升级影响以下逻辑：

  * 升级前：

    * 服务端每 5 分钟会发送 ping 帧，客户端应当在 15 分钟内回复 pong 帧，否则服务端会主动断开链接。允许客户端发送不成对的 pong 帧(即客户端可以以高于 15 分钟每次的频率发送 pong 帧保持链接)
  * 升级后

    * 服务端每 3 分钟会发送 ping 帧，客户端应当在 10 分钟内回复 pong 帧，否则服务端会主动断开链接。允许客户端发送不成对的 pong 帧(即客户端可以以高于 10 分钟每次的频率发送 pong 帧保持链接)



* * *

## 2023-08-29

欧式期权

REST

  * `GET /eapi/v1/account`: 新增字段`riskLevel`显示账户风险等级
  * `GET /eapi/v1/marginAccount`: 新增字段`riskLevel`显示账户风险等级



Websocket 用户信息流

  * 新增更新时间`RISK_LEVEL_CHANGE`以显示账户风险等级变化



* * *

## 2023-08-29

U本位合约

  * **自成交保护(发布时间待定)**

  * U 本位合约系统中将支持 Self-Trade Prevention（STP）自成交保护。此功能将阻止订单与来自同一账户或者同一 `tradeGroupId` 账户的订单交易。详情请参考 [FAQ](https://www.binance.com/cn/support/faq/0941126f6413485b9a3df964a9aa2306)

  * 合约所有交易对支持通过下单时设置`selfTradePreventionMode`为下面之一的 STP 模式：

    * NONE: 不设置自成交保护
    * EXPIRE_TAKER: 自成交过期 taker 订单
    * EXPIRE_MAKER: 自成交过期 maker 订单
    * EXPIRE_BOTH: 自成交过期 taker 和 maker 订单
  * REST 更新:

    * 新的订单状态：`EXPIRED_IN_MATCH` \- 订单由于 STP 触发而过期
      * `GET /fapi/v2/account`中响应新增字段`tradeGroupId`显示用户的 tradeGroupId
    * 以下接口新增可选参数`selfTradePreventionMode`以设置该订单的自成交保护模式：
      * `POST /fapi/v1/order`
      * `POST /fapi/v1/batchOrders`
    * 以下接口新增响应字段`selfTradePreventionMode`以显示订单的自成交保护模式：
      * `POST /fapi/v1/order`
      * `POST /fapi/v1/batchOrders`
      * `POST /fapi/v1/order`
      * `POST /fapi/v1/order`
      * `GET /fapi/v1/order`
      * `GET /fapi/v1/openOrders`
      * `GET /fapi/v1/allOrders`
      * `PUT /fapi/v1/order`
      * `PUT /fapi/v1/batchOrders`
      * `DELETE /fapi/v1/order`
      * `DELETE /fapi/v1/batchOrders`
  * WEBSOCKET 账户信息推送更新:

    * `ORDER_TRADE_UPDATE`中新增字段`V`显示用户订单的自成交保护模式



* * *

## 2023-08-25

币本位合约

  * 币安合约在进行 Websocket 服务升级，升级影响以下连接方式：
    * 无信息流订阅连接 Websocket 服务：
      * 升级前， 用户可以用以下方式连接:
        * `wss://dstream.binance.com/ws`
        * `wss://dstream.binance.com/stream`
        * `wss://dstream.binance.com/ws/`
        * `wss://dstream.binance.com/stream/`
      * 升级后，用户可以用以下方式连接:
        * `wss://dstream.binance.com/ws`
        * `wss://dstream.binance.com/stream`
        * `/` 在 url 结尾不再支持
    * 带信息流订阅连接 Websocket 服务:
      * 不支持如下类型的 stream:`wss://fstream.binance.com/illegal_parameter/stream?steams=<streamName>`或`wss://fstream.binance.com/illegal_parameter/ws/<streamName>`，请移除 `/ws` 和 `/stream`前的`illegal_parameter/`



* * *

## 2023-08-19

U本位合约

  * 币安合约在进行 Websocket 服务升级，升级影响以下连接方式：
    * 无信息流订阅连接 Websocket 服务：
      * 升级前， 用户可以用以下方式连接:
        * `wss://fstream.binance.com/ws`
        * `wss://fstream.binance.com/stream`
        * `wss://fstream.binance.com/ws/`
        * `wss://fstream.binance.com/stream/`
      * 升级后，用户可以用以下方式连接:
        * `wss://fstream.binance.com/ws`
        * `wss://fstream.binance.com/stream`
        * `/` 在 url 结尾不再支持
    * 带信息流订阅连接 Websocket 服务:
      * 不支持如下类型的 stream:`wss://fstream.binance.com/illegal_parameter/stream?steams=<streamName>`或`wss://fstream.binance.com/illegal_parameter/ws/<streamName>`，请移除 `/ws` 和 `/stream`前的`illegal_parameter/`



* * *

## 2023-08-18

统一账户

  * 新增查询接口：
    * `GET /papi/v1/margin/order`: 杠杆下单
    * `GET /papi/v1/margin/openOrders`: 查询杠杆账户挂单记录
    * `GET /papi/v1/margin/allOrders`: 查询杠杆账户的所有订单
    * `GET /papi/v1/margin/orderList`: 查询杠杆账户 OCO
    * `GET /papi/v1/margin/allOrderList`: 查询特定杠杆账户所有 OCO
    * `GET /papi/v1/margin/openOrderList`: 查询杠杆账户 OCO 挂单
    * `GET /papi/v1/margin/myTrades`: 查询杠杆账户交易历史



* * *

## 2023-08-14

币本位合约

  * 更新账户和交易接口：
    * `GET /dapi/v1/income`：增加字段`page`用以分页



* * *

## 2023-08-14

U本位合约

  * 更新账户和交易接口：
    * `GET /fapi/v1/income`：增加字段`page`用以分页



* * *

## 2023-07-28

统一账户

  * 新增账户接口：
    * `POST /papi/v1/asset-collection`: 特定资产资金归集



* * *

## 2023-07-21

欧式期权

REST

  * 新增接口`GET /eapi/v1/income/asyn` 获取期权流水历史下载 id
  * 新增接口`GET /eapi/v1/income/asyn/id` 通过下载 id 获取期权流水历史下载链接



* * *

## 2023-07-20

统一账户

  * 新增账户接口：
    * `GET /papi/v1/um/adlQuantile`: UM 持仓 ADL 队列估算
    * `GET /papi/v1/cm/adlQuantile`: CM 持仓 ADL 队列估算



* * *

## 2023-07-19

币本位合约

REST

  * `GET /dapi/v2/leverageBracket` 新增字段`notionalCoef`显示用户相对默认 bracket 的调整倍数



* * *

## 2023-07-18

统一账户

  * 新增统一账户账户接口：
    * `POST /papi/v1/repay-futures-switch`: 更改自动清还合约负余额模式
    * `GET /papi/v1/repay-futures-switch`: 查询自动清还合约负余额模式
    * `POST /papi/v1/repay-futures-negative-balance`: 清还合约负余额



* * *

## 2023-07-18

U本位合约

REST

  * `GET /fapi/v1/leverageBracket` 新增字段`notionalCoef`显示用户相对默认 bracket 的调整倍数



* * *

## 2023-07-13

欧式期权

Websocket Market Streams

  * 下面更新将在 2023-7-14 生效：
    * 在数据流`<symbol>@ticker`, `<underlyingAsset>@ticker@<expirationDate>`新增参数`T`显示交易时间
    * 在数据流`<symbol>@depth<levels>`新增参数`E`显示事件时间



* * *

## 2023-07-13

统一账户

  * 新增用户数据推送`riskLevelChange`（2023-7-14 生效）



* * *

## 2023-07-12

币本位合约

REST

  * 以下接口返回新增`breakEvenPrice`字段代表仓位盈亏平衡价：
    * GET /dapi/v1/account (HMAC SHA256)
    * GET /dapi/v1/positionRisk (HMAC SHA256)



WEBSOCKET

  * Position 更新推送 payload `ACCOUNT_UPDATE`中"P"新增`bep`字段代表仓位盈亏平衡价



* * *

## 2023-07-11

统一账户

REST

  * 增加新接口`POST /papi/v1/ping` 测试服务器连通性



* * *

## 2023-07-04

U本位合约

REST

  * 以下接口将改为仅保留最近 3 个月数据：
    * `GET /fapi/v1/order`(2023-07-27 生效)
    * `GET /fapi/v1/allOrders`(2023-07-27 生效)
    * `GET /fapi/v1/userTrades`(具体时间待定)
  * 请自行维护和保留 3 个月之前的历史数据或使用以下新接口获得历史订单/交易信息：
    * 新增接口`GET /fapi/v1/order/asyn` 获取合约订单历史下载 id
    * 新增接口`GET /fapi/v1/order/asyn/id` 通过下载 id 获取合约订单历史下载链接
    * 新增接口`GET /fapi/v1/trade/asyn` 获取合约交易历史下载 id
    * 新增接口`GET /fapi/v1/trade/asyn/id` 通过下载 id 获取合约交易历史下载链接



* * *

## 2023-06-28

U本位合约

**注意:**

REST

  * 以下接口将于 2023-07-15 后不再支持：
    * `GET /fapi/v1/account`
    * `GET /fapi/v1/balance`
    * `GET /fapi/v1/positionRisk`
  * 请及时替换为对应的 v2 接口:
    * `GET /fapi/v2/account`
    * `GET /fapi/v2/balance`
    * `GET /fapi/v2/positionRisk`



* * *

## 2023-06-22

币本位合约

**注意:**

WEBSOCKET

  * 订阅格式 **/ws? <streamName>** 不被支持， 如`wss://dstream.binance.com/ws?btcusd@depth` 会被认为是非法请求.
  * 发送带有不合法 JSON 格式的 websocket 消息将导致连接断开，返回错误`{"error":{"code":3,"msg":"Invalid JSON: expected value at line 1 column 1"}}`



* * *

## 2023-06-22

U本位合约

**注意:**

WEBSOCKET

  * 订阅格式 **/ws? <streamName>** 不被支持， 如`wss://fstream.binance.com/ws?btcusdt@depth` 会被认为是非法请求.
  * 发送带有不合法 JSON 格式的 websocket 消息将导致连接断开，返回错误`{"error":{"code":3,"msg":"Invalid JSON: expected value at line 1 column 1"}}`



* * *

## 2023-06-19

统一账户

REST

  * 在 `POST /papi/v1/um/conditional/order`和`POST/papi/v1/cm/conditional/order`新增参数`CONTRACT_PRICE`，`priceProtect`



* * *

## 2023-06-16

U本位合约

**注意：**

  * 建议使用标准的 HTTP 请求格式，fapi 中将不支持非标准请求格式。以下是一些正确的代码实践示例：
    * 不再支持使用 '\x22' 进行转义（"），请改用标准的 '%22'，需要对中括号[]和中括号内部的双引号进行 URL encode DELETE /fapi/v1/batchOrders?origClientOrderIdList= 不支持： [\x229151944646313025900\x22] 建议： ["9151944646313025900"] --经过 URL 编码后-- DELETE /fapi/v1/batchOrders?origClientOrderIdList=%5B%229151944646313025900%22%5D

    * 不支持非标准嵌套 JSON 格式
          
          Code
          
          POST /fapi/v1/batchOrders?batchOrders=

不支持：

["{"type":"LIMIT","timeInForce":"GTC"}"]

建议：

[{"type":"LIMIT","timeInForce":"GTC"}]

\--经过 URL 编码后--

POST /fapi/v1/batchOrders?batchOrders=%5B%7B%22type%22%3A%22LIMIT%22%2C%22timeInForce%22%3A%22GTC%22%7D%5D

    * 不支持使用不正确的数据类型
          
          Code
          
          DELETE /fapi/v1/batchOrders?orderIdList=

由于 'orderIdList' 参数的数据类型为 LIST<LONG> 不支持：

["159856286502","159856313662"]

建议：

[159856286502,159856313662]

\--经过 URL 编码后--

DELETE /fapi/v1/batchOrders?orderIdList=%5B159856286502%2C159856313662%5D

    * 不支持从请求参数中的无效空白字符
          
          Code
          
          不支持：

POST symbol=BTCUSDT& price= 40000.0 & signature=2d24a314

建议：

POST symbol=BTCUSDT&&price=40000.0&signature=2d24a314

    * 不支持请求参数传空值
          
          Code
          
          不支持：

GET symbol=BTCUSDT&orderId=&signature=2d24a314

建议：

GET symbol=BTCUSDT&signature=2d24a314




* * *

## 2023-06-14

币本位合约

WEBSOCKET

  * 在`<symbol>@markPrice` and `<pair>@markPrice`中新增指数`i`字段



* * *

## 2023-06-14

U本位合约

**注意:**

  * 新增市场信息流 `!assetIndex@arr`OR`<assetSymbol>@assetIndex`推送多资产模式资产指数价格



* * *

## 2023-06-01

统一账户

REST

  * 下列接口将于 2023-06-02 生效：
    * New endpoints `GET /papi/v1/um/income` and `GET /papi/v1/cm/income` to query portfolio margin UM/CM income history
    * New endpoints `GET /papi/v1/um/account` and `GET /papi/v1/cm/account` to query portfolio margin UM/CM account history



* * *

## 2023-05-31

U本位合约

WEBSOCKET

  * 新增账户信息流:
    * 新增推送 `CONDITIONAL_ORDER_TRIGGER_REJECT` 以显示被触发的止盈止损单被拒绝原因



* * *

## 2023-05-30

欧式期权

General Information on Endpoints

  * `GET`方法的接口, 参数必须在`query string`中发送且 HTTP 头中不设置 content type.



* * *

## 2023-05-05

U本位合约

REST

  * 新增 `PUT /fapi/v1/order` 和 `PUT /fapi/v1/batchOrders` 接口以支持限价订单修改功能
  * 新增 `GET /fapi/v1/orderAmendment` 接口以查询订单修改历史



WEBSOCKET

  * 订单/交易 更新推送 `ORDER_TRADE_UPDATE` 中本次事件的具体执行类型 `x` 新增 "AMENDMENT" 代表订单修改



* * *

## 2023-05-04

统一账户

  * 新增统一账户文档



* * *

## 2023-04-17

币本位合约

**发布日期待确定**

`recvWindow` 校验也将在订单到达撮合后进行。`recvWindow` 校验在下单相关接口更加精确。
    
    
    Code
    
    {
        "code": -4188,
        "msg": "Timestamp for this request is outside of the ME recvWindow"
    }

**发布前 recvWindow 逻辑：**

  * 下单类请求在 `recvWindow` \+ `timestamp` => REST API 服务器`timestamp`时有效



**发布后 recvWindow 逻辑：**

  * 新增校验：下单类请求在 `recvWindow` \+ `timestamp` => 撮合`timestamp`时有效

  * 受影响接口:

    * POST /dapi/v1/order (HMAC SHA256)
    * PUT /dapi/v1/order (HMAC SHA256)
    * POST /dapi/v1/batchOrders (HMAC SHA256)
    * PUT /dapi/v1/batchOrders (HMAC SHA256)



* * *

## 2023-04-17

U本位合约

**发布日期 2023-04-18**

`recvWindow` 校验也将在订单到达撮合后进行。`recvWindow` 校验在下单相关接口更加精确。
    
    
    Code
    
    {
        "code": -5028,
        "msg": "Timestamp for this request is outside of the ME recvWindow"
    }

**发布前 recvWindow 逻辑：**

  * 下单类请求在 `recvWindow` \+ `timestamp` => REST API 服务器`timestamp`时有效



**发布后 recvWindow 逻辑：**

  * 新增校验：下单类请求在 `recvWindow` \+ `timestamp` => 撮合`timestamp`时有效

  * 受影响接口:

    * POST /fapi/v1/order
    * PUT /fapi/v1/order
    * POST /fapi/v1/batchOrders
    * PUT /fapi/v1/batchOrders



* * *

## 2023-03-28

U本位合约

**发布前推荐返佣逻辑：**

  * 每笔交易实时返佣，用户会在 USER-DATA-STREAM 的 `ACCOUNT_UPDATE` 事件中收到如下推送：


    
    
    Code
    
    {
      "e": "ACCOUNT_UPDATE",
      "T": 1679974782150,
      "E": 1679974782155,
      "a": {
        "B": [
       {
           "a": "USDT",
           "wb": "685.31478079",
           "cw": "677.17212454",
           "bc": "0.00258637"
          }
     ],
        "P": [],
        "m": "ADMIN_DEPOSIT"
      }
    }

**发布后推荐返佣逻辑：**

  * 每 20 分钟聚合一次计算返佣上账，用户会在 USER-DATA-STREAM 的 `ACCOUNT_UPDATE` 事件中收到相同推送，余额变化为聚合后的返佣加总。



* * *

## 2023-03-08

U本位合约

**发布日期 2023-03-22**

**发布前订单逻辑：**

  * 下单时传参 `timeInForce`为 `FOK` 或 `GTX`(Post-only)，用户会收到订单返回 `status` = “NEW” 并收到推送 `order_trade_update`消息`x` = “NEW”， `X` = “NEW”。 如果订单不满足执行条件，用户会收到另一条 `order_trade_update` 消息，其`x` = “EXPIRED”, `X` = “EXPIRED”。 该订单可以在`GET /fapi/v1/order`或`GET /fapi/v1/allOrders`查到。


    
    
    Code
    
    {
        "code": -5021,
        "msg": "Due to the order could not be filled immediately, the FOK order has been rejected. The order will not be recorded in the order history"
    }

**发布后订单逻辑：**

  * 下单时传参 `timeInForce`为 `FOK` 或 `GTX`(Post-only)，如果该订单不满足执行条件，订单会被直接拒绝并收到报错信息，`order_trade_update`不会推送此订单的消息。该订单不能在`GET /fapi/v1/order`或`GET /fapi/v1/allOrders`中查到。


    
    
    Code
    
    {
        "code": -5022,
        "msg": "Due to the order could not be executed as maker, the Post Only order will be rejected. The order will not be recorded in the order history"
    }

  * 受影响接口:
    * POST /fapi/v1/order
    * POST /fapi/v1/batchOrders
    * GET /fapi/v1/order
    * GET /fapi/v1/allOrders



* * *

## 2023-02-02

欧式期权

REST

  * 接口`POST /eapi/v1/transfer`不再使用.



* * *

## 2023-01-11

欧式期权

REST

  * 增加`GET /eapi/v1/order`以查询单个订单状态



* * *

## 2023-01-04

U本位合约

WEBSOCKET

  * Order Update: 订单状态中删除`NEW_INSURANCE`风险保障基金(强平)与`NEW_ADL`自动减仓序列(强平)



* * *

## 2022-12-16

币本位合约

WEBSOCKET

  * 新增订阅信息流 `!contractInfo` 获取交易对信息更新



* * *

## 2022-12-16

U本位合约

WEBSOCKET

  * 新增订阅信息流 `!contractInfo` 获取交易对信息更新



* * *

## 2022-12-13

欧式期权

WEBSOCKET

  * 在`<symbol>@depth1000`中新增字段`u`和`pu`以获取增量 orderbook 更新



* * *

## 2022-12-09

欧式期权

REST

  * 在`GET /eapi/v1/depth`中新增更新 id 字段`u`
  * 在`GET /eapi/v1/exerciseHistory`中增加入参`underlying`



* * *

## 2022-11-29

币本位合约

WEB SOCKET USER DATA STREAM

  * USER-DATA-STREAM 中新增事件`STRATEGY_UPDATE`: 在策略交易创建、取消、失效等等时候更新。
  * USER-DATA-STREAM 中新增事件`GRID_UPDATE`: 在网格子订单有部份或是完全成交时更新。



* * *

## 2022-11-29

U本位合约

WEB SOCKET USER DATA STREAM

  * USER-DATA-STREAM 中新增事件`STRATEGY_UPDATE`: 在策略交易创建、取消、失效等等时候更新。
  * USER-DATA-STREAM 中新增事件`GRID_UPDATE`: 在网格子订单有部份或是完全成交时更新。



* * *

## 2022-11-18

欧式期权

REST

  * 新增接口`GET /eapi/v1/openInterest`用来获取特定标的资产特定到期日的期权持仓量



WEBSOCKET

  * 增加数据流`<underlyingAsset>@openInterest@<expirationDate>`用来获取特定标的资产期权持仓量



* * *

## 2022-11-16

欧式期权

WEBSOCKET

  * 增加交易数据流`<underlyingAsset>@trade`用来获取特定标的资产的所有期权交易
  * 调整数据流`option_pair`输出格式



* * *

## 2022-11-03

欧式期权

REST

  * 将于 2022-11-07 日新增做市商倒计时自动取消接口:
    * `POST /eapi/v1/countdownCancelAll`：设置倒计时取消所有订单配置
    * `GET /eapi/v1/countdownCancelAll`：获得倒计时自动取消所有订单配置
    * `POST /eapi/v1/countdownCancelAllHeartBeat`：重置倒计时取消所有订单心跳



* * *

## 2022-10-13

币本位合约

**注意:** 此变动会在 2022-10-17 生效

REST RATE LIMIT WEIGHT

接口 `GET /dapi/v1/ticker/bookTicker`

**权重更新:**

  * 单交易对`2`
  * 无交易对`5`



* * *

## 2022-10-13

U本位合约

**注意:** 此变动会在 2022-10-17 生效

REST RATE LIMIT WEIGHT

接口 `GET /fapi/v1/ticker/bookTicker`

**权重更新:**

  * 单交易对`2`
  * 无交易对`5`



* * *

## 2022-09-22

币本位合约

  * 新增统一账户接口：
    * `GET /dapi/v1/pmAccountInfo`：查询统一账户当前账户信息。



* * *

## 2022-09-22

U本位合约

  * 更新账户和交易接口：
    * `GET /fapi/v1/income`：支持更多收益类型
  * 新增统一账户接口：
    * `GET /fapi/v1/pmAccountInfo`：查询统一账户当前账户信息。



* * *

## 2022-09-20

欧式期权

WEBSOCKET

  * 新增数据流 `<underlyingAsset>@markPrice` 和 `<underlyingAsset>@ticker@<expirationDate>`
  * 数据流 `<!miniTicker@arr>` 将于 2022/10/30 弃用



* * *

## 2022-09-14

欧式期权

REST

  * 修改`GET /eapi/v1/exchangeInfo`中`strikePrice`,`makerFeeRate`,`takerFeeRate`,`minQty`,`maxQty`,`initialMargin`,`maintenanceMargin`,`minInitialMargin`,`minMaintenanceMargin`为 string
  * `GET /eapi/v1/historyOrders`中仅保留最近 5 天订单



* * *

## 2022-09-05

欧式期权

REST

  * 修改`DELETE /eapi/v1/allOpenOrdersByUnderlying`中 response 的格式



* * *

## 2022-07-27

币本位合约

REST RATE LIMIT WEIGHT

  * 接口 `GET /dapi/v1/trades` 的请求权重更新为 5



* * *

## 2022-07-27

U本位合约

REST RATE LIMIT WEIGHT

  * 接口 `GET /fapi/v1/trades` 的请求权重更新为 5



* * *

## 2022-06-28

币本位合约

REST

  * 新增接口 `GET /dapi/v1/pmExchangeInfo` 获取统一账户交易规则



* * *

## 2022-06-28

U本位合约

REST

  * 新增接口 `GET /fapi/v1/pmExchangeInfo` 获取统一账户交易规则



* * *

## 2022-04-28

币本位合约

REST

  * 新增 `PUT /dapi/v1/order` 和 `PUT /dapi/v1/batchOrders` 接口以支持限价订单修改功能
  * 新增 `GET /dapi/v1/orderAmendment` 接口以查询订单修改历史



WEBSOCKET

  * 订单/交易 更新推送 `ORDER_TRADE_UPDATE` 中本次事件的具体执行类型 `x` 新增 "AMENDMENT" 代表订单修改



* * *

## 2022-04-14

币本位合约

WEB SOCKET USER DATA STREAM

  * USER-DATA-STREAM 中新增事件`ACCOUNT_CONFIG_UPDATE`以获取交易对杠杆倍数变动更新



* * *

## 2022-03-01

U本位合约

REST

  * 新增接口`GET /fapi/v1/income/asyn` 获取合约资金流水下载 id
  * 新增接口`GET /fapi/v1/income/asyn/id` 通过下载 id 获取合约资金流水下载链接



* * *

## 2022-02-18

币本位合约

REST

  * 查询账户成交历史接口`GET /dapi/v1/userTrades`接口参数`limit`的最大值调整至 1000



* * *

## 2022-02-10

U本位合约

REST

  * 更新`GET /fapi/v2/account`接口：
    * 若用户开启多资产模式,`totalInitialMargin``totalMaintMargin``totalWalletBalance``totalUnrealizedProfit``totalMarginBalance``totalPositionInitialMargin``totalOpenOrderInitialMargin``totalCrossWalletBalance``totalCrossUnPnl``availableBalance``maxWithdrawAmount` 计入各种资产并转化为其 USD 价值显示
    * 若用户使用单资产模式, 仅 USDT 资产会被计入计算（和改动前一致）



* * *

## 2021-12-30

U本位合约

WEBSOCKET

  * 新增 WEBSOCKET 连接方式：
    * Base Url：`wss://fstream-auth.binance.com`
    * 订阅单一 stream 格式为 `/ws/<streamName>?listenKey=<validateListenKey>`
    * 组合 streams 的 URL 格式为 `/stream?streams=<streamName1>/<streamName2>/<streamName3>&listenKey=<validateListenKey>`
    * `<validateListenKey>`在建立连接时，必须为一个有效的 listenKey
  * 详细说明见 [Websocket 行情推送](/zh-CN/docs/products/derivatives-trading-usds-futures/websocket-market-streams/Connect)和[Websocket 账户信息推送](/zh-CN/docs/products/derivatives-trading-usds-futures/user-data-streams)



* * *

## 2021-11-02

U本位合约

REST

  * 新增接口`GET /fapi/v1/assetIndex`以获取多资产模式保证金资产汇率指数



* * *

## 2021-08-18

币本位合约

REST

  * `GET /dapi/v1/account` 响应内容加入 `positionAmt` 以表示持仓数量



* * *

## 2021-08-17

币本位合约

REST

  * 新增 `PUT /dapi/v1/order` 和 `PUT /dapi/v1/batchOrders` 接口以支持限价订单修改功能
  * 新增 `GET /dapi/v1/orderAmendment` 接口以查询订单修改历史



WEBSOCKET

  * 订单/交易 更新推送 `ORDER_TRADE_UPDATE` 中本次事件的具体执行类型 `x` 新增 "AMENDMENT" 代表订单修改



* * *

## 2021-07-23

币本位合约

REST

  * `GET /dapi/v1/account` 和 `GET /dapi/v1/positionRisk`响应内容加入`updateTime`以表示资产，仓位的最新更新时间



* * *

## 2021-07-06

币本位合约

REST

  * `GET /dapi/v1/exchangeInfo` 响应内容增加以下字段:
    * "liquidationFee" 表示强平费率
    * "marketTakeBound" 表示市价吃单(相对于标记价格)允许可造成的最大价格偏离比例



* * *

## 2021-07-06

U本位合约

REST

  * `GET /fapi/v2/account` 和 `GET /fapi/v2/positionRisk`响应内容加入`updateTime`以表示资产，仓位的最新更新时间
  * `GET /fapi/v1/exchangeInfo` 响应内容增加以下字段:
    * "liquidationFee" 表示强平费率
    * "marketTakeBound" 表示市价吃单(相对于标记价格)允许可造成的最大价格偏离比例



* * *

## 2021-06-15

U本位合约

WEBSOCKET

  * 综合指数交易对信息流 `<symbol>@compositeIndex` 新增返回字段 "q" 表示报价资产， "i" 表示指数价格



REST

  * 更新以下接口:
    * `GET /fapi/v1/indexInfo` 响应加入`component`成分资产，`quoteAsset`报价资产字段



* * *

## 2021-05-06

币本位合约

WEBSOCKET

  * "ACCOUNT_UPDATE" 事件新增返回字段 "bc" 表示账户余额改变量。



* * *

## 2021-05-06

U本位合约

WEBSOCKET

  * 更新以下接口：
    * 原有杠杆倍数更新推送事件`ACCOUNT_CONFIG_UPDATE`扩展为账户配置更新推送事件，包含杠杆倍数与联合保证金状态更新推送
    * Balance 和 Position 更新推送`ACCOUNT_UPDATE`的事件`m`枚举类型新增`AUTO_EXCHANGE`代表联合保证金自动兑换事件



REST

  * 新增以下接口:

    * `POST /fapi/v1/multiAssetsMargin` 以更改联合保证金模式
    * `GET /fapi/v1/multiAssetsMargin` 以查询联合保证金模式
  * 更新以下接口:

    * `GET /fapi/v1/exchangeInfo` 响应加入`assets`资产信息
    * `GET /fapi/v2/balance`与`GET /fapi/v2/account` 响应加入`marginAvailable`字段代表是否可用作联合保证金



* * *

## 2021-04-27

币本位合约

WEBSOCKET

  * 以下市场强平订单推送事件由实时推送调整为快照推送，即每秒最多推送一条强平订单数据:
    * `<symbol>@forceOrder`
    * `!forceOrder@arr`



REST

  * 获取市场强平订单接口 `GET /dapi/v1/allForceOrders`停止维护，不再接受请求



* * *

## 2021-04-27

U本位合约

WEBSOCKET

  * 以下市场强平订单推送事件由实时推送调整为快照推送，即每秒最多推送一条强平订单数据:
    * `<symbol>@forceOrder`
    * `!forceOrder@arr`



REST

  * 获取市场强平订单接口 `GET /fapi/v1/allForceOrders`停止维护，不再接受请求



* * *

## 2021-04-22

U本位合约

WEBSOCKET

  * "ACCOUNT_UPDATE" 事件新增返回字段 "bc" 表示账户余额改变量。



* * *

## 2021-03-10

币本位合约

REST

  * 接口 `GET /dapi/v1/allForceOrders` 的查询时间范围最大为 7 天（默认查询最近 7 天内的数据）



* * *

## 2021-03-02

U本位合约

  * 新增接口 `GET /fapi/v1/indexPriceKlines` 以获取价格指数 K 线数据。

  * 新增接口 `GET /fapi/v1/markPriceKlines` 以获取标记价格 K 线数据。




* * *

## 2021-02-24

U本位合约

REST RATE LIMIT WEIGHT

  * 接口 `GET /fapi/v2/balance` 的请求权重更新为 5
  * 接口 `GET /fapi/v2/positionRisk` 的请求权重更新为 5



* * *

## 2021-02-22

U本位合约

REST RATE LIMIT WEIGHT

  * 接口 `GET /fapi/v1/income` 的请求权重更新为 30



REST

  * 接口`GET /fapi/v1/allOrders` 的查询时间范围最大为 7 天.
  * 接口`GET /fapi/v1/allForceOrders`的查询范围仅限于最近 7 天内的数据.



* * *

## 2021-01-26

币本位合约

REST RATE LIMIT WEIGHT

  * 以下接口的权重调整为 带 symbol 20, 不带 symbol 50
    * `GET /dapi/v1/allForceOrders`
    * `GET /dapi/v1/forceOrders`



* * *

## 2021-01-26

U本位合约

WEB SOCKET USER DATA STREAM

  * USER-DATA-STREAM 中新增事件`ACCOUNT_CONFIG_UPDATE`以获取交易对杠杆倍数变动更新



REST RATE LIMIT WEIGHT

  * 以下接口的权重调整为 带 symbol 20, 不带 symbol 50
    * `GET /fapi/v1/allForceOrders`
    * `GET /fapi/v1/forceOrders`



REST

  * 新增交易对过滤器 "MIN_NOTIONAL"，定义了交易对订单所允许的最小名义价值，并在 `fapi/v1/exchangeInfo` 的响应中返回



* * *

## 2021-01-21

币本位合约

合约订单用户自定义 id`newClientOrderId`更新正则规则为: `^[\.A-Z\:/a-z0-9_-]{1,36}$`

* * *

## 2021-01-21

U本位合约

合约订单用户自定义 id`newClientOrderId`更新正则规则为: `^[\.A-Z\:/a-z0-9_-]{1,36}$`

* * *

## 2021-01-04

U本位合约

REST

  * 以下接口的 IP 限制权重将采用基于参数 LIMIT 数值的新权重规则:

    * `GET /fapi/v1/klines`
    * `GET /fapi/v1/continuousKlines`
  * 以下接口的 IP 限制权重调整到 20:

    * `GET /fapi/v1/historicalTrades`
    * `GET /fapi/v1/allForceOrders`
    * `GET /fapi/v1/forceOrders`
    * `GET /fapi/v1/aggTrades`



* * *

## 2020-12-30

币本位合约

REST RATE LIMIT WEIGHT

  * 以下接口的 IP 限制权重将采用基于参数 LIMIT 数值的新权重规则:

    * `GET /dapi/v1/klines`
    * `GET /dapi/v1/continuousKlines`
    * `GET /dapi/v1/indexPriceKlines`
    * `GET /dapi/v1/markPriceKlines`
  * 以下接口的 IP 限制权重调整到 20:

    * `GET /dapi/v1/historicalTrades`
    * `GET /dapi/v1/allForceOrders`
    * `GET /dapi/v1/forceOrders`
    * `GET /dapi/v1/aggTrades`



* * *

## 2020-12-08

U本位合约

WEBSOCKET

  * 行情消息推送 `<symbol>@bookTicker` 和 `!bookTicker` 返回内容新增字段`e` 表示事件类型
  * 行情消息推送`<symbol>@markPrice`, `<symbol>@markPrice@1s`, `!markPrice@arr`, 和 `!markPrice@arr@1s` 返回内容新增字段`P` 表示估计结算价
  * 新增行情连续合约 K 线推送 `<pair>_<contractType>@continuousKline_<interval>`



REST API

  * 接口 `GET /fapi/v1/premiumIndex` 返回内容新增字段 "estimatedSettlePrice" 表示估计结算价。

  * 接口`GET /fapi/v1/exchangeInfo` 返回内容新增字段:

    * "pair" 标的交易对
    * "contractType" 合约类型
    * "deliveryDate" 交割日期
    * "onboardDate" 上线日期
  * 新增接口 `GET /fapi/v1/continuousKlines` 获取连续合约 K 线数据




ENUM

  * 合约类型:
    * PERPETUAL 永续合约
    * CURRENT_MONTH 当月交割合约
    * NEXT_MONTH 次月交割合约
    * CURRENT_QUARTER 当季交割合约
    * NEXT_QUARTER 次季交割合约



* * *

## 2020-11-27

币本位合约

  * 新增接口 `GET /dapi/v1/commissionRate` 以查询用户交易手续费率。



* * *

## 2020-11-27

U本位合约

  * 新增接口 `GET /fapi/v1/commissionRate` 以查询用户交易手续费率。



* * *

## 2020-11-13

U本位合约

WEB SOCKET STREAM

  * 为了给用户提供更安全稳定的服务，`<symbol>depth@0ms` and `<symbol>@depth<level>@0ms` 的更新频率调整为根据数据流量总量和其他客观情况动态调整



* * *

## 2020-11-10

U本位合约

  * 接口`GET /fapi/v1/exchangeInfo` 新增返回字段 "marginAsset" 表示保证金资产
  * 接口`GET /fapi/v2/account`新增返回字段 "positionAmt" 表示持仓数量



* * *

## 2020-11-09

U本位合约

WEB SOCKET USER DATA STREAM

USER-DATA-STREAM 中的事件`ACCOUNT_UPDATE`推送规则作出了以下更新和优化：

  * 当用户某项资产发生变化时：

    * 资产项目"B"中仅会推送本次发生变化的资产及其余额
    * 其他资产不会被推送，即便资产不为 0
    * 如果资产变化不涉及持仓变化，持仓项目"P"将仅返回空`[]`
  * 当合约某 symbol 的持仓或全逐仓配置发生变动时

    * "P"中会推送该 symbol 对应的"BOTH"方向上的持仓详情
    * 如果是多空方向上发生持仓变动, "P"中会推送该 symbol 发生持仓变动的对应"LONG"或"SHORT"方向上的持仓详情
    * 该 symbol 上被初始化过的"LONG"或"SHORT"方向的逐仓持仓, 也会被推送
    * 所以该 symbol 上推送的 position 方向组合, 由具体场景决定()
    * 其他 symbol 的所有持仓信息都不会被推送，即使其持仓不为 0
  * 简言之, 您应该通过相关的 rest 接口( `GET /fapi/v2/account` 和 `GET /fapi/v2/positionRisk`) 获取资产和头寸的**全量** 信息; 通过 Websocket USER-DATA-STREAM 中的事件`ACCOUNT_UPDATE`对本地缓存的资产或头寸数据进行**增量** 更新。

  * 可以访问[这里](https://dev.binance.vision/t/838) 获取示例以帮助对本次优化升级的理解




* * *

## 2020-10-27

U本位合约

WEB SOCKET STREAM

  * 单个连接可订阅的最大 stream 数量调整为 200



* * *

## 2020-10-10

U本位合约

WEBSOCKET

  * 新增 WebSocket 综合指数交易对信息更新`<symbol>@compositeIndex` 。



* * *

## 2020-10-09

U本位合约

  * 新增接口 `GET /fapi/v1/indexInfo` 以获取交易对为综合指数的基础成分信息。



* * *

## 2020-09-18

U本位合约

  * 新增 API 交易量化规则指标查询接口 `GET /fapi/v1/apiTradingStatus`。



* * *

## 2020-09-16

U本位合约

  * 新增杠杆代币历史净值 K 线接口 `GET /fapi/v1/lvtKlines`。  
杠杆代币净值系统基于合约架构，故该接口采用 fapi。



WEBSOCKET

  * 新增 WebSocket 杠杆代币信息更新`<tokenName>@tokenNav` 和  
净值 K 线更新`<tokenName>@nav_Kline_<interval>`。  
杠杆代币净值系统基于合约架构，故该推送采用合约 WS 服务。



* * *

## 2020-09-09

U本位合约

  * 一些过期或者被取消的订单将在未来开始逐步不会从 API 的接口返回。
    * 被移除的订单需要满足如下条件:
      * 订单的最终状态为 `CANCELED` 或者 `EXPIRED`, **并且**
      * 订单没有任何的成交记录, **并且**
      * 订单生成时间 + 7 天 < 当前时间
    * 如下的接口会受影响:
      * `GET /fapi/v1/order`
      * `GET /fapi/v1/allOrders`



* * *

## 2020-08-16

币本位合约

WEBSOCKET

  * 新增 Websocket 账户信息请求功能, 并开放以下请求:
    * `<listenKey>@account` 请求获取账户信息
    * `<listenKey>@balance` 请求获取账户余额
    * `<listenKey>@balance` 请求获取持仓信息



REST

  * 新增接口`GET /dapi/v1/adlQuantile` 以获取持仓 ADL 队列位置估算分数



* * *

## 2020-08-14

U本位合约

  * 接口`GET /fapi/v1/premiumIndex` 新增返回字段 "indexPrice", 表示现货指数价格。
  * 以下 websocket 行情，新增返回字段 "i" 表示现货指数价格：
    * `<symbol>@markPrice`,
    * `<symbol>@markPrice@1s`,
    * `!markPrice@arr`,
    * `!markPrice@arr@1s`



* * *

## 2020-08-12

币本位合约

  * 新增接口 `GET /dapi/v1/forceOrders` 以获取用户强平订单历史.



* * *

## 2020-08-12

U本位合约

  * 新增接口 `GET /fapi/v1/forceOrders` 以获取用户强平订单历史.



* * *

## 2020-08-11

币本位合约

币本位永续合约

  * 新增合约类型("contractType") `PERPETUAL` 表示币本位永续合约

  * 接口`GET /dapi/v1/premiumIndex`新增返回内容:

    * `lastFundingRate` 表示(永续合约的)最近更新的资金费率
    * `nextFundingTime` 表示(永续合约的)下次资金费时间
  * 新增接口`GET /dapi/v1/fundingRate` 用以获取币本位永续合约的资金费率历史

  * WSS 推送`<symbol>@markPrice`, `<symbol>@markPrice@1s`, `<pair>@markPrice`, 和 `<pair>@markPrice@1s`新增推送内容:

    * `r` 表示(永续合约的)最近更新的资金费率
    * `T` 表示(永续合约的)下次资金费时间



* * *

## 2020-07-30

U本位合约

  * 新增接口`GET /fapi/v1/adlQuantile` 以获取持仓 ADL 队列位置估算分数



* * *

## 2020-07-22

币本位合约

  * 新增币本位合约大数据接口:
    * `GET /futures/data/openInterestHist`
    * `GET /futures/data/topLongShortAccountRatio`
    * `GET /futures/data/topLongShortPositionRatio`
    * `GET /futures/data/globalLongShortAccountRatio`
    * `GET /futures/data/takerBuySellVol`
    * `GET /futures/data/basis`



* * *

## 2020-07-17

U本位合约

  * 接口 `GET /fapi/v1/income` 权重调整为 20



* * *

## 2020-07-02

U本位合约

WEBSOCKET

  * "ACCOUNT_UPDATE" 事件新增返回字段 "m" 表示事件推出缘由。
  * "ORDER_TRADE_UPDATE" 事件新增返回字段 "rp" 表示该交易实现损益。



* * *

## 2020-06-15

U本位合约

  * 接口`GET /fapi/v2/account`，`GET /fapi/v2/balance`返回内容新增字段:
    * `availableBalance`
    * `maxWithdrawAmount`



* * *

## 2020-06-04

U本位合约

  * 新增 `/fapi/v2/` 接口, 较 v1 对应接口性能有较大提升:
    * `GET /fapi/v2/account`
    * `GET /fapi/v2/balance`



* * *

## 2020-06-02

U本位合约

  * 新增 `/fapi/v2/` 接口 `GET /fapi/v2/positionRisk`:
    * 允许用户指定 symbol 查询
    * 市场上所有 symbol 都可以被查询
    * 返回内容有效区分单向持仓模式和双向持仓模式
    * 较 ‘/fapi/v1/positionRisk’ 性能有较大改善



* * *

## 2020-05-18

U本位合约

  * 新增参数 `closePosition` 于下单接口 `POST /fapi/v1/order`, 表示条件全部平仓:  
如果一个`STOP_MARKET` 或 `TAKE_PROFIT_MARKET` 条简单设置了 `closePosition=true` 并被触发了，当时持有**所有** 多头仓位(若为卖单)或当时持有**所有** 空头仓位(若为买单)将会被平仓。
  * 新增返回字段`closePosition`于以下接口表示是否为条件全平仓单:
    * `POST /fapi/v1/order`
    * `POST /fapi/v1/batchOrders`
    * `GET /fapi/v1/order`
    * `DELETE /fapi/v1/order`
    * `DELETE /fapi/v1/batchOrders`
    * `GET /fapi/v1/openOrder`
    * `GET /fapi/v1/openOrders`
    * `GET /fapi/v1/allOrders`



* * *

## 2020-05-18

U本位合约

  * 一些过期或者被取消的订单将在未来开始逐步不会从 API 的接口返回, 但是还可以从网页端查询到。
    * 被移除的订单需要满足如下条件:
      * 订单的最终状态为 `CANCELED` 或者 `EXPIRED`, **并且**
      * 订单没有任何的成交记录, **并且**
      * 订单生成时间 + 30 天 < 当前时间
    * 如下的接口会受影响:
      * `GET /fapi/v1/order`
      * `GET /fapi/v1/allOrders`



* * *

## 2020-05-15

U本位合约

  * Wesocket 行情消息 `<symbol>@bookTicker` 和 `!bookTicker` 增加返回字段:
    * `E` 表示事件推出事件
    * `T` 表示撮合时间



* * *

## 2020-05-14

U本位合约

  * 以下接口返回内容增加`time`字段，表示撮合引擎时间：
    * `GET /fapi/v1/ticker/price`
    * `GET /fapi/v1/ticker/bookTicker`
    * `GET /fapi/v1/openInterest`



* * *

## 2020-05-11

U本位合约

  * 新增接口 `POST /fapi/v1/countdownCancelAll` 以实现倒计时自动撤单。
    * 该接口可以被用于确保在倒计时结束时撤销指定 symbol 上的所有挂单。
    * 在使用这个功能时，接口应像心跳一样在倒计时内被反复调用，以便可以取消既有的倒计时并开始新的倒数计时设置。



* * *

## 2020-05-06

U本位合约

REST 接口

  * 接口 `GET /fapi/v1/leverageBracket` 调整为 USER-DATA 权限访问，需要验签以及 timestamp



WEBSOCKET 账户信息推送

  * 请注意: 当某一持仓发生"FUNDING FEE"时，事件`ACCOUNT_UPDATE`将只会推送相关的用户资产余额信息和持仓信息，而不会推送其余无关的资产和持仓信息。
    * 当用户某**全仓** 持仓发生"FUNDING FEE"时，事件`ACCOUNT_UPDATE`将只会推送相关的用户资产余额信息`B`(仅推送 FUNDING FEE 发生相关的资产余额信息)，而不会推送任何持仓信息`P`。
    * 当用户某**逐仓** 仓持仓发生"FUNGDING FEE"时，事件`ACCOUNT_UPDATE`将只会推送相关的用户资产余额信息`B`(仅推送"FUNDING FEE"所使用的资产余额信息)，和相关的持仓信息`P`(仅推送这笔"FUNDING FEE"发生所在的持仓信息)，其余持仓信息不会被推送



* * *

## 2020-04-25

U本位合约

  * 用户"订单/交易更新推送" `ORDER_TRADE_UPDATE` 新增以下字段:

    * `cp` 表示是否为平仓条件单
    * `AP` 表示追踪止损单的追踪止损激活价格
    * `cr` 表示追踪止损单的追踪止损回调比例
  * 新增账户信息推送事件: "追加保证金通知"`MARGIN_CALL`.




* * *

## 2020-04-17

U本位合约

  * 下单接口支持新的可选参数 `newOrderRespType` 表示下单响应类型。支持`ACK` 和 `RESULT`,  
如果`newOrderRespType= RESULT`:
    * `MARKET` 订单将直接返回成交(FILLED)结果；
    * 配合使用特殊 `timeInForce` 的 `LIMIT` 订单将直接返回成交/过期(FILLED/EXPIRED)结果。



* * *

## 2020-04-14

U本位合约

WEB SOCKET 连接限制

  * Websocket 服务器每秒最多接受 10 个消息。消息包括:
    * PING 帧
    * PONG 帧
    * JSON 格式的消息, 比如订阅, 断开订阅.
  * 如果用户发送的消息超过限制，连接会被断开连接。反复被断开连接的 IP 有可能被服务器屏蔽。
  * 单个连接最多可以订阅 **200** 个 Streams。



* * *

## 2020-04-09

U本位合约

  * 新增接口合约大数据 `GET /futures/data/takerlongshortRatio` 以查询合约主动买卖量



* * *

## 2020-04-08

U本位合约

  * 新增接口 `GET /fapi/v1/positionSide/dual` 以查询用户当前持仓模式
  * 新增接口 `POST /fapi/v1/batchOrders` 以实现批量下单



* * *

## 2020-04-06

U本位合约

  * 请注意 账户信息推送 事件 "Balance 和 Position 更新推送"(`ACCOUNT_UPDATE`)将不再未发生更新时推送，具体规则如下：

    * 仅当账户信息有变动时(包括资金、仓位、保证金模式等发生变化)，才会推送此事件；
    * 订单状态变化没有引起账户和持仓变化的，不会推送此事件；
    * 每次推送的 position 信息，仅包含当前持仓不为 0 或逐仓仓位保证金不为 0 的 symbol position。
  * 新增接口 `POST /fapi/v1/positionSide/dual` 更改持仓模式：双向或单向持仓模式。

  * 以下接口新增参数 `positionSide` 用以支持单向/双向持仓模式，表示持仓方向：

    * `POST /fapi/v1/order`
    * `POST /fapi/v1/positionMargin`
  * 以下接口新增返回字段 `positionSide` 用以支持单向/双向持仓模式，表示持仓方向：

    * `POST /fapi/v1/order`
    * `GET /fapi/v1/order`
    * `DELETE /fapi/v1/order`
    * `DELETE /fapi/v1/batchOrders`
    * `GET /fapi/v1/openOrder`
    * `GET /fapi/v1/openOrders`
    * `GET /fapi/v1/allOrders`
    * `GET /fapi/v1/account`
    * `POST /fapi/v1/positionMargin`
    * `GET /fapi/v1/positionMargin/history`
    * `GET /fapi/v1/positionRisk`
    * `GET /fapi/v1/userTrades`
  * 账户信息推送 事件 "Balance 和 Position 更新推送"(`ACCOUNT_UPDATE`)和 "订单/交易更新推送"(ORDER_TRADE_UPDATE)中新增字段 `ps` 表示持仓方向。




* * *

## 2020-03-30

U本位合约

  * 新增接口合约大数据:
    * `GET /futures/data/openInterestHist`
    * `GET /futures/data/topLongShortAccountRatio`
    * `GET /futures/data/topLongShortPositionRatio`
    * `GET /futures/data/globalLongShortAccountRatio`



* * *

## 2020-02-26

U本位合约

  * 新增订单类型:跟踪止损 `TRAILING_STOP_MARKET`



* * *

## 2020-02-20

U本位合约

  * 新增接口以查询指定的当前挂单: `GET /fapi/v1/openOrder`



* * *

## 2020-02-17

U本位合约

  * `<symbol>@ticker` 与 `!ticker@arr` 更新频率提升为 1000ms
  * 新增 500ms 更新的增量深度信息流选项: `<symbol>@depth@500ms`
  * 新增 500ms 更新的有限档深度信息流选项: `<symbol>@depth<level>@500ms`



* * *

## 2020-02-12

U本位合约

  * Java [SDK 和代码示例](/zh-CN/docs/sdks-tools/overview) 发布

  * 实现每秒更新的标记价格信息流选项:  
`<symbol>@markPrice@1s` and `!markPrice@arr@1s`




* * *

## 2020-02-05

U本位合约

  * 新增接口`GET /fapi/v1/leverageBracket`: 查询杠杆分层标准。



* * *

## 2020-01-19

U本位合约

  * "cumQty" 字段将于未来几周从 `DELETE /fapi/v1/order`，`DELETE /fapi/v1/batchOrders` 等 `order` 相关接口的返回内容中去除，请使用 "executedQty" 字段予以替代。



* * *

## 2019-12-19

U本位合约

  * 新增接口获取市场当前未平仓合约数： `GET /fapi/v1/openInterest`



* * *

## 2019-12-18

U本位合约

  * 新增账户信息推送事件：`listenKeyExpired`。



* * *

## 2019-12-12

U本位合约

  * 新增接口撤销指定 symbol 的所有订单: `DELETE /fapi/v1/allOpenOrders`
  * 新增接口批量撤销订单：`DELETE /fapi/v1/batchOrders`
  * 新增支持仅减仓`reduceOnly`的订单类型：
    * `TAKE_PROFIT`
    * `TAKE_PROFIT_MARKET`
    * `STOP`
    * `STOP_MARKET`



* * *

## 2019-11-29

U本位合约

  * 新增接口获取市场强平订单：`GET /fapi/v1/allForceOrders`
  * 新增市场行情推送：
    * 强平订单：`<symbol>@forceOrder`
    * 全市场强平订单：`!forceOrder@arr`



* * *

## 2019-11-25

U本位合约

  * `GET /fapi/v1/account` 新增返回内容: `positions`
  * 以下接口新增返回值 `time` 表示订单创建时间:
    * `GET /fapi/v1/openOrders`
    * `GET /fapi/v1/order`
    * `GET /fapi/v1/allOrders`



* * *

## 2019-11-15

U本位合约

  * Websocket 新增市场行情流：
    * `!miniTicker@arr`: 全市场的精简 Ticker 更新
    * `!ticker@arr`: : 全市场的完整 Ticker 更新



* * *

## 2019-11-12

U本位合约

  * WSS 支持实时订阅和取消数据流。



* * *

## 2019-11-05

U本位合约

  * 新增订单类型:
    * `STOP_MARKET`止损市价单，
    * `TAKE_PROFIT_MARKET`止盈市价单
  * 下单新增可选参数: `workingType` 可选`stopPrice`由 "CONTRACT_PRICE" 或 "MARK_PRICE"触发
  * USER-DATA-STREAMS 新增:
    * `ORDER_TRADE_UPDATE`订单/交易 更新推送 增加：
      * "T": 撮合时间
      * "wt": workingType
    * `ACCOUNT_UPDATE` Balance 和 Position 更新推送 增加："T": 撮合时间



* * *

## 2019-10-28

U本位合约

  * 新增接口查询账户损益资金流水：`GET /fapi/v1/income`



* * *

## 2019-10-25

U本位合约

  * 账户信息推送事件`ACCOUNT_UPDATE`增加字段 "up"，表示持仓未实现盈亏。
  * 账户信息推送事件`ORDER_TRADE_UPDATE`增加字段 "R"，表示该成交是否作为只减仓单。



* * *

## 2019-10-24

U本位合约

  * 新增最优挂单信息行情流: `<symbol>@bookTicker` 与`!bookTicker`
  * 新增有限档深度信息行情流： `<symbol>@depth<levels>` 与 `<symbol>@depth<levels>@100ms`
  * 更新频率达到 100ms 的更快的增量深度信息流选项: `<symbol>@depth@100ms`
  * `Websocket行情推送` 增加 `Update Speed` 更新速度



* * *

## 2019-10-18

U本位合约

  * 新增接口 `POST /fapi/v1/leverage` 以调整开仓杠杆倍数。
  * 接口 `GET /fapi/v1/positionRisk` 的返回内容中新增字段：
  * "leverage": 当前开仓杠杆倍数；
  * "maxNotionalValue": 当前开仓杠杆倍数下的名义价值上限。
  * `MARKET` 市价单支持 `reduceOnly` 只减仓参数。



* * *

## 2019-10-14

U本位合约

  * 新增接口`GET /fapi/v1/fundingRate`: 获取资金费率历史。



* * *

## 2019-10-11

U本位合约

  * 账户信息推送事件`ORDER_TRADE_UPDATE`增加字段 "m"，表示该成交是否作为挂单成交



* * *

## 2019-10-08

U本位合约

  * 新增限价指令订单参数 `reduceOnly` ：只减仓
  * 新增订单类型 `TAKE_PROFIT`： 止盈单



* * *

此页面是否有帮助？

Last modified on November 12, 2026

[快速开始](/zh-CN/docs/products/derivatives-trading-portfolio-margin-pro/quick-start)[基本信息](/zh-CN/docs/products/derivatives-trading-portfolio-margin-pro/general-info)