---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/binance-link/change-log
api_type: Changelog
updated_at: 2026-11-22 18:33:26.889517
---

# Change Log

## 2026-09-10

- Documentation and navigation only. The service itself is unchanged — no endpoint, request or
  response behaviour changes.
  - "Exchange Link" is now presented as **Crypto-As-A-Service (CAAS)**.
  - "Link and Trade" is now presented as **OMS Toolkit**.
  - The standalone "Crypto-as-a-Service (CAAS)" section is now **CAAS > Integration Basics >
    Markup**.
  - "KYC SaaS" is now nested under **CAAS**.
  - Added **Institutional Crypto Buy/Sell Solution** under **Crypto-As-A-Service (CAAS)** as an
    optional CAAS module.
- **Page URLs have changed.** Existing links redirect to their new location, so saved links and
  bookmarks keep working.
  - Documentation pages:
    - `/products/exchange-link/*` is now `/products/caas/*`
    - `/products/link-and-trade/*` is now `/products/oms/*`
    - `/products/vip-caas/*` is now `/products/caas/markup/*`
  - API Reference pages:
    - `/catalog/vip-and-institutional-exchange-link/*` is now
      `/catalog/vip-and-institutional-caas/*`
    - `/catalog/vip-and-institutional-link-and-trade/*` is now
      `/catalog/vip-and-institutional-oms/*`
- **Markup API Reference** — corrected to match what the service returns.
  - The success envelope was documented as `code` `"000000"` with a `message` field. The service
    returns `status`, `type`, `code` `"000000000"` and `data`, and no `message`.
  - Removed a `status` field documented on the markup trade aggregations response that the service
    does not return.
  - Documented the existing limit of 10 entries on `subUserIds` for Assign Members and Unassign
    Members.
- **OMS Toolkit** — COIN-M Futures reporting is served by the existing `/fapi/v1/apiReferral/*`
  endpoints with `type=2`. There is no separate `dapi.binance.com` base URL for reporting.
- **Institutional Crypto Buy/Sell Solution** — API request signing now specifies **2048-bit RSA**
  keys. The guide and its key-generation examples previously showed 1024-bit.

---

## 2026-05-08

- Update KYC SaaS endpoints to support KZ Entity Broker Partial Sharing mode.
  - POST `/bapi/ekyc/v2/public/ekyc/customer/share-kyc-data`
    - `basicInfo` / `identityInfo` changed from `YES` to `Conditional` (required for standard
      brokers; optional for KZ Entity brokers).
    - New optional `KycInfo` fields: `tncInfo`, `questionnaireInfo`.
    - New sub-sections: `TncInfo`, `QuestionnaireInfo`, `QuestionnaireAnswer`.
  - POST `/bapi/ekyc/v2/public/ekyc/customer/query-kyc-info`
    - New `KycInfoVo` response fields: `questionInfo`, `tncInfo`.
    - New sub-sections: `QuestionInfo`, `TncInfo` (response shape).

---

## 2026-04-20

- **Markup** — Initial release of the Commission Markup APIs under `/sapi/v1/vip/caas/commission/*`:
  create, query, update and delete fee groups; assign, unassign and query fee group members; and
  markup trade commission aggregation and detail reportings.

---

## 2026-03-27

- **Institutional Buy/Sell** — New endpoint `Get Symbol Detail` for cryptocurrency details (market
  cap, volume, rank, circulating supply).
- **Institutional Buy/Sell** — New endpoint `Get Kline Data` for candlestick data, supporting 3m, 1h
  and 1d intervals.
- **Institutional Buy/Sell** — New endpoint `Get Discover Price` for quotation prices and 24-hour
  changes.

---

## 2025-11-25

- New response fields for GET `/sapi/v1/apiReferral/rebate/recentRecord`
  - `distributeTime`
  - `commissionAsset`
  - `commission`
  - `convertPrice`

---

## 2025-11-07

- **Institutional Buy/Sell** — New merchant-side API requirements added.
- **Institutional Buy/Sell** — Updated typical buy/sell sequence diagrams and flow descriptions;
  added curl examples for all endpoints.

---

## 2025-11-03

- **Institutional Buy/Sell** — `Get Fiat Crypto Amount Limit` returns new fields for more accurate
  limits.

---

## 2025-10-20

- **Institutional Buy/Sell** — New field `webhookEventType` in the order-status webhook payload.

---

## 2025-10-15

- **Institutional Buy/Sell** — Request signing now supports 1024-bit RSA keys.

---

## 2025-09-30

- **Institutional Buy/Sell** — New endpoint `Get Fiat Crypto Amount Limit`; the fiat and crypto
  amount limit fields are removed from `Get Trading Pair` in favour of it.
- **Institutional Buy/Sell** — Updated typical buy/sell sequence diagrams and flow descriptions.

---

## 2025-09-22

- **Institutional Buy/Sell** — `Get Quote` request field `spreadLevel` replaced with `customSpread`.
- **Institutional Buy/Sell** — Added typical buy/sell sequence diagrams and flow descriptions.
- New Futures Transfer for Link Sub-account endpoints

* POST `/sapi/v1/broker/futures/accountTransfer`

---

## 2025-09-16

- Futures commission rebate query endpoints require to input `symbol` or `pair`.

* GET `/sapi/v1/broker/subAccountApi/commission/futures`
* GET `/sapi/v1/broker/subAccountApi/commission/coinFutures`

---

## 2025-09-05

- **Institutional Buy/Sell** — Initial release of the Institutional Crypto Buy/Sell Solution under
  `/papi/v1/ramp/connect/prime/*`.

---

## 2025-07-02

- New endpoints for KYC SaaS Integration, KYC Querying, and Request for Information (RFI).

---

## 2025-04-18

- New Endpoint for delete sub account `DELETE /sapi/v1/broker/subAccount `.
- Create Link sub account API key endpoint and FAST api key creation endpoint support asymmetrical
  key type(Ed25519 and RSA). Please see
  https://www.binance.com/en/support/faq/detail/6b9a63f1e3384cf48a2eedb82767a69a

---

## 2025-03-07

- New Endpoint for query sub account deposit by depositId
  `GET /sapi/v2/broker/subAccount/depositHist `.

---

## 2025-02-26

- Update sub account deposit history Endpoint `GET /sapi/v1/broker/subAccount/depositHist `, adding
  "travelRuleStatus".

---

## 2024-10-30

- Update the `Weight(UID)` to 60 for Endpoint `GET /sapi/v3/broker/subAccount/futuresSummary `.

---

## 2024-08-15

- New parameter `filterResult ` will be available on August 16, 2024 for query futures commission
  rebate record:`GET /sapi/v1/broker/rebate/futures/recentRecord `. If `filterResult ` = TRUE,
  rebates not from its own sub accounts will be filtered out in response.

---

## 2024-06-28

- New Endpoint for query futures assets of
  sub-accounts:`GET /sapi/v3/broker/subAccount/futuresSummary `.
- Following endpoints will be deleted in a month:
  `GET /sapi/v1/broker/subAccount/futuresSummary `,`GET /sapi/v2/broker/subAccount/futuresSummary `.
  Please migrate the usage of legacy version(v1&v2) to the new (v3) version as soon as possible.

---

## 2024-06-06

- Endpoints adjustment: for internal transfers, the txid prefix has been replaced to “Off-chain
  transfer”on 28 May 2024. “internal transfer” flag is no longer available in the TXID field,
  including historical transactions, the following endpoints are impacted:
  `GET /sapi/v1/broker/subAccount/depositHist`.

---

## 2024-04-30

- Update the request limit for endpoint: `POST /sapi/v1/broker/subAccountApi`. You can only create 1
  api key for each sub account per second

- Update the request limit for endpoint: `DELETE /sapi/v1/broker/subAccountApi`. You can only delete
  1 api key for each sub account per second

---

## 2024-03-05

- Remove endpoint: `POST /sapi/v1/broker/subAccount/blvt`.

---

## 2023-12-15

- Update the default parameter values of endpoint: `GET /sapi/v1/broker/universalTransfer`.

---

## 2023-11-20

- Add `depositId` and `selfReturnStatus` in response of endpoint:
  `GET /sapi/v1/broker/subAccount/deposit`.

---

## 2023-10-04

- Remove endpoint: `POST /sapi/v1/broker/subAccountApi/permission/vanillaOptions`.

---

## 2023-08-31

- Remove endpoint: `POST /sapi/v1/broker/subAccount/margin`. To enable the margin account, simply
  transfer assets into Cross Margin wallet.

---

## 2023-06-08

- Update weight for endpoint: `POST /sapi/v1/broker/subAccountApi`. Weight(Master Account) changed
  to 3000

---

## 2023-01-13

- Remove 2 endpoints: `POST /sapi/v1/broker/subAccountApi/ipRestriction`,
  `POST /sapi/v1/broker/subAccountApi/ipRestriction/ipList`.

---

## 2022-12-16

- Remove "thirdPartyName" for `POST /sapi/v2/broker/subAccountApi/ipRestriction (HMAC SHA256)`,
  `POST /sapi/v1/broker/subAccountApi/ipRestriction`,
  `POST /sapi/v1/broker/subAccountApi/ipRestriction/ipList`,
  `DELETE /sapi/v1/broker/subAccountApi/ipRestriction/ipList`.

---

## 2022-11-28

- Add "the max length is 32 characters" in the description of clientTranId for endpoints
  `POST /sapi/v1/broker/universalTransfer`, `POST /sapi/v1/broker/transfer/futures`,
  `POST /sapi/v1/broker/transfer`.

---

## 2022-11-18

- Added new endpoint `POST /sapi/v2/sub-account/subAccountApi/ipRestriction` to support user update
  IP Restriction for Sub-Account API key.

---

## 2022-09-22

- Update `POST /sapi/v1/broker/subAccountApi/ipRestriction` to support user enable or disable Third
  party IP list name restriction for sub-account api key.
- Update `POST /sapi/v1/broker/subAccountApi/ipRestriction/ipList` to support user update Third
  party IP list name restriction for sub-account api key.
- Update `DELETE /sapi/v1/broker/subAccountApi/ipRestriction/ipList` to support user delete Third
  party IP list name restriction for sub-account api key.

---

## 2022-09-12

- Update `GET /sapi/v1/broker/subAccountApi/ipRestriction` to support user query third party IP list
  name.

---

## 2022-08-23

- Add 100-days query scope for `GET /sapi/v1/broker/universalTransfer` and
  `GET /sapi/v1/broker/transfer`.
- Add requests per UID are limited to 60 requests per minute for
  `GET /sapi/v1/broker/subAccount/spotSummary`.

---

## 2022-06-27

- Added a new rebate status field in API response for endpoints
  `GET /sapi/v1/broker/rebate/futures/recentRecord` and `GET /sapi/v1/broker/rebate/recentRecord`.

---

## 2021-04-29

- Added parameter `tag` and new field `email` in endpoint `POST /sapi/v1/broker/subAccount`.

---

## 2021-03-26

- Added new endpoint `POST /sapi/v1/broker/subAccountApi/permission/universalTransfer` to enable the
  api permission for a sub account to use `POST /sapi/v1/asset/transfer`endpoint.
- Added new endpoint `POST /sapi/v1/broker/subAccountApi/permission/vanillaOptions` to enable
  Vanilla Options permission for sub account api key.

---

## 2021-02-04

- Added parameter `fromId` and `toId` in endpoint `GET /sapi/v1/broker/transfer`. The parameter
  `subaccountId` will be removed on 02/10 16:00(UTC+8). Please adjust the program as soon as
  possible.

---

## 2021-02-04

- Added parameter showAllStatus in endpoint `GET /sapi/v1/broker/universalTransfer`.

---

## 2021-01-27

- Added new endpoint `GET /sapi/v2/broker/subAccount/futuresSummary` to support query subaccount
  Coin Margined Futures asset info.

---

## 2021-01-14

- Added parameter clientTranId in endpoint `POST /sapi/v1/broker/transfer/futures` and
  `GET /sapi/v1/broker/transfer/futures`.

---

## 2020-12-28

- Added parameters page and size in endpoint `GET /sapi/v1/broker/subAccountApi`.

---

## 2020-12-14

- The endpoint `GET /sapi/v1/broker/transfer/futures` can only get the latest history of past 30
  days.

---

## 2020-12-10

- Added new endpoint `POST /sapi/v1/broker/universalTransfer` to transfer spot and futures asset
  between master account and sub accounts.
- Added new endpoint `GET /sapi/v1/broker/universalTransfer` to get universal transfer history.

---

## 2020-11-27

- Added tranId in response of endpoint `GET /sapi/v1/broker/transfer/futures`.

---

## 2020-10-23

- Added parameter showAllStatus in endpoint `GET /sapi/v1/broker/transfer`.

---

## 2020-10-12

- Added parameter status in the response of endpoint `GET /sapi/v1/broker/transfer`.

---

## 2020-09-16

- Added new endpoint `POST /sapi/v1/broker/subAccountApi/commission/coinFutures` to change sub-
  account COIN-Ⓜ futures commission adjustment.
- Added new endpoint `GET /sapi/v1/broker/subAccountApi/commission/coinFutures` query sub- account
  COIN-Ⓜ futures commission adjustment.
- Added parameter confirmTimes in endpoint `GET /sapi/v1/broker/subAccount/depositHist`.

## 2020-09-11

- Added parameter email in endpoint `GET /sapi/v1/broker/subAccount`.

---

## 2020-09-07

- Added new endpoint `POST /sapi/v1/broker/subAccountApi/ipRestriction` to enable or disable IP
  restriction for sub-account api key.
- Added new endpoint `POST /sapi/v1/broker/subAccountApi/ipRestriction/ipList` to add IP restricion
  for sub-account api key.
- Added new endpoint `GET /sapi/v1/broker/subAccountApi/ipRestriction` to get IP restriction for
  sub-account api key.
- Added new endpoint `DELETE /sapi/v1/broker/subAccountApi/ipRestriction/ipList` to delete IP
  restriction for sub-account api key.

---

## 2020-09-02

- Added new endpoint `GET /sapi/v1/broker/rebate/futures/recentRecord` to get futures commision
  rebate record.
- Added new endpoint `POST /sapi/v1/broker/transfer/futures` to transfer futures asset directly.
- Added new endpoint `GET /sapi/v1/broker/transfer/futures` to get futures transfer history.

---

## 2020-08-25

- Added parameters page and size in endpoint `GET /sapi/v1/broker/rebate/recentRecord`.

---

## 2020-07-29

- Added new endpoint `POST /sapi/v1/broker/subAccount/blvt` to enable leverage token for
  sub-account.

---

## 2020-07-21

- Added parameters page and size in endpoint `GET /sapi/v1/broker/subAccount`.

---

## 2020-07-10

- Added default limit 500 in endpoint `GET /sapi/v1/broker/transfer`.

---

## 2020-06-15

- Added new endpoint `GET /sapi/v1/broker/subAccount/spotSummary` to query sub accounts spot asset.
- Added new endpoint `GET /sapi/v1/broker/subAccount/marginSummary` to query sub accounts margin
  asset.
- Added new endpoint `GET /sapi/v1/broker/subAccount/futuresSummary` to query sub accounts futures
  asset.

---

## 2020-06-12

- Added new endpoint `GET /sapi/v1/broker/rebate/recentRecord` to query broker commission rebate
  recent record.

---

## 2020-06-11

- Added new endpoint `GET /sapi/v1/broker/subAccount/depositHist` to query sub accounts deposit
  history.

---

## 2020-04-22

- New fields in response to `GET /sapi/v1/broker/subAccountApi/commission/futures` and
  `POST /sapi/v1/broker/subAccountApi/commission/futures`:
  - `makerCommission` for current futures commission ratio for maker;
  - `takerCommission` for current futures commission ratio for taker;

---

## 2020-04-03

- Added new endpoint `POST /sapi/v1/broker/subAccount/bnbBurn/spot` to enable or disable BNB Burn
  for sub-account spot and margin.

- Added new endpoint `POST /sapi/v1/broker/subAccount/bnbBurn/marginInterest` to enable or disable
  BNB Burn for sub-account margin interest.

- Added new endpoint `GET /sapi/v1/broker/subAccount/bnbBurn/status` to get BNB Burn status for
  sub-account.

---

## 2020-03-27

- Added parameters `clientTranId `in endpoints:
  - `POST /sapi/v1/broker/transfer`,
  - `GET /sapi/v1/broker/transfer`.

---

## 2020-02-12

- The below endpoints will be released in the future:
  - new endpoint `GET /sapi/v1/broker/rebate/recentRecord` to query broker commission rebate recent
    record.
  - new endpoint `GET /sapi/v1/broker/rebate/historicalRecord ` to get broker commission rebate
    historical record.

---

## 2019-12-23

- Added new endpoint `POST /sapi/v1/broker/subAccountApi/commission/futures` to change sub-account
  futures commission adjustment.

- Added new endpoint `GET /sapi/v1/broker/subAccountApi/commission/futures` to query sub-account
  futures commission adjustment.

---

## 2019-11-11

- Added parameters `marginTrade ` and `futuresTrade` in endpoints:
  - `POST /sapi/v1/broker/subAccountApi`,
  - `POST /sapi/v1/broker/subAccountApi/permission`.
- Added keys `marginTrade ` and `futuresTrade` in responses to endpoints:
  - `POST /sapi/v1/broker/subAccountApi`,
  - `GET /sapi/v1/broker/subAccountApi`,
  - `POST /sapi/v1/broker/subAccountApi/permission`.
- Added parameters `marginMakerCommission ` and `marginTakerCommission ` in endpoint
  `POST /sapi/v1/broker/subAccountApi/commission`.

- Added keys `marginMakerCommission ` and `marginTakerCommission ` in responses to endpoints:
  - `POST /sapi/v1/broker/subAccountApi/commission`,
  - `Get /sapi/v1/broker/subAccount/`.
- Added new endpoint `POST /sapi/v1/broker/subAccount/margin` for setting subaccount enable on
  margin.

- Added new endpoint `POST /sapi/v1/broker/subAccount/futures` for setting subaccount enable on
  futures.

---

# Change Log

## 2026-09-10

- Documentation and navigation only. The service itself is unchanged — no endpoint, request or
  response behaviour changes.
  - "Exchange Link" is now presented as **Crypto-As-A-Service (CAAS)**.
  - "Link and Trade" is now presented as **OMS Toolkit**.
  - The standalone "Crypto-as-a-Service (CAAS)" section is now **CAAS > Integration Basics >
    Markup**.
  - "KYC SaaS" is now nested under **CAAS**.
  - Added **Institutional Crypto Buy/Sell Solution** under **Crypto-As-A-Service (CAAS)** as an
    optional CAAS module.
- **Page URLs have changed.** Existing links redirect to their new location, so saved links and
  bookmarks keep working.
  - Documentation pages:
    - `/products/exchange-link/*` is now `/products/caas/*`
    - `/products/link-and-trade/*` is now `/products/oms/*`
    - `/products/vip-caas/*` is now `/products/caas/markup/*`
  - API Reference pages:
    - `/catalog/vip-and-institutional-exchange-link/*` is now
      `/catalog/vip-and-institutional-caas/*`
    - `/catalog/vip-and-institutional-link-and-trade/*` is now
      `/catalog/vip-and-institutional-oms/*`
- **Markup API Reference** — corrected to match what the service returns.
  - The success envelope was documented as `code` `"000000"` with a `message` field. The service
    returns `status`, `type`, `code` `"000000000"` and `data`, and no `message`.
  - Removed a `status` field documented on the markup trade aggregations response that the service
    does not return.
  - Documented the existing limit of 10 entries on `subUserIds` for Assign Members and Unassign
    Members.
- **OMS Toolkit** — COIN-M Futures reporting is served by the existing `/fapi/v1/apiReferral/*`
  endpoints with `type=2`. There is no separate `dapi.binance.com` base URL for reporting.
- **Institutional Crypto Buy/Sell Solution** — API request signing now specifies **2048-bit RSA**
  keys. The guide and its key-generation examples previously showed 1024-bit.

---

## 2026-05-08

- Update KYC SaaS endpoints to support KZ Entity Broker Partial Sharing mode.
  - POST `/bapi/ekyc/v2/public/ekyc/customer/share-kyc-data`
    - `basicInfo` / `identityInfo` changed from `YES` to `Conditional` (required for standard
      brokers; optional for KZ Entity brokers).
    - New optional `KycInfo` fields: `tncInfo`, `questionnaireInfo`.
    - New sub-sections: `TncInfo`, `QuestionnaireInfo`, `QuestionnaireAnswer`.
  - POST `/bapi/ekyc/v2/public/ekyc/customer/query-kyc-info`
    - New `KycInfoVo` response fields: `questionInfo`, `tncInfo`.
    - New sub-sections: `QuestionInfo`, `TncInfo` (response shape).

---

## 2026-04-20

- **Markup** — Initial release of the Commission Markup APIs under `/sapi/v1/vip/caas/commission/*`:
  create, query, update and delete fee groups; assign, unassign and query fee group members; and
  markup trade commission aggregation and detail reportings.

---

## 2026-03-27

- **Institutional Buy/Sell** — New endpoint `Get Symbol Detail` for cryptocurrency details (market
  cap, volume, rank, circulating supply).
- **Institutional Buy/Sell** — New endpoint `Get Kline Data` for candlestick data, supporting 3m, 1h
  and 1d intervals.
- **Institutional Buy/Sell** — New endpoint `Get Discover Price` for quotation prices and 24-hour
  changes.

---

## 2025-11-25

- New response fields for GET `/sapi/v1/apiReferral/rebate/recentRecord`
  - `distributeTime`
  - `commissionAsset`
  - `commission`
  - `convertPrice`

---

## 2025-11-07

- **Institutional Buy/Sell** — New merchant-side API requirements added.
- **Institutional Buy/Sell** — Updated typical buy/sell sequence diagrams and flow descriptions;
  added curl examples for all endpoints.

---

## 2025-11-03

- **Institutional Buy/Sell** — `Get Fiat Crypto Amount Limit` returns new fields for more accurate
  limits.

---

## 2025-10-20

- **Institutional Buy/Sell** — New field `webhookEventType` in the order-status webhook payload.

---

## 2025-10-15

- **Institutional Buy/Sell** — Request signing now supports 1024-bit RSA keys.

---

## 2025-09-30

- **Institutional Buy/Sell** — New endpoint `Get Fiat Crypto Amount Limit`; the fiat and crypto
  amount limit fields are removed from `Get Trading Pair` in favour of it.
- **Institutional Buy/Sell** — Updated typical buy/sell sequence diagrams and flow descriptions.

---

## 2025-09-22

- **Institutional Buy/Sell** — `Get Quote` request field `spreadLevel` replaced with `customSpread`.
- **Institutional Buy/Sell** — Added typical buy/sell sequence diagrams and flow descriptions.
- New Futures Transfer for Link Sub-account endpoints

* POST `/sapi/v1/broker/futures/accountTransfer`

---

## 2025-09-16

- Futures commission rebate query endpoints require to input `symbol` or `pair`.

* GET `/sapi/v1/broker/subAccountApi/commission/futures`
* GET `/sapi/v1/broker/subAccountApi/commission/coinFutures`

---

## 2025-09-05

- **Institutional Buy/Sell** — Initial release of the Institutional Crypto Buy/Sell Solution under
  `/papi/v1/ramp/connect/prime/*`.

---

## 2025-07-02

- New endpoints for KYC SaaS Integration, KYC Querying, and Request for Information (RFI).

---

## 2025-04-18

- New Endpoint for delete sub account `DELETE /sapi/v1/broker/subAccount `.
- Create Link sub account API key endpoint and FAST api key creation endpoint support asymmetrical
  key type(Ed25519 and RSA). Please see
  https://www.binance.com/en/support/faq/detail/6b9a63f1e3384cf48a2eedb82767a69a

---

## 2025-03-07

- New Endpoint for query sub account deposit by depositId
  `GET /sapi/v2/broker/subAccount/depositHist `.

---

## 2025-02-26

- Update sub account deposit history Endpoint `GET /sapi/v1/broker/subAccount/depositHist `, adding
  "travelRuleStatus".

---

## 2024-10-30

- Update the `Weight(UID)` to 60 for Endpoint `GET /sapi/v3/broker/subAccount/futuresSummary `.

---

## 2024-08-15

- New parameter `filterResult ` will be available on August 16, 2024 for query futures commission
  rebate record:`GET /sapi/v1/broker/rebate/futures/recentRecord `. If `filterResult ` = TRUE,
  rebates not from its own sub accounts will be filtered out in response.

---

## 2024-06-28

- New Endpoint for query futures assets of
  sub-accounts:`GET /sapi/v3/broker/subAccount/futuresSummary `.
- Following endpoints will be deleted in a month:
  `GET /sapi/v1/broker/subAccount/futuresSummary `,`GET /sapi/v2/broker/subAccount/futuresSummary `.
  Please migrate the usage of legacy version(v1&v2) to the new (v3) version as soon as possible.

---

## 2024-06-06

- Endpoints adjustment: for internal transfers, the txid prefix has been replaced to “Off-chain
  transfer”on 28 May 2024. “internal transfer” flag is no longer available in the TXID field,
  including historical transactions, the following endpoints are impacted:
  `GET /sapi/v1/broker/subAccount/depositHist`.

---

## 2024-04-30

- Update the request limit for endpoint: `POST /sapi/v1/broker/subAccountApi`. You can only create 1
  api key for each sub account per second

- Update the request limit for endpoint: `DELETE /sapi/v1/broker/subAccountApi`. You can only delete
  1 api key for each sub account per second

---

## 2024-03-05

- Remove endpoint: `POST /sapi/v1/broker/subAccount/blvt`.

---

## 2023-12-15

- Update the default parameter values of endpoint: `GET /sapi/v1/broker/universalTransfer`.

---

## 2023-11-20

- Add `depositId` and `selfReturnStatus` in response of endpoint:
  `GET /sapi/v1/broker/subAccount/deposit`.

---

## 2023-10-04

- Remove endpoint: `POST /sapi/v1/broker/subAccountApi/permission/vanillaOptions`.

---

## 2023-08-31

- Remove endpoint: `POST /sapi/v1/broker/subAccount/margin`. To enable the margin account, simply
  transfer assets into Cross Margin wallet.

---

## 2023-06-08

- Update weight for endpoint: `POST /sapi/v1/broker/subAccountApi`. Weight(Master Account) changed
  to 3000

---

## 2023-01-13

- Remove 2 endpoints: `POST /sapi/v1/broker/subAccountApi/ipRestriction`,
  `POST /sapi/v1/broker/subAccountApi/ipRestriction/ipList`.

---

## 2022-12-16

- Remove "thirdPartyName" for `POST /sapi/v2/broker/subAccountApi/ipRestriction (HMAC SHA256)`,
  `POST /sapi/v1/broker/subAccountApi/ipRestriction`,
  `POST /sapi/v1/broker/subAccountApi/ipRestriction/ipList`,
  `DELETE /sapi/v1/broker/subAccountApi/ipRestriction/ipList`.

---

## 2022-11-28

- Add "the max length is 32 characters" in the description of clientTranId for endpoints
  `POST /sapi/v1/broker/universalTransfer`, `POST /sapi/v1/broker/transfer/futures`,
  `POST /sapi/v1/broker/transfer`.

---

## 2022-11-18

- Added new endpoint `POST /sapi/v2/sub-account/subAccountApi/ipRestriction` to support user update
  IP Restriction for Sub-Account API key.

---

## 2022-09-22

- Update `POST /sapi/v1/broker/subAccountApi/ipRestriction` to support user enable or disable Third
  party IP list name restriction for sub-account api key.
- Update `POST /sapi/v1/broker/subAccountApi/ipRestriction/ipList` to support user update Third
  party IP list name restriction for sub-account api key.
- Update `DELETE /sapi/v1/broker/subAccountApi/ipRestriction/ipList` to support user delete Third
  party IP list name restriction for sub-account api key.

---

## 2022-09-12

- Update `GET /sapi/v1/broker/subAccountApi/ipRestriction` to support user query third party IP list
  name.

---

## 2022-08-23

- Add 100-days query scope for `GET /sapi/v1/broker/universalTransfer` and
  `GET /sapi/v1/broker/transfer`.
- Add requests per UID are limited to 60 requests per minute for
  `GET /sapi/v1/broker/subAccount/spotSummary`.

---

## 2022-06-27

- Added a new rebate status field in API response for endpoints
  `GET /sapi/v1/broker/rebate/futures/recentRecord` and `GET /sapi/v1/broker/rebate/recentRecord`.

---

## 2021-04-29

- Added parameter `tag` and new field `email` in endpoint `POST /sapi/v1/broker/subAccount`.

---

## 2021-03-26

- Added new endpoint `POST /sapi/v1/broker/subAccountApi/permission/universalTransfer` to enable the
  api permission for a sub account to use `POST /sapi/v1/asset/transfer`endpoint.
- Added new endpoint `POST /sapi/v1/broker/subAccountApi/permission/vanillaOptions` to enable
  Vanilla Options permission for sub account api key.

---

## 2021-02-04

- Added parameter `fromId` and `toId` in endpoint `GET /sapi/v1/broker/transfer`. The parameter
  `subaccountId` will be removed on 02/10 16:00(UTC+8). Please adjust the program as soon as
  possible.

---

## 2021-02-04

- Added parameter showAllStatus in endpoint `GET /sapi/v1/broker/universalTransfer`.

---

## 2021-01-27

- Added new endpoint `GET /sapi/v2/broker/subAccount/futuresSummary` to support query subaccount
  Coin Margined Futures asset info.

---

## 2021-01-14

- Added parameter clientTranId in endpoint `POST /sapi/v1/broker/transfer/futures` and
  `GET /sapi/v1/broker/transfer/futures`.

---

## 2020-12-28

- Added parameters page and size in endpoint `GET /sapi/v1/broker/subAccountApi`.

---

## 2020-12-14

- The endpoint `GET /sapi/v1/broker/transfer/futures` can only get the latest history of past 30
  days.

---

## 2020-12-10

- Added new endpoint `POST /sapi/v1/broker/universalTransfer` to transfer spot and futures asset
  between master account and sub accounts.
- Added new endpoint `GET /sapi/v1/broker/universalTransfer` to get universal transfer history.

---

## 2020-11-27

- Added tranId in response of endpoint `GET /sapi/v1/broker/transfer/futures`.

---

## 2020-10-23

- Added parameter showAllStatus in endpoint `GET /sapi/v1/broker/transfer`.

---

## 2020-10-12

- Added parameter status in the response of endpoint `GET /sapi/v1/broker/transfer`.

---

## 2020-09-16

- Added new endpoint `POST /sapi/v1/broker/subAccountApi/commission/coinFutures` to change sub-
  account COIN-Ⓜ futures commission adjustment.
- Added new endpoint `GET /sapi/v1/broker/subAccountApi/commission/coinFutures` query sub- account
  COIN-Ⓜ futures commission adjustment.
- Added parameter confirmTimes in endpoint `GET /sapi/v1/broker/subAccount/depositHist`.

## 2020-09-11

- Added parameter email in endpoint `GET /sapi/v1/broker/subAccount`.

---

## 2020-09-07

- Added new endpoint `POST /sapi/v1/broker/subAccountApi/ipRestriction` to enable or disable IP
  restriction for sub-account api key.
- Added new endpoint `POST /sapi/v1/broker/subAccountApi/ipRestriction/ipList` to add IP restricion
  for sub-account api key.
- Added new endpoint `GET /sapi/v1/broker/subAccountApi/ipRestriction` to get IP restriction for
  sub-account api key.
- Added new endpoint `DELETE /sapi/v1/broker/subAccountApi/ipRestriction/ipList` to delete IP
  restriction for sub-account api key.

---

## 2020-09-02

- Added new endpoint `GET /sapi/v1/broker/rebate/futures/recentRecord` to get futures commision
  rebate record.
- Added new endpoint `POST /sapi/v1/broker/transfer/futures` to transfer futures asset directly.
- Added new endpoint `GET /sapi/v1/broker/transfer/futures` to get futures transfer history.

---

## 2020-08-25

- Added parameters page and size in endpoint `GET /sapi/v1/broker/rebate/recentRecord`.

---

## 2020-07-29

- Added new endpoint `POST /sapi/v1/broker/subAccount/blvt` to enable leverage token for
  sub-account.

---

## 2020-07-21

- Added parameters page and size in endpoint `GET /sapi/v1/broker/subAccount`.

---

## 2020-07-10

- Added default limit 500 in endpoint `GET /sapi/v1/broker/transfer`.

---

## 2020-06-15

- Added new endpoint `GET /sapi/v1/broker/subAccount/spotSummary` to query sub accounts spot asset.
- Added new endpoint `GET /sapi/v1/broker/subAccount/marginSummary` to query sub accounts margin
  asset.
- Added new endpoint `GET /sapi/v1/broker/subAccount/futuresSummary` to query sub accounts futures
  asset.

---

## 2020-06-12

- Added new endpoint `GET /sapi/v1/broker/rebate/recentRecord` to query broker commission rebate
  recent record.

---

## 2020-06-11

- Added new endpoint `GET /sapi/v1/broker/subAccount/depositHist` to query sub accounts deposit
  history.

---

## 2020-04-22

- New fields in response to `GET /sapi/v1/broker/subAccountApi/commission/futures` and
  `POST /sapi/v1/broker/subAccountApi/commission/futures`:
  - `makerCommission` for current futures commission ratio for maker;
  - `takerCommission` for current futures commission ratio for taker;

---

## 2020-04-03

- Added new endpoint `POST /sapi/v1/broker/subAccount/bnbBurn/spot` to enable or disable BNB Burn
  for sub-account spot and margin.

- Added new endpoint `POST /sapi/v1/broker/subAccount/bnbBurn/marginInterest` to enable or disable
  BNB Burn for sub-account margin interest.

- Added new endpoint `GET /sapi/v1/broker/subAccount/bnbBurn/status` to get BNB Burn status for
  sub-account.

---

## 2020-03-27

- Added parameters `clientTranId `in endpoints:
  - `POST /sapi/v1/broker/transfer`,
  - `GET /sapi/v1/broker/transfer`.

---

## 2020-02-12

- The below endpoints will be released in the future:
  - new endpoint `GET /sapi/v1/broker/rebate/recentRecord` to query broker commission rebate recent
    record.
  - new endpoint `GET /sapi/v1/broker/rebate/historicalRecord ` to get broker commission rebate
    historical record.

---

## 2019-12-23

- Added new endpoint `POST /sapi/v1/broker/subAccountApi/commission/futures` to change sub-account
  futures commission adjustment.

- Added new endpoint `GET /sapi/v1/broker/subAccountApi/commission/futures` to query sub-account
  futures commission adjustment.

---

## 2019-11-11

- Added parameters `marginTrade ` and `futuresTrade` in endpoints:
  - `POST /sapi/v1/broker/subAccountApi`,
  - `POST /sapi/v1/broker/subAccountApi/permission`.
- Added keys `marginTrade ` and `futuresTrade` in responses to endpoints:
  - `POST /sapi/v1/broker/subAccountApi`,
  - `GET /sapi/v1/broker/subAccountApi`,
  - `POST /sapi/v1/broker/subAccountApi/permission`.
- Added parameters `marginMakerCommission ` and `marginTakerCommission ` in endpoint
  `POST /sapi/v1/broker/subAccountApi/commission`.

- Added keys `marginMakerCommission ` and `marginTakerCommission ` in responses to endpoints:
  - `POST /sapi/v1/broker/subAccountApi/commission`,
  - `Get /sapi/v1/broker/subAccount/`.
- Added new endpoint `POST /sapi/v1/broker/subAccount/margin` for setting subaccount enable on
  margin.

- Added new endpoint `POST /sapi/v1/broker/subAccount/futures` for setting subaccount enable on
  futures.