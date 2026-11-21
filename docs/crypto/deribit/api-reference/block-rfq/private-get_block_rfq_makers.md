---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/block-rfq/private-get_block_rfq_makers
api_type: JSON-RPC
updated_at: 2026-11-21 19:01:40.599134
---

# private/get_block_rfq_makers

> Returns a list of all available Block RFQ makers. This method takes no parameters.

Use this method to retrieve the list of makers that can be specified when creating a Block RFQ with [private/create_block_rfq](https://docs.deribit.com/api-reference/block-rfq/private-create_block_rfq).

**📖 Related Article:** [Deribit Block RFQ API walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough)

**Scope:** `block_rfq:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_block_rfq_makers)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_block_rfq_makers
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
  /private/get_block_rfq_makers:
    get:
      tags:
        - Block RFQ
        - Private
      description: >+
        Returns a list of all available Block RFQ makers. This method takes no
        parameters.


        Use this method to retrieve the list of makers that can be specified
        when creating a Block RFQ with
        [private/create_block_rfq](https://docs.deribit.com/api-reference/block-rfq/private-create_block_rfq).


        **📖 Related Article:** [Deribit Block RFQ API
        walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough)


        **Scope:** `block_rfq:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_block_rfq_makers)

      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 1
                  method: private/get_block_rfq_makers
                  params: {}
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateGetBlockRfqMakersResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 1
                    result:
                      - MAKER1
                      - MAKER2
                      - MAKER3
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_block_rfq_makers \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 1,
              "method": "private/get_block_rfq_makers",
              "params": {}
            }'
components:
  schemas:
    PrivateGetBlockRfqMakersResponse:
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
          description: A list of available makers.
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [private/get_block_rfqs](https://docs.deribit.com/api-reference/block-rfq/private-get_block_rfqs.md)
- [private/get_block_rfq_user_info](https://docs.deribit.com/api-reference/block-rfq/private-get_block_rfq_user_info.md)
- [private/get_block_rfq_quotes](https://docs.deribit.com/api-reference/block-rfq/private-get_block_rfq_quotes.md)
- [private/cancel_block_rfq](https://docs.deribit.com/api-reference/block-rfq/private-cancel_block_rfq.md)
- [private/add_block_rfq_quote](https://docs.deribit.com/api-reference/block-rfq/private-add_block_rfq_quote.md)