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
source_url: 'https://docs.kraken.com/institutional/api-reference/prime-websocket/ping'
updated_at: 2026-11-13
---

# Ping

> Optional client-initiated ping to verify connectivity; server responds with a Pong message.

> [!NOTE]
>
> Public channel. Connect to: `wss://wss.prime.kraken.com/ws/v1`

Pings may be optionally initiated by the client. They are not required to keep the session alive. On a valid request, the server responds with a `Pong` message. If `data` is omitted or empty, the server responds with an `error` message instead.

## Request

> [tab] Request Schema
>
> **reqid** `number` *required*
>
> A unique number that identifies this ping request.
>
> **type** `string` *required*
>
> Request type. Value: `Ping`
>
> **ts** `string` *required*
>
> An ISO-8601 UTC string of the form `2019-02-13T05:17:32.000000Z`.
>
> **data** `array` *required*
>
> Non-empty list of objects that is forwarded in the `Pong` response. Must contain at least one object; an empty array is rejected.

> [tab] Example
>
> ```json theme={null}
> {
>   "reqid": 2,
>   "type": "Ping",
>   "ts": "2024-01-13T05:17:32.000000Z",
>   "data": [
>     {}
>   ]
> }
> ```

## Response

> [tab] Pong Schema
>
> **reqid** `number` *required*
>
> The request ID from the ping request.
>
> **type** `string` *required*
>
> Response type. Value: `Pong`
>
> **seqNum** `number`
>
> Sequence number, always 0 for ping/pong when present. This field may be omitted from the response.
>
> **ts** `string` *required*
>
> An ISO-8601 UTC string of the form `2019-02-13T05:17:32.000000Z`.
>
> **data** `array` *required*
>
> Objects forwarded from the ping request `data` array.

> [tab] Pong Example
>
> ```json theme={null}
> {
>   "reqid": 2,
>   "type": "Pong",
>   "ts": "2024-01-13T05:17:32.002500Z",
>   "data": [
>     {}
>   ]
> }
> ```

> [tab] Error Schema
>
> Returned when `data` is omitted or empty.
>
> **reqid** `number` *required*
>
> The request ID from the ping request.
>
> **type** `string` *required*
>
> Response type. Value: `error`
>
> **seq** `number` *required*
>
> Sequence number for the error response. Error responses use `seq`, not `seqNum`.
>
> **ts** `string` *required*
>
> An ISO-8601 UTC string of the form `2019-02-13T05:17:32.000000Z`.
>
> **error** `object` *required*
>
> Error details.
>
> **properties**
>
> **code** `number` *required*
>
> Error code.
>
> **msg** `string` *required*
>
> Human-readable error message.

> [tab] Error Example
>
> If `data` is omitted:
>
> ```json theme={null}
> {
>   "reqid": 2,
>   "type": "Ping",
>   "ts": "2024-01-13T05:17:32.000000Z"
> }
> ```
>
> The server responds with:
>
> ```json theme={null}
> {
>   "reqid": 2,
>   "type": "error",
>   "seq": 1,
>   "ts": "2024-01-13T05:17:32.002500Z",
>   "error": {
>     "code": 1,
>     "msg": "missing Ping data"
>   }
> }
> ```
>
> If `data` is an empty array, the same error is returned.

## Notes

* `data` is required and must contain at least one object. Requests that omit `data`, or send `"data": []`, are rejected with `"missing Ping data"`.
* Any objects included in `data` are echoed back unchanged in the `Pong` response.
* `seqNum` may be omitted from successful `Pong` responses.
* Error responses use `seq` (not `seqNum`) and include an `error` object with `code` and `msg` fields.
