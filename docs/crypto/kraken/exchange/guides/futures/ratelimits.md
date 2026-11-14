---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/guides/futures/ratelimits'
updated_at: 2026-11-13
---

# Derivatives Rate Limits

> Request cost budgets and WebSocket connection limits for the Derivatives REST and WebSocket APIs

> [!NOTE]
>
> These limits apply to Derivatives endpoints only. For Spot trading engine limits see [Spot trading limits](https://docs.kraken.com/exchange/guides/general/ratelimits.md). For Spot REST call counter limits see [REST rate limits](https://docs.kraken.com/exchange/guides/rest/ratelimits.md).

## REST Request Limits

Request limits are determined from cost associated with each API call and rate limiting budgets depend on which path the endpoint uses. Public endpoints do not have a cost and therefore do not count against any rate limiting budget.
For `/derivatives` endpoints, clients can spend up to 500 every 10 seconds.

The below table displays the cost associated with each API call for `/derivatives` endpoints:

| Endpoint | Cost |
| :- | - |
| sendorder | 10 |
| editorder | 10 |
| cancelorder | 10 |
| batchorder | 9 + size of batch |
| accounts | 2 |
| openpositions | 2 |
| fills (without lastFillTime specified) | 2 |
| fills (with lastFillTime specified) | 25 |
| cancelallorders | 25 |
| cancelallordersafter | 25 |
| withdrawaltospotwallet | 100 |
| openorders | 2 |
| orders/status | 1 |
| unwindqueue | 200 |
| GET leveragepreferences | 2 |
| PUT leveragepreferences | 10 |
| GET pnlpreferences | 2 |
| PUT pnlpreferences | 10 |
| transfer (between Futures wallets) | 10 |
| transfer (to or from Spot) | 100 |
| GET transfer/assets | 2 |
| transfer/subaccount | 10 |
| subaccount/:subaccountUid/trading-enabled | 2 |
| self-trade-strategy | 2 |

On the [Batch Order](https://docs.kraken.com/api-reference/order-management/batch-order-management.md) endpoint, the cost is 9 + size of the batch of the requests.
For example, a batch of 10 order requests, (send, edit, and or cancel) sent through the Batch Order endpoint would cost 19.

If the API limit is exceeded, the API will return `error` equal to `apiLimitExceeded`.
For the FIX API the API Limit is done at the `CompID` level.

For `/history` endpoints, clients have a pool of up to 100 tokens that continually replenishes at a rate of 100 every 10 minutes.

The below table displays the cost associated with each API call for `/history` endpoints. The accountlog rate limit cost varies on the optional 'count' parameter (default count is 500):

| Endpoint | Cost |
| :- | - |
| historicalorders | 1 |
| historicaltriggers | 1 |
| historicalexecutions | 1 |
| positions | 1 |
| accountlogcsv | 6 |
| accountlog (count: 1 - 25) | 1 |
| accountlog (count: 26 - 50) | 2 |
| accountlog (count: 51 - 1000) | 3 |
| accountlog (count: 1001 - 5000) | 6 |
| accountlog (count: 5001 - 10000) | 10 |

### Example

The following shows the return of call of the `sendorder` endpoint where the API limit has been exceeded.

```json theme={null}
{
  "result": "error",
  "serverTime": "2016-02-25T09:45:53.818Z",
  "error": "apiLimitExceeded"
}
```

## Websocket Limits

There are limits to both the number of connections a client can have open concurrently and the number of requests an individual connection can make.
Limit values are subject to change and additional limits may be added in the future.

The current limits are:

| Resource | Allowance | Replenish Period |
| - | - | - |
| Connections | 100 | N/A |
| Requests | 100 | 1 second |
