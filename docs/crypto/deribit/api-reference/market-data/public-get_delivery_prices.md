---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/market-data/public-get_delivery_prices
api_type: JSON-RPC
updated_at: 2026-11-18 18:59:16.798712
---

# public/get_delivery_prices

> Retrieves historical delivery prices for a given index. Delivery prices are the settlement prices used when futures or options contracts expire and are settled.

Results can be paginated using the `offset` and `count` parameters. Optionally, results can be limited to a date range using `start_timestamp` and `end_timestamp` — each is mapped to the UTC calendar date of the delivery and both bounds are inclusive; `records_total` reflects the filtered set. This method is useful for analyzing historical settlement prices and understanding how contracts have been settled over time.

**📖 Related Article:** [Options Data Collection Best Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_delivery_prices)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/get_delivery_prices
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
  /public/get_delivery_prices:
    get:
      tags:
        - Market Data
      description: >+
        Retrieves historical delivery prices for a given index. Delivery prices
        are the settlement prices used when futures or options contracts expire
        and are settled.


        Results can be paginated using the `offset` and `count` parameters.
        Optionally, results can be limited to a date range using
        `start_timestamp` and `end_timestamp` — each is mapped to the UTC
        calendar date of the delivery and both bounds are inclusive;
        `records_total` reflects the filtered set. This method is useful for
        analyzing historical settlement prices and understanding how contracts
        have been settled over time.


        **📖 Related Article:** [Options Data Collection Best
        Practices](https://docs.deribit.com/articles/options-data-collection-best-practices)


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_delivery_prices)

      parameters:
        - name: index_name
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/index_name'
          description: Index identifier, matches (base) cryptocurrency with quote currency
        - name: offset
          in: query
          required: false
          schema:
            example: 10
            type: integer
          description: The offset for pagination, default - `0`
        - name: count
          required: false
          in: query
          schema:
            type: integer
            maximum: 1000
            minimum: 1
          description: Number of requested items, default - `10`, maximum - `1000`
        - name: start_timestamp
          required: false
          in: query
          schema:
            $ref: '#/components/schemas/timestamp'
          description: >-
            The earliest timestamp to return result from (milliseconds since the
            UNIX epoch)
        - name: end_timestamp
          required: false
          in: query
          schema:
            $ref: '#/components/schemas/timestamp'
          description: >-
            The most recent timestamp to return result from (milliseconds since
            the UNIX epoch)
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 3601
                  method: public/get_delivery_prices
                  params:
                    index_name: btc_usd
                    offset: 0
                    count: 5
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicGetDeliveryPricesResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 3601
                    result:
                      data:
                        - date: '2020-01-02'
                          delivery_price: 7131.214606410254
                        - date: '2019-12-21'
                          delivery_price: 7150.943217777777
                        - date: '2019-12-20'
                          delivery_price: 7175.988445532345
                        - date: '2019-12-19'
                          delivery_price: 7189.540776143791
                        - date: '2019-12-18'
                          delivery_price: 6698.353743857118
                      records_total: 58
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/get_delivery_prices \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 3601,
              "method": "public/get_delivery_prices",
              "params": {
                "index_name": "btc_usd",
                "offset": 0,
                "count": 5
              }
            }'
components:
  schemas:
    index_name:
      enum:
        - btc_usd
        - eth_usd
        - ada_usdc
        - algo_usdc
        - avax_usdc
        - bch_usdc
        - bnb_usdc
        - btc_usdc
        - btcdvol_usdc
        - buidl_usdc
        - doge_usdc
        - dot_usdc
        - eurr_usdc
        - eth_usdc
        - ethdvol_usdc
        - hype_usdc
        - link_usdc
        - ltc_usdc
        - near_usdc
        - paxg_usdc
        - shib_usdc
        - sol_usdc
        - steth_usdc
        - ton_usdc
        - trump_usdc
        - trx_usdc
        - uni_usdc
        - usde_usdc
        - usyc_usdc
        - xrp_usdc
        - btc_usdt
        - eth_usdt
        - eurr_usdt
        - sol_usdt
        - steth_usdt
        - usdc_usdt
        - usde_usdt
        - btc_eurr
        - btc_usde
        - btc_usyc
        - eth_btc
        - eth_eurr
        - eth_usde
        - eth_usyc
        - steth_eth
        - paxg_btc
        - drbfix-btc_usdc
        - drbfix-eth_usdc
      type: string
      description: Index identifier, matches (base) cryptocurrency with quote currency
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
    PublicGetDeliveryPricesResponse:
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
          type: object
          properties:
            records_total:
              type: number
              example: 120
              description: Available delivery prices
            data:
              type: array
              items:
                type: object
                properties:
                  date:
                    $ref: '#/components/schemas/date'
                  delivery_price:
                    $ref: '#/components/schemas/delivery_price'
                required:
                  - date
                  - delivery_price
          required:
            - records_total
            - data
      required:
        - result
        - jsonrpc
      type: object
    date:
      example: '2019-11-24'
      type: string
      description: The event date with year, month and day
    delivery_price:
      type: number
      description: The settlement price for the instrument. Only when `state = closed`

````

## Related topics

- [Market Data Collection](https://docs.deribit.com/articles/market-data-collection-best-practices.md)
- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md)
- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [public/get_index_price](https://docs.deribit.com/api-reference/market-data/public-get_index_price.md)
- [public/get_index_price_names](https://docs.deribit.com/api-reference/market-data/public-get_index_price_names.md)