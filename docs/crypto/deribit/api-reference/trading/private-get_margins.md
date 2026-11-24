---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/trading/private-get_margins
api_type: JSON-RPC
updated_at: 2026-11-24 18:59:53.833268
---

# private/get_margins

> Calculates margin requirements for a hypothetical order on a given instrument. Returns initial margin and maintenance margin for the specified instrument, quantity, and price.

This method is useful for estimating margin requirements before placing an order, helping to ensure sufficient funds are available and understanding the margin impact of potential trades.

For spot instruments, `amount_type` selects whether `amount` is a base currency quantity (fees charged on top) or a total quote currency spend (fees included).

**📖 Related Article:** [Using the currency Parameter](https://docs.deribit.com/articles/currency-parameter)

**Scope:** `trade:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_margins)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_margins
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
  /private/get_margins:
    get:
      tags:
        - Trading
        - Private
      description: >+
        Calculates margin requirements for a hypothetical order on a given
        instrument. Returns initial margin and maintenance margin for the
        specified instrument, quantity, and price.


        This method is useful for estimating margin requirements before placing
        an order, helping to ensure sufficient funds are available and
        understanding the margin impact of potential trades.


        For spot instruments, `amount_type` selects whether `amount` is a base
        currency quantity (fees charged on top) or a total quote currency spend
        (fees included).


        **📖 Related Article:** [Using the currency
        Parameter](https://docs.deribit.com/articles/currency-parameter)


        **Scope:** `trade:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_margins)

      parameters:
        - name: instrument_name
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/instrument_name'
          description: Instrument name
        - name: amount
          in: query
          schema:
            type: number
          required: true
          description: >-
            It represents the requested order size. For perpetual and inverse
            futures the amount is in USD units. For options and linear futures
            it is the underlying base currency coin. For spot instruments the
            unit is controlled by `amount_type`.
        - name: amount_type
          in: query
          schema:
            type: string
            enum:
              - base
              - quote
            default: base
          required: false
          description: >
            How the `amount` parameter is interpreted. Spot instruments only.


            `base` (the default) reads `amount` as a quantity of the base
            currency, with fees charged on top of it. `quote` reads `amount` as
            a total spend in the quote currency, with fees included in it. For
            every spot order the matching base amounts are returned in
            `taker_base_amount` and `maker_base_amount`.


            Because the taker and maker fee rates differ, a fee-inclusive spend
            buys a slightly different quantity in each role. Both quantities are
            floored to a whole multiple of the instrument's `min_trade_amount`,
            so the cost plus the fee never exceeds the requested spend. Where
            the fee rate is negative (a maker rebate) the cost alone exceeds the
            spend and the rebate brings the total back within it.


            In `quote` mode the `buy` field reports the taker notional. The
            maker notional differs, and the fee-inclusive maker total is in
            `maker_margin_required`.


            On the sell side the spend is the gross proceeds: the base amount
            sold is worth exactly that, and the fee is deducted from what is
            received. The sell quantity does not depend on the fee role, so it
            is the same in `taker_base_amount` and `maker_base_amount`.
        - in: query
          name: price
          required: true
          schema:
            type: number
            example: 3725
          description: Price
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 7
                  method: private/get_margins
                  params:
                    instrument_name: BTC-PERPETUAL
                    amount: 10000
                    price: 3725
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateGetMarginsResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 7
                    result:
                      sell: 0
                      min_price: 3684.8
                      max_price: 3759.24
                      buy: 0.0219949
                      buy_taker_fee: 0.000085
                      buy_maker_fee: 0.000017
                      sell_taker_fee: 0.000085
                      sell_maker_fee: 0.000017
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_margins \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 7,
              "method": "private/get_margins",
              "params": {
                "instrument_name": "BTC-PERPETUAL",
                "amount": 10000,
                "price": 3725
              }
            }'
components:
  schemas:
    instrument_name:
      example: BTC-PERPETUAL
      type: string
      description: Unique instrument identifier
    PrivateGetMarginsResponse:
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
          properties:
            buy:
              example: 0.01681367
              type: number
              description: >-
                Margin when buying. For spot instruments with `amount_type` set
                to `quote` this is the taker notional; the fee-inclusive maker
                total is in `maker_margin_required`.
            sell:
              example: 0.01680479
              type: number
              description: Margin when selling
            buy_taker_fee:
              example: 0.000017
              type: number
              description: Estimated fee when buying as a taker
            buy_maker_fee:
              example: 0.000017
              type: number
              description: Estimated fee when buying as a maker
            sell_taker_fee:
              example: 0.000017
              type: number
              description: Estimated fee when selling as a taker
            sell_maker_fee:
              example: 0.000017
              type: number
              description: Estimated fee when selling as a maker
            min_price:
              $ref: '#/components/schemas/min_price'
            max_price:
              $ref: '#/components/schemas/max_price'
            taker_base_amount:
              type: object
              properties:
                buy:
                  example: 0.0009
                  type: number
                  description: Base currency amount bought
                sell:
                  example: 0.001
                  type: number
                  description: Base currency amount sold
              description: >-
                Base currency amount a taker order would trade. Spot only. When
                `amount_type` is `base` this equals the requested `amount` on
                both sides. When `amount_type` is `quote` the buy side is
                derived so cost plus the taker fee comes to the spend.
            maker_base_amount:
              type: object
              properties:
                buy:
                  example: 0.0009
                  type: number
                  description: Base currency amount bought
                sell:
                  example: 0.001
                  type: number
                  description: Base currency amount sold
              description: >-
                Base currency amount a maker order would trade. Spot only.
                Equals `taker_base_amount` when `amount_type` is `base`. When
                `amount_type` is `quote` the buy side differs because the maker
                fee rate differs; the sell side is always identical.
          required:
            - buy
            - sell
            - buy_taker_fee
            - buy_maker_fee
            - sell_taker_fee
            - sell_maker_fee
            - min_price
            - max_price
          type: object
      required:
        - result
        - jsonrpc
      type: object
    min_price:
      type: number
      description: >-
        The minimum price for the future. Any sell orders you submit lower than
        this price will be clamped to this minimum.
    max_price:
      type: number
      description: >-
        The maximum price for the future. Any buy orders you submit higher than
        this price, will be clamped to this maximum.

````

## Related topics

- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Using the currency Parameter](https://docs.deribit.com/articles/currency-parameter.md)
- [private/get_position](https://docs.deribit.com/api-reference/account-management/private-get_position.md)
- [private/get_order_margin_by_ids](https://docs.deribit.com/api-reference/trading/private-get_order_margin_by_ids.md)
- [private/get_subaccounts](https://docs.deribit.com/api-reference/account-management/private-get_subaccounts.md)