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
source_url: 'https://docs.kraken.com/exchange/api-reference/drop-copy/reject'
updated_at: 2026-11-27
---

# Reject

> Session-level rejection of a malformed message

FIX
session: drop copy
35=3

Session-level rejection of a message that is malformed, cannot be parsed, or fails a field-level validation check. RefSeqNum identifies the offending message and RefTagID names the offending tag where one can be identified. A session-level reject is not the same thing as a business rejection.

**Direction:** Either direction

***

**header** *required*

35=`3`

**45 - RefSeqNum** `SeqNum` *required*

MsgSeqNum of the message being rejected.

**Format:** Sequence number.

**371 - RefTagID** `integer`

Tag that caused the rejection, where one can be identified.

**Format:** FIX tag number.

Required: Conditional

**372 - RefMsgType** `string`

MsgType being referred to.

**Format:** Any MsgType value.

Required: Conditional

**373 - SessionRejectReason** `integer`

Why the message was rejected at session level.

**Possible values:**

* `0` : Invalid tag number.
* `1` : Required tag missing.
* `2` : Tag not defined for this message type.
* `3` : Undefined tag.
* `4` : Tag specified without a value.
* `5` : Value is incorrect or out of range for this tag.
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

Free-text description. Carries the reject reason, the logout reason, or other detail.

**Format:** Free text set by the sender.

**354 - EncodedTextLen** `Length`

Length in bytes of the EncodedText field that follows.

**Format:** Byte count.

Required: Conditional

**355 - EncodedText** `data`

Text repeated in a non-ASCII encoding, as named by MessageEncoding (347).

**Format:** Raw data; length given by EncodedTextLen (354).

Required: Conditional

**trailer** *required*
