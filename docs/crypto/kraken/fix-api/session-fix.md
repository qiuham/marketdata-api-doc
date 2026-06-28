---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/fix-api/session-fix
api_type: REST
updated_at: 2026-05-27 19:44:03.758794
---

# Header & Trailer

The baseline specification for this API is FIX 4.4. A standard header must be present at the start of every message in both directions. All messages sent in either direction should contain both _**SenderCompID**_ and _**TargetCompID**_. These values will be communicated by kraken during the onboarding process.

## Standard Header 

### MESSAGE BODY

**8 - BeginString** string required

Must be `FIX.4.4`

**9 - BodyLength** integer required

Length of message expressed as the number of characters in the message following the BodyLength field up to, and including, the delimiter immediately preceding the checksum tag(10)

**35 - MsgType** char required

The message type

**34 - MsgSeqNum** integer required

The sequence number for this message

**52 - SendingTime** string required

**Format:** YYYYMMDD-HH:MM:SS.uuu

Time of message transmission by the sender expressed in UTC.

**49 - SenderCompID** string required

Identifies the party sending the message

**56 - TargetCompID** string required

Identifies the party receiving the message

**122 - OrigSendingTime** string conditional

**Condition:** Required for retransmission of message

**Format:** YYYYMMDD-HH:MM:SS.uuu

If no data is available, this value is set to the SendingTime value.

**43 - PossDupFlag** boolean

**Possible values:**[`true`, ` false`]

Indicates possible retransmission of message with this sequence number

## Standard Trailer

**10 - Checksum** string required

Always the last field in a FIX message