---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/resend-request
api_type: FIX
updated_at: 2026-11-22 18:59:23.430142
---

# Resend Request(2) (Production FIX API)

> ResendRequest(2) recovers missed FIX messages from the Deribit production sequence gap by asking the counterparty to resend a specified message range.

The `Resend Request`(`2`) message is used by the server to initiate the
retransmission of messages. This function is utilized if a sequence number gap
is detected, if the receiving application lost a message, or as a function of
the initialization process.

### Arguments

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 7 | `BeginSeqNo` | int | Yes | The first message to repeat |
| 16 | `EndSeqNo` | int | Yes | The last message to repeat |


## Related topics

- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [Sequence Reset(4) (Production FIX API)](https://docs.deribit.com/fix-api/production/sequence-reset.md)
- [Request For Positions(AN) (Production FIX API)](https://docs.deribit.com/fix-api/production/request-for-positions.md)
- [User Request(BE) (Production FIX API)](https://docs.deribit.com/fix-api/production/user-request.md)
- [Test Request(1) (Production FIX API)](https://docs.deribit.com/fix-api/production/test-request.md)