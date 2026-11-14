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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/quotes'
updated_at: 2026-11-13
---

# Quotes

> Subscribe to your RFQs with their best quotes, and to the offers you have placed

UWS
uws.kraken.com/v2/private
quotes

The `quotes` channel streams your side of the request for quote (RFQ) workflow. It sends two types of entry:

* `rfq`: an RFQ you created, with the best bid and best ask offered on it so far.
* `offer`: an offer you placed on another account's RFQ.

For the public list of all open RFQs, see the [`rfqs`](https://docs.kraken.com/exchange/api-reference/unified-ws/rfqs) channel. That channel never shows offers or who made a request.

When the requester accepts an offer, the trades it produces are sent as ordinary executions with `order_type` `rfq` on the [`executions`](https://docs.kraken.com/exchange/api-reference/unified-ws/executions) channel. There is one fill per leg. They are not sent on this channel. The order in which the RFQ status update, the executions and the [`positions`](https://docs.kraken.com/exchange/api-reference/unified-ws/positions) updates arrive is not guaranteed.

The channel does not carry mark prices. To get them, subscribe to the [`ticker`](https://docs.kraken.com/exchange/api-reference/unified-ws/ticker) channel.

> [!NOTE]
>
> Messages on this channel carry no sequence numbers. To recover after a gap, resubscribe with `snapshot` set to `true`.

The `asset_class` parameter is required on every `subscribe` and `unsubscribe` request for the `quotes` channel. Requests that omit it are not accepted.

This channel contains account specific data, an authentication token is required in the request.

## Subscribe

> [tab] Request
>
> **method** `string` *required*
>
> Value: `subscribe`
>
> **params** `object` *required*
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `quotes`
>
> **asset\_class** `string` *required*
>
> One of: `derivatives`
>
> The asset class for the request. Must be included.
>
> **token** `string` *required*
>
> Authentication token. See [authentication guide](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for details.
>
> **snapshot** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `true`
>
> Request a snapshot of your open RFQs and offers after subscribing.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> **method** `string` *required*
>
> Value: `subscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `quotes`
>
> **asset\_class** `string`
>
> The asset class of the subscription.
>
> **snapshot** `boolean`
>
> Indicates if a snapshot is requested.
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **time\_in** `string`
>
> The timestamp when the subscription was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.
>
> If the feed is not ready yet, for example just after the service starts, the subscription fails with the error `RFQ feed warming up, please retry`. Retry with backoff.

## Snapshot / Update

The snapshot and update messages share the same schema. The snapshot lists your open RFQs and your open offers. After that, an update is sent each time one of them changes:

* The best offers on your RFQ change: an offer is placed, re-quoted or withdrawn.
* You re-quote one of your offers. The update keeps the same `offer_id`.
* You withdraw one of your offers, or it is cancelled because it failed its checks when the requester tried to accept it. Your offer gets a final update with status `cancelled`.
* An RFQ closes. Your RFQ, and each offer on it, gets a final update with the RFQ's status: `expired`, `cancelled`, `filled_bid_side` or `filled_ask_side`.

After its final update, an entry is no longer sent.

> [!WARNING]
>
> When an RFQ is filled, every offer on it gets the status `filled_bid_side` or `filled_ask_side`, including offers that were not accepted. This status does not mean your offer traded. To see whether it did, check the [`executions`](https://docs.kraken.com/exchange/api-reference/unified-ws/executions) channel.

If the closing message is lost, the RFQ and its offers are closed with status `expired` 10 seconds after the RFQ's `expiry`. A snapshot never includes an RFQ that is past its `expiry`, or its offers.

You may receive another `snapshot` after the first one if you subscribed with `snapshot` set to `true`. This happens when the feed recovers from a connection loss or the trading engine restarts. When you receive one, replace your RFQs and offers with its contents. After an engine restart, every open RFQ and offer first receives an update with status `cancelled`, then you receive an empty snapshot.

Each entry in `data` has a `type` field, `rfq` or `offer`, that tells you which fields it carries.

**channel** `string`

Value: `quotes`

**type** `string`

One of: `snapshot`, `update`

**data** `object[]`

A list of RFQ and offer entries.

**properties**

**type** `string`

One of: `rfq`, `offer`

The type of entry.

**offer\_id** `string`

Condition: `offer` entries only.\\

Format: UUID

The unique identifier of your offer.

**rfq\_id** `string`

Format: UUID

The unique identifier of the RFQ. On an `offer` entry, this is the RFQ the offer was placed on.

**legs** `object[]`

Condition: `rfq` entries only.

The contracts you asked to trade.

**properties**

**symbol** `string`

Example: `OF_XBTUSD_261225_80000_C`

The symbol of the derivatives contract.

**size** `float`

The size of the leg.

**expiry** `string`

Condition: `rfq` entries only.\\

Format: RFC3339\\

Example: `2026-10-08T15:05:00.000000Z`

The time at which the RFQ expires.

**best\_bid** `float`

Condition: `rfq` entries, when at least one offer has a bid.

The total price of the best bid across all offers on your RFQ. If two offers have the same price, the one that was updated first is the best.

**best\_ask** `float`

Condition: `rfq` entries, when at least one offer has an ask.

The total price of the best ask across all offers on your RFQ. If two offers have the same price, the one that was updated first is the best.

**best\_bid\_legs** `object[]`

Condition: `rfq` entries, when the offer that set `best_bid` was priced per leg. Omitted for package offers, which have a total price only.

The per-leg prices of the offer that set `best_bid`.

**properties**

**symbol** `string`

The symbol of the derivatives contract.

**price** `float`

The price for this leg.

**best\_ask\_legs** `object[]`

Condition: `rfq` entries, when the offer that set `best_ask` was priced per leg. Omitted for package offers, which have a total price only.

The per-leg prices of the offer that set `best_ask`.

**properties**

**symbol** `string`

The symbol of the derivatives contract.

**price** `float`

The price for this leg.

**bid** `float`

Condition: `offer` entries, when your offer has a bid.

The total price of your bid. If you priced the bid per leg, the total is computed from your leg prices.

**ask** `float`

Condition: `offer` entries, when your offer has an ask.

The total price of your ask. If you priced the ask per leg, the total is computed from your leg prices.

**bid\_legs** `object[]`

Condition: `offer` entries, when your bid was priced per leg.

The per-leg prices of your bid.

**properties**

**symbol** `string`

The symbol of the derivatives contract.

**price** `float`

The price for this leg.

**ask\_legs** `object[]`

Condition: `offer` entries, when your ask was priced per leg.

The per-leg prices of your ask.

**properties**

**symbol** `string`

The symbol of the derivatives contract.

**price** `float`

The price for this leg.

**status** `string`

One of: `open`, `expired`, `cancelled`, `filled_bid_side`, `filled_ask_side`

The status of the entry. The values are the same as in REST.

On an `rfq` entry:

* `open`: the RFQ accepts offers.
* `expired` and `cancelled`: the RFQ closed without a trade.
* `filled_bid_side` and `filled_ask_side`: you accepted an offer on that side.

On an `offer` entry, the status is the RFQ's status, except that a withdrawn offer, or one cancelled at acceptance, is `cancelled` while the RFQ stays open. A `filled_*` status does not mean your offer was the one accepted.

**error** `string`

One of: `snapshot_too_large`\\

Condition: if the snapshot exceeded the maximum message size.

The snapshot could not be delivered, and `data` is empty. Resubscribe to request the snapshot again.

Fields that do not apply to an entry are omitted. For example, `best_ask` is omitted while no offer has an ask, and an offer's `bid` is omitted when it quoted only the ask side.

## Unsubscribe

> [tab] Request
>
> **method** `string` *required*
>
> Value: `unsubscribe`
>
> **params** `object` *required*
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `quotes`
>
> **asset\_class** `string` *required*
>
> One of: `derivatives`
>
> The asset class for the request. Must be included.
>
> **token** `string` *required*
>
> Authentication token. See [authentication guide](https://docs.kraken.com/exchange/guides/websockets/authentication.md) for details.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> **method** `string` *required*
>
> Value: `unsubscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `quotes`
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **time\_in** `string`
>
> The timestamp when the subscription was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

```json Subscribe Request theme={null}
{
    "method": "subscribe",
    "params": {
        "channel": "quotes",
        "asset_class": "derivatives",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "result": {
        "channel": "quotes",
        "asset_class": "derivatives",
        "snapshot": true
    },
    "success": true,
    "time_in": "2026-10-08T14:58:13.111530Z",
    "time_out": "2026-10-08T14:58:13.111775Z"
}
```

```json Snapshot theme={null}
{
    "channel": "quotes",
    "type": "snapshot",
    "data": [
        {
            "type": "rfq",
            "rfq_id": "3f9a6c1e-7b42-4d1a-9c55-2e8b0d4f6a13",
            "legs": [
                {
                    "symbol": "OF_XBTUSD_261225_80000_C",
                    "size": 5
                },
                {
                    "symbol": "OF_XBTUSD_261225_90000_C",
                    "size": 10
                }
            ],
            "expiry": "2026-10-08T15:05:00.000000Z",
            "status": "open",
            "best_bid": 4150.0,
            "best_ask": 4310.0,
            "best_bid_legs": [
                {
                    "symbol": "OF_XBTUSD_261225_80000_C",
                    "price": 2450.0
                },
                {
                    "symbol": "OF_XBTUSD_261225_90000_C",
                    "price": 1700.0
                }
            ]
        },
        {
            "type": "offer",
            "offer_id": "a81d2f40-5c3e-4b6f-8e19-7d0c2b9a4e55",
            "rfq_id": "c6e4b7a2-1f08-4d93-b3a5-90e1f7d26c84",
            "bid": 1180.0,
            "ask": 1240.0,
            "status": "open"
        }
    ]
}
```

```json RFQ Update theme={null}
{
    "channel": "quotes",
    "type": "update",
    "data": [
        {
            "type": "rfq",
            "rfq_id": "3f9a6c1e-7b42-4d1a-9c55-2e8b0d4f6a13",
            "legs": [
                {
                    "symbol": "OF_XBTUSD_261225_80000_C",
                    "size": 5
                },
                {
                    "symbol": "OF_XBTUSD_261225_90000_C",
                    "size": 10
                }
            ],
            "expiry": "2026-10-08T15:05:00.000000Z",
            "status": "filled_bid_side",
            "best_bid": 4150.0,
            "best_ask": 4310.0,
            "best_bid_legs": [
                {
                    "symbol": "OF_XBTUSD_261225_80000_C",
                    "price": 2450.0
                },
                {
                    "symbol": "OF_XBTUSD_261225_90000_C",
                    "price": 1700.0
                }
            ]
        }
    ]
}
```

```json Offer Withdrawn theme={null}
{
    "channel": "quotes",
    "type": "update",
    "data": [
        {
            "type": "offer",
            "offer_id": "a81d2f40-5c3e-4b6f-8e19-7d0c2b9a4e55",
            "rfq_id": "c6e4b7a2-1f08-4d93-b3a5-90e1f7d26c84",
            "bid": 1180.0,
            "ask": 1240.0,
            "status": "cancelled"
        }
    ]
}
```

```json Snapshot Too Large theme={null}
{
    "channel": "quotes",
    "type": "snapshot",
    "error": "snapshot_too_large",
    "data": []
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "quotes",
        "asset_class": "derivatives",
        "token": "G38a1tGFzqGiUCmnegBcm8d4nfP3tytiNQz6tkCBYXY"
    }
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "result": {
        "channel": "quotes"
    },
    "success": true,
    "time_in": "2026-10-08T15:10:13.111530Z",
    "time_out": "2026-10-08T15:10:13.111775Z"
}
```
