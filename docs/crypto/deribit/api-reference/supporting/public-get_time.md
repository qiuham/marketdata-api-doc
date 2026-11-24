---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/supporting/public-get_time
api_type: JSON-RPC
updated_at: 2026-11-24 18:59:53.250256
---

# public/get_time

> Retrieves the current time (in milliseconds). This API endpoint can be used to check the clock skew between your software and Deribit's systems.

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_time)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/get_time
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
  /public/get_time:
    get:
      tags:
        - Supporting
        - Public
      description: >+
        Retrieves the current time (in milliseconds). This API endpoint can be
        used to check the clock skew between your software and Deribit's
        systems.


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_time)

      parameters: []
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 7365
                  method: public/get_time
                  params: {}
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicGetTimeResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 7365
                    result: 1550147385946
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/get_time \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 7365,
              "method": "public/get_time",
              "params": {}
            }'
components:
  schemas:
    PublicGetTimeResponse:
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
          type: integer
          example: 1517329113791
          description: Current timestamp (milliseconds since the UNIX epoch)
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [public/get_announcements](https://docs.deribit.com/api-reference/account-management/public-get_announcements.md)
- [public/get_combos](https://docs.deribit.com/api-reference/combo-books/public-get_combos.md)
- [public/get_last_trades_by_instrument_and_time](https://docs.deribit.com/api-reference/market-data/public-get_last_trades_by_instrument_and_time.md)
- [public/get_last_trades_by_currency_and_time](https://docs.deribit.com/api-reference/market-data/public-get_last_trades_by_currency_and_time.md)
- [public/get_delivery_prices](https://docs.deribit.com/api-reference/market-data/public-get_delivery_prices.md)