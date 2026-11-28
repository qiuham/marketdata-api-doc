---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/wallet/private-remove_from_address_book
api_type: JSON-RPC
updated_at: 2026-11-28 18:58:47.523587
---

# private/remove_from_address_book

> Removes an entry from the address book. This method allows you to delete a saved address that is no longer needed.

**Coinbase wallet type**

For Coinbase wallet type accounts the required parameters are `currency` (portfolio currencies or `"all"`) and `type`, plus one of `address` or `id` (the entry identifier returned by `private/get_address_book`). Use `network` and `tag` together with `address` to disambiguate entries sharing the same address.

**📖 Related Article:** [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)

**Scope:** `wallet:read_write`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fremove_from_address_book)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/remove_from_address_book
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
  /private/remove_from_address_book:
    get:
      tags:
        - Wallet
        - Private
      description: >+
        Removes an entry from the address book. This method allows you to delete
        a saved address that is no longer needed.


        **Coinbase wallet type**


        For Coinbase wallet type accounts the required parameters are `currency`
        (portfolio currencies or `"all"`) and `type`, plus one of `address` or
        `id` (the entry identifier returned by `private/get_address_book`). Use
        `network` and `tag` together with `address` to disambiguate entries
        sharing the same address.


        **📖 Related Article:** [Managing
        Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api)


        **Scope:** `wallet:read_write`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fremove_from_address_book)

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
            $ref: '#/components/schemas/address_book_type_without_deposit_source'
            example: transfer
          description: Address book type
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
            entries sharing the same address.
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
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 42
                  method: private/remove_from_address_book
                  params:
                    currency: BTC
                    type: transfer
                    address: bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf0uyj
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateRemoveFromAddressBookResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 42
                    result: ok
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/remove_from_address_book \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 42,
              "method": "private/remove_from_address_book",
              "params": {
                "currency": "BTC",
                "type": "transfer",
                "address": "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf0uyj"
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
    address_book_type_without_deposit_source:
      enum:
        - transfer
        - withdrawal
      type: string
      description: Address book type
    currency_address:
      example: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
      type: string
      description: Address in proper format for currency
    PrivateRemoveFromAddressBookResponse:
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
          type: string
          example: ok
          description: ok
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Coinbase Wallet API](https://docs.deribit.com/articles/coinbase-wallet-api.md)
- [private/get_address_book](https://docs.deribit.com/api-reference/wallet/private-get_address_book.md)
- [private/add_to_address_book](https://docs.deribit.com/api-reference/wallet/private-add_to_address_book.md)