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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/logon'
updated_at: 2026-11-13
---

# Logon

> Authenticate and establish a US Perps FIX order-entry session

FIX
session: admin
35=A

Authenticates the session and sets session-level parameters: the heartbeat interval, whether sequence numbers reset, and what happens to open orders on disconnect. Cancel-on-disconnect is done by the FIX gateway, which cancels the session's orders when it sees the disconnect; the matching engine's cancel-all-after timer is not used on US Perps. Trading sessions carry the API key, the HMAC-SHA512 password signature and a nonce close to Kraken server time (UAT accepts up to 60 seconds of drift; the production window is to be confirmed); keep your clock NTP-synced, because clock drift is the commonest cause of logon failure. All connections require TLS.

**Direction:** Client → Kraken, then Kraken → client

***

**header** *required*

35=`A`

**98 - EncryptMethod** `integer` *required*

Encryption method for the session. Always none, since TLS 1.3 encrypts at the transport layer.

**Possible values:**

* `0` : No encryption. The only value Kraken accepts - TLS 1.3 does the encrypting at the transport layer.

**108 - HeartBtInt** `integer` *required*

Heartbeat interval in seconds. Kraken recommends 60.

**Format:** Seconds. Kraken recommends 60.

**141 - ResetSeqNumFlag** `boolean`

Whether both sides reset their sequence numbers to 1 on this logon.

**Possible values:**

* `N` : Continue the existing sequence. Default - expect a ResendRequest if there is a gap.
* `Y` : Both sides reset MsgSeqNum to 1. Use on a first connect or after a session reset.

**553 - Username** `string`

Your FIX API key, created in Kraken Pro settings with FIX as the key type. Trading sessions only.

Required: Conditional

**554 - Password** `string`

Base64 HMAC-SHA512 signature over the logon fields and the nonce, keyed with the base64-decoded API secret. Trading sessions only.

**Format:** base64( HMAC-SHA512( base64decode(secret), SHA256(message input + nonce) ) )

Required: Conditional

**5025 - Nonce** `string`

Current time in milliseconds since the Unix epoch, as a string. The same value must appear in the password input. UAT accepts a nonce within 60 seconds of Kraken server time; the production window is to be confirmed, so keep your clock NTP-synced. Trading sessions only.

**Format:** Milliseconds since the Unix epoch, as a string, within 60 s of Kraken server time (UAT).

Required: Conditional

> [!NOTE]
>
> **Nonce freshness: venue differences**
>
> The nonce is still part of the signed password input on every venue.
>
> | | US Perps | Spot | Futures |
> | :- | :- | :- | :- |
> | Allowed drift | 60 seconds in UAT; production to be confirmed | Not checked in any deployment | Not checked in any deployment |

**5030 - ForceResetClOrdID** `boolean`

Whether to reset the session ClOrdID sequence on re-logon. Emergency use only.

**Possible values:**

* `N` : Keep enforcing ClOrdID uniqueness. Default.
* `Y` : Wipe the session's ClOrdID uniqueness history so previously used ids can be reused. Emergency use only.

**5033 - RelaxedClOrdID** `boolean`

Whether the strictly increasing ClOrdID requirement is relaxed. On US Perps a ClOrdID must always be a positive integer of at most 19 digits, whatever this value is. With `Y` the ClOrdID no longer has to be greater than the previous one, and you are responsible for never reusing a ClOrdID within the session. See [New Order Single](https://docs.kraken.com/exchange/api-reference/unified-fix-v2/nos.md) for how invalid values are rejected.

**Possible values:**

* `N` : ClOrdIDs must be strictly increasing within the session. Default.
* `Y` : Any positive integer (positive int64) is accepted, provided you do not reuse it within the session. Anything else is rejected with `35=3` and reason `5`.

**8674 - CancelOrdersOnDisconnect** `integer`

What happens to open orders if the session disconnects. Cancel-on-disconnect is on by default and needs no onboarding step. The FIX gateway cancels the orders; on US Perps the matching engine's cancel-all-after timer is off.

**Possible values:**

* `0` : Cancel open orders on disconnect. Default.
* `1` : Leave orders working after disconnect.

> [!NOTE]
>
> **Cancel-on-disconnect: venue differences**
>
> | | US Perps | Spot | Futures |
> | :- | :- | :- | :- |
> | Who cancels | The FIX gateway only | The gateway cancels the orders and, by default, also arms the back end's account-wide cancel-all-after timer as a backstop | The gateway only; one production deployment also arms the back-end timer |

**trailer** *required*
