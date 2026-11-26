---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/wallet/private-estimate_withdrawal_fee
api_type: JSON-RPC
updated_at: 2026-11-26 19:02:06.472655
---

# private/coinbase/estimate_withdrawal_fee

> Estimates the network fee for a withdrawal on the given currency and network. **Available to institutional Coinbase wallet type accounts only.**

The `network_name` parameter is not validated against `coinbase_networks`; it is passed through to the custodian. The networks available for each currency are returned by `public/get_currencies` in the `coinbase_networks` field.

**📖 Related Article:** [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)

**Scope:** `wallet:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fcoinbase%2Festimate_withdrawal_fee)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/coinbase/estimate_withdrawal_fee
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
  /private/coinbase/estimate_withdrawal_fee:
    get:
      tags:
        - Wallet
        - Private
      description: >+
        Estimates the network fee for a withdrawal on the given currency and
        network. **Available to institutional Coinbase wallet type accounts
        only.**


        The `network_name` parameter is not validated against
        `coinbase_networks`; it is passed through to the custodian. The networks
        available for each currency are returned by `public/get_currencies` in
        the `coinbase_networks` field.


        **📖 Related Article:** [Managing
        Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)


        **Scope:** `wallet:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fcoinbase%2Festimate_withdrawal_fee)

      parameters:
        - name: currency
          in: query
          required: true
          schema:
            $ref: '#/components/schemas/currency'
            example: BTC
          description: The currency symbol (any portfolio currency)
        - name: network_name
          in: query
          schema:
            type: string
            example: networks/bitcoin-mainnet
          required: true
          description: >-
            Network resource name (e.g. `"networks/bitcoin-mainnet"`). Passed
            through to the custodian; not validated against `coinbase_networks`.
            Use a `resource_name` from `public/get_currencies`.
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 42
                  method: private/coinbase/estimate_withdrawal_fee
                  params:
                    currency: BTC
                    network_name: networks/bitcoin-mainnet
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/PrivateCoinbaseEstimateWithdrawalFeeResponse
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 42
                    result:
                      estimated_fee: '0.0005'
                      estimated_fee_before_subsidy: '0.001'
                      expires_at: '2026-04-06T12:00:00Z'
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/coinbase/estimate_withdrawal_fee \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 42,
              "method": "private/coinbase/estimate_withdrawal_fee",
              "params": {
                "currency": "BTC",
                "network_name": "networks/bitcoin-mainnet"
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
    PrivateCoinbaseEstimateWithdrawalFeeResponse:
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
            estimated_fee:
              type: string
              example: '0.0005'
              description: Estimated network fee for the withdrawal, in the given currency
            estimated_fee_before_subsidy:
              type: string
              example: '0.001'
              description: Estimated network fee before subsidy, in the given currency
            expires_at:
              type: string
              nullable: true
              example: '2026-04-06T12:00:00Z'
              description: >-
                Timestamp when the fee estimate expires (RFC 3339), `null` when
                not provided
          required:
            - estimated_fee
            - estimated_fee_before_subsidy
            - expires_at
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [Coinbase Wallet API](https://docs.deribit.com/articles/coinbase-wallet-api.md)
- [private/withdraw](https://docs.deribit.com/api-reference/wallet/private-withdraw.md)
- [private/set_coinbase_subaccount_withdrawals_allowed](https://docs.deribit.com/api-reference/wallet/private-set_coinbase_subaccount_withdrawals_allowed.md)
- [private/cancel_withdrawal](https://docs.deribit.com/api-reference/wallet/private-cancel_withdrawal.md)
- [private/get_withdrawals](https://docs.deribit.com/api-reference/wallet/private-get_withdrawals.md)