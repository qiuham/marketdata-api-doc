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
source_url: 'https://docs.kraken.com/api-reference/funding-beta/list-funding-claimed-addresses-v2'
updated_at: 2026-11-13
---

# List Funding Claimed Addresses (v2)

> Retrieve claimed deposit addresses. Results are paginated; use the `cursor` parameter to iterate through the list of addresses (page size equal to the value of `limit`).

**API Key Permissions Required:** `Funds permissions - Query`

> [!NOTE]
>
> Filter with `scope.method_id` for a specific method. See [how `method_id` is chosen](https://docs.kraken.com/exchange/guides/rest/funding#the-same-address-two-method_id-values).

> [!NOTE]
>
> Not every method on a network shares an address. Methods on the same network often do (ERC-20s on Ethereum, TRC-20s on Tron, SPLs on Solana). Methods in the same network group do not always.


## OpenAPI

````yaml /openapi/spot-rest.yaml get /funding/v2/deposit/addresses
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
  /funding/v2/deposit/addresses:
    get:
      tags:
        - funding-beta
      summary: List Funding Claimed Addresses (v2)
      description: >-
        Retrieve claimed deposit addresses. Results are paginated; use the
        `cursor` parameter to iterate through the list of addresses (page size
        equal to the value of `limit`).


        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: listFundingClaimedAddressesV2
      parameters:
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
            description: >-
              Optional filter by method or network. Claimed deposit addresses
              are not saved against a scope; this filters the list to claimed
              addresses for funding methods within the selected scope. Prefer
              `method_id` as the recommended filter.
          style: deepObject
          description: >-
            Optional filter by method or network. Claimed deposit addresses are
            not saved against a scope; this filters the list to claimed
            addresses for funding methods within the selected scope. Prefer
            `method_id` as the recommended filter.
          example:
            method_id: 27ede8db-804b-4d91-8e25-46b7b9668730
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
            description: Maximum number of claimed deposit addresses to return.
            type: integer
            format: int32
            exclusiveMinimum: true
            minimum: 0
            maximum: 500
          style: form
          example: 20
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
                description: Response containing a page of claimed deposit addresses.
                type: object
                properties:
                  addresses:
                    description: Claimed deposit addresses.
                    type: array
                    items:
                      description: >-
                        A deposit address that has been claimed by the user,
                        with usage and expiration information.
                      type: object
                      properties:
                        method_id:
                          description: >-
                            Funding method for this claimed address. The value
                            depends on the `scope` you passed:


                            - `scope.method_id`: the method you filtered by.
                            Listing USDC on Ethereum returns the USDC
                              method, even when the address is stored against ETH on Ethereum.
                            - `scope.network_id` or no `scope`: the method the
                            address is stored against (ETH on
                              Ethereum in that example).

                            Pass `scope.method_id` when you need the address for
                            a specific deposit method. See

                            [Shared deposit
                            addresses](/exchange/guides/rest/funding#shared-deposit-addresses).
                          type: string
                          pattern: >-
                            ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                        id:
                          description: Identifier of the claimed deposit address.
                          type: string
                          pattern: ^[Ff][Tt][a-zA-Z0-9]{5}-[a-zA-Z0-9]{22}$
                        last_used:
                          $ref: '#/components/schemas/google.protobuf.Timestamp'
                        expire_time:
                          $ref: '#/components/schemas/google.protobuf.Timestamp'
                        address_details:
                          oneOf:
                            - type: object
                              properties:
                                crypto:
                                  description: Crypto deposit address details.
                                  type: object
                                  properties:
                                    address:
                                      description: Crypto address.
                                      type: string
                                    tag:
                                      description: Tag associated with the address.
                                      type: string
                                    memo:
                                      description: Memo associated with the address.
                                      type: string
                                  required:
                                    - address
                              title: crypto
                            - type: object
                              properties:
                                fiat:
                                  description: Fiat deposit address details.
                                  type: object
                                  properties:
                                    account:
                                      description: Bank account number.
                                      type: string
                                    account_type:
                                      description: Bank account type.
                                      type: string
                                    address:
                                      description: Bank or wallet address.
                                      type: string
                                    bank:
                                      description: Bank name.
                                      type: string
                                    bank_code:
                                      description: Bank code.
                                      type: string
                                    bic:
                                      description: Bank identifier code (BIC).
                                      type: string
                                    branch:
                                      description: Bank branch.
                                      type: string
                                    bank_address:
                                      description: Bank address.
                                      type: string
                                    bsb:
                                      description: Bank State Branch (BSB) code.
                                      type: string
                                    iban:
                                      description: >-
                                        International Bank Account Number
                                        (IBAN).
                                      type: string
                                    memo:
                                      description: Payment memo.
                                      type: string
                                    name_on_account:
                                      description: Account holder name.
                                      type: string
                                    routing:
                                      description: Bank routing number.
                                      type: string
                                    sort:
                                      description: Bank sort code.
                                      type: string
                                    swift:
                                      description: SWIFT code.
                                      type: string
                                    tag:
                                      description: Destination tag.
                                      type: string
                                    transit:
                                      description: Bank transit number.
                                      type: string
                              title: fiat
                  next_cursor:
                    description: >-
                      Cursor to use in the next request to retrieve the next
                      page. Omitted when there are no more

                      results.
                    type: string
                    minLength: 1
              example:
                addresses:
                  - method_id: 27ede8db-804b-4d91-8e25-46b7b9668730
                    shares_addresses_with_method_id: a001231f-488e-48c0-b36c-6e0d2c1ee247
                    address_details:
                      crypto:
                        address: 0x0d5cff23d40bcc6b98537c7ad5a839a247f546...
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
