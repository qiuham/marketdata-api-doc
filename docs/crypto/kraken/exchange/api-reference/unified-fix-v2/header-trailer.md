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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/header-trailer'
updated_at: 2026-11-13
---

# Header & Trailer

> Standard FIX message header and trailer fields

FIX
session: admin
35=\*

The baseline specification for Unified FIX v2 is FIX 4.4. A standard header must be present at the start of every message in both directions, and a standard trailer closes every message. SenderCompID and TargetCompID are communicated by Kraken during onboarding.

## Standard Header

Present at the start of every message in both directions. Nine header fields are used, with the same tags, types and required flags as Unified FIX.

**8 - BeginString** `string` *required*

FIX protocol version. Always FIX.4.4.

**9 - BodyLength** `Length` *required*

Number of characters between this field and the checksum, counting the delimiter before the checksum.

**Format:** Character count from after this field up to and including the delimiter before tag 10.

**35 - MsgType** `string` *required*

Message type of this message.

**Possible values:**

* `0` : Heartbeat.
* `1` : TestRequest.
* `2` : ResendRequest.
* `3` : Reject.
* `4` : SequenceReset.
* `5` : Logout.
* `8` : ExecutionReport.
* `9` : OrderCancelReject.
* `A` : Logon.
* `D` : NewOrderSingle.
* `F` : OrderCancelRequest.
* `G` : OrderCancelReplaceRequest.
* `H` : OrderStatusRequest.
* `j` : BusinessMessageReject.
* `q` : OrderMassCancelRequest.

**49 - SenderCompID** `string` *required*

Identifier of the party sending the message. Provided by Kraken during onboarding.

**Format:** Assigned by Kraken at onboarding.

**56 - TargetCompID** `string` *required*

Identifier of the party receiving the message. KRAKEN-PERPS-TRD for US Perps order entry sessions.

**Format:** KRAKEN-PERPS-TRD

**34 - MsgSeqNum** `SeqNum` *required*

Sequence number of this message on the session.

**43 - PossDupFlag** `boolean`

Whether the message may be a retransmission of one already sent with this sequence number.

**Possible values:**

* `Y` : Possible duplicate — this sequence number may have been sent before.
* `N` : Not a duplicate.

**52 - SendingTime** `UTCTimestamp` *required*

Time the sender transmitted the message, in UTC, formatted YYYYMMDD-HH:MM:SS.uuu.

**Format:** UTC timestamp, YYYYMMDD-HH:MM:SS.uuu

**122 - OrigSendingTime** `UTCTimestamp`

Original sending time of a retransmitted message; set to SendingTime when no original is available.

**Format:** UTC timestamp, YYYYMMDD-HH:MM:SS.uuu

Required: Conditional

***

## Standard Trailer

Closes every message. CheckSum is always the final field.

**10 - CheckSum** `string` *required*

Modulo-256 checksum of the message. Always the last field.

**Format:** Three digits, modulo-256 sum of every preceding byte.
