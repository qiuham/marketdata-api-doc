---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/trading/private-cancel_all_by_instrument
api_type: JSON-RPC
updated_at: 2026-11-27 19:00:59.189223
---

# private/cancel_all_by_instrument

> Cancels all open orders for a specific instrument. This is useful for quickly clearing all orders for a single instrument.

Orders can be optionally filtered by order type (limit, market, stop, etc.). Use the `detailed` parameter to receive a list of all cancelled orders. The `include_combos` parameter can be used to include combo orders in the cancellation.

**Scope:** `trade:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fcancel_all_by_instrument)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/cancel_all_by_instrument
openapi: 3.0.0
info:
  title: Deribit API
  version: 2.1.1
servers:
  - url: https://test.deribit.com/api/v2
security: []
tags:
  - name: WebSocket Only
    description: Can only be used over websockets.
  - name: Public
    description: Public methods can be used without authentication.
  - name: Private
    description: >-
      <p>Private methods require authentication. All requests must include a
      valid OAuth2 token.</p>

      <p>A token can be requested using the <a
      href="#public-auth">/public/auth</a> method.</p>

      <p>When using the websockets protocol, the token must be included as a
      parameter <code>access_token</code> in the message. When using REST (HTTP
      GET), the token may also be passed in the <code>Authorization</code>
      header.</p>
  - name: Authentication
  - name: Session Management
  - name: Subscription Management
    description: >-
      Subscription works as [notifications](#notifications), so users will
      automatically (after subscribing) receive messages from the server.
      Overview for each channel response format is described in
      [subscriptions](#subscriptions) section.
  - name: Account Management
  - name: Trading
  - name: Market Data
  - name: Wallet
  - name: Chat
  - name: lsp
    description: >-
      Methods and notifications for the Liquidity Support Program (LSP), the
      mechanism that assigns risk from liquidated positions to designated LSP
      participant subaccounts before falling back to auto-deleveraging (ADL).
paths:
  /private/cancel_all_by_instrument:
    get:
      tags:
        - Trading
        - Matching Engine
        - Private
      description: >+
        Cancels all open orders for a specific instrument. This is useful for
        quickly clearing all orders for a single instrument.


        Orders can be optionally filtered by order type (limit, market, stop,
        etc.). Use the `detailed` parameter to receive a list of all cancelled
        orders. The `include_combos` parameter can be used to include combo
        orders in the cancellation.


        **Scope:** `trade:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fcancel_all_by_instrument)

      parameters:
        - name: instrument_name
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/instrument_name'
          description: Instrument name
        - name: type
          required: false
          in: query
          schema:
            $ref: '#/components/schemas/simple_order_type'
          description: >-
            Order type - `limit`, `stop`, `take`, `trigger_all` or `all`,
            default - `all`
        - name: detailed
          required: false
          in: query
          schema:
            type: boolean
          description: >
            When `detailed` is set to `true`, the output format is changed to
            include a list of all cancelled orders.


            **📖 Related Article:** [Detailed Response for Cancel
            Methods](https://docs.deribit.com/articles/json-rpc-overview#detailed-response-for-cancel-methods)


            Default: `false`
        - name: include_combos
          required: false
          in: query
          schema:
            type: boolean
          description: >-
            When set to `true` orders in combo instruments affecting a given
            position will also be cancelled. Default: `false`
        - name: freeze_quotes
          required: false
          in: query
          schema:
            type: boolean
          description: >-
            Whether or not to reject incoming quotes for 1 second after
            cancelling (`false` by default). Related to `private/mass_quote`
            request.
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 4122
                  method: private/cancel_all_by_instrument
                  params:
                    instrument_name: ETH-22FEB19-120-P
                    type: all
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateCancelAllResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 4122
                    result: 7
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/cancel_all_by_instrument \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 4122,
              "method": "private/cancel_all_by_instrument",
              "params": {
                "instrument_name": "ETH-22FEB19-120-P",
                "type": "all"
              }
            }'
components:
  schemas:
    instrument_name:
      example: BTC-PERPETUAL
      type: string
      description: Unique instrument identifier
    simple_order_type:
      enum:
        - all
        - limit
        - trigger_all
        - stop
        - take
        - trailing_stop
      type: string
      description: >-
        Order type filter: `all`, `limit`, `trigger_all`, `stop`, `take`, or
        `trailing_stop`.
    PrivateCancelAllResponse:
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        result:
          type: number
          example: 7
          description: Total number of successfully cancelled orders
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [Rate Limits](https://docs.deribit.com/articles/rate-limits.md)
- [JSON-RPC 2.0 Protocol](https://docs.deribit.com/articles/json-rpc-overview.md)
- [Order Management](https://docs.deribit.com/articles/order-management-best-practices.md)
- [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)