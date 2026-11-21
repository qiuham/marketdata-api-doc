---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/wallet/private-update_in_address_book
api_type: JSON-RPC
updated_at: 2026-11-21 19:01:45.274018
---

# private/update_in_address_book

> Updates beneficiary information for an address in the address book. This method allows you to add or modify beneficiary details required for compliance purposes when making withdrawals to certain addresses.

**Coinbase wallet type**

For Coinbase wallet type accounts the method behaves differently:

- Required parameters are `currency` (portfolio currencies or `"all"`) and `type`, plus one of `address` or `id` (the entry identifier returned by `private/get_address_book`). Use `network` and `tag` together with `address` to disambiguate entries sharing the same address.
- `type` accepts only `withdrawal` and `transfer`.
- `label` is optional.
- Travel rule data is provided with the fields `name`, `country`, `address`, `financial_institution`, `account`, `account_location`, `entity_type` (`organization` or `individual`), `wallet_type` (`exchange` or `self_hosted`) and `is_self` instead of the legacy `beneficiary_*`, `agreed` and `personal` fields.
- The response contains the updated Coinbase address book entry object instead of `"ok"`.

**📖 Related Article:** [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)

**Scope:** `wallet:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fupdate_in_address_book)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/update_in_address_book
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
  /private/update_in_address_book:
    get:
      tags:
        - Wallet
        - Private
      description: >+
        Updates beneficiary information for an address in the address book. This
        method allows you to add or modify beneficiary details required for
        compliance purposes when making withdrawals to certain addresses.


        **Coinbase wallet type**


        For Coinbase wallet type accounts the method behaves differently:


        - Required parameters are `currency` (portfolio currencies or `"all"`)
        and `type`, plus one of `address` or `id` (the entry identifier returned
        by `private/get_address_book`). Use `network` and `tag` together with
        `address` to disambiguate entries sharing the same address.

        - `type` accepts only `withdrawal` and `transfer`.

        - `label` is optional.

        - Travel rule data is provided with the fields `name`, `country`,
        `address`, `financial_institution`, `account`, `account_location`,
        `entity_type` (`organization` or `individual`), `wallet_type`
        (`exchange` or `self_hosted`) and `is_self` instead of the legacy
        `beneficiary_*`, `agreed` and `personal` fields.

        - The response contains the updated Coinbase address book entry object
        instead of `"ok"`.


        **📖 Related Article:** [Managing
        Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)


        **Scope:** `wallet:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fupdate_in_address_book)

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
            $ref: '#/components/schemas/address_book_type'
            example: withdrawal
          description: >-
            Address book type. Legacy wallet type: `withdrawal`, `transfer` or
            `deposit_source`. Coinbase wallet type: `withdrawal` or `transfer`
            only.
        - name: address
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/currency_address'
            example: bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf0uyj
          description: >-
            Address in currency format, it must be in address book. **Required
            for legacy wallet type.** **Coinbase wallet type:** required when
            `id` is not provided; use `network` and `tag` to disambiguate
            entries sharing the same address. For Coinbase wallet type the same
            value is also stored as the beneficiary address travel rule field.
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
        - name: tag
          in: query
          schema:
            type: string
          required: false
          description: >-
            Destination tag / memo for networks that support one. **Coinbase
            wallet type only.** Used together with `address` and `network`; also
            serves to disambiguate address book entries that share the same
            address.
        - name: id
          in: query
          schema:
            type: string
            example: 0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b
          required: false
          description: >-
            Unique identifier (UUID7) of the address book entry, as returned in
            the `id` field of `private/get_address_book` results. **Coinbase
            wallet type only.** Can be used instead of `address` (with `network`
            and `tag`) to identify the entry.
        - name: label
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/address_label'
            example: Main address
          description: >-
            Label of the address book entry. **Required for legacy wallet
            type**; optional for Coinbase wallet type.
        - name: beneficiary_vasp_name
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/beneficiary_vasp_name'
            example: Money`s Gone
          description: Name of beneficiary VASP. **Legacy wallet type only.**
        - name: beneficiary_vasp_did
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/beneficiary_vasp_did'
            example: did:example:123456789abcdefghi
          description: DID of beneficiary VASP. **Legacy wallet type only.**
        - name: beneficiary_vasp_website
          in: query
          schema:
            $ref: '#/components/schemas/beneficiary_vasp_website'
          required: false
          description: >-
            Website of the beneficiary VASP. Required if the address book entry
            is associated with a VASP that is not included in the list of known
            VASPs
        - name: beneficiary_first_name
          in: query
          schema:
            $ref: '#/components/schemas/beneficiary_first_name'
          description: First name of beneficiary (if beneficiary is a person)
          required: false
        - name: beneficiary_last_name
          in: query
          schema:
            $ref: '#/components/schemas/beneficiary_last_name'
          description: First name of beneficiary (if beneficiary is a person)
          required: false
        - name: beneficiary_company_name
          in: query
          schema:
            $ref: '#/components/schemas/beneficiary_company_name'
          description: Beneficiary company name (if beneficiary is a company)
          required: false
        - name: beneficiary_address
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/beneficiary_address'
            example: NL, Amsterdam, Street, 1
          description: >-
            Geographical address of the beneficiary. **Legacy wallet type
            only.**
        - name: agreed
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/agree_to_share_with_3rd_party'
            example: true
          description: >-
            Indicates that the user agreed to shared provided information with
            3rd parties. **Legacy wallet type only.**
        - name: personal
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/personal_wallet'
            example: false
          description: >-
            The user confirms that he provided address belongs to him and he has
            access to it via an un-hosted wallet software. **Legacy wallet type
            only.**
        - name: name
          in: query
          schema:
            type: string
            example: Alice Smith
          required: false
          description: >-
            Full name of the beneficiary (person or organization). **Coinbase
            wallet type only** — travel rule data.
        - name: country
          in: query
          schema:
            type: string
            example: NL
          required: false
          description: >-
            Country code of the beneficiary (ISO 3166-1 alpha-2). **Coinbase
            wallet type only** — travel rule data.
        - name: financial_institution
          in: query
          schema:
            type: string
          required: false
          description: >-
            Name of the financial institution holding the beneficiary account.
            **Coinbase wallet type only** — travel rule data.
        - name: account
          in: query
          schema:
            type: string
          required: false
          description: >-
            Account identifier of the beneficiary at the financial institution.
            **Coinbase wallet type only** — travel rule data.
        - name: account_location
          in: query
          schema:
            type: string
          required: false
          description: >-
            Location of the beneficiary account. **Coinbase wallet type only** —
            travel rule data.
        - name: entity_type
          in: query
          schema:
            type: string
            enum:
              - organization
              - individual
          required: false
          description: >-
            Type of the beneficiary entity. **Coinbase wallet type only** —
            travel rule data.
        - name: wallet_type
          in: query
          schema:
            type: string
            enum:
              - exchange
              - self_hosted
          required: false
          description: >-
            Type of the beneficiary wallet. **Coinbase wallet type only** —
            travel rule data.
        - name: is_self
          in: query
          schema:
            type: boolean
          required: false
          description: >-
            Indicates that the beneficiary is the account owner. **Coinbase
            wallet type only** — travel rule data.
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 42
                  method: private/update_in_address_book
                  params:
                    currency: BTC
                    type: withdrawal
                    address: bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf0uyj
                    label: Main address
                    beneficiary_vasp_name: Money`s Gone
                    beneficiary_vasp_did: did:example:123456789abcdefghi
                    beneficiary_first_name: John
                    beneficiary_last_name: Doe
                    beneficiary_address: NL, Amsterdam, Street, 1
                    agreed: true
                    personal: false
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateUpdateInAddressBookResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 42
                    result: ok
                coinbaseResponse:
                  summary: Coinbase response example
                  value:
                    jsonrpc: '2.0'
                    id: 42
                    result:
                      id: 0190a1b2-7c3d-7e5f-8a9b-0c1d2e3f4a5b
                      currency: ETH
                      address: '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'
                      type: withdrawal
                      kind: onchain
                      label: Updated label
                      creation_timestamp: 1719993033041
                      updated_timestamp: 1720252232860
                      status: ready
                      requires_confirmation: false
                      requires_confirmation_change: false
                      requires_security_key: true
                      info_required: false
                      network: networks/ethereum-mainnet
                      network_display_name: Ethereum
                      name: Alice Smith
                      country: NL
                      beneficiary_created: 1719993033041
                      beneficiary_updated: 1720252232860
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/update_in_address_book \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 42,
              "method": "private/update_in_address_book",
              "params": {
                "currency": "BTC",
                "type": "withdrawal",
                "address": "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf0uyj",
                "label": "Main address",
                "beneficiary_vasp_name": "Money`s Gone",
                "beneficiary_vasp_did": "did:example:123456789abcdefghi",
                "beneficiary_first_name": "John",
                "beneficiary_last_name": "Doe",
                "beneficiary_address": "NL, Amsterdam, Street, 1",
                "agreed": true,
                "personal": false
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
    address_book_type:
      enum:
        - transfer
        - withdrawal
        - deposit_source
      type: string
      description: Address book type
    currency_address:
      example: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
      type: string
      description: Address in proper format for currency
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
    PrivateUpdateInAddressBookResponse:
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
            - type: string
              example: ok
              description: '"ok" for legacy wallet type accounts'
            - $ref: '#/components/schemas/coinbase_address_book_item'
      required:
        - result
        - jsonrpc
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
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
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

- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Coinbase Wallet API](https://docs.deribit.com/articles/coinbase-wallet-api.md)
- [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api.md)
- [private/get_address_book](https://docs.deribit.com/api-reference/wallet/private-get_address_book.md)
- [private/add_to_address_book](https://docs.deribit.com/api-reference/wallet/private-add_to_address_book.md)