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
source_url: 'https://docs.kraken.com/institutional/guides/custody-rest-auth'
updated_at: 2026-11-13
---

# Custody REST Authentication

> Authenticate Custody v0 requests with API keys, nonce headers, and HMAC-SHA512 signatures.

Authenticate nonce-based API-key requests to `/v0/insto/custody/` with the headers and signature described below. First, create a Custody API user and obtain its API key and Base64-encoded secret.

## API Users and Access Control

API users function similarly to human users in that they are assigned roles, permissions, and vault access at the time of creation. When an API user interacts with the system, these settings are enforced to control which data they can access and which actions they can perform.

However, unlike regular users, API users cannot log in to the Custody application. Their interaction with the system is limited strictly to API calls, making them an essential component for programmatic access while maintaining strict security boundaries.

## Creating a new API Key

A system administrator must initiate the creation of a new API user before generating an API key:

1. Log in to your Custody environment
2. Navigate to Settings → Users → API Users
3. Submit a request for a new API user and complete the two-factor authentication (2FA) process
4. The request will appear under Tasks → Pending until it is approved by the Admin Quorum
5. Once approved, open the request details to view the API key information
6. The admin user who submitted the request can access the API key and secret from the API key details page

> [!WARNING]
>
> Only the admin user who created the API user request can view the API key and secret. Store these credentials securely. For security reasons, the API key and secret will not be viewable again after they are generated. API key credentials are a prime target for malicious actors. Ensure you follow security best practices to protect them.

## Authentication headers

Send these headers with each authenticated v0 request:

| Header | Value |
| - | - |
| `api-key` | Your public API key. |
| `api-nonce` | A strictly increasing decimal integer for this API key. |
| `api-sign` | The Base64-encoded HMAC-SHA512 signature calculated below. |

Keep the secret on your client. Use it to calculate the signature; send only the
public key and signature in the request headers.

The nonce belongs in the `api-nonce` header. You do not need to add a `nonce` field
to a v0 JSON body. Generate nonces consistently across every process that shares
the key, and continue the key's existing sequence when migrating from a legacy
endpoint. A millisecond timestamp is suitable for a single request; concurrent
requests need coordinated nonce generation so values do not repeat or arrive out
of order.

## Calculate the signature

Use the exact request target and body you will send:

1. Take the complete path and query string, including `/v0/insto/custody/`, and
   preserve their URL encoding and query parameter order. Exclude the scheme,
   host, and HTTP method.
2. Append the exact request body bytes to the ASCII-encoded `api-nonce` value and
   calculate their SHA-256 digest. Keep the raw 32-byte digest.
3. Append that digest to the UTF-8-encoded path and query string.
4. Calculate HMAC-SHA512 over those bytes using your Base64-decoded API secret.
5. Base64-encode the HMAC result and send it as `api-sign`.

```text theme={null}
body_hash = SHA256(ASCII(api_nonce) || body_bytes)
api_sign = Base64(HMAC-SHA512(Base64Decode(api_secret), UTF8(path_and_query) || body_hash))
```

For a GET request with no body, `body_bytes` is empty. For JSON requests,
serialize the body once, sign those UTF-8 bytes, and send the same bytes with
`Content-Type: application/json`. Changing whitespace or property order after
signing changes the signature.

## Request examples

Set `KRAKEN_CUSTODY_API_KEY` and `KRAKEN_CUSTODY_API_SECRET` in your environment.
These examples list vaults with an empty GET body.

> [tab] Python
>
> ```python theme={null}
> import base64
> import hashlib
> import hmac
> import json
> import os
> import time
> import urllib.request
>
>
> def sign_request(path_and_query: str, nonce: str, body: bytes, secret: str) -> str:
>     body_hash = hashlib.sha256(nonce.encode("ascii") + body).digest()
>     message = path_and_query.encode("utf-8") + body_hash
>     signature = hmac.new(base64.b64decode(secret), message, hashlib.sha512).digest()
>     return base64.b64encode(signature).decode("ascii")
>
>
> path_and_query = "/v0/insto/custody/vaults?limit=10"
> nonce = str(time.time_ns() // 1_000_000)
> body = b""
> headers = {
>     "api-key": os.environ["KRAKEN_CUSTODY_API_KEY"],
>     "api-nonce": nonce,
>     "api-sign": sign_request(
>         path_and_query, nonce, body, os.environ["KRAKEN_CUSTODY_API_SECRET"]
>     ),
> }
> request = urllib.request.Request(
>     "https://api.kraken.com" + path_and_query,
>     headers=headers,
>     method="GET",
> )
> with urllib.request.urlopen(request, timeout=30) as response:
>     print(json.load(response))
> ```

> [tab] Node.js
>
> ```javascript theme={null}
> import { createHash, createHmac } from "node:crypto";
>
> function signRequest(pathAndQuery, nonce, body, secret) {
>   const bodyHash = createHash("sha256")
>     .update(nonce, "ascii")
>     .update(body)
>     .digest();
>   return createHmac("sha512", Buffer.from(secret, "base64"))
>     .update(pathAndQuery, "utf8")
>     .update(bodyHash)
>     .digest("base64");
> }
>
> const apiKey = process.env.KRAKEN_CUSTODY_API_KEY;
> const apiSecret = process.env.KRAKEN_CUSTODY_API_SECRET;
> if (!apiKey || !apiSecret) {
>   throw new Error("Set KRAKEN_CUSTODY_API_KEY and KRAKEN_CUSTODY_API_SECRET");
> }
>
> const pathAndQuery = "/v0/insto/custody/vaults?limit=10";
> const nonce = Date.now().toString();
> const body = Buffer.alloc(0);
> const response = await fetch("https://api.kraken.com" + pathAndQuery, {
>   method: "GET",
>   headers: {
>     "api-key": apiKey,
>     "api-nonce": nonce,
>     "api-sign": signRequest(pathAndQuery, nonce, body, apiSecret),
>   },
> });
> if (!response.ok) {
>   throw new Error(`Request failed with HTTP ${response.status}`);
> }
> console.log(await response.json());
> ```

## Verify your implementation

Use this fixed test vector to check your signature calculation offline. The
secret is an example value, and the nonce is fixed for this check. Use your own
credentials and a fresh nonce for API requests.

| Field | Value |
| - | - |
| API secret, Base64 | `c2VjcmV0` |
| `api-nonce` | `1700000000000` |
| Path and query | `/v0/insto/custody/vaults?limit=10` |
| Request body | Empty: zero bytes |

The expected `api-sign` is:

```text theme={null}
SRZSnh/6bbws0k08SS+JyjUpzbscES+wSYM9FGE7KoUabSMfA/R76tkzJQ3Mub3UMTsGbo0yo0JkZ8Z5x3WVeA==
```

## Migrating legacy authentication

Legacy `/0/private/*` requests carry `nonce` in the request body. Sign the legacy
path and the complete encoded body required by that endpoint, including its
`nonce` field.

For v0 requests, send `api-nonce` as a header and sign the complete v0 path and
query string. Follow the [legacy method mapping](https://docs.kraken.com/institutional/api-reference/custody-rest.md#moving-from-the-legacy-methods)
for the replacement routes.
