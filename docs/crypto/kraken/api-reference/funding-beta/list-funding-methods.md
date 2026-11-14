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
source_url: 'https://docs.kraken.com/api-reference/funding-beta/list-funding-methods'
updated_at: 2026-11-13
---

# List Funding Methods

> Retrieve funding methods for the requested direction (deposit or withdraw). Results are paginated; use the `cursor` parameter to iterate through the list of methods (page size equal to the value of `limit`).

**API Key Permissions Required:** `Funds permissions - Query`



## OpenAPI

````yaml /openapi/spot-rest.yaml get /funding/v1/methods/{direction}
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
  /funding/v1/methods/{direction}:
    get:
      tags:
        - funding-beta
      summary: List Funding Methods
      description: >-
        Retrieve funding methods for the requested direction (deposit or
        withdraw). Results are paginated; use the `cursor` parameter to iterate
        through the list of methods (page size equal to the value of `limit`).


        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: listFundingMethodsV1
      parameters:
        - in: path
          name: direction
          required: true
          schema:
            description: Filter by direction.
            type: string
            enum:
              - deposit
              - withdraw
          style: simple
          example: deposit
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
                example: currency
              name:
                description: Asset name to match, if specified.
                type: string
                minLength: 1
                maxLength: 16
                example: USDC
            required:
              - class
          style: deepObject
          example:
            class: currency
            name: USDC
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
          name: limit
          schema:
            description: Maximum number of methods to return.
            type: integer
            format: int32
            exclusiveMinimum: true
            minimum: 0
            maximum: 10000
          style: form
          example: 50
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
                description: >-
                  All funding methods available to the user for funding its
                  kraken account.
                type: object
                properties:
                  methods:
                    description: Available funding methods.
                    type: array
                    items:
                      description: >-
                        A deposit or withdrawal method for an asset on a
                        specific network.
                      type: object
                      properties:
                        deposit:
                          description: >-
                            Deposit specific details. Present only for deposit
                            methods.
                          type: object
                          properties:
                            shares_addresses_with_method_id:
                              description: >-
                                The funding method this method shares its
                                deposit address family with. Present only when
                                this

                                method reuses another method's deposit
                                addresses; omitted when it has its own. See

                                [Shared deposit
                                addresses](/exchange/guides/rest/funding#shared-deposit-addresses)

                                for how shared addresses work when you list or
                                claim.
                              type: string
                              pattern: >-
                                ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                            address_setup_fee:
                              description: >-
                                Fee charged when the user first claims an
                                address for this funding method.
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
                            address_generation:
                              description: Address generation availability and limit.
                              type: object
                              properties:
                                status:
                                  description: Address generation availability.
                                  type: string
                                  enum:
                                    - unsupported
                                    - unlimited
                                    - limited
                                limit:
                                  description: >-
                                    Maximum number of addresses when `status` is
                                    `limited`.
                                  type: integer
                                  format: int32
                                  exclusiveMinimum: true
                                  minimum: 0
                              required:
                                - status
                            allow_credit_cards:
                              description: >-
                                Whether credit card deposits are allowed. Only
                                provided for credit card methods; `false` means

                                only debit cards are allowed in the user's
                                country.
                              type: boolean
                            exempted_withdrawal_hold:
                              description: >-
                                Whether deposits made with this method are
                                exempt from its withdrawal hold. Only provided
                                for

                                methods that impose a withdrawal hold.
                              type: boolean
                        withdrawal:
                          description: Present only for withdrawal methods.
                          type: object
                        asset:
                          description: Asset supported by the funding method.
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
                        method_id:
                          description: Unique identifier of the funding method.
                          type: string
                          pattern: >-
                            ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                        method_name:
                          description: Display name of the funding method.
                          type: string
                          minLength: 1
                        minimum_amount:
                          description: Minimum amount per transaction.
                          type: string
                          pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                        maximum_amount:
                          description: Maximum amount per transaction.
                          type: string
                          pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                        fees:
                          description: Fees charged per transaction.
                          type: object
                          properties:
                            base:
                              description: Base fee charged per transaction.
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
                            percentage:
                              description: Percentage fee charged per transaction.
                              type: string
                              pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                            included:
                              description: >-
                                Whether the fee is included in the transaction
                                amount.
                              type: boolean
                            min:
                              description: Minimum fee charged per transaction.
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
                            max:
                              description: Maximum fee charged per transaction.
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
                          required:
                            - base
                            - included
                        network:
                          description: Network used by the funding method.
                          type: object
                          properties:
                            network_id:
                              description: Unique identifier of the network.
                              type: string
                              pattern: >-
                                ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                            network_name:
                              description: Network name.
                              type: string
                              minLength: 1
                            contract_address:
                              description: Token contract address on the network.
                              type: string
                            on_chain_asset_symbol:
                              description: Asset symbol used on the network.
                              type: string
                          required:
                            - network_id
                            - network_name
                      required:
                        - asset
                        - method_id
                        - method_name
                        - fees
                  next_cursor:
                    description: >-
                      Cursor to use in the next request to retrieve the next
                      page. Omitted when there are no more

                      results.
                    type: string
                    minLength: 1
              example:
                methods:
                  - asset:
                      class: currency
                      name: USDC
                    method_id: 27ede8db-804b-4d91-8e25-46b7b9668730
                    method_name: Standard
                    minimum_amount: '2'
                    fees:
                      base:
                        asset:
                          class: currency
                          name: USDC
                        amount: '0.00000000'
                      included: true
                    network:
                      network_id: d9d375da-44b7-4be1-8a00-8b281acfe366
                      network_name: Ethereum
                      contract_address: '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
                      on_chain_asset_symbol: USDC
                    deposit:
                      address_generation:
                        status: limited
                        limit: 5
                      shares_addresses_with_method_id: a001231f-488e-48c0-b36c-6e0d2c1ee247
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
