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
source_url: 'https://docs.kraken.com/exchange/api-reference/drop-copy/test-request'
updated_at: 2026-11-19
---

# Test Request

> Probe whether the counterparty is still alive

FIX
session: drop copy
35=1

Probes whether the counterparty is still alive when nothing has arrived within the heartbeat interval. The counterparty must answer with a Heartbeat echoing TestReqID, which is how the probe is matched to its answer.

**Direction:** Either direction

***

**header** *required*

35=`1`

**112 - TestReqID** `string` *required*

Token identifying a test request. A Heartbeat answering a Test Request must echo the value the request carried.

**trailer** *required*
