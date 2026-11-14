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
source_url: 'https://docs.kraken.com/api-reference/funding-beta/list-funding-deposits'
updated_at: 2026-11-13
---

# List Funding Deposits

> Retrieve information about deposits. Results are sorted by recency; use the `cursor` parameter to iterate through the list of deposits (page size equal to the value of `limit`) from newest to oldest.

**API Key Permissions Required:** `Funds permissions - Query`



## OpenAPI

````yaml /openapi/spot-rest.yaml get /funding/v1/deposits
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
  /funding/v1/deposits:
    get:
      tags:
        - funding-beta
      summary: List Funding Deposits
      description: >-
        Retrieve information about deposits. Results are sorted by recency; use
        the `cursor` parameter to iterate through the list of deposits (page
        size equal to the value of `limit`) from newest to oldest.


        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: listFundingDepositsV1
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
            oneOf:
              - type: object
                properties:
                  list:
                    description: Match any of the specified statuses.
                    type: array
                    items:
                      type: string
                      enum:
                        - initial
                        - pending
                        - settled
                        - success
                        - failure
                title: list
              - type: object
                properties:
                  range:
                    description: Match statuses within an inclusive range.
                    type: object
                    properties:
                      start:
                        description: Inclusive lower bound. Omitted for no lower bound.
                        type: string
                        enum:
                          - initial
                          - pending
                          - settled
                          - success
                          - failure
                      end:
                        description: Inclusive upper bound. Omitted for no upper bound.
                        type: string
                        enum:
                          - initial
                          - pending
                          - settled
                          - success
                          - failure
                title: range
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
            description: Maximum number of deposits to return.
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
                description: Response containing the list of funding deposits.
                type: object
                properties:
                  deposits:
                    description: Deposits.
                    type: array
                    items:
                      description: A deposit.
                      type: object
                      properties:
                        deposit_id:
                          description: Unique identifier of the deposit.
                          type: string
                          pattern: ^[Ff][Tt][a-zA-Z0-9]{5}-[a-zA-Z0-9]{22}$
                        method_id:
                          description: Funding method used for the deposit.
                          type: string
                          pattern: >-
                            ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                        network_id:
                          description: Network used for the deposit.
                          type: string
                          pattern: >-
                            ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                        status:
                          description: Settlement status.
                          type: string
                          enum:
                            - initial
                            - pending
                            - settled
                            - success
                            - failure
                        amount:
                          description: Deposit amount. Omitted while unknown.
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
                          description: >-
                            Fee charged for the deposit. Omitted until the
                            deposit is complete.
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
                        create_time:
                          $ref: '#/components/schemas/google.protobuf.Timestamp'
                        onchain_transaction:
                          description: >-
                            Blockchain transaction hash for the deposit (when
                            applicable).
                          type: string
                  next_cursor:
                    description: >-
                      Cursor to use in the next request to retrieve the next
                      page. Omitted when there are no more

                      results.
                    type: string
                    minLength: 1
              example:
                deposits:
                  - deposit_id: FTcQ4qW-fWGQbQwUfqdnZo4dsMn1ao
                    method_id: 3e7f8072-cc6d-4394-982a-5f4ca6ab27dd
                    network_id: b336ce74-8d60-42b8-8714-b1095e06b711
                    status: success
                    amount:
                      asset:
                        class: currency
                        name: USDC
                      amount: '20.00000000'
                    fee:
                      asset:
                        class: currency
                        name: USDC
                      amount: '0.00000000'
                    create_time: '2026-07-01T08:31:33Z'
                    onchain_transaction: >-
                      0d0a8f941a1ee0caeca3396757c847e0a3fa326d6994c320b4f283db99cd5e48
                  - deposit_id: FTAsxe1-PHt8Ni7NodvtOEw8FBvLAJ
                    method_id: a897bb0b-e7bc-4eff-969f-433bc811e4ad
                    network_id: d9d375da-44b7-4be1-8a00-8b281acfe366
                    status: success
                    amount:
                      asset:
                        class: currency
                        name: LINK
                      amount: '5555.0000000000'
                    fee:
                      asset:
                        class: currency
                        name: LINK
                      amount: '0.0000000000'
                    create_time: '2026-06-23T08:41:17Z'
                    onchain_transaction: >-
                      0941a1d057c847e0a3fa326da8fee0caeca339676994c320283db99cdb4f5e48
                next_cursor: >-
                  gqNrZXm-RlREc1IxRC1oOTd3c1Y4RFJKUWpPQ0ZTTjVic0NxpnBhcmFtc4qudXNlcl9zZWxlY3Rpb27ArGFzc2V0X2ZpbHRlcsClc2NvcGXArXN0YXR1c19maWx0ZXLArGZsYWdzX2ZpbHRlcsCzZXF1aXZfYW1vdW50X2ZpbHRlcsCqc3RhcnRfdGltZcCoZW5kX3RpbWXAqG9yZGVyaW5nqmRlc2NlbmRpbmexcmViYXNlX211bHRpcGxpZXLA
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
