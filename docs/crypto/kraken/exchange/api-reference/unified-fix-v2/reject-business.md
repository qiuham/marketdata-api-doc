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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-fix-v2/reject-business'
updated_at: 2026-11-22
---

# Business Message Reject

> Business-level rejection at the gateway or the trading engine

FIX
session: trading
35=j

Business-level rejection, used when a message is well formed but fails a business rule, at the gateway, when the matching engine admits it, or, for an amend, when the matching engine refuses it (a refused amend gets no Execution Report). This is where unsupported order features, an invalid Account, unknown symbols and orders, a ClOrdID that is not increasing or is already in use, rate limit breaches, risk limits and requests that time out surface. BusinessRejectRefID echoes the ClOrdID of the rejected message and BusinessRejectReason gives the code, with the detail in Text. A `35=j` for a request that timed out does not mean the request was refused: the engine may still apply it, an amend for example. Treat the outcome as unknown and check the order with an OrderStatusRequest (`35=H`) before you send the request again.

**Direction:** Kraken → client

***

**header** *required*

35=`j`

**45 - RefSeqNum** `SeqNum`

MsgSeqNum of the message being rejected.

**372 - RefMsgType** `string` *required*

MsgType of the message being rejected.

**379 - BusinessRejectRefID** `string`

ClOrdID of the message being rejected.

Required: Conditional

**380 - BusinessRejectReason** `integer` *required*

Why the message was rejected.

**Possible values:**

* `0` : Other - used for nearly every business reject: unsupported order features, an invalid Account, a ClOrdID that is not increasing or already in use, rate limit breaches, risk limits, engine refusals and a priced order on an instrument with no usable tick size (Text: "Instrument tick size is unavailable"). Also used when the lookup behind an OrderStatusRequest fails. Read Text (58).
* `1` : Unknown id - an amend names an order the session does not hold. A cancel for an unknown order is answered with an OrderCancelReject (`35=9`, CxlRejReason `1`) where that is enabled.
* `2` : Unknown instrument - Symbol or InstrumentID matches no tradable contract.
* `101` : Unknown order - an OrderStatusRequest for an order that is finished or not in the cache.
* `104` : Order too old - defined, but effectively never sent on US Perps: a finished order is answered with `101`.

Values `3`, `4`, `5`, `6`, `8`, `100`, `102` and `103` are defined by the Unified FIX dictionary but are not sent on US Perps order entry: a rate limit breach, a reused ClOrdID and an engine refusal all arrive as `0`, with the cause in Text (58).

> [!NOTE]
>
> **Business rejects: venue differences**
>
> | | US Perps | Spot | Futures |
> | :- | :- | :- | :- |
> | Unknown order on a cancel | `35=9` with CxlRejReason `1` (where enabled) | `35=j`, `380=1` | `35=j`, `380=1` |
> | Unknown order on an amend | `35=j`, `380=1` | `35=j`, `380=1` | `35=j`, `380=1` |
> | Unknown order on a status request | `35=j`, `380=101` | `35=j`, `380=101` | Status requests are off |

**58 - Text** `string`

Free-text description: the cancellation reason, reject reason, or order status detail.

**Format:** Free text set by Kraken; carries the reject or cancellation reason.

**trailer** *required*

***

> [accordion] Responses
>
> ```text Business Message Reject, unknown instrument theme={null}
> 8=FIX.4.4|9=156|35=j|34=4|49=KRAKEN-PERPS-TRD|52=20261030-22:26:26.060|56=CLIENT|45=4|58=ClOrdId 37954270166087300 : Invalid InstrumentID|372=D|379=37954270166087300|380=2|10=198|
> ```
