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
source_url: 'https://docs.kraken.com/institutional/guides/prime-websocket-auth'
updated_at: 2026-11-13
---

# Prime WebSocket Authentication

> How to authenticate WebSocket connections to the Kraken Prime API using HMAC-SHA256 signed headers.

> [!NOTE]
>
> Authenticated connection. Connect to: `wss://wss.prime.kraken.com/ws/v1`

WebSocket connections must be authenticated by signing the request and sending the signature in HTTP headers.

## Connection Headers

> [tab] Header Schema
>
> | Header | Type | Description |
> | - | - | - |
> | **ApiKey** | string | Your Kraken API key |
> | **ApiSign** | string | base64-encoded signature |
> | **ApiTimestamp** | string | An ISO-8601 UTC string of the form `2019-02-13T05:17:32.000000Z` |

> [tab] Signature Generation
>
> The signature is a base64 encoded sha256 HMAC using the API secret of the following:
>
> ```
> GET\n<ApiTimestamp>\n<host>\n<path>
> ```
>
> For example:
>
> ```
> GET\n2019-02-13T05:17:32.000000Z\nwss.sandbox.prime.kraken.com\n/ws/v1
> ```

> [tab] Python Example
>
> ```python theme={null}
> # to install websocket lib:
> # $ pip install websocket-client
> from websocket import create_connection
> import datetime
> import hmac
> import hashlib
> import base64
>
> api_key = "<apikey>"
> api_secret = "<apisecret>"
>
> utc_now = datetime.datetime.utcnow()
> utc_datetime = utc_now.strftime("%Y-%m-%dT%H:%M:%S.000000Z")
>
> host = "<websocket host>"  # wss.sandbox.prime.kraken.com, for example
> path = "/ws/v1"
>
> params = "\n".join([
>     "GET",
>     utc_datetime,
>     host,
>     path,
> ])
>
> hash = hmac.new(
>     api_secret.encode('ascii'), params.encode('ascii'), hashlib.sha256)
> hash.hexdigest()
>
> signature = base64.urlsafe_b64encode(hash.digest()).decode()
>
> header = {
>     "ApiKey": api_key,
>     "ApiSign": signature,
>     "ApiTimestamp": utc_datetime,
> }
>
> ws = create_connection("wss://" + host + path, header=header)
>
> while True:
>     print(ws.recv())
> ```

## Environments

| Environment | WebSocket Endpoint |
| - | - |
| **Sandbox** | `wss://wss.sandbox.prime.kraken.com/ws/v1` |
| **Production** | `wss://wss.prime.kraken.com/ws/v1` |

## API Keys

For initial Prime access and onboarding, contact Kraken support at [prime\_trading@kraken.com](mailto:prime_trading@kraken.com) or your Account Manager.

After your Prime account is onboarded, you can create and manage API keys self-service from the [Prime UI API settings](https://pro.kraken.com/app/prime/api-settings). Sign in with your standard Kraken Pro credentials.

You will need separate API keys for the sandbox and production environments.

## Rate Limits

There is no limit to how many concurrent websocket connections you're allowed, though this may change in the future. If you expect to have more than \~10 active connections, please contact [prime\_trading@kraken.com](mailto:prime_trading@kraken.com).
