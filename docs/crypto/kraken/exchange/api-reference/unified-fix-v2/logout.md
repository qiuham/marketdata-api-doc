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
updated_at: 2026-11-13
---

# Logout

> End a FIX session

FIX
session: admin
35=5

Initiates or confirms the end of the session, and carries the reason for a failed logon.

**Direction:** Either direction

***

**header** *required*

35=`5`

**58 - Text** `string`

Free-text description: the cancellation reason, reject reason, or order status detail.

**Format:** Free text set by Kraken; carries the reject or cancellation reason.

**trailer** *required*
