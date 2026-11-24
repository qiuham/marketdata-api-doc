---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/subscription-management/public-subscribe
api_type: JSON-RPC
updated_at: 2026-11-24 18:59:53.120620
---

# public/subscribe

> Subscribe to one or more channels. This is the same method as `/private/subscribe`, but it can only be used for 'public' channels.

For a complete list of available subscription channels and their notification formats, see [Notifications and Subscriptions](https://docs.deribit.com/articles/notifications).

**Note - This method has distinct API rate limiting requirements:** Sustained rate: ~3.3 requests/second. For more information, see [Rate Limits](https://docs.deribit.com/articles/rate-limits).

**📖 Related Articles:** 
- [Market Data Collection Best Practices](https://docs.deribit.com/articles/market-data-collection-best-practices)
- [Options Data Collection Best Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fsubscribe)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/subscribe
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
  /public/subscribe:
    get:
      tags:
        - Subscription Management
        - Public
        - WebSocket Only
      description: >+
        Subscribe to one or more channels. This is the same method as
        `/private/subscribe`, but it can only be used for 'public' channels.


        For a complete list of available subscription channels and their
        notification formats, see [Notifications and
        Subscriptions](https://docs.deribit.com/articles/notifications).


        **Note - This method has distinct API rate limiting requirements:**
        Sustained rate: ~3.3 requests/second. For more information, see [Rate
        Limits](https://docs.deribit.com/articles/rate-limits).


        **📖 Related Articles:** 

        - [Market Data Collection Best
        Practices](https://docs.deribit.com/articles/market-data-collection-best-practices)

        - [Options Data Collection Best
        Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fsubscribe)

      parameters:
        - name: channels
          in: query
          schema:
            type: array
            items:
              type: string
              example: deribit_price_index.btc_usd
            example:
              - deribit_price_index.btc_usd
          required: true
          description: >-
            A list of channels to subscribe to. See [Notifications and
            Subscriptions](https://docs.deribit.com/articles/notifications) for
            all available channels.
          style: form
          explode: true
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 3600
                  method: public/subscribe
                  params:
                    channels:
                      - deribit_price_index.btc_usd
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateSubscribeResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 3600
                    result:
                      - deribit_price_index.btc_usd
          description: Success response
        '401':
          $ref: '#/components/responses/ErrorMessageResponse'
      x-codeSamples:
        - lang: json
          label: WebSocket
          source: |-
            {
              "jsonrpc": "2.0",
              "id": 3600,
              "method": "public/subscribe",
              "params": {
                "channels": [
                  "deribit_price_index.btc_usd"
                ]
              }
            }
components:
  schemas:
    PrivateSubscribeResponse:
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
          type: array
          items:
            type: string
            example: deribit_price_index.btc_usd
          description: A list of subscribed channels.
      required:
        - result
        - jsonrpc
      type: object
    ErrorMessageResponse:
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
            data:
              description: Optional error details.
          required:
            - code
            - message
      required:
        - error
        - jsonrpc
      type: object
  responses:
    ErrorMessageResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorMessageResponse'
      description: Success response

````

## Related topics

- [Market Data Collection](https://docs.deribit.com/articles/market-data-collection-best-practices.md)
- [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues.md)
- [Notifications](https://docs.deribit.com/articles/notifications.md)
- [Quickstart Guide](https://docs.deribit.com/articles/deribit-quickstart.md)
- [Rate Limits](https://docs.deribit.com/articles/rate-limits.md)