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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/cancel'
updated_at: 2026-11-13
---

# Cancel Stream

> Cancel an existing stream by request ID. The stream stops sending data; no response unless there is an error.

> [!NOTE]
>
> Public channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Cancels an existing stream by request ID. No response is sent unless there is an error — the stream associated with the specified `reqid` simply stops sending data.

If there is an error (for example, the `reqid` does not exist or the stream is already cancelled), an error response may be sent with details about the failure.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> Request ID to cancel. Must match an existing subscription request ID from a [Subscribe](https://docs.kraken.com/institutional/api-reference/prime-websocket/subscribe.md) request.
>
> **type** `string` *required*
>
> Request type for cancelling the subscription. Value: `cancel`

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 1,
>   "type": "cancel"
> }
> ```

## Response

No response is sent unless there is an error. The stream associated with the specified `reqid` will stop sending data.
