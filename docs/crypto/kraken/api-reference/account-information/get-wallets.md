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
source_url: 'https://docs.kraken.com/api-reference/account-information/get-wallets'
updated_at: 2026-11-13
---

# Get wallets

> This endpoint returns key information relating to all your accounts which may either be
cash accounts or margin accounts. This includes digital asset balances, instrument balances,
margin requirements, margin trigger estimates and auxiliary information such as available
funds, PnL of open positions and portfolio value.



## OpenAPI

````yaml /openapi/futures-rest.yaml get /accounts
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
  /accounts:
    get:
      tags:
        - Account Information
      summary: Get wallets
      description: >-
        This endpoint returns key information relating to all your accounts
        which may either be

        cash accounts or margin accounts. This includes digital asset balances,
        instrument balances,

        margin requirements, margin trigger estimates and auxiliary information
        such as available

        funds, PnL of open positions and portfolio value.
      operationId: getAccounts
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                title: Accounts Response
                oneOf:
                  - title: Success Response
                    allOf:
                      - type: object
                        properties:
                          accounts:
                            $ref: '#/components/schemas/Account'
                            description: >-
                              A structure containing structures with
                              account-related information for

                              all margin and cash accounts.
                        required:
                          - accounts
                      - $ref: '#/components/schemas/SuccessResponse'
                  - $ref: '#/components/schemas/ErrorResponse'
              examples:
                success:
                  $ref: '#/components/examples/AccountsExample'
        '409':
          $ref: '#/components/responses/CancelOnly'
      security:
        - general-api-key-read-only: []
          authent: []
components:
  schemas:
    Account:
      description: Information for all margin and cash accounts
      type: object
      properties:
        cash:
          $ref: '#/components/schemas/CashAccount'
        flex:
          $ref: '#/components/schemas/FlexBalanceSummary'
          description: Structure showing multi-collateral wallet details.
      required:
        - cash
        - flex
      additionalProperties:
        $ref: '#/components/schemas/MarginAccount'
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
    CashAccount:
      type: object
      properties:
        type:
          type: string
          enum:
            - cashAccount
          description: The type of the account (always "cashAccount").
        balances:
          $ref: '#/components/schemas/CashAccountBalances'
          description: A structure containing account balances.
      required:
        - type
        - balances
    FlexBalanceSummary:
      x-kfOnly: true
      type: object
      properties:
        type:
          type: string
          enum:
            - multiCollateralMarginAccount
          description: The type of the account (always multiCollateralMarginAccount)
        currencies:
          $ref: '#/components/schemas/FlexCurrencies'
          description: Structure with collateral currency details.
        initialMargin:
          type: number
          description: Total initial margin held for open positions (USD).
        initialMarginWithOrders:
          type: number
          description: Total initial margin held for open positions and open orders (USD).
        maintenanceMargin:
          type: number
          description: Total maintenance margin held for open positions (USD).
        balanceValue:
          type: number
          description: USD value of all collateral in multi-collateral wallet.
        portfolioValue:
          type: number
          description: Balance value plus unrealised PnL in USD.
        collateralValue:
          type: number
          description: >-
            USD value of balances in account usable for margin (Balance Value *
            Haircut).
        pnl:
          type: number
          description: Unrealised PnL in USD.
        unrealizedFunding:
          type: number
          description: Unrealised funding from funding rate (USD).
        totalUnrealized:
          type: number
          description: Total USD value of unrealised funding and unrealised PnL.
        totalUnrealizedAsMargin:
          type: number
          description: >-
            Unrealised pnl and unrealised funding that is usable as margin
            `[(Unrealised Profit/Loss

            + Unrealised Funding Rate) * Haircut - Conversion Fee]`.
        availableMargin:
          type: number
          description: Margin Equity - Total Initial Margin.
        marginEquity:
          type: number
          description: >-
            `[Balance Value in USD * (1-Haircut)] + (Total Unrealised
            Profit/Loss as Margin in USD)`
        portfolioMarginBreakdown:
          $ref: '#/components/schemas/PortfolioMarginBreakdown'
          description: Breakdown of portfolio margin components.
        upnlInterestRate:
          type:
            - number
            - 'null'
          description: Interest rate applied to unrealized profit/loss.
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
    MarginAccount:
      type: object
      properties:
        type:
          type: string
          enum:
            - marginAccount
          description: The type of the account (always "marginAccount").
        currency:
          type: string
          description: >-
            The currency of the account. All figures shown in `auxiliary` and
            `marginRequirements`

            are in this currency.
        balances:
          $ref: '#/components/schemas/MarginAccountBalances'
          description: A structure containing account balances.
        auxiliary:
          $ref: '#/components/schemas/Auxiliary'
          description: A structure containing auxiliary account information.
        marginRequirements:
          $ref: '#/components/schemas/MarginRequirements'
          description: A structure containing the account's margin requirements.
        triggerEstimates:
          $ref: '#/components/schemas/MarginRequirements'
          description: A structure containing the account's margin trigger estimates.
      required:
        - type
        - currency
        - balances
        - auxiliary
        - marginRequirements
        - triggerEstimates
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
    CashAccountBalances:
      type: object
      additionalProperties:
        $ref: '#/components/schemas/DecimalString'
    FlexCurrencies:
      x-kfOnly: true
      type: object
      additionalProperties:
        $ref: '#/components/schemas/FlexCurrencySummary'
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
    MarginAccountBalances:
      type: object
      additionalProperties:
        $ref: '#/components/schemas/DecimalString'
    Auxiliary:
      type: object
      properties:
        usd:
          type: number
        pv:
          type: number
          description: The portfolio value of the account, in currency.
        pnl:
          type: number
          description: The PnL of current open positions of the account, in  currency.
        af:
          type: number
          description: The available funds of the account, in currency.
        funding:
          type: number
      required:
        - usd
        - pv
        - pnl
        - af
        - funding
    MarginRequirements:
      type: object
      properties:
        im:
          type: number
          description: The initial margin requirement of the account.
        mm:
          type: number
          description: The maintenance margin requirement of the account.
        lt:
          type: number
          description: The liquidation threshold of the account.
        tt:
          type: number
          description: The termination threshold of the account
      required:
        - im
        - mm
        - lt
        - tt
    DecimalString:
      type: string
      format: decimal
      example: '12.0353200'
    FlexCurrencySummary:
      x-kfOnly: true
      type: object
      properties:
        quantity:
          type: number
          description: Quantity of asset.
        value:
          type: number
          description: USD value of asset.
        collateral:
          type: number
          description: USD value of the asset usable for margin (Asset Value * Haircut).
        available:
          type: number
          description: Margin (in base currency) available for trading.
      required:
        - quantity
        - value
        - collateral
        - available
  examples:
    AccountsExample:
      value:
        accounts:
          cash:
            balances:
              xbt: '141.31756797'
              xrp: '52465.1254'
            type: cashAccount
          fi_xbtusd:
            auxiliary:
              af: 100.73891563
              funding: 100.73891563
              pnl: 12.42134766
              pv: 153.73891563
              usd: 0
            balances:
              FI_XBTUSD_171215: '50000'
              FI_XBTUSD_180615: '-15000'
              xbt: '141.31756797'
              xrp: '0'
            currency: xbt
            marginRequirements:
              im: 52.8
              lt: 39.6
              mm: 23.76
              tt: 15.84
            triggerEstimates:
              im: 3110
              lt: 2890
              mm: 3000
              tt: 2830
            type: marginAccount
          flex:
            type: multiCollateralMarginAccount
            currencies:
              XBT:
                quantity: 0.1185308247
                value: 4998.721054420551
                collateral: 4886.49976674881
                available: 0.1185308247
              USD:
                quantity: 5000
                value: 5000
                collateral: 5000
                available: 5000
              EUR:
                quantity: 4540.5837374453
                value: 4999.137289089901
                collateral: 4886.906656949836
                available: 4540.5837374453
            balanceValue: 34995.52
            portfolioValue: 34995.52
            collateralValue: 34122.66
            initialMargin: 0
            initialMarginWithOrders: 0
            maintenanceMargin: 0
            pnl: 0
            unrealizedFunding: 0
            totalUnrealized: 0
            totalUnrealizedAsMargin: 0
            marginEquity: 34122.66
            availableMargin: 34122.66
        result: success
        serverTime: '2016-02-25T09:45:53.818Z'
  responses:
    CancelOnly:
      description: The venue is cancel-only.
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
