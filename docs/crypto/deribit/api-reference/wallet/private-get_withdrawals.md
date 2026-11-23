---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/wallet/private-get_withdrawals
api_type: JSON-RPC
updated_at: 2026-11-23 19:00:41.085989
---

# private/get_withdrawals

> Retrieve the latest user withdrawals. Returns a list of withdrawal requests with their status, amounts, addresses, and other relevant details.

**📖 Related Article:** [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)

**Scope:** `wallet:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_withdrawals)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_withdrawals
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
  /private/get_withdrawals:
    get:
      tags:
        - Wallet
        - Private
      description: >+
        Retrieve the latest user withdrawals. Returns a list of withdrawal
        requests with their status, amounts, addresses, and other relevant
        details.


        **📖 Related Article:** [Managing
        Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)


        **Scope:** `wallet:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_withdrawals)

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
        - name: count
          required: false
          in: query
          schema:
            type: integer
            maximum: 1000
            minimum: 1
          description: Number of requested items, default - `10`, maximum - `1000`
        - name: offset
          in: query
          required: false
          schema:
            example: 10
            type: integer
          description: The offset for pagination, default - `0`
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 2745
                  method: private/get_withdrawals
                  params:
                    currency: BTC
                    count: 10
                    offset: 0
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateGetWithdrawalsResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 2745
                    result:
                      count: 1
                      data:
                        - address: 2NBqqD5GRJ8wHy1PYyCXTe9ke5226FhavBz
                          amount: 0.5
                          confirmed_timestamp: null
                          created_timestamp: 1550571443070
                          currency: BTC
                          fee: 0.0001
                          id: 1
                          priority: 0.15
                          state: unconfirmed
                          transaction_id: null
                          updated_timestamp: 1550571443070
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_withdrawals \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 2745,
              "method": "private/get_withdrawals",
              "params": {
                "currency": "BTC",
                "count": 10,
                "offset": 0
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
    PrivateGetWithdrawalsResponse:
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
            data:
              type: array
              items:
                $ref: '#/components/schemas/withdrawal'
            count:
              $ref: '#/components/schemas/result_count'
          required:
            - data
            - count
      required:
        - result
        - jsonrpc
      type: object
    withdrawal:
      properties:
        address:
          $ref: '#/components/schemas/currency_address'
        amount:
          $ref: '#/components/schemas/currency_amount'
        confirmed_timestamp:
          type: integer
          example: 1536569522277
          nullable: true
          description: >-
            The timestamp (milliseconds since the Unix epoch) of withdrawal
            confirmation, `null` when not confirmed
        created_timestamp:
          $ref: '#/components/schemas/timestamp'
        currency:
          $ref: '#/components/schemas/currency'
        fee:
          $ref: '#/components/schemas/fee'
        id:
          type: integer
          example: 1
          description: Withdrawal id in Deribit system
        priority:
          type: number
          example: 1
          description: Id of priority level
        state:
          $ref: '#/components/schemas/withdrawal_state'
        transaction_id:
          $ref: '#/components/schemas/currency_transaction_id'
        updated_timestamp:
          $ref: '#/components/schemas/timestamp'
        nonce:
          type: string
          description: Optional idempotency nonce if provided in the request
        note:
          type: string
          description: Withdrawal note.
        completed:
          type: integer
          description: Number of completed withdrawals to this address.
        execution_timestamp:
          type: integer
          description: >-
            Execution timestamp in milliseconds since the Unix epoch; present
            only when set and state is confirmed.
        clearance_state:
          $ref: '#/components/schemas/clearance_state'
      required:
        - currency
        - address
        - amount
        - state
        - transaction_id
        - updated_timestamp
      type: object
    result_count:
      example: 101
      type: integer
      description: Total number of results available
    currency_address:
      example: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
      type: string
      description: Address in proper format for currency
    currency_amount:
      example: 1
      type: number
      description: Amount of funds in given currency
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
    fee:
      example: 0.000023
      type: number
      description: Fee in currency
    withdrawal_state:
      enum:
        - unconfirmed
        - confirmed
        - cancelled
        - completed
        - interrupted
        - rejected
      type: string
      description: >-
        Withdrawal state, allowed values : `unconfirmed`, `confirmed`,
        `cancelled`, `completed`, `interrupted`, `rejected`
    currency_transaction_id:
      nullable: true
      example: 1b1fb5568515e2b79503501e3d3680b2d0838d5dfc2d15a04eb8cd9fbbe0b572
      type: string
      description: >-
        Transaction id in proper format for currency, `null` if id is not
        available
    clearance_state:
      enum:
        - in_progress
        - pending_admin_decision
        - pending_user_input
        - success
        - failed
        - cancelled
        - refund_initiated
        - refunded
      type: string
      description: >-
        Clearance state indicating the current status of the transaction
        clearance process. Allowed values: <li><code>in_progress</code>:
        clearance process is in progress</li>
        <li><code>pending_admin_decision</code>: transaction is under manual
        review by Deribit admin</li> <li><code>pending_user_input</code>: user
        should provide additional information regarding the transaction</li>
        <li><code>success</code>: clearance process completed successfully</li>
        <li><code>failed</code>: clearance process failed, transaction is
        rejected</li> <li><code>cancelled</code>: transaction is cancelled
        (currently used only for withdrawals, meaning the withdrawal is
        cancelled)</li> <li><code>refund_initiated</code>: clearance process
        failed, transaction refund is initiated, funds are removed from Deribit
        balance (valid for deposits only)</li> <li><code>refunded</code>:
        clearance process failed, deposit amount is refunded back to the client
        (valid for deposits only)</li>

````

## Related topics

- [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api.md)
- [Coinbase Wallet API](https://docs.deribit.com/articles/coinbase-wallet-api.md)
- [Using the currency Parameter](https://docs.deribit.com/articles/currency-parameter.md)
- [private/get_address_book](https://docs.deribit.com/api-reference/wallet/private-get_address_book.md)
- [private/get_address_beneficiary](https://docs.deribit.com/api-reference/wallet/private-get_address_beneficiary.md)