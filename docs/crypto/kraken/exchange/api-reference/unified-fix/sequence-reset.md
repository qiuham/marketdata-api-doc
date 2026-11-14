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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/sequence-reset'
updated_at: 2026-11-13
---

# Sequence Reset

> Reset message sequence numbers via FIX

FIX
session: admin
35=4

The Sequence Reset message is used to reset the incoming sequence number on the opposing side.

***

**header** *required*

35=`4`

**123 - SequenceReset** `boolean` *required*

Indicates that the Sequence Reset (4) message is replacing administrative or application messages which will not be resent.

**Possible values:**

* `Y` : Gap Fill message, MsgSeqNum field valid
* `N` : Sequence Reset, ignore MsgSeqNum

**36 - NewSeqNo** `integer` *required*

New sequence number.

**trailer** *required*

```text Gap Fill — Skip a range of messages (client → server) theme={null}
8=FIX.4.4|9=70|35=4|34=8|49=CLIENT|56=KRAKEN-MD|52=20260407-14:32:01.000|123=Y|36=14|10=064|
```

```text Hard Reset — Reset sequence to 1 (client → server) theme={null}
8=FIX.4.4|9=70|35=4|34=1|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:01.000|123=N|36=1|10=083|
```
