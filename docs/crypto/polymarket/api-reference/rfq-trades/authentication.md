---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/api-reference/rfq-trades/authentication'
updated_at: 2026-11-13
---

# Authentication

> Sign every RFQ Trades Partner API request, and the trade status stream's handshake, with your partner API key.

Every request is signed with your partner API key. Polymarket identifies your
platform from the key and never from the request body, so a request can only
read and create your own trades.

The API key identifies your platform. It does not authorize moving funds: each
counterparty authorizes its own side through its
[order signature](https://docs.polymarket.com/partners/rfq-trades.md#sign-the-orders).

## Your API Key

Polymarket issues each partner an API key during onboarding:

* **Key ID**: the public half, sent on every request.
* **Secret**: a base64url-encoded string, shared once through a secure
  channel. Decode it to bytes before using it as the HMAC key.

## Sign a Request

Sign every request except `GET /v1/time`:

**1. Create the Request Timestamp**

First, create a new Unix timestamp in seconds for each request. It must be
within 30 seconds of server time, in either direction. See
[Keep Your Clock in Sync](#keep-your-clock-in-sync).

**2. Create the Request Signature**

Next, concatenate the timestamp, the uppercase HTTP method, the request
path, and the exact serialized body you send, with no separators. Then sign
the result with your API key's secret, decoded from base64url:

```text theme={null}
rfq_timestamp = <unix_seconds>
method = "POST"
request_path = "/v1/rfq-trades/validate"
body = <exact_serialized_request_body>

message = rfq_timestamp + method + request_path + body
rfq_signature = urlsafeBase64WithPadding(
  HMAC-SHA256(base64UrlDecode(<rfq_secret>), message)
)
```

Where:

* `request_path` is the URL path only. The query string is not signed.
* `body` is the exact bytes sent. For a `GET`, it is empty. Serialize the
  body once and reuse that string for both the signature and the request,
  to avoid mismatches from key ordering or whitespace.
* `rfq_signature` is base64url-encoded **with padding** (RFC 4648 §5). It
  is not hex and not standard base64.

These helpers create the three headers for a request:

```typescript TypeScript theme={null}
import { createHmac } from "node:crypto";

const keyId = process.env.RFQ_KEY_ID!;
const secret = Buffer.from(process.env.RFQ_SECRET!, "base64url");

function signRequest(method: string, path: string, body = "") {
  const timestamp = Math.floor(Date.now() / 1000).toString();
  const signature = createHmac("sha256", secret)
    .update(timestamp + method.toUpperCase() + path + body)
    .digest("base64") // Node's "base64url" digest drops the padding.
    .replace(/\+/g, "-")
    .replace(/\//g, "_");

  return {
    "RFQ-Key-Id": keyId,
    "RFQ-Timestamp": timestamp,
    "RFQ-Signature": signature,
  };
}

const body = JSON.stringify({ marketId: "253591" /* ... */ });
await fetch(
  "https://external-rfq-partner.polymarket.com/v1/rfq-trades/validate",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...signRequest("POST", "/v1/rfq-trades/validate", body),
    },
    body,
  },
);
```

```python Python theme={null}
import base64
import hashlib
import hmac
import os
import time

KEY_ID = os.environ["RFQ_KEY_ID"]
SECRET = base64.urlsafe_b64decode(os.environ["RFQ_SECRET"])


def sign_request(method: str, path: str, body: bytes = b"") -> dict[str, str]:
    timestamp = str(int(time.time()))
    message = timestamp.encode() + method.upper().encode() + path.encode() + body
    digest = hmac.new(SECRET, message, hashlib.sha256).digest()
    return {
        "RFQ-Key-Id": KEY_ID,
        "RFQ-Timestamp": timestamp,
        "RFQ-Signature": base64.urlsafe_b64encode(digest).decode(),
    }
```

> [accordion] Test vector
>
> Use these inputs to check your implementation:
>
> | Input | Value |
> | - | - |
> | Secret (base64url) | `MDEyMzQ1Njc4OWFiY2RlZjAxMjM0NTY3ODlhYmNkZWY=` |
> | `RFQ-Timestamp` | `1753185296` |
> | Method | `POST` |
> | Path | `/v1/rfq-trades/validate` |
> | Body | `{"marketId":"253591"}` |
> | Expected `RFQ-Signature` | `H-yYb9AqRHJ7ysPVyqTxdT83YWWUB8KvS4okVchrrcU=` |

**3. Send an Authenticated Request**

Finally, send the key ID, the timestamp, and the signature as headers. This
request validates the terms of a trade:

```bash theme={null}
curl -X POST "https://external-rfq-partner.polymarket.com/v1/rfq-trades/validate" \
  -H "Content-Type: application/json" \
  -H "RFQ-Key-Id: <rfq_key_id>" \
  -H "RFQ-Timestamp: <rfq_timestamp>" \
  -H "RFQ-Signature: <rfq_signature>" \
  --data '{
    "marketId": "253591",
    "operation": "split",
    "price": "0.65",
    "shares": "1500000000",
    "parties": {
      "yes": { "maker": "<yes_deposit_wallet>", "signatureType": 3 },
      "no": { "maker": "<no_deposit_wallet>", "signatureType": 3 }
    }
  }'
```

Every authenticated request uses the same three headers:

| Header | Value |
| - | - |
| `RFQ-Key-Id` | Your API key ID |
| `RFQ-Timestamp` | The Unix timestamp used to build the signature |
| `RFQ-Signature` | The signature from the previous step |

## Keep Your Clock in Sync

`RFQ-Timestamp` must be within 30 seconds of server time, in either direction.
Keep your clock NTP-synced. If your requests start failing with `401`, compare
your clock with the server's: `GET /v1/time` needs no authentication.

```bash theme={null}
curl "https://external-rfq-partner.polymarket.com/v1/time"
```

The response body gives the server time:

```json theme={null}
{ "serverTime": "2026-07-24T12:34:56Z", "timestamp": 1784896496 }
```

`timestamp` is the server time in Unix seconds, in the same format as
`RFQ-Timestamp`.

## Authenticate the WebSocket

The trade status stream is authenticated once, on the upgrade request. Sign it
like any `GET`, with an empty body, and send the same three headers on the
handshake:

```text theme={null}
message = <rfq_timestamp> + "GET" + "/v1/ws/rfq-trades"
```

The stream then delivers only your own trades. See
[Track the Trade](https://docs.polymarket.com/partners/rfq-trades.md#track-the-trade).

## Authentication Errors

A request that fails authentication returns `401` with code
`authentication_failed`. Missing headers, a timestamp that isn't whole Unix
seconds, and a timestamp outside the 30-second window each have their own
message. An unknown or revoked key ID and a signature mismatch share one
generic message, for security.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
