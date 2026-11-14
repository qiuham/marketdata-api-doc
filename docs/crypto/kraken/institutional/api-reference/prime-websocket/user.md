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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/user'
updated_at: 2026-11-13
---

# User

> Authenticated channel for streaming updates for the current customer user.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Request for updates for this customer user. No subscription parameters required.

## Subscribe Request

> [tab] Subscribe Schema
>
> **reqid** `number` *required*
>
> Request ID - will be echoed back in the response structure.
>
> **type** `string` *required*
>
> Request type. Value: `subscribe`
>
> **streams** `array` *required*
>
> Array containing the User stream configuration.
>
> **properties**
>
> **name** `string` *required*
>
> Subscription name. Value: `User`

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 10,
>   "type": "subscribe",
>   "streams": [
>     {
>       "name": "User"
>     }
>   ]
> }
> ```

## Response

> [tab] Response Schema
>
> **reqid** `number` *required*
>
> A number that relates this response to a request.
>
> **type** `string` *required*
>
> The type of message sent.
>
> **ts** `string` *required*
>
> An ISO-8601 UTC string of the form `2019-02-13T05:17:32.000000Z`.
>
> **initial** `boolean`
>
> If this is initial data for a request, the initial flag will be set.
>
> **seqNum** `number` *required*
>
> The sequence number for this response per request.
>
> **action** `string`
>
> "Update" or "Remove" - tells the client if the given entity should be removed or added/updated.
>
> **data** `array` *required*
>
> Array of User data.
>
> **properties**
>
> **CustomerUserID** `string` *required*
>
> Server assigned ID of this Customer User.
>
> **Email** `string` *required*
>
> Email of Customer User.
>
> **DisplayName** `string` *required*
>
> Friendly name for customer user.
>
> **Config** `array` *required*
>
> List of user config settings.
>
> **properties**
>
> **Timestamp** `string` *required*
>
> Timestamp of config setting update.
>
> **CustomerUserID** `string` *required*
>
> Customer User for this config setting.
>
> **Mode** `string`
>
> Setting whether config is enabled, values Enabled or Disabled.
>
> **Key** `string` *required*
>
> User config key.
>
> **Value** `string` *required*
>
> Configuration value, JSON-serialized and transmitted as a string. Escaped characters in the wire format are normal JSON encoding.
>
> **Permissions** `array`
>
> List of permissions for the customer user.
>
> **MarketAccountAuthorizations** `object`
>
> Market account authorizations mapping market accounts to their respective permissions.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 10,
>   "type": "User",
>   "ts": "2021-09-15T03:33:07.545223Z",
>   "initial": true,
>   "seqNum": 1,
>   "data": [
>     {
>       "CustomerUserID": "174K1Q9GC0C00",
>       "Email": "tom@company.com",
>       "DisplayName": "Tom",
>       "Config": [
>         {
>           "Timestamp": 1628004805337309202,
>           "CustomerUserID": "174K1Q9GC0C00",
>           "Key": "recentSymbols",
>           "Value": "{\"BTC-USD\":[1626111502357],\"ADA-USD\":[1626732116743],\"BCH-USD\":[1628004751665]}"
>         },
>         {
>           "Timestamp": 1628004805377207692,
>           "CustomerUserID": "174K1Q9GC0C00",
>           "Key": "symbol",
>           "Value": "\"BTC-USD\""
>         }
>       ],
>       "Permissions": [
>         "read::orders",
>         "write::orders",
>         "read::marketdata",
>         "read::entity"
>       ],
>       "MarketAccountAuthorizations": {
>         "market-account-1": [
>           "read::orders",
>           "read::marketdata",
>           "read::entity"
>         ],
>         "market-account-2": ["read::orders", "read::marketdata", "read::entity"]
>       }
>     }
>   ]
> }
> ```
