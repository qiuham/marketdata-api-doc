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
source_url: 'https://docs.kraken.com/exchange/api-reference/drop-copy/header-trailer'
updated_at: 2026-11-27
---

# Header & Trailer

> Standard FIX message header and trailer fields

FIX
session: drop copy
35=\*

The baseline specification for the US Perps drop copy is FIX 4.4. A standard header must be present at the start of every message in both directions, and a standard trailer closes every message. Kraken's CompID is `KRAKEN-PERPS-DC`. The client's CompID is assigned by Kraken at onboarding. See SenderCompID (49) and TargetCompID (56) for which goes where.

## Standard Header

Present at the start of every message in both directions. The full standard FIX 4.4 header is supported: thirty fields, including the SecureData, XmlData and NoHops constructs that most drop-copy sessions never populate. Six fields are required; the remaining twenty-four are optional and may be left unused.

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
* `A` : Logon.

**49 - SenderCompID** `string` *required*

Identifier of the party sending the message.

**Format:**

* Message from the client: assigned by Kraken at onboarding.
* Message from the exchange: `KRAKEN-PERPS-DC`.

**56 - TargetCompID** `string` *required*

Identifier of the party receiving the message.

**Format:**

* Message from the client: `KRAKEN-PERPS-DC`.
* Message from the exchange: assigned by Kraken at onboarding.

**115 - OnBehalfOfCompID** `string`

CompID of the firm the message is sent on behalf of, when a third party is relaying.

**128 - DeliverToCompID** `string`

CompID of the firm the message is ultimately to be delivered to, when a third party is relaying.

**90 - SecureDataLen** `Length`

Length in bytes of the SecureData field that follows.

**Format:** Byte count.

Required: Conditional

**91 - SecureData** `data`

Encrypted portion of the message. Unused where TLS protects the transport.

**Format:** Raw data; length given by SecureDataLen (90).

Required: Conditional

**34 - MsgSeqNum** `SeqNum` *required*

Sequence number of this message on the session.

**Format:** Sequence number of this message on the session, per direction.

**50 - SenderSubID** `string`

Sub-identifier within SenderCompID, e.g. a desk or trader.

**142 - SenderLocationID** `string`

Location of the sending party, e.g. a country or state code.

**57 - TargetSubID** `string`

Sub-identifier within TargetCompID.

**143 - TargetLocationID** `string`

Location of the receiving party.

**116 - OnBehalfOfSubID** `string`

Sub-identifier within OnBehalfOfCompID.

**144 - OnBehalfOfLocationID** `string`

Location of the OnBehalfOfCompID party.

**129 - DeliverToSubID** `string`

Sub-identifier within DeliverToCompID.

**145 - DeliverToLocationID** `string`

Location of the DeliverToCompID party.

**43 - PossDupFlag** `boolean`

Whether the message may be a retransmission of one already sent with this sequence number.

**Possible values:**

* `Y` : Possible duplicate — this sequence number may have been sent before.
* `N` : Not a duplicate.

**97 - PossResend** `boolean`

Whether the message was resent from the application layer rather than the session layer, so the receiver should check for a duplicate at the business level.

**Possible values:**

* `Y` : Yes.
* `N` : No.

**52 - SendingTime** `UTCTimestamp` *required*

Time the sender transmitted the message, in UTC.

**Format:** UTC timestamp, YYYYMMDD-HH:MM:SS.uuu

**122 - OrigSendingTime** `UTCTimestamp`

Original sending time of a retransmitted message; set to SendingTime when no original is available. Required on a retransmission.

**Format:** UTC timestamp, YYYYMMDD-HH:MM:SS.uuu

Required: Conditional

**212 - XmlDataLen** `Length`

Length in bytes of the XmlData field that follows.

**Format:** Byte count.

Required: Conditional

**213 - XmlData** `data`

XML payload carried inside the FIX message.

**Format:** Raw data; length given by XmlDataLen (212).

Required: Conditional

**347 - MessageEncoding** `string`

Character encoding of the Encoded\* fields in this message.

**Format:** EUC-JP, ISO-2022-JP, Shift\_JIS or UTF-8.

**369 - LastMsgSeqNumProcessed** `SeqNum`

Highest MsgSeqNum the sender has processed from the counterparty. Lets each side confirm its position without a Test Request.

**Format:** Sequence number.

**627 - NoHops** `NumInGroup`

Number of hop entries that follow, recording each third party the message passed through.

**repeating group**

**628 - HopCompID** `string`

CompID of the third party that forwarded this message.

**629 - HopSendingTime** `UTCTimestamp`

Time that third party sent the message.

**Format:** UTC timestamp, YYYYMMDD-HH:MM:SS.uuu

**630 - HopRefID** `SeqNum`

MsgSeqNum the message carried on that hop.

**Format:** Sequence number.

***

## Standard Trailer

Closes every message. CheckSum is always the final field. SignatureLength and Signature are the standard FIX 4.4 message-signing pair and are optional; they are rarely used where the transport is already protected by TLS.

**93 - SignatureLength** `Length`

Length in bytes of the Signature field that follows.

**Format:** Byte count.

**89 - Signature** `data`

Message signature. Optional, and rarely used where TLS already protects the transport.

**Format:** Raw data; length given by SignatureLength (93).

**10 - CheckSum** `string` *required*

Modulo-256 checksum of the message. Always the last field.

**Format:** Three digits, modulo-256 sum of every preceding byte.
