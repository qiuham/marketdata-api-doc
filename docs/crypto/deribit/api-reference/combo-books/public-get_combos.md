---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/combo-books/public-get_combos
api_type: JSON-RPC
updated_at: 2026-11-19 19:05:53.211741
---

# public/get_combos

> Retrieves **active** combos for the specified settlement `currency` (`"any"` for every currency). Inactive, closed, and archivized combos are omitted. There is no `state` parameter on this method.

Each result is a combo object (`id`, `legs`, `state`, timestamps, `instrument_id`), not the full instrument spec from `public/get_instrument`. Combo `state` here is the combo-book state (`active`), which is not the same as the instrument order-book `state`.

This is not the same list as `public/get_instruments` with `kind=future_combo` or `kind=option_combo`, which returns visible combo **instruments** (including `locked` / `halted` / `settlement` books) and omits inactive combos.

For IDs including inactive combos, use [public/get_combo_ids](https://docs.deribit.com/api-reference/combo-books/public-get_combo_ids). For one combo, use [public/get_combo_details](https://docs.deribit.com/api-reference/combo-books/public-get_combo_details). Expired or archivized combo names are looked up with `public/get_instrument`, not this method.

**📖 Related Article:** [Options Data Collection Best Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_combos)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/get_combos
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
  /public/get_combos:
    get:
      tags:
        - Combo Books
        - Public
      description: >+
        Retrieves **active** combos for the specified settlement `currency`
        (`"any"` for every currency). Inactive, closed, and archivized combos
        are omitted. There is no `state` parameter on this method.


        Each result is a combo object (`id`, `legs`, `state`, timestamps,
        `instrument_id`), not the full instrument spec from
        `public/get_instrument`. Combo `state` here is the combo-book state
        (`active`), which is not the same as the instrument order-book `state`.


        This is not the same list as `public/get_instruments` with
        `kind=future_combo` or `kind=option_combo`, which returns visible combo
        **instruments** (including `locked` / `halted` / `settlement` books) and
        omits inactive combos.


        For IDs including inactive combos, use
        [public/get_combo_ids](https://docs.deribit.com/api-reference/combo-books/public-get_combo_ids).
        For one combo, use
        [public/get_combo_details](https://docs.deribit.com/api-reference/combo-books/public-get_combo_details).
        Expired or archivized combo names are looked up with
        `public/get_instrument`, not this method.


        **📖 Related Article:** [Options Data Collection Best
        Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_combos)

      parameters:
        - name: currency
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/currency_with_any'
          description: >
            The currency symbol or `"any"` for all.


            **📖 Related Article:** [Using the currency
            Parameter](https://docs.deribit.com/articles/currency-parameter)
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 2
                  method: public/get_combos
                  params:
                    currency: BTC
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicGetCombosResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 2
                    result:
                      - state_timestamp: 1650636265101
                        state: active
                        legs:
                          - instrument_name: BTC-29APR22-39300-C
                            amount: 1
                          - instrument_name: BTC-29APR22-39600-C
                            amount: -1
                        id: BTC-CS-29APR22-39300_39600
                        instrument_id: 28
                        creation_timestamp: 1650636235000
                      - state_timestamp: 1650620605150
                        state: active
                        legs:
                          - instrument_name: BTC-PERPETUAL
                            amount: -1
                          - instrument_name: BTC-29APR22
                            amount: 1
                        id: BTC-FS-29APR22_PERP
                        instrument_id: 27
                        creation_timestamp: 1650620575000
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/get_combos \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 2,
              "method": "public/get_combos",
              "params": {
                "currency": "BTC"
              }
            }'
components:
  schemas:
    currency_with_any:
      enum:
        - BTC
        - ETH
        - USDC
        - USDT
        - EURR
        - any
      type: string
      description: Currency name or `"any"` if don't care
    PublicGetCombosResponse:
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
            $ref: '#/components/schemas/combo'
      required:
        - result
        - jsonrpc
      type: object
    combo:
      properties:
        id:
          $ref: '#/components/schemas/combo_id'
        instrument_id:
          $ref: '#/components/schemas/instrument_id'
        state:
          $ref: '#/components/schemas/combo_state'
        state_timestamp:
          $ref: '#/components/schemas/timestamp'
          description: >-
            Time the combo book last changed state (milliseconds since the UNIX
            epoch).
        creation_timestamp:
          $ref: '#/components/schemas/timestamp'
          description: >-
            Time the combo instrument was created (milliseconds since the UNIX
            epoch).
        legs:
          type: array
          items:
            $ref: '#/components/schemas/combo_leg'
      type: object
      description: >-
        Combo book metadata from `public/get_combos`,
        `public/get_combo_details`, and `private/create_combo`. Not the full
        instrument object returned by `public/get_instrument`.
    combo_id:
      example: BTC-FS-31DEC21-PERP
      type: string
      description: Unique combo identifier
    instrument_id:
      type: integer
      description: Instrument ID
    combo_state:
      enum:
        - active
        - inactive
      type: string
      description: >-
        Combo book state: `"active"` or `"inactive"`. Distinct from the
        instrument order-book `state` (`open`, `locked`, and so on).
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
    combo_leg:
      properties:
        instrument_name:
          $ref: '#/components/schemas/instrument_name'
        amount:
          $ref: '#/components/schemas/combo_leg_amount'
      type: object
    instrument_name:
      example: BTC-PERPETUAL
      type: string
      description: Unique instrument identifier
    combo_leg_amount:
      example: -1
      type: integer
      description: >-
        Size multiplier of a leg. A negative value indicates that the trades on
        given leg are in opposite direction to the combo trades they originate
        from

````

## Related topics

- [public/get_combo_ids](https://docs.deribit.com/api-reference/combo-books/public-get_combo_ids.md)
- [public/get_combo_details](https://docs.deribit.com/api-reference/combo-books/public-get_combo_details.md)
- [public/get_instrument](https://docs.deribit.com/api-reference/market-data/public-get_instrument.md)
- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [private/create_combo](https://docs.deribit.com/api-reference/combo-books/private-create_combo.md)