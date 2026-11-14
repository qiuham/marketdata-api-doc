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
source_url: 'https://docs.kraken.com/api-reference/funding-beta/calculate-funding-fees'
updated_at: 2026-11-13
---

# Calculate Funding Fees

> Calculate the fee for a funding method and amount. For withdrawals, the response also includes a unique
`withdrawal_fee_token` that pins the quoted fee rate for later use with
[Create Funding Withdrawal](/api-reference/funding-beta/create-funding-withdrawal). The token expires after
5 minutes and can be used on multiple withdrawals.

**API Key Permissions Required:** `Funds permissions - Query`



## OpenAPI

````yaml /openapi/spot-rest.yaml get /funding/v1/fees/{method_id}
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
  /funding/v1/fees/{method_id}:
    get:
      tags:
        - funding-beta
      summary: Calculate Funding Fees
      description: >-
        Calculate the fee for a funding method and amount. For withdrawals, the
        response also includes a unique

        `withdrawal_fee_token` that pins the quoted fee rate for later use with

        [Create Funding
        Withdrawal](/api-reference/funding-beta/create-funding-withdrawal). The
        token expires after

        5 minutes and can be used on multiple withdrawals.


        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: calculateFundingFeesV1
      parameters:
        - in: path
          name: method_id
          required: true
          schema:
            description: Funding method to calculate fees for.
            type: string
            pattern: ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
          style: simple
          example: d4ec4d52-b159-428e-ba64-f45455a978a1
        - in: query
          name: amount
          required: true
          schema:
            description: Amount to calculate fees for.
            type: string
            pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
          style: form
          example: '5'
        - in: query
          name: fee_included
          schema:
            description: Whether the amount includes the fee.
            type: boolean
          style: form
          example: true
        - in: query
          name: withdrawal_fee_token
          schema:
            description: >-
              Token identifying a previously calculated withdrawal fee quote.
              Expires after 5 minutes and can be used on multiple withdrawals.
            type: string
            minLength: 1
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
                type: object
                properties:
                  fee:
                    description: Calculated funding fee.
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
                  gross_amount:
                    description: Amount including the fee.
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
                  net_amount:
                    description: Amount excluding the fee.
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
                  fee_details:
                    description: Components of the calculated fee.
                    type: object
                    properties:
                      base_fee:
                        description: Fixed fee component.
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
                      fee_percentage:
                        description: Percentage fee component.
                        type: string
                        pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
                    required:
                      - base_fee
                      - fee_percentage
                  withdrawal_fee_token:
                    description: >-
                      Token identifying the calculated withdrawal fee quote for
                      a later request. Expires after 5 minutes and can be used
                      on multiple withdrawals.
                    type: string
                    minLength: 1
                required:
                  - fee
                  - gross_amount
                  - net_amount
                  - fee_details
              example:
                fee:
                  asset:
                    class: currency
                    name: USDC
                  amount: '1.00000000'
                gross_amount:
                  asset:
                    class: currency
                    name: USDC
                  amount: '5.00000000'
                net_amount:
                  asset:
                    class: currency
                    name: USDC
                  amount: '4.00000000'
                fee_details:
                  base_fee:
                    asset:
                      class: currency
                      name: USDC
                    amount: '1.00000000'
                  fee_percentage: '0'
                withdrawal_fee_token: >-
                  AAAAAAAAAAHG33Wc1eES6QpeGgMok_gUnlZC7Y5niezI2,MBriLCyg8oqCX7SH1bSqY6SfmC2ZLf_SgTxNZj4Cd1RLPaTyZE...
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
