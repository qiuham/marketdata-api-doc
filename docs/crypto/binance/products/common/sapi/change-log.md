---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/common/sapi/change-log
api_type: Changelog
updated_at: 2026-11-24 18:41:40.649066
---

# Change Log

## 2023-05-26

**Notice:** The change below are being rolled out, and will take approximately a week to complete.

- The following base endpoints may give better performance but have less stability than
  **https://api.binance.com**:
  - **https://api1.binance.com**
  - **https://api2.binance.com**
  - **https://api3.binance.com**
  - **https://api4.binance.com**

---

## 2023-05-24

- **The previous market data URLs have been deprecated. Please update your code immediately to
  prevent interruption of our services.**
  - API Market data from `data.binance.com` can now be accessed from `data-api.binance.vision`.
  - Websocket Market Data from `data-stream.binance.com` can now be accessed from
    `data-stream.binance.vision`.
- New endpoints for Classic Portfolio Margin:
  - `POST /sapi/v1/portfolio/auto-collection`: classic portfolio Margin fund collection
  - `POST /sapi/v1/portfolio/bnb-transfer`: classic portfolio margin BNB transfer
- `GET /sapi/v1/portfolio/interest-rate` has be deprecated, users can query the Classic Portfolio
  Margin Negative Balance Interest Rate by using `GET /sapi/v1/margin/interestRateHistory`.

---

## 2023-05-18

- New endpoints for Wallet：
  - `POST /sapi/v1/capital/deposit/credit-apply`: apply deposit credit for expired address

---

## 2023-05-09

- New endpoints for Portfolio Margin：
  - `GET /sapi/v1/portfolio/asset-index-price`: query portfolio margin asset index price
- Update endpoints for Wallet:
  - `POST /sapi/v1/asset/transfer`: add enum `MAIN_PORTFOLIO_MARGIN` and `PORTFOLIO_MARGIN_MAIN`

---

## 2023-04-20

- New endpoints for Sub-Account：
  - `GET /sapi/v1/managed-subaccount/deposit/address`: get managed sub-account deposit address
- Update endpoints for VIP Loans:
  - `GET /sapi/v1/loan/vip/ongoing/orders`: add fields `totalCollateralValueAfterHaircut` and
    `lockedCollateralValue`

---

## 2023-04-18

- New endpoints for Spot Algo：
  - `POST /sapi/v1/algo/spot/newOrderTwap` to support new order
  - `DELETE /sapi/v1/algo/spot/order` to support cancel Algo order
  - `GET /sapi/v1/algo/spot/openOrders` to support query Algo open orders
  - `GET /sapi/v1/algo/spot/historicalOrders` to support query Algo historical orders
  - `GET /sapi/v1/algo/spot/subOrders` to support query Algo sub orders for a specified algoId

---

## 2023-03-23

- Update endpoints for Sub-Account:
  - `GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`: Add response field `tranId`
  - `GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`: Add response field `tranId`
- New endpoints for Sub-Account:
  - `GET /sapi/v1/managed-subaccount/info`: query investor's managed sub-account list
  - `GET /sapi/v1/sub-account/transaction-statistics`: Query sub-account transaction tatistics

---

## 2023-03-13

**Notice:** All changes are being rolled out gradually to all our servers, and may take a week to
complete.

GENERAL CHANGES

- The error messages for certain issues have been improved for easier troubleshooting.

<table>
    <tr>
        <th>Situation</th>
        <th>Old Error Message</th>
        <th>New Error Message</th>
    </tr>
    <tr>
        <td>An account cannot place or cancel an order, due to trading ability disabled.</td>
        <td rowspan="3">This action is disabled on this account.</td>
        <td>This account may not place or cancel orders.</td>
    </tr>
    <tr>
        <td>When the permissions configured on the symbol do not match the permissions on the account.</td>
        <td>This symbol is not permitted for this account.</td>
    </tr>
    <tr>
        <td>When the account tries to place an order on a symbol it has no permissions for.</td>
        <td>This symbol is restricted for this account.</td>
    </tr>
    <tr>
        <td>Placing an order when <tt>symbol</tt> is not <tt>TRADING</tt>. </td>
        <td rowspan="2">Unsupported order combination.</td>
        <td>This order type is not possible in this trading phase.</td>
    </tr>
    <tr>
        <td>Placing an order with <tt>timeinForce</tt>=<tt>IOC</tt> or <tt>FOK</tt> on a trading phase that does not support it.</td>
        <td>Limit orders require GTC for this phase.</td>
    </tr>
</table>

- Fixed error message for querying archived orders:
  - Previously, If an archived order (i.e. order with status `CANCELED` or `EXPIRED` where
    `executedQty` == 0 that occurred more than 90 days in the past.) is queried, the error message
    would be:
    - `{"code": -2013,"msg": "Order does not exist."}`
  - Now, the error message is:
    - `{"code": -2026,"msg": "Order was canceled or expired with no executed qty over 90 days ago and has been archived."}`
- Behavior for API requests with `startTime` and `endTime`:
  - Previously some requests failed if the `startTime` == `endTime`.
  - Now, all API requests that accept `startTime` and `endTime` allow the parameters to be equal.
    This applies to the following requests:
    - Rest API
      - `GET /api/v3/aggTrades`
      - `GET /api/v3/klines`
      - `GET /api/v3/allOrderList`
      - `GET /api/v3/allOrders`
      - `GET /api/v3/myTrades`

The following changes will take effect **approximately a week from the release date**, but the rest
of the documentation has been updated to reflect the future changes:

- Changes to Filter Evaluation:
  - Previous behavior: `LOT_SIZE` and `MARKET_LOT_SIZE` required that (`quantity` - `minQty`) %
    `stepSize` == 0.
  - New behavior: This has now been changed to (`quantity` % `stepSize`) == 0.
- Bug fix with reverse `MARKET` orders (i.e., `MARKET` using `quoteOrderQty`):
  - Previous behavior: Reverse market orders would always have the status `FILLED` even if the order
    did not fully fill due to low liquidity.
  - New behavior: If the reverse market order did not fully fill due to low liquidity the order
    status will be `EXPIRED`, and `FILLED` only if the order was completely filled.

SPOT API

- Changes to `DELETE /api/v3/order` and `POST /api/v3/order/cancelReplace`:
  - A new optional parameter `cancelRestrictions` that determines whether the cancel will succeed if
    the order status is `NEW` or `PARTIALLY_FILLED`.
  - If the order cancellation fails due to `cancelRestrictions`, the error will be:
    - `{"code": -2011,"msg": "Order was not canceled due to cancel restrictions."}`

---

## 2023-02-27

- New endpoints for Margin:
  - `/sapi/v1/margin/next-hourly-interest-rate`: Get user the next hourly estimate interest
- New endpoints for Porfolio Margin:
  - `GET /sapi/v1/portfolio/interest-history`: get user's portfolio margin interest history
  - `GET /sapi/v1/portfolio/interest-rate`: get portfolio margin interest rate

---

## 2023-02-21

- Adjusted endpoints for Crypto Loan:
  - `POST /sapi/v1/loan/borrow`: paramater `loanTerm` is restricted to 7 or 30

---

## 2023-02-17

The Websocket Stream now only allows 300 connections requests every 5 minutes.

This limit is **per IP address**.

Please be careful when trying to open multiple connections or reconnecting to the Websocket API.

---

## 2023-02-13

- New endpoints for Sub-Account:
  - `GET /sapi/v4/sub-account/assets`: Fetch sub-account assets

---

## 2023-02-02

- New endpoints for Margin:
  - `GET /sapi/v1/margin/exchange-small-liability`: Query the coins which can be small liability
    exchange
  - `POST /sapi/v1/margin/exchange-small-liability`: Cross Margin Small Liability Exchange
  - `GET /sapi/v1/margin/exchange-small-liability-history`: Get Small liability Exchange History
- Update endpoints for Wallet:
  - Universal Transfer `POST /sapi/v1/asset/transfer` support option transfer

---

## 2023-01-26

As per the
[announcement](https://www.binance.com/en/support/announcement/binance-spot-launches-self-trade-prevention-stp-function-on-api-312fd0112fb44635b397c116e56d8f84),
Self Trade Prevention will be enabled at **2023-01-26 08:00 UTC**.

Please refer to `GET /api/v3/exchangeInfo` from the Rest API or `exchangeInfo` from the Websocket
API on the default and allowed modes.

---

## 2023-01-23

New API cluster has been added. Note that all endpoints are functionally equal, but may vary in
performance.

- https://api4.binance.com

---

## 2023-01-19

**ACTUAL RELEASE DATE TBD**

SPOT API

**New Feature**: Self-Trade Prevention (aka STP) will be added to the system at a later date. This
will prevent orders from matching with orders from the same account, or accounts under the same
`tradeGroupId`.

Please refer to `GET /api/v3/exchangeInfo` from the SPOT API or `exchangeInfo` from the Websocket
API on the status.

```javascript
"defaultSelfTradePreventionMode": "NONE",   //If selfTradePreventionMode not provided, this will be the value passed to the engine
"allowedSelfTradePreventionModes": [        //What the allowed modes of selfTradePrevention are
    "NONE",
    "EXPIRE_TAKER",
    "EXPIRE_BOTH",
    "EXPIRE_MAKER"
]
```

- New order status: `EXPIRED_IN_MATCH` - This means that the order expired due to STP being
  triggered.
- New endpoint:
  - `GET /api/v3/myPreventedMatches` - This queries the orders that expired due to STP being
    triggered.
- New optional parameter `selfTradePreventionMode` has been added to the following endpoints:
  - `POST /api/v3/order`
  - `POST /api/v3/order/oco`
  - `POST /api/v3/cancelReplace`
- New responses that will appear for all order placement endpoints if there was a prevented match
  (i.e. if an order could have matched with an order of the same account, or the accounts are in the
  same `tradeGroupId`):
  - `tradeGroupId` - This will only appear if account is configured to a `tradeGroupId` and if there
    was a prevented match.
  - `preventedQuantity` - Only appears if there was a prevented match.
  - An array `preventedMatches` with the following fields:
    - `preventedMatchId`
    - `makerOrderId`
    - `price`
    - `takerPreventedQuantity` - This will only appear if `selfTradePreventionMode` set is
      `EXPIRE_TAKER` or `EXPIRE_BOTH`.
    - `makerPreventedQuantity` - This will only appear if `selfTradePreventionMode` set is
      `EXPIRE_MAKER` or `EXPIRE_BOTH`.
- New fields `preventedMatchId` and `preventedQuantity` that can appear in the order query endpoints
  if the order had expired due to an STP trigger:
  - `GET /api/v3/order`
  - `GET /api/v3/openOrders`
  - `GET /api/v3/allOrders`

USER DATA STREAM

- New execution Type: `TRADE_PREVENTION`
- New fields for `executionReport` (These fields will only appear if the order has expired due to
  STP trigger)
  - `u` - `tradeGroupId`
  - `v` - `preventedMatchId`
  - `U` - `counterOrderId`
  - `A` - `preventedQuantity`
  - `B` - `lastPreventedQuantity`

---

## 2023-01-13

- The following endpoints will be discontinued on January 13, 2023 6:00 AM UTC:
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account enable and
    disable IP restriction for a sub-account API Key
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account add IP
    list for a sub-account API Key
- New endpoints for Sub-Account:
  - `GET /sapi/v1/managed-subaccount/fetch-future-asset`: Investor can use this api to query managed
    sub account futures asset details
  - `GET /sapi/v1/managed-subaccount/marginAsset`: Investor can use this api to query managed sub
    account margin asset details
- New endpoin for Margin:
  - `GET /sapi/v1/margin/crossMarginCollateralRatio`: Get cross margin collateral ratio

---

## 2023-01-05

- New endpoints for Sub-Account:
  - `GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`: Investor can use this api to query
    managed sub account transfer log
  - `GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`: Trading team can use this api to
    query managed sub account transfer log

---

## 2022-12-26

- New endpoints for wallet:
  - `GET /sapi/v1/capital/contract/convertible-coins`: Get a user's auto-conversion settings in
    deposit/withdrawal
  - `POST /sapi/v1/capital/contract/convertible-coins`: User can use it to turn on or turn off the
    BUSD auto-conversion from/to a specific stable coin.

---

## 2022-12-15

- New RSA signature
  - Documentation has been updated to show how to sign a request using an RSA key.
  - For security reasons, we recommend to use RSA keys instead of HMAC keys when generating an API
    key.
  - We accept `PKCS#8` (BEGIN PUBLIC KEY).
  - More details on how to upload your RSA public key will be added at a later date.

---

## 2022-12-13

REST API

Some error messages on error code `-1003` have changed:

- Previous error message:

`Too much request weight used; current limit is %s request weight per %s %s. Please use the websocket for live updates to avoid polling the API.`

has been updated to:

`Too much request weight used; current limit is %s request weight per %s. Please use WebSocket Streams for live updates to avoid polling the API.`

- Previous error message

`Way too much request weight used; IP banned until %s. Please use the websocket for live updates to avoid bans.`

has been updated to:

`Way too much request weight used; IP banned until %s. Please use WebSocket Streams for live updates to avoid bans.`

---

## 2022-12-05

**Notice:** These changes are being rolled out gradually to all our servers, and will take
approximately a week to complete.

WEBSOCKET

- `!bookTicker` will be removed by **December 7, 2022**. Please use the Individual Book Ticker
  Streams instead. (&lt;symbol&gt;@bookTicker).
  - Multiple &lt;symbol&gt;@bookTicker streams can be subscribed to over one connection. (E.g.
    `wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker/bnbbtc@bookTicker`)

SPOT API

- New error code `-1135`
  - This error code will occur if a parameter requiring a JSON object is invalid.
- New error code `-1108`
  - This error will occur if a value to a parameter being sent was too large, potentially causing
    overflow.
  - This error code can occur in the following endpoints:
    - `POST /api/v3/order`
    - `POST /api/v3/order/cancelReplace`
    - `POST /api/v3/order/oco`
- Changes to `GET /api/v3/aggTrades`
  - Previous behavior: `startTime` and `endTime` had to be used in combination and could only be an
    hour apart.
  - New behavior: `startTime` and `endTime` can be used individually and the 1 hour limit has been
    removed.
    - When using `startTime` only, this will return trades from that time, up to the `limit`
      provided.
    - When using `endTime` only, this will return trades starting from the `endTime` including all
      trades before that time, up to the limit provided.
    - If `limit` not provided, regardless of used in combination or sent individually, the endpoint
      will use the default limit.
- Changes to `GET /api/v3/myTrades`
  - Fixed a bug where `symbol` + `orderId` combination would return all trades even if the number of
    trades went beyond the `500` default limit.
  - Previous behavior: The API would send specific error messages depending on the combination of
    parameters sent. E.g:

    `   {     "code": -1106,     "msg": "Parameter X was sent when not required."   }   `

  - New behavior: If the combinations of optional parameters to the endpoint were not supported,
    then the endpoint will respond with the generic error:

    `   {     "code": -1128,     "msg": "Combination of optional parameters invalid."   }   `

  - Added a new combination of supported parameters: `symbol` + `orderId` + `fromId`.
  - The following combinations of parameters were previously supported but no longer accepted, as
    these combinations were only taking `fromId` into consideration, ignoring `startTime` and
    `endTime`:
    - `symbol` + `fromId` + `startTime`
    - `symbol` + `fromId` + `endTime`
    - `symbol` + `fromId` + `startTime` + `endTime`
  - Thus, these are the supported combinations of parameters:
    - `symbol`
    - `symbol` + `orderId`
    - `symbol` + `startTime`
    - `symbol` + `endTime`
    - `symbol` + `fromId`
    - `symbol` + `startTime` + `endTime`
    - `symbol`+ `orderId` + `fromId`

**Note:** These new fields will appear approximately a week from the release date.

- Changes to `GET /api/v3/exchangeInfo`
  - New fields `defaultSelfTradePreventionMode` and `allowedSelfTradePreventionModes`
- Changes to the Order Placement Endpoints/Order Query/Order Cancellation Endpoints:
  - New field `selfTradePreventionMode` will appear in the response.
  - Affects the following endpoints:
    - `POST /api/v3/order`
    - `POST /api/v3/order/oco`
    - `POST /api/v3/order/cancelReplace`
    - `GET /api/v3/order`
    - `DELETE /api/v3/order`
    - `DELETE /api/v3/orderList`
- Changes to `GET /api/v3/account`
  - New field `requireSelfTradePrevention` will appear in the response.
- New field `workingTime`, indicating when the order started working on the order book, will appear
  in the following endpoints:
  - `POST /api/v3/order`
  - `GET /api/v3/order`
  - `POST /api/v3/order/cancelReplace`
  - `POST /api/v3/order/oco`
  - `GET /api/v3/order`
  - `GET /api/v3/openOrders`
  - `GET /api/v3/allOrders`
- Field `trailingTime`, indicating the time when the trailing order is active and tracking price
  changes, will appear for the following order types (`TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`,
  `STOP_LOSS`, `STOP_LOSS_LIMIT` if `trailingDelta` parameter was provided) for the following
  endpoints:
  - `POST /api/v3/order`
  - `GET /api/v3/order`
  - `GET /api/v3/openOrders`
  - `GET /api/v3/allOrders`
  - `POST /api/v3/order/cancelReplace`
  - `DELETE /api/v3/order`
- Field `commissionRates` will appear in the `GET /api/v3/acccount` response

USER DATA STREAM

- eventType `executionReport` has new fields
  - `V` - `selfTradePreventionMode`
  - `D` - `trailing_time` (Appears if the trailing stop order is active)
  - `W` - `workingTime` (Appears if `isWorking`=`true`)

---

## 2022-12-02

- Added a new market data base URL `https://data.binance.com`.
- Added a new WebSocket URL `wss://data-stream.binance.com`.

---

## 2022-11-29

- New endpoint for VIP Loan:
  - `GET /sapi/v1/loan/vip/collateral/account: Check Locked Value of VIP Collateral Account

---

## 2022-11-22

- New endpoints for Convert:
  - `GET /sapi/v1/convert/exchangeInfo`: Query for all convertible token pairs and the tokens’
    respective upper/lower limits
  - `GET /sapi/v1/convert/assetInfo`: Query for supported asset’s precision information
  - `POST /sapi/v1/convert/getQuote`: Request a quote for the requested token pairs
  - `POST /sapi/v1/convert/acceptQuote`: Accept the offered quote by quote ID.
  - `GET /sapi/v1/convert/orderStatus`: Query order status by order ID.

---

## 2022-11-18

- New endpoint for Wallet:
  - `GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage`: The query of Cloud-Mining payment
    and refund history
- New endpoints for Sub-account:
  - `GET /sapi/v1/sub-account/apiRestrictions/ipRestriction/thirdPartyList`: To query Sub-Account
    API key Third Party IP whitelist
  - `POST /sapi/v2/sub-account/subAccountApi/ipRestriction`: To support master account update IP
    Restriction for Sub-Account API key

---

## 2022-11-14

- New endpoints for VIP Loan:
  - `GET /sapi/v1/loan/vip/ongoing/orders`: Get VIP Loan Ongoing Orders
  - `POST /sapi/v1/loan/vip/repay`: VIP Loan Repay
  - `GET /sapi/v1/loan/vip/repay/history`: Get VIP Loan Repayment History

---

## 2022-11-02

- Update endpoints for Wallet:
  - `POST /sapi/v1/capital/withdraw/apply`: Weight changed to Weight(UID): 600

---

## 2022-11-01

- New endpoints for Crypto Loan:
  - `GET /sapi/v1/loan/loanable/data`: Get interest rate and borrow limit of loanable assets. The
    borrow limit is shown in USD value.
  - `GET /sapi/v1/loan/collateral/data`: Get LTV information and collateral limit of collateral
    assets. The collateral limit is shown in USD value.
  - `GET /sapi/v1/loan/repay/collateral/rate`: Get the rate of collateral coin / loan coin when
    using collateral repay, the rate will be valid within 8 second.
  - `POST /sapi/v1/loan/customize/margin_call`: Customize margin call for ongoing orders only.

---

## 2022-10-28

- Update endpoints for Wallet:
  - `POST /sapi/v1/asset/convert-transfer`: New parameter `accountType`
  - `POST /sapi/v1/asset/convert-transfer/queryByPage`: request method is changed to `GET`, new
    parameter `clientTranId`

---

## 2022-10-15

- New endpoints for Binance Code:
  - `POST /sapi/v1/giftcard/buyCode`: For buying a fixed-value Binance Code.
  - `GET /sapi/v1/giftcard/buyCode/token-limit`: To verify which tokens are available for you to
    purchase fixed-value gift cards as mentioned in section 2 and its’ limitation.

---

## 2022-09-30

- Delete endpoints for Futures Cross Collateral:
  - `POST /sapi/v1/futures/loan/borrow`
  - `POST /sapi/v1/futures/loan/repay`
  - `GET /sapi/v1/futures/loan/configs`
  - `GET /sapi/v2/futures/loan/configs`
  - `GET /sapi/v1/futures/loan/calcAdjustLevel`
  - `GET /sapi/v2/futures/loan/calcAdjustLevel`
  - `GET /sapi/v1/futures/loan/calcMaxAdjustAmount`
  - `GET /sapi/v2/futures/loan/calcMaxAdjustAmount`
  - `POST /sapi/v1/futures/loan/adjustCollateral`
  - `POST /sapi/v2/futures/loan/adjustCollateral`
  - `GET /sapi/v1/futures/loan/collateralRepayLimit`
  - `GET /sapi/v1/futures/loan/collateralRepay`
  - `POST /sapi/v1/futures/loan/collateralRepay`
  - `GET /sapi/v1/futures/loan/collateralRepayResult`

---

## 2022-09-30

Scheduled changes to the removal of `!bookTicker` around November 2022.

- The All Book Tickers stream (`!bookTicker`) is set to be removed in **November 2022**
- More details of the actual removal date will be announced at a later time.
- Please use the Individual Book Ticker Streams instead. (`<symbol>@bookTicker`).
- Multiple `<symbol>@bookTicker` streams can be subscribed to over one connection.
  - Example: wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker/bnbbtc@bookTicker

---

## 2022-09-29

- New endpoints for Wallet:
  - `POST /sapi/v1/asset/convert-transfer`: Convert transfer, convert between BUSD and stablecoins.
  - `POST /sapi/v1/asset/convert-transfer/queryByPage`: Query convert transfer

---

## 2022-09-22

- Update endpoint for Sub-Account:
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction`: Add new param `thirdParty`
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`: Add new param `thirdPartyName`
  - `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`: Add new param `thirdPartyName`
- Add Rate Limit for following endpoints:
  - `GET /sapi/v1/bswap/liquidity`: 3/1s per account and per pool
  - `GET /sapi/v1/bswap/quote`: 3/1s per account and per pool
  - `POST /sapi/v1/lending/daily/purchase`: 1/3s per account
  - `POST /sapi/v1/lending/customizedFixed/purchase`: 1/3s per account
  - `POST /sapi/v1/staking/purchase`: 1/3s per account

---

## 2022-09-16

- New endpoint for Margin：
  - `GET /sapi/v1/margin/tradeCoeff`: Get personal margin level information

---

## 2022-09-15

- New endpoints for Crypto Loan
  - `POST /sapi/v1/loan/borrow`: Borrow - Crypto Loan Borrow
  - `GET /sapi/v1/loan/borrow/history`: Borrow - Get Loan Borrow History
  - `GET/sapi/v1/loan/ongoing/orders`: Borrow - Get Loan Ongoing Orders
  - `POST/sapi/v1/loan/repay`: Repay - Crypto Loan Repay
  - `GET/sapi/v1/loan/repay/history`: Repay - Get Loan Repayment History
  - `POST/sapi/v1/loan/adjust/ltv`: Adjust LTV - Crypto Loan Adjust LTV
  - `GET/sapi/v1/loan/ltv/adjustment/history`: Adjust LTV - Get Loan LTV Adjustment History

---

## 2022-09-15

Note that these are rolling changes, so it may take a few days for it to rollout to all our servers.

- Changes to `GET /api/v3/exchangeInfo`
  - New optional parameter `permissions` added to display all symbols with the permissions matching
    the parameter provided. (eg.`SPOT`, `MARGIN`, `LEVERAGED`)
  - If not provided, the default value will be `["SPOT","MARGIN", "LEVERAGED"]`.
    - This means the request `GET /api/v3/exchangeInfo` without any parameters will show all symbols
      that can be used for `SPOT`,`MARGIN` and/or `LEVERAGED` trading.
    - To search for symbols that can be traded on other permissions (e.g. `TRD_GRP_004`, etc), then
      this needs to be searched for explicitly. (e.g.`permissions`=`TRD_GRP_004`)
  - Cannot be combined with `symbol` or `symbols`

---

## 2022-09-12

- Update endpoint for Sub-account: \* `GET /sapi/v1/sub-account/subAccountApi/ipRestriction`: To
  support master account query Third party IP list name for a sub account API key

---

## 2022-09-05

- Delete endpoint for Futures:
  - `GET /sapi/v1/futures/loan/wallet`

---

## 2022-08-23

SPOT API

Note that these are rolling changes, so it may take a few days for it to rollout to all our servers.

- Changes to `GET /api/v3/ticker` and `GET /api/v3/ticker/24hr`
  - New optional parameter `type` added
  - Supported values for parameter `type` are `FULL` and `MINI`
    - `FULL` is the default value and the response that is currently being returned from the
      endpoint
    - `MINI` omits the following fields from the response: `priceChangePercent`, `weightedAvgPrice`,
      `bidPrice`, `bidQty`, `askPrice`, `askQty`, and `lastQty`
- New error code `-1008`
  - This is sent whenever the servers are overloaded with requests.
  - This error code only appears for the SPOT API.
- New field `brokered` has been added to `GET /api/v3/account`
- New endpoint: `GET /api/v3/uiKlines`
- New kline interval: `1s`

---

## 2022-08-18

- Update endpoint for Convert:
  - `GET /sapi/v1/convert/tradeFlow`: Update weight from Weight(IP) 3000 to Weight(UID) 3000.

---

## 2022-08-08

SPOT API

- Changes to `POST /api/v3/order` and `POST /api/v3/order/cancelReplace`
  - New optional field `strategyId` is a parameter used to identify an order as part of a strategy.
  - New optional field `strategyType` is a parameter used to identify what strategy was running.
    (E.g. If all the orders are part of spot grid strategy, it can be set to `strategyType=1000000`)
  - **Note:** `strategyType` cannot be less than `1000000`.
- Changes to `POST /api/v3/order/oco`
  - New optional fields `limitStrategyId`, `limitStrategyType`. `stopStrategyId`, `stopStrategyType`
  - These are the strategy metadata parameters for both legs of the OCO orders.
  - `limitStrategyType` and `stopStrategyType` both cannot be less than `1000000`.
- Changes to `GET /api/v3/order`, `GET /api/v3/openOrders`, and `GET /api/v3/allOrders`
  - New fields `strategyId` and `strategyType` will appear in the response JSON for orders that had
    these fields populated upon order placement.
- Changes to `DELETE /api/v3/order` and `DELETE /api/v3/openOrders`
  - New fields `strategyId` and `strategyType` will appear in the response JSON for cancelled orders
    that had these fields populated upon order placement.

USER DATA STREAM

- New fields to eventType `executionReport`
  - `j` for `strategyId`
  - `J` for `strategyType`
  - Note that these fields only appear if these were populated upon order placement.

---

## 2022-08-05

- Update endpoint for Convert:
  - `GET /sapi/v1/convert/tradeFlow`: Update weight from Weight(IP) 100 to Weight(IP) 3000.

---

## 2022-07-21

- New endpoint for Portfolio Margin:
  - `GET /sapi/v1/portfolio/pmLoan` Query Portfolio Margin Bankruptcy Loan Record
  - `POST /sapi/v1/portfolio/repay` Portfolio Margin Bankruptcy Loan Repay

---

## 2022-07-18

- New endpoint for Portfolio Margin:
  - `GET /sapi/v1/portfolio/collateralRate` to get Portfolio Margin Collateral Rate.

---

## 2022-07-01

- New endpoint for Wallet:
  - `POST /sapi/v3/asset/getUserAsset` to get user assets.
- New endpoint for Margin:
  - `GET /sapi/v1/margin/dribblet` to query the historical information of user's margin account
    small-value asset conversion BNB.
- Update endpoint for Convert:
  - `GET /sapi/v1/convert/tradeFlow`: Update weight from 3000 to 100.
- Update endpoint for Margin:
  - `GET /sapi/v1/margin/repay`: Add response field rawAsset.

---

## 2022-06-20

SPOT API: Changes to `GET /api/v3/ticker`

- Weight has been reduced from 5 to 2 per symbol, regardless of `windowSize`.
- The max number of symbols that can be processed in a request is 100.
  - If the number of `symbols` sent is more than 100, the error will be as follows:

```json
{
  "code": -1101,
  "msg": "Too many values sent for parameter 'symbols', maximum allowed up to 100."
}
```

- The max Weight(IP) for this endpoint will cap at 100.
  - I.e. If the request has more than 50 symbols, the Weight will still be 100, regardless of
    `windowSize`.

---

## 2022-06-15

**Note:** The update is being rolled out over the next few days, so these changes may not be visible
right away.

- `GET /api/v3/ticker` added
  - Rolling window price change statistics based on `windowSize` provided.
  - Contrary to `GET /api/v3/ticker/24hr` the list of symbols cannot be omitted.
  - If `windowSize` not specified, the value will default to `1d`.
  - Response is similar to `GET /api/v3/ticker/24hr`, minus the following fields: `prevClosePrice`,
    `lastQty`, `bidPrice`, `bidQty`, `askPrice`, `askQty`
- `POST /api/v3/order/cancelReplace` added
  - Cancels an existing order and places a new order on the same symbol.
  - The filters are evaluated **before** the cancel order is placed.
    - e.g. If the `MAX_NUM_ORDERS` filter is 10, and the total number of open orders on the account
      is also 10, when using `POST /api/v3/order/cancelReplace` both the cancel order placement and
      new order will fail because of the filter.
  - The change is being rolled out in the next few days, thus this feature will be enabled once the
    upgrade is completed.
- `GET /api/v3/exchangeInfo` returns new field `cancelReplaceAllowed` in `symbols` list.
- New filter `NOTIONAL` has been added.
  - Defines the allowed notional value (`price * quantity`) based on a configured `minNotional` and
    `maxNotional`
- New exchange filter `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` has been added.
  - Defines the limit of open iceberg orders on an account

WEBSOCKETS

- New symbol ticker streams with 1h and 4h windows:
  - Individual symbol ticker streams
    - `<symbol>@ticker_<window-size>`
  - All market ticker streams
    - `!ticker_<window-size>@arr`

---

## 2022-06-02

- Update endpoint for Subaccount:
  - `GET /sapi/v1/sub-account/sub/transfer/history`: fromEmail and toEmail can be master email.

---

## 2022-05-31

- Update endpoint for Fiat:
  - `GET /sapi/v1/fiat/orders`: Weight changes from UID(3000) to UID(90000)
- Update endpoint for Pay:
  - `GET /sapi/v1/pay/transactions`: Param names changed: startTimestamp -> startTime; endTimestamp
    -> endTime.

---

## 2022-05-26

- Update endpoint for Fiat:
  - `GET /sapi/v1/fiat/orders`: Weight changes from IP(1) to UID(3000)
- Update info for the following margin account endpoints: The max interval between `startTime` and
  `endTime` is 30 days.:
  - `GET /sapi/v1/margin/transfer`
  - `GET /sapi/v1/margin/loan`
  - `GET /sapi/v1/margin/repay`
  - `GET /sapi/v1/margin/isolated/transfer`
  - `GET /sapi/v1/margin/interestHistory`

---

## 2022-05-23

- Changes to Order Book Depth Levels
  - Quantities in the Depth levels were returning negative values in situations where they were
    exceeding the max value, resulting in an overflow.
  - Going forward depth levels will not overflow, but will be capped at the max value based on the
    precision of the base asset. This means that the depth level is at max value _or more_.
    - E.g. If the precision is 8, then the max value for quantity will be at
      92,233,720,368.54775807.
  - When the fix has been applied, a change in the order book at the affected price level is
    required for the changes to be visible.
- What does this affect?
  - SPOT API
    - `GET /api/v3/depth`
  - Websocket Streams
    - `<symbol>@depth`
    - `<symbol>@depth@100ms`
    - `<symbol>@depth<levels>`
    - `<symbol>@depth<levels>@100ms`

- Updates to `MAX_POSITION`
  - If an order's `quantity` can cause the position to overflow, this will now fail the
    `MAX_POSITION` filter.

---

## 2022-05-19

- Update endpoint for Mining:
  - `GET /sapi/v1/mining/pub/algoList` and `GET /sapi/v1/mining/pub/coinList`: Need no parameter.
- Add error codes (21xxx) for Portfolio Margin Account: -21001, -21002, -21003

---

## 2022-05-17

SPOT API

- Changes to `GET api/v3/aggTrades`
  - When providing `startTime` and `endTime`, the oldest items are returned.
- Changed error messaging on `GET /api/v3/myTrades` where parameter `symbol` is not provided:

```json
{
  "code": -1102,
  "msg": "Mandatory parameter 'symbol' was not sent, was empty/null, or malformed."
}
```

- The following endpoints now support multi-symbol querying using the parameter `symbols`.
  - `GET /api/v3/ticker/24hr`
  - `GET /api/v3/ticker/price`
  - `GET /api/v3/ticker/bookTicker`
- In the above, the request weight will depend on the number of symbols provided in `symbols`.
  <br></br> Please refer to the table below:

| Endpoint                        | Number of Symbols | Weight |
| ------------------------------- | ----------------- | ------ |
| `GET /api/v3/ticker/price`      | Any               | 2      |
| `GET /api/v3/ticker/bookTicker` | Any               | 2      |
| `GET /api/v3/ticker/24hr`       | 1-20              | 1      |
| `GET /api/v3/ticker/24hr`       | 21-100            | 20     |
| `GET /api/v3/ticker/24hr`       | 101 or more       | 40     |

---

## 2022-05-05

- New endpoint for Binance Code:
  - `GET /sapi/v1/giftcard/cryptography/rsa-public-key` to fetch RSA public key.
- Update endpoint for Binance Code:
  - `POST /sapi/v1/giftcard/redeemCode`: new optional parameter `externalUid`. Each external unique
    ID represents a unique user on the partner platform. The function helps you to identify the
    redemption behavior of different users.

---

## 2022-04-28

- New endpoints for Staking:
  - `GET /sapi/v1/staking/productList` to get Staking product list
  - `POST /sapi/v1/staking/purchase` to stake product
  - `POST /sapi/v1/staking/redeem` to redeem product
  - `GET /sapi/v1/staking/position` to get Staking product holding position
  - `GET /sapi/v1/staking/stakingRecord` to inquiry Staking history records
  - `POST /sapi/v1/staking/setAutoStaking` to set Auto Staking function
  - `GET /sapi/v1/staking/personalLeftQuota` to inquiry Staking left quota

---

## 2022-04-27

- New endpoint for Futures Algo：
  - `POST /sapi/v1/algo/futures/newOrderTwap` to support Twap new order

FAQ:
[Time-Weighted Average Price(Twap) Introduction](https://www.binance.com/en/support/faq/093927599fd54fd48857237f6ebec0b0)

---

## 2022-04-26

- `GET /sapi/v1/margin/rateLimit/order` added
  - The endpoint will display the user's current margin order count usage for all intervals.

---

## 2022-04-20

- New endpoint for Portfolio Margin:
  - `GET /sapi/v1/portfolio/account` to support query portfolio margin account info

FAQ:
[Portfolio Margin Program](https://www.binance.com/en/support/faq/5054378212d240cca17ecd6006c11f23)

Only Portfolio Margin Account is accessible to this endpoint. To enroll, kindly refer to:
[How to Enroll into the Binance Portfolio Margin Program](https://www.binance.com/en/support/faq/a7834b9bc03140728583a90bcb469144)

---

## 2022-04-13

- New endpoints for Futures Algo：
  - `POST /sapi/v1/algo/futures/newOrderVp` to support VP new order
  - `DELETE  /sapi/v1/algo/futures/order` to support cancel Algo order
  - `GET  /sapi/v1/algo/futures/openOrders` to support query Algo open orders
  - `GET  /sapi/v1/algo/futures/historicalOrders` to support query Algo historical orders
  - `GET  /sapi/v1/algo/futures/subOrders` to support query Algo sub orders for a specified algoId

FAQ:
[Volume Participation(VP) Introduction](https://www.binance.com/en/support/faq/b0b94dcc8eb64c2585763b8747b60702)

---

## 2022-04-13

**Information on Trailing Stops**

SPOT API

- Trailing Stops have been enabled.
  - This is a type of algo order where the activation is based on a percentage of a price change in
    the market using the new parameter `trailingDelta`.
  - This can only used with any of the following order types: `STOP_LOSS`, `STOP_LOSS_LIMIT`,
    `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.
  - The `trailingDelta` parameter will be done in Basis Points or BIPS.
    - For example: a STOP_LOSS SELL order with a `trailingDelta` of 100 will trigger after a price
      decrease of 1%. (100 / 10,000 => 0.01 => 1%)
  - When used in combination with OCO Orders, the `trailingDelta` will determine when the contingent
    leg of the OCO will trigger.
  - When `trailingDelta` is used in combination with `stopPrice`, once the `stopPrice` condition is
    met, the trailing stop starts tracking the price change from the `stopPrice` based on the
    `trailingDelta` provided.
  - When no `stopPrice` is sent, the trailing stop starts tracking the price changes from the last
    price based on the `trailingDelta` provided.
- Changes to POST `/api/v3/order`
  - New optional field `trailingDelta`
- Changes to POST `/api/v3/order/test`
  - New optional field `trailingDelta`
- Changes to POST `/api/v3/order/oco`
  - New optional field `trailingDelta`
- A new filter `TRAILING_DELTA` has been added.
  - This filter is defined by the minimum and maximum values for the `trailingDelta` value.

USER DATA STREAM

- New field in `executionReport`
  - "d" for `trailingDelta`

---

## 2022-04-12

**Note:** The changes are being rolled out during the next few days, so these will not appear right
away.

- Error message changed on `GET api/v3/allOrders` where `symbol` is not provided: <br></br>
  ```
  {
   "code": -1102,
   "msg": "Mandatory parameter 'symbol' was not sent, was empty/null, or malformed."
  }
  ```
- Fixed a typo with an error message when an account has disabled permissions (e.g. to withdraw, to
  trade, etc) <br></br>
  ```
  "This action is disabled on this account."
  ```
- During a market data audit, we detected some issues with the Spot aggregate trade data.
  - Missing aggregate trades were recovered.
  - Duplicated records were marked invalid with the following values:
    - p = '0' // price
    - q = '0' // qty
    - f = -1 // ﬁrst_trade_id
    - l = -1 // last_trade_id

---

## 2022-04-08

- Update WEBSOCKET for BLVT：\* Base url changed to `wss://nbstream.binance.com/lvt-p` for BLVT
  streams `<tokenName>@tokenNav` and `<tokenName>@nav_Kline_<interval>`

---

## 2022-3-29

The following updates will take effect on **March 31, 2022 08:00 AM UTC**

- Update endpoint for Sub-account：
  - `GET /sapi/v1/sub-account/universalTransfer`

The query time period must be less then 30 days; If `startTime` and `endTime` not sent, return
records of the last 30 days by default

---

## 2022-03-25

- Update endpoint for Sub-Account:
  - New endpoint`GET /sapi/v1/managed-subaccount/accountSnapshot` to support investor master account
    query asset snapshot of managed sub-account

---

## 2022-03-08

- Update endpoint for Sub-Account:
  - New transfer types`MARGIN`,`ISOLATED_MARGIN` and parameter`symbol`added
    in`POST /sapi/v1/sub-account/universalTransfer` to support transfer to sub-account cross margin
    account and isolated margin account

---

## 2022-02-28

- New field `allowTrailingStop` has been added to `GET /api/v3/exchangeInfo`

---

## 2022-02-22

SPOT API

- `(price-minPrice) % tickSize == 0` rule in `PRICE_FILTER` has been changed to
  `price % tickSize == 0`.
- A new filter `PERCENT_PRICE_BY_SIDE` has been added.
- Changes to GET `api/v3/depth`
  - The `limit` value can be outside of the previous values (i.e. 5, 10, 20, 50, 100, 500,
    1000,5000) and will return the correct limit. (i.e. if limit=3 then the response will be the top
    3 bids and asks)
  - The limit still cannot exceed 5000. If the limit provided is greater than 5000, then the
    response will be truncated to 5000.
  - Due to the changes, these are the updated request weights based on the limit value provided:

| Limit     | Request Weight |
| --------- | -------------- |
| 1-100     | 1              |
| 101-500   | 5              |
| 501-1000  | 10             |
| 1001-5000 | 50             |

- Changes to GET `api/v3/aggTrades`
  - When providing `startTime` and `endTime`, the oldest items are returned.

---

## 2022-2-18

- Update endpoint for Sub-Account:
  - New fields `isManagedSubAccount`and `isAssetManagementSubAccount` added
    in`GET /sapi/v1/sub-account/list`to support query whether the sub-account is a managed
    sub-account or a asset management sub-account

---

## 2022-2-17

The following updates will take effect on **February 24, 2022 08:00 AM UTC**

- Update endpoint for Wallet：
  - `GET /sapi/v1/accountSnapshot`

The time limit of this endpoint is shortened to only support querying the data of the latest month

---

## 2022-2-09

- New endpoint for Wallet:
  - `POST /sapi/v1/asset/dust-btc` to get assets that can be converted into BNB

---

## 2022-1-25

- From **January 28, 2022 4:00 AM UTC**, You need to open`Enable Spot & Margin Trading`permission
  for the API key which requests these endpoints as following：
  - `POST /sapi/v1/asset/dust` Dust transfer
  - `POST /sapi/v1/lending/daily/purchase` Purchase Savings flexible product
  - `POST /sapi/v1/lending/daily/redeem` Redeem Savings flexible product
  - `POST /sapi/v1/lending/customizedFixed/purchase` Purchase Savings Fixed/Activity project
  - `POST /sapi/v1/lending/positionChanged` Change Savings Fixed/Activity position to Daily position
  - `POST /sapi/v1/bswap/liquidityAdd` Bswap add liquidity
  - `POST /sapi/v1/bswap/liquidityRemove` Bswap remove liquidity
  - `POST /sapi/v1/bswap/swap` Bswap swap
  - `POST /sapi/v1/bswap/claimRewards` Bswap claim rewards

---

## 2022-1-21

- New endpoints for Binance Code:
  - `POST /sapi/v1/giftcard/createCode` to create a Binance Code.
  - `POST /sapi/v1/giftcard/redeemCode` to redeem a Binance Code.
  - `GET /sapi/v1/giftcard/verify` to verify a Binance Code.

---

## 2022-1-4

- New endpoint for Mining:
  - `GET /sapi/v1/mining/payment/uid` to get Mining account earning.

- New endpoints for BSwap:
  - `GET /sapi/v1/bswap/unclaimedRewards` to get unclaimed rewards record.
  - `POST /sapi/v1/bswap/claimRewards` to claim swap rewards or liquidity rewards.
  - `GET /sapi/v1/bswap/claimedHistory` to get history of claimed rewards.

---

## 2021-12-30

- Update endpoint for Margin：
  - Removed out `limit` from`GET /sapi/v1/margin/interestRateHistory`; The max interval between
    startTime and endTime is 30 days.

- Update endpoint for Wallet：
  - As the Mining account is merged into Funding account, transfer types MAIN_MINING, MINING_MAIN,
    MINING_UMFUTURE, MARGIN_MINING, and MINING_MARGIN will be discontinued in Universal Transfer
    endpoint `POST /sapi/v1/asset/transfer` on **January 05, 2022 08:00 AM UTC**

---

## 2021-12-29

- Removed out dated "Symbol Type" enum; added "Permissions" enum.

---

## 2021-12-24

- Update endpoints for Sub-Account:
  - New parameter`clientTranId`added in`POST /sapi/v1/sub-account/universalTransfer` and
    `GET /sapi/v1/sub-account/universalTransfer` to support custom transfer id

---

## 2021-12-03

- New endpoints for Margin:
  - `GET  /sapi/v1/margin/crossMarginData` to get cross margin fee data collection
  - `GET  /sapi/v1/margin/isolatedMarginData` to get isolated margin fee data collection
  - `GET  /sapi/v1/margin/isolatedMarginTier` to get isolated margin tier data collection

- New endpoints for NFT:
  - `GET  /sapi/v1/nft/history/transactions` to get NFT transaction history
  - `GET  /sapi/v1/nft/history/deposit` to get NFT deposit history
  - `GET  /sapi/v1/nft/history/withdraw` to get NFT withdraw history
  - `GET  /sapi/v1/nft/user/getAsset` to get NFT asset

---

## 2021-11-30

- New endpoint for Convert:
  - `GET  /sapi/v1/convert/tradeFlow` to support user query convert trade history records

- New endpoint for Rebate:
  - `GET  /sapi/v1/rebate/taxQuery` to support user query spot rebate history records

---

## 2021-11-19

- New endpoint for Pay:
  - `GET /sapi/v1/pay/transactions`to support user query Pay trade history
- Update endpoint for Wallet:
  - New field`info`added in`GET /sapi/v1/capital/withdraw/history`to show the reason for withdrawal
    failure

---

## 2021-11-18

The following updates will take effect on **November 25, 2021 08:00 AM UTC**

- Update endpoint for Wallet：
  - `GET /sapi/v1/accountSnapshot`

The query time range of both endpoints are shortened to support data query within the last 6 months
only, where startTime does not support selecting a timestamp beyond 6 months. If you do not specify
startTime and endTime, the data of the last 7 days will be returned by default.

---

## 2021-11-17

- The following endpoints will be discontinued on **November 17, 2021 13:00 PM UTC**:
  - `POST /sapi/v1/account/apiRestrictions/ipRestriction` to support user enable and disable IP
    restriction for an API Key
  - `POST /sapi/v1/account/apiRestrictions/ipRestriction/ipList` to support user add IP list for an
    API Key
  - `GET /sapi/v1/account/apiRestrictions/ipRestriction` to support user query IP restriction for an
    API Key
  - `DELETE /sapi/v1/account/apiRestrictions/ipRestriction/ipList` to support user delete IP list
    for an API Key

---

## 2021-11-16

- New endpoints for Sub-Account:
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account enable and
    disable IP restriction for a sub-account API Key
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account add IP
    list for a sub-account API Key
  - `GET /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account query IP
    restriction for a sub-account API Key
  - `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account
    delete IP list for a sub-account API Key

---

## 2021-11-09

- New endpoints for Wallet:
  - `POST /sapi/v1/account/apiRestrictions/ipRestriction` to support user enable and disable IP
    restriction for an API Key
  - `POST /sapi/v1/account/apiRestrictions/ipRestriction/ipList` to support user add IP list for an
    API Key
  - `GET /sapi/v1/account/apiRestrictions/ipRestriction` to support user query IP restriction for an
    API Key
  - `DELETE /sapi/v1/account/apiRestrictions/ipRestriction/ipList` to support user delete IP list
    for an API Key

---

## 2021-11-08

- New endpoint for Crypto Loans:
  - New endpoint`GET /sapi/v1/loan/income`to support user query crypto loans income history

---

## 2021-11-05

- Update endpoint for Wallet:
  - New parameter `walletType `added in `POST /sapi/v1/capital/withdraw/apply` to support user
    choose wallet type `spot wallet` and `funding wallet` when withdraw crypto.

---

## 2021-11-04

The following updates will take effect on **November 11, 2021 08:00 AM UTC**

- Update endpoints for Wallet and Futures：
  - `GET /sapi/v1/asset/transfer`
  - `GET /sapi/v1/futures/transfer`

The query time range of both endpoints are shortened to support data query within the last 6 months
only, where startTime does not support selecting a timestamp beyond 6 months. If you do not specify
startTime and endTime, the data of the last 7 days will be returned by default.

---

## 2021-11-01

- `GET /api/v3/rateLimit/order` added
  - The endpoint will display the user's current order count usage for all intervals.
  - This endpoint will have a request weight of 20.

---

## 2021-10-22

- Update endpoint for Wallet:
  - New transfer types
    `MAIN_FUNDING`,`FUNDING_MAIN`,`FUNDING_UMFUTURE`,`UMFUTURE_FUNDING`,`MARGIN_FUNDING`,`FUNDING_MARGIN`,`FUNDING_CMFUTURE`and
    `CMFUTURE_FUNDING` added in Universal Transfer endpoint `POST /sapi/v1/asset/transfer` and
    `GET /sapi/v1/asset/transfer` to support transfer assets among funding account and other
    accounts
  - As the C2C account, Binance Payment, Binance Card and other business account are merged into a
    Funding account, transfer types
    `MAIN_C2C`,`C2C_MAIN`,`C2C_UMFUTURE`,`C2C_MINING`,`UMFUTURE_C2C`,`MINING_C2C`,`MARGIN_C2C`,`C2C_MARGIN`,`MAIN_PAY`and
    `PAY_MAIN` will be discontinued in Universal Transfer endpoint `POST /sapi/v1/asset/transfer`
    and `GET /sapi/v1/asset/transfer` on **November 04, 2021 08:00 AM UTC**

---

## 2021-10-14

- Update the time range of the response data for the following margin account endpoints, `startTime`
  and `endTime` time span will not exceed 30 days, without time parameter sent the system will
  return the last 7 days of data by default, while the `archived` parameter is `true`, the system
  will return the last 7 days of data 6 months ago by default:
  - `GET /sapi/v1/margin/transfer`
  - `GET /sapi/v1/margin/loan`
  - `GET /sapi/v1/margin/repay`
  - `GET /sapi/v1/margin/isolated/transfer`
  - `GET /sapi/v1/margin/interestHistory`

---

## 2021-09-18

- New endpoints for BSwap:
  - `GET /sapi/v1/bswap/poolConfigure` to get pool configure
  - `GET /sapi/v1/bswap/addLiquidityPreview` to get add liquidity preview
  - `GET /sapi/v1/bswap/removeLiquidityPreview` to get remove liquidity preview

---

## 2021-09-17

- Add`/api/*`and`/sapi/*` limit introduction in General Info

---

## 2021-09-08

- Add endpoints for enabled isolated margin account limit:
  - `DELETE /sapi/v1/margin/isolated/account` to disable isolated margin account for a specific
    symbol
  - `POST /sapi/v1/margin/isolated/account` to enable isolated margin account for a specific symbol
  - `GET /sapi/v1/margin/isolated/accountLimit` to query enabled isolated margin account limit

- New field "enabled" in response of `GET /sapi/v1/margin/isolated/account` to check if the isolated
  margin account is enabled

---

## 2021-09-03

- Update endpoint for Wallet: _ New fields `sameAddress`,`depositDust` and
  `specialWithdrawTips`added in `GET /sapi/v1/capital/config/getall` `sameAddress` means if the coin
  needs to provide memo to withdraw `depositDust` means minimum creditable amount
  `specialWithdrawTips` means special tips for withdraw _ New field `confirmNo`added in
  `GET /sapi/v1/capital/withdraw/history` to support query confirm times for withdraw history

---

## 2021-08-27

- Update endpoint for Wallet:
  - New parameter `withdrawOrderId`added in `GET  /sapi/v1/capital/withdraw/history` to support user
    query withdraw history by withdrawOrderId
  - New field `unlockConfirm`added in `GET /sapi/v1/capital/deposit/hisrec` to support query network
    confirm times for unlocking

---

## 2021-08-23

- New endpoints for Margin Account OCO:
  - `POST /sapi/v1/margin/order/oco`
  - `DELETE /sapi/v1/margin/orderList`
  - `GET /sapi/v1/margin/orderList`
  - `GET /sapi/v1/margin/allOrderList`
  - `GET /sapi/v1/margin/openOrderList`

Same usage as spot account OCO

---

## 2021-08-20

- Update endpoint for Wallet:
  - New parameters`fromSymbol`,`toSymbol`and new transfer types `ISOLATEDMARGIN_MARGIN`,
    `MARGIN_ISOLATEDMARGIN`and `ISOLATEDMARGIN_ISOLATEDMARGIN` added in
    `POST /sapi/v1/asset/transfer` and `GET /sapi/v1/asset/transfer` to support user transfer assets
    between Margin(cross) account and Margin(isolated) account

---

## 2021-08-12

- GET `api/v3/myTrades` has a new optional field `orderId`

---

## 2021-08-05

- New endpoint for C2C:
  - `GET /sapi/v1/c2c/orderMatch/listUserOrderHistory` to query user C2C trade history

---

## 2021-08-05

- Update endpoints for Savings:
  - `GET /sapi/v1/lending/union/purchaseRecord`
  - `GET /sapi/v1/lending/union/redemptionRecord`
  - `GET /sapi/v1/lending/union/interestHistory`

The time between `startTime` and `endTime` cannot be longer than 30 days.
If `startTime` and `endTime` are both not sent, then the last 30 days' data will be returned

---

## 2021-07-29

- Update endpoint for Sub-Account:
  - `GET /sapi/v1/sub-account/transfer/subUserHistory` if `startTime`and`endTime`are not sent, the
    recent 30-day data will be returned by default

---

## 2021-07-27

- New endpoint for Fiat:
  - `GET /sapi/v1/fiat/orders` to query user fiat deposit and withdraw history
  - `GET /sapi/v1/fiat/payments` to query user fiat payments history

---

## 2021-07-16

- New endpoint for Wallet:
  - `GET /sapi/v1/account/apiRestrictions` to query user API Key permission

---

## 2021-07-09

- New endpoint for Wallet:
  - `POST /sapi/v1/asset/get-funding-asset` to query funding wallet, includes Binance Pay, Binance
    Card, Binance Gift Card, Stock Token

---

## 2021-06-24

- Update endpoints for Wallet:
  - `GET /sapi/v1/capital/withdraw/history` added default value 1000, max value 1000 for the
    parameter`limit`
  - `GET /sapi/v1/capital/deposit/hisrec` added default value 1000, max value 1000 for the
    parameter`limit`

---

## 2021-06-17

- Update endpoint for Savings:
  - `GET /sapi/v1/lending/daily/product/list` to include new parameters `current` and `size`

---

## 2021-06-15

- New endpoints for Sub-Account:
  - `POST /sapi/v1/managed-subaccount/deposit ` to deposit assets into the managed sub-account (only
    for investor master account)
  - `GET /sapi/v1/managed-subaccount/asset` to query managed sub-account asset details (only for
    investor master account)
  - `POST /sapi/v1/managed-subaccount/withdraw` to withdrawal assets from the managed sub-account
    (only for investor master account)

---

## 2021-06-04

On **August 01, 2021 02:00 AM UTC** the WAPI endpoints will be discontinued:

- `GET /wapi/v3/systemStatus.html`
- `POST /wapi/v3/withdraw.html`
- `GET /wapi/v3/depositHistory.html`
- `GET /wapi/v3/withdrawHistory.html`
- `GET /wapi/v3/depositAddress.html`
- `GET /wapi/v3/accountStatus.html`
- `GET /wapi/v3/apiTradingStatus.html`
- `GET /wapi/v3/userAssetDribbletLog.html`
- `GET /wapi/v3/assetDetail.html`
- `GET /wapi/v3/tradeFee.html`
- `GET /wapi/v3/sub-account/list.html`
- `GET /wapi/v3/sub-account/transfer/history.html`
- `POST /wapi/v3/sub-account/transfer.html`
- `GET /wapi/v3/sub-account/assets.html`

The WAPI endpoints have been removed from Binance API Documentation.To ensure your trading
strategies are not affected, all API users are encouraged to upgrade trading bots to SAPI endpoints
as soon as possible.

---

## 2021-05-26

- Update endpoint for Wallet:
  - New transfer types `MAIN_PAY` ,`PAY_MAIN` added in Universal Transfer endpoint
    `POST /sapi/v1/asset/transfer` and `GET /sapi/v1/asset/transfer` to support trasnfer assets
    between spot account and pay account

---

## 2021-05-12

- Added `Data Source` in the documentation to explain where each endpoint is retrieving its data
- Added field `Data Source` to each Spot API endpoint in the documentation
- GET `api/v3/exchangeInfo` now supports single or multi-symbol query

---

## 2021-04-28

On **May 15, 2021 08:00 UTC** the SAPI Create Margin Account endpoint will be discontinued:

- `POST /sapi/v1/margin/isolated/create`

Isolated Margin account creation and trade preparation can be completed directly through Isolated
Margin funds transfer `POST /sapi/v1/margin/isolated/transfer`

---

## 2021-04-26

On **April 28, 2021 00:00 UTC** the weights to the following endpoints will be adjusted:

- `GET /api/v3/order` weight increased to 2
- `GET /api/v3/openOrders` weight increased to 3
- `GET /api/v3/allOrders` weight increased to 10
- `GET /api/v3/orderList` weight increased to 2
- `GET /api/v3/openOrderList` weight increased to 3
- `GET /api/v3/account` weight increased to 10
- `GET /api/v3/myTrades` weight increased to 10
- `GET /api/v3/exchangeInfo` weight increased to 10

---

## 2021-04-08

- Update endpoint for Sub-Account:
  - `GET /sapi/v1/sub-account/futures/accountSummary` and
    `GET /sapi/v2/sub-account/futures/accountSummary` the unit of field `asset` changed to
    USD valued summary of sub-account assets

---

## 2021-04-02

- New endpoints for Wallet:
  - `GET /sapi/v1/system/status` to query system status
  - `GET /sapi/v1/account/status` to query account status
  - `GET /sapi/v1/account/apiTradingStatus` to query account API trading status
  - `GET /sapi/v1/asset/dribblet` to query dust log
  - `GET /sapi/v1/asset/assetDetail` to query asset detail
  - `GET /sapi/v1/asset/tradeFee` to query trade fee
- New endpoint for Sub-Account:
  - `GET /sapi/v3/sub-account/assets` to query sub-account assets

---

## 2021-04-01

- Update endpoint for Sub-Account:
  - `GET /sapi/v1/sub-account/transfer/subUserHistory` new fields `fromAccountType` and
    `toAccountType` added in response

---

## 2021-03-31

- Update endpoint for Sub-Account:
  - `GET /wapi/v3/sub-account/transfer/history.html` added new parameters `fromEmail` and `toEmail`,
    the original parameter`email` is equal to`fromEmail`by default

---

## 2021-03-08

- New endpoint for Sub-Account:
  - `POST /sapi/v1/sub-account/virtualSubAccount` to support create a virtual sub-account
  - `GET /sapi/v1/sub-account/list` to support query sub-account list
  - `POST /sapi/v1/sub-account/blvt/enable` to support enable blvt for sub-account

---

## 2021-03-05

- New endpoints for Margin:
  - `GET /sapi/v1/margin/interestRateHistory` to support margin interest rate history query

---

## 2021-02-08

- New endpoints for Futures:
  - `GET /sapi/v2/futures/loan/wallet` to support BUSD loan query
  - `GET /sapi/v2/futures/loan/configs` to support BUSD loan query
  - `GET /sapi/v2/futures/loan/calcAdjustLevel` to support BUSD loan
  - `GET /sapi/v2/futures/loan/calcMaxAdjustAmount` to support adjustment of BUSD loan
  - `POST /sapi/v2/futures/loan/adjustCollateral` to support adjustment of BUSD loan
- Update endpoints for Futures
  - `GET /sapi/v1/futures/loan/adjustCollateral/history` new parameter and fields in response
    `loanCoin` for BUSD loan
  - `GET /sapi/v1/futures/loan/liquidationHistory` new parameter and fields in response `loanCoin`
    for BUSD loan

---

## 2021-02-04

- New transfer types `MARGIN_MINING` ,`MINING_MARGIN`, `MARGIN_C2C` ,`C2C_MARGIN`,
  `MARGIN_CMFUTURE`, `CMFUTURE_MARGIN` added in Universal Transfer endpoint
  `POST /sapi/v1/asset/transfer` and `GET /sapi/v1/asset/transfer`.

---

## 2021-01-15

- New endpoint `DELETE /sapi/v1/margin/openOrders` for Margin Trade
  - This will allow a user to cancel all open orders on a single symbol for margin account.
  - This endpoint will cancel all open orders including OCO orders for margin account.

---

## 2021-01-10

- New parameter `pageSize` for Mining endpoint `GET /sapi/v1/mining/payment/list`
- New fields in response to Mining endpoint `GET /sapi/v1/mining/payment/list`:
  - "type" for income type
  - "hashTransfer" for resale Hashrate
  - "transferAmount" for transferred Income

- New Mining endpoints:
  - `GET /sapi/v1/mining/payment/other`
  - `GET /sapi/v1/mining/hash-transfer/config/details`
  - `GET /sapi/v1/mining/hash-transfer/config/details/list`
  - `GET /sapi/v1/mining/hash-transfer/profit/details`
  - `POST /sapi/v1/mining/hash-transfer/config`
  - `POST /sapi/v1/mining/hash-transfer/config/cancel`

---

## 2021-01-01

USER DATA STREAM

- `outboundAccountInfo` has been removed.

---

## 2020-12-30

- New endpoint for Wallet:
  - `POST   /sapi/v1/asset/transfer` to support user universal transfer among Spot, Margin, Futures,
    C2C, MINING accounts.
  - `GET   /sapi/v1/asset/transfer` to get user universal transfer history.

---

## 2020-12-22

- New endpoint for Sub-Account:
  - `GET /sapi/v1/sub-account/sub/transfer/history` to get spot asset transfer history.

---

## 2020-12-11

- Update endpoints for Futures Cross-Collateral:
  - `GET /sapi/v1/futures/loan/wallet` new fields in response `interestFreeLimit` for total interest
    free limit, `interestFreeLimitUsed` for interest free limit used.
  - `GET /sapi/v1/futures/loan/interestHistory` new fields in response `interestFreeLimitUsed` for
    interest free limit used.

---

## 2020-12-04

- Update endpoint for BLVT:
  - `GET /sapi/v1/blvt/tokenInfo` new fields in response `currentBaskets`(include `symbol`, `amount`
    , `notionalValue` ),`purchaseFeePct`,`dailyPurchaseLimit`,`redeemFeePct`,`dailyRedeemLimit`.
- New endpoint for BLVT:
  - `GET /sapi/v1/blvt/userLimit` to get BLVT user limit info.

---

## 2020-12-02

- New endpoints for Sub-Account:
  - `GET /sapi/v2/sub-account/futures/account` to get detail on sub-account's USDT margined futures
    account and COIN margined futures account.
  - `GET /sapi/v2/sub-account/futures/accountSummary` to get summary of sub-account's USDT margined
    futures account and COIN margined futures account.
  - `GET /sapi/v2/sub-account/futures/positionRisk` to get position risk of sub-account's USDT
    margined futures account and COIN margined futures account.

---

## 2020-12-01

- Update Margin Trade Endpoint:
  - `POST /sapi/v1/margin/order` new parameter `quoteOrderQty` allow a user to specify the total
    `quoteOrderQty` spent or received in the `MARKET` order.

---

## 2020-11-27

New API clusters have been added in order to improve performance.

Users can access any of the following API clusters, in addition to `api.binance.com`

If there are any performance issues with accessing `api.binance.com` please try any of the following
instead:

- https://api1.binance.com/api/v3/*
- https://api2.binance.com/api/v3/*
- https://api3.binance.com/api/v3/*

---

## 2020-11-16

- Updated endpoints for Margin, new parameter `archived` to query data from 6 months ago:
  - `GET /sapi/v1/margin/loan`
  - `GET /sapi/v1/margin/repay`
  - `GET /sapi/v1/margin/interestHistory`

---

## 2020-11-13

- New endpoints for Sub-Account:
  - `POST /sapi/v1/sub-account/universalTransfer` to transfer spot and futures asset between master
    account and sub accounts.
  - `GET /sapi/v1/sub-account/universalTransfer` to search transfer records.

---

## 2020-11-10

- New endpoint to toggle BNB Burn:
  - `POST /sapi/v1/bnbBurn` to toggle BNB Burn on spot trade and margin interest.
  - `GET /sapi/v1/bnbBurn` to get BNB Burn status.

---

## 2020-11-09

- New field `tranId` is available from endpoints:
  - `GET /sapi/v1/sub-account/futures/internalTransfer`
  - `GET /sapi/v1/sub-account/transfer/subUserHistory`

---

## 2020-11-03

- Update endpoints for Futures Cross-Collateral:
  - `GET /sapi/v1/futures/loan/repay/history` new fields in response `repayType`(`NORMAL` for normal
    repayment, `COLLATERAL` for collateral repayment), `price` (collateral repayment rate),
    `repayCollateral`(collateral amount for collateral repayment).
  - `GET /sapi/v1/futures/loan/wallet` new fields in response `totalInterest` (total interest for
    cross-collateral), `principalForInterest`(cross-collateral principal for interest),
    `interest`(cross-collateral interest).
  - `GET /sapi/v1/futures/loan/configs` new fields in response `interestRate` (interest rate for
    cross-collateral), `interestGracePeriod` (interest grace period for cross-collateral).

- New endpoints for Futures Cross-Collateral:
  - `GET /sapi/v1/futures/loan/collateralRepayLimit` to check the maximum and minimum limit when
    repay with collateral.
  - `GET /sapi/v1/futures/loan/collateralRepay` to get quote for collateral repayment.
  - `POST /sapi/v1/futures/loan/collateralRepay` to repay with collateral.
  - `GET /sapi/v1/futures/loan/collateralRepayResult` to check collateral repayment result.
  - `GET /sapi/v1/futures/loan/interestHistory` to get cross-collateral interest history.

---

## 2020-10-14

- Update endpoints for Futures Cross-Collateral:
  - `POST /sapi/v1/futures/loan/borrow` and `GET /sapi/v1/futures/loan/borrow/history` new field
    `borrowId` in response for ID of Cross-Collateral borrow operation.
  - `POST /sapi/v1/futures/loan/repay` and `GET /sapi/v1/futures/loan/repay/history` new field
    `repayId` in response for ID of Cross-Collateral repay operation.

---

## 2020-10-10

- New `type` added in the endpoint `POST /sapi/v1/sub-account/futures/transfer`to support transfer
  asset from subaccount's spot account to its COIN-margined futures account and transfer asset from
  subaccount's COIN-margined futures account to its spot account.

---

## 2020-09-30

- Update endpoints for Margin Account:
  - `GET /sapi/v1/margin/maxBorrowable` new field `borrowLimit` in response for account borrow
    limit.

---

## 2020-09-28

- New endpoints for Binance Savings:
  - `POST /sapi/v1/lending/positionChanged` to change fixed/activity position to daily position.
- New parameter `ACTIVITY` replace `REGULAR`in the following Binance Savings endpoints:
  - `GET /sapi/v1/lending/project/list`
  - `POST /sapi/v1/lending/customizedFixed/purchase`
  - `GET /sapi/v1/lending/project/position/list`
  - `GET /sapi/v1/lending/union/purchaseRecord`
  - `GET /sapi/v1/lending/union/interestHistory`

---

## 2020-09-23

- New SAPI endpoints for BSwap:
  - `GET /sapi/v1/bswap/pools` to list all swap pools.
  - `GET /sapi/v1/bswap/liquidity` to get liquidity information of a pool.
  - `POST /sapi/v1/bswap/liquidityAdd` to add liquidity.
  - `POST /sapi/v1/bswap/liquidityRemove` to remove liquidity.
  - `GET /sapi/v1/bswap/liquidityOps` to get liquidity operation record.
  - `GET /sapi/v1/bswap/quote` to request quotes.
  - `POST /sapi/v1/bswap/swap` to swap.
  - `GET /sapi/v1/bswap/swap` to get swap history.

---

## 2020-09-16

- New SAPI endpoints for BLVT:
  - `GET /sapi/v1/blvt/tokenInfo` to get BLVT info.
  - `POST /sapi/v1/blvt/subscribe (HMAC SHA256)` to subscribe BLVT.
  - `GET /sapi/v1/blvt/subscribe/record  (HMAC SHA256)` to get subscription record。
  - `POST /sapi/v1/blvt/redeem (HMAC SHA256)` to redeem BLVT.
  - `GET /sapi/v1/blvt/redeem/record  (HMAC SHA256` to get redemption record.

- The BLVT NAV system is working relatively with Binance Futures, so some endpoints are based on
  futures system:
  - New endpoint to get historical BLVT Kline.
  - New WebSocket streams for BLVT Info and BLVT NAV Kline:

## 2020-09-09

USER DATA STREAM

- `outboundAccountInfo` has been deprecated.
- `outboundAccountInfo` will be removed in the future. (Exact date unknown) **Please use
  `outboundAccountPosition` instead.**
- `outboundAccountInfo` will now only show the balance of non-zero assets and assets that have been
  reduced to 0.

---

## 2020-09-03

- New endpoint `POST /sapi/v1/sub-account/futures/internalTransfer` to transfer futures asset
  between master account and subaccount.
- New endpoint`GET /sapi/v1/sub-account/futures/internalTransfer` to get futures transfer history of
  subaccount.

---

## 2020-09-01

- New parameter `masterAccountTotalAsset` added in the endpoint
  `GET /sapi/v1/sub-account/spotSummary` to get BTC valued asset summary of master account.

---

## 2020-08-27

- New endpoint `GET /sapi/v1/sub-account/spotSummary` to get BTC valued asset summary of subaccout.

---

## 2020-08-26

- New parameter `symbols` added in the endpoint `GET /sapi/v1/margin/isolated/account`.

---

## 2020-07-28

ISOLATED MARGIN

- New parameters "isIsolated" and "symbol" added for isolated margin in the following endpoints:
  - `POST /sapi/v1/margin/loan`
  - `POST /sapi/v1/margin/repay`
- New parameter "isIsolated" and new response field "isIsolated" added for isolated margin in the
  following endpoints:
  - `POST /sapi/v1/margin/order`
  - `DELETE /sapi/v1/margin/order`
  - `GET /sapi/v1/margin/order`
  - `GET /sapi/v1/margin/openOrders`
  - `GET /sapi/v1/margin/allOrders`
  - `GET /sapi/v1/margin/myTrades`

- New parameter "isolatedSymbol" and new response field "isolatedSymbol" added for isolated margin
  in the following endpoints:
  - `GET /sapi/v1/margin/loan`
  - `GET /sapi/v1/margin/repay`
  - `GET /sapi/v1/margin/interestHistory`

- New parameter "isolatedSymbol" and new response field "isIsolated" added for isolated margin in
  the following endpoint `GET /sapi/v1/margin/forceLiquidationRec`

- New parameter "isolatedSymbol" added for isolated margin in the following endpoints:
  - `GET /sapi/v1/margin/maxBorrowable`
  - `GET /sapi/v1/margin/maxTransferable`
- New endpoints for isolated margin:
  - `POST /sapi/v1/margin/isolated/create`
  - `POST /sapi/v1/margin/isolated/transfer`
  - `GET /sapi/v1/margin/isolated/transfer`
  - `GET /sapi/v1/margin/isolated/account`
  - `GET /sapi/v1/margin/isolated/pair`
  - `GET /sapi/v1/margin/isolated/allPairs`

- New endpoints for listenKey management of isolated margin account:
  - `POST /sapi/v1/userDataStream/isolated`
  - `PUT /sapi/v1/userDataStream/isolated`
  - `DELETE /sapi/v1/userDataStream/isolated`

---

## 2020-07-20

- The max value of parameter "limit" in `GET /sapi/v1/margin/allOrders` has been changed as 500.

---

## 2020-07-17

- There is now a request limit specifically for the sapi/v1/margin/allOrders endpoint at 60 raw
  requests per minute for a single IP address.

---

## 2020-07-13

- New SAPI Endpoints for futures Cross-Collateral:
  - `POST /sapi/v1/futures/loan/borrow`
  - `GET /sapi/v1/futures/loan/borrow/history`
  - `POST /sapi/v1/futures/loan/repay`
  - `GET /sapi/v1/futures/loan/repay/history`
  - `GET /sapi/v1/futures/loan/wallet`
  - `GET /sapi/v1/futures/loan/configs`
  - `GET /sapi/v1/futures/loan/calcAdjustLevel`
  - `GET /sapi/v1/futures/loan/calcMaxAdjustAmount`
  - `POST /sapi/v1/futures/loan/adjustCollateral`
  - `GET /sapi/v1/futures/loan/adjustCollateral/history`
  - `GET /sapi/v1/futures/loan/liquidationHistory`

---

## 2020-06-28

- SAPI Endpoints for futures:
  - `POST /sapi/v1/futures/transfer`
  - `GET /sapi/v1/futures/transfer`

---

## 2020-05-06

- New endpoints for Mining:
  - `GET /sapi/v1/mining/pub/algoList`
  - `GET /sapi/v1/mining/pub/coinList`
  - `GET /sapi/v1/mining/worker/detail`
  - `GET /sapi/v1/mining/worker/list`
  - `GET /sapi/v1/mining/payment/list`
  - `GET /sapi/v1/mining/statistics/user/status`
  - `GET /sapi/v1/mining/statistics/user/list`

---

## 2020-05-01

- From 2020-05-01 UTC 00:00, all symbols will have a limit of 200 open orders using the
  [MAX_NUM_ORDERS](https://binance-docs.github.io/apidocs/spot/en/#filters) filter.
  - No existing orders will be removed or canceled.
  - Accounts that have 200 or more open orders on a symbol will not be able to place new orders on
    that symbol until the open order count is below 200.
  - OCO orders count as 2 open orders before the `LIMIT` order is touched or the `STOP_LOSS` (or
    `STOP_LOSS_LIMIT`) order is triggered; once this happens the other order is canceled and will no
    longer count as an open order.

---

## 2020-04-25

<font size=4>SPOT API</font>

- New field `permissions`
  - Defines the trading permissions that are allowed on accounts and symbols.
  - `permissions` is an enum array; values:
    - `SPOT`
    - `MARGIN`
  - `permissions` will replace `isSpotTradingAllowed` and `isMarginTradingAllowed` on
    `GET api/v3/exchangeInfo` in future API versions (v4+).
  - For an account to trade on a symbol, the account and symbol must share at least 1 permission in
    common.
- Updates to GET `api/v3/exchangeInfo`
  - New field `permissions` added.
  - New field `quoteAssetPrecision` added; a duplicate of the `quotePrecision` field.
    `quotePrecision` will be removed in future API versions (v4+).
- Updates to GET `api/v3/account`
  - New field `permissions` added.
- New endpoint DELETE `api/v3/openOrders`
  - This will allow a user to cancel all open orders on a single symbol.
  - This endpoint will cancel all open orders including OCO orders.
- Orders can be canceled via the API on symbols in the `BREAK` or `HALT` status.

<font size=4> USER DATA STREAM </font>

- `OutboundAccountInfo` has new field `P` which shows the trading permissions of the account.

---

## 2020-04-23

WEB SOCKET STREAM

- WebSocket connections have a limit of 5 incoming messages per second. A message is considered:
  - A PING frame
  - A PONG frame
  - A JSON control message (e.g. subscribe, unsubscribe)
- A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected
  may be banned.
- A single connection can listen to a maximum of 1024 streams.

## 2020-04-16

- New fields in response to endpoint`GET /sapi/v1/lending/daily/token/position`：
  - `todayPurchasedAmount` for user's purchased amount today

- New lending endpoints for customized fixed projects:
  - `GET /sapi/v1/lending/project/list`
  - `POST /sapi/v1/lending/customizedFixed/purchase`
  - `GET /sapi/v1/lending/project/position/list`

---

## 2020-04-02

- New fields in response to endpoint`GET /sapi/v1/capital/config/getall`：
  - `minConfirm` for min number for balance confirmation
  - `unLockConfirm` for confirmation number for balance unlock

---

## 2020-03-24

- `MAX_POSITION` filter added.
  - This filter defines the allowed maximum position an account can have on the base asset of a
    symbol. An account's position defined as the sum of the account's:
    - free balance of the base asset
    - locked balance of the base asset
    - sum of the qty of all open BUY orders

  - `BUY` orders will be rejected if the account's position is greater than the maximum position
    allowed.

---

## 2020-03-13

- New parameter `transactionFeeFlag` is available in endpoint:
  - `POST /sapi/v1/capital/withdraw/apply` and
  - `POST /wapi/v3/withdraw.html`

---

## 2020-02-05

- New sub account endpoints:
  - `POST /sapi/v1/sub-account/futures/transfer` to transfer between futures and spot accout of
    sub-account.
  - `POST /sapi/v1/sub-account/margin/transfer` to transfer between margin and spot accout of
    sub-account.
  - `POST /sapi/v1/sub-account/transfer/subToSub` to transfer to another account by sub-account.
  - `POST /sapi/v1/sub-account/transfer/subToMaster` to transfer to same master by sub-account.
  - `GET /sapi/v1/sub-account/transfer/subUserHistory` to get transfer history of sub-account.

---

## 2020-01-15

- New parameter `withdrawOrderId` for client customized withdraw id for endpoint
  `POST /wapi/v3/withdraw.html`.

- New field `withdrawOrderId` in response to `GET /wapi/v3/withdrawHistory.html`

---

## 2019-12-25

- New endpoints for Binance Savings:
  - `GET /sapi/v1/lending/daily/product/list`
  - `GET /sapi/v1/lending/daily/userLeftQuota`
  - `POST /sapi/v1/lending/daily/purchase `
  - `GET /sapi/v1/lending/daily/userRedemptionQuota`
  - `POST /sapi/v1/lending/daily/redeem`
  - `GET /sapi/v1/lending/daily/token/position`
  - `GET /sapi/v1/lending/union/account`
  - `GET /sapi/v1/lending/union/purchaseRecord`
  - `GET /sapi/v1/lending/union/redemptionRecord`
  - `GET /sapi/v1/lending/union/interestHistory`

- Added time interval limit in  
  `GET  /sapi/v1/capital/withdraw/history`,  
  `GET /wapi/v3/withdrawHistory.html`,  
  `GET /sapi/v1/capital/deposit/hisrec` and  
  `GET /wapi/v3/depositHistory.html`: _ The default `startTime` is 90 days from current time, and
  the default `endTime` is current time. _ Please notice the default `startTime` and `endTime` to
  make sure that time interval is within 0-90 days. \* If both `startTime` and `endTime` are sent,
  time between `startTime` and `endTime` must be less than 90 days.

---

## 2019-12-18

- New endpoint to get daily snapshot of account:  
  `GET /sapi/v1/accountSnapshot`

---

## 2019-11-30

- Added parameter `sideEffectType` in `POST  /sapi/v1/margin/order (HMAC SHA256)` with enums:
  - `NO_SIDE_EFFECT` for normal trade order;
  - `MARGIN_BUY` for margin trade order;
  - `AUTO_REPAY` for making auto repayment after order filled.

- New field `marginBuyBorrowAmount` and `marginBuyBorrowAsset` in `FULL` response to
  `POST  /sapi/v1/margin/order (HMAC SHA256)`

---

## 2019-11-28

- New SAPI endpoint to disable fast withdraw switch:  
  `POST /sapi/v1/account/disableFastWithdrawSwitch (HMAC SHA256)`
- New SAPI endpoint to enable fast withdraw switch:  
  `POST /sapi/v1/account/enableFastWithdrawSwitch (HMAC SHA256)`

---

## 2019-11-22

- Quote Order Qty Market orders have been enabled on all symbols.
  - Quote Order Qty `MARKET` orders allow a user to specify the total `quoteOrderQty` spent or
    received in the `MARKET` order.
  - Quote Order Qty `MARKET` orders will not break `LOT_SIZE` filter rules; the order will execute a
    quantity that will have the notional value as close as possible to `quoteOrderQty`.
  - Using `BNBBTC` as an example:
    - On the `BUY` side, the order will buy as many BNB as `quoteOrderQty` BTC can.
    - On the `SELL` side, the order will sell as much BNB as needed to receive `quoteOrderQty` BTC.

---

## 2019-11-19

- `GET /sapi/v1/sub-account/margin/account` has new field: `marginTradeCoeffVo` which contains
  - `forceLiquidationBar` for liquidation margin ratio
  - `marginCallBar` for margin call margin ratio
  - `normalBar` for initial margin ratio

---

## 2019-11-13

<font size=4>Rest API </font>

- api/v3/exchangeInfo has new fields:
  - `quoteOrderQtyMarketAllowed`
  - `baseCommissionPrecision`
  - `quoteCommissionPrecision`
- `MARKET` orders have a new optional field: `quoteOrderQty` used to specify the quote quantity to
  BUY or SELL. This cannot be used in combination with `quantity`.
  - The exact timing that `quoteOrderQty` MARKET orders will be enabled is TBD. There will be a
    separate announcement and further details at that time.
- All order query endpoints will return a new field `origQuoteOrderQty` in the JSON payload. (e.g.
  GET api/v3/allOrders)

```json
{
  "code": -1128,
  "msg": "Combination of optional parameters invalid. Recommendation: 'stopLimitTimeInForce' should also be sent."
}
```

- Updated error messages for -1128
  - Sending an `OCO` with a `stopLimitPrice` but without a `stopLimitTimeInForce` will return the
    error:

- Updated error messages for -1003 to specify the limit is referring to the request weight, not to
  the number of requests.

**Deprecation of v1 endpoints**:

By end of Q1 2020, the following endpoints will be removed from the API. The documentation has been
updated to use the v3 versions of these endpoints.

- GET api/v1/depth
- GET api/v1/historicalTrades
- GET api/v1/aggTrades
- GET api/v1/klines
- GET api/v1/ticker/24hr
- GET api/v1/ticker/price
- GET api/v1/exchangeInfo
- POST api/v1/userDataStream
- PUT api/v1/userDataStream
- GET api/v1/ping
- GET api/v1/time
- GET api/v1/ticker/bookTicker

**These endpoints however, will NOT be migrated to v3. Please use the following endpoints instead
moving forward.**

<table>
<tr>
<th>Old V1 Endpoints</th>
<th>New V3 Endpoints</th>
</tr>
<tr>
<td>GET api/v1/ticker/allPrices</td>
<td>GET api/v3/ticker/price</td>
</tr>
<tr>
<td>GET api/v1/ticker/allBookTickers</td>
<td>GET api/v3/ticker/bookTicker</td>
</tr>
</table>

<font size=4>USER DATA STREAM </font>

- Changes to`executionReport` event
  - If the C field is empty, it will now properly return `null`, instead of `"null"`.
  - New field Q which represents the `quoteOrderQty`.

- `balanceUpdate` event type added
  - This event occurs when funds are deposited or withdrawn from your account.

<font size=4> WEB SOCKET STREAM</font>

- WSS now supports live subscribing/unsubscribing to streams.

---

## 2019-11-08

- New sapi for subaccount management on margin and futures:
  - `GET /sapi/v1/sub-account/status (HMAC SHA256)`
  - `POST /sapi/v1/sub-account/margin/enable (HMAC SHA256)`
  - `GET /sapi/v1/sub-account/margin/account (HMAC SHA256)`
  - `GET /sapi/v1/sub-account/margin/accountSummary (HMAC SHA256)`
  - `POST /sapi/v1/sub-account/futures/enable (HMAC SHA256)`
  - `GET /sapi/v1/sub-account/futures/account (HMAC SHA256)`
  - `GET /sapi/v1/sub-account/futures/accountSummary (HMAC SHA256)`
  - `GET /sapi/v1/sub-account/futures/positionRisk (HMAC SHA256)`

---

## 2019-11-04

- New sapi endpoints for subaccount wallet.
  - `GET /sapi/v1/capital/deposit/subAddress (HMAC SHA256))`: fetch subaccount deposit address.
  - `GET /sapi/v1/capital/deposit/subHisrec (HMAC SHA256))`: fetch subaccount deposit history.

---

## 2019-10-29

- New sapi endpoints for wallet.
  - `POST /sapi/v1/capital/withdraw/apply (HMAC SHA256)`: withdraw.
  - `Get /sapi/v1/capital/withdraw/history (HMAC SHA256)`: fetch withdraw history with network.

---

## 2019-10-14

- New sapi endpoints for wallet.
  - `GET /sapi/v1/capital/config/getall (HMAC SHA256)`: get all coins' information for user.
  - `GET /sapi/v1/capital/deposit/hisrec (HMAC SHA256)`: fetch deposit history with network.
  - `GET /sapi/v1/capital/deposit/address (HMAC SHA256)`: fetch deposit address with network.

---

## 2019-10-11

- Added parameter `network` in `POST /wapi/v3/withdraw.html` so that asset can be withdrawed with
  specific network.

---

## 2019-09-09

- New WebSocket streams for bookTickers added: `<symbol>@bookTicker` and `!bookTicker`.

---

## 2019-09-03

- Faster order book data with 100ms updates: `<symbol>@depth@100ms` and `<symbol>@depth#@100ms`
- Added "Update Speed:" to `Websocket Market Streams`
- Removed deprecated v1 endpoints as per previous announcement:
  - GET api/v1/order
  - GET api/v1/openOrders
  - POST api/v1/order
  - DELETE api/v1/order
  - GET api/v1/allOrders
  - GET api/v1/account
  - GET api/v1/myTrades

---

## 2019-08-16

- GET api/v1/depth `limit` of 10000 has been temporarily removed

- In Q4 2017, the following endpoints were deprecated and removed from the API documentation. They
  have been permanently removed from the API as of this version. We apologize for the omission from
  the original changelog:
  - GET api/v1/order
  - GET api/v1/openOrders
  - POST api/v1/order
  - DELETE api/v1/order
  - GET api/v1/allOrders
  - GET api/v1/account
  - GET api/v1/myTrades

- Streams, endpoints, parameters, payloads, etc. described in the documents in this repository are
  **considered official** and **supported**. The use of any other streams, endpoints, parameters, or
  payloads, etc. is **not supported; use them at your own risk and with no guarantees.**

---

## 2019-09-15

<font size=4>Rest API</font>

- New order type: OCO ("One Cancels the Other")
  - An OCO has 2 orders: (also known as legs in financial terms)
    - `STOP_LOSS` or `STOP_LOSS_LIMIT` leg
    - `LIMIT_MAKER` leg

  - Price Restrictions:
    - `SELL Orders` : Limit Price > Last Price > Stop Price
    - `BUY Orders` : Limit Price < Last Price < Stop Price
    - As stated, the prices must "straddle" the last traded price on the symbol. EX: If the last
      price is 10:
      - A SELL OCO must have the limit price greater than 10, and the stop price less than 10.
      - A BUY OCO must have a limit price less than 10, and the stop price greater than 10.

  - Quantity Restrictions:
    - Both legs must have the **same quantity**.
    - `ICEBERG` quantities however, do not have to be the same.

  - Execution Order:
    - If the `LIMIT_MAKER` is touched, the limit maker leg will be executed first BEFORE canceling
      the Stop Loss Leg.
    - if the Market Price moves such that the `STOP_LOSS` or `STOP_LOSS_LIMIT` will trigger, the
      Limit Maker leg will be cancelled BEFORE executing the `STOP_LOSS` Leg.

  - Cancelling an OCO
    - Cancelling either order leg will cancel the entire OCO.
    - The entire OCO can be canceled via the `orderListId` or the `listClientOrderId`.

  - New Enums for OCO:
    1. `ListStatusType`
       - `RESPONSE` - used when ListStatus is responding to a failed action. (either order list
         placement or cancellation)
       - `EXEC_STARTED` - used when an order list has been placed or there is an update to a list's
         status.
       - `ALL_DONE` - used when an order list has finished executing and is no longer active.
    2. `ListOrderStatus`
       - `EXECUTING` - used when an order list has been placed or there is an update to a list's
         status.
       - `ALL_DONE` - used when an order list has finished executing and is no longer active.
       - `REJECT` - used when ListStatus is responding to a failed action. (either order list
         placement or cancellation)
    3. `ContingencyType`
       - `OCO` - specifies the type of order list.

  - New Endpoints:
    - POST api/v3/order/oco
    - DELETE api/v3/orderList
    - GET api/v3/orderList

- `recvWindow` cannot exceed 60000.
- New `intervalLetter` values for headers:
  - SECOND => S
  - MINUTE => M
  - HOUR => H
  - DAY => D
- New Headers `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)` will give your current used request
  weight for the (intervalNum)(intervalLetter) rate limiter. For example, if there is a one minute
  request rate weight limiter set, you will get a `X-MBX-USED-WEIGHT-1M` header in the response. The
  legacy header `X-MBX-USED-WEIGHT` will still be returned and will represent the current used
  weight for the one minute request rate weight limit.
- New Header `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)`that is updated on any valid order
  placement and tracks your current order count for the interval; rejected/unsuccessful orders are
  not guaranteed to have `X-MBX-ORDER-COUNT-**` headers in the response.
  - Eg. `X-MBX-ORDER-COUNT-1S` for "orders per 1 second" and `X-MBX-ORDER-COUNT-1D` for orders per
    "one day"
- GET api/v1/depth now supports `limit` 5000 and 10000; weights are 50 and 100 respectively.
- GET api/v1/exchangeInfo has a new parameter `ocoAllowed`.

<font size=4>USER DATA STREAM</font>

- `executionReport` event now contains "g" which has the `orderListId`; it will be set to -1 for
  non-OCO orders.
- New Event Type `listStatus`; `listStatus` is sent on an update to any OCO order.
- New Event Type `outboundAccountPosition`; `outboundAccountPosition` is sent any time an account's
  balance changes and contains the assets that could have changed by the event that generated the
  balance change (a deposit, withdrawal, trade, order placement, or cancelation).

<font size=4>NEW ERRORS</font>

- **-1131 BAD_RECV_WINDOW**
  - `recvWindow` must be less than 60000
- **-1099 Not found, authenticated, or authorized**
  - This replaces error code -1999

<font size=4>NEW -2011 ERRORS</font>

- **OCO_BAD_ORDER_PARAMS**
  - A parameter for one of the orders is incorrect.
- **OCO_BAD_PRICES**
  - The relationship of the prices for the orders is not correct.
- **UNSUPPORTED_ORD_OCO**
  - OCO orders are not supported for this symbol.

---

## 2019-03-12

<font size=4>Rest API</font>

- X-MBX-USED-WEIGHT header added to Rest API responses.
- Retry-After header added to Rest API 418 and 429 responses.
- When canceling the Rest API can now return `errorCode` -1013 OR -2011 if the symbol's `status`
  isn't `TRADING`.
- `api/v1/depth` no longer has the ignored and empty `[]`.
- `api/v3/myTrades` now returns `quoteQty`; the price \* qty of for the trade.

<font size=4>Websocket streams</font>

- `<symbol>@depth` and `<symbol>@depthX` streams no longer have the ignored and empty `[]`.

<font size=4>System improvements</font>

- Matching Engine stability/reliability improvements.
- Rest API performance improvements.

---

## 2018-11-13

<font size=4>Rest API</font>

- Can now cancel orders through the Rest API during a trading ban.
- New filters: `PERCENT_PRICE`, `MARKET_LOT_SIZE`, `MAX_NUM_ICEBERG_ORDERS`.
- Added `RAW_REQUESTS` rate limit. Limits based on the number of requests over X minutes regardless
  of weight.
- /api/v3/ticker/price increased to weight of 2 for a no symbol query.
- /api/v3/ticker/bookTicker increased weight of 2 for a no symbol query.
- DELETE /api/v3/order will now return an execution report of the final state of the order.
- `MIN_NOTIONAL` filter has two new parameters: `applyToMarket` (whether or not the filter is
  applied to MARKET orders) and `avgPriceMins` (the number of minutes over which the price averaged
  for the notional estimation).
- `intervalNum` added to /api/v1/exchangeInfo limits. `intervalNum` describes the amount of the
  interval. For example: `intervalNum` 5, with `interval` minute, means "every 5 minutes".

<font size=4>Explanation for the average price calculation:</font>

1. (qty \* price) of all trades / sum of qty of all trades over previous 5 minutes.

2. If there is no trade in the last 5 minutes, it takes the first trade that happened outside of the
   5min window. For example if the last trade was 20 minutes ago, that trade's price is the 5 min
   average.

3. If there is no trade on the symbol, there is no average price and market orders cannot be placed.
   On a new symbol with `applyToMarket` enabled on the `MIN_NOTIONAL` filter, market orders cannot
   be placed until there is at least 1 trade.

4. The current average price can be checked here:
   `https://api.binance.com/api/v3/avgPrice?symbol=<symbol>` For example:
   https://api.binance.com/api/v3/avgPrice?symbol=BNBUSDT

<font size=4>User data stream</font>

- `Last quote asset transacted quantity` (as variable `Y`) added to execution reports. Represents
  the `lastPrice` \* `lastQty` (`L` \* `l`).

---

## 2018-07-18

<font size=4>Rest API</font>

- New filter: `ICEBERG_PARTS`
- `POST api/v3/order` new defaults for `newOrderRespType`. `ACK`, `RESULT`, or `FULL`; `MARKET` and
  `LIMIT` order types default to `FULL`, all other orders default to `ACK`.
- POST api/v3/order `RESULT` and `FULL` responses now have `cummulativeQuoteQty`
- GET api/v3/openOrders with no symbol weight reduced to 40.
- GET api/v3/ticker/24hr with no symbol weight reduced to 40.
- Max amount of trades from GET /api/v1/trades increased to 1000.
- Max amount of trades from GET /api/v1/historicalTrades increased to 1000.
- Max amount of aggregate trades from GET /api/v1/aggTrades increased to 1000.
- Max amount of aggregate trades from GET /api/v1/klines increased to 1000.
- Rest API Order lookups now return `updateTime` which represents the last time the order was
  updated; `time` is the order creation time.
- Order lookup endpoints will now return `cummulativeQuoteQty`. If `cummulativeQuoteQty` is < 0, it
  means the data isn't available for this order at this time.
- `REQUESTS` rate limit type changed to `REQUEST_WEIGHT`. This limit was always logically request
  weight and the previous name for it caused confusion.

<font size=4>User data stream</font>

- `cummulativeQuoteQty` field added to order responses and execution reports (as variable `Z`).
  Represents the cummulative amount of the `quote` that has been spent (with a `BUY` order) or
  received (with a `SELL` order). Historical orders will have a value < 0 in this field indicating
  the data is not available at this time. `cummulativeQuoteQty` divided by `cummulativeQty` will
  give the average price for an order.
- `O` (order creation time) added to execution reports

---

## 2018-01-23

- GET /api/v1/historicalTrades weight decreased to 5
- GET /api/v1/aggTrades weight decreased to 1
- GET /api/v1/klines weight decreased to 1
- GET /api/v1/ticker/24hr all symbols weight decreased to number of trading symbols / 2
- GET /api/v3/allOrders weight decreased to 5
- GET /api/v3/myTrades weight decreased to 5
- GET /api/v3/account weight decreased to 5
- GET /api/v1/depth limit=500 weight decreased to 5
- GET /api/v1/depth limit=1000 weight decreased to 10
- -1003 error message updated to direct users to websockets

---

## 2018-01-20

- GET /api/v1/ticker/24hr single symbol weight decreased to 1
- GET /api/v3/openOrders all symbols weight decreased to number of trading symbols / 2
- GET /api/v3/allOrders weight decreased to 15
- GET /api/v3/myTrades weight decreased to 15
- GET /api/v3/order weight decreased to 1
- myTrades will now return both sides of a self-trade/wash-trade

---

## 2018-01-14

- GET /api/v1/aggTrades weight changed to 2
- GET /api/v1/klines weight changed to 2
- GET /api/v3/order weight changed to 2
- GET /api/v3/allOrders weight changed to 20
- GET /api/v3/account weight changed to 20
- GET /api/v3/myTrades weight changed to 20
- GET /api/v3/historicalTrades weight changed to 20

---

# Change Log

## 2023-05-26

**Notice:** The change below are being rolled out, and will take approximately a week to complete.

- The following base endpoints may give better performance but have less stability than
  **https://api.binance.com**:
  - **https://api1.binance.com**
  - **https://api2.binance.com**
  - **https://api3.binance.com**
  - **https://api4.binance.com**

---

## 2023-05-24

- **The previous market data URLs have been deprecated. Please update your code immediately to
  prevent interruption of our services.**
  - API Market data from `data.binance.com` can now be accessed from `data-api.binance.vision`.
  - Websocket Market Data from `data-stream.binance.com` can now be accessed from
    `data-stream.binance.vision`.
- New endpoints for Classic Portfolio Margin:
  - `POST /sapi/v1/portfolio/auto-collection`: classic portfolio Margin fund collection
  - `POST /sapi/v1/portfolio/bnb-transfer`: classic portfolio margin BNB transfer
- `GET /sapi/v1/portfolio/interest-rate` has be deprecated, users can query the Classic Portfolio
  Margin Negative Balance Interest Rate by using `GET /sapi/v1/margin/interestRateHistory`.

---

## 2023-05-18

- New endpoints for Wallet：
  - `POST /sapi/v1/capital/deposit/credit-apply`: apply deposit credit for expired address

---

## 2023-05-09

- New endpoints for Portfolio Margin：
  - `GET /sapi/v1/portfolio/asset-index-price`: query portfolio margin asset index price
- Update endpoints for Wallet:
  - `POST /sapi/v1/asset/transfer`: add enum `MAIN_PORTFOLIO_MARGIN` and `PORTFOLIO_MARGIN_MAIN`

---

## 2023-04-20

- New endpoints for Sub-Account：
  - `GET /sapi/v1/managed-subaccount/deposit/address`: get managed sub-account deposit address
- Update endpoints for VIP Loans:
  - `GET /sapi/v1/loan/vip/ongoing/orders`: add fields `totalCollateralValueAfterHaircut` and
    `lockedCollateralValue`

---

## 2023-04-18

- New endpoints for Spot Algo：
  - `POST /sapi/v1/algo/spot/newOrderTwap` to support new order
  - `DELETE /sapi/v1/algo/spot/order` to support cancel Algo order
  - `GET /sapi/v1/algo/spot/openOrders` to support query Algo open orders
  - `GET /sapi/v1/algo/spot/historicalOrders` to support query Algo historical orders
  - `GET /sapi/v1/algo/spot/subOrders` to support query Algo sub orders for a specified algoId

---

## 2023-03-23

- Update endpoints for Sub-Account:
  - `GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`: Add response field `tranId`
  - `GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`: Add response field `tranId`
- New endpoints for Sub-Account:
  - `GET /sapi/v1/managed-subaccount/info`: query investor's managed sub-account list
  - `GET /sapi/v1/sub-account/transaction-statistics`: Query sub-account transaction tatistics

---

## 2023-03-13

**Notice:** All changes are being rolled out gradually to all our servers, and may take a week to
complete.

GENERAL CHANGES

- The error messages for certain issues have been improved for easier troubleshooting.

<table>
    <tr>
        <th>Situation</th>
        <th>Old Error Message</th>
        <th>New Error Message</th>
    </tr>
    <tr>
        <td>An account cannot place or cancel an order, due to trading ability disabled.</td>
        <td rowspan="3">This action is disabled on this account.</td>
        <td>This account may not place or cancel orders.</td>
    </tr>
    <tr>
        <td>When the permissions configured on the symbol do not match the permissions on the account.</td>
        <td>This symbol is not permitted for this account.</td>
    </tr>
    <tr>
        <td>When the account tries to place an order on a symbol it has no permissions for.</td>
        <td>This symbol is restricted for this account.</td>
    </tr>
    <tr>
        <td>Placing an order when <tt>symbol</tt> is not <tt>TRADING</tt>. </td>
        <td rowspan="2">Unsupported order combination.</td>
        <td>This order type is not possible in this trading phase.</td>
    </tr>
    <tr>
        <td>Placing an order with <tt>timeinForce</tt>=<tt>IOC</tt> or <tt>FOK</tt> on a trading phase that does not support it.</td>
        <td>Limit orders require GTC for this phase.</td>
    </tr>
</table>

- Fixed error message for querying archived orders:
  - Previously, If an archived order (i.e. order with status `CANCELED` or `EXPIRED` where
    `executedQty` == 0 that occurred more than 90 days in the past.) is queried, the error message
    would be:
    - `{"code": -2013,"msg": "Order does not exist."}`
  - Now, the error message is:
    - `{"code": -2026,"msg": "Order was canceled or expired with no executed qty over 90 days ago and has been archived."}`
- Behavior for API requests with `startTime` and `endTime`:
  - Previously some requests failed if the `startTime` == `endTime`.
  - Now, all API requests that accept `startTime` and `endTime` allow the parameters to be equal.
    This applies to the following requests:
    - Rest API
      - `GET /api/v3/aggTrades`
      - `GET /api/v3/klines`
      - `GET /api/v3/allOrderList`
      - `GET /api/v3/allOrders`
      - `GET /api/v3/myTrades`

The following changes will take effect **approximately a week from the release date**, but the rest
of the documentation has been updated to reflect the future changes:

- Changes to Filter Evaluation:
  - Previous behavior: `LOT_SIZE` and `MARKET_LOT_SIZE` required that (`quantity` - `minQty`) %
    `stepSize` == 0.
  - New behavior: This has now been changed to (`quantity` % `stepSize`) == 0.
- Bug fix with reverse `MARKET` orders (i.e., `MARKET` using `quoteOrderQty`):
  - Previous behavior: Reverse market orders would always have the status `FILLED` even if the order
    did not fully fill due to low liquidity.
  - New behavior: If the reverse market order did not fully fill due to low liquidity the order
    status will be `EXPIRED`, and `FILLED` only if the order was completely filled.

SPOT API

- Changes to `DELETE /api/v3/order` and `POST /api/v3/order/cancelReplace`:
  - A new optional parameter `cancelRestrictions` that determines whether the cancel will succeed if
    the order status is `NEW` or `PARTIALLY_FILLED`.
  - If the order cancellation fails due to `cancelRestrictions`, the error will be:
    - `{"code": -2011,"msg": "Order was not canceled due to cancel restrictions."}`

---

## 2023-02-27

- New endpoints for Margin:
  - `/sapi/v1/margin/next-hourly-interest-rate`: Get user the next hourly estimate interest
- New endpoints for Porfolio Margin:
  - `GET /sapi/v1/portfolio/interest-history`: get user's portfolio margin interest history
  - `GET /sapi/v1/portfolio/interest-rate`: get portfolio margin interest rate

---

## 2023-02-21

- Adjusted endpoints for Crypto Loan:
  - `POST /sapi/v1/loan/borrow`: paramater `loanTerm` is restricted to 7 or 30

---

## 2023-02-17

The Websocket Stream now only allows 300 connections requests every 5 minutes.

This limit is **per IP address**.

Please be careful when trying to open multiple connections or reconnecting to the Websocket API.

---

## 2023-02-13

- New endpoints for Sub-Account:
  - `GET /sapi/v4/sub-account/assets`: Fetch sub-account assets

---

## 2023-02-02

- New endpoints for Margin:
  - `GET /sapi/v1/margin/exchange-small-liability`: Query the coins which can be small liability
    exchange
  - `POST /sapi/v1/margin/exchange-small-liability`: Cross Margin Small Liability Exchange
  - `GET /sapi/v1/margin/exchange-small-liability-history`: Get Small liability Exchange History
- Update endpoints for Wallet:
  - Universal Transfer `POST /sapi/v1/asset/transfer` support option transfer

---

## 2023-01-26

As per the
[announcement](https://www.binance.com/en/support/announcement/binance-spot-launches-self-trade-prevention-stp-function-on-api-312fd0112fb44635b397c116e56d8f84),
Self Trade Prevention will be enabled at **2023-01-26 08:00 UTC**.

Please refer to `GET /api/v3/exchangeInfo` from the Rest API or `exchangeInfo` from the Websocket
API on the default and allowed modes.

---

## 2023-01-23

New API cluster has been added. Note that all endpoints are functionally equal, but may vary in
performance.

- https://api4.binance.com

---

## 2023-01-19

**ACTUAL RELEASE DATE TBD**

SPOT API

**New Feature**: Self-Trade Prevention (aka STP) will be added to the system at a later date. This
will prevent orders from matching with orders from the same account, or accounts under the same
`tradeGroupId`.

Please refer to `GET /api/v3/exchangeInfo` from the SPOT API or `exchangeInfo` from the Websocket
API on the status.

```javascript
"defaultSelfTradePreventionMode": "NONE",   //If selfTradePreventionMode not provided, this will be the value passed to the engine
"allowedSelfTradePreventionModes": [        //What the allowed modes of selfTradePrevention are
    "NONE",
    "EXPIRE_TAKER",
    "EXPIRE_BOTH",
    "EXPIRE_MAKER"
]
```

- New order status: `EXPIRED_IN_MATCH` - This means that the order expired due to STP being
  triggered.
- New endpoint:
  - `GET /api/v3/myPreventedMatches` - This queries the orders that expired due to STP being
    triggered.
- New optional parameter `selfTradePreventionMode` has been added to the following endpoints:
  - `POST /api/v3/order`
  - `POST /api/v3/order/oco`
  - `POST /api/v3/cancelReplace`
- New responses that will appear for all order placement endpoints if there was a prevented match
  (i.e. if an order could have matched with an order of the same account, or the accounts are in the
  same `tradeGroupId`):
  - `tradeGroupId` - This will only appear if account is configured to a `tradeGroupId` and if there
    was a prevented match.
  - `preventedQuantity` - Only appears if there was a prevented match.
  - An array `preventedMatches` with the following fields:
    - `preventedMatchId`
    - `makerOrderId`
    - `price`
    - `takerPreventedQuantity` - This will only appear if `selfTradePreventionMode` set is
      `EXPIRE_TAKER` or `EXPIRE_BOTH`.
    - `makerPreventedQuantity` - This will only appear if `selfTradePreventionMode` set is
      `EXPIRE_MAKER` or `EXPIRE_BOTH`.
- New fields `preventedMatchId` and `preventedQuantity` that can appear in the order query endpoints
  if the order had expired due to an STP trigger:
  - `GET /api/v3/order`
  - `GET /api/v3/openOrders`
  - `GET /api/v3/allOrders`

USER DATA STREAM

- New execution Type: `TRADE_PREVENTION`
- New fields for `executionReport` (These fields will only appear if the order has expired due to
  STP trigger)
  - `u` - `tradeGroupId`
  - `v` - `preventedMatchId`
  - `U` - `counterOrderId`
  - `A` - `preventedQuantity`
  - `B` - `lastPreventedQuantity`

---

## 2023-01-13

- The following endpoints will be discontinued on January 13, 2023 6:00 AM UTC:
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account enable and
    disable IP restriction for a sub-account API Key
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account add IP
    list for a sub-account API Key
- New endpoints for Sub-Account:
  - `GET /sapi/v1/managed-subaccount/fetch-future-asset`: Investor can use this api to query managed
    sub account futures asset details
  - `GET /sapi/v1/managed-subaccount/marginAsset`: Investor can use this api to query managed sub
    account margin asset details
- New endpoin for Margin:
  - `GET /sapi/v1/margin/crossMarginCollateralRatio`: Get cross margin collateral ratio

---

## 2023-01-05

- New endpoints for Sub-Account:
  - `GET /sapi/v1/managed-subaccount/queryTransLogForInvestor`: Investor can use this api to query
    managed sub account transfer log
  - `GET /sapi/v1/managed-subaccount/queryTransLogForTradeParent`: Trading team can use this api to
    query managed sub account transfer log

---

## 2022-12-26

- New endpoints for wallet:
  - `GET /sapi/v1/capital/contract/convertible-coins`: Get a user's auto-conversion settings in
    deposit/withdrawal
  - `POST /sapi/v1/capital/contract/convertible-coins`: User can use it to turn on or turn off the
    BUSD auto-conversion from/to a specific stable coin.

---

## 2022-12-15

- New RSA signature
  - Documentation has been updated to show how to sign a request using an RSA key.
  - For security reasons, we recommend to use RSA keys instead of HMAC keys when generating an API
    key.
  - We accept `PKCS#8` (BEGIN PUBLIC KEY).
  - More details on how to upload your RSA public key will be added at a later date.

---

## 2022-12-13

REST API

Some error messages on error code `-1003` have changed:

- Previous error message:

`Too much request weight used; current limit is %s request weight per %s %s. Please use the websocket for live updates to avoid polling the API.`

has been updated to:

`Too much request weight used; current limit is %s request weight per %s. Please use WebSocket Streams for live updates to avoid polling the API.`

- Previous error message

`Way too much request weight used; IP banned until %s. Please use the websocket for live updates to avoid bans.`

has been updated to:

`Way too much request weight used; IP banned until %s. Please use WebSocket Streams for live updates to avoid bans.`

---

## 2022-12-05

**Notice:** These changes are being rolled out gradually to all our servers, and will take
approximately a week to complete.

WEBSOCKET

- `!bookTicker` will be removed by **December 7, 2022**. Please use the Individual Book Ticker
  Streams instead. (&lt;symbol&gt;@bookTicker).
  - Multiple &lt;symbol&gt;@bookTicker streams can be subscribed to over one connection. (E.g.
    `wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker/bnbbtc@bookTicker`)

SPOT API

- New error code `-1135`
  - This error code will occur if a parameter requiring a JSON object is invalid.
- New error code `-1108`
  - This error will occur if a value to a parameter being sent was too large, potentially causing
    overflow.
  - This error code can occur in the following endpoints:
    - `POST /api/v3/order`
    - `POST /api/v3/order/cancelReplace`
    - `POST /api/v3/order/oco`
- Changes to `GET /api/v3/aggTrades`
  - Previous behavior: `startTime` and `endTime` had to be used in combination and could only be an
    hour apart.
  - New behavior: `startTime` and `endTime` can be used individually and the 1 hour limit has been
    removed.
    - When using `startTime` only, this will return trades from that time, up to the `limit`
      provided.
    - When using `endTime` only, this will return trades starting from the `endTime` including all
      trades before that time, up to the limit provided.
    - If `limit` not provided, regardless of used in combination or sent individually, the endpoint
      will use the default limit.
- Changes to `GET /api/v3/myTrades`
  - Fixed a bug where `symbol` + `orderId` combination would return all trades even if the number of
    trades went beyond the `500` default limit.
  - Previous behavior: The API would send specific error messages depending on the combination of
    parameters sent. E.g:

    `   {     "code": -1106,     "msg": "Parameter X was sent when not required."   }   `

  - New behavior: If the combinations of optional parameters to the endpoint were not supported,
    then the endpoint will respond with the generic error:

    `   {     "code": -1128,     "msg": "Combination of optional parameters invalid."   }   `

  - Added a new combination of supported parameters: `symbol` + `orderId` + `fromId`.
  - The following combinations of parameters were previously supported but no longer accepted, as
    these combinations were only taking `fromId` into consideration, ignoring `startTime` and
    `endTime`:
    - `symbol` + `fromId` + `startTime`
    - `symbol` + `fromId` + `endTime`
    - `symbol` + `fromId` + `startTime` + `endTime`
  - Thus, these are the supported combinations of parameters:
    - `symbol`
    - `symbol` + `orderId`
    - `symbol` + `startTime`
    - `symbol` + `endTime`
    - `symbol` + `fromId`
    - `symbol` + `startTime` + `endTime`
    - `symbol`+ `orderId` + `fromId`

**Note:** These new fields will appear approximately a week from the release date.

- Changes to `GET /api/v3/exchangeInfo`
  - New fields `defaultSelfTradePreventionMode` and `allowedSelfTradePreventionModes`
- Changes to the Order Placement Endpoints/Order Query/Order Cancellation Endpoints:
  - New field `selfTradePreventionMode` will appear in the response.
  - Affects the following endpoints:
    - `POST /api/v3/order`
    - `POST /api/v3/order/oco`
    - `POST /api/v3/order/cancelReplace`
    - `GET /api/v3/order`
    - `DELETE /api/v3/order`
    - `DELETE /api/v3/orderList`
- Changes to `GET /api/v3/account`
  - New field `requireSelfTradePrevention` will appear in the response.
- New field `workingTime`, indicating when the order started working on the order book, will appear
  in the following endpoints:
  - `POST /api/v3/order`
  - `GET /api/v3/order`
  - `POST /api/v3/order/cancelReplace`
  - `POST /api/v3/order/oco`
  - `GET /api/v3/order`
  - `GET /api/v3/openOrders`
  - `GET /api/v3/allOrders`
- Field `trailingTime`, indicating the time when the trailing order is active and tracking price
  changes, will appear for the following order types (`TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`,
  `STOP_LOSS`, `STOP_LOSS_LIMIT` if `trailingDelta` parameter was provided) for the following
  endpoints:
  - `POST /api/v3/order`
  - `GET /api/v3/order`
  - `GET /api/v3/openOrders`
  - `GET /api/v3/allOrders`
  - `POST /api/v3/order/cancelReplace`
  - `DELETE /api/v3/order`
- Field `commissionRates` will appear in the `GET /api/v3/acccount` response

USER DATA STREAM

- eventType `executionReport` has new fields
  - `V` - `selfTradePreventionMode`
  - `D` - `trailing_time` (Appears if the trailing stop order is active)
  - `W` - `workingTime` (Appears if `isWorking`=`true`)

---

## 2022-12-02

- Added a new market data base URL `https://data.binance.com`.
- Added a new WebSocket URL `wss://data-stream.binance.com`.

---

## 2022-11-29

- New endpoint for VIP Loan:
  - `GET /sapi/v1/loan/vip/collateral/account: Check Locked Value of VIP Collateral Account

---

## 2022-11-22

- New endpoints for Convert:
  - `GET /sapi/v1/convert/exchangeInfo`: Query for all convertible token pairs and the tokens’
    respective upper/lower limits
  - `GET /sapi/v1/convert/assetInfo`: Query for supported asset’s precision information
  - `POST /sapi/v1/convert/getQuote`: Request a quote for the requested token pairs
  - `POST /sapi/v1/convert/acceptQuote`: Accept the offered quote by quote ID.
  - `GET /sapi/v1/convert/orderStatus`: Query order status by order ID.

---

## 2022-11-18

- New endpoint for Wallet:
  - `GET /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage`: The query of Cloud-Mining payment
    and refund history
- New endpoints for Sub-account:
  - `GET /sapi/v1/sub-account/apiRestrictions/ipRestriction/thirdPartyList`: To query Sub-Account
    API key Third Party IP whitelist
  - `POST /sapi/v2/sub-account/subAccountApi/ipRestriction`: To support master account update IP
    Restriction for Sub-Account API key

---

## 2022-11-14

- New endpoints for VIP Loan:
  - `GET /sapi/v1/loan/vip/ongoing/orders`: Get VIP Loan Ongoing Orders
  - `POST /sapi/v1/loan/vip/repay`: VIP Loan Repay
  - `GET /sapi/v1/loan/vip/repay/history`: Get VIP Loan Repayment History

---

## 2022-11-02

- Update endpoints for Wallet:
  - `POST /sapi/v1/capital/withdraw/apply`: Weight changed to Weight(UID): 600

---

## 2022-11-01

- New endpoints for Crypto Loan:
  - `GET /sapi/v1/loan/loanable/data`: Get interest rate and borrow limit of loanable assets. The
    borrow limit is shown in USD value.
  - `GET /sapi/v1/loan/collateral/data`: Get LTV information and collateral limit of collateral
    assets. The collateral limit is shown in USD value.
  - `GET /sapi/v1/loan/repay/collateral/rate`: Get the rate of collateral coin / loan coin when
    using collateral repay, the rate will be valid within 8 second.
  - `POST /sapi/v1/loan/customize/margin_call`: Customize margin call for ongoing orders only.

---

## 2022-10-28

- Update endpoints for Wallet:
  - `POST /sapi/v1/asset/convert-transfer`: New parameter `accountType`
  - `POST /sapi/v1/asset/convert-transfer/queryByPage`: request method is changed to `GET`, new
    parameter `clientTranId`

---

## 2022-10-15

- New endpoints for Binance Code:
  - `POST /sapi/v1/giftcard/buyCode`: For buying a fixed-value Binance Code.
  - `GET /sapi/v1/giftcard/buyCode/token-limit`: To verify which tokens are available for you to
    purchase fixed-value gift cards as mentioned in section 2 and its’ limitation.

---

## 2022-09-30

- Delete endpoints for Futures Cross Collateral:
  - `POST /sapi/v1/futures/loan/borrow`
  - `POST /sapi/v1/futures/loan/repay`
  - `GET /sapi/v1/futures/loan/configs`
  - `GET /sapi/v2/futures/loan/configs`
  - `GET /sapi/v1/futures/loan/calcAdjustLevel`
  - `GET /sapi/v2/futures/loan/calcAdjustLevel`
  - `GET /sapi/v1/futures/loan/calcMaxAdjustAmount`
  - `GET /sapi/v2/futures/loan/calcMaxAdjustAmount`
  - `POST /sapi/v1/futures/loan/adjustCollateral`
  - `POST /sapi/v2/futures/loan/adjustCollateral`
  - `GET /sapi/v1/futures/loan/collateralRepayLimit`
  - `GET /sapi/v1/futures/loan/collateralRepay`
  - `POST /sapi/v1/futures/loan/collateralRepay`
  - `GET /sapi/v1/futures/loan/collateralRepayResult`

---

## 2022-09-30

Scheduled changes to the removal of `!bookTicker` around November 2022.

- The All Book Tickers stream (`!bookTicker`) is set to be removed in **November 2022**
- More details of the actual removal date will be announced at a later time.
- Please use the Individual Book Ticker Streams instead. (`<symbol>@bookTicker`).
- Multiple `<symbol>@bookTicker` streams can be subscribed to over one connection.
  - Example: wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker/bnbbtc@bookTicker

---

## 2022-09-29

- New endpoints for Wallet:
  - `POST /sapi/v1/asset/convert-transfer`: Convert transfer, convert between BUSD and stablecoins.
  - `POST /sapi/v1/asset/convert-transfer/queryByPage`: Query convert transfer

---

## 2022-09-22

- Update endpoint for Sub-Account:
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction`: Add new param `thirdParty`
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`: Add new param `thirdPartyName`
  - `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList`: Add new param `thirdPartyName`
- Add Rate Limit for following endpoints:
  - `GET /sapi/v1/bswap/liquidity`: 3/1s per account and per pool
  - `GET /sapi/v1/bswap/quote`: 3/1s per account and per pool
  - `POST /sapi/v1/lending/daily/purchase`: 1/3s per account
  - `POST /sapi/v1/lending/customizedFixed/purchase`: 1/3s per account
  - `POST /sapi/v1/staking/purchase`: 1/3s per account

---

## 2022-09-16

- New endpoint for Margin：
  - `GET /sapi/v1/margin/tradeCoeff`: Get personal margin level information

---

## 2022-09-15

- New endpoints for Crypto Loan
  - `POST /sapi/v1/loan/borrow`: Borrow - Crypto Loan Borrow
  - `GET /sapi/v1/loan/borrow/history`: Borrow - Get Loan Borrow History
  - `GET/sapi/v1/loan/ongoing/orders`: Borrow - Get Loan Ongoing Orders
  - `POST/sapi/v1/loan/repay`: Repay - Crypto Loan Repay
  - `GET/sapi/v1/loan/repay/history`: Repay - Get Loan Repayment History
  - `POST/sapi/v1/loan/adjust/ltv`: Adjust LTV - Crypto Loan Adjust LTV
  - `GET/sapi/v1/loan/ltv/adjustment/history`: Adjust LTV - Get Loan LTV Adjustment History

---

## 2022-09-15

Note that these are rolling changes, so it may take a few days for it to rollout to all our servers.

- Changes to `GET /api/v3/exchangeInfo`
  - New optional parameter `permissions` added to display all symbols with the permissions matching
    the parameter provided. (eg.`SPOT`, `MARGIN`, `LEVERAGED`)
  - If not provided, the default value will be `["SPOT","MARGIN", "LEVERAGED"]`.
    - This means the request `GET /api/v3/exchangeInfo` without any parameters will show all symbols
      that can be used for `SPOT`,`MARGIN` and/or `LEVERAGED` trading.
    - To search for symbols that can be traded on other permissions (e.g. `TRD_GRP_004`, etc), then
      this needs to be searched for explicitly. (e.g.`permissions`=`TRD_GRP_004`)
  - Cannot be combined with `symbol` or `symbols`

---

## 2022-09-12

- Update endpoint for Sub-account: \* `GET /sapi/v1/sub-account/subAccountApi/ipRestriction`: To
  support master account query Third party IP list name for a sub account API key

---

## 2022-09-05

- Delete endpoint for Futures:
  - `GET /sapi/v1/futures/loan/wallet`

---

## 2022-08-23

SPOT API

Note that these are rolling changes, so it may take a few days for it to rollout to all our servers.

- Changes to `GET /api/v3/ticker` and `GET /api/v3/ticker/24hr`
  - New optional parameter `type` added
  - Supported values for parameter `type` are `FULL` and `MINI`
    - `FULL` is the default value and the response that is currently being returned from the
      endpoint
    - `MINI` omits the following fields from the response: `priceChangePercent`, `weightedAvgPrice`,
      `bidPrice`, `bidQty`, `askPrice`, `askQty`, and `lastQty`
- New error code `-1008`
  - This is sent whenever the servers are overloaded with requests.
  - This error code only appears for the SPOT API.
- New field `brokered` has been added to `GET /api/v3/account`
- New endpoint: `GET /api/v3/uiKlines`
- New kline interval: `1s`

---

## 2022-08-18

- Update endpoint for Convert:
  - `GET /sapi/v1/convert/tradeFlow`: Update weight from Weight(IP) 3000 to Weight(UID) 3000.

---

## 2022-08-08

SPOT API

- Changes to `POST /api/v3/order` and `POST /api/v3/order/cancelReplace`
  - New optional field `strategyId` is a parameter used to identify an order as part of a strategy.
  - New optional field `strategyType` is a parameter used to identify what strategy was running.
    (E.g. If all the orders are part of spot grid strategy, it can be set to `strategyType=1000000`)
  - **Note:** `strategyType` cannot be less than `1000000`.
- Changes to `POST /api/v3/order/oco`
  - New optional fields `limitStrategyId`, `limitStrategyType`. `stopStrategyId`, `stopStrategyType`
  - These are the strategy metadata parameters for both legs of the OCO orders.
  - `limitStrategyType` and `stopStrategyType` both cannot be less than `1000000`.
- Changes to `GET /api/v3/order`, `GET /api/v3/openOrders`, and `GET /api/v3/allOrders`
  - New fields `strategyId` and `strategyType` will appear in the response JSON for orders that had
    these fields populated upon order placement.
- Changes to `DELETE /api/v3/order` and `DELETE /api/v3/openOrders`
  - New fields `strategyId` and `strategyType` will appear in the response JSON for cancelled orders
    that had these fields populated upon order placement.

USER DATA STREAM

- New fields to eventType `executionReport`
  - `j` for `strategyId`
  - `J` for `strategyType`
  - Note that these fields only appear if these were populated upon order placement.

---

## 2022-08-05

- Update endpoint for Convert:
  - `GET /sapi/v1/convert/tradeFlow`: Update weight from Weight(IP) 100 to Weight(IP) 3000.

---

## 2022-07-21

- New endpoint for Portfolio Margin:
  - `GET /sapi/v1/portfolio/pmLoan` Query Portfolio Margin Bankruptcy Loan Record
  - `POST /sapi/v1/portfolio/repay` Portfolio Margin Bankruptcy Loan Repay

---

## 2022-07-18

- New endpoint for Portfolio Margin:
  - `GET /sapi/v1/portfolio/collateralRate` to get Portfolio Margin Collateral Rate.

---

## 2022-07-01

- New endpoint for Wallet:
  - `POST /sapi/v3/asset/getUserAsset` to get user assets.
- New endpoint for Margin:
  - `GET /sapi/v1/margin/dribblet` to query the historical information of user's margin account
    small-value asset conversion BNB.
- Update endpoint for Convert:
  - `GET /sapi/v1/convert/tradeFlow`: Update weight from 3000 to 100.
- Update endpoint for Margin:
  - `GET /sapi/v1/margin/repay`: Add response field rawAsset.

---

## 2022-06-20

SPOT API: Changes to `GET /api/v3/ticker`

- Weight has been reduced from 5 to 2 per symbol, regardless of `windowSize`.
- The max number of symbols that can be processed in a request is 100.
  - If the number of `symbols` sent is more than 100, the error will be as follows:

```json
{
  "code": -1101,
  "msg": "Too many values sent for parameter 'symbols', maximum allowed up to 100."
}
```

- The max Weight(IP) for this endpoint will cap at 100.
  - I.e. If the request has more than 50 symbols, the Weight will still be 100, regardless of
    `windowSize`.

---

## 2022-06-15

**Note:** The update is being rolled out over the next few days, so these changes may not be visible
right away.

- `GET /api/v3/ticker` added
  - Rolling window price change statistics based on `windowSize` provided.
  - Contrary to `GET /api/v3/ticker/24hr` the list of symbols cannot be omitted.
  - If `windowSize` not specified, the value will default to `1d`.
  - Response is similar to `GET /api/v3/ticker/24hr`, minus the following fields: `prevClosePrice`,
    `lastQty`, `bidPrice`, `bidQty`, `askPrice`, `askQty`
- `POST /api/v3/order/cancelReplace` added
  - Cancels an existing order and places a new order on the same symbol.
  - The filters are evaluated **before** the cancel order is placed.
    - e.g. If the `MAX_NUM_ORDERS` filter is 10, and the total number of open orders on the account
      is also 10, when using `POST /api/v3/order/cancelReplace` both the cancel order placement and
      new order will fail because of the filter.
  - The change is being rolled out in the next few days, thus this feature will be enabled once the
    upgrade is completed.
- `GET /api/v3/exchangeInfo` returns new field `cancelReplaceAllowed` in `symbols` list.
- New filter `NOTIONAL` has been added.
  - Defines the allowed notional value (`price * quantity`) based on a configured `minNotional` and
    `maxNotional`
- New exchange filter `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` has been added.
  - Defines the limit of open iceberg orders on an account

WEBSOCKETS

- New symbol ticker streams with 1h and 4h windows:
  - Individual symbol ticker streams
    - `<symbol>@ticker_<window-size>`
  - All market ticker streams
    - `!ticker_<window-size>@arr`

---

## 2022-06-02

- Update endpoint for Subaccount:
  - `GET /sapi/v1/sub-account/sub/transfer/history`: fromEmail and toEmail can be master email.

---

## 2022-05-31

- Update endpoint for Fiat:
  - `GET /sapi/v1/fiat/orders`: Weight changes from UID(3000) to UID(90000)
- Update endpoint for Pay:
  - `GET /sapi/v1/pay/transactions`: Param names changed: startTimestamp -> startTime; endTimestamp
    -> endTime.

---

## 2022-05-26

- Update endpoint for Fiat:
  - `GET /sapi/v1/fiat/orders`: Weight changes from IP(1) to UID(3000)
- Update info for the following margin account endpoints: The max interval between `startTime` and
  `endTime` is 30 days.:
  - `GET /sapi/v1/margin/transfer`
  - `GET /sapi/v1/margin/loan`
  - `GET /sapi/v1/margin/repay`
  - `GET /sapi/v1/margin/isolated/transfer`
  - `GET /sapi/v1/margin/interestHistory`

---

## 2022-05-23

- Changes to Order Book Depth Levels
  - Quantities in the Depth levels were returning negative values in situations where they were
    exceeding the max value, resulting in an overflow.
  - Going forward depth levels will not overflow, but will be capped at the max value based on the
    precision of the base asset. This means that the depth level is at max value _or more_.
    - E.g. If the precision is 8, then the max value for quantity will be at
      92,233,720,368.54775807.
  - When the fix has been applied, a change in the order book at the affected price level is
    required for the changes to be visible.
- What does this affect?
  - SPOT API
    - `GET /api/v3/depth`
  - Websocket Streams
    - `<symbol>@depth`
    - `<symbol>@depth@100ms`
    - `<symbol>@depth<levels>`
    - `<symbol>@depth<levels>@100ms`

- Updates to `MAX_POSITION`
  - If an order's `quantity` can cause the position to overflow, this will now fail the
    `MAX_POSITION` filter.

---

## 2022-05-19

- Update endpoint for Mining:
  - `GET /sapi/v1/mining/pub/algoList` and `GET /sapi/v1/mining/pub/coinList`: Need no parameter.
- Add error codes (21xxx) for Portfolio Margin Account: -21001, -21002, -21003

---

## 2022-05-17

SPOT API

- Changes to `GET api/v3/aggTrades`
  - When providing `startTime` and `endTime`, the oldest items are returned.
- Changed error messaging on `GET /api/v3/myTrades` where parameter `symbol` is not provided:

```json
{
  "code": -1102,
  "msg": "Mandatory parameter 'symbol' was not sent, was empty/null, or malformed."
}
```

- The following endpoints now support multi-symbol querying using the parameter `symbols`.
  - `GET /api/v3/ticker/24hr`
  - `GET /api/v3/ticker/price`
  - `GET /api/v3/ticker/bookTicker`
- In the above, the request weight will depend on the number of symbols provided in `symbols`.
  <br></br> Please refer to the table below:

| Endpoint                        | Number of Symbols | Weight |
| ------------------------------- | ----------------- | ------ |
| `GET /api/v3/ticker/price`      | Any               | 2      |
| `GET /api/v3/ticker/bookTicker` | Any               | 2      |
| `GET /api/v3/ticker/24hr`       | 1-20              | 1      |
| `GET /api/v3/ticker/24hr`       | 21-100            | 20     |
| `GET /api/v3/ticker/24hr`       | 101 or more       | 40     |

---

## 2022-05-05

- New endpoint for Binance Code:
  - `GET /sapi/v1/giftcard/cryptography/rsa-public-key` to fetch RSA public key.
- Update endpoint for Binance Code:
  - `POST /sapi/v1/giftcard/redeemCode`: new optional parameter `externalUid`. Each external unique
    ID represents a unique user on the partner platform. The function helps you to identify the
    redemption behavior of different users.

---

## 2022-04-28

- New endpoints for Staking:
  - `GET /sapi/v1/staking/productList` to get Staking product list
  - `POST /sapi/v1/staking/purchase` to stake product
  - `POST /sapi/v1/staking/redeem` to redeem product
  - `GET /sapi/v1/staking/position` to get Staking product holding position
  - `GET /sapi/v1/staking/stakingRecord` to inquiry Staking history records
  - `POST /sapi/v1/staking/setAutoStaking` to set Auto Staking function
  - `GET /sapi/v1/staking/personalLeftQuota` to inquiry Staking left quota

---

## 2022-04-27

- New endpoint for Futures Algo：
  - `POST /sapi/v1/algo/futures/newOrderTwap` to support Twap new order

FAQ:
[Time-Weighted Average Price(Twap) Introduction](https://www.binance.com/en/support/faq/093927599fd54fd48857237f6ebec0b0)

---

## 2022-04-26

- `GET /sapi/v1/margin/rateLimit/order` added
  - The endpoint will display the user's current margin order count usage for all intervals.

---

## 2022-04-20

- New endpoint for Portfolio Margin:
  - `GET /sapi/v1/portfolio/account` to support query portfolio margin account info

FAQ:
[Portfolio Margin Program](https://www.binance.com/en/support/faq/5054378212d240cca17ecd6006c11f23)

Only Portfolio Margin Account is accessible to this endpoint. To enroll, kindly refer to:
[How to Enroll into the Binance Portfolio Margin Program](https://www.binance.com/en/support/faq/a7834b9bc03140728583a90bcb469144)

---

## 2022-04-13

- New endpoints for Futures Algo：
  - `POST /sapi/v1/algo/futures/newOrderVp` to support VP new order
  - `DELETE  /sapi/v1/algo/futures/order` to support cancel Algo order
  - `GET  /sapi/v1/algo/futures/openOrders` to support query Algo open orders
  - `GET  /sapi/v1/algo/futures/historicalOrders` to support query Algo historical orders
  - `GET  /sapi/v1/algo/futures/subOrders` to support query Algo sub orders for a specified algoId

FAQ:
[Volume Participation(VP) Introduction](https://www.binance.com/en/support/faq/b0b94dcc8eb64c2585763b8747b60702)

---

## 2022-04-13

**Information on Trailing Stops**

SPOT API

- Trailing Stops have been enabled.
  - This is a type of algo order where the activation is based on a percentage of a price change in
    the market using the new parameter `trailingDelta`.
  - This can only used with any of the following order types: `STOP_LOSS`, `STOP_LOSS_LIMIT`,
    `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.
  - The `trailingDelta` parameter will be done in Basis Points or BIPS.
    - For example: a STOP_LOSS SELL order with a `trailingDelta` of 100 will trigger after a price
      decrease of 1%. (100 / 10,000 => 0.01 => 1%)
  - When used in combination with OCO Orders, the `trailingDelta` will determine when the contingent
    leg of the OCO will trigger.
  - When `trailingDelta` is used in combination with `stopPrice`, once the `stopPrice` condition is
    met, the trailing stop starts tracking the price change from the `stopPrice` based on the
    `trailingDelta` provided.
  - When no `stopPrice` is sent, the trailing stop starts tracking the price changes from the last
    price based on the `trailingDelta` provided.
- Changes to POST `/api/v3/order`
  - New optional field `trailingDelta`
- Changes to POST `/api/v3/order/test`
  - New optional field `trailingDelta`
- Changes to POST `/api/v3/order/oco`
  - New optional field `trailingDelta`
- A new filter `TRAILING_DELTA` has been added.
  - This filter is defined by the minimum and maximum values for the `trailingDelta` value.

USER DATA STREAM

- New field in `executionReport`
  - "d" for `trailingDelta`

---

## 2022-04-12

**Note:** The changes are being rolled out during the next few days, so these will not appear right
away.

- Error message changed on `GET api/v3/allOrders` where `symbol` is not provided: <br></br>
  ```
  {
   "code": -1102,
   "msg": "Mandatory parameter 'symbol' was not sent, was empty/null, or malformed."
  }
  ```
- Fixed a typo with an error message when an account has disabled permissions (e.g. to withdraw, to
  trade, etc) <br></br>
  ```
  "This action is disabled on this account."
  ```
- During a market data audit, we detected some issues with the Spot aggregate trade data.
  - Missing aggregate trades were recovered.
  - Duplicated records were marked invalid with the following values:
    - p = '0' // price
    - q = '0' // qty
    - f = -1 // ﬁrst_trade_id
    - l = -1 // last_trade_id

---

## 2022-04-08

- Update WEBSOCKET for BLVT：\* Base url changed to `wss://nbstream.binance.com/lvt-p` for BLVT
  streams `<tokenName>@tokenNav` and `<tokenName>@nav_Kline_<interval>`

---

## 2022-3-29

The following updates will take effect on **March 31, 2022 08:00 AM UTC**

- Update endpoint for Sub-account：
  - `GET /sapi/v1/sub-account/universalTransfer`

The query time period must be less then 30 days; If `startTime` and `endTime` not sent, return
records of the last 30 days by default

---

## 2022-03-25

- Update endpoint for Sub-Account:
  - New endpoint`GET /sapi/v1/managed-subaccount/accountSnapshot` to support investor master account
    query asset snapshot of managed sub-account

---

## 2022-03-08

- Update endpoint for Sub-Account:
  - New transfer types`MARGIN`,`ISOLATED_MARGIN` and parameter`symbol`added
    in`POST /sapi/v1/sub-account/universalTransfer` to support transfer to sub-account cross margin
    account and isolated margin account

---

## 2022-02-28

- New field `allowTrailingStop` has been added to `GET /api/v3/exchangeInfo`

---

## 2022-02-22

SPOT API

- `(price-minPrice) % tickSize == 0` rule in `PRICE_FILTER` has been changed to
  `price % tickSize == 0`.
- A new filter `PERCENT_PRICE_BY_SIDE` has been added.
- Changes to GET `api/v3/depth`
  - The `limit` value can be outside of the previous values (i.e. 5, 10, 20, 50, 100, 500,
    1000,5000) and will return the correct limit. (i.e. if limit=3 then the response will be the top
    3 bids and asks)
  - The limit still cannot exceed 5000. If the limit provided is greater than 5000, then the
    response will be truncated to 5000.
  - Due to the changes, these are the updated request weights based on the limit value provided:

| Limit     | Request Weight |
| --------- | -------------- |
| 1-100     | 1              |
| 101-500   | 5              |
| 501-1000  | 10             |
| 1001-5000 | 50             |

- Changes to GET `api/v3/aggTrades`
  - When providing `startTime` and `endTime`, the oldest items are returned.

---

## 2022-2-18

- Update endpoint for Sub-Account:
  - New fields `isManagedSubAccount`and `isAssetManagementSubAccount` added
    in`GET /sapi/v1/sub-account/list`to support query whether the sub-account is a managed
    sub-account or a asset management sub-account

---

## 2022-2-17

The following updates will take effect on **February 24, 2022 08:00 AM UTC**

- Update endpoint for Wallet：
  - `GET /sapi/v1/accountSnapshot`

The time limit of this endpoint is shortened to only support querying the data of the latest month

---

## 2022-2-09

- New endpoint for Wallet:
  - `POST /sapi/v1/asset/dust-btc` to get assets that can be converted into BNB

---

## 2022-1-25

- From **January 28, 2022 4:00 AM UTC**, You need to open`Enable Spot & Margin Trading`permission
  for the API key which requests these endpoints as following：
  - `POST /sapi/v1/asset/dust` Dust transfer
  - `POST /sapi/v1/lending/daily/purchase` Purchase Savings flexible product
  - `POST /sapi/v1/lending/daily/redeem` Redeem Savings flexible product
  - `POST /sapi/v1/lending/customizedFixed/purchase` Purchase Savings Fixed/Activity project
  - `POST /sapi/v1/lending/positionChanged` Change Savings Fixed/Activity position to Daily position
  - `POST /sapi/v1/bswap/liquidityAdd` Bswap add liquidity
  - `POST /sapi/v1/bswap/liquidityRemove` Bswap remove liquidity
  - `POST /sapi/v1/bswap/swap` Bswap swap
  - `POST /sapi/v1/bswap/claimRewards` Bswap claim rewards

---

## 2022-1-21

- New endpoints for Binance Code:
  - `POST /sapi/v1/giftcard/createCode` to create a Binance Code.
  - `POST /sapi/v1/giftcard/redeemCode` to redeem a Binance Code.
  - `GET /sapi/v1/giftcard/verify` to verify a Binance Code.

---

## 2022-1-4

- New endpoint for Mining:
  - `GET /sapi/v1/mining/payment/uid` to get Mining account earning.

- New endpoints for BSwap:
  - `GET /sapi/v1/bswap/unclaimedRewards` to get unclaimed rewards record.
  - `POST /sapi/v1/bswap/claimRewards` to claim swap rewards or liquidity rewards.
  - `GET /sapi/v1/bswap/claimedHistory` to get history of claimed rewards.

---

## 2021-12-30

- Update endpoint for Margin：
  - Removed out `limit` from`GET /sapi/v1/margin/interestRateHistory`; The max interval between
    startTime and endTime is 30 days.

- Update endpoint for Wallet：
  - As the Mining account is merged into Funding account, transfer types MAIN_MINING, MINING_MAIN,
    MINING_UMFUTURE, MARGIN_MINING, and MINING_MARGIN will be discontinued in Universal Transfer
    endpoint `POST /sapi/v1/asset/transfer` on **January 05, 2022 08:00 AM UTC**

---

## 2021-12-29

- Removed out dated "Symbol Type" enum; added "Permissions" enum.

---

## 2021-12-24

- Update endpoints for Sub-Account:
  - New parameter`clientTranId`added in`POST /sapi/v1/sub-account/universalTransfer` and
    `GET /sapi/v1/sub-account/universalTransfer` to support custom transfer id

---

## 2021-12-03

- New endpoints for Margin:
  - `GET  /sapi/v1/margin/crossMarginData` to get cross margin fee data collection
  - `GET  /sapi/v1/margin/isolatedMarginData` to get isolated margin fee data collection
  - `GET  /sapi/v1/margin/isolatedMarginTier` to get isolated margin tier data collection

- New endpoints for NFT:
  - `GET  /sapi/v1/nft/history/transactions` to get NFT transaction history
  - `GET  /sapi/v1/nft/history/deposit` to get NFT deposit history
  - `GET  /sapi/v1/nft/history/withdraw` to get NFT withdraw history
  - `GET  /sapi/v1/nft/user/getAsset` to get NFT asset

---

## 2021-11-30

- New endpoint for Convert:
  - `GET  /sapi/v1/convert/tradeFlow` to support user query convert trade history records

- New endpoint for Rebate:
  - `GET  /sapi/v1/rebate/taxQuery` to support user query spot rebate history records

---

## 2021-11-19

- New endpoint for Pay:
  - `GET /sapi/v1/pay/transactions`to support user query Pay trade history
- Update endpoint for Wallet:
  - New field`info`added in`GET /sapi/v1/capital/withdraw/history`to show the reason for withdrawal
    failure

---

## 2021-11-18

The following updates will take effect on **November 25, 2021 08:00 AM UTC**

- Update endpoint for Wallet：
  - `GET /sapi/v1/accountSnapshot`

The query time range of both endpoints are shortened to support data query within the last 6 months
only, where startTime does not support selecting a timestamp beyond 6 months. If you do not specify
startTime and endTime, the data of the last 7 days will be returned by default.

---

## 2021-11-17

- The following endpoints will be discontinued on **November 17, 2021 13:00 PM UTC**:
  - `POST /sapi/v1/account/apiRestrictions/ipRestriction` to support user enable and disable IP
    restriction for an API Key
  - `POST /sapi/v1/account/apiRestrictions/ipRestriction/ipList` to support user add IP list for an
    API Key
  - `GET /sapi/v1/account/apiRestrictions/ipRestriction` to support user query IP restriction for an
    API Key
  - `DELETE /sapi/v1/account/apiRestrictions/ipRestriction/ipList` to support user delete IP list
    for an API Key

---

## 2021-11-16

- New endpoints for Sub-Account:
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account enable and
    disable IP restriction for a sub-account API Key
  - `POST /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account add IP
    list for a sub-account API Key
  - `GET /sapi/v1/sub-account/subAccountApi/ipRestriction` to support master account query IP
    restriction for a sub-account API Key
  - `DELETE /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList` to support master account
    delete IP list for a sub-account API Key

---

## 2021-11-09

- New endpoints for Wallet:
  - `POST /sapi/v1/account/apiRestrictions/ipRestriction` to support user enable and disable IP
    restriction for an API Key
  - `POST /sapi/v1/account/apiRestrictions/ipRestriction/ipList` to support user add IP list for an
    API Key
  - `GET /sapi/v1/account/apiRestrictions/ipRestriction` to support user query IP restriction for an
    API Key
  - `DELETE /sapi/v1/account/apiRestrictions/ipRestriction/ipList` to support user delete IP list
    for an API Key

---

## 2021-11-08

- New endpoint for Crypto Loans:
  - New endpoint`GET /sapi/v1/loan/income`to support user query crypto loans income history

---

## 2021-11-05

- Update endpoint for Wallet:
  - New parameter `walletType `added in `POST /sapi/v1/capital/withdraw/apply` to support user
    choose wallet type `spot wallet` and `funding wallet` when withdraw crypto.

---

## 2021-11-04

The following updates will take effect on **November 11, 2021 08:00 AM UTC**

- Update endpoints for Wallet and Futures：
  - `GET /sapi/v1/asset/transfer`
  - `GET /sapi/v1/futures/transfer`

The query time range of both endpoints are shortened to support data query within the last 6 months
only, where startTime does not support selecting a timestamp beyond 6 months. If you do not specify
startTime and endTime, the data of the last 7 days will be returned by default.

---

## 2021-11-01

- `GET /api/v3/rateLimit/order` added
  - The endpoint will display the user's current order count usage for all intervals.
  - This endpoint will have a request weight of 20.

---

## 2021-10-22

- Update endpoint for Wallet:
  - New transfer types
    `MAIN_FUNDING`,`FUNDING_MAIN`,`FUNDING_UMFUTURE`,`UMFUTURE_FUNDING`,`MARGIN_FUNDING`,`FUNDING_MARGIN`,`FUNDING_CMFUTURE`and
    `CMFUTURE_FUNDING` added in Universal Transfer endpoint `POST /sapi/v1/asset/transfer` and
    `GET /sapi/v1/asset/transfer` to support transfer assets among funding account and other
    accounts
  - As the C2C account, Binance Payment, Binance Card and other business account are merged into a
    Funding account, transfer types
    `MAIN_C2C`,`C2C_MAIN`,`C2C_UMFUTURE`,`C2C_MINING`,`UMFUTURE_C2C`,`MINING_C2C`,`MARGIN_C2C`,`C2C_MARGIN`,`MAIN_PAY`and
    `PAY_MAIN` will be discontinued in Universal Transfer endpoint `POST /sapi/v1/asset/transfer`
    and `GET /sapi/v1/asset/transfer` on **November 04, 2021 08:00 AM UTC**

---

## 2021-10-14

- Update the time range of the response data for the following margin account endpoints, `startTime`
  and `endTime` time span will not exceed 30 days, without time parameter sent the system will
  return the last 7 days of data by default, while the `archived` parameter is `true`, the system
  will return the last 7 days of data 6 months ago by default:
  - `GET /sapi/v1/margin/transfer`
  - `GET /sapi/v1/margin/loan`
  - `GET /sapi/v1/margin/repay`
  - `GET /sapi/v1/margin/isolated/transfer`
  - `GET /sapi/v1/margin/interestHistory`

---

## 2021-09-18

- New endpoints for BSwap:
  - `GET /sapi/v1/bswap/poolConfigure` to get pool configure
  - `GET /sapi/v1/bswap/addLiquidityPreview` to get add liquidity preview
  - `GET /sapi/v1/bswap/removeLiquidityPreview` to get remove liquidity preview

---

## 2021-09-17

- Add`/api/*`and`/sapi/*` limit introduction in General Info

---

## 2021-09-08

- Add endpoints for enabled isolated margin account limit:
  - `DELETE /sapi/v1/margin/isolated/account` to disable isolated margin account for a specific
    symbol
  - `POST /sapi/v1/margin/isolated/account` to enable isolated margin account for a specific symbol
  - `GET /sapi/v1/margin/isolated/accountLimit` to query enabled isolated margin account limit

- New field "enabled" in response of `GET /sapi/v1/margin/isolated/account` to check if the isolated
  margin account is enabled

---

## 2021-09-03

- Update endpoint for Wallet: _ New fields `sameAddress`,`depositDust` and
  `specialWithdrawTips`added in `GET /sapi/v1/capital/config/getall` `sameAddress` means if the coin
  needs to provide memo to withdraw `depositDust` means minimum creditable amount
  `specialWithdrawTips` means special tips for withdraw _ New field `confirmNo`added in
  `GET /sapi/v1/capital/withdraw/history` to support query confirm times for withdraw history

---

## 2021-08-27

- Update endpoint for Wallet:
  - New parameter `withdrawOrderId`added in `GET  /sapi/v1/capital/withdraw/history` to support user
    query withdraw history by withdrawOrderId
  - New field `unlockConfirm`added in `GET /sapi/v1/capital/deposit/hisrec` to support query network
    confirm times for unlocking

---

## 2021-08-23

- New endpoints for Margin Account OCO:
  - `POST /sapi/v1/margin/order/oco`
  - `DELETE /sapi/v1/margin/orderList`
  - `GET /sapi/v1/margin/orderList`
  - `GET /sapi/v1/margin/allOrderList`
  - `GET /sapi/v1/margin/openOrderList`

Same usage as spot account OCO

---

## 2021-08-20

- Update endpoint for Wallet:
  - New parameters`fromSymbol`,`toSymbol`and new transfer types `ISOLATEDMARGIN_MARGIN`,
    `MARGIN_ISOLATEDMARGIN`and `ISOLATEDMARGIN_ISOLATEDMARGIN` added in
    `POST /sapi/v1/asset/transfer` and `GET /sapi/v1/asset/transfer` to support user transfer assets
    between Margin(cross) account and Margin(isolated) account

---

## 2021-08-12

- GET `api/v3/myTrades` has a new optional field `orderId`

---

## 2021-08-05

- New endpoint for C2C:
  - `GET /sapi/v1/c2c/orderMatch/listUserOrderHistory` to query user C2C trade history

---

## 2021-08-05

- Update endpoints for Savings:
  - `GET /sapi/v1/lending/union/purchaseRecord`
  - `GET /sapi/v1/lending/union/redemptionRecord`
  - `GET /sapi/v1/lending/union/interestHistory`

The time between `startTime` and `endTime` cannot be longer than 30 days.
If `startTime` and `endTime` are both not sent, then the last 30 days' data will be returned

---

## 2021-07-29

- Update endpoint for Sub-Account:
  - `GET /sapi/v1/sub-account/transfer/subUserHistory` if `startTime`and`endTime`are not sent, the
    recent 30-day data will be returned by default

---

## 2021-07-27

- New endpoint for Fiat:
  - `GET /sapi/v1/fiat/orders` to query user fiat deposit and withdraw history
  - `GET /sapi/v1/fiat/payments` to query user fiat payments history

---

## 2021-07-16

- New endpoint for Wallet:
  - `GET /sapi/v1/account/apiRestrictions` to query user API Key permission

---

## 2021-07-09

- New endpoint for Wallet:
  - `POST /sapi/v1/asset/get-funding-asset` to query funding wallet, includes Binance Pay, Binance
    Card, Binance Gift Card, Stock Token

---

## 2021-06-24

- Update endpoints for Wallet:
  - `GET /sapi/v1/capital/withdraw/history` added default value 1000, max value 1000 for the
    parameter`limit`
  - `GET /sapi/v1/capital/deposit/hisrec` added default value 1000, max value 1000 for the
    parameter`limit`

---

## 2021-06-17

- Update endpoint for Savings:
  - `GET /sapi/v1/lending/daily/product/list` to include new parameters `current` and `size`

---

## 2021-06-15

- New endpoints for Sub-Account:
  - `POST /sapi/v1/managed-subaccount/deposit ` to deposit assets into the managed sub-account (only
    for investor master account)
  - `GET /sapi/v1/managed-subaccount/asset` to query managed sub-account asset details (only for
    investor master account)
  - `POST /sapi/v1/managed-subaccount/withdraw` to withdrawal assets from the managed sub-account
    (only for investor master account)

---

## 2021-06-04

On **August 01, 2021 02:00 AM UTC** the WAPI endpoints will be discontinued:

- `GET /wapi/v3/systemStatus.html`
- `POST /wapi/v3/withdraw.html`
- `GET /wapi/v3/depositHistory.html`
- `GET /wapi/v3/withdrawHistory.html`
- `GET /wapi/v3/depositAddress.html`
- `GET /wapi/v3/accountStatus.html`
- `GET /wapi/v3/apiTradingStatus.html`
- `GET /wapi/v3/userAssetDribbletLog.html`
- `GET /wapi/v3/assetDetail.html`
- `GET /wapi/v3/tradeFee.html`
- `GET /wapi/v3/sub-account/list.html`
- `GET /wapi/v3/sub-account/transfer/history.html`
- `POST /wapi/v3/sub-account/transfer.html`
- `GET /wapi/v3/sub-account/assets.html`

The WAPI endpoints have been removed from Binance API Documentation.To ensure your trading
strategies are not affected, all API users are encouraged to upgrade trading bots to SAPI endpoints
as soon as possible.

---

## 2021-05-26

- Update endpoint for Wallet:
  - New transfer types `MAIN_PAY` ,`PAY_MAIN` added in Universal Transfer endpoint
    `POST /sapi/v1/asset/transfer` and `GET /sapi/v1/asset/transfer` to support trasnfer assets
    between spot account and pay account

---

## 2021-05-12

- Added `Data Source` in the documentation to explain where each endpoint is retrieving its data
- Added field `Data Source` to each Spot API endpoint in the documentation
- GET `api/v3/exchangeInfo` now supports single or multi-symbol query

---

## 2021-04-28

On **May 15, 2021 08:00 UTC** the SAPI Create Margin Account endpoint will be discontinued:

- `POST /sapi/v1/margin/isolated/create`

Isolated Margin account creation and trade preparation can be completed directly through Isolated
Margin funds transfer `POST /sapi/v1/margin/isolated/transfer`

---

## 2021-04-26

On **April 28, 2021 00:00 UTC** the weights to the following endpoints will be adjusted:

- `GET /api/v3/order` weight increased to 2
- `GET /api/v3/openOrders` weight increased to 3
- `GET /api/v3/allOrders` weight increased to 10
- `GET /api/v3/orderList` weight increased to 2
- `GET /api/v3/openOrderList` weight increased to 3
- `GET /api/v3/account` weight increased to 10
- `GET /api/v3/myTrades` weight increased to 10
- `GET /api/v3/exchangeInfo` weight increased to 10

---

## 2021-04-08

- Update endpoint for Sub-Account:
  - `GET /sapi/v1/sub-account/futures/accountSummary` and
    `GET /sapi/v2/sub-account/futures/accountSummary` the unit of field `asset` changed to
    USD valued summary of sub-account assets

---

## 2021-04-02

- New endpoints for Wallet:
  - `GET /sapi/v1/system/status` to query system status
  - `GET /sapi/v1/account/status` to query account status
  - `GET /sapi/v1/account/apiTradingStatus` to query account API trading status
  - `GET /sapi/v1/asset/dribblet` to query dust log
  - `GET /sapi/v1/asset/assetDetail` to query asset detail
  - `GET /sapi/v1/asset/tradeFee` to query trade fee
- New endpoint for Sub-Account:
  - `GET /sapi/v3/sub-account/assets` to query sub-account assets

---

## 2021-04-01

- Update endpoint for Sub-Account:
  - `GET /sapi/v1/sub-account/transfer/subUserHistory` new fields `fromAccountType` and
    `toAccountType` added in response

---

## 2021-03-31

- Update endpoint for Sub-Account:
  - `GET /wapi/v3/sub-account/transfer/history.html` added new parameters `fromEmail` and `toEmail`,
    the original parameter`email` is equal to`fromEmail`by default

---

## 2021-03-08

- New endpoint for Sub-Account:
  - `POST /sapi/v1/sub-account/virtualSubAccount` to support create a virtual sub-account
  - `GET /sapi/v1/sub-account/list` to support query sub-account list
  - `POST /sapi/v1/sub-account/blvt/enable` to support enable blvt for sub-account

---

## 2021-03-05

- New endpoints for Margin:
  - `GET /sapi/v1/margin/interestRateHistory` to support margin interest rate history query

---

## 2021-02-08

- New endpoints for Futures:
  - `GET /sapi/v2/futures/loan/wallet` to support BUSD loan query
  - `GET /sapi/v2/futures/loan/configs` to support BUSD loan query
  - `GET /sapi/v2/futures/loan/calcAdjustLevel` to support BUSD loan
  - `GET /sapi/v2/futures/loan/calcMaxAdjustAmount` to support adjustment of BUSD loan
  - `POST /sapi/v2/futures/loan/adjustCollateral` to support adjustment of BUSD loan
- Update endpoints for Futures
  - `GET /sapi/v1/futures/loan/adjustCollateral/history` new parameter and fields in response
    `loanCoin` for BUSD loan
  - `GET /sapi/v1/futures/loan/liquidationHistory` new parameter and fields in response `loanCoin`
    for BUSD loan

---

## 2021-02-04

- New transfer types `MARGIN_MINING` ,`MINING_MARGIN`, `MARGIN_C2C` ,`C2C_MARGIN`,
  `MARGIN_CMFUTURE`, `CMFUTURE_MARGIN` added in Universal Transfer endpoint
  `POST /sapi/v1/asset/transfer` and `GET /sapi/v1/asset/transfer`.

---

## 2021-01-15

- New endpoint `DELETE /sapi/v1/margin/openOrders` for Margin Trade
  - This will allow a user to cancel all open orders on a single symbol for margin account.
  - This endpoint will cancel all open orders including OCO orders for margin account.

---

## 2021-01-10

- New parameter `pageSize` for Mining endpoint `GET /sapi/v1/mining/payment/list`
- New fields in response to Mining endpoint `GET /sapi/v1/mining/payment/list`:
  - "type" for income type
  - "hashTransfer" for resale Hashrate
  - "transferAmount" for transferred Income

- New Mining endpoints:
  - `GET /sapi/v1/mining/payment/other`
  - `GET /sapi/v1/mining/hash-transfer/config/details`
  - `GET /sapi/v1/mining/hash-transfer/config/details/list`
  - `GET /sapi/v1/mining/hash-transfer/profit/details`
  - `POST /sapi/v1/mining/hash-transfer/config`
  - `POST /sapi/v1/mining/hash-transfer/config/cancel`

---

## 2021-01-01

USER DATA STREAM

- `outboundAccountInfo` has been removed.

---

## 2020-12-30

- New endpoint for Wallet:
  - `POST   /sapi/v1/asset/transfer` to support user universal transfer among Spot, Margin, Futures,
    C2C, MINING accounts.
  - `GET   /sapi/v1/asset/transfer` to get user universal transfer history.

---

## 2020-12-22

- New endpoint for Sub-Account:
  - `GET /sapi/v1/sub-account/sub/transfer/history` to get spot asset transfer history.

---

## 2020-12-11

- Update endpoints for Futures Cross-Collateral:
  - `GET /sapi/v1/futures/loan/wallet` new fields in response `interestFreeLimit` for total interest
    free limit, `interestFreeLimitUsed` for interest free limit used.
  - `GET /sapi/v1/futures/loan/interestHistory` new fields in response `interestFreeLimitUsed` for
    interest free limit used.

---

## 2020-12-04

- Update endpoint for BLVT:
  - `GET /sapi/v1/blvt/tokenInfo` new fields in response `currentBaskets`(include `symbol`, `amount`
    , `notionalValue` ),`purchaseFeePct`,`dailyPurchaseLimit`,`redeemFeePct`,`dailyRedeemLimit`.
- New endpoint for BLVT:
  - `GET /sapi/v1/blvt/userLimit` to get BLVT user limit info.

---

## 2020-12-02

- New endpoints for Sub-Account:
  - `GET /sapi/v2/sub-account/futures/account` to get detail on sub-account's USDT margined futures
    account and COIN margined futures account.
  - `GET /sapi/v2/sub-account/futures/accountSummary` to get summary of sub-account's USDT margined
    futures account and COIN margined futures account.
  - `GET /sapi/v2/sub-account/futures/positionRisk` to get position risk of sub-account's USDT
    margined futures account and COIN margined futures account.

---

## 2020-12-01

- Update Margin Trade Endpoint:
  - `POST /sapi/v1/margin/order` new parameter `quoteOrderQty` allow a user to specify the total
    `quoteOrderQty` spent or received in the `MARKET` order.

---

## 2020-11-27

New API clusters have been added in order to improve performance.

Users can access any of the following API clusters, in addition to `api.binance.com`

If there are any performance issues with accessing `api.binance.com` please try any of the following
instead:

- https://api1.binance.com/api/v3/*
- https://api2.binance.com/api/v3/*
- https://api3.binance.com/api/v3/*

---

## 2020-11-16

- Updated endpoints for Margin, new parameter `archived` to query data from 6 months ago:
  - `GET /sapi/v1/margin/loan`
  - `GET /sapi/v1/margin/repay`
  - `GET /sapi/v1/margin/interestHistory`

---

## 2020-11-13

- New endpoints for Sub-Account:
  - `POST /sapi/v1/sub-account/universalTransfer` to transfer spot and futures asset between master
    account and sub accounts.
  - `GET /sapi/v1/sub-account/universalTransfer` to search transfer records.

---

## 2020-11-10

- New endpoint to toggle BNB Burn:
  - `POST /sapi/v1/bnbBurn` to toggle BNB Burn on spot trade and margin interest.
  - `GET /sapi/v1/bnbBurn` to get BNB Burn status.

---

## 2020-11-09

- New field `tranId` is available from endpoints:
  - `GET /sapi/v1/sub-account/futures/internalTransfer`
  - `GET /sapi/v1/sub-account/transfer/subUserHistory`

---

## 2020-11-03

- Update endpoints for Futures Cross-Collateral:
  - `GET /sapi/v1/futures/loan/repay/history` new fields in response `repayType`(`NORMAL` for normal
    repayment, `COLLATERAL` for collateral repayment), `price` (collateral repayment rate),
    `repayCollateral`(collateral amount for collateral repayment).
  - `GET /sapi/v1/futures/loan/wallet` new fields in response `totalInterest` (total interest for
    cross-collateral), `principalForInterest`(cross-collateral principal for interest),
    `interest`(cross-collateral interest).
  - `GET /sapi/v1/futures/loan/configs` new fields in response `interestRate` (interest rate for
    cross-collateral), `interestGracePeriod` (interest grace period for cross-collateral).

- New endpoints for Futures Cross-Collateral:
  - `GET /sapi/v1/futures/loan/collateralRepayLimit` to check the maximum and minimum limit when
    repay with collateral.
  - `GET /sapi/v1/futures/loan/collateralRepay` to get quote for collateral repayment.
  - `POST /sapi/v1/futures/loan/collateralRepay` to repay with collateral.
  - `GET /sapi/v1/futures/loan/collateralRepayResult` to check collateral repayment result.
  - `GET /sapi/v1/futures/loan/interestHistory` to get cross-collateral interest history.

---

## 2020-10-14

- Update endpoints for Futures Cross-Collateral:
  - `POST /sapi/v1/futures/loan/borrow` and `GET /sapi/v1/futures/loan/borrow/history` new field
    `borrowId` in response for ID of Cross-Collateral borrow operation.
  - `POST /sapi/v1/futures/loan/repay` and `GET /sapi/v1/futures/loan/repay/history` new field
    `repayId` in response for ID of Cross-Collateral repay operation.

---

## 2020-10-10

- New `type` added in the endpoint `POST /sapi/v1/sub-account/futures/transfer`to support transfer
  asset from subaccount's spot account to its COIN-margined futures account and transfer asset from
  subaccount's COIN-margined futures account to its spot account.

---

## 2020-09-30

- Update endpoints for Margin Account:
  - `GET /sapi/v1/margin/maxBorrowable` new field `borrowLimit` in response for account borrow
    limit.

---

## 2020-09-28

- New endpoints for Binance Savings:
  - `POST /sapi/v1/lending/positionChanged` to change fixed/activity position to daily position.
- New parameter `ACTIVITY` replace `REGULAR`in the following Binance Savings endpoints:
  - `GET /sapi/v1/lending/project/list`
  - `POST /sapi/v1/lending/customizedFixed/purchase`
  - `GET /sapi/v1/lending/project/position/list`
  - `GET /sapi/v1/lending/union/purchaseRecord`
  - `GET /sapi/v1/lending/union/interestHistory`

---

## 2020-09-23

- New SAPI endpoints for BSwap:
  - `GET /sapi/v1/bswap/pools` to list all swap pools.
  - `GET /sapi/v1/bswap/liquidity` to get liquidity information of a pool.
  - `POST /sapi/v1/bswap/liquidityAdd` to add liquidity.
  - `POST /sapi/v1/bswap/liquidityRemove` to remove liquidity.
  - `GET /sapi/v1/bswap/liquidityOps` to get liquidity operation record.
  - `GET /sapi/v1/bswap/quote` to request quotes.
  - `POST /sapi/v1/bswap/swap` to swap.
  - `GET /sapi/v1/bswap/swap` to get swap history.

---

## 2020-09-16

- New SAPI endpoints for BLVT:
  - `GET /sapi/v1/blvt/tokenInfo` to get BLVT info.
  - `POST /sapi/v1/blvt/subscribe (HMAC SHA256)` to subscribe BLVT.
  - `GET /sapi/v1/blvt/subscribe/record  (HMAC SHA256)` to get subscription record。
  - `POST /sapi/v1/blvt/redeem (HMAC SHA256)` to redeem BLVT.
  - `GET /sapi/v1/blvt/redeem/record  (HMAC SHA256` to get redemption record.

- The BLVT NAV system is working relatively with Binance Futures, so some endpoints are based on
  futures system:
  - New endpoint to get historical BLVT Kline.
  - New WebSocket streams for BLVT Info and BLVT NAV Kline:

## 2020-09-09

USER DATA STREAM

- `outboundAccountInfo` has been deprecated.
- `outboundAccountInfo` will be removed in the future. (Exact date unknown) **Please use
  `outboundAccountPosition` instead.**
- `outboundAccountInfo` will now only show the balance of non-zero assets and assets that have been
  reduced to 0.

---

## 2020-09-03

- New endpoint `POST /sapi/v1/sub-account/futures/internalTransfer` to transfer futures asset
  between master account and subaccount.
- New endpoint`GET /sapi/v1/sub-account/futures/internalTransfer` to get futures transfer history of
  subaccount.

---

## 2020-09-01

- New parameter `masterAccountTotalAsset` added in the endpoint
  `GET /sapi/v1/sub-account/spotSummary` to get BTC valued asset summary of master account.

---

## 2020-08-27

- New endpoint `GET /sapi/v1/sub-account/spotSummary` to get BTC valued asset summary of subaccout.

---

## 2020-08-26

- New parameter `symbols` added in the endpoint `GET /sapi/v1/margin/isolated/account`.

---

## 2020-07-28

ISOLATED MARGIN

- New parameters "isIsolated" and "symbol" added for isolated margin in the following endpoints:
  - `POST /sapi/v1/margin/loan`
  - `POST /sapi/v1/margin/repay`
- New parameter "isIsolated" and new response field "isIsolated" added for isolated margin in the
  following endpoints:
  - `POST /sapi/v1/margin/order`
  - `DELETE /sapi/v1/margin/order`
  - `GET /sapi/v1/margin/order`
  - `GET /sapi/v1/margin/openOrders`
  - `GET /sapi/v1/margin/allOrders`
  - `GET /sapi/v1/margin/myTrades`

- New parameter "isolatedSymbol" and new response field "isolatedSymbol" added for isolated margin
  in the following endpoints:
  - `GET /sapi/v1/margin/loan`
  - `GET /sapi/v1/margin/repay`
  - `GET /sapi/v1/margin/interestHistory`

- New parameter "isolatedSymbol" and new response field "isIsolated" added for isolated margin in
  the following endpoint `GET /sapi/v1/margin/forceLiquidationRec`

- New parameter "isolatedSymbol" added for isolated margin in the following endpoints:
  - `GET /sapi/v1/margin/maxBorrowable`
  - `GET /sapi/v1/margin/maxTransferable`
- New endpoints for isolated margin:
  - `POST /sapi/v1/margin/isolated/create`
  - `POST /sapi/v1/margin/isolated/transfer`
  - `GET /sapi/v1/margin/isolated/transfer`
  - `GET /sapi/v1/margin/isolated/account`
  - `GET /sapi/v1/margin/isolated/pair`
  - `GET /sapi/v1/margin/isolated/allPairs`

- New endpoints for listenKey management of isolated margin account:
  - `POST /sapi/v1/userDataStream/isolated`
  - `PUT /sapi/v1/userDataStream/isolated`
  - `DELETE /sapi/v1/userDataStream/isolated`

---

## 2020-07-20

- The max value of parameter "limit" in `GET /sapi/v1/margin/allOrders` has been changed as 500.

---

## 2020-07-17

- There is now a request limit specifically for the sapi/v1/margin/allOrders endpoint at 60 raw
  requests per minute for a single IP address.

---

## 2020-07-13

- New SAPI Endpoints for futures Cross-Collateral:
  - `POST /sapi/v1/futures/loan/borrow`
  - `GET /sapi/v1/futures/loan/borrow/history`
  - `POST /sapi/v1/futures/loan/repay`
  - `GET /sapi/v1/futures/loan/repay/history`
  - `GET /sapi/v1/futures/loan/wallet`
  - `GET /sapi/v1/futures/loan/configs`
  - `GET /sapi/v1/futures/loan/calcAdjustLevel`
  - `GET /sapi/v1/futures/loan/calcMaxAdjustAmount`
  - `POST /sapi/v1/futures/loan/adjustCollateral`
  - `GET /sapi/v1/futures/loan/adjustCollateral/history`
  - `GET /sapi/v1/futures/loan/liquidationHistory`

---

## 2020-06-28

- SAPI Endpoints for futures:
  - `POST /sapi/v1/futures/transfer`
  - `GET /sapi/v1/futures/transfer`

---

## 2020-05-06

- New endpoints for Mining:
  - `GET /sapi/v1/mining/pub/algoList`
  - `GET /sapi/v1/mining/pub/coinList`
  - `GET /sapi/v1/mining/worker/detail`
  - `GET /sapi/v1/mining/worker/list`
  - `GET /sapi/v1/mining/payment/list`
  - `GET /sapi/v1/mining/statistics/user/status`
  - `GET /sapi/v1/mining/statistics/user/list`

---

## 2020-05-01

- From 2020-05-01 UTC 00:00, all symbols will have a limit of 200 open orders using the
  [MAX_NUM_ORDERS](https://binance-docs.github.io/apidocs/spot/en/#filters) filter.
  - No existing orders will be removed or canceled.
  - Accounts that have 200 or more open orders on a symbol will not be able to place new orders on
    that symbol until the open order count is below 200.
  - OCO orders count as 2 open orders before the `LIMIT` order is touched or the `STOP_LOSS` (or
    `STOP_LOSS_LIMIT`) order is triggered; once this happens the other order is canceled and will no
    longer count as an open order.

---

## 2020-04-25

<font size=4>SPOT API</font>

- New field `permissions`
  - Defines the trading permissions that are allowed on accounts and symbols.
  - `permissions` is an enum array; values:
    - `SPOT`
    - `MARGIN`
  - `permissions` will replace `isSpotTradingAllowed` and `isMarginTradingAllowed` on
    `GET api/v3/exchangeInfo` in future API versions (v4+).
  - For an account to trade on a symbol, the account and symbol must share at least 1 permission in
    common.
- Updates to GET `api/v3/exchangeInfo`
  - New field `permissions` added.
  - New field `quoteAssetPrecision` added; a duplicate of the `quotePrecision` field.
    `quotePrecision` will be removed in future API versions (v4+).
- Updates to GET `api/v3/account`
  - New field `permissions` added.
- New endpoint DELETE `api/v3/openOrders`
  - This will allow a user to cancel all open orders on a single symbol.
  - This endpoint will cancel all open orders including OCO orders.
- Orders can be canceled via the API on symbols in the `BREAK` or `HALT` status.

<font size=4> USER DATA STREAM </font>

- `OutboundAccountInfo` has new field `P` which shows the trading permissions of the account.

---

## 2020-04-23

WEB SOCKET STREAM

- WebSocket connections have a limit of 5 incoming messages per second. A message is considered:
  - A PING frame
  - A PONG frame
  - A JSON control message (e.g. subscribe, unsubscribe)
- A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected
  may be banned.
- A single connection can listen to a maximum of 1024 streams.

## 2020-04-16

- New fields in response to endpoint`GET /sapi/v1/lending/daily/token/position`：
  - `todayPurchasedAmount` for user's purchased amount today

- New lending endpoints for customized fixed projects:
  - `GET /sapi/v1/lending/project/list`
  - `POST /sapi/v1/lending/customizedFixed/purchase`
  - `GET /sapi/v1/lending/project/position/list`

---

## 2020-04-02

- New fields in response to endpoint`GET /sapi/v1/capital/config/getall`：
  - `minConfirm` for min number for balance confirmation
  - `unLockConfirm` for confirmation number for balance unlock

---

## 2020-03-24

- `MAX_POSITION` filter added.
  - This filter defines the allowed maximum position an account can have on the base asset of a
    symbol. An account's position defined as the sum of the account's:
    - free balance of the base asset
    - locked balance of the base asset
    - sum of the qty of all open BUY orders

  - `BUY` orders will be rejected if the account's position is greater than the maximum position
    allowed.

---

## 2020-03-13

- New parameter `transactionFeeFlag` is available in endpoint:
  - `POST /sapi/v1/capital/withdraw/apply` and
  - `POST /wapi/v3/withdraw.html`

---

## 2020-02-05

- New sub account endpoints:
  - `POST /sapi/v1/sub-account/futures/transfer` to transfer between futures and spot accout of
    sub-account.
  - `POST /sapi/v1/sub-account/margin/transfer` to transfer between margin and spot accout of
    sub-account.
  - `POST /sapi/v1/sub-account/transfer/subToSub` to transfer to another account by sub-account.
  - `POST /sapi/v1/sub-account/transfer/subToMaster` to transfer to same master by sub-account.
  - `GET /sapi/v1/sub-account/transfer/subUserHistory` to get transfer history of sub-account.

---

## 2020-01-15

- New parameter `withdrawOrderId` for client customized withdraw id for endpoint
  `POST /wapi/v3/withdraw.html`.

- New field `withdrawOrderId` in response to `GET /wapi/v3/withdrawHistory.html`

---

## 2019-12-25

- New endpoints for Binance Savings:
  - `GET /sapi/v1/lending/daily/product/list`
  - `GET /sapi/v1/lending/daily/userLeftQuota`
  - `POST /sapi/v1/lending/daily/purchase `
  - `GET /sapi/v1/lending/daily/userRedemptionQuota`
  - `POST /sapi/v1/lending/daily/redeem`
  - `GET /sapi/v1/lending/daily/token/position`
  - `GET /sapi/v1/lending/union/account`
  - `GET /sapi/v1/lending/union/purchaseRecord`
  - `GET /sapi/v1/lending/union/redemptionRecord`
  - `GET /sapi/v1/lending/union/interestHistory`

- Added time interval limit in  
  `GET  /sapi/v1/capital/withdraw/history`,  
  `GET /wapi/v3/withdrawHistory.html`,  
  `GET /sapi/v1/capital/deposit/hisrec` and  
  `GET /wapi/v3/depositHistory.html`: _ The default `startTime` is 90 days from current time, and
  the default `endTime` is current time. _ Please notice the default `startTime` and `endTime` to
  make sure that time interval is within 0-90 days. \* If both `startTime` and `endTime` are sent,
  time between `startTime` and `endTime` must be less than 90 days.

---

## 2019-12-18

- New endpoint to get daily snapshot of account:  
  `GET /sapi/v1/accountSnapshot`

---

## 2019-11-30

- Added parameter `sideEffectType` in `POST  /sapi/v1/margin/order (HMAC SHA256)` with enums:
  - `NO_SIDE_EFFECT` for normal trade order;
  - `MARGIN_BUY` for margin trade order;
  - `AUTO_REPAY` for making auto repayment after order filled.

- New field `marginBuyBorrowAmount` and `marginBuyBorrowAsset` in `FULL` response to
  `POST  /sapi/v1/margin/order (HMAC SHA256)`

---

## 2019-11-28

- New SAPI endpoint to disable fast withdraw switch:  
  `POST /sapi/v1/account/disableFastWithdrawSwitch (HMAC SHA256)`
- New SAPI endpoint to enable fast withdraw switch:  
  `POST /sapi/v1/account/enableFastWithdrawSwitch (HMAC SHA256)`

---

## 2019-11-22

- Quote Order Qty Market orders have been enabled on all symbols.
  - Quote Order Qty `MARKET` orders allow a user to specify the total `quoteOrderQty` spent or
    received in the `MARKET` order.
  - Quote Order Qty `MARKET` orders will not break `LOT_SIZE` filter rules; the order will execute a
    quantity that will have the notional value as close as possible to `quoteOrderQty`.
  - Using `BNBBTC` as an example:
    - On the `BUY` side, the order will buy as many BNB as `quoteOrderQty` BTC can.
    - On the `SELL` side, the order will sell as much BNB as needed to receive `quoteOrderQty` BTC.

---

## 2019-11-19

- `GET /sapi/v1/sub-account/margin/account` has new field: `marginTradeCoeffVo` which contains
  - `forceLiquidationBar` for liquidation margin ratio
  - `marginCallBar` for margin call margin ratio
  - `normalBar` for initial margin ratio

---

## 2019-11-13

<font size=4>Rest API </font>

- api/v3/exchangeInfo has new fields:
  - `quoteOrderQtyMarketAllowed`
  - `baseCommissionPrecision`
  - `quoteCommissionPrecision`
- `MARKET` orders have a new optional field: `quoteOrderQty` used to specify the quote quantity to
  BUY or SELL. This cannot be used in combination with `quantity`.
  - The exact timing that `quoteOrderQty` MARKET orders will be enabled is TBD. There will be a
    separate announcement and further details at that time.
- All order query endpoints will return a new field `origQuoteOrderQty` in the JSON payload. (e.g.
  GET api/v3/allOrders)

```json
{
  "code": -1128,
  "msg": "Combination of optional parameters invalid. Recommendation: 'stopLimitTimeInForce' should also be sent."
}
```

- Updated error messages for -1128
  - Sending an `OCO` with a `stopLimitPrice` but without a `stopLimitTimeInForce` will return the
    error:

- Updated error messages for -1003 to specify the limit is referring to the request weight, not to
  the number of requests.

**Deprecation of v1 endpoints**:

By end of Q1 2020, the following endpoints will be removed from the API. The documentation has been
updated to use the v3 versions of these endpoints.

- GET api/v1/depth
- GET api/v1/historicalTrades
- GET api/v1/aggTrades
- GET api/v1/klines
- GET api/v1/ticker/24hr
- GET api/v1/ticker/price
- GET api/v1/exchangeInfo
- POST api/v1/userDataStream
- PUT api/v1/userDataStream
- GET api/v1/ping
- GET api/v1/time
- GET api/v1/ticker/bookTicker

**These endpoints however, will NOT be migrated to v3. Please use the following endpoints instead
moving forward.**

<table>
<tr>
<th>Old V1 Endpoints</th>
<th>New V3 Endpoints</th>
</tr>
<tr>
<td>GET api/v1/ticker/allPrices</td>
<td>GET api/v3/ticker/price</td>
</tr>
<tr>
<td>GET api/v1/ticker/allBookTickers</td>
<td>GET api/v3/ticker/bookTicker</td>
</tr>
</table>

<font size=4>USER DATA STREAM </font>

- Changes to`executionReport` event
  - If the C field is empty, it will now properly return `null`, instead of `"null"`.
  - New field Q which represents the `quoteOrderQty`.

- `balanceUpdate` event type added
  - This event occurs when funds are deposited or withdrawn from your account.

<font size=4> WEB SOCKET STREAM</font>

- WSS now supports live subscribing/unsubscribing to streams.

---

## 2019-11-08

- New sapi for subaccount management on margin and futures:
  - `GET /sapi/v1/sub-account/status (HMAC SHA256)`
  - `POST /sapi/v1/sub-account/margin/enable (HMAC SHA256)`
  - `GET /sapi/v1/sub-account/margin/account (HMAC SHA256)`
  - `GET /sapi/v1/sub-account/margin/accountSummary (HMAC SHA256)`
  - `POST /sapi/v1/sub-account/futures/enable (HMAC SHA256)`
  - `GET /sapi/v1/sub-account/futures/account (HMAC SHA256)`
  - `GET /sapi/v1/sub-account/futures/accountSummary (HMAC SHA256)`
  - `GET /sapi/v1/sub-account/futures/positionRisk (HMAC SHA256)`

---

## 2019-11-04

- New sapi endpoints for subaccount wallet.
  - `GET /sapi/v1/capital/deposit/subAddress (HMAC SHA256))`: fetch subaccount deposit address.
  - `GET /sapi/v1/capital/deposit/subHisrec (HMAC SHA256))`: fetch subaccount deposit history.

---

## 2019-10-29

- New sapi endpoints for wallet.
  - `POST /sapi/v1/capital/withdraw/apply (HMAC SHA256)`: withdraw.
  - `Get /sapi/v1/capital/withdraw/history (HMAC SHA256)`: fetch withdraw history with network.

---

## 2019-10-14

- New sapi endpoints for wallet.
  - `GET /sapi/v1/capital/config/getall (HMAC SHA256)`: get all coins' information for user.
  - `GET /sapi/v1/capital/deposit/hisrec (HMAC SHA256)`: fetch deposit history with network.
  - `GET /sapi/v1/capital/deposit/address (HMAC SHA256)`: fetch deposit address with network.

---

## 2019-10-11

- Added parameter `network` in `POST /wapi/v3/withdraw.html` so that asset can be withdrawed with
  specific network.

---

## 2019-09-09

- New WebSocket streams for bookTickers added: `<symbol>@bookTicker` and `!bookTicker`.

---

## 2019-09-03

- Faster order book data with 100ms updates: `<symbol>@depth@100ms` and `<symbol>@depth#@100ms`
- Added "Update Speed:" to `Websocket Market Streams`
- Removed deprecated v1 endpoints as per previous announcement:
  - GET api/v1/order
  - GET api/v1/openOrders
  - POST api/v1/order
  - DELETE api/v1/order
  - GET api/v1/allOrders
  - GET api/v1/account
  - GET api/v1/myTrades

---

## 2019-08-16

- GET api/v1/depth `limit` of 10000 has been temporarily removed

- In Q4 2017, the following endpoints were deprecated and removed from the API documentation. They
  have been permanently removed from the API as of this version. We apologize for the omission from
  the original changelog:
  - GET api/v1/order
  - GET api/v1/openOrders
  - POST api/v1/order
  - DELETE api/v1/order
  - GET api/v1/allOrders
  - GET api/v1/account
  - GET api/v1/myTrades

- Streams, endpoints, parameters, payloads, etc. described in the documents in this repository are
  **considered official** and **supported**. The use of any other streams, endpoints, parameters, or
  payloads, etc. is **not supported; use them at your own risk and with no guarantees.**

---

## 2019-09-15

<font size=4>Rest API</font>

- New order type: OCO ("One Cancels the Other")
  - An OCO has 2 orders: (also known as legs in financial terms)
    - `STOP_LOSS` or `STOP_LOSS_LIMIT` leg
    - `LIMIT_MAKER` leg

  - Price Restrictions:
    - `SELL Orders` : Limit Price > Last Price > Stop Price
    - `BUY Orders` : Limit Price < Last Price < Stop Price
    - As stated, the prices must "straddle" the last traded price on the symbol. EX: If the last
      price is 10:
      - A SELL OCO must have the limit price greater than 10, and the stop price less than 10.
      - A BUY OCO must have a limit price less than 10, and the stop price greater than 10.

  - Quantity Restrictions:
    - Both legs must have the **same quantity**.
    - `ICEBERG` quantities however, do not have to be the same.

  - Execution Order:
    - If the `LIMIT_MAKER` is touched, the limit maker leg will be executed first BEFORE canceling
      the Stop Loss Leg.
    - if the Market Price moves such that the `STOP_LOSS` or `STOP_LOSS_LIMIT` will trigger, the
      Limit Maker leg will be cancelled BEFORE executing the `STOP_LOSS` Leg.

  - Cancelling an OCO
    - Cancelling either order leg will cancel the entire OCO.
    - The entire OCO can be canceled via the `orderListId` or the `listClientOrderId`.

  - New Enums for OCO:
    1. `ListStatusType`
       - `RESPONSE` - used when ListStatus is responding to a failed action. (either order list
         placement or cancellation)
       - `EXEC_STARTED` - used when an order list has been placed or there is an update to a list's
         status.
       - `ALL_DONE` - used when an order list has finished executing and is no longer active.
    2. `ListOrderStatus`
       - `EXECUTING` - used when an order list has been placed or there is an update to a list's
         status.
       - `ALL_DONE` - used when an order list has finished executing and is no longer active.
       - `REJECT` - used when ListStatus is responding to a failed action. (either order list
         placement or cancellation)
    3. `ContingencyType`
       - `OCO` - specifies the type of order list.

  - New Endpoints:
    - POST api/v3/order/oco
    - DELETE api/v3/orderList
    - GET api/v3/orderList

- `recvWindow` cannot exceed 60000.
- New `intervalLetter` values for headers:
  - SECOND => S
  - MINUTE => M
  - HOUR => H
  - DAY => D
- New Headers `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)` will give your current used request
  weight for the (intervalNum)(intervalLetter) rate limiter. For example, if there is a one minute
  request rate weight limiter set, you will get a `X-MBX-USED-WEIGHT-1M` header in the response. The
  legacy header `X-MBX-USED-WEIGHT` will still be returned and will represent the current used
  weight for the one minute request rate weight limit.
- New Header `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)`that is updated on any valid order
  placement and tracks your current order count for the interval; rejected/unsuccessful orders are
  not guaranteed to have `X-MBX-ORDER-COUNT-**` headers in the response.
  - Eg. `X-MBX-ORDER-COUNT-1S` for "orders per 1 second" and `X-MBX-ORDER-COUNT-1D` for orders per
    "one day"
- GET api/v1/depth now supports `limit` 5000 and 10000; weights are 50 and 100 respectively.
- GET api/v1/exchangeInfo has a new parameter `ocoAllowed`.

<font size=4>USER DATA STREAM</font>

- `executionReport` event now contains "g" which has the `orderListId`; it will be set to -1 for
  non-OCO orders.
- New Event Type `listStatus`; `listStatus` is sent on an update to any OCO order.
- New Event Type `outboundAccountPosition`; `outboundAccountPosition` is sent any time an account's
  balance changes and contains the assets that could have changed by the event that generated the
  balance change (a deposit, withdrawal, trade, order placement, or cancelation).

<font size=4>NEW ERRORS</font>

- **-1131 BAD_RECV_WINDOW**
  - `recvWindow` must be less than 60000
- **-1099 Not found, authenticated, or authorized**
  - This replaces error code -1999

<font size=4>NEW -2011 ERRORS</font>

- **OCO_BAD_ORDER_PARAMS**
  - A parameter for one of the orders is incorrect.
- **OCO_BAD_PRICES**
  - The relationship of the prices for the orders is not correct.
- **UNSUPPORTED_ORD_OCO**
  - OCO orders are not supported for this symbol.

---

## 2019-03-12

<font size=4>Rest API</font>

- X-MBX-USED-WEIGHT header added to Rest API responses.
- Retry-After header added to Rest API 418 and 429 responses.
- When canceling the Rest API can now return `errorCode` -1013 OR -2011 if the symbol's `status`
  isn't `TRADING`.
- `api/v1/depth` no longer has the ignored and empty `[]`.
- `api/v3/myTrades` now returns `quoteQty`; the price \* qty of for the trade.

<font size=4>Websocket streams</font>

- `<symbol>@depth` and `<symbol>@depthX` streams no longer have the ignored and empty `[]`.

<font size=4>System improvements</font>

- Matching Engine stability/reliability improvements.
- Rest API performance improvements.

---

## 2018-11-13

<font size=4>Rest API</font>

- Can now cancel orders through the Rest API during a trading ban.
- New filters: `PERCENT_PRICE`, `MARKET_LOT_SIZE`, `MAX_NUM_ICEBERG_ORDERS`.
- Added `RAW_REQUESTS` rate limit. Limits based on the number of requests over X minutes regardless
  of weight.
- /api/v3/ticker/price increased to weight of 2 for a no symbol query.
- /api/v3/ticker/bookTicker increased weight of 2 for a no symbol query.
- DELETE /api/v3/order will now return an execution report of the final state of the order.
- `MIN_NOTIONAL` filter has two new parameters: `applyToMarket` (whether or not the filter is
  applied to MARKET orders) and `avgPriceMins` (the number of minutes over which the price averaged
  for the notional estimation).
- `intervalNum` added to /api/v1/exchangeInfo limits. `intervalNum` describes the amount of the
  interval. For example: `intervalNum` 5, with `interval` minute, means "every 5 minutes".

<font size=4>Explanation for the average price calculation:</font>

1. (qty \* price) of all trades / sum of qty of all trades over previous 5 minutes.

2. If there is no trade in the last 5 minutes, it takes the first trade that happened outside of the
   5min window. For example if the last trade was 20 minutes ago, that trade's price is the 5 min
   average.

3. If there is no trade on the symbol, there is no average price and market orders cannot be placed.
   On a new symbol with `applyToMarket` enabled on the `MIN_NOTIONAL` filter, market orders cannot
   be placed until there is at least 1 trade.

4. The current average price can be checked here:
   `https://api.binance.com/api/v3/avgPrice?symbol=<symbol>` For example:
   https://api.binance.com/api/v3/avgPrice?symbol=BNBUSDT

<font size=4>User data stream</font>

- `Last quote asset transacted quantity` (as variable `Y`) added to execution reports. Represents
  the `lastPrice` \* `lastQty` (`L` \* `l`).

---

## 2018-07-18

<font size=4>Rest API</font>

- New filter: `ICEBERG_PARTS`
- `POST api/v3/order` new defaults for `newOrderRespType`. `ACK`, `RESULT`, or `FULL`; `MARKET` and
  `LIMIT` order types default to `FULL`, all other orders default to `ACK`.
- POST api/v3/order `RESULT` and `FULL` responses now have `cummulativeQuoteQty`
- GET api/v3/openOrders with no symbol weight reduced to 40.
- GET api/v3/ticker/24hr with no symbol weight reduced to 40.
- Max amount of trades from GET /api/v1/trades increased to 1000.
- Max amount of trades from GET /api/v1/historicalTrades increased to 1000.
- Max amount of aggregate trades from GET /api/v1/aggTrades increased to 1000.
- Max amount of aggregate trades from GET /api/v1/klines increased to 1000.
- Rest API Order lookups now return `updateTime` which represents the last time the order was
  updated; `time` is the order creation time.
- Order lookup endpoints will now return `cummulativeQuoteQty`. If `cummulativeQuoteQty` is < 0, it
  means the data isn't available for this order at this time.
- `REQUESTS` rate limit type changed to `REQUEST_WEIGHT`. This limit was always logically request
  weight and the previous name for it caused confusion.

<font size=4>User data stream</font>

- `cummulativeQuoteQty` field added to order responses and execution reports (as variable `Z`).
  Represents the cummulative amount of the `quote` that has been spent (with a `BUY` order) or
  received (with a `SELL` order). Historical orders will have a value < 0 in this field indicating
  the data is not available at this time. `cummulativeQuoteQty` divided by `cummulativeQty` will
  give the average price for an order.
- `O` (order creation time) added to execution reports

---

## 2018-01-23

- GET /api/v1/historicalTrades weight decreased to 5
- GET /api/v1/aggTrades weight decreased to 1
- GET /api/v1/klines weight decreased to 1
- GET /api/v1/ticker/24hr all symbols weight decreased to number of trading symbols / 2
- GET /api/v3/allOrders weight decreased to 5
- GET /api/v3/myTrades weight decreased to 5
- GET /api/v3/account weight decreased to 5
- GET /api/v1/depth limit=500 weight decreased to 5
- GET /api/v1/depth limit=1000 weight decreased to 10
- -1003 error message updated to direct users to websockets

---

## 2018-01-20

- GET /api/v1/ticker/24hr single symbol weight decreased to 1
- GET /api/v3/openOrders all symbols weight decreased to number of trading symbols / 2
- GET /api/v3/allOrders weight decreased to 15
- GET /api/v3/myTrades weight decreased to 15
- GET /api/v3/order weight decreased to 1
- myTrades will now return both sides of a self-trade/wash-trade

---

## 2018-01-14

- GET /api/v1/aggTrades weight changed to 2
- GET /api/v1/klines weight changed to 2
- GET /api/v3/order weight changed to 2
- GET /api/v3/allOrders weight changed to 20
- GET /api/v3/account weight changed to 20
- GET /api/v3/myTrades weight changed to 20
- GET /api/v3/historicalTrades weight changed to 20