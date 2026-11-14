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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/reject-business'
updated_at: 2026-11-13
---

# Reject - Business Level

> Business level message rejection via FIX

FIX
session: admin
35=j

If Kraken needs to reject a message before it reaches the Trading engine and gets an OrderID, the order or cancellation will be rejected using a Business level reject.

***

**header** *required*

35=`j`

**45 - RefSeqNum** `integer` *required*

Sequence number of the rejected message.

**372 - RefMsgType** `char` *required*

The MsgType `35` of the FIX message being referenced.

**379 - BusinessRejectRefID** `string` *required*

The value of the ClOrdID field on the message being rejected.

**380 - BusinessRejectReason** `integer` *required*

Code to identify reason for a Business Message Reject message.

**Possible values:**

* `0` : Others
* `1` : Unknown ID
* `2` : Unknown Instrument
* `3` : Unsupported Message Type
* `4` : Application not available
* `5` : Conditionally Required Field Missing
* `6` : Not Authorized
* `101` : Unknown order
* `104` : Order too old

**58 - Text** `string`

Full description for rejection.

**trailer** *required*

```text Insufficient Funds (BusinessRejectReason=0) theme={null}
8=FIX.4.4|9=127|35=j|34=16|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:05.122|45=0|58=EOrder:Insufficient funds|372=D|379=1744036325000000|380=0|10=080|
```

```text Order Minimum Not Met (BusinessRejectReason=0) theme={null}
8=FIX.4.4|9=130|35=j|34=18|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:05.000|45=0|58=EOrder:Order minimum not met|372=D|379=1744036334000000|380=0|10=015|
```

```text Unknown Order on Cancel (BusinessRejectReason=101) theme={null}
8=FIX.4.4|9=124|35=j|34=17|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:06.000|45=0|58=EOrder:Unknown order|372=F|379=1744036325999000|380=101|10=206|
```

```text Futures IOC — Would Enter Book (BusinessRejectReason=0) theme={null}
8=FIX.4.4|9=150|35=j|34=10|49=KRAKEN-DRV-TRD|56=CLIENT-DRV|52=20260407-14:32:05.122|45=0|58=IOC_WOULD_ENTER_BOOK|372=D|379=a17d4971-f00d-4f67-94d1-e7d604104ed2|380=0|10=242|
```
