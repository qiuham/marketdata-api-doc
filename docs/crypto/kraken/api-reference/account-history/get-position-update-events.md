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
source_url: 'https://docs.kraken.com/api-reference/account-history/get-position-update-events'
updated_at: 2026-11-13
---

# Get position update events

> Lists position events for authenticated account.



## OpenAPI

````yaml /openapi/futures-history-rest.yaml get /positions
openapi: 3.1.0
info:
  title: History
  version: '3'
  description: |
    Public history APIs.
servers:
  - url: https://futures.kraken.com/api/history/v3
    description: Kraken Futures
    x-kfOnly: true
security: []
tags:
  - name: Account History
    description: >
      Account History provides account-specific data, including account logs (
      history of all balance and position changes) and history for executions,
      orders, and triggers.


      * The `/account-log` endpoint provides a paginated JSON response, with
      access to all account log history specified by ranges of timestamp or ID.

      * The `/accountlogcsv` endpoint provides a CSV formatted response of
      500,000 rows of most recent account logs.
       See also the websocket feed of account log snapshots
      * The `/executions` endpoint provides a paginated JSON response, with
      access to all private execution history specified by ranges of timestamp
      or ID

      * The `/orders` endpoint provides a paginated JSON response, with access
      to all private order history specified by ranges of timestamp or ID

      * The `/triggers` endpoint provides a paginated JSON response, with access
      to all private trigger history specified by ranges of timestamp or ID
  - name: Market History
paths:
  /positions:
    get:
      tags:
        - Account History
      summary: Get position update events
      description: Lists position events for authenticated account.
      operationId: getPositionEvents
      parameters:
        - $ref: '#/components/parameters/SinceDateFilter'
        - $ref: '#/components/parameters/BeforeDateFilter'
        - $ref: '#/components/parameters/SortOrder'
        - $ref: '#/components/parameters/ContinuationToken'
        - $ref: '#/components/parameters/CountPublic'
        - $ref: '#/components/parameters/IncludeOpenedPositions'
        - $ref: '#/components/parameters/IncludeClosedPositions'
        - $ref: '#/components/parameters/IncludeIncreasedPositions'
        - $ref: '#/components/parameters/IncludeDecreasedPositions'
        - $ref: '#/components/parameters/IncludeReversedPositions'
        - $ref: '#/components/parameters/IncludeNoChangePositions'
        - $ref: '#/components/parameters/IncludeTradePositions'
        - $ref: '#/components/parameters/IncludeFundingRealizationPositions'
        - $ref: '#/components/parameters/IncludeSettlementPositions'
        - $ref: '#/components/parameters/Tradeable'
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  accountUid:
                    type: string
                    format: uuid
                  len:
                    type: integer
                    format: uint64
                  serverTime:
                    type: string
                    format: date-time
                  elements:
                    type: array
                    items:
                      $ref: '#/components/schemas/HistoricalPositionUpdateElement'
                  continuationToken:
                    $ref: '#/components/schemas/NextContinuationToken'
                required:
                  - accountUid
                  - len
                  - elements
      security:
        - general-api-key-read-only: []
          authent: []
components:
  parameters:
    SinceDateFilter:
      name: since
      in: query
      description: Timestamp in milliseconds.
      schema:
        $ref: '#/components/schemas/TimestampMilliseconds'
    BeforeDateFilter:
      name: before
      in: query
      description: Timestamp in milliseconds.
      schema:
        $ref: '#/components/schemas/TimestampMilliseconds'
    SortOrder:
      name: sort
      in: query
      description: |
        Determines the order of events in response(s).

        - `asc` = chronological
        - `desc` = reverse-chronological
      required: false
      schema:
        type: string
        enum:
          - asc
          - desc
        default: desc
        x-exhaustive: true
    ContinuationToken:
      name: continuation_token
      in: query
      description: >
        Opaque token from the `Next-Continuation-Token` header used to continue
        listing events. The

        `sort` parameter must be the same as in the previous request to continue
        listing in the same

        direction.
      schema:
        type: string
        format: base64
    CountPublic:
      name: count
      in: query
      description: >
        The maximum number of results to return. Larger values are not rejected,
        they are silently

        capped at 1000; when more events match, the `Next-Continuation-Token`
        header is returned to

        continue the listing.
      schema:
        type: integer
        format: int64
        minimum: 1
        x-rustType: usize
    IncludeOpenedPositions:
      name: opened
      in: query
      schema:
        type: boolean
      description: >
        True if results should include opened position events. Setting this to

        false has no effect.


        If multiple position change filters
        (opened/closed/increased/decreased/reversed/no_change)

        are provided, then positions matching any of these will be included.


        When combined with update reason filters
        (trades/funding_realization/settlement),

        positions must match at least one position change filter AND at least
        one

        update reason filter.


        If no filters are provided for the request, all position events will be
        included.
      required: false
    IncludeClosedPositions:
      name: closed
      in: query
      schema:
        type: boolean
      description: >
        True if results should include closed position events. Setting this to

        false has no effect.


        If multiple position change filters
        (opened/closed/increased/decreased/reversed/no_change)

        are provided, then positions matching any of these will be included.


        When combined with update reason filters
        (trades/funding_realization/settlement),

        positions must match at least one position change filter AND at least
        one

        update reason filter.


        If no filters are provided for the request, all position events will be
        included.
      required: false
    IncludeIncreasedPositions:
      name: increased
      in: query
      schema:
        type: boolean
      description: >
        True if results should include increased position events. Setting this
        to

        false has no effect.


        If multiple position change filters
        (opened/closed/increased/decreased/reversed/no_change)

        are provided, then positions matching any of these will be included.


        When combined with update reason filters
        (trades/funding_realization/settlement),

        positions must match at least one position change filter AND at least
        one

        update reason filter.


        If no filters are provided for the request, all position events will be
        included.
      required: false
    IncludeDecreasedPositions:
      name: decreased
      in: query
      schema:
        type: boolean
      description: >
        True if results should include decreased position events. Setting this
        to

        false has no effect.


        If multiple position change filters
        (opened/closed/increased/decreased/reversed/no_change)

        are provided, then positions matching any of these will be included.


        When combined with update reason filters
        (trades/funding_realization/settlement),

        positions must match at least one position change filter AND at least
        one

        update reason filter.


        If no filters are provided for the request, all position events will be
        included.
      required: false
    IncludeReversedPositions:
      name: reversed
      in: query
      schema:
        type: boolean
      description: >
        True if results should include reversed position events. Setting this to

        false has no effect.


        If multiple position change filters
        (opened/closed/increased/decreased/reversed/no_change)

        are provided, then positions matching any of these will be included.


        When combined with update reason filters
        (trades/funding_realization/settlement),

        positions must match at least one position change filter AND at least
        one

        update reason filter.


        If no filters are provided for the request, all position events will be
        included.
      required: false
    IncludeNoChangePositions:
      name: no_change
      in: query
      schema:
        type: boolean
      description: >
        True if results should include "no change" position events - where the

        position has not changed. Setting this to false has no effect.


        If multiple position change filters
        (opened/closed/increased/decreased/reversed/no_change)

        are provided, then positions matching any of these will be included.


        When combined with update reason filters
        (trades/funding_realization/settlement),

        positions must match at least one position change filter AND at least
        one

        update reason filter.


        If no filters are provided for the request, all position events will be
        included.
      required: false
    IncludeTradePositions:
      name: trades
      in: query
      schema:
        type: boolean
      description: >
        True if results should include position events caused by a trade.

        Setting this to false has no effect.


        If multiple update reason filters
        (trades/funding_realization/settlement)

        are provided, then positions matching any of these will be included.


        When combined with position change filters
        (opened/closed/increased/decreased/reversed/no_change),

        positions must match at least one update reason filter AND at least one

        position change filter.


        If no filters are provided for the request, all position events will be
        included.
      required: false
    IncludeFundingRealizationPositions:
      name: funding_realization
      in: query
      schema:
        type: boolean
      description: >
        True if results should include position events caused by a funding

        realisation. Setting this to false has no effect.


        If multiple update reason filters
        (trades/funding_realization/settlement)

        are provided, then positions matching any of these will be included.


        When combined with position change filters
        (opened/closed/increased/decreased/reversed/no_change),

        positions must match at least one update reason filter AND at least one

        position change filter.


        If no filters are provided for the request, all position events will be
        included.
      required: false
    IncludeSettlementPositions:
      name: settlement
      in: query
      schema:
        type: boolean
      description: >
        True if results should include position events caused by a settlement.

        Setting this to false has no effect.


        If multiple update reason filters
        (trades/funding_realization/settlement)

        are provided, then positions matching any of these will be included.


        When combined with position change filters
        (opened/closed/increased/decreased/reversed/no_change),

        positions must match at least one update reason filter AND at least one

        position change filter.


        If no filters are provided for the request, all position events will be
        included.
      required: false
    Tradeable:
      description: If present events of other tradeables are filtered out.
      name: tradeable
      in: query
      required: false
      schema:
        type: string
  schemas:
    HistoricalPositionUpdateElement:
      type: object
      properties:
        uid:
          type: string
        timestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
        event:
          $ref: '#/components/schemas/HistoricalPositionUpdateEvent'
      required:
        - uid
        - timestamp
        - event
    NextContinuationToken:
      description: >
        Opaque token to pass to the next request to continue listing events. The
        `sort` parameter

        must be the same as in the previous request to continue listing in the
        same direction.
      type: string
      format: base64
    TimestampMilliseconds:
      type: integer
      format: timestamp-milliseconds
      example: 1604937694000
    HistoricalPositionUpdateEvent:
      type: object
      properties:
        PositionUpdate:
          $ref: '#/components/schemas/HistoricalPositionUpdate'
      required:
        - PositionUpdate
    HistoricalPositionUpdate:
      type: object
      properties:
        accountUid:
          description: Account UID
          type: string
        tradeable:
          type: string
        oldPosition:
          type: string
        oldAverageEntryPrice:
          type:
            - string
            - 'null'
        newPosition:
          type: string
        newAverageEntryPrice:
          type: string
        fillTime:
          type:
            - integer
            - 'null'
          format: timestamp-milliseconds
        fee:
          type: string
        feeCurrency:
          type: string
        realizedPnL:
          type: string
        positionChange:
          type: string
          description: >
            `unknown` is returned when the source value couldn't be decoded;
            this will be replaced with a real value as soon as possible.
          enum:
            - open
            - close
            - increase
            - decrease
            - reverse
            - noChange
            - unknown
        executionUid:
          type: string
        executionPrice:
          type: string
        executionSize:
          type: string
        tradeType:
          type: string
          description: >
            `unknown` is returned when the source value couldn't be decoded;
            this will be replaced with a real value as soon as possible.
          enum:
            - userExecution
            - liquidation
            - partialLiquidation
            - assignment
            - unwind
            - unknown
        fundingRealizationTime:
          type: integer
          format: timestamp-milliseconds
        realizedFunding:
          type: string
        settlementPrice:
          type: string
        timestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
        updateReason:
          type: string
          description: >
            `unknown` is returned when the source value couldn't be decoded;
            this will be replaced with a real value as soon as possible.
          enum:
            - trade
            - fundingRealisation
            - settlement
            - unknown
      required:
        - accountUid
        - tradeable
        - oldPosition
        - newPosition
        - newAverageEntryPrice
        - positionChange
        - timestamp
        - updateReason
  securitySchemes:
    general-api-key-read-only:
      type: apiKey
      description: General API key with at least **read-only** access
      in: header
      name: APIKey
      x-inlineDescription: true
    authent:
      type: apiKey
      description: Authentication string
      in: header
      name: Authent
      x-inlineDescription: true

````
