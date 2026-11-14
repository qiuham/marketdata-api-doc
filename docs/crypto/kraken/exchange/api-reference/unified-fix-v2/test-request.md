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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/test-request'
updated_at: 2026-11-13
---

# Test Request

> Probe whether the counterparty is still alive

FIX
session: admin
35=1

Sent when nothing has arrived within the heartbeat interval and the session's liveness is in doubt. The counterparty must respond with a Heartbeat echoing TestReqID, which is how the probe is matched to its answer.

**Direction:** Either direction

***

**header** *required*

35=`1`

**112 - TestReqID** `string` *required*

Token identifying the test request. A heartbeat answering a test request must echo the value it carried.

**trailer** *required*
