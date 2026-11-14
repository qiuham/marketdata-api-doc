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
source_url: 'https://docs.kraken.com/api-reference/order-management/dead-mans-switch'
updated_at: 2026-11-13
---

# Dead man's switch

> This endpoint provides a Dead Man's Switch mechanism to protect the user from network malfunctions. The user can send a request with a timeout in seconds which will trigger a countdown timer that will cancel all user orders when timeout expires. The user has to keep sending request to push back the timeout expiration or they can deactivate the mechanism by specifying a timeout of zero (0).

The recommended mechanism usage is making a call every 15 to 20 seconds and provide a timeout of 60 seconds. This allows the user to keep the orders in place on a brief network failure, while keeping them safe in case of a network breakdown.



## OpenAPI

````yaml /openapi/futures-rest.yaml post /cancelallordersafter
openapi: 3.1.0
info:
  title: Kraken Futures Trading API
  version: v3
  description: Market data and order management endpoints.
servers:
  - url: https://futures.kraken.com/derivatives/api/v3
    description: Kraken Futures
    x-kfOnly: true
security: []
tags:
  - name: Multi-Collateral
    description: Endpoints pertaining to the multi-collateral (MC) futures markets.
  - name: Instrument Details
    description: >-
      - The `/instruments/status` endpoint provides a list of statuses for all
      instruments.

      - The `/instruments/{symbol}/status` endpoint provides the status of a
      single instrument.
  - name: Account Information
  - name: Assignment Program
  - name: Fee Schedules
    description: >-
      **DEPRECATED** — Effective 2026-06-22, the fee values returned by these

      endpoints no longer reflect the fees actually charged on Futures trades.

      Futures fee calculation has been migrated to a centralised Kraken fee

      service.


      To determine the fee rate applied to your trades, use the Spot

      [`GetTradeVolume`](https://docs.kraken.com/api/docs/rest-api/get-trade-volume)

      endpoint authenticated with a Spot API key.
  - name: General
  - name: Historical Data
  - name: Historical Funding Rates
  - name: Market Data
  - name: Order Management
  - name: Trading Settings
  - name: Subaccounts
  - name: Transfers
  - name: RFQs
paths:
  /cancelallordersafter:
    post:
      tags:
        - Order Management
      summary: Dead man's switch
      description: >-
        This endpoint provides a Dead Man's Switch mechanism to protect the user
        from network malfunctions. The user can send a request with a timeout in
        seconds which will trigger a countdown timer that will cancel all user
        orders when timeout expires. The user has to keep sending request to
        push back the timeout expiration or they can deactivate the mechanism by
        specifying a timeout of zero (0).


        The recommended mechanism usage is making a call every 15 to 20 seconds
        and provide a timeout of 60 seconds. This allows the user to keep the
        orders in place on a brief network failure, while keeping them safe in
        case of a network breakdown.
      operationId: cancelAllOrdersAfter
      parameters:
        - $ref: '#/components/parameters/AlgoId'
        - description: The timeout specified in seconds.
          name: timeout
          in: query
          required: false
          schema:
            type: number
            format: uint32
            example: 60
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - title: Success Response
                    allOf:
                      - type: object
                        properties:
                          status:
                            $ref: '#/components/schemas/DeadManSwitchStatusJson'
                            description: The status of the switch.
                        required:
                          - status
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/CancelAllOrdersAfterSuccessExample'
                cancel:
                  $ref: '#/components/examples/CancelAllOrdersAfterCancelExample'
                failure:
                  $ref: '#/components/examples/CancelAllOrdersAfterFailureExample'
      security:
        - general-api-key: []
          authent: []
components:
  parameters:
    AlgoId:
      description: ID of the algorithm that is making the request.
      name: algoId
      in: header
      required: false
      schema:
        type: string
      x-cfOnly: true
  schemas:
    DeadManSwitchStatusJson:
      type: object
      properties:
        currentTime:
          type: string
          description: The server date and time that server received the request.
        triggerTime:
          type: string
          description: The server date and time that the switch will be activated.
      required:
        - currentTime
        - triggerTime
    SuccessResponse:
      allOf:
        - $ref: '#/components/schemas/ResultSuccess'
        - $ref: '#/components/schemas/ServerTime'
    ErrorResponse:
      allOf:
        - title: Errors
          type: object
          properties:
            errors:
              type: array
              items:
                $ref: '#/components/schemas/Error'
            error:
              $ref: '#/components/schemas/Error'
          required:
            - error
        - $ref: '#/components/schemas/ResultError'
        - $ref: '#/components/schemas/ServerTime'
    ResultSuccess:
      type: object
      properties:
        result:
          type: string
          enum:
            - success
          example: success
      required:
        - result
    ServerTime:
      type: object
      properties:
        serverTime:
          description: Server time in Coordinated Universal Time (UTC)
          type: string
          format: date-time
          example: '2020-08-27T17:03:33.196Z'
      required:
        - serverTime
    Error:
      type: string
      description: |-
        Error description.

          - `accountInactive`: The Futures account the request refers to is inactive
          - `accountNotFound`: The account the transfer request refers to could not be found
          - `apiLimitExceeded`: The API limit for the calling IP address has been exceeded
          - `authenticationError`: The request could not be authenticated
          - `cancelOnly`: The venue is in cancel-only mode and accepts only cancellations until it is lifted
          - `cannotTransferBonusCurrency`: Deprecated and no longer returned, since bonus currency has been removed
          - `cashAccountTypeAccessForbidden`: The account's platform does not give access to the requested wallet
          - `cashAccountTypeNotFound`: The requested wallet does not exist
          - `insufficientFunds`: The amount requested for transfer is below the amount of funds available
          - `invalidAccount`: The Futures account the transfer request refers to is invalid
          - `invalidAmount`: The amount the transfer request refers to is invalid
          - `invalidArgument`: One or more arguments provided are invalid
          - `invalidCurrency`: The currency cannot be transferred between the requested wallets
          - `invalidUnit`: The unit the transfer request refers to is invalid
          - `Json Parse Error`: The request failed to pass valid JSON as an argument
          - `marketUnavailable`: The market is currently unavailable
          - `nonceBelowThreshold`: The provided nonce is below the threshold
          - `nonceDuplicate`: The provided nonce is a duplicate as it has been used in a previous request
          - `notFound`: The requested information could not be found
          - `requiredArgumentMissing`: One or more required arguments are missing
          - `Server Error`: There was an error processing the request
          - `transferFailed`: The transfer was refused for a reason the venue does not disclose
          - `Unavailable`: The endpoint being called is unavailable
          - `unknownError`: An unknown error has occurred
      enum:
        - accountInactive
        - accountNotFound
        - apiLimitExceeded
        - authenticationError
        - cancelOnly
        - cannotTransferBonusCurrency
        - cashAccountTypeAccessForbidden
        - cashAccountTypeNotFound
        - insufficientFunds
        - invalidAccount
        - invalidAmount
        - invalidArgument
        - invalidCurrency
        - invalidUnit
        - Json Parse Error
        - marketUnavailable
        - nonceBelowThreshold
        - nonceDuplicate
        - notFound
        - requiredArgumentMissing
        - Server Error
        - transferFailed
        - Unavailable
        - unknownError
    ResultError:
      type: object
      properties:
        result:
          type: string
          enum:
            - error
          example: error
      required:
        - result
  examples:
    CancelAllOrdersAfterSuccessExample:
      value:
        result: success
        status:
          currentTime: '2018-06-19T16:51:23.839Z'
          triggerTime: '2018-06-19T16:52:23.839Z'
        serverTime: '2018-06-19T16:51:23.839Z'
    CancelAllOrdersAfterCancelExample:
      value:
        result: success
        status:
          currentTime: '2018-06-19T16:51:23.839Z'
          triggerTime: '0'
        serverTime: '2018-06-19T16:51:23.839Z'
    CancelAllOrdersAfterFailureExample:
      value:
        result: error
        serverTime: '2016-02-25T09:45:53.818Z'
        error: apiLimitExceeded
  securitySchemes:
    general-api-key:
      type: apiKey
      description: General API key with **full** access
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
