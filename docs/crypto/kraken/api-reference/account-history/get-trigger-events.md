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
source_url: 'https://docs.kraken.com/api-reference/account-history/get-trigger-events'
updated_at: 2026-11-13
---

# Get trigger events

> Lists trigger events for authenticated account.




## OpenAPI

````yaml /openapi/futures-history-rest.yaml get /triggers
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
  /triggers:
    get:
      tags:
        - Account History
      summary: Get trigger events
      description: |
        Lists trigger events for authenticated account.
      operationId: getTriggerEvents
      parameters:
        - $ref: '#/components/parameters/SinceDateFilter'
        - $ref: '#/components/parameters/BeforeDateFilter'
        - $ref: '#/components/parameters/SortOrder'
        - $ref: '#/components/parameters/ContinuationToken'
        - $ref: '#/components/parameters/CountPublic'
        - $ref: '#/components/parameters/Tradeable'
        - $ref: '#/components/parameters/OpenedTrigger'
        - $ref: '#/components/parameters/ClosedTrigger'
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
                      $ref: '#/components/schemas/HistoricalTriggerElement'
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
    Tradeable:
      description: If present events of other tradeables are filtered out.
      name: tradeable
      in: query
      required: false
      schema:
        type: string
    OpenedTrigger:
      name: opened
      in: query
      schema:
        type: boolean
      description: >
        Determines status of the triggers that should be included in
        response(s).


        - `true` = return triggers that have been placed within given time
        range.

        - `false` = don't return triggers that have been placed within given
        time range.
      required: false
    ClosedTrigger:
      name: closed
      in: query
      schema:
        type: boolean
      description: >
        Determines status of the trigger that should be included in response(s).


        - `true` = return triggers that have been closed/cancelled/rejected
        within given time range.

        - `false` = don't return triggers that have been
        closed/cancelled/rejected within given time range.
      required: false
  schemas:
    HistoricalTriggerElement:
      type: object
      properties:
        uid:
          type: string
        timestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
        event:
          $ref: '#/components/schemas/HistoricalTriggerEvent'
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
    HistoricalTriggerEvent:
      type: object
      oneOf:
        - type: object
          properties:
            OrderTriggerPlaced:
              $ref: '#/components/schemas/TriggerPlaced'
          required:
            - OrderTriggerPlaced
        - type: object
          properties:
            OrderTriggerCancelled:
              $ref: '#/components/schemas/TriggerCancelled'
          required:
            - OrderTriggerCancelled
        - type: object
          properties:
            OrderTriggerUpdated:
              $ref: '#/components/schemas/TriggerUpdated'
          required:
            - OrderTriggerUpdated
        - type: object
          properties:
            OrderTriggerActivated:
              $ref: '#/components/schemas/TriggerActivated'
          required:
            - OrderTriggerActivated
        - type: object
          properties:
            OrderTriggerEditRejected:
              $ref: '#/components/schemas/TriggerEditRejected'
          required:
            - OrderTriggerEditRejected
    TriggerPlaced:
      type: object
      properties:
        order:
          $ref: '#/components/schemas/HistoricalTrigger'
        reason:
          type: string
      required:
        - order
        - reason
    TriggerCancelled:
      type: object
      properties:
        order:
          $ref: '#/components/schemas/HistoricalTrigger'
        reason:
          type: string
      required:
        - order
        - reason
    TriggerUpdated:
      type: object
      properties:
        oldOrderTrigger:
          $ref: '#/components/schemas/HistoricalTrigger'
        newOrderTrigger:
          $ref: '#/components/schemas/HistoricalTrigger'
        reason:
          type: string
      required:
        - oldOrderTrigger
        - newOrderTrigger
        - reason
    TriggerActivated:
      type: object
      properties:
        order:
          $ref: '#/components/schemas/HistoricalTrigger'
      required:
        - order
    TriggerEditRejected:
      type: object
      properties:
        attemptedOrderTrigger:
          $ref: '#/components/schemas/HistoricalTrigger'
        oldOrderTrigger:
          $ref: '#/components/schemas/HistoricalTrigger'
        reason:
          type: string
        orderError:
          type: string
      required:
        - attemptedOrderTrigger
        - oldOrderTrigger
        - reason
        - orderError
    HistoricalTrigger:
      type: object
      properties:
        uid:
          type: string
          format: uuid
        accountId:
          type: number
          format: uint64
        accountUid:
          type: string
          format: uuid
        tradeable:
          type: string
        direction:
          description: >
            `Unknown` is returned when the source value couldn't be decoded;
            this will be replaced with a real value as soon as possible.
          type: string
          enum:
            - Buy
            - Sell
            - Unknown
        quantity:
          $ref: '#/components/schemas/Decimal'
        timestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
        limitPrice:
          $ref: '#/components/schemas/Decimal'
        orderType:
          type: string
        clientId:
          type: string
        reduceOnly:
          type: boolean
        lastUpdateTimestamp:
          $ref: '#/components/schemas/TimestampMilliseconds'
        triggerOptions:
          $ref: '#/components/schemas/TriggerOptions'
      required:
        - uid
        - accountId
        - accountUid
        - tradeable
        - direction
        - quantity
        - timestamp
        - limitPrice
        - orderType
        - clientId
        - reduceOnly
        - lastUpdateTimestamp
        - triggerOptions
    Decimal:
      type: string
      format: decimal
      example: '1234.56789'
    TriggerOptions:
      type: object
      properties:
        triggerPrice:
          $ref: '#/components/schemas/Decimal'
        triggerSignal:
          description: >
            `Unknown` is returned when the source value couldn't be decoded;
            this will be replaced with a real value as soon as possible.
          type: string
          enum:
            - MarkPrice
            - LastPrice
            - SpotPrice
            - Unknown
        triggerSide:
          description: >
            `Unknown` is returned when the source value couldn't be decoded;
            this will be replaced with a real value as soon as possible.
          type: string
          enum:
            - Above
            - Below
            - Unknown
        trailingStopOptions:
          $ref: '#/components/schemas/TrailingStopOptions'
        limitPriceOffset:
          $ref: '#/components/schemas/PriceOffset'
      required:
        - triggerPrice
        - triggerSignal
        - triggerSide
        - trailingStopOptions
        - limitPriceOffset
    TrailingStopOptions:
      type: object
      properties:
        maxDeviation:
          $ref: '#/components/schemas/Decimal'
        unit:
          description: >
            `Unknown` is returned when the source value couldn't be decoded;
            this will be replaced with a real value as soon as possible.
          type: string
          enum:
            - Percent
            - QuoteCurrency
            - Unknown
      required:
        - maxDeviation
        - unit
    PriceOffset:
      type: object
      properties:
        priceOffset:
          $ref: '#/components/schemas/Decimal'
        unit:
          description: >
            `Unknown` is returned when the source value couldn't be decoded;
            this will be replaced with a real value as soon as possible.
          type: string
          enum:
            - Percent
            - QuoteCurrency
            - Unknown
      required:
        - priceOffset
        - unit
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
