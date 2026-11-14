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
source_url: 'https://docs.kraken.com/api-reference/subaccounts/get-subaccounts'
updated_at: 2026-11-13
---

# Get subaccounts

> Return information about subaccounts, including balances and UIDs.



## OpenAPI

````yaml /openapi/futures-rest.yaml get /subaccounts
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
  /subaccounts:
    get:
      tags:
        - Subaccounts
      summary: Get subaccounts
      description: Return information about subaccounts, including balances and UIDs.
      operationId: listSubaccounts
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
                          masterAccountUid:
                            type: string
                            description: Master account UID
                          subaccounts:
                            type: array
                            items:
                              $ref: '#/components/schemas/SubAccount'
                            description: The sub-accounts.
                        required:
                          - masterAccountUid
                          - subaccounts
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                cfSuccess:
                  $ref: '#/components/examples/SubaccountsExample'
                kfSuccess:
                  $ref: '#/components/examples/SubaccountsWithFlexExample'
      security:
        - general-api-key-read-only: []
          authent: []
components:
  schemas:
    SubAccount:
      type: object
      properties:
        accountUid:
          type: string
          description: The account UID
        email:
          type: string
          description: The email associated with the account
        fullName:
          type:
            - string
            - 'null'
          description: The name of the account
        holdingAccounts:
          type: array
          items:
            $ref: '#/components/schemas/HoldingAccountBalance'
          description: >-
            Structure containing structures with holding accounts information
            for a specific holding

            account asset.
        futuresAccounts:
          type: array
          items:
            $ref: '#/components/schemas/FutureAccountBalance'
          description: >-
            Structure containing structures with single-collateral accounts
            information for a

            specific futures account asset.
        flexAccount:
          $ref: '#/components/schemas/FlexAccountBalance'
          x-kfOnly: true
          type: object
          description: Multi-collateral account structure.
      required:
        - accountUid
        - email
        - fullName
        - holdingAccounts
        - futuresAccounts
        - flexAccount
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
    HoldingAccountBalance:
      type: object
      properties:
        currency:
          type: string
          description: The currency of the account. All figures shown in this currency.
        amount:
          type: number
          description: The amount of currency in the holding account.
      required:
        - currency
        - amount
    FutureAccountBalance:
      type: object
      properties:
        name:
          type: string
          description: The name of the futures account as the account pair.
        availableMargin:
          type: number
          description: >-
            The amount of currency in the holding account in the quote currency
            of the name pair.
      required:
        - name
        - availableMargin
    FlexAccountBalance:
      x-kfOnly: true
      type: object
      properties:
        currencies:
          type: array
          items:
            $ref: '#/components/schemas/FlexCurrencyBalance'
        initialMargin:
          type: number
          description: The total initial margin for the multi-collateral account in USD.
        initialMarginWithOrders:
          type: number
          description: >-
            The total initial margin of open positions without the margin held
            by open orders for

            the multi-collateral account in USD.
        maintenanceMargin:
          type: number
          description: >-
            The total maintenance margin for the multi-collateral account in
            USD.
        balanceValue:
          type: number
          description: The total balance value for the multi-collateral account in USD.
        portfolioValue:
          type: number
          description: >-
            The total value of the portfolio in USD (Balance Value + Total
            Unrealised Profit/Loss).
        collateralValue:
          type: number
          description: >-
            The USD value of balances in account usable for margin [(Balance
            Value * (1-Haircut)].
        pnl:
          type: number
          description: The unrealised pnl for the multi-collateral account.
        unrealizedFunding:
          type: number
          description: >-
            The total unrealised funding for the multi-collateral account in
            USD.
        totalUnrealized:
          type: number
          description: >-
            Total unrealised Profit/Loss and unrealised funding of open
            positions in USD `(Unrealised

            Position(s) Profit/Loss + Unrealised Funding Rate Profit/Loss) * USD
            rate`.
        totalUnrealizedAsMargin:
          type: number
          description: >-
            Unrealised Profit/Loss and unrealised funding that is usable as
            margin `(Unrealised

            Profit/Loss + Unrealised Funding Rate) * Haircut - Conversion Fee`.
        availableMargin:
          type: number
          description: >-
            Account-wide margin available to create new orders (Margin Equity -
            Total Initial

            Margin).
        marginEquity:
          type: number
          description: >-
            The Balance Value multiplied by the dollar rate and with haircuts
            applied to non-USD currencies, plus unrealised profit or loss as
            Margin.


            `[Balance Value in USD * (1-Haircut)] + (Total Unrealised
            Profit/Loss as Margin in USD)`
        portfolioMarginBreakdown:
          $ref: '#/components/schemas/PortfolioMarginBreakdown'
          description: Breakdown of portfolio margin components.
      required:
        - currencies
        - initialMargin
        - initialMarginWithOrders
        - maintenanceMargin
        - balanceValue
        - portfolioValue
        - collateralValue
        - pnl
        - unrealizedFunding
        - totalUnrealized
        - totalUnrealizedAsMargin
        - availableMargin
        - marginEquity
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
    FlexCurrencyBalance:
      x-kfOnly: true
      type: object
      properties:
        currency:
          type: string
          description: The name of the currency.
        quantity:
          type: number
          description: The amount of currency in the multi-collateral account.
        value:
          type: number
          description: The value of the currency quantity.
        collateral:
          type: number
          description: The collateral value of the currency quantity (value * haircut).
        available:
          type: number
          description: The available currency (quantity - margin requirement)
      required:
        - currency
        - quantity
        - value
        - collateral
        - available
    PortfolioMarginBreakdown:
      description: Breakdown of components that make up the portfolio margin calculation.
      type: object
      properties:
        totalCrossAssetNettedMarketRisk:
          type: number
          format: double
          deprecated: true
          description: >-
            **DEPRECATED** - Always equal to `totalMarketRisk`. Cross-asset
            netting

            was removed. This field will be removed in a future release.
        totalMarketRisk:
          type: number
          format: double
        totalScenarioPnls:
          oneOf:
            - type: array
              items:
                type: number
                format: double
            - type: 'null'
        totalAbsoluteOptionPositionDeltaNotional:
          type: number
          format: double
        netPortfolioDelta:
          type: number
          format: double
        totalPremium:
          type: number
          format: double
        isBuyOnly:
          type: boolean
        futuresMaintenanceMargin:
          type: number
          format: double
      required:
        - totalCrossAssetNettedMarketRisk
        - totalMarketRisk
        - totalScenarioPnls
        - totalAbsoluteOptionPositionDeltaNotional
        - netPortfolioDelta
        - totalPremium
        - isBuyOnly
        - futuresMaintenanceMargin
  examples:
    SubaccountsExample:
      x-cfOnly: true
      value:
        result: success
        serverTime: '2022-03-31T20:38:53.677Z'
        masterAccountUid: ba598ca1-65c1-4f48-927d-0e2b647d627a
        subaccounts:
          - accountUid: 7f5c528e-2285-45f0-95f5-83d53d4bfcd2
            fullName: John Doe
            email: john.doe@example.com
            holdingAccounts:
              - currency: gbp
                amount: 0
              - currency: bch
                amount: 0.00004
              - currency: xrp
                amount: 13662.85078
              - currency: usd
                amount: 0
              - currency: eth
                amount: 3.0000485057
              - currency: usdt
                amount: 0
              - currency: ltc
                amount: 0.00002
              - currency: usdc
                amount: 0
              - currency: xbt
                amount: 3.46e-9
            futuresAccounts:
              - name: f-xrp:usd
                availableMargin: 16187.33210488726
              - name: f-eth:usd
                availableMargin: 67.59768318324302
              - name: f-xbt:usd
                availableMargin: -0.0009056832839642471
              - name: f-ltc:usd
                availableMargin: 67.51126059691163
              - name: f-xrp:xbt
                availableMargin: 2.34e-9
              - name: f-bch:usd
                availableMargin: 47.151615710695495
            flexAccount:
              currencies:
                - currency: eth
                  quantity: 0.5
                  value: 1646.575
                  collateral: 1543.91104875
                  available: 0.49999966035931903
                - currency: usdt
                  quantity: 0
                  value: 0
                  collateral: 0
                  available: 0
                - currency: gbp
                  quantity: 0
                  value: 0
                  collateral: 0
                  available: 0
                - currency: xbt
                  quantity: 0
                  value: 0
                  collateral: 0
                  available: 0
                - currency: usdc
                  quantity: 0
                  value: 0
                  collateral: 0
                  available: 0
                - currency: usd
                  quantity: 0
                  value: 0
                  collateral: 0
                  available: 0
              initialMargin: 0
              initialMarginWithOrders: 0
              maintenanceMargin: 0
              balanceValue: 1646.58
              portfolioValue: 1646.58
              collateralValue: 1543.91
              pnl: 0
              unrealizedFunding: 0
              totalUnrealized: 0
              totalUnrealizedAsMargin: 0
              availableMargin: 1543.91
              marginEquity: 1543.91
    SubaccountsWithFlexExample:
      x-kfOnly: true
      value:
        result: success
        serverTime: '2022-03-31T20:38:53.677Z'
        masterAccountUid: ba598ca1-65c1-4f48-927d-0e2b647d627a
        subaccounts:
          - holdingAccounts:
              - currency: gbp
                amount: 0
              - currency: bch
                amount: 0.00004
              - currency: xrp
                amount: 13662.85078
              - currency: usd
                amount: 0
              - currency: eth
                amount: 3.0000485057
              - currency: usdt
                amount: 0
              - currency: ltc
                amount: 0.00002
              - currency: usdc
                amount: 0
              - currency: xbt
                amount: 3.46e-9
            futuresAccounts:
              - name: f-xrp:usd
                availableMargin: 16187.33210488726
              - name: f-eth:usd
                availableMargin: 67.59768318324302
              - name: f-xbt:usd
                availableMargin: -0.0009056832839642471
              - name: f-ltc:usd
                availableMargin: 67.51126059691163
              - name: f-xrp:xbt
                availableMargin: 2.34e-9
              - name: f-bch:usd
                availableMargin: 47.151615710695495
            flexAccount:
              currencies:
                - currency: eth
                  quantity: 0.5
                  value: 1646.575
                  collateral: 1543.91104875
                  available: 0.49999966035931903
                - currency: usdt
                  quantity: 0
                  value: 0
                  collateral: 0
                  available: 0
                - currency: gbp
                  quantity: 0
                  value: 0
                  collateral: 0
                  available: 0
                - currency: xbt
                  quantity: 0
                  value: 0
                  collateral: 0
                  available: 0
                - currency: usdc
                  quantity: 0
                  value: 0
                  collateral: 0
                  available: 0
                - currency: usd
                  quantity: 0
                  value: 0
                  collateral: 0
                  available: 0
              initialMargin: 0
              initialMarginWithOrders: 0
              maintenanceMargin: 0
              balanceValue: 1646.58
              portfolioValue: 1646.58
              collateralValue: 1543.91
              pnl: 0
              unrealizedFunding: 0
              totalUnrealized: 0
              totalUnrealizedAsMargin: 0
              availableMargin: 1543.91
              marginEquity: 1543.91
            fullName: fullname redacted
            email: email redacted
            accountUid: 7f5c528e-2285-45f0-95f5-83d53d4bfcd2
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
