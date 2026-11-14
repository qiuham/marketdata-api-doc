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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/reject-session'
updated_at: 2026-11-13
---

# Reject - Session Level

> Session level message rejection via FIX

FIX
session: admin
35=3

Kraken will disregard any message that is garbled, cannot be parsed or fails a data integrity check. These messages will be rejected using the Session Level reject.

***

**header** *required*

35=`3`

**45 - RefSeqNum** `integer` *required*

Sequence number of the rejected message.

**371 - RefTagID** `char`

Condition: When rejected due to a specific tag

**372 - RefMsgType** `char` *required*

The MsgType `35` of the FIX message being referenced.

**373 - SessionRejectReason** `integer` *required*

Refer to standard FIX 4.4 documentation.

**58 - Text** `string`

Full description for rejection.

**trailer** *required*

```text Missing Mandatory Field (SessionRejectReason=1) theme={null}
8=FIX.4.4|9=123|35=3|34=14|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:05.122|45=12|371=54|372=D|373=1|58=Missing mandatory field: Side (54)|10=139|
```

```text Invalid Field Value (SessionRejectReason=5) theme={null}
8=FIX.4.4|9=124|35=3|34=15|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:05.122|45=13|371=40|372=D|373=5|58=Invalid value for tag 40: OrderType|10=042|
```

```text Futures — COMB UUID Required for ClOrdID theme={null}
8=FIX.4.4|9=143|35=3|34=16|49=KRAKEN-DRV-TRD|56=CLIENT-DRV|52=20260407-14:32:05.122|45=3|371=11|372=D|373=5|58=COMB UUIDv4 required for ClOrdID on derivatives|10=054|
```
