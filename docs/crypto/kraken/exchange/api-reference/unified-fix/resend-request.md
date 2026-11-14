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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix/resend-request'
updated_at: 2026-11-13
---

# Resend Request

> Request retransmission of messages when a sequence gap is detected

FIX
session: admin
35=2

The Resend Request message (`35=2`) is sent by either party when a sequence number gap is detected — that is, when an incoming message has a sequence number higher than expected. It requests the counterparty to retransmit all messages in the gap range.

Upon receiving a Resend Request, the counterparty should respond with either:

* The original messages with `PossDupFlag (43) = Y`, or
* A [Sequence Reset](https://docs.kraken.com/exchange/api-reference/unified-fix/sequence-reset.md) with `GapFillFlag (123) = Y` to skip messages that are no longer available (e.g. administrative messages).

***

## Fields

**header** *required*

35=`2`

**7 - BeginSeqNo** `integer` *required*

First message sequence number to be retransmitted.

**16 - EndSeqNo** `integer` *required*

Last message sequence number to be retransmitted. Use `0` to request all messages from `BeginSeqNo` onwards (i.e. up to the current sequence).

**trailer** *required*

***

## Sequence Reset — Gap Fill

When a Resend Request is received, respond with a Sequence Reset using `GapFillFlag (123) = Y` and `NewSeqNo (36)` set to the sequence number *after* the gap. This tells the server the client is skipping over the requested range rather than replaying it.

```text Resend Request (server → client) theme={null}
8=FIX.4.4|9=58|35=2|34=114|49=KRAKEN-MD|56=damien|52=20260407-20:23:52.000|7=8|16=0|10=142|
```

```text Sequence Reset GapFill (client → server) theme={null}
8=FIX.4.4|9=57|35=4|34=8|49=damien|56=KRAKEN-MD|52=20260407-20:23:52.000|123=Y|36=14|10=088|
```

> [!NOTE]
>
> **When to expect a Resend Request:** If your client reconnects to an existing session without resetting sequence numbers (`141=N`), or if a message is dropped in transit, the server will send a Resend Request for the missing range. Always be prepared to handle it.
