---
exchange: kraken
source_url: https://docs.kraken.com/exchange/api-reference/drop-copy/heartbeat
api_type: FIX
updated_at: 2026-11-18 01:44:47.778816
---

# Heartbeat

> Keep the session alive during inactivity

FIX
session: drop copy
35=0

Sent when no other traffic has passed within the negotiated heartbeat interval, so that each side can tell a quiet session from a dead one. When it answers a Test Request it must echo that request's TestReqID.

**Direction:** Either direction

***

**header** *required*

35=`0`

**112 - TestReqID** `string`

Token identifying a test request. A Heartbeat answering a Test Request must echo the value the request carried.

Required: Conditional

**trailer** *required*