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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/logout'
updated_at: 2026-11-18
---

# Logout

> End a FIX session

FIX
session: admin
35=5

Ends the session. A client sends it to end the session: Kraken does not reply and the connection is closed, so do not wait for a Logout in return. Kraken sends it, with the reason in Text (58), when a logon fails.

**Direction:** Either direction

***

**header** *required*

35=`5`

**58 - Text** `string`

Free-text description: the cancellation reason, reject reason, or order status detail.

**Format:** Free text set by Kraken; carries the reject or cancellation reason.

**trailer** *required*

***

```text Logout theme={null}
8=FIX.4.4|9=97|35=5|49=CLIENT|56=KRAKEN-PERPS-TRD|34=24|52=20261027-14:17:05.689|58=Client initiated disconnect|10=155|
```
