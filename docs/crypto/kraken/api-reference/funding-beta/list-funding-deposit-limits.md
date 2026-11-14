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
source_url: 'https://docs.kraken.com/api-reference/funding-beta/list-funding-deposit-limits'
updated_at: 2026-11-13
---

# List Funding Deposit Limits

> Retrieve deposit limits for an asset, including remaining and maximum amounts where applicable.

**API Key Permissions Required:** `Funds permissions - Query`



## OpenAPI

````yaml /openapi/spot-rest.yaml get /funding/v1/limits/deposit/{asset_class}/{asset}
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
  /funding/v1/limits/deposit/{asset_class}/{asset}:
    get:
      tags:
        - funding-beta
      summary: List Funding Deposit Limits
      description: >-
        Retrieve deposit limits for an asset, including remaining and maximum
        amounts where applicable.


        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: listFundingDepositLimitsV1
      parameters:
        - in: path
          name: asset_class
          required: true
          schema:
            description: Filter by asset class.
            type: string
            enum:
              - currency
              - tokenized_asset
          style: simple
          example: currency
        - in: path
          name: asset
          required: true
          schema:
            description: Filter by asset.
            type: string
            minLength: 1
            maxLength: 16
          style: simple
          example: BTC
        - in: query
          name: preferred_asset
          schema:
            description: >-
              Asset in which to express returned limit amounts. When omitted,
              amounts are returned in the

              funding method’s asset.
            type: object
            properties:
              class:
                description: Asset class to match.
                type: string
                enum:
                  - currency
                  - tokenized_asset
              name:
                description: Asset name to match.
                type: string
                minLength: 1
                maxLength: 16
            required:
              - name
          style: deepObject
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
                type: object
                properties:
                  deposit_limits:
                    description: Deposit limits by funding method.
                    type: array
                    items:
                      type: object
                      properties:
                        method_id:
                          description: Funding method associated with the limits.
                          type: string
                          pattern: >-
                            ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                        maximum_amount:
                          description: >-
                            Maximum deposit amount allowed by amount based
                            limits. Attempt and transaction-count limits are

                            not included.
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
                        limits:
                          description: Funding limits for the method.
                          type: array
                          items:
                            description: A funding limit for a time window.
                            type: object
                            properties:
                              time_window:
                                description: >-
                                  Length of the time window over which the limit
                                  applies.
                                type: string
                                format: uint64
                                pattern: ^\d+$
                              limit:
                                description: Limit values for the applicable metric.
                                oneOf:
                                  - type: object
                                    properties:
                                      limit_type:
                                        type: string
                                        enum:
                                          - equiv_amount_usd
                                      remaining:
                                        description: Amount remaining in the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                      maximum:
                                        description: Maximum amount for the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                      used:
                                        description: Amount used in the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                    required:
                                      - remaining
                                      - maximum
                                      - limit_type
                                    title: limit_type | remaining | maximum | used
                                  - type: object
                                    properties:
                                      limit_type:
                                        type: string
                                        enum:
                                          - equiv_amount_eur
                                      remaining:
                                        description: Amount remaining in the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                      maximum:
                                        description: Maximum amount for the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                      used:
                                        description: Amount used in the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                    required:
                                      - remaining
                                      - maximum
                                      - limit_type
                                    title: limit_type | remaining | maximum | used
                                  - type: object
                                    properties:
                                      limit_type:
                                        type: string
                                        enum:
                                          - equiv_amount_cad
                                      remaining:
                                        description: Amount remaining in the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                      maximum:
                                        description: Maximum amount for the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                      used:
                                        description: Amount used in the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                    required:
                                      - remaining
                                      - maximum
                                      - limit_type
                                    title: limit_type | remaining | maximum | used
                                  - type: object
                                    properties:
                                      limit_type:
                                        type: string
                                        enum:
                                          - equiv_amount_gbp
                                      remaining:
                                        description: Amount remaining in the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                      maximum:
                                        description: Maximum amount for the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                      used:
                                        description: Amount used in the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                    required:
                                      - remaining
                                      - maximum
                                      - limit_type
                                    title: limit_type | remaining | maximum | used
                                  - type: object
                                    properties:
                                      limit_type:
                                        type: string
                                        enum:
                                          - attempt
                                      remaining:
                                        description: Count remaining in the time window.
                                        type: string
                                        pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                                      maximum:
                                        description: Maximum count for the time window.
                                        type: string
                                        pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                                      used:
                                        description: Count used in the time window.
                                        type: string
                                        pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                                    required:
                                      - remaining
                                      - maximum
                                      - limit_type
                                    title: limit_type | remaining | maximum | used
                                  - type: object
                                    properties:
                                      limit_type:
                                        type: string
                                        enum:
                                          - success
                                      remaining:
                                        description: Count remaining in the time window.
                                        type: string
                                        pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                                      maximum:
                                        description: Maximum count for the time window.
                                        type: string
                                        pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                                      used:
                                        description: Count used in the time window.
                                        type: string
                                        pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                                    required:
                                      - remaining
                                      - maximum
                                      - limit_type
                                    title: limit_type | remaining | maximum | used
                                  - type: object
                                    properties:
                                      limit_type:
                                        type: string
                                        enum:
                                          - amount
                                      remaining:
                                        description: Amount remaining in the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                      maximum:
                                        description: Maximum amount for the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                      used:
                                        description: Amount used in the time window.
                                        type: object
                                        properties:
                                          policy_asset_amount:
                                            description: >-
                                              Amount in the asset used by the limit
                                              policy.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          usd_amount:
                                            description: Equivalent amount in USD.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          requested_asset_amount:
                                            description: >-
                                              Equivalent amount in the requested
                                              asset. Uses the funding method's asset
                                              when

                                              `preferred_asset` is omitted.
                                            type: object
                                            properties:
                                              asset:
                                                description: >-
                                                  Asset in which the amount is
                                                  denominated.
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
                                          - policy_asset_amount
                                    required:
                                      - remaining
                                      - maximum
                                      - limit_type
                                    title: limit_type | remaining | maximum | used
                            required:
                              - time_window
                              - limit
                      required:
                        - method_id
                        - limits
              example:
                deposit_limits:
                  - method_id: 742656ee-ecc8-4287-a301-5a472ca16c24
                    maximum_amount:
                      asset:
                        class: currency
                        name: USDC
                      amount: '100032.01024328'
                    limits: []
                  - method_id: 98de2213-0e3c-422c-9b08-81078557ad3a
                    limits: []
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
