---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/wallet/private-submit_transfer_between_subaccounts
api_type: JSON-RPC
updated_at: 2026-11-28 18:58:47.615313
---

# private/submit_transfer_between_subaccounts

> Transfer funds between two subaccounts or between a subaccount and the main account.

**📖 Related Article:** [Managing Transfers](https://docs.deribit.com/articles/managing-transfers-api)

**Scope:** `wallets:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fsubmit_transfer_between_subaccounts)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/submit_transfer_between_subaccounts
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
  /private/submit_transfer_between_subaccounts:
    get:
      tags:
        - Wallet
        - Private
      description: >+
        Transfer funds between two subaccounts or between a subaccount and the
        main account.


        **📖 Related Article:** [Managing
        Transfers](https://docs.deribit.com/articles/managing-transfers-api)


        **Scope:** `wallets:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fsubmit_transfer_between_subaccounts)

      parameters:
        - name: currency
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/currency'
          description: >
            The currency symbol.


            **📖 Related Article:** [Using the currency
            Parameter](https://docs.deribit.com/articles/currency-parameter)
        - name: amount
          in: query
          schema:
            type: number
          required: true
          description: Amount of funds to be transferred
        - name: destination
          in: query
          schema:
            type: integer
            example: 1
          required: true
          description: >-
            Id of destination subaccount. Can be found in `My Account >>
            Subaccounts` tab
        - name: source
          in: query
          schema:
            type: integer
            example: 1
          required: false
          description: >-
            Source account id, defaulting to the caller. With main-account
            authorization, either the main account or one of its subaccounts may
            be the source; a subaccount caller can transfer only from itself to
            its main account.
        - in: query
          name: nonce
          required: false
          schema:
            $ref: '#/components/schemas/nonce'
          description: >-
            Optional idempotency nonce. If provided, subsequent requests with
            the same nonce will return the previously created transaction
            instead of creating a new one. Must be 8-128 characters. The nonce
            is persisted on the resulting transaction and returned in the
            response.
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 210
                  method: private/submit_transfer_between_subaccounts
                  params:
                    currency: ETH
                    amount: 12.1234
                    destination: 20
                    source: 10
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateSubmitTransferResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 210
                    result:
                      updated_timestamp: 1550226218504
                      type: subaccount
                      state: confirmed
                      other_side: MySubAccount
                      id: 1
                      direction: payment
                      currency: ETH
                      created_timestamp: 1550226218504
                      amount: 12.1234
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/submit_transfer_between_subaccounts \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 210,
              "method": "private/submit_transfer_between_subaccounts",
              "params": {
                "currency": "ETH",
                "amount": 12.1234,
                "destination": 20,
                "source": 10
              }
            }'
components:
  schemas:
    currency:
      enum:
        - BTC
        - ETH
        - USDC
        - USDT
        - EURR
      type: string
      description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`
    nonce:
      example: bF1_gfgcsd
      type: string
      description: Nonce
    PrivateSubmitTransferResponse:
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
          $ref: '#/components/schemas/transfer_item'
      required:
        - result
        - jsonrpc
      type: object
    transfer_item:
      properties:
        id:
          $ref: '#/components/schemas/transfer_id'
        created_timestamp:
          $ref: '#/components/schemas/timestamp'
        type:
          $ref: '#/components/schemas/transfer_type'
        currency:
          $ref: '#/components/schemas/currency'
        amount:
          $ref: '#/components/schemas/currency_amount'
        other_side:
          $ref: '#/components/schemas/transfer_other_side'
        state:
          $ref: '#/components/schemas/transfer_state'
        direction:
          $ref: '#/components/schemas/transfer_direction'
        updated_timestamp:
          $ref: '#/components/schemas/timestamp'
        source:
          type: integer
          description: Source account id; present for subaccount transfer submissions.
        note:
          type: string
          description: Transfer note (empty string if unset).
        nonce:
          type: string
          description: Optional idempotency nonce if provided in the request
      required:
        - currency
        - id
        - type
        - amount
        - state
        - other_side
        - updated_timestamp
        - created_timestamp
      type: object
    transfer_id:
      example: 12
      type: integer
      description: Id of transfer
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
    transfer_type:
      enum:
        - user
        - subaccount
      type: string
      description: >-
        Type of transfer: `user` - sent to user, `subaccount` - sent to
        subaccount
    currency_amount:
      example: 1
      type: number
      description: Amount of funds in given currency
    transfer_other_side:
      example: Smith
      type: string
      description: >-
        For transfer from/to subaccount returns this subaccount name, for
        transfer to other account returns address, for transfer from other
        account returns that accounts username.
    transfer_state:
      type: string
      description: >-
        Transfer state, allowed values : `prepared`, `confirmed`, `cancelled`,
        `waiting_for_admin`, `insufficient_funds`,  `withdrawal_limit` otherwise
        rejection reason
    transfer_direction:
      enum:
        - payment
        - income
      type: string
      description: Transfer direction

````

## Related topics

- [Managing Transfers](https://docs.deribit.com/articles/managing-transfers-api.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [private/submit_transfer_to_subaccount](https://docs.deribit.com/api-reference/wallet/private-submit_transfer_to_subaccount.md)
- [private/submit_transfer_to_user](https://docs.deribit.com/api-reference/wallet/private-submit_transfer_to_user.md)
- [private/get_transfers](https://docs.deribit.com/api-reference/wallet/private-get_transfers.md)