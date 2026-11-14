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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/user-config'
updated_at: 2026-11-13
---

# User Config

> Authenticated command to update user configuration settings for the session user.

> [!NOTE]
>
> Authenticated channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Command used to update user config on behalf of session user. Results of this command will be visible in the User stream.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> Request ID.
>
> **type** `string` *required*
>
> Command type. Value: `UserConfig`
>
> **data** `array` *required*
>
> User config data array.
>
> **properties**
>
> **Key** `string` *required*
>
> Key of config.
>
> **Value** `string`
>
> Configuration value, JSON-serialized and transmitted as a string. Escaped characters in the wire format are normal JSON encoding.
>
> **Mode** `string`
>
> Optional mode on config. Possible values: `Enabled`, `Disabled`
>
> **Timestamp** `string`
>
> Timestamp of the message.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 18,
>   "type": "UserConfig",
>   "data": [
>     {
>       "Key": "symbol",
>       "Value": "\"ETH-BTC\""
>     }
>   ]
> }
> ```
