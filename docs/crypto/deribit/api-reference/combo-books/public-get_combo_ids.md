---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/combo-books/public-get_combo_ids
api_type: JSON-RPC
updated_at: 2026-11-25 19:00:48.526654
---

# public/get_combo_ids

> Retrieves combo IDs for a required settlement `currency`. `"any"` is not accepted here — use `public/get_combos` with `currency=any` for active combos across currencies.

`state` defaults to `"any"`, which returns **active and inactive** IDs and excludes `closed`. Pass `"active"` or `"inactive"` to filter. Public clients cannot select `closed` or `archivized`.

Use [public/get_combo_details](https://docs.deribit.com/api-reference/combo-books/public-get_combo_details) for legs and timestamps of a live combo. Archivized combos are not in this list; look them up with `public/get_instrument`.

**📖 Related Article:** [Options Data Collection Best Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_combo_ids)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/get_combo_ids
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
  /public/get_combo_ids:
    get:
      tags:
        - Combo Books
        - Public
      description: >+
        Retrieves combo IDs for a required settlement `currency`. `"any"` is not
        accepted here — use `public/get_combos` with `currency=any` for active
        combos across currencies.


        `state` defaults to `"any"`, which returns **active and inactive** IDs
        and excludes `closed`. Pass `"active"` or `"inactive"` to filter. Public
        clients cannot select `closed` or `archivized`.


        Use
        [public/get_combo_details](https://docs.deribit.com/api-reference/combo-books/public-get_combo_details)
        for legs and timestamps of a live combo. Archivized combos are not in
        this list; look them up with `public/get_instrument`.


        **📖 Related Article:** [Options Data Collection Best
        Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_combo_ids)

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
        - name: state
          required: false
          in: query
          schema:
            $ref: '#/components/schemas/combo_state_filter'
          description: >-
            Combo state filter. If omitted, `"any"` (active and inactive,
            excluding closed).
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 1
                  method: public/get_combo_ids
                  params:
                    currency: BTC
                    state: active
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicGetComboIdsResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 1
                    result:
                      - BTC-CS-29APR22-39300_39600
                      - BTC-FS-29APR22_PERP
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/get_combo_ids \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 1,
              "method": "public/get_combo_ids",
              "params": {
                "currency": "BTC",
                "state": "active"
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
    combo_state_filter:
      enum:
        - active
        - inactive
        - any
      type: string
      description: >
        Combo state filter for `public/get_combo_ids`: `"active"`, `"inactive"`,
        or `"any"` (default) for active and inactive IDs. `"any"` excludes
        `closed`. Public clients cannot select `closed` or `archivized`.
    PublicGetComboIdsResponse:
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
            $ref: '#/components/schemas/combo_id'
      required:
        - result
        - jsonrpc
      type: object
    combo_id:
      example: BTC-FS-31DEC21-PERP
      type: string
      description: Unique combo identifier

````

## Related topics

- [public/get_combo_details](https://docs.deribit.com/api-reference/combo-books/public-get_combo_details.md)
- [public/get_combos](https://docs.deribit.com/api-reference/combo-books/public-get_combos.md)
- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [Security Definition Request(c) (Production FIX API)](https://docs.deribit.com/fix-api/production/security-definition-request.md)
- [public/get_instrument](https://docs.deribit.com/api-reference/market-data/public-get_instrument.md)