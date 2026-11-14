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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/heartbeat'
updated_at: 2026-11-13
---

# Heartbeat

> Keep the session alive during inactivity

FIX
session: admin
35=0

Sent when no other traffic has passed within the negotiated heartbeat interval, so that both sides can tell a quiet session from a dead one. When it answers a Test Request it must echo that request's TestReqID. The interval is negotiated through HeartBtInt (108) on Logon.

**Direction:** Either direction

***

**header** *required*

35=`0`

**112 - TestReqID** `string`

Token identifying the test request. A heartbeat answering a test request must echo the value it carried.

Required: Conditional

**trailer** *required*
