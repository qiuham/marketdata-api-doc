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
source_url: 'https://docs.kraken.com/exchange/api-reference/drop-copy/logon'
updated_at: 2026-11-23
---

# Logon

> Authenticate and establish a US Perps drop copy session

FIX
session: drop copy
35=A

Opens the session and agrees its parameters: the heartbeat interval, whether both sides reset sequence numbers, and the credentials. Credentials are required: the logon is authenticated the same way as the Unified FIX v2 trading session, with the API key, the HMAC-SHA512 password signature and a nonce within five seconds of Kraken server time. Without them the logon fails. Must be the first message after the transport connection is established. Alongside the standard FIX 4.4 Logon fields it carries a NoMsgTypes group and venue-defined tags in the 5025 and 9000 ranges: Nonce, user and publication preferences, and ApplicationName / Version / Vendor identification.

**Direction:** Either direction

***

**header** *required*

35=`A`

**98 - EncryptMethod** `integer` *required*

Encryption method for the session. Where TLS protects the transport the only meaningful value is 0 (None).

**Possible values:**

* `0` : None.
* `1` : PKCS.
* `2` : DES.
* `3` : PKCS/DES.
* `4` : PGP/DES.
* `5` : PGP/DES-MD5.
* `6` : PEM/DES-MD5.

**108 - HeartbeatInt** `integer` *required*

Heartbeat interval in seconds. This dialect names the field HeartbeatInt rather than the FIX 4.4 standard HeartBtInt.

**Format:** Interval in seconds.

**95 - RawDataLength** `Length`

Length in bytes of the RawData field that follows.

**Format:** Byte count.

Required: Conditional

**96 - RawData** `data`

Free-form binary payload. Not used for credentials; send them in Username (553) and Password (554).

**Format:** Raw data; length given by RawDataLength (95).

Required: Conditional

**141 - ResetSeqNumFlag** `boolean`

Whether both sides reset their sequence numbers to 1 on this logon.

**Possible values:**

* `Y` : Both sides reset MsgSeqNum to 1. Use it only on the first logon after the daily reset (22:00 UTC). At any other time, reports sent but not yet received are lost.
* `N` : Continue the existing sequence. Expect a ResendRequest if there is a gap.

**789 - NextExpectedMsgSeqNum** `SeqNum`

Next MsgSeqNum the sender expects to receive. An alternative to a Resend Request for resynchronising at logon.

**Format:** Sequence number.

**383 - MaxMessageSize** `Length`

Largest message in bytes the sender is willing to receive.

**Format:** Byte count.

**384 - NoMsgTypes** `NumInGroup`

Number of message-type entries that follow, declaring which message types the session will send or receive.

Required: Conditional

**repeating group**

**372 - RefMsgType** `string`

MsgType being referred to.

**Format:** Any MsgType value.

**385 - MsgDirection** `char`

Whether the referenced message type is sent or received by the party declaring it.

**Possible values:**

* `S` : The session sends this message type.
* `R` : The session receives this message type.

**464 - TestMessageIndicator** `boolean`

Whether this session is a test session rather than production.

**Possible values:**

* `Y` : Yes.
* `N` : No.

**553 - Username** `string` *required*

Your FIX API key, created in Kraken Pro settings with FIX as the key type.

**554 - Password** `string` *required*

Base64 HMAC-SHA512 signature over the logon fields and the nonce, keyed with the base64-decoded API secret.

**Format:** base64( HMAC-SHA512( base64decode(secret), SHA256(message input + nonce) ) )

**5025 - Nonce** `string` *required*

Current time in milliseconds since the Unix epoch, as a string, within five seconds of Kraken server time. The same value must appear in the password input. Clock drift is the commonest cause of logon failure.

**Format:** Milliseconds since the Unix epoch, as a string, within 5 s of Kraken server time.

**9001 - UserType** `integer`

Venue-defined. Category of user establishing the session.

**Format:** Venue-defined integer.

**9006 - StrategyPreference** `integer`

Venue-defined. Strategy handling preference for the session.

**Format:** Venue-defined integer.

**9007 - TimeStampPreference** `integer`

Venue-defined. Timestamp granularity or format preference for the session.

**Format:** Venue-defined integer.

**9008 - PublishClearingAllocations** `integer`

Venue-defined. Whether clearing allocations are published to this session.

**Format:** Venue-defined integer.

**9009 - PublishMiFIDRegisteredDetails** `integer`

Venue-defined. Whether MiFID registered details are published to this session.

**Format:** Venue-defined integer.

**9010 - PublishMktCreationRealtime** `integer`

Venue-defined. Whether market creation events are published to this session in real time.

**Format:** Venue-defined integer.

**9450 - ApplicationName** `string`

Venue-defined. Name of the client application connecting.

**9451 - ApplicationVersion** `string`

Venue-defined. Version of the client application.

**9452 - ApplicationVendor** `string`

Venue-defined. Vendor of the client application.

**trailer** *required*
