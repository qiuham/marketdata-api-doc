---
exchange: deribit
source_url: https://docs.deribit.com/fix-api/production/sequence-reset
api_type: FIX
updated_at: 2026-11-25 19:00:45.507595
---

# Sequence Reset(4) (Production FIX API)

> SequenceReset(4) repositions FIX sequence numbers on the Deribit production FIX session to recover from gaps or apply a graceful counterparty reset.

The `Sequence Reset`(`4`) is to recover from an out-of-sequence condition, to
reestablish a FIX session after a sequence loss. The `MsgSeqNum`(`34`) in the
header is ignored.

### Arguments

| Tag | Name | Type | Required | Comments |
| - | - | - | - | - |
| 36 | `NewSeqNo` | SeqNum | Yes | New Sequence Number |

### Response

In reply to `Sequence Reset`(`4`), the exchange replies with `Resend
Request`(`2`) with `BeginSeqNo`(`7`) and `EndSeqNo`(`16`) equal to the passed
`NewSeqNo`(`36`) in case of success. In case of wrong arguments, the server
replies with `Resend Request`(`2`) with `BeginSeqNo`(`7`) and `EndSeqNo`(`16`)
equal to the current incoming sequence on the server.

The `Sequence Reset` (`4`) can only increase the sequence number. If a `Sequence
Reset`(`4`) is received attempting to decrease the next expected sequence number
the reply is `Resend Request`(`2`) with `BeginSeqNo`(`7`) and `EndSeqNo`(`16`)
equal to the current incoming sequence on the server.

After sending the correct `Sequence Reset`(`4`), the client should start sending
messages starting from the sequence number equal to the `NewSeqNo`(`36`) passed.


## Related topics

- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md)
- [Logout(5) (Production FIX API)](https://docs.deribit.com/fix-api/production/logout.md)
- [MMProtection Reset(MZ) (Production FIX API)](https://docs.deribit.com/fix-api/production/mmprotection-reset.md)
- [Resend Request(2) (Production FIX API)](https://docs.deribit.com/fix-api/production/resend-request.md)
- [MMProtection Limits Result (MR) (Production FIX API)](https://docs.deribit.com/fix-api/production/mmprotection-limits-result.md)