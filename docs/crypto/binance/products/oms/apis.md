---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/oms/apis
api_type: Guide
updated_at: 2026-11-18 18:29:05.178804
---

# APIs

The OMS Toolkit API is the `apiReferral` family — it configures the custom tag applied to an end
user's trades, and reports on the activity tagged to you.

> This index does not replace the endpoint reference. Each endpoint's parameters, responses, and
> error codes are in the [OMS REST API](/catalog/vip-and-institutional-oms/api/rest-api).

| Area                                                                 | What it covers                                                                                                                            |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Spot](/catalog/vip-and-institutional-oms/api/rest-api/spot)         | Set and query the customize ID applied to a spot user's trades, check whether a user is new, and query rebate and kickback records.       |
| [Futures](/catalog/vip-and-institutional-oms/api/rest-api/futures)   | The same customization and new-user checks for futures and Portfolio Margin, plus trade volume, rebate volume, trader counts, and income. |
| [Fast API](/catalog/vip-and-institutional-oms/api/rest-api/fast-api) | Create an API key for a user and query that key's status. See [Fast-API](/products/oms/Fast-API/overview) for onboarding and error codes. |

## How the tag reaches your reporting

You set a customize ID against a user, that user trades using their own Binance API key, and the
resulting activity is attributed to you. You then read it back through the reporting endpoints above
or in the OMS dashboard.

Note that the tag is configured and read through these REST endpoints — OMS Toolkit does not deliver
tagged activity over a user data stream.

For a walkthrough of becoming a Link & Trade partner, setting up your Link ID and querying rebate
stats, see
[How to Set Up the API Link ID?](https://www.binance.com/en/support/faq/detail/a78a065d0c4846aaa1af474d8e712ab9)

---

# APIs

The OMS Toolkit API is the `apiReferral` family — it configures the custom tag applied to an end
user's trades, and reports on the activity tagged to you.

> This index does not replace the endpoint reference. Each endpoint's parameters, responses, and
> error codes are in the [OMS REST API](/catalog/vip-and-institutional-oms/api/rest-api).

| Area                                                                 | What it covers                                                                                                                            |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Spot](/catalog/vip-and-institutional-oms/api/rest-api/spot)         | Set and query the customize ID applied to a spot user's trades, check whether a user is new, and query rebate and kickback records.       |
| [Futures](/catalog/vip-and-institutional-oms/api/rest-api/futures)   | The same customization and new-user checks for futures and Portfolio Margin, plus trade volume, rebate volume, trader counts, and income. |
| [Fast API](/catalog/vip-and-institutional-oms/api/rest-api/fast-api) | Create an API key for a user and query that key's status. See [Fast-API](/products/oms/Fast-API/overview) for onboarding and error codes. |

## How the tag reaches your reporting

You set a customize ID against a user, that user trades using their own Binance API key, and the
resulting activity is attributed to you. You then read it back through the reporting endpoints above
or in the OMS dashboard.

Note that the tag is configured and read through these REST endpoints — OMS Toolkit does not deliver
tagged activity over a user data stream.

For a walkthrough of becoming a Link & Trade partner, setting up your Link ID and querying rebate
stats, see
[How to Set Up the API Link ID?](https://www.binance.com/en/support/faq/detail/a78a065d0c4846aaa1af474d8e712ab9)