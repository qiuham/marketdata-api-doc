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
source_url: 'https://docs.kraken.com/exchange/guides/fix/authentication'
updated_at: 2026-11-13
---

# FIX Authentication

> SenderCompID assignment, Logon message structure, password encoding, and session-level authentication for the Kraken Unified FIX API

## SenderCompID

Every FIX message — including the initial [Logon](https://docs.kraken.com/exchange/api-reference/unified-fix/logon.md) — requires a `SenderCompID` (tag 49). This identifier is assigned to you by Kraken during onboarding.

* **Spot** sessions use your standard SenderCompID
* **Derivatives** sessions use a SenderCompID with a `DRV` suffix
* Trading and Market Data sessions use the same SenderCompID but connect to different ports

> [!NOTE]
>
> Contact your Account Manager to request your SenderCompID and connection details.

## API Key Setup

Private trading sessions require an API Key with **FIX** permissions. Create one in [Kraken Pro settings](https://pro.kraken.com/app/settings/api).

| Session | API Key type needed |
| - | - |
| Spot trading | FIX key created under your Spot account |
| Derivatives trading | FIX key created under your Derivatives account |

Note that a FIX key is created as a Spot key, even when used for Derivatives trading.

We recommend using separate API Keys for Spot and Derivatives, even though the authentication mechanism is identical.

## Authentication Flow

Market Data sessions authenticate with the SenderCompID alone. Trading sessions require an additional HMAC signature:

1. Generate a `Nonce` — current time in milliseconds since Unix epoch
2. Build the `MessageInput` string from fixed FIX fields
3. Compute `SHA256(MessageInput + Nonce)`
4. Sign it with `HMAC-SHA512` using your base64-decoded API Secret
5. base64-encode the result → this is your `Password` (tag 554)
6. Send the Logon with `UserName` (tag 553), `Password` (tag 554), and `Nonce` (tag 5025)

See the [Logon](https://docs.kraken.com/exchange/api-reference/unified-fix/logon.md) page for the full field reference and code examples in Python, Node.js, Java, Go, and C#.
