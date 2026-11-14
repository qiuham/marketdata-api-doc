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
source_url: 'https://docs.kraken.com/api-reference/account-data/get-export-report-status'
updated_at: 2026-11-13
---

# Get Export Report Status

> Get status of requested data exports.

**API Key Permissions Required:** `Data - Export data`




## OpenAPI

````yaml /openapi/spot-rest.yaml post /private/ExportStatus
openapi: 3.0.0
info:
  title: REST API
  version: 1.1.0
  description: ''
servers:
  - url: https://api.kraken.com/0
    description: Production Server
security:
  - API-Key: []
    API-Sign: []
tags:
  - name: Market Data
  - name: Account Data
  - name: Trading
  - name: Algo Trading
    description: >
      Algo Trading endpoints create and manage **strategies**: parent
      instructions that Kraken executes on your behalf as a series of regular
      child orders.


      The only strategy available today is **TWAP** (time-weighted average
      price). A TWAP buys or sells a total `volume` evenly between `starttm` and
      `expiretm`. How child orders are sized, timed and placed is managed by
      Kraken and may change as execution improves.


      An algo runs as a strategy. In Kraken Pro, TWAP strategies show under
      Bots.


      ### Strategy lifecycle


      `pending` → `open` → `closed` | `expired` | `cancelled`


      - `pending`: accepted, waiting for `starttm`.

      - `open`: running, child orders are being placed.

      - `closed`: the full `volume` was filled before `expiretm`.

      - `expired`: `expiretm` was reached before the full `volume` was filled.

      - `cancelled`: cancelled with `CancelStrategy`.


      TWAP child orders are immediate-or-cancel limit orders and do not rest on
      the book. Completed child orders appear in `ClosedOrders`, and fills
      appear in trade history. Use the strategy endpoints to monitor overall
      progress.
  - name: funding-beta
    x-group: Funding (Beta)
    x-displayName: Funding (Beta)
  - name: Funding
    x-group: Funding (Legacy)
    x-displayName: Funding (Legacy)
  - name: Subaccounts
    description: >-
      Subaccounts are currently only available to institutional clients. Please
      contact your Account Manager for more details.
  - name: Earn
    description: >
      The earn API allows interacting with all of Kraken's yield generating
      products. It replaces the old `/staking` part of the API.


      The different available earn products are represented by earn strategies.
      This corresponds to the legacy `Staking/Assets`. `Stake`/`Unstake` are
      replaced by `Allocate`/`Deallocate`.


      ### Overview of the available endpoints under `/Earn`:


      - `Strategies` - list all earn strategies for which you are eligible or
      have a balance.

      - `Allocations` - lists the balance in your earn account for each
      strategy. Requires the `Query Funds` API key permission.

      - `Allocate`/`Deallocate` - allocate/deallocate to an earn strategy
      through an async operation. Requires the `Earn Funds` API key permission.

      - `AllocateStatus`/`DeallocateStatus` - verifies the state of the last
      allocation/deallocation. Requires the `Earn Funds` or `Query Funds` API
      key permission.


      ### Example usage:


      ### Determine which funds are earning rewards:


      1. Call `Strategies` to obtain information about the relevant strategy.
      The `lock_type` field shows whether bonding/unbonding funds are earning
      yield. The relevant fields are `bonding_rewards`/`unbonding_rewards`.

      2. Call `Allocations` for the relevant strategy. From the previous step,
      for strategies where bonding/unbonding does not earn yield, substract
      these balances from `amount_allocated.total` to determine which balances
      are currently earning.


      ### Get allocatable balance:


      Call `/0/private/BalanceEx`, subtract `hold_trading` amount. Remaining
      balance is available for allocation to a strategy.


      ### Geo restrictions:


      Some earn strategies are not available in all geographic regions.
      `Strategies` will return only strategies available to the caller.
  - name: Transparency
paths:
  /private/ExportStatus:
    post:
      tags:
        - Account Data
      summary: Get Export Report Status
      description: |
        Get status of requested data exports.

        **API Key Permissions Required:** `Data - Export data`
      operationId: exportStatus
      requestBody:
        required: true
        content:
          application/json:
            schema:
              required:
                - nonce
                - report
              properties:
                nonce:
                  $ref: '#/components/schemas/nonce'
                report:
                  type: string
                  description: Type of reports to inquire about
                  enum:
                    - trades
                    - ledgers
              example:
                nonce: 1695828490
                report: trades
      responses:
        '200':
          description: Export status retrieved
          content:
            application/json:
              schema:
                properties:
                  result:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: Report ID
                        descr:
                          type: string
                        format:
                          type: string
                        report:
                          type: string
                        subtype:
                          type: string
                        status:
                          type: string
                          description: Status of the report
                          enum:
                            - Queued
                            - Processing
                            - Processed
                        error:
                          type: string
                          description: Error of the report
                          enum:
                            - EExport:Internal error
                            - EExport:Unexpected error
                            - EExport:Canceled
                            - EExport:Deleted
                            - EExport:Exported size too big
                        flags:
                          type: string
                          deprecated: true
                        fields:
                          type: string
                        createdtm:
                          type: string
                          description: UNIX timestamp of report request
                        expiretm:
                          type: string
                          deprecated: true
                        starttm:
                          type: string
                          description: UNIX timestamp report processing began
                        completedtm:
                          type: string
                          description: UNIX timestamp report processing finished
                        datastarttm:
                          type: string
                          description: UNIX timestamp of the report data start time
                        dataendtm:
                          type: string
                          description: UNIX timestamp of the report data end time
                        aclass:
                          type: string
                          deprecated: true
                        asset:
                          type: string
                        asset_classes:
                          type: array
                          description: Asset classes included in the report
                          items:
                            type: string
                        endtm:
                          type: string
                          description: UNIX timestamp of the report end time
                        delete:
                          type: boolean
                          description: Whether the report is pending deletion
                  error:
                    $ref: '#/components/schemas/error'
                example:
                  error: []
                  result:
                    - id: VSKC
                      descr: my_trades_1
                      format: CSV
                      report: trades
                      subtype: all
                      status: Processed
                      flags: '0'
                      fields: all
                      createdtm: '1688669085'
                      expiretm: '1688878685'
                      starttm: '1688669093'
                      completedtm: '1688669093'
                      datastarttm: '1683556800'
                      dataendtm: '1688669085'
                      aclass: forex
                      asset: all
                    - id: TCJA
                      descr: my_trades_1
                      format: CSV
                      report: trades
                      subtype: all
                      status: Processed
                      flags: '0'
                      fields: all
                      createdtm: '1688363637'
                      expiretm: '1688573237'
                      starttm: '1688363664'
                      completedtm: '1688363664'
                      datastarttm: '1683235200'
                      dataendtm: '1688363637'
                      aclass: forex
                      asset: all
components:
  schemas:
    nonce:
      description: Nonce used in construction of `API-Sign` header
      type: integer
      format: int64
    error:
      type: array
      items:
        description: Kraken API error
        type: string
        example: EGeneral:Invalid arguments
  securitySchemes:
    API-Key:
      type: apiKey
      description: The "API-Key" header should contain your API key.
      name: API-Key
      in: header
    API-Sign:
      type: apiKey
      description: >-
        Authenticated requests should be signed with the "API-Sign" header,
        using a signature generated with your private key, nonce, encoded
        payload, and URI path.
      name: API-Sign
      in: header

````
