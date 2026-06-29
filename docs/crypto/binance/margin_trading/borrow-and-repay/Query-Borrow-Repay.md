---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/borrow-and-repay/Query-Borrow-Repay
api_type: REST
updated_at: 2026-06-29 19:09:25.491697
---

# Change Log

## 2026-06-17[​](/docs/margin_trading/change-log#2026-06-17 "Direct link to 2026-06-17")

Effective at **2026-06-15 08:00 (UTC)**

  * `POST /sapi/v1/margin/order/oto`:

    * `pendingPrice` is now **mandatory** when `pendingTrailingDelta` is provided.
  * `POST /sapi/v1/margin/order/otoco`:

    * `pendingAbovePrice` is now **mandatory** when `pendingAboveTrailingDelta` is provided.
    * `pendingBelowPrice` is now **mandatory** when `pendingBelowTrailingDelta` is provided.



* * *

## 2026-05-05[​](/docs/margin_trading/change-log#2026-05-05 "Direct link to 2026-05-05")

  * New endpoints for querying and repaying cross-margin liquidation loans: 
    * `GET /sapi/v1/margin/liquidation-loan` — Query the current liquidation loan status
    * `POST /sapi/v1/margin/liquidation-loan/repay` — Repay a liquidation loan
    * `GET /sapi/v1/margin/liquidation-loan/repay-history` — Query liquidation loan repayment history



* * *

## 2026-04-23[​](/docs/margin_trading/change-log#2026-04-23 "Direct link to 2026-04-23")

Effective at **2026-05-07 08:00 (UTC)**

  * Updated the request weight for the following Margin Trade endpoints: 
    * `POST /sapi/v1/margin/order`
    * `POST /sapi/v1/margin/order/oco`
    * `POST /sapi/v1/margin/order/oto`
    * `POST /sapi/v1/margin/order/otoco`
    * Previous request weight: 6(UID)
    * New request weight: 
      * 6(UID) when `sideEffectType` is **not** `MARGIN_BUY` or `AUTO_BORROW_REPAY`
      * 1500(UID) when `sideEffectType` is `MARGIN_BUY` or `AUTO_BORROW_REPAY`



* * *

## 2026-04-22[​](/docs/margin_trading/change-log#2026-04-22 "Direct link to 2026-04-22")

  * New endpoint `POST /sapi/v1/margin/exit-special-key-mode` to exit the Margin Special Key mode for Cross Margin Classic accounts.



* * *

## 2026-04-16[​](/docs/margin_trading/change-log#2026-04-16 "Direct link to 2026-04-16")

  * `GET /sapi/v1/margin/maxBorrowable` request weight updated from 50(IP) to 750(UID).



* * *

## 2026-04-13[​](/docs/margin_trading/change-log#2026-04-13 "Direct link to 2026-04-13")

  * The following endpoint is no longer supported due to the sunset of Cross Margin Pro Mode: 
    * `GET /sapi/v1/margin/leverageBracket`



* * *

## 2026-01-21[​](/docs/margin_trading/change-log#2026-01-21 "Direct link to 2026-01-21")

  * Following the announcement from 2025-11-10, the following endpoints/methods will no longer be available starting from **2026-02-20 07:00 UTC** :

**REST API**

    * POST /sapi/v1/userDataStream
    * PUT /sapi/v1/userDataStream
    * DELETE /sapi/v1/userDataStream
    * POST /sapi/v1/userDataStream/isolated
    * PUT /sapi/v1/userDataStream/isolated
    * DELETE /sapi/v1/userDataStream/isolated



## 2026-01-16[​](/docs/margin_trading/change-log#2026-01-16 "Direct link to 2026-01-16")

  * Update on endpoints restrictions 
    * `GET /sapi/v1/margin/capital-flow`：Addition of query time range restriction. This restriction will take effect from approximately **2026-02-02 07:00 UTC**.
    * When both `startTime` and `endTime` are specified, the time span cannot exceed 7 days, otherwise, the endpoint is expected to return an error: 
          
          {  
            "code": -4047,  
            "msg": "Time interval must be within 0-7 days"  
          }  
          

    * Please split your query into multiple requests if the time range required exceeds 7 days.



## 2025-12-26[​](/docs/margin_trading/change-log#2025-12-26 "Direct link to 2025-12-26")

**Time-sensitive Notice**

  * **The following change to REST API will occur at approximately 2026-01-15 07:00 UTC:**   
When calling endpoints that require signatures, percent-encode payloads before computing signatures. Requests that do not follow this order will be rejected with [`-1022 INVALID_SIGNATURE`](/docs/margin_trading/error-code#-1022-invalid_signature). Please review and update your signing logic accordingly.



**REST API**

  * Updated documentation for REST API regarding [Signed Endpoints examples for placing an order](/docs/margin_trading/general-info#signed-endpoint-examples-for-post-apiv3order).



## 2025-11-10[​](/docs/margin_trading/change-log#2025-11-10 "Direct link to 2025-11-10")

  * **All documentation related with listenKey for use on wss://[stream.binance.com](http://stream.binance.com) removed from the Margin Trading SAPI portal on 2025-11-10. The features below will remain available until a future retirement announcement is made..**
    * POST /sapi/v1/userDataStream
    * PUT /sapi/v1/userDataStream
    * DELETE /sapi/v1/userDataStream
    * POST /sapi/v1/userDataStream/isolated
    * PUT /sapi/v1/userDataStream/isolated
    * DELETE /sapi/v1/userDataStream/isolated
  * **Users are recommended to move to the new listen token subscription method below, which offers slightly better performance (lower latency):**
    * POST /sapi/v1/userListenToken : Create a new user data stream and return a listenToken.
    * method userDataStream.subscribe.listenToken : Subscribe to the user data stream using listenToken.
  * The [User Data Stream](https://developers.binance.com/docs/margin_trading/trade-data-stream) documentation will remain as reference for the payloads users can receive: 
    * [Account Update](https://developers.binance.com/docs/margin_trading/trade-data-stream/Event-Account-Update): outboundAccountPosition is sent any time an account balance has changed and contains the assets that were possibly changed by the event that generated the balance change.
    * [Balance Update](https://developers.binance.com/docs/margin_trading/trade-data-stream/Event-Balance-Update): Balance Update occurs when transfer of funds between accounts.
    * [Order Update](https://developers.binance.com/docs/margin_trading/trade-data-stream/Event-Order-Update): Orders are updated with the executionReport event.



## 2025-10-06[​](/docs/margin_trading/change-log#2025-10-06 "Direct link to 2025-10-06")

  * **Receiving user data stream on wss://stream.binance.com:9443 using a listenKey is now deprecated.**
    * This feature will be removed from our system at a later date.
    * The related documents will also be removed together with the feature removal.
    * Users are recommended to move to the new listen token subscription method below.
  * New user data stream subscription with [Websocket API](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/general-api-information) released: 
    * POST /sapi/v1/userListenToken : Create a new user data stream and return a listenToken.
    * method userDataStream.subscribe.listenToken : Subscribe to the user data stream using listenToken.



## 2025-09-16[​](/docs/margin_trading/change-log#2025-09-16 "Direct link to 2025-09-16")

  * One endpoint updated : 
    * POST `/sapi/v1/margin/apiKey`: Supported produects scope and error code description added into the API description.



## 2025-06-17[​](/docs/margin_trading/change-log#2025-06-17 "Direct link to 2025-06-17")

  * Best Practice section uploaded on the Margin Trading



## 2025-06-16[​](/docs/margin_trading/change-log#2025-06-16 "Direct link to 2025-06-16")

  * List schedule endpoint is now released for Margin: 
    * GET `/sapi/v1/margin/list-schedule`: Get the upcoming tokens or symbols listing schedule for Cross Margin and Isolated Margin.



## 2024-09-19[​](/docs/margin_trading/change-log#2024-09-19 "Direct link to 2024-09-19")

  * Binance Margin offers low-latency trading through a special key, available exclusively to users with VIP level 4 or higher.

If you are VIP level 3 or below, please contact your VIP manager for eligibility criterias.

The endpoints below are available :

    * POST /sapi/v1/margin/apiKey
    * DELETE /sapi/v1/margin/apiKey
    * PUT /sapi/v1/margin/apiKey/ip
    * GET /sapi/v1/margin/apiKey
    * GET /sapi/v1/margin/api-key-list
  * How to use the special API key

    1. Use SAPI to create a special pair of "margin trade only" key/secret via the endpoint above.

    2. For cross margin account, do not send the symbol parameter.

    3. For isolated margin account of a specific symbol, please send the symbol as the isolated margin pair.

    4. Use the key/secret responded in step 1 to do the margin trading and listenKey creating via SPOT REST api (<https://api.binance.com/api/v3/>) endpoints.




## 2024-09-13[​](/docs/margin_trading/change-log#2024-09-13 "Direct link to 2024-09-13")

  * One-Triggers-the-Other (OTO) orders and One-Triggers-a-One-Cancels-The-Other (OTOCO) orders are now enabled for Margin: 
    * POST `/sapi/v1/margin/order/oto`: Post a new OTO order for margin account
    * POST `/sapi/v1/margin/order/otoco`: Post a new OTOCO order for margin account
  * New parameters added into response body to replace the parameter of 'transferEnabled' in the endpoint of GET `/sapi/v1/margin/account`: 
    * transferInEnabled
    * transferOutEnabled



* * *

## 2024-01-09[​](/docs/margin_trading/change-log#2024-01-09 "Direct link to 2024-01-09")

  * According to the [announcement](https://www.binance.com/en/support/announcement/updates-on-binance-margin-sapi-endpoints-2024-03-31-a1868c686ce7448da8c3061a82a87b0c), Binance Margin will remove the following SAPI interfaces at 4:00 on March 31, 2024 (UTC). Please switch to the corresponding alternative interfaces in time:

    * `POST /sapi/v1/margin/transfer` will be removed, please replace with `POST /sapi/v1/asset/transfer` universal transfer
    * `POST /sapi/v1/margin/isolated/transfer` will be removed, please replace with `POST /sapi/v1/asset/transfer` universal transfer
    * `POST /sapi/v1/margin/loan` will be removed, please replace with the new `POST /sapi/v1/margin/borrow-repay` borrowing and repayment interface
    * `POST /sapi/v1/margin/repay` will be removed, please replace with the new `POST /sapi/v1/margin/borrow-repay` borrowing and repayment interface
    * `GET /sapi/v1/margin/isolated/transfer` will be removed, please replace it with `GET /sapi/v1/margin/transfer` to get total margin transfer history
    * `GET /sapi/v1/margin/asset` will be removed, please replace with `GET /sapi/v1/margin/allAssets`
    * `GET /sapi/v1/margin/pair` will be removed, please replace with `GET /sapi/v1/margin/allPairs`
    * `GET /sapi/v1/margin/isolated/pair` will be removed, please replace with `GET /sapi/v1/margin/isolated/allPairs`
    * `GET /sapi/v1/margin/loan` will be removed, please replace with `GET /sapi/v1/margin/borrow-repay`
    * `GET /sapi/v1/margin/repay` will be removed, please replace with `GET /sapi/v1/margin/borrow-repay`
    * `GET /sapi/v1/margin/dribblet` will be removed, please replace with `GET /sapi/v1/asset/dribblet`
    * `GET /sapi/v1/margin/dust` will be removed, please replace with `POST /sapi/v1/asset/dust-btc`
    * `POST /sapi/v1/margin/dust` will be removed, please replace with `POST /sapi/v1/asset/dust`
  * New Endpoints for Margin:

    * `POST /sapi/v1/margin/borrow-repay`: Margin account borrow/repay
    * `GET /sapi/v1/margin/borrow-repay`: Query borrow/repay records in Margin account
  * Update Endpoints fpr Margin:

    * `GET /sapi/v1/margin/transfer`: add parameter `isolatedSymbol`, add response body
    * `GET /sapi/v1/margin/allAssets`: add parameter `asset`, add response body
    * `GET /sapi/v1/margin/allPairs`: add parameter `symbol`
    * `GET /sapi/v1/margin/isolated/allPairs`: add parameter `symbol`



* * *

## 2023-12-22[​](/docs/margin_trading/change-log#2023-12-22 "Direct link to 2023-12-22")

  * New Websocket for Margin Trading: 
    * New Base url `wss://margin-stream.binance.com` for two events: Liability update event and Margin call event



* * *

## 2023-11-21[​](/docs/margin_trading/change-log#2023-11-21 "Direct link to 2023-11-21")

  * Update endpoints for Margin 
    * `POST /sapi/v1/margin/order`：New enumerate value `AUTO_BORROW_REPAY` for the field of `sideEffectType`
    * `POST /sapi/v1/margin/order/oco`：New enumerate value `AUTO_BORROW_REPAY` for the field of `sideEffectType`
    * `GET /sapi/v1/margin/available-inventory`：New response field of `updateTime` which indicates the acquisition time of lending inventory.



* * *

## 2023-11-17[​](/docs/margin_trading/change-log#2023-11-17 "Direct link to 2023-11-17")

  * New endpoint for Margin to support cross margin Pro mode[FAQ](https://www.binance.com/en/support/faq/introduction-to-binance-cross-margin-pro-0b5441a1c1ff431bb2e135dfa8e6ffba): 
    * `GET /sapi/v1/margin/leverageBracket`: query Liability coin leverage bracket in cross margin Pro mode
  * Update endpoints for Margin: 
    * `POST /sapi/v1/margin/max-leverage`: field `maxLeverage` adds value 10 for Cross Margin Pro
    * `GET /sapi/v1/margin/account`: add new response field `accountType`, `MARGIN_2` for Cross Margin Pro



* * *

## 2023-10-16[​](/docs/margin_trading/change-log#2023-10-16 "Direct link to 2023-10-16")

  * New endpoint for Margin: 
    * `GET /sapi/v1/margin/available-inventory`: Query margin available inventory
    * `POST /sapi/v1/margin/manual-liquidation`: Margin manual liquidation



* * *

## 2023-08-31[​](/docs/margin_trading/change-log#2023-08-31 "Direct link to 2023-08-31")

  * New endpoint for Margin: 
    * `/sapi/v1/margin/capital-flow`: Get cross or isolated margin capital flow



* * *

## 2023-07-07[​](/docs/margin_trading/change-log#2023-07-07 "Direct link to 2023-07-07")

  * New endpoints for Margin: 
    * `POST /sapi/v1/margin/max-leverage`: Adjust cross margin max leverage



* * *

## 2023-06-29[​](/docs/margin_trading/change-log#2023-06-29 "Direct link to 2023-06-29")

  * New endpoints for Margin: 
    * `GET /sapi/v1/margin/dust`: Get Assets That Can Be Converted Into BNB
    * `POST /sapi/v1/margin/dust`: Convert dust assets to BNB.



* * *

## 2023-06-22[​](/docs/margin_trading/change-log#2023-06-22 "Direct link to 2023-06-22")

  * Update endpoints for Margin: 
    * `POST /sapi/v1/margin/order`: add fields `autoRepayAtCancel` and `selfTradePreventionMode`
    * `POST /sapi/v1/margin/order/oco`: add field `selfTradePreventionMode`



* * *

## 2023-06-20[​](/docs/margin_trading/change-log#2023-06-20 "Direct link to 2023-06-20")

  * Update endpoints for Margin: 
    * `GET /sapi/v1/margin/delist-schedule`: get tokens or symbols delist schedule for cross margin and isolated margin



* * *

## 2023-02-27[​](/docs/margin_trading/change-log#2023-02-27 "Direct link to 2023-02-27")

  * New endpoints for Margin: 
    * `/sapi/v1/margin/next-hourly-interest-rate`: Get user the next hourly estimate interest



* * *

## 2023-02-02[​](/docs/margin_trading/change-log#2023-02-02 "Direct link to 2023-02-02")

  * New endpoints for Margin: 
    * `GET /sapi/v1/margin/exchange-small-liability`: Query the coins which can be small liability exchange
    * `POST /sapi/v1/margin/exchange-small-liability`: Cross Margin Small Liability Exchange
    * `GET /sapi/v1/margin/exchange-small-liability-history`: Get Small liability Exchange History



* * *

## 2022-09-16[​](/docs/margin_trading/change-log#2022-09-16 "Direct link to 2022-09-16")

  * New endpoint for Margin： 
    * `GET /sapi/v1/margin/tradeCoeff`: Get personal margin level information



* * *

## 2022-07-01[​](/docs/margin_trading/change-log#2022-07-01 "Direct link to 2022-07-01")

  * New endpoint for Margin: 
    * `GET /sapi/v1/margin/dribblet` to query the historical information of user's margin account small-value asset conversion BNB.
  * Update endpoint for Margin: 
    * `GET /sapi/v1/margin/repay`: Add response field rawAsset.



* * *

## 2022-05-26[​](/docs/margin_trading/change-log#2022-05-26 "Direct link to 2022-05-26")

  * Update info for the following margin account endpoints: The max interval between `startTime` and `endTime` is 30 days.: 
    * `GET /sapi/v1/margin/transfer`
    * `GET /sapi/v1/margin/loan`
    * `GET /sapi/v1/margin/repay`
    * `GET /sapi/v1/margin/isolated/transfer`
    * `GET /sapi/v1/margin/interestHistory`



* * *

## 2022-04-26[​](/docs/margin_trading/change-log#2022-04-26 "Direct link to 2022-04-26")

  * `GET /sapi/v1/margin/rateLimit/order` added 
    * The endpoint will display the user's current margin order count usage for all intervals.



* * *

## 2021-12-30[​](/docs/margin_trading/change-log#2021-12-30 "Direct link to 2021-12-30")

  * Update endpoint for Margin： 
    * Removed out `limit` from`GET /sapi/v1/margin/interestRateHistory`; The max interval between startTime and endTime is 30 days.



* * *

## 2021-12-03[​](/docs/margin_trading/change-log#2021-12-03 "Direct link to 2021-12-03")

  * New endpoints for Margin: 
    * `GET /sapi/v1/margin/crossMarginData` to get cross margin fee data collection
    * `GET /sapi/v1/margin/isolatedMarginData` to get isolated margin fee data collection
    * `GET /sapi/v1/margin/isolatedMarginTier` to get isolated margin tier data collection



* * *

## 2021-10-14[​](/docs/margin_trading/change-log#2021-10-14 "Direct link to 2021-10-14")

  * Update the time range of the response data for the following margin account endpoints, `startTime` and `endTime` time span will not exceed 30 days, without time parameter sent the system will return the last 7 days of data by default, while the `archived` parameter is `true`, the system will return the last 7 days of data 6 months ago by default: 
    * `GET /sapi/v1/margin/transfer`
    * `GET /sapi/v1/margin/loan`
    * `GET /sapi/v1/margin/repay`
    * `GET /sapi/v1/margin/isolated/transfer`
    * `GET /sapi/v1/margin/interestHistory`



* * *

## 2021-09-08[​](/docs/margin_trading/change-log#2021-09-08 "Direct link to 2021-09-08")

  * Add endpoints for enabled isolated margin account limit:

    * `DELETE /sapi/v1/margin/isolated/account` to disable isolated margin account for a specific symbol
    * `POST /sapi/v1/margin/isolated/account` to enable isolated margin account for a specific symbol
    * `GET /sapi/v1/margin/isolated/accountLimit` to query enabled isolated margin account limit
  * New field "enabled" in response of `GET /sapi/v1/margin/isolated/account` to check if the isolated margin account is enabled




* * *

## 2021-08-23[​](/docs/margin_trading/change-log#2021-08-23 "Direct link to 2021-08-23")

  * New endpoints for Margin Account OCO: 
    * `POST /sapi/v1/margin/order/oco`
    * `DELETE /sapi/v1/margin/orderList`
    * `GET /sapi/v1/margin/orderList`
    * `GET /sapi/v1/margin/allOrderList`
    * `GET /sapi/v1/margin/openOrderList`



Same usage as spot account OCO

* * *

## 2021-04-28[​](/docs/margin_trading/change-log#2021-04-28 "Direct link to 2021-04-28")

On **May 15, 2021 08:00 UTC** the SAPI Create Margin Account endpoint will be discontinued:

  * `POST /sapi/v1/margin/isolated/create`



Isolated Margin account creation and trade preparation can be completed directly through Isolated Margin funds transfer `POST /sapi/v1/margin/isolated/transfer`

* * *

## 2021-03-05[​](/docs/margin_trading/change-log#2021-03-05 "Direct link to 2021-03-05")

  * New endpoints for Margin: 
    * `GET /sapi/v1/margin/interestRateHistory` to support margin interest rate history query



* * *

## 2021-01-15[​](/docs/margin_trading/change-log#2021-01-15 "Direct link to 2021-01-15")

  * New endpoint `DELETE /sapi/v1/margin/openOrders` for Margin Trade 
    * This will allow a user to cancel all open orders on a single symbol for margin account.
    * This endpoint will cancel all open orders including OCO orders for margin account.



* * *

## 2020-12-01[​](/docs/margin_trading/change-log#2020-12-01 "Direct link to 2020-12-01")

  * Update Margin Trade Endpoint: 
    * `POST /sapi/v1/margin/order` new parameter `quoteOrderQty` allow a user to specify the total `quoteOrderQty` spent or received in the `MARKET` order.



* * *

## 2020-11-16[​](/docs/margin_trading/change-log#2020-11-16 "Direct link to 2020-11-16")

  * Updated endpoints for Margin, new parameter `archived` to query data from 6 months ago: 
    * `GET /sapi/v1/margin/loan`
    * `GET /sapi/v1/margin/repay`
    * `GET /sapi/v1/margin/interestHistory`



* * *

## 2020-11-10[​](/docs/margin_trading/change-log#2020-11-10 "Direct link to 2020-11-10")

  * New endpoint to toggle BNB Burn: 
    * `POST /sapi/v1/bnbBurn` to toggle BNB Burn on spot trade and margin interest.
    * `GET /sapi/v1/bnbBurn` to get BNB Burn status.



* * *

## 2020-09-30[​](/docs/margin_trading/change-log#2020-09-30 "Direct link to 2020-09-30")

  * Update endpoints for Margin Account: 
    * `GET /sapi/v1/margin/maxBorrowable` new field `borrowLimit` in response for account borrow limit.



* * *

## 2020-08-26[​](/docs/margin_trading/change-log#2020-08-26 "Direct link to 2020-08-26")

  * New parameter `symbols` added in the endpoint `GET /sapi/v1/margin/isolated/account`.



* * *

## 2020-07-28[​](/docs/margin_trading/change-log#2020-07-28 "Direct link to 2020-07-28")

ISOLATED MARGIN

  * New parameters "isIsolated" and "symbol" added for isolated margin in the following endpoints:

    * `POST /sapi/v1/margin/loan`
    * `POST /sapi/v1/margin/repay`
  * New parameter "isIsolated" and new response field "isIsolated" added for isolated margin in the following endpoints:

    * `POST /sapi/v1/margin/order`
    * `DELETE /sapi/v1/margin/order`
    * `GET /sapi/v1/margin/order`
    * `GET /sapi/v1/margin/openOrders`
    * `GET /sapi/v1/margin/allOrders`
    * `GET /sapi/v1/margin/myTrades`
  * New parameter "isolatedSymbol" and new response field "isolatedSymbol" added for isolated margin in the following endpoints:

    * `GET /sapi/v1/margin/loan`
    * `GET /sapi/v1/margin/repay`
    * `GET /sapi/v1/margin/interestHistory`
  * New parameter "isolatedSymbol" and new response field "isIsolated" added for isolated margin in the following endpoint `GET /sapi/v1/margin/forceLiquidationRec`

  * New parameter "isolatedSymbol" added for isolated margin in the following endpoints:

    * `GET /sapi/v1/margin/maxBorrowable`
    * `GET /sapi/v1/margin/maxTransferable`
  * New endpoints for isolated margin:

    * `POST /sapi/v1/margin/isolated/create`
    * `POST /sapi/v1/margin/isolated/transfer`
    * `GET /sapi/v1/margin/isolated/transfer`
    * `GET /sapi/v1/margin/isolated/account`
    * `GET /sapi/v1/margin/isolated/pair`
    * `GET /sapi/v1/margin/isolated/allPairs`
  * New endpoints for listenKey management of isolated margin account:

    * `POST /sapi/v1/userDataStream/isolated`
    * `PUT /sapi/v1/userDataStream/isolated`
    * `DELETE /sapi/v1/userDataStream/isolated`



* * *

## 2019-12-18[​](/docs/margin_trading/change-log#2019-12-18 "Direct link to 2019-12-18")

  * New endpoint to get daily snapshot of account:  
`GET /sapi/v1/accountSnapshot`



* * *

## 2019-11-30[​](/docs/margin_trading/change-log#2019-11-30 "Direct link to 2019-11-30")

  * Added parameter `sideEffectType` in `POST /sapi/v1/margin/order (HMAC SHA256)` with enums:

    * `NO_SIDE_EFFECT` for normal trade order;
    * `MARGIN_BUY` for margin trade order;
    * `AUTO_REPAY` for making auto repayment after order filled.
  * New field `marginBuyBorrowAmount` and `marginBuyBorrowAsset` in `FULL` response to `POST /sapi/v1/margin/order (HMAC SHA256)`




* * *

## 2019-11-28[​](/docs/margin_trading/change-log#2019-11-28 "Direct link to 2019-11-28")

  * New SAPI endpont to disable fast withdraw switch:  
`POST /sapi/v1/account/disableFastWithdrawSwitch (HMAC SHA256)`
  * New SAPI endpont to enable fast withdraw switch:  
`POST /sapi/v1/account/enableFastWithdrawSwitch (HMAC SHA256)`

---

# 更新日志

## 2026-06-17[​](/docs/zh-CN/margin_trading/change-log#2026-06-17 "2026-06-17的直接链接")

生效时间: **2026-06-15 08:00 (UTC)**

  * `POST /sapi/v1/margin/order/oto`:

    * 当提供 `pendingTrailingDelta` 时，`pendingPrice` 现在是**必填参数** 。
  * `POST /sapi/v1/margin/order/otoco`:

    * 当提供 `pendingAboveTrailingDelta` 时，`pendingAbovePrice` 现在是**必填参数** 。
    * 当提供 `pendingBelowTrailingDelta` 时，`pendingBelowPrice` 现在是**必填参数** 。



* * *

## 2026-05-05[​](/docs/zh-CN/margin_trading/change-log#2026-05-05 "2026-05-05的直接链接")

  * 新增全仓杠杆强平穿仓欠款相关接口： 
    * `GET /sapi/v1/margin/liquidation-loan` — 查询当前强平穿仓欠款
    * `POST /sapi/v1/margin/liquidation-loan/repay` — 偿还强平穿仓欠款
    * `GET /sapi/v1/margin/liquidation-loan/repay-history` — 查询强平穿仓欠款还款历史



* * *

## 2026-04-23[​](/docs/zh-CN/margin_trading/change-log#2026-04-23 "2026-04-23的直接链接")

生效时间: **2026-05-07 08:00 (UTC)**

  * 更新以下杠杆交易接口的请求权重: 
    * `POST /sapi/v1/margin/order`
    * `POST /sapi/v1/margin/order/oco`
    * `POST /sapi/v1/margin/order/oto`
    * `POST /sapi/v1/margin/order/otoco`
    * 原请求权重: 6(UID)
    * 新请求权重: 
      * `sideEffectType` **不是** `MARGIN_BUY` 或 `AUTO_BORROW_REPAY` 时: 6(UID)
      * `sideEffectType` 是 `MARGIN_BUY` 或 `AUTO_BORROW_REPAY` 时: 1500(UID)



* * *

## 2026-04-22[​](/docs/zh-CN/margin_trading/change-log#2026-04-22 "2026-04-22的直接链接")

  * 新增接口 `POST /sapi/v1/margin/exit-special-key-mode`，用于退出全仓杠杆经典模式的 Margin Special Key 模式。



* * *

## 2026-04-16[​](/docs/zh-CN/margin_trading/change-log#2026-04-16 "2026-04-16的直接链接")

  * `GET /sapi/v1/margin/maxBorrowable` 请求权重从 50(IP) 更新为 750(UID)。



* * *

## 2026-04-13[​](/docs/zh-CN/margin_trading/change-log#2026-04-13 "2026-04-13的直接链接")

  * 由于全仓杠杆 Pro 模式下线，以下接口不再支持： 
    * `GET /sapi/v1/margin/leverageBracket`



* * *

## 2026-01-21[​](/docs/zh-CN/margin_trading/change-log#2026-01-21 "2026-01-21的直接链接")

根据2025-11-10的公告，以下接口/方法将于**2026-02-20 07:00 UTC** 起停止服务：

**REST API**

  * POST /sapi/v1/userDataStream
  * PUT /sapi/v1/userDataStream
  * DELETE /sapi/v1/userDataStream
  * POST /sapi/v1/userDataStream/isolated
  * PUT /sapi/v1/userDataStream/isolated
  * DELETE /sapi/v1/userDataStream/isolated



## 2026-01-16[​](/docs/zh-CN/margin_trading/change-log#2026-01-16 "2026-01-16的直接链接")

  * 更新端点限制 
    * `GET /sapi/v1/margin/capital-flow`：新增查询时间范围限制。此限制将于大约 2026-02-02 07:00 UTC 起生效。
    * 当同时指定 `startTime` 和 `endTime` 时，时间跨度不能超过7天，否则接口将返回错误： 
          
          {  
            "code": -4047,  
            "msg": "Time interval must be within 0-7 days"  
          }  
          

    * 如果所需时间范围超过7天，请将查询拆分为多个请求。



## 2025-12-26[​](/docs/zh-CN/margin_trading/change-log#2025-12-26 "2025-12-26的直接链接")

**时效性通知**

  * **以下有关于REST API变更将在 2026-01-15 07:OO UTC 发生:**   
调用需要签名的接口时，请在计算签名之前对 payload 进行百分比编码（percent-encode）。不符合此顺序的请求将被拒绝，并返回错误代码 [`-1022 签名不正确`](/docs/zh-CN/margin_trading/error-code#-1022-invalid_signature)。请检查并相应地更新您代码中的签名逻辑部分。



**REST API**

  * 更新了 REST API 文档中有关于 [签名请求示例](/docs/zh-CN/margin_trading/general-info#post-apiv3order-%E7%9A%84%E7%AD%BE%E5%90%8D%E7%A4%BA%E4%BE%8B) 的部分。



## 2025-11-10[​](/docs/zh-CN/margin_trading/change-log#2025-11-10 "2025-11-10的直接链接")

  * **所有关于在 wss://stream.binance.com 上使用 listenKey 的文档于2025年11月10日从杠杆交易接口文档中移除。以下功能将持续可用，直至另行发布停用公告：**
    * POST /sapi/v1/userDataStream
    * PUT /sapi/v1/userDataStream
    * DELETE /sapi/v1/userDataStream
    * POST /sapi/v1/userDataStream/isolated
    * PUT /sapi/v1/userDataStream/isolated
    * DELETE /sapi/v1/userDataStream/isolated
  * **用户应通过订阅[WebSocket API](https://developers.binance.com/docs/zh-CN/margin_trading/trade-data-stream) 上的用户数据流来获取用户数据更新，这样可以提供更好的性能（更低的延迟）:**
    * POST /sapi/v1/userListenToken : 创建一个新的用户数据流并返回一个listenToken令牌。
    * 方法 userDataStream.subscribe.listenToken : 使用生成的listenToken订阅用户数据流。
  * [用户数据流文档](https://developers.binance.com/docs/zh-CN/margin_trading/trade-data-stream)将持续提供有效载荷的参考: 
    * 账户更新 : 每当帐户余额发生更改时，都会发送一个事件outboundAccountPosition，其中包含可能由生成余额变动的事件而变动的资产。
    * 余额更新 : 杠杆账户和其他账户之间发生划转时更新。
    * 订单更新 ： 订单通过executionReport事件进行更新。



## 2025-10-06[​](/docs/zh-CN/margin_trading/change-log#2025-10-06 "2025-10-06的直接链接")

  * **在 wss://stream.binance.com:9443 上使用 listenKey方式订阅用户数据流的功能即将弃用。**
    * 该功能将会在不久的将来从我们系统里移除，具体时间另行通知。
    * 相关文档也会随之全部删除.
    * 建议用户使用以下已经发布的新的用户数据流订阅方式。
  * 新的用户数据流订阅方式采用 [Websocket API](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/general-api-information) 连接方式，包含如下: 
    * POST /sapi/v1/userListenToken : 创建一个新的用户数据流并返回一个listenToken令牌。
    * 方法 userDataStream.subscribe.listenToken : 使用生成的listenToken订阅用户数据流。



## 2025-09-16[​](/docs/zh-CN/margin_trading/change-log#2025-09-16 "2025-09-16的直接链接")

  * 更新一个接口 : 
    * POST `/sapi/v1/margin/apiKey`: 接口描述增加可支持产品的详细说明，以及错误码说明。



## 2025-06-17[​](/docs/zh-CN/margin_trading/change-log#2025-06-17 "2025-06-17的直接链接")

  * 杠杆交易新增最佳实践模块。



## 2025-06-16[​](/docs/zh-CN/margin_trading/change-log#2025-06-16 "2025-06-16的直接链接")

  * 杠杆交易新增币种或币对预上架接口: 
    * GET `/sapi/v1/margin/list-schedule`: 查询全仓和逐仓的币种或币对的上架计划



## 2024-09-19[​](/docs/zh-CN/margin_trading/change-log#2024-09-19 "2024-09-19的直接链接")

  * 杠杆交易为VIP4及以上的用户提供了低延迟交易接口，这类接口通过特定的SpecialKey实现杠杆交易。

若您的VIP级别为3及以下，请联系您的VIP经理获取相关SpecialKey的使用许可标准。

关于SpecialKey的接口包含：

    * POST /sapi/v1/margin/apiKey
    * DELETE /sapi/v1/margin/apiKey
    * PUT /sapi/v1/margin/apiKey/ip
    * GET /sapi/v1/margin/apiKey
    * GET /sapi/v1/margin/api-key-list

## special API key使用步骤[​](/docs/zh-CN/margin_trading/change-log#special-api-key使用步骤 "special API key使用步骤的直接链接")

    1. 通过上述新建SAPI接口创建"margin trade only" 权限的key/secret对；

    2. 全仓杠杆无需传递symbol参数；

    3. 逐仓杠杆则用symbol参数指定特定交易对；

    4. 使用步骤#1生成的key/secret对进行杠杆交易，同时可用现货REST api (<https://api.binance.com/api/v3/>) 接口创建listenKey进行监听。




## 2024-09-13[​](/docs/zh-CN/margin_trading/change-log#2024-09-13 "2024-09-13的直接链接")

  * 我们将在杠杆市场开始推出新功能 One-Triggers-the-Other (OTO) 订单和 One-Triggers-a-One-Cancels-The-Other (OTOCO) 订单。 
    * POST `/sapi/v1/margin/order/oto`: One-Triggers-the-Other (OTO) 订单
    * POST `/sapi/v1/margin/order/otoco`: One-Triggers-a-One-Cancels-The-Other (OTOCO) 订单
  * 在全仓杠杆账户接口GET `/sapi/v1/margin/account`新增2个返回参数并替换原有参数'transferEnabled' ： 
    * transferInEnabled
    * transferOutEnabled



## 2024-01-09[​](/docs/zh-CN/margin_trading/change-log#2024-01-09 "2024-01-09的直接链接")

  * 根据[公告](https://www.binancezh.info/zh-CN/support/announcement/%E5%85%B3%E4%BA%8E%E5%B8%81%E5%AE%89%E6%9D%A0%E6%9D%86sapi%E7%AB%AF%E7%82%B9%E6%9B%B4%E6%96%B0%E7%9A%84%E5%85%AC%E5%91%8A-2024-03-31-a1868c686ce7448da8c3061a82a87b0c)，币安杠杆将于 2024 年 03 月 31 日 12:00（东八区时间）下架以下 SAPI 接口，请及时更换为对应替代接口:

    * 将下架`POST /sapi/v1/margin/transfer`，应替换为`POST /sapi/v1/asset/transfer`万能划转
    * 将下架`POST /sapi/v1/margin/isolated/transfer`，应替换为`POST /sapi/v1/asset/transfer`万能划转
    * 将下架`POST /sapi/v1/margin/loan`，应替换为`POST /sapi/v1/margin/borrow-repay`借还款接口（新增）
    * 将下架`POST /sapi/v1/margin/repay`，应替换为`POST /sapi/v1/margin/borrow-repay`借还款接口（新增）
    * 将下架`GET /sapi/v1/margin/isolated/transfer`，应替换为`GET /sapi/v1/margin/transfer`获取全仓杠杆划转历史
    * 将下架`GET /sapi/v1/margin/asset`，应替换为`GET /sapi/v1/margin/allAssets`
    * 将下架`GET /sapi/v1/margin/pair`，应替换为`GET /sapi/v1/margin/allPairs`
    * 将下架`GET /sapi/v1/margin/isolated/pair`，应替换为`GET /sapi/v1/margin/isolated/allPairs`
    * 将下架`GET /sapi/v1/margin/loan`，应替换为`GET /sapi/v1/margin/borrow-repay`
    * 将下架`GET /sapi/v1/margin/repay`，应替换为`GET /sapi/v1/margin/borrow-repay`
    * 将下架`GET /sapi/v1/margin/dribblet`，应替换为`GET /sapi/v1/asset/dribblet`
    * 将下架`GET /sapi/v1/margin/dust`，应替换为`POST /sapi/v1/asset/dust-btc`
    * 将下架`POST /sapi/v1/margin/dust`，应替换为`POST /sapi/v1/asset/dust`
  * 新增杠杆交易接口:

    * `POST /sapi/v1/margin/borrow-repay`：杠杆账户借贷/还款
    * `GET /sapi/v1/margin/borrow-repay`：查询借贷/还款记录
  * 更新 3 个杠杆交易接口:

    * `GET /sapi/v1/margin/transfer`：新增参数 `isolatedSymbol`，新增响应信息
    * `GET /sapi/v1/margin/allAssets`：新增参数`asset`，新增响应信息
    * `GET /sapi/v1/margin/allPairs`：新增参数`symbol`
    * `GET /sapi/v1/margin/isolated/allPairs`：新增参数`symbol`



* * *

## 2023-12-22[​](/docs/zh-CN/margin_trading/change-log#2023-12-22 "2023-12-22的直接链接")

  * 新增杠杆交易 Websocket： 
    * 新的 base url 为`wss://margin-stream.binance.com`，推送两类事件：负债变化事件和 Margin Call 事件



* * *

## 2023-11-21[​](/docs/zh-CN/margin_trading/change-log#2023-11-21 "2023-11-21的直接链接")

  * 更新杠杆接口 
    * `POST /sapi/v1/margin/order`: 参数`sideEffectType`增加`AUTO_BORROW_REPAY`选项
    * `POST /sapi/v1/margin/order/oco`: 参数`sideEffectType`增加`AUTO_BORROW_REPAY`选项
    * `GET /sapi/v1/margin/available-inventory`: 响应增加返回参数 updateTime ，表示放贷库存的获取时间



* * *

## 2023-11-17[​](/docs/zh-CN/margin_trading/change-log#2023-11-17 "2023-11-17的直接链接")

  * 新增杠杠接口支持全仓 Pro 模式[FAQ](https://www.binance.com/en/support/faq/introduction-to-binance-cross-margin-pro-0b5441a1c1ff431bb2e135dfa8e6ffba): 
    * `GET /sapi/v1/margin/leverageBracket`: 查询全仓杠杆 Pro 模式下的负债币种杠杆与保证金率
  * 更新杠杠接口: 
    * `POST /sapi/v1/margin/max-leverage`: 增加 `maxLeverage`入参 10 以支持全仓 Pro 模式
    * `GET /sapi/v1/margin/account`: 新增响应字段`accountType`, `MARGIN_2` 以支持全仓 Pro 模式



* * *

## 2023-10-16[​](/docs/zh-CN/margin_trading/change-log#2023-10-16 "2023-10-16的直接链接")

  * 新增杠杆接口: 
    * `GET /sapi/v1/margin/available-inventory`: 杠杆可用放贷库存查询
    * `POST /sapi/v1/margin/manual-liquidation`: 杠杆手动强平



* * *

## 2023-08-31[​](/docs/zh-CN/margin_trading/change-log#2023-08-31 "2023-08-31的直接链接")

  * 新增杠杆接口： 
    * `/sapi/v1/margin/capital-flow`: 查询全仓/逐仓资金流水



* * *

## 2023-07-07[​](/docs/zh-CN/margin_trading/change-log#2023-07-07 "2023-07-07的直接链接")

  * 新增杠杆接口： 
    * `POST /sapi/v1/margin/max-leverage`: 调整全仓最大杠杆倍数



* * *

## 2023-06-22[​](/docs/zh-CN/margin_trading/change-log#2023-06-22 "2023-06-22的直接链接")

  * 更新杠杆接口： 
    * `POST /sapi/v1/margin/order`：增加参数`autoRepayAtCancel`和 `selfTradePreventionMode`
    * `POST /sapi/v1/margin/order/oco`: 增加参数 `selfTradePreventionMode`



* * *

## 2023-06-20[​](/docs/zh-CN/margin_trading/change-log#2023-06-20 "2023-06-20的直接链接")

  * 新增杠杆接口： 
    * `GET /sapi/v1/margin/delist-schedule`：查询全仓和逐仓的币种或币对的下架计划



* * *

## 2023-02-27[​](/docs/zh-CN/margin_trading/change-log#2023-02-27 "2023-02-27的直接链接")

  * 新增杠杆接口: 
    * `/sapi/v1/margin/next-hourly-interest-rate`: 查询用户币种预估下小时利率



* * *

## 2023-02-02[​](/docs/zh-CN/margin_trading/change-log#2023-02-02 "2023-02-02的直接链接")

  * 添加杠杆接口: 
    * `GET /sapi/v1/margin/exchange-small-liability`: 查询可小额负债转换的资产
    * `POST /sapi/v1/margin/exchange-small-liability`: 全仓杠杆小额负债转换
    * `GET /sapi/v1/margin/exchange-small-liability-history`: 查询全仓杠杆小额负债转换历史



* * *

## 2023-01-13[​](/docs/zh-CN/margin_trading/change-log#2023-01-13 "2023-01-13的直接链接")

  * 添加杠杆账户接口： 
    * `GET /sapi/v1/margin/crossMarginCollateralRatio`: 获取全仓币种质押率信息



* * *

## 2022-09-16[​](/docs/zh-CN/margin_trading/change-log#2022-09-16 "2022-09-16的直接链接")

  * 添加杠杆账户接口： 
    * `GET /sapi/v1/margin/tradeCoeff`：获取用户个人杠杆账户信息汇总



* * *

## 2022-07-01[​](/docs/zh-CN/margin_trading/change-log#2022-07-01 "2022-07-01的直接链接")

  * 添加新杠杆账户接口：

    * `GET /sapi/v1/margin/dribblet` 查询用户杠杆账户小额资产转换 BNB 历史信息。
  * 更新杠杆账户接口：

    * `GET /sapi/v1/margin/repay`： 响应出参增加字段 rawAsset，表示原始币种。



* * *

## 2022-05-26[​](/docs/zh-CN/margin_trading/change-log#2022-05-26 "2022-05-26的直接链接")

  * 更新杠杆账户接口： 查询时间范围最大不得超过 30 天： 
    * `GET /sapi/v1/margin/transfer`
    * `GET /sapi/v1/margin/loan`
    * `GET /sapi/v1/margin/repay`
    * `GET /sapi/v1/margin/isolated/transfer`
    * `GET /sapi/v1/margin/interestHistory`



* * *

## 2022-04-26[​](/docs/zh-CN/margin_trading/change-log#2022-04-26 "2022-04-26的直接链接")

  * 新增接口 `GET /sapi/v1/margin/rateLimit/order`
    * 回传用户在当前时间区间内的杠杆账户下单总数



* * *

## 2021-12-30[​](/docs/zh-CN/margin_trading/change-log#2021-12-30 "2021-12-30的直接链接")

  * 更新杠杆接口： 
    * 获取杠杆利率历史接口`GET /sapi/v1/margin/interestRateHistory`移除参数`limit`，查询时间间隔更改为最大 1 个月



* * *

## 2021-12-03[​](/docs/zh-CN/margin_trading/change-log#2021-12-03 "2021-12-03的直接链接")

  * 新增杠杆接口: 
    * 新增接口 `GET /sapi/v1/margin/crossMarginData` 以获取全仓杠杆利率及限额
    * 新增接口 `GET /sapi/v1/margin/isolatedMarginData` 以获取逐仓杠杆利率及限额
    * 新增接口 `GET /sapi/v1/margin/isolatedMarginTier` 以获取逐仓档位信息



* * *

## 2021-10-14[​](/docs/zh-CN/margin_trading/change-log#2021-10-14 "2021-10-14的直接链接")

  * 以下杠杆账户接口更新返回数据的时间范围，`startTime`与`endTime`时间跨度不能超过 30 天，如果不传时间参数默认返回最近 7 天数据，如果`archived`参数为`true`，则默认返回 6 个月以前的最后 7 天数据: 
    * `GET /sapi/v1/margin/transfer`
    * `GET /sapi/v1/margin/loan`
    * `GET /sapi/v1/margin/repay`
    * `GET /sapi/v1/margin/isolated/transfer`
    * `GET /sapi/v1/margin/interestHistory`



* * *

## 2021-09-08[​](/docs/zh-CN/margin_trading/change-log#2021-09-08 "2021-09-08的直接链接")

  * 新增以下杠杆账户接口支持杠杆逐仓账户启用限制:

    * 新增接口 `DELETE /sapi/v1/margin/isolated/account` 以支持杠杆逐仓账户停用
    * 新增接口 `POST /sapi/v1/margin/isolated/account` 以支持杠杆逐仓账户启用
    * 新增接口 `GET /sapi/v1/margin/isolated/accountLimit` 以查询杠杆逐仓账户上限
  * 查询杠杆逐仓账户信息接口 `GET /sapi/v1/margin/isolated/account` 响应加入字段 "enabled" 判断账户是否启用




* * *

## 2021-08-23[​](/docs/zh-CN/margin_trading/change-log#2021-08-23 "2021-08-23的直接链接")

  * 新增杠杆账户 OCO 接口: 
    * `POST /sapi/v1/margin/order/oco`
    * `DELETE /sapi/v1/margin/orderList`
    * `GET /sapi/v1/margin/orderList`
    * `GET /sapi/v1/margin/allOrderList`
    * `GET /sapi/v1/margin/openOrderList`



用法与现货账户 OCO 相同

* * *

## 2021-04-28[​](/docs/zh-CN/margin_trading/change-log#2021-04-28 "2021-04-28的直接链接")

从 **May 15, 2021 08:00 UTC** 开始, 以下创建逐仓杠杆账户接口将关闭:

  * `POST /sapi/v1/margin/isolated/create`



后续，用户可通过逐仓杠杆账户划转 `POST /sapi/v1/margin/isolated/transfer` 直接完成逐仓杠杆账户的创建与交易准备，无需调用接口创建账户

* * *

## 2021-04-02[​](/docs/zh-CN/margin_trading/change-log#2021-04-02 "2021-04-02的直接链接")

  * 新增钱包接口: 
    * `GET /sapi/v1/system/status` 以获取系统状态
    * `GET /sapi/v1/account/status` 以获取账户状态
    * `GET /sapi/v1/account/apiTradingStatus` 以获取账户 API 交易状态
    * `GET /sapi/v1/asset/dribblet` 以获取小额资产转换 BNB 历史
    * `GET /sapi/v1/asset/assetDetail` 以获取上架资产详情
    * `GET /sapi/v1/asset/tradeFee` 以获取交易手续费率查询
  * 新增子母账户接口: 
    * `GET /sapi/v3/sub-account/assets` 以查询子账户资产



* * *

## 2021-03-05[​](/docs/zh-CN/margin_trading/change-log#2021-03-05 "2021-03-05的直接链接")

  * 新增杠杆接口： 
    * `GET /sapi/v1/margin/interestRateHistory` 以支持杠杆利率历史查询



* * *

## 2021-02-04[​](/docs/zh-CN/margin_trading/change-log#2021-02-04 "2021-02-04的直接链接")

  * 更新钱包接口： 
    * 用户万向划转接口 `POST /sapi/v1/asset/transfer` 和`GET /sapi/v1/asset/transfer` 新增划转类型 `MARGIN_MINING` ,`MINING_MARGIN`, `MARGIN_C2C` ,`C2C_MARGIN`, `MARGIN_CMFUTURE`, `CMFUTURE_MARGIN` 以支持全仓杠杆，矿池，C2C，币本位合约账户间划转。



* * *

## 2021-01-15[​](/docs/zh-CN/margin_trading/change-log#2021-01-15 "2021-01-15的直接链接")

  * 杠杆交易添加新接口 `DELETE /sapi/v1/margin/openOrders`
    * 此接口便于用户撤销单一交易对的所有挂单, 包括 OCO 的挂单。



* * *

## 2020-12-04[​](/docs/zh-CN/margin_trading/change-log#2020-12-04 "2020-12-04的直接链接")

  * 更新杠杆代币接口: 
    * 接口`GET /sapi/v1/blvt/tokenInfo` 新增返回参数 `currentBaskets`(包括 `symbol`， `amount` ， `notionalValue` )，`purchaseFeePct`申购费率，`dailyPurchaseLimit`每日申购数量上限，`redeemFeePct`赎回费率，`dailyRedeemLimit`每日赎回数量上限。
  * 新增杠杆代币接口: 
    * `GET /sapi/v1/blvt/userLimit` 以查询用户每日申购赎回限额。



* * *

## 2020-12-01[​](/docs/zh-CN/margin_trading/change-log#2020-12-01 "2020-12-01的直接链接")

  * 更新杠杆交易接口: 
    * `POST /sapi/v1/margin/order` 加入参数 `quoteOrderQty` 支持"报价总额市价单"。



* * *

## 2020-11-16[​](/docs/zh-CN/margin_trading/change-log#2020-11-16 "2020-11-16的直接链接")

  * 更新杠杆接口加入 `archived` 参数以支持查询 6 个月以前数据: 
    * `GET /sapi/v1/margin/loan`
    * `GET /sapi/v1/margin/repay`
    * `GET /sapi/v1/margin/interestHistory`



* * *

## 2020-11-10[​](/docs/zh-CN/margin_trading/change-log#2020-11-10 "2020-11-10的直接链接")

  * 新增 BNB 抵扣开关接口: 
    * `POST /sapi/v1/bnbBurn` BNB 现货交易和杠杆利息抵扣开关。
    * `GET /sapi/v1/bnbBurn` 获取 BNB 抵扣开关状态。



* * *

## 2020-09-30[​](/docs/zh-CN/margin_trading/change-log#2020-09-30 "2020-09-30的直接链接")

  * 杠杆账户接口更新: 
    * `GET /sapi/v1/margin/maxBorrowable` 返回新字段 `borrowLimit` 为用户账户借贷限额。



* * *

## 2020-08-26[​](/docs/zh-CN/margin_trading/change-log#2020-08-26 "2020-08-26的直接链接")

  * 逐仓杠杆接口 `GET /sapi/v1/margin/isolated/account` 新增可选参数 `symbols`, 以支持查询至多 5 个指定 symbol 的杠杆逐仓资产。



* * *

## 2020-07-28[​](/docs/zh-CN/margin_trading/change-log#2020-07-28 "2020-07-28的直接链接")

逐仓杠杆相关接口

  * 以下接口新增可选参数"isIsolated", 并在返回内容中新增字段 "symbol":

    * `POST /sapi/v1/margin/loan`
    * `POST /sapi/v1/margin/repay`
  * 以下接口新增可选参数"isIsolated", 并在返回内容中新增字段 "isIsolated":

    * `POST /sapi/v1/margin/order`
    * `DELETE /sapi/v1/margin/order`
    * `GET /sapi/v1/margin/order`
    * `GET /sapi/v1/margin/openOrders`
    * `GET /sapi/v1/margin/allOrders`
    * `GET /sapi/v1/margin/myTrades`
  * 以下接口新增可选参数"isolatedSymbol", 并在返回内容中新增字段 "isolatedSymbol":

    * `GET /sapi/v1/margin/loan`
    * `GET /sapi/v1/margin/repay`
    * `GET /sapi/v1/margin/interestHistory`
  * 接口 `GET /sapi/v1/margin/forceLiquidationRec` 新增可选参数"isolatedSymbol", 并在返回内容中新增字段 "isIsolated"

  * 以下接口新增可选参数"isolatedSymbol":

    * `GET /sapi/v1/margin/maxBorrowable`
    * `GET /sapi/v1/margin/maxTransferable`
  * 新增以下逐仓杠杆功能接口:

    * `POST /sapi/v1/margin/isolated/create`
    * `POST /sapi/v1/margin/isolated/transfer`
    * `GET /sapi/v1/margin/isolated/transfer`
    * `GET /sapi/v1/margin/isolated/account`
    * `GET /sapi/v1/margin/isolated/pair`
    * `GET /sapi/v1/margin/isolated/allPairs`
  * 新增以下接口，管理逐仓杠杆账户 listenKey:

    * `POST /sapi/v1/userDataStream/isolated`
    * `PUT /sapi/v1/userDataStream/isolated`
    * `DELETE /sapi/v1/userDataStream/isolated`



* * *

## 2020-07-20[​](/docs/zh-CN/margin_trading/change-log#2020-07-20 "2020-07-20的直接链接")

  * 接口`GET /sapi/v1/margin/allOrders` 参数"limit"的可传最大值更新为 500.



* * *

## 2020-07-17[​](/docs/zh-CN/margin_trading/change-log#2020-07-17 "2020-07-17的直接链接")

  * 接口 `GET /sapi/v1/margin/allOrders` 增加访问限制为每个 IP 最多每分钟 60 次



* * *

## 2019-11-30[​](/docs/zh-CN/margin_trading/change-log#2019-11-30 "2019-11-30的直接链接")

  * 接口`POST /sapi/v1/margin/order (HMAC SHA256)`新增参数`sideEffectType`，可选内容如下:

    * `NO_SIDE_EFFECT`: 普通交易订单;
    * `MARGIN_BUY`: 自动借款交易订单;
    * `AUTO_REPAY`: 自动还款交易订单.
  * New field `marginBuyBorrowAmount` and `marginBuyBorrowAsset` in `FULL` response to `POST /sapi/v1/margin/order (HMAC SHA256)`