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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/header-trailer'
updated_at: 2026-11-13
---

# Header & Trailer

> Standard FIX message header and trailer fields

FIX
session: admin
35=\*

The baseline specification for this API is FIX 4.4. A standard header must be present at the start of every message in both directions. All messages sent in either direction should contain both **SenderCompID** and **TargetCompID**.
These values will be communicated by Kraken during the onboarding process.

## Standard Header

**8 - BeginString** `string` *required*

Must be `FIX.4.4`

**9 - BodyLength** `integer` *required*

Length of message expressed as the number of characters in the message following the BodyLength field up to, and including, the delimiter immediately preceding the checksum tag (10).

**35 - MsgType** `char` *required*

The message type.

**34 - MsgSeqNum** `integer` *required*

The sequence number for this message.

**52 - SendingTime** `string` *required*

Time of message transmission by the sender expressed in UTC. Format: `YYYYMMDD-HH:MM:SS.uuu`

**49 - SenderCompID** `string` *required*

Identifies the party sending the message.

**56 - TargetCompID** `string` *required*

Identifies the party receiving the message.

**122 - OrigSendingTime** `string`

If no data is available, this value is set to the SendingTime value. Format: `YYYYMMDD-HH:MM:SS.uuu`

Condition: Required for retransmission of message

**43 - PossDupFlag** `boolean`

Indicates possible retransmission of message with this sequence number.

***

## Standard Trailer

**10 - Checksum** `string` *required*

Always the last field in a FIX message.
