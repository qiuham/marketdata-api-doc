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
source_url: 'https://docs.kraken.com/exchange/guides/rest/introduction'
updated_at: 2026-11-13
---

# Spot REST Introduction

> Overview of the Kraken Spot REST API organisation, requests, responses, and error handling

## OpenAPI spec

> [card] [Spot REST OpenAPI](https://docs.kraken.com/openapi/spot-rest.yaml)
>
> Download the Spot REST OpenAPI spec (YAML)

> [card] [Derivatives REST OpenAPI](https://docs.kraken.com/openapi/futures-rest.yaml)
>
> Download the Derivatives REST OpenAPI spec (YAML)

## API Organisation

The Spot REST API is organised by function, covering a wide range of services:

* [Market Data](https://docs.kraken.com/api-reference/market-data/get-order-book.md)
* [Account Data](https://docs.kraken.com/api-reference/account-data/get-account-balance.md)
* [Trading](https://docs.kraken.com/api-reference/trading/add-order.md)
* [Funding (Beta)](https://docs.kraken.com/api-reference/funding-beta/list-funding-methods.md)
* [Funding (Legacy)](https://docs.kraken.com/api-reference/funding/get-deposit-addresses.md)
* [Subaccounts](https://docs.kraken.com/api-reference/subaccounts/create-subaccount.md)
* [Earn](https://docs.kraken.com/api-reference/earn/allocate-earn-funds.md)
* [WebSocket Authentication](https://docs.kraken.com/api-reference/trading/get-websockets-token.md)

## Requests, Responses and Errors

### Requests

Request payloads supports Json encoding (`Content-Type: application/json`) as well as  form-encoded (`Content-Type: application/x-www-form-urlencoded`).
We recommend clients to specify `User-Agent` in the headers of all their requests. This will help us optimize interactions and improve the overall efficiency and security of the API.

### Responses

Responses are JSON encoded and contain one or two top-level keys (`result` and `error` for successful requests or those with warnings, or only `error` for failed or rejected requests)

### Example

Request:

```text theme={null}
GET <https://api.kraken.com/0/public/SystemStatus>
```

Successful response:

```json theme={null}
{
    "error": [],
    "result": {
        "status": "online",
        "timestamp": "2021-03-22T17:18:03Z"
    }
}
```

Error response:

```json theme={null}
{
    "error": [
        "EGeneral:Invalid arguments:ordertype"
    ]
}
```

### Error Details

HTTP status codes are generally not used by our API to convey information about the state of requests and any errors or warnings are denoted in the `error` field of the response as described above. Status codes **other** than 200 indicate that there was an issue with the request reaching our servers.

Error messages follow the general format "\<severity>\<category>: \<description>"

* \<severity> : `E` for error, `W` for warning.
* \<category> : `General`, `Auth`, `API`, `Query`, `Order`, `Trade`, `Funding`, or `Service`.
* \<description> : a text string that describes the reason for the error.

```text theme={null}
i.e., "EGeneral: Invalid arguments:ordertype"
```

Additional information can be found on the [error reference](https://docs.kraken.com/exchange/guides/general/errors.md) guide or the [support center](https://support.kraken.com/hc/en-us/articles/360001491786-API-error-messages).

## Related guides

> [card] [Authentication](https://docs.kraken.com/exchange/guides/rest/authentication.md)
>
> HMAC-SHA512 signature, nonce management, and API-Key header

> [card] [API key permissions](https://docs.kraken.com/exchange/guides/rest/api-keys.md)
>
> Which permissions to enable for each use case

> [card] [Error reference](https://docs.kraken.com/exchange/guides/general/errors.md)
>
> Full list of error codes and handling strategies

> [card] [Rate limits](https://docs.kraken.com/exchange/guides/rest/ratelimits.md)
>
> How the REST rate counter works

> [card] [API comparison](https://docs.kraken.com/exchange/guides/general/api-comparison.md)
>
> When to use REST vs WebSocket vs FIX
