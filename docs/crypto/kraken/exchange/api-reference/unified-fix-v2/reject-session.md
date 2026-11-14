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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/reject-session'
updated_at: 2026-11-13
---

# Reject (Session)

> Session-level rejection of a malformed message

FIX
session: admin
35=3

Session-level rejection. Kraken discards any message that is garbled, cannot be parsed, or fails a data integrity or field-level check, and reports it here with the sequence number and message type of the offending message. RefTagID names the offending tag where one can be identified. A FIX field-level validation failure on an order arrives here rather than as a business reject.

**Direction:** Kraken → client

***

**header** *required*

35=`3`

**45 - RefSeqNum** `SeqNum` *required*

MsgSeqNum of the message being rejected.

**371 - RefTagID** `integer`

Tag that caused the rejection.

Required: Conditional

**372 - RefMsgType** `string`

MsgType of the message being rejected.

**373 - SessionRejectReason** `integer`

Why the message was rejected at session level.

**Possible values:**

* `0` : Invalid tag number.
* `1` : Required tag missing. For example, `AllAccounts (5034)` on a US Perps OrderMassCancelRequest, or `Account (1)` with `AllAccounts=N`.
* `2` : Tag not defined for this message type. For example, `AllAccounts (5034)` or `Account (1)` on an OrderMassCancelRequest on a Spot or Futures session.
* `3` : Undefined tag.
* `4` : Tag specified without a value.
* `5` : Value is incorrect or out of range for this tag. For example, a ClOrdID that is not a positive integer (with `RelaxedClOrdID=Y`, anything other than a positive int64), or an ExecInst of `E` or `s` on an amend, or an `Account (1)` that is not a usable id (or is sent with `AllAccounts=Y`) on an OrderMassCancelRequest.
* `6` : Incorrect data format for value.
* `7` : Decryption problem.
* `8` : Signature problem.
* `9` : CompID problem.
* `10` : SendingTime accuracy problem.
* `11` : Invalid MsgType.
* `12` : XML validation error.
* `13` : Tag appears more than once.
* `14` : Tag out of required order.
* `15` : Repeating group fields out of order.
* `16` : Incorrect NumInGroup count.
* `17` : Field delimiter inside a non-data value.
* `99` : Other.

**58 - Text** `string`

Free-text description: the cancellation reason, reject reason, or order status detail.

**Format:** Free text set by Kraken; carries the reject or cancellation reason.

**trailer** *required*
