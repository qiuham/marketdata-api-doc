---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/supporting/public-status
api_type: JSON-RPC
updated_at: 2026-11-27 19:00:58.873741
---

# public/status

> Method used to get information about locked currencies

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fstatus)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/status
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
  /public/status:
    get:
      tags:
        - Supporting
        - Public
      description: >+
        Method used to get information about locked currencies


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fstatus)

      parameters: []
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 55
                  method: public/status
                  params: {}
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicStatusResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 55
                    result:
                      locked_currencies:
                        - BTC
                        - ETH
                      locked: true
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/status \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 55,
              "method": "public/status",
              "params": {}
            }'
components:
  schemas:
    PublicStatusResponse:
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
          type: object
          properties:
            locked:
              type: string
              description: >-
                `true` when platform is locked in all currencies, `partial` when
                some currencies are locked, `false` - when there are not
                currencies locked
            locked_indices:
              type: array
              items:
                type: string
              description: List of currency indices locked platform-wise
          required:
            - locked
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [public/get_tradingview_chart_data](https://docs.deribit.com/api-reference/market-data/public-get_tradingview_chart_data.md)
- [public/auth](https://docs.deribit.com/api-reference/authentication/public-auth.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [public/subscribe](https://docs.deribit.com/api-reference/subscription-management/public-subscribe.md)
- [public/unsubscribe](https://docs.deribit.com/api-reference/subscription-management/public-unsubscribe.md)