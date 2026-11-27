---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/wallet/private-withdraw
api_type: JSON-RPC
updated_at: 2026-11-27 19:01:01.518313
---

# private/withdraw

> Creates a new withdrawal request. This method allows you to withdraw funds from your account to an external address. The withdrawal can be configured with priority settings and must use an address from your address book.

**Withdrawal Checks & Balance Updates**

Withdrawal funds are checked twice: when a user requests a withdrawal and again when they confirm it via the email link. If available funds decrease between these steps, the withdrawal may be rejected.

A withdrawal may also be rejected if the on-chain fee increases between the request and confirmation.

The withdrawal amount is deducted only after all checks pass and the transaction is scheduled. The web-interface Withdrawal tab displays all withdrawals regardless of their status (pending, cancelled, rejected, or completed).

**Coinbase wallet type**

For Coinbase wallet type accounts the method supports network selection and CTN (Coinbase Transfer Network) counterparties, and behaves differently:

- Required parameters are `currency` (any portfolio currency) and `amount`, plus one of `address` or `id` (the address book entry identifier returned by `private/get_address_book`).
- When `address` is an on-chain address, pass `network` (and `tag` when applicable) to identify the address book entry. For a CTN withdrawal, pass the CTN counterparty identifier of the entry as `address`.
- `priority` and `nonce` are not supported. Use `private/coinbase/estimate_withdrawal_fee` to estimate the network fee.
- Subaccounts can withdraw only when enabled by the main account via `private/set_coinbase_subaccount_withdrawals_allowed`.
- The response is a Coinbase withdrawal object instead of the legacy withdrawal object. Its `state` is one of `prepared`, `awaiting_second_email`, `unconfirmed`, `completed` or `cancelled`; withdrawals to an address that is not trusted start as `prepared` and require email confirmation, in which case `transfer_idem` is absent until the withdrawal is submitted to the custodian. Fields that are not set are omitted from the response.

**📖 Related Article:** [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)

**Scope:** `wallet:read_write` and mainaccount

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fwithdraw)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/withdraw
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
  /private/withdraw:
    get:
      tags:
        - Wallet
        - Private
      description: >+
        Creates a new withdrawal request. This method allows you to withdraw
        funds from your account to an external address. The withdrawal can be
        configured with priority settings and must use an address from your
        address book.


        **Withdrawal Checks & Balance Updates**


        Withdrawal funds are checked twice: when a user requests a withdrawal
        and again when they confirm it via the email link. If available funds
        decrease between these steps, the withdrawal may be rejected.


        A withdrawal may also be rejected if the on-chain fee increases between
        the request and confirmation.


        The withdrawal amount is deducted only after all checks pass and the
        transaction is scheduled. The web-interface Withdrawal tab displays all
        withdrawals regardless of their status (pending, cancelled, rejected, or
        completed).


        **Coinbase wallet type**


        For Coinbase wallet type accounts the method supports network selection
        and CTN (Coinbase Transfer Network) counterparties, and behaves
        differently:


        - Required parameters are `currency` (any portfolio currency) and
        `amount`, plus one of `address` or `id` (the address book entry
        identifier returned by `private/get_address_book`).

        - When `address` is an on-chain address, pass `network` (and `tag` when
        applicable) to identify the address book entry. For a CTN withdrawal,
        pass the CTN counterparty identifier of the entry as `address`.

        - `priority` and `nonce` are not supported. Use
        `private/coinbase/estimate_withdrawal_fee` to estimate the network fee.

        - Subaccounts can withdraw only when enabled by the main account via
        `private/set_coinbase_subaccount_withdrawals_allowed`.

        - The response is a Coinbase withdrawal object instead of the legacy
        withdrawal object. Its `state` is one of `prepared`,
        `awaiting_second_email`, `unconfirmed`, `completed` or `cancelled`;
        withdrawals to an address that is not trusted start as `prepared` and
        require email confirmation, in which case `transfer_idem` is absent
        until the withdrawal is submitted to the custodian. Fields that are not
        set are omitted from the response.


        **📖 Related Article:** [Managing
        Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)


        **Scope:** `wallet:read_write` and mainaccount


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fwithdraw)

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
        - name: address
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/currency_address'
            example: 2NBqqD5GRJ8wHy1PYyCXTe9ke5226FhavBz
          description: >-
            Address in currency format, it must be in address book. **Required
            for legacy wallet type.** **Coinbase wallet type:** required when
            `id` is not provided — the on-chain address (use `network` and `tag`
            to disambiguate entries sharing the same address) or the CTN
            counterparty identifier of an existing address book entry.
        - name: amount
          in: query
          schema:
            type: number
          required: true
          description: Amount of funds to be withdrawn
        - name: network
          in: query
          schema:
            type: string
            example: networks/ethereum-mainnet
          required: false
          description: >-
            Blockchain network resource name (e.g. networks/ethereum-mainnet),
            for Coinbase wallet types. Available networks are returned by
            public/get_currencies in coinbase_networks. Requiredness depends on
            the operation. When resolving an existing address-book entry, it is
            optional if the entry resolves uniquely; it disambiguates an address
            present on multiple networks.
        - name: tag
          in: query
          schema:
            type: string
          required: false
          description: >-
            Destination tag / memo for networks that support one. **Coinbase
            wallet type only.** Used together with `address` and `network`; also
            serves to disambiguate address book entries that share the same
            address.
        - name: id
          in: query
          schema:
            type: string
            example: 0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b
          required: false
          description: >-
            Unique identifier (UUID7) of the address book entry, as returned in
            the `id` field of `private/get_address_book` results. **Coinbase
            wallet type only.** Can be used instead of `address` (with `network`
            and `tag`) to identify the entry.
        - name: priority
          in: query
          schema:
            type: string
            enum:
              - insane
              - extreme_high
              - very_high
              - high
              - normal
              - mid
              - low
              - very_low
          required: false
          description: >-
            Withdrawal priority, default: `high`. Note: fee priority levels are
            only configured for BTC; other currencies default to standard ratio
            1.0.
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
                  id: 6931
                  method: private/withdraw
                  params:
                    currency: BTC
                    address: 2NBqqD5GRJ8wHy1PYyCXTe9ke5226FhavBz
                    amount: 0.4
                    priority: mid
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateWithdrawResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 6931
                    result:
                      address: 2NBqqD5GRJ8wHy1PYyCXTe9ke5226FhavBz
                      amount: 0.4
                      confirmed_timestamp: null
                      created_timestamp: 1550574558607
                      currency: BTC
                      fee: 0.0001
                      id: 4
                      priority: 1
                      state: unconfirmed
                      transaction_id: null
                      updated_timestamp: 1550574558607
                coinbaseResponse:
                  summary: Coinbase response example
                  value:
                    jsonrpc: '2.0'
                    id: 6931
                    result:
                      id: 0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b
                      transfer_idem: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d
                      currency: ETH
                      state: unconfirmed
                      amount: 0.5
                      address: '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'
                      network: networks/ethereum-mainnet
                      network_display_name: Ethereum
                      created_timestamp: 1719993033041
                      updated_timestamp: 1719993033041
                      note: ''
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/withdraw \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 6931,
              "method": "private/withdraw",
              "params": {
                "currency": "BTC",
                "address": "2NBqqD5GRJ8wHy1PYyCXTe9ke5226FhavBz",
                "amount": 0.4,
                "priority": "mid"
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
    currency_address:
      example: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
      type: string
      description: Address in proper format for currency
    nonce:
      example: bF1_gfgcsd
      type: string
      description: Nonce
    PrivateWithdrawResponse:
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
          oneOf:
            - $ref: '#/components/schemas/withdrawal'
            - $ref: '#/components/schemas/coinbase_withdrawal_result'
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
    coinbase_withdrawal_result:
      properties:
        id:
          type: string
          example: 0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b
          description: Unique identifier (UUID7) of the withdrawal
        transfer_idem:
          type: string
          example: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d
          description: >-
            Idempotency identifier of the transfer at the custodian. Absent
            until the withdrawal has been submitted to the custodian — for
            example while the withdrawal is still `prepared` and awaiting email
            confirmation.
        currency:
          $ref: '#/components/schemas/currency'
        state:
          type: string
          enum:
            - prepared
            - awaiting_second_email
            - unconfirmed
            - completed
            - cancelled
          description: State of the withdrawal
        amount:
          type: number
          example: 0.5
          description: Amount of the withdrawal, in the given currency
        address:
          type: string
          example: '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'
          description: >-
            Destination of the withdrawal: the on-chain address, or the CTN
            counterparty identifier for a CTN withdrawal
        transaction_id:
          type: string
          description: >-
            Hash of the on-chain transaction. Absent until the transaction has
            been broadcast.
        network:
          type: string
          example: networks/ethereum-mainnet
          description: >-
            Network resource name of the destination (e.g.
            `"networks/ethereum-mainnet"`); absent for CTN withdrawals
        network_display_name:
          type: string
          example: Ethereum
          description: >-
            Human-readable name of the network (e.g. `"Ethereum"`); absent for
            CTN withdrawals
        destination_tag:
          type: string
          description: Destination tag / memo of the withdrawal; absent when not set
        payment_id:
          type: string
          description: Payment identifier assigned by the custodian; absent when not set
        source_ctn_id:
          type: string
          description: >-
            CTN counterparty identifier of the source; present for CTN
            withdrawals
        destination_ctn_id:
          type: string
          description: >-
            CTN counterparty identifier of the destination; present for CTN
            withdrawals
        created_timestamp:
          $ref: '#/components/schemas/timestamp'
        updated_timestamp:
          $ref: '#/components/schemas/timestamp'
        confirmed_timestamp:
          $ref: '#/components/schemas/timestamp'
        clearance_state:
          type: string
          example: success
          description: >-
            Compliance clearance state of the withdrawal; absent while no
            clearance decision has been recorded
        note:
          type: string
          description: Note attached to the withdrawal; empty string when not set
      required:
        - id
        - currency
        - state
        - amount
        - created_timestamp
        - updated_timestamp
        - note
      type: object
      description: >-
        Result of a withdrawal for a Coinbase wallet type account. Returned
        instead of `withdrawal` for Coinbase wallet type users. Fields that are
        not set are omitted from the response.
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

- [private/set_coinbase_subaccount_withdrawals_allowed](https://docs.deribit.com/api-reference/wallet/private-set_coinbase_subaccount_withdrawals_allowed.md)
- [Coinbase Wallet API](https://docs.deribit.com/articles/coinbase-wallet-api.md)
- [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [private/get_withdrawals](https://docs.deribit.com/api-reference/wallet/private-get_withdrawals.md)