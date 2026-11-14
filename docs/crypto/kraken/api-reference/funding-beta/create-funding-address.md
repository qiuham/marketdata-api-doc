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
source_url: 'https://docs.kraken.com/api-reference/funding-beta/create-funding-address'
updated_at: 2026-11-13
---

# Create Funding Address

> Save a withdrawal address to the account for a funding method, network, or network group. See
[Adding a withdrawal address](/exchange/guides/rest/funding#section-1-adding-a-withdrawal-address) for how
those scopes work.

**API Key Permissions Required:** `Funds permissions - Add withdrawal addresses`

> [!WARNING]
>
> Addresses added via the Create Funding Address endpoint are automatically verified and do not require email verification. See [Withdrawal addresses API permission](https://support.kraken.com/articles/withdrawal-addresses-api-permission) for the risks of this permission.

> [!NOTE]
>
> Managing fiat withdrawal addresses through this endpoint is not available at this time. Only crypto withdrawal addresses can be created. Fiat withdrawals can still be submitted with [Create Funding Withdrawal](https://docs.kraken.com/api-reference/funding-beta/create-funding-withdrawal.md) using fiat addresses added via the Kraken UI.


## OpenAPI

````yaml /openapi/spot-rest.yaml post /funding/v1/addresses
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
    post:
      tags:
        - funding-beta
      summary: Create Funding Address
      description: >-
        Save a withdrawal address to the account for a funding method, network,
        or network group. See

        [Adding a withdrawal
        address](/exchange/guides/rest/funding#section-1-adding-a-withdrawal-address)
        for how

        those scopes work.


        **API Key Permissions Required:** `Funds permissions - Add withdrawal
        addresses`
      operationId: createFundingAddressV1
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
                Request to create a withdrawal address for a given network
                group, network

                or funding method.
              type: object
              properties:
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
                          description: Crypto address details.
                          type: object
                          properties:
                            address:
                              description: Crypto address.
                              type: string
                              minLength: 1
                            tag:
                              description: >-
                                Optional destination tag for the withdrawal
                                address. Only used on blockchains that allow a
                                tag

                                or memo. `tag` and `memo` are both accepted. If
                                you send `tag` but the method or network uses

                                `memo`, [List Funding
                                Addresses](/api-reference/funding-beta/list-funding-addresses)
                                returns the

                                value as `memo`, and the other way around.
                              type: string
                            memo:
                              description: >-
                                Optional memo for the withdrawal address. Only
                                used on blockchains that allow a tag or memo.

                                `tag` and `memo` are both accepted. If you send
                                `memo` but the method or network uses `tag`,

                                [List Funding
                                Addresses](/api-reference/funding-beta/list-funding-addresses)
                                returns the value as

                                `tag`, and the other way around.
                              type: string
                      title: crypto
                name:
                  description: >-
                    User provided name for the address. Must be unique and
                    contain at least one non-whitespace

                    character. Surrounding whitespace is removed.
                  type: string
                  minLength: 1
                description:
                  description: User provided description of the address.
                  type: string
              required:
                - scope
                - address_details
                - name
              example:
                scope:
                  network_id: d9d375da-44b7-4be1-8a00-8b281acfe366
                address_details:
                  crypto:
                    address: 0xBef7B36845cA31045E86D0B46DBCac4e6752...
                name: Personal Wallet
                description: My hardware wallet address
            example:
              scope:
                network_id: d9d375da-44b7-4be1-8a00-8b281acfe366
              address_details:
                crypto:
                  address: 0xBef7B36845cA31045E86D0B46DBCac4e6752...
              name: Personal Wallet
              description: My hardware wallet address
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  address_id:
                    description: Unique identifier of the created address.
                    type: string
                    pattern: ^AB[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{6}$
                  verified:
                    description: Whether the address is verified and ready for use.
                    type: boolean
                required:
                  - address_id
                  - verified
              example:
                address_id: AB7J4FF-BGM7G-V2JMIH
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
