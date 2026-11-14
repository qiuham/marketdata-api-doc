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
source_url: 'https://docs.kraken.com/api-reference/funding-beta/claim-funding-deposit-address'
updated_at: 2026-11-13
---

# Claim Funding Deposit Address

> Claim a deposit address for a funding method. This generates an address for receiving funds.

**API Key Permissions Required:** `Funds permissions - Deposit`

> [!NOTE]
>
> Claim with the deposit `method_id` you want to use. If that method shares addresses with another method on the same network (for example ERC-20s with ETH on Ethereum, TRC-20s with TRX on Tron, or SPLs with SOL on Solana), Kraken returns the shared address. You do not need to claim against the owner method first.

> [!NOTE]
>
> Not every method on a network shares an address. Methods on the same network often do (ERC-20s on Ethereum, TRC-20s on Tron, SPLs on Solana). Methods in the same network group do not always.


## OpenAPI

````yaml /openapi/spot-rest.yaml put /funding/v1/deposit/address
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
  /funding/v1/deposit/address:
    put:
      tags:
        - funding-beta
      summary: Claim Funding Deposit Address
      description: >-
        Claim a deposit address for a funding method. This generates an address
        for receiving funds.


        **API Key Permissions Required:** `Funds permissions - Deposit`
      operationId: claimFundingDepositAddressV1
      parameters:
        - in: query
          name: account_id
          description: Account ID
          schema:
            type: string
          x-selected-account: true
          style: form
      requestBody:
        content:
          application/json:
            schema:
              description: >-
                Request to claim a deposit address for a specific funding
                method.

                This generates a deposit address for receiving funds.
              type: object
              properties:
                method_id:
                  description: Funding method to claim a deposit address for.
                  type: string
                  pattern: ^[0-9a-fA-F]{8}-?(?:[0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$
              example:
                method_id: 27ede8db-804b-4d91-8e25-46b7b9668730
            example:
              method_id: 27ede8db-804b-4d91-8e25-46b7b9668730
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                description: >-
                  Response containing the details of the claimed deposit
                  address.
                type: object
                properties:
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
                                description: International Bank Account Number (IBAN).
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
              example:
                address_details:
                  crypto:
                    address: AikyzpZZcNAeovd6XnyEaEe6YB1tPKkXZF37rUWD...
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
