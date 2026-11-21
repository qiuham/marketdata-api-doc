---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/market-data/public-get_book_summary_by_instrument
api_type: JSON-RPC
updated_at: 2026-11-21 19:01:41.566153
---

# public/get_book_summary_by_instrument

> Retrieves summary information such as open interest, 24-hour volume, best bid/ask prices, last trade price, mark price, and other market statistics for a specific instrument.

**Note:** `open_interest` is always reported with an 8-hour delay, regardless of trade type (on-screen, Block Trade or Block RFQ). `volume` equals `volume_realtime` plus `volume_delayed`; `volume_delayed` covers Block RFQ trades with delayed publication and is reported 8 hours late.

This method provides a quick overview of current market activity and liquidity for a single instrument.

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_book_summary_by_instrument)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/get_book_summary_by_instrument
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
  /public/get_book_summary_by_instrument:
    get:
      tags:
        - Market Data
        - Public
      description: >+
        Retrieves summary information such as open interest, 24-hour volume,
        best bid/ask prices, last trade price, mark price, and other market
        statistics for a specific instrument.


        **Note:** `open_interest` is always reported with an 8-hour delay,
        regardless of trade type (on-screen, Block Trade or Block RFQ). `volume`
        equals `volume_realtime` plus `volume_delayed`; `volume_delayed` covers
        Block RFQ trades with delayed publication and is reported 8 hours late.


        This method provides a quick overview of current market activity and
        liquidity for a single instrument.


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Fget_book_summary_by_instrument)

      parameters:
        - name: instrument_name
          required: true
          in: query
          schema:
            $ref: '#/components/schemas/instrument_name'
          description: Instrument name
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 3659
                  method: public/get_book_summary_by_instrument
                  params:
                    instrument_name: ETH-22FEB19-140-P
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicGetBookSummaryResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 3659
                    result:
                      - volume: 0.55
                        volume_realtime: 0.55
                        volume_delayed: 0
                        volume_usd: 66.76
                        volume_realtime_usd: 66.76
                        volume_delayed_usd: 0
                        underlying_price: 121.38
                        underlying_index: index_price
                        quote_currency: USD
                        price_change: -26.7793594
                        open_interest: 0.55
                        mid_price: 0.2444
                        mark_price: 80
                        low: 0.34
                        last: 0.34
                        interest_rate: 0.207
                        instrument_name: ETH-22FEB19-140-P
                        high: 0.34
                        creation_timestamp: 1550227952163
                        bid_price: 0.1488
                        base_currency: ETH
                        ask_price: 0.34
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/get_book_summary_by_instrument \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 3659,
              "method": "public/get_book_summary_by_instrument",
              "params": {
                "instrument_name": "ETH-22FEB19-140-P"
              }
            }'
components:
  schemas:
    instrument_name:
      example: BTC-PERPETUAL
      type: string
      description: Unique instrument identifier
    PublicGetBookSummaryResponse:
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
            $ref: '#/components/schemas/book_summary'
      required:
        - result
        - jsonrpc
      type: object
    book_summary:
      properties:
        instrument_name:
          $ref: '#/components/schemas/instrument_name'
        high:
          example: 7022.89
          type: number
          nullable: true
          description: Price of the 24h highest trade
        low:
          example: 7022.89
          type: number
          nullable: true
          description: Price of the 24h lowest trade, `null` if there weren't any trades
        base_currency:
          example: ETH
          type: string
          description: Base currency
        quote_currency:
          example: USD
          type: string
          description: Quote currency
        volume:
          example: 223
          type: number
          description: >-
            The total 24h traded volume (in base currency). Equals
            `volume_realtime` plus `volume_delayed`.
        volume_realtime:
          $ref: '#/components/schemas/volume_realtime'
        volume_delayed:
          $ref: '#/components/schemas/volume_delayed'
        bid_price:
          example: 7022.89
          type: number
          nullable: true
          description: The current best bid price, `null` if there aren't any bids
        ask_price:
          example: 7022.89
          type: number
          nullable: true
          description: The current best ask price, `null` if there aren't any asks
        mid_price:
          example: 7022.89
          type: number
          nullable: true
          description: >-
            The average of the best bid and ask, `null` if there aren't any asks
            or bids
        mark_price:
          example: 7022.89
          type: number
          description: The current instrument market price
        last:
          example: 7022.89
          type: number
          nullable: true
          description: The price of the latest trade, `null` if there weren't any trades
        open_interest:
          example: 0.5
          type: number
          description: >-
            Optional (only for derivatives). The total amount of outstanding
            contracts in the corresponding amount units. For perpetual and
            inverse futures the amount is in USD units. For options and linear
            futures it is the underlying base currency coin. Always reported
            with an 8-hour delay, i.e. the open interest as of 8 hours ago,
            regardless of trade type (on-screen, Block Trade or Block RFQ).
        creation_timestamp:
          $ref: '#/components/schemas/timestamp'
        estimated_delivery_price:
          example: 11628.81
          type: number
          description: >-
            Optional (only for derivatives). Estimated delivery price for the
            market.
        volume_usd:
          type: number
          description: Volume in USD
        volume_realtime_usd:
          $ref: '#/components/schemas/volume_realtime_usd'
        volume_delayed_usd:
          $ref: '#/components/schemas/volume_delayed_usd'
        volume_notional:
          type: number
          description: Volume in quote currency (futures and spots only)
        volume_realtime_notional:
          $ref: '#/components/schemas/volume_realtime_notional'
        volume_delayed_notional:
          $ref: '#/components/schemas/volume_delayed_notional'
        current_funding:
          type: number
          example: 0.12344
          description: >-
            Current instantaneous funding rate (perpetual only). Calculated as
            `(mark_price − index_price) / index_price` at this moment. This is
            the rate that would apply if a funding settlement occurred right
            now.
        funding_8h:
          type: number
          description: >-
            Projected 8-hour funding rate for the current settlement window
            (perpetual only). This is the time-weighted accumulation of the
            funding rate since the last 8-hour settlement — i.e. the total rate
            that will be charged or received at the next settlement.
            `current_funding` shows the instantaneous rate; `funding_8h` shows
            what has accumulated toward the next settlement.
        mark_iv:
          $ref: '#/components/schemas/mark_iv'
        interest_rate:
          example: 0
          type: number
          description: Interest rate used in implied volatility calculations (options only)
        underlying_index:
          example: index_price
          type: string
          description: Name of the underlying future, or `'index_price'` (options only)
        underlying_price:
          example: 6745.34
          type: number
          description: underlying price for implied volatility calculations (options only)
        price_change:
          example: 10.23
          type: number
          nullable: true
          description: >-
            24-hour price change expressed as a percentage, `null` if there
            weren't any trades
      required:
        - instrument_name
        - high
        - low
        - base_currency
        - quote_currency
        - volume
        - bid_price
        - ask_price
        - mid_price
        - mark_price
        - last
        - creation_timestamp
      type: object
    volume_realtime:
      type: number
      description: >-
        24-hour volume in base currency of trades published in real time, i.e.
        all trades except Block RFQ trades with delayed publication.
    volume_delayed:
      type: number
      description: >-
        24-hour volume in base currency of Block RFQ trades with delayed
        publication. Delayed volume is reported 8 hours late: it covers delayed
        Block RFQ trades executed between 32 and 8 hours ago.
    timestamp:
      example: 1536569522277
      type: integer
      description: The timestamp (milliseconds since the Unix epoch)
    volume_realtime_usd:
      type: number
      description: >-
        24-hour volume in USD of trades published in real time; returned
        together with `volume_usd`.
    volume_delayed_usd:
      type: number
      description: >-
        24-hour volume in USD of Block RFQ trades with delayed publication,
        reported 8 hours late like `volume_delayed`; returned together with
        `volume_usd`.
    volume_realtime_notional:
      type: number
      description: >-
        24-hour volume in quote currency of trades published in real time;
        returned together with `volume_notional`.
    volume_delayed_notional:
      type: number
      description: >-
        24-hour volume in quote currency of Block RFQ trades with delayed
        publication, reported 8 hours late like `volume_delayed`; returned
        together with `volume_notional`.
    mark_iv:
      type: number
      description: (Only for option) implied volatility for mark price

````

## Related topics

- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md)
- [Starbase Reference Data and Instrument Definitions](https://docs.deribit.com/starbase/reference-data.md)
- [public/get_book_summary_by_currency](https://docs.deribit.com/api-reference/market-data/public-get_book_summary_by_currency.md)
- [public/get_order_book_by_instrument_id](https://docs.deribit.com/api-reference/market-data/public-get_order_book_by_instrument_id.md)
- [public/get_combos](https://docs.deribit.com/api-reference/combo-books/public-get_combos.md)