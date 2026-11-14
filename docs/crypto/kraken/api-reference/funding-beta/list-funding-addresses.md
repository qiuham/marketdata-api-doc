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
source_url: 'https://docs.kraken.com/api-reference/funding-beta/list-funding-addresses'
updated_at: 2026-11-13
---

# List Funding Addresses

> Retrieve saved withdrawal addresses for your account. Results are paginated; use the `cursor` parameter to iterate through the list of addresses (page size equal to the value of `limit`).

**API Key Permissions Required:** `Funds permissions - Query`



## OpenAPI

````yaml /openapi/spot-rest.yaml get /funding/v1/addresses
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
  /funding/v1/addresses:
    get:
      tags:
        - funding-beta
      summary: List Funding Addresses
      description: >-
        Retrieve saved withdrawal addresses for your account. Results are
        paginated; use the `cursor` parameter to iterate through the list of
        addresses (page size equal to the value of `limit`).


        **API Key Permissions Required:** `Funds permissions - Query`
      operationId: listFundingAddressesV1
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
              - type: object
                properties:
                  network_group_id:
                    description: Network group defining the scope.
                    type: string
                    pattern: ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                title: network_group_id
          style: deepObject
          example:
            method_id: 67b765fd-4efd-42dc-8ce7-63352971d566
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
            description: Maximum number of addresses to return.
            type: integer
            format: int32
            exclusiveMinimum: true
            minimum: 0
            maximum: 500
          style: form
          example: 20
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
                  addresses:
                    description: Withdrawal addresses.
                    type: array
                    items:
                      description: A saved withdrawal address.
                      type: object
                      properties:
                        address_id:
                          description: Unique identifier of the withdrawal address.
                          type: string
                          pattern: ^AB[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{6}$
                        scope:
                          oneOf:
                            - type: object
                              properties:
                                method_id:
                                  description: Funding method defining the scope.
                                  type: string
                                  pattern: >-
                                    ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                              title: method_id
                            - type: object
                              properties:
                                network_id:
                                  description: Network defining the scope.
                                  type: string
                                  pattern: >-
                                    ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                              title: network_id
                            - type: object
                              properties:
                                network_group_id:
                                  description: Network group defining the scope.
                                  type: string
                                  pattern: >-
                                    ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
                              title: network_group_id
                        address_details:
                          oneOf:
                            - type: object
                              properties:
                                crypto:
                                  description: Crypto withdrawal address details.
                                  type: object
                                  properties:
                                    address:
                                      description: Crypto address.
                                      type: string
                                    tag:
                                      description: Tag associated with the address.
                                      type: string
                                    beneficiary:
                                      description: Beneficiary information.
                                      type: object
                                      properties:
                                        recipient:
                                          description: >-
                                            Whether the beneficiary is the user
                                            (`sender`) or another party (`other`).
                                          type: string
                                        typ:
                                          description: >-
                                            Beneficiary type (`individual` or
                                            `business`).
                                          type: string
                                        name:
                                          description: Beneficiary first name.
                                          type: string
                                        last_name:
                                          description: Beneficiary last name.
                                          type: string
                                        country:
                                          description: Beneficiary country.
                                          type: string
                                        state_province:
                                          description: Beneficiary state or province.
                                          type: string
                                        address_1:
                                          description: First line of the beneficiary address.
                                          type: string
                                        address_2:
                                          description: Second line of the beneficiary address.
                                          type: string
                                        city:
                                          description: Beneficiary city.
                                          type: string
                                        postal_code:
                                          description: Beneficiary postal code.
                                          type: string
                                        counterparty_vasp_name:
                                          description: >-
                                            Name of the counterparty virtual asset
                                            service provider (VASP).
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
                                  description: Fiat withdrawal address details.
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
                                    branch_code:
                                      description: Bank branch code.
                                      type: string
                                    bank_address:
                                      description: Bank address.
                                      type: string
                                    bsb:
                                      description: Bank State Branch (BSB) code.
                                      type: string
                                    beneficiary:
                                      description: Beneficiary information.
                                      type: object
                                      properties:
                                        recipient:
                                          description: >-
                                            Whether the beneficiary is the user
                                            (`sender`) or another party (`other`).
                                          type: string
                                        typ:
                                          description: >-
                                            Beneficiary type (`individual` or
                                            `business`).
                                          type: string
                                        name:
                                          description: Beneficiary first name.
                                          type: string
                                        last_name:
                                          description: Beneficiary last name.
                                          type: string
                                        country:
                                          description: Beneficiary country.
                                          type: string
                                        state_province:
                                          description: Beneficiary state or province.
                                          type: string
                                        address_1:
                                          description: First line of the beneficiary address.
                                          type: string
                                        address_2:
                                          description: Second line of the beneficiary address.
                                          type: string
                                        city:
                                          description: Beneficiary city.
                                          type: string
                                        postal_code:
                                          description: Beneficiary postal code.
                                          type: string
                                        counterparty_vasp_name:
                                          description: >-
                                            Name of the counterparty virtual asset
                                            service provider (VASP).
                                          type: string
                                    card_number:
                                      description: Card number.
                                      type: string
                                    card_number_last:
                                      description: Last four digits of the card number.
                                      type: string
                                    card_type:
                                      description: Card type.
                                      type: string
                                    cvc:
                                      description: Card verification code.
                                      type: string
                                    expire_month:
                                      description: Card expiration month.
                                      type: string
                                    expire_year:
                                      description: Card expiration year.
                                      type: string
                                    iban:
                                      description: >-
                                        International Bank Account Number
                                        (IBAN).
                                      type: string
                                    masked_iban:
                                      description: Masked IBAN.
                                      type: string
                                    intermediary_address:
                                      description: Intermediary bank address.
                                      type: string
                                    intermediary_bank:
                                      description: Intermediary bank name.
                                      type: string
                                    intermediary_branch:
                                      description: Intermediary bank branch.
                                      type: string
                                    intermediary_routing:
                                      description: Intermediary bank routing number.
                                      type: string
                                    intermediary_swift:
                                      description: Intermediary bank SWIFT or BIC.
                                      type: string
                                    memo:
                                      description: Payment memo.
                                      type: string
                                    merchant_reference:
                                      description: Merchant reference.
                                      type: string
                                    name_on_account:
                                      description: Account holder name.
                                      type: string
                                    notes:
                                      description: Additional notes.
                                      type: string
                                    password:
                                      description: Account password.
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
                                    third_party_email:
                                      description: Third-party email address.
                                      type: string
                                    transaction_id:
                                      description: Payment provider transaction identifier.
                                      type: string
                                    transit:
                                      description: Bank transit number.
                                      type: string
                                    username:
                                      description: Account username.
                                      type: string
                                    signature:
                                      description: >-
                                        Digital signature proving address
                                        ownership.
                                      type: string
                              title: fiat
                        name:
                          description: User provided name for the address. Must be unique.
                          type: string
                        description:
                          description: User provided description of the address.
                          type: string
                        modifier:
                          description: Indicates that the address belongs to a third party.
                          type: string
                          enum:
                            - third_party
                        verified:
                          description: Whether the address is verified and ready for use.
                          type: boolean
                      required:
                        - address_id
                        - scope
                        - verified
                  next_cursor:
                    description: >-
                      Cursor to use in the next request to retrieve the next
                      page. Omitted when there are no more

                      results.
                    type: string
                    minLength: 1
                required:
                  - addresses
              example:
                addresses:
                  - address_id: AB7J4FF-BGM7G-V2JMIH
                    scope:
                      network_id: d9d375da-44b7-4be1-8a00-8b281acfe366
                    address_details:
                      crypto:
                        address: 0xBef7B36845cA31045E86D0B46DBCac4e6752...
                    name: Personal Wallet
                    description: My Ethereum hardware wallet address
                    verified: true
                  - address_id: ABSXEMA-3FXQS-T7Q2FG
                    scope:
                      method_id: 67b765fd-4efd-42dc-8ce7-63352971d566
                    address_details:
                      crypto:
                        address: 0xBef7B36845cA31045E86D0B46DBCac4e6752...
                    verified: true
                    name: Trading Desk Wallet
                    description: Shared EVM withdrawal address
                  - address_id: ABR6SXP-SF6CY-VJMONY
                    scope:
                      network_group_id: f95acdb7-48fb-4441-b5b4-843d3bf60e61
                    address_details:
                      crypto:
                        address: 0xBef7B36845cA31045E86D0B46DBCac4e6752...
                    verified: true
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
