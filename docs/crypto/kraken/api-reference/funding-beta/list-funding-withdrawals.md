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
source_url: 'https://docs.kraken.com/api-reference/funding-beta/list-funding-withdrawals'
updated_at: 2026-11-13
---

# List Funding Withdrawals

> Retrieve information about withdrawals. Results are sorted by recency; use the `cursor` parameter to iterate through the list of withdrawals (page size equal to the value of `limit`) from newest to oldest.

**API Key Permissions Required:** `Funds permissions - Query`



## OpenAPI

````yaml /openapi/spot-rest.yaml get /funding/v1/withdrawals
openapi: 3.0.0
info:
  title: REST API
  version: 1.1.0
  description: ''
servers:
  - url: https://api.kraken.com/0
    description: Production Server
security:
  - API-Key: []
    API-Sign: []
tags:
  - name: Market Data
  - name: Account Data
  - name: Trading
  - name: Algo Trading
    description: >
      Algo Trading endpoints create and manage **strategies**: parent
      instructions that Kraken executes on your behalf as a series of regular
      child orders.


      The only strategy available today is **TWAP** (time-weighted average
      price). A TWAP buys or sells a total `volume` evenly between `starttm` and
      `expiretm`. How child orders are sized, timed and placed is managed by
      Kraken and may change as execution improves.


      An algo runs as a strategy. In Kraken Pro, TWAP strategies show under
      Bots.


      ### Strategy lifecycle


      `pending` → `open` → `closed` | `expired` | `cancelled`


      - `pending`: accepted, waiting for `starttm`.

      - `open`: running, child orders are being placed.

      - `closed`: the full `volume` was filled before `expiretm`.

      - `expired`: `expiretm` was reached before the full `volume` was filled.

      - `cancelled`: cancelled with `CancelStrategy`.


      TWAP child orders are immediate-or-cancel limit orders and do not rest on
      the book. Completed child orders appear in `ClosedOrders`, and fills
      appear in trade history. Use the strategy endpoints to monitor overall
      progress.
  - name: funding-beta
    x-group: Funding (Beta)
    x-displayName: Funding (Beta)
  - name: Funding
    x-group: Funding (Legacy)
    x-displayName: Funding (Legacy)
  - name: Subaccounts
    description: >-
      Subaccounts are currently only available to institutional clients. Please
      contact your Account Manager for more details.
  - name: Earn
    description: >
      The earn API allows interacting with all of Kraken's yield generating
      products. It replaces the old `/staking` part of the API.


      The different available earn products are represented by earn strategies.
      This corresponds to the legacy `Staking/Assets`. `Stake`/`Unstake` are
      replaced by `Allocate`/`Deallocate`.


      ### Overview of the available endpoints under `/Earn`:


      - `Strategies` - list all earn strategies for which you are eligible or
      have a balance.

      - `Allocations` - lists the balance in your earn account for each
      strategy. Requires the `Query Funds` API key permission.

      - `Allocate`/`Deallocate` - allocate/deallocate to an earn strategy
      through an async operation. Requires the `Earn Funds` API key permission.

      - `AllocateStatus`/`DeallocateStatus` - verifies the state of the last
      allocation/deallocation. Requires the `Earn Funds` or `Query Funds` API
      key permission.


      ### Example usage:


      ### Determine which funds are earning rewards:


      1. Call `Strategies` to obtain information about the relevant strategy.
      The `lock_type` field shows whether bonding/unbonding funds are earning
      yield. The relevant fields are `bonding_rewards`/`unbonding_rewards`.

      2. Call `Allocations` for the relevant strategy. From the previous step,
      for strategies where bonding/unbonding does not earn yield, substract
      these balances from `amount_allocated.total` to determine which balances
      are currently earning.


      ### Get allocatable balance:


      Call `/0/private/BalanceEx`, subtract `hold_trading` amount. Remaining
      balance is available for allocation to a strategy.


      ### Geo restrictions:


      Some earn strategies are not available in all geographic regions.
      `Strategies` will return only strategies available to the caller.
  - name: Transparency
paths:
  /funding/v1/withdrawals:
    get:
      tags:
        - funding-beta
      summary: List Funding Withdrawals
      description: >-
        Retrieve information about withdrawals. Results are sorted by recency;
        use the `cursor` parameter to iterate through the list of withdrawals
        (page size equal to the value of `limit`) from newest to oldest.


        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: listFundingWithdrawalsV1
      parameters:
        - in: query
          name: asset
          schema:
            description: >-
              Optional filter by asset. When this parameter is provided, `class`
              is required; `name` is optional.
            type: object
            properties:
              class:
                description: Asset class to match. Required when `asset` is provided.
                type: string
                enum:
                  - currency
                  - tokenized_asset
              name:
                description: Asset name to match, if specified.
                type: string
                minLength: 1
                maxLength: 16
            required:
              - class
          style: deepObject
        - in: query
          name: scope
          schema:
            oneOf:
              - type: object
                properties:
                  method_id:
                    description: Funding method defining the scope.
                    type: string
                    pattern: ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                title: method_id
              - type: object
                properties:
                  network_id:
                    description: Network defining the scope.
                    type: string
                    pattern: ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                title: network_id
              - type: object
                properties:
                  network_group_id:
                    description: Network group defining the scope.
                    type: string
                    pattern: ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                title: network_group_id
          style: deepObject
        - in: query
          name: status
          schema:
            description: Filter by status.
            type: string
            enum:
              - pending
              - success
              - failed
          style: form
        - in: query
          name: cursor
          schema:
            description: >-
              Cursor from a previous response used to retrieve the next page. Do
              not provide other request

              parameters with a cursor.
            type: string
            minLength: 1
          style: form
        - in: query
          name: limit
          schema:
            description: Maximum number of withdrawals to return.
            type: integer
            format: int32
            exclusiveMinimum: true
            minimum: 0
            maximum: 500
          style: form
          example: 20
        - in: query
          name: start_time
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          style: form
        - in: query
          name: end_time
          schema:
            $ref: '#/components/schemas/google.protobuf.Timestamp'
          style: form
        - in: query
          name: rebase_multiplier
          schema:
            description: >-
              For tokenized assets, controls whether amounts (eg fees, minimums,
              maximums) use rebased or

              base units.
            type: string
            enum:
              - rebased
              - base
          style: form
        - in: query
          name: account_id
          description: Account ID
          schema:
            type: string
          x-selected-account: true
          style: form
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                description: Response containing the list of funding withdrawals.
                type: object
                properties:
                  withdrawals:
                    description: Withdrawals.
                    type: array
                    items:
                      description: A withdrawal.
                      type: object
                      properties:
                        withdrawal_id:
                          description: Unique identifier of the withdrawal.
                          type: string
                          pattern: ^[Ff][Tt][a-zA-Z0-9]{5}-[a-zA-Z0-9]{22}$
                        amount:
                          description: Withdrawal amount.
                          type: object
                          properties:
                            asset:
                              description: Asset in which the amount is denominated.
                              type: object
                              properties:
                                class:
                                  description: Asset class.
                                  type: string
                                  enum:
                                    - currency
                                    - tokenized_asset
                                name:
                                  description: Asset name.
                                  type: string
                                  minLength: 1
                                  maxLength: 16
                              required:
                                - class
                                - name
                            amount:
                              description: Decimal amount.
                              type: string
                              pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                          required:
                            - asset
                            - amount
                        fee:
                          description: Withdrawal fee.
                          type: object
                          properties:
                            asset:
                              description: Asset in which the amount is denominated.
                              type: object
                              properties:
                                class:
                                  description: Asset class.
                                  type: string
                                  enum:
                                    - currency
                                    - tokenized_asset
                                name:
                                  description: Asset name.
                                  type: string
                                  minLength: 1
                                  maxLength: 16
                              required:
                                - class
                                - name
                            amount:
                              description: Decimal amount.
                              type: string
                              pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                          required:
                            - asset
                            - amount
                        method_id:
                          description: Funding method used for the withdrawal.
                          type: string
                          pattern: >-
                            ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                        status:
                          description: Withdrawal status.
                          type: string
                          enum:
                            - pending
                            - success
                            - failed
                        create_time:
                          $ref: '#/components/schemas/google.protobuf.Timestamp'
                        address_id:
                          description: >-
                            Unique identifier of the withdrawal address. Omitted
                            for withdrawals created without a saved

                            address.
                          type: string
                          pattern: ^AB[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{6}$
                        onchain_transaction:
                          description: On-chain transaction identifier, if available.
                          type: string
                        utxo_vout:
                          description: Bitcoin transaction output index.
                          type: string
                          format: uint64
                          pattern: ^\d+$
                  next_cursor:
                    description: >-
                      Cursor to use in the next request to retrieve the next
                      page. Omitted when there are no more

                      results.
                    type: string
                    minLength: 1
              example:
                withdrawals:
                  - withdrawal_id: FTVZiTI-e02T84mm87JmibnObWNdnW
                    amount:
                      asset:
                        class: currency
                        name: USDC
                      amount: '4.00000000'
                    fee:
                      asset:
                        class: currency
                        name: USDC
                      amount: '1.00000000'
                    method_id: d4ec4d52-b159-428e-ba64-f45455a978a1
                    status: pending
                    create_time: '2026-08-12T10:10:30Z'
                    address_id: ABR6SXP-SF6CY-VJMONY
                  - withdrawal_id: FTa55AO-u7dazcZpBR1nS3Uk42k6LI
                    amount:
                      asset:
                        class: tokenized_asset
                        name: TSLAx
                      amount: '1.30000000'
                    fee:
                      asset:
                        class: tokenized_asset
                        name: TSLAx
                      amount: '0.01300000'
                    method_id: 5104c28e-9da8-43c8-8194-33d9ea1fbdc0
                    status: pending
                    create_time: '2026-08-12T10:07:04Z'
                    address_id: ABVXBF7-RC3Z5-WYUBPD
                next_cursor: >-
                  gqNrZXm-RlRSeFJ2WS1PSHBXSUlrTkYwQU1tM0MzNDg2dkxFpnBhcmFtc4qudXNlcl9zZWxlY3Rpb27ArGFzc2V0X2ZpbHRlcsCzbXVsdGlfbmV0d29ya19zY29wZcCtc3RhdHVzX2ZpbHRlcsCsZmxhZ3NfZmlsdGVywK1hbW91bnRfZmlsdGVywKpzdGFydF90aW1lwKhlbmRfdGltZcCob3JkZXJpbmeqZGVzY2VuZGluZ7FyZWJhc2VfbXVsdGlwbGllcsA
      security:
        - API-Key: []
          API-Sign: []
          API-Nonce: []
        - API-Key: []
          API-Sign: []
          API-Nonce: []
          API-OTP: []
      servers:
        - url: https://api.kraken.com
          description: Production Server
components:
  schemas:
    google.protobuf.Timestamp:
      description: Filter by creation time at or after the specified time.
      type: string
      format: date-time
  securitySchemes:
    API-Key:
      type: apiKey
      description: The "API-Key" header should contain your API key.
      name: API-Key
      in: header
    API-Sign:
      type: apiKey
      description: >-
        Authenticated requests should be signed with the "API-Sign" header,
        using a signature generated with your private key, nonce, encoded
        payload, and URI path.
      name: API-Sign
      in: header
    API-Nonce:
      type: apiKey
      description: >-
        The "API-Nonce" header should contain an always-increasing 64-bit
        integer, most commonly a Unix timestamp in milliseconds. Each request
        must use a nonce greater than the nonce of the previous request signed
        with the same API key.
      name: API-Nonce
      in: header
    API-OTP:
      type: apiKey
      description: >-
        The "API-OTP" header should contain your two-factor authentication
        one-time password. Required only if 2FA is configured for the API key.
      name: API-OTP
      in: header

````
