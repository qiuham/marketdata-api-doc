---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/wallet/private-create_deposit_address
api_type: JSON-RPC
updated_at: 2026-11-20 19:00:15.515803
---

# private/create_deposit_address

> Creates a new deposit address for the specified currency. Each currency can have multiple deposit addresses. Use this method to generate a new address for receiving deposits.

**Coinbase wallet type**

For Coinbase wallet type accounts the `network` parameter is required and selects the blockchain network of the deposit address. The networks available for each currency are returned by `public/get_currencies` in the `coinbase_networks` field; a network that is not configured for the currency is rejected. An optional `label` can be provided, defaulting to `"deposit address"`. This method is available to institutional Coinbase accounts only.

**Note:**

For Bitcoin, a new address can be generated every 24 hours.

For ERC20, Solana and XRP only one address can be generated.

**Note:**

If an ERC20 address is generated, this address will be automatically added for every asset that uses ERC20 addresses.

**📖 Related Article:** [Managing Deposits](https://docs.deribit.com/articles/managing-deposits-api)

**Scope:** `wallet:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fcreate_deposit_address)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/create_deposit_address
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
  /private/create_deposit_address:
    get:
      tags:
        - Wallet
        - Private
      description: >+
        Creates a new deposit address for the specified currency. Each currency
        can have multiple deposit addresses. Use this method to generate a new
        address for receiving deposits.


        **Coinbase wallet type**


        For Coinbase wallet type accounts the `network` parameter is required
        and selects the blockchain network of the deposit address. The networks
        available for each currency are returned by `public/get_currencies` in
        the `coinbase_networks` field; a network that is not configured for the
        currency is rejected. An optional `label` can be provided, defaulting to
        `"deposit address"`. This method is available to institutional Coinbase
        accounts only.


        **Note:**


        For Bitcoin, a new address can be generated every 24 hours.


        For ERC20, Solana and XRP only one address can be generated.


        **Note:**


        If an ERC20 address is generated, this address will be automatically
        added for every asset that uses ERC20 addresses.


        **📖 Related Article:** [Managing
        Deposits](https://docs.deribit.com/articles/managing-deposits-api)


        **Scope:** `wallet:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fcreate_deposit_address)

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
        - name: label
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/address_label'
          description: Label of the deposit address. **Coinbase wallet type only.**
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 7538
                  method: private/create_deposit_address
                  params:
                    currency: BTC
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateDepositAddressResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 7538
                    result:
                      address: 2N8udZGBc1hLRCFsU9kGwMPpmYUwMFTuCwB
                      creation_timestamp: 1550575165170
                      currency: BTC
                      type: deposit
                coinbaseResponse:
                  summary: Coinbase response example
                  value:
                    jsonrpc: '2.0'
                    id: 7538
                    result:
                      id: 0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b
                      currency: ETH
                      address: '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'
                      type: deposit
                      kind: onchain
                      label: deposit address
                      creation_timestamp: 1719993033041
                      updated_timestamp: 1719993033041
                      status: active
                      waiting_timestamp: null
                      requires_confirmation: false
                      requires_confirmation_change: false
                      requires_security_key: false
                      info_required: true
                      network: networks/ethereum-mainnet
                      network_display_name: Ethereum
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/create_deposit_address \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 7538,
              "method": "private/create_deposit_address",
              "params": {
                "currency": "BTC"
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
    address_label:
      example: Main address
      type: string
      description: Label of the address book entry
    PrivateDepositAddressResponse:
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
            - type: object
              properties:
                creation_timestamp:
                  $ref: '#/components/schemas/timestamp'
                currency:
                  $ref: '#/components/schemas/currency'
                address:
                  $ref: '#/components/schemas/currency_address'
                type:
                  $ref: '#/components/schemas/wallet_address_type'
              required:
                - creation_timestamp
                - currency
                - address
                - type
              description: Deposit address of a legacy wallet type account
            - $ref: '#/components/schemas/coinbase_address_book_item'
          description: Object if address is created, null otherwise
      required:
        - result
        - jsonrpc
      type: object
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
    currency_address:
      example: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
      type: string
      description: Address in proper format for currency
    wallet_address_type:
      type: string
      description: 'Address type/purpose, allowed values : `deposit`'
    coinbase_address_book_item:
      properties:
        id:
          type: string
          example: 0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b
          description: Unique identifier (UUID7) of the address book entry
        currency:
          type: string
          example: ETH
          description: >-
            The currency symbol, or `"all"` for CTN counterparty entries that
            apply to all currencies
        address:
          type: string
          example: '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'
          description: >-
            The on-chain address, or the CTN counterparty identifier when `kind`
            is `"ctn"`
        type:
          enum:
            - deposit
            - withdrawal
            - transfer
          type: string
          description: Address book entry type
        kind:
          type: string
          enum:
            - onchain
            - ctn
          description: >-
            Kind of the destination: `"onchain"` — blockchain address, `"ctn"` —
            Coinbase Transfer Network counterparty
        label:
          $ref: '#/components/schemas/address_label'
        creation_timestamp:
          $ref: '#/components/schemas/timestamp'
        updated_timestamp:
          $ref: '#/components/schemas/timestamp'
        status:
          type: string
          enum:
            - active
            - waiting
            - ready
          description: >-
            Status of the entry: `"active"` for deposit addresses, `"waiting"`
            while the security delay is pending, `"ready"` otherwise
        waiting_timestamp:
          $ref: '#/components/schemas/waiting_timestamp'
        requires_confirmation:
          $ref: '#/components/schemas/requires_confirmation'
        requires_confirmation_change:
          $ref: '#/components/schemas/requires_confirmation_change'
        requires_security_key:
          type: boolean
          example: false
          description: If withdrawals to this address require a security key
        info_required:
          $ref: '#/components/schemas/address_info_required'
        network:
          type: string
          example: networks/ethereum-mainnet
          description: >-
            Network resource name of the destination (e.g.
            `"networks/ethereum-mainnet"`); absent for CTN entries
        network_display_name:
          type: string
          example: Ethereum
          description: >-
            Human-readable name of the network (e.g. `"Ethereum"`); absent for
            CTN entries
        tag:
          type: string
          description: Destination tag / memo of the entry; absent when not set
        name:
          type: string
          description: Beneficiary name — travel rule data (present when provided)
        country:
          type: string
          description: >-
            Beneficiary country code (ISO 3166-1 alpha-2) — travel rule data
            (present when provided)
        financial_institution:
          type: string
          description: >-
            Financial institution of the beneficiary — travel rule data (present
            when provided)
        account:
          type: string
          description: >-
            Account identifier of the beneficiary — travel rule data (present
            when provided)
        account_location:
          type: string
          description: >-
            Location of the beneficiary account — travel rule data (present when
            provided)
        entity_type:
          type: string
          enum:
            - organization
            - individual
          description: >-
            Type of the beneficiary entity — travel rule data (present when
            provided)
        wallet_type:
          type: string
          enum:
            - exchange
            - self_hosted
          description: >-
            Type of the beneficiary wallet — travel rule data (present when
            provided)
        is_self:
          type: boolean
          description: >-
            Indicates that the beneficiary is the account owner — travel rule
            data (present when provided)
        beneficiary_created:
          $ref: '#/components/schemas/timestamp'
        beneficiary_updated:
          $ref: '#/components/schemas/timestamp'
      required:
        - id
        - currency
        - address
        - type
        - kind
        - creation_timestamp
      type: object
      description: >-
        Address book entry of a Coinbase wallet type account. Returned instead
        of `address_book_item` for Coinbase wallet type users.
    waiting_timestamp:
      nullable: true
      example: 1720252232860
      type: integer
      description: >-
        Timestamp (milliseconds since the Unix epoch) at which the address
        becomes usable; present while status is waiting; null for Coinbase
        deposit addresses.
    requires_confirmation:
      example: true
      type: boolean
      description: If address requires email confirmation for withdrawals
    requires_confirmation_change:
      example: true
      type: boolean
      description: If email confirmation change is in progress
    address_info_required:
      example: true
      type: boolean
      description: >-
        Signalises that addition information regarding the beneficiary of the
        address is required

````

## Related topics

- [Managing Deposits](https://docs.deribit.com/articles/managing-deposits-api.md)
- [private/get_address_book](https://docs.deribit.com/api-reference/wallet/private-get_address_book.md)
- [Coinbase Wallet API](https://docs.deribit.com/articles/coinbase-wallet-api.md)
- [Coinbase International Exchange API Migration](https://docs.deribit.com/articles/intx-api-migration.md)
- [private/get_current_deposit_address](https://docs.deribit.com/api-reference/wallet/private-get_current_deposit_address.md)