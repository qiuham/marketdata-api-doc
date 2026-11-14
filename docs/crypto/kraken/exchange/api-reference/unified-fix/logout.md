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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/logout'
updated_at: 2026-11-13
---

# Logout

> Terminate a FIX session

FIX
session: admin
35=5

The Logout message initiates or confirms the termination of a FIX session. Disconnection without the exchange of logout messages will be interpreted as an abnormal condition.
Before actually closing the session, the logout initiator must wait for the opposite side to respond with a confirming logout message. Abnormal disconnection without logout will activate cancel-on-disconnect on the session.

***

**header** *required*

35=`5`

**58 - Text** `string`

Reason for the logout. This will be used to explain why a logon failed.

**trailer** *required*

```text Client-initiated Logout (client → server) theme={null}
8=FIX.4.4|9=60|35=5|34=10|49=CLIENT|56=KRAKEN-TRD|52=20260407-14:32:10.000|10=137|
```

```text Server Confirms Logout (server → client) theme={null}
8=FIX.4.4|9=59|35=5|34=8|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:10.000|10=104|
```

```text Server-initiated Logout — Auth Failure (server → client) theme={null}
8=FIX.4.4|9=96|35=5|34=2|49=KRAKEN-TRD|56=CLIENT|52=20260407-14:32:01.000|58=Logon failed: invalid credentials|10=129|
```
