---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/wallet/private-get_address_book
api_type: JSON-RPC
updated_at: 2026-11-28 18:58:47.339872
---

# private/get_address_book

> Retrieves the address book entries of the given type. Returns all saved addresses that can be used for withdrawals, along with their labels and beneficiary information if available.

**Coinbase wallet type**

For Coinbase wallet type accounts `currency` accepts any portfolio currency or `"all"`, and `type` accepts `withdrawal`, `transfer` or `deposit` (deposit addresses created via `private/create_deposit_address`). The returned entries are Coinbase address book entry objects: they include the entry `id` (usable instead of `address` in the other address book methods), `kind` (`onchain` or `ctn`), `network`, `network_display_name`, `tag` and the Coinbase travel rule fields (`name`, `country`, `financial_institution`, `account`, `account_location`, `entity_type`, `wallet_type`, `is_self`) when set.

**📖 Related Article:** [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)

**Scope:** `wallet:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_address_book)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_address_book
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
  /private/get_address_book:
    get:
      tags:
        - Wallet
        - Private
      description: >+
        Retrieves the address book entries of the given type. Returns all saved
        addresses that can be used for withdrawals, along with their labels and
        beneficiary information if available.


        **Coinbase wallet type**


        For Coinbase wallet type accounts `currency` accepts any portfolio
        currency or `"all"`, and `type` accepts `withdrawal`, `transfer` or
        `deposit` (deposit addresses created via
        `private/create_deposit_address`). The returned entries are Coinbase
        address book entry objects: they include the entry `id` (usable instead
        of `address` in the other address book methods), `kind` (`onchain` or
        `ctn`), `network`, `network_display_name`, `tag` and the Coinbase travel
        rule fields (`name`, `country`, `financial_institution`, `account`,
        `account_location`, `entity_type`, `wallet_type`, `is_self`) when set.


        **📖 Related Article:** [Managing
        Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)


        **Scope:** `wallet:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_address_book)

      parameters:
        - name: currency
          in: query
          required: true
          schema:
            $ref: '#/components/schemas/currency'
            example: BTC
          description: >-
            The currency symbol. Legacy wallet type: wallet currencies only.
            Coinbase wallet type: any portfolio currency or `"all"`.
        - name: type
          in: query
          required: true
          schema:
            $ref: '#/components/schemas/address_book_type_with_deposit'
            example: withdrawal
          description: >-
            Address book type. Legacy wallet type: `withdrawal`, `transfer` or
            `deposit_source`. Coinbase wallet type: `withdrawal`, `transfer` or
            `deposit`.
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 31
                  method: private/get_address_book
                  params:
                    currency: BTC
                    type: withdrawal
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateAddressBookResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 31
                    result:
                      - waiting_timestamp: 1720252232860
                        creation_timestamp: 1719993033041
                        requires_confirmation_change: false
                        personal: true
                        info_required: false
                        beneficiary_first_name: John
                        beneficiary_last_name: Doe
                        beneficiary_address: NL, Amsterdam, Street, 1
                        requires_confirmation: true
                        currency: BTC
                        agreed: true
                        address: 2NBqqD5GRJ8wHy1PYyCXTe9ke5226FhavBz
                        type: withdrawal
                        status: waiting
                        label: Main Address
                      - waiting_timestamp: 1720252232760
                        creation_timestamp: 1719993032041
                        requires_confirmation_change: false
                        personal: true
                        info_required: false
                        beneficiary_company_name: MyCompany
                        beneficiary_address: NL, Haarlem, Street, 5
                        requires_confirmation: false
                        currency: BTC
                        agreed: true
                        address: bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf0uyj
                        type: withdrawal
                        status: waiting
                        label: One More Address
                coinbaseResponse:
                  summary: Coinbase response example
                  value:
                    jsonrpc: '2.0'
                    id: 31
                    result:
                      - id: 0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b
                        currency: ETH
                        address: '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'
                        type: withdrawal
                        kind: onchain
                        label: Main address
                        creation_timestamp: 1719993033041
                        updated_timestamp: 1719993033041
                        status: waiting
                        waiting_timestamp: 1720252232860
                        requires_confirmation: false
                        requires_confirmation_change: false
                        requires_security_key: true
                        info_required: false
                        network: networks/ethereum-mainnet
                        network_display_name: Ethereum
                        name: Alice Smith
                        country: NL
                        beneficiary_created: 1719993033041
                        beneficiary_updated: 1719993033041
                      - id: 0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5c
                        currency: all
                        address: cp-8f3e2a1b9c4d
                        type: withdrawal
                        kind: ctn
                        label: CTN Partner
                        creation_timestamp: 1719993032041
                        updated_timestamp: 1719993032041
                        status: ready
                        requires_confirmation: false
                        requires_confirmation_change: false
                        requires_security_key: true
                        info_required: true
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_address_book \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 31,
              "method": "private/get_address_book",
              "params": {
                "currency": "BTC",
                "type": "withdrawal"
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
    address_book_type_with_deposit:
      enum:
        - transfer
        - withdrawal
        - deposit_source
        - deposit
      type: string
      description: >-
        Address book type. `deposit_source` is legacy wallet type only;
        `deposit` is Coinbase wallet type only.
    PrivateAddressBookResponse:
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
          type: array
          items:
            oneOf:
              - $ref: '#/components/schemas/address_book_item'
              - $ref: '#/components/schemas/coinbase_address_book_item'
      required:
        - result
        - jsonrpc
      type: object
    address_book_item:
      properties:
        currency:
          $ref: '#/components/schemas/wallet_currency'
        address:
          $ref: '#/components/schemas/currency_address'
        creation_timestamp:
          $ref: '#/components/schemas/timestamp'
        type:
          $ref: '#/components/schemas/address_book_type'
        label:
          $ref: '#/components/schemas/address_label'
        beneficiary_vasp_name:
          $ref: '#/components/schemas/beneficiary_vasp_name'
        beneficiary_vasp_did:
          $ref: '#/components/schemas/beneficiary_vasp_did'
        beneficiary_vasp_website:
          $ref: '#/components/schemas/beneficiary_vasp_website'
        beneficiary_first_name:
          $ref: '#/components/schemas/beneficiary_first_name'
        beneficiary_last_name:
          $ref: '#/components/schemas/beneficiary_last_name'
        beneficiary_company_name:
          $ref: '#/components/schemas/beneficiary_company_name'
        beneficiary_address:
          $ref: '#/components/schemas/beneficiary_address'
        agreed:
          $ref: '#/components/schemas/agree_to_share_with_3rd_party'
        personal:
          $ref: '#/components/schemas/personal_wallet'
        info_required:
          $ref: '#/components/schemas/address_info_required'
        status:
          $ref: '#/components/schemas/status'
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
      required:
        - currency
        - address
        - creation_timestamp
      type: object
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
    wallet_currency:
      enum:
        - BTC
        - ETH
        - STETH
        - ETHW
        - USDC
        - USDT
        - EURR
        - SOL
        - XRP
        - USYC
        - PAXG
        - BNB
        - USDE
      type: string
      description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`
    currency_address:
      example: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
      type: string
      description: Address in proper format for currency
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
    address_book_type:
      enum:
        - transfer
        - withdrawal
        - deposit_source
      type: string
      description: Address book type
    address_label:
      example: Main address
      type: string
      description: Label of the address book entry
    beneficiary_vasp_name:
      example: Money's Gone
      type: string
      description: Name of beneficiary VASP
    beneficiary_vasp_did:
      example: did:example:123456789abcdefghi
      type: string
      description: DID of beneficiary VASP
    beneficiary_vasp_website:
      type: string
      description: Website of the beneficiary VASP
    beneficiary_first_name:
      example: John
      type: string
      description: First name of the beneficiary (if beneficiary is a person)
    beneficiary_last_name:
      example: Doe
      type: string
      description: Last name of the beneficiary (if beneficiary is a person)
    beneficiary_company_name:
      example: Company Name
      type: string
      description: Company name of the beneficiary (if beneficiary is a company)
    beneficiary_address:
      example: NL, Amsterdam, Street, 1
      type: string
      description: Geographical address of the beneficiary
    agree_to_share_with_3rd_party:
      example: true
      type: boolean
      description: >-
        Indicates that the user agreed to shared provided information with 3rd
        parties
    personal_wallet:
      example: true
      type: boolean
      description: >-
        The user confirms that he provided address belongs to him and he has
        access to it via an un-hosted wallet software
    address_info_required:
      example: true
      type: boolean
      description: >-
        Signalises that addition information regarding the beneficiary of the
        address is required
    status:
      enum:
        - admin_locked
        - waiting
        - confirmed
        - ready
      type: string
      description: >-
        Wallet address status, values: [`admin_locked`, `waiting`, `confirmed`,
        `ready`]
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

````

## Related topics

- [private/remove_from_address_book](https://docs.deribit.com/api-reference/wallet/private-remove_from_address_book.md)
- [private/update_in_address_book](https://docs.deribit.com/api-reference/wallet/private-update_in_address_book.md)
- [private/set_address_requires_security_key](https://docs.deribit.com/api-reference/wallet/private-set_address_requires_security_key.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api.md)