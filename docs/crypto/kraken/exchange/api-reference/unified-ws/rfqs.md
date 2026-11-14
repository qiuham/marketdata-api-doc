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
source_url: 'https://docs.kraken.com/exchange/api-reference/unified-ws/rfqs'
updated_at: 2026-11-13
---

# RFQs

> Subscribe to all open requests for quotes on options

UWS
uws.kraken.com/v2/public
rfqs

The `rfqs` channel streams every open request for quote (RFQ) on options. Each RFQ lists the legs the requester wants to trade, when the RFQ expires and its status.

The channel carries user RFQs only.

The channel is public. It does not show who made a request, and it does not show offers. To follow your own RFQs and the offers you have placed, subscribe to the private [`quotes`](https://docs.kraken.com/exchange/api-reference/unified-ws/quotes) channel.

The channel does not carry mark prices. To get them, subscribe to the [`ticker`](https://docs.kraken.com/exchange/api-reference/unified-ws/ticker) channel.

> [!NOTE]
>
> Messages on this channel carry no sequence numbers. To recover after a gap, resubscribe with `snapshot` set to `true`.

The `asset_class` parameter is required on every `subscribe` and `unsubscribe` request for the `rfqs` channel. Requests that omit it are not accepted.

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
> Value: `rfqs`
>
> **asset\_class** `string` *required*
>
> One of: `derivatives`
>
> The asset class for the request. Must be included.
>
> **snapshot** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `true`
>
> Request a snapshot of all open RFQs after subscribing.
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
> Value: `rfqs`
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

The snapshot and update messages share the same schema. The snapshot lists every open RFQ. After that, an update is sent each time an RFQ opens or changes status.

When an RFQ closes, you receive one last update with its final status: `expired`, `cancelled`, `filled_bid_side` or `filled_ask_side`. After that, the RFQ is no longer sent, and the channel keeps no history of closed RFQs.

If the closing message is lost, the RFQ is closed with status `expired` 10 seconds after its `expiry`. A snapshot never includes an RFQ that is past its `expiry`.

You may receive another `snapshot` after the first one if you subscribed with `snapshot` set to `true`. This happens when the feed recovers from a connection loss or the trading engine restarts. When you receive one, replace your list of RFQs with its contents. After an engine restart, every open RFQ first receives an update with status `cancelled`, then you receive an empty snapshot.

**channel** `string`

Value: `rfqs`

**type** `string`

One of: `snapshot`, `update`

**data** `object[]`

A list of RFQs.

**properties**

**rfq\_id** `string`

Format: UUID

The unique identifier of the RFQ.

**legs** `object[]`

The contracts the requester wants to trade.

**properties**

**symbol** `string`

Example: `OF_XBTUSD_261225_80000_C`

The symbol of the derivatives contract.

**size** `float`

The size of the leg.

**expiry** `string`

Format: RFC3339\\

Example: `2026-10-08T15:05:00.000000Z`

The time at which the RFQ expires.

**status** `string`

One of: `open`, `expired`, `cancelled`, `filled_bid_side`, `filled_ask_side`

The status of the RFQ. The values are the same as in REST:

* `open`: the RFQ accepts offers.
* `expired` and `cancelled`: the RFQ closed without a trade.
* `filled_bid_side` and `filled_ask_side`: the requester accepted an offer on that side.

**error** `string`

One of: `snapshot_too_large`\\

Condition: if the snapshot exceeded the maximum message size.

The snapshot could not be delivered, and `data` is empty. Resubscribe to request the snapshot again.

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
> Value: `rfqs`
>
> **asset\_class** `string` *required*
>
> One of: `derivatives`
>
> The asset class for the request. Must be included.
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
> Value: `rfqs`
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
        "channel": "rfqs",
        "asset_class": "derivatives"
    }
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "result": {
        "channel": "rfqs",
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
    "channel": "rfqs",
    "type": "snapshot",
    "data": [
        {
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
            "status": "open"
        }
    ]
}
```

```json Update theme={null}
{
    "channel": "rfqs",
    "type": "update",
    "data": [
        {
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
            "status": "filled_bid_side"
        }
    ]
}
```

```json Snapshot Too Large theme={null}
{
    "channel": "rfqs",
    "type": "snapshot",
    "error": "snapshot_too_large",
    "data": []
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "rfqs",
        "asset_class": "derivatives"
    }
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "result": {
        "channel": "rfqs"
    },
    "success": true,
    "time_in": "2026-10-08T15:10:13.111530Z",
    "time_out": "2026-10-08T15:10:13.111775Z"
}
```
