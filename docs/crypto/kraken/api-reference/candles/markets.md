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
source_url: 'https://docs.kraken.com/api-reference/candles/markets'
updated_at: 2026-11-13
---

# Markets

> Markets available for specified tick type.

List of available tick types can be fetched from the [tick types](#operation/tickTypes)
endpoint.



## OpenAPI

````yaml /openapi/futures-charts-rest.yaml get /{tick_type}
openapi: 3.1.0
info:
  title: Charts
  version: v1.0
  description: Public chart candle and analytics APIs.
servers:
  - url: https://futures.kraken.com/api/charts/v1
    description: Kraken Futures
    x-kfOnly: true
security: []
tags:
  - name: Candles
  - name: Analytics
paths:
  /{tick_type}:
    get:
      tags:
        - Candles
      summary: Markets
      description: >-
        Markets available for specified tick type.


        List of available tick types can be fetched from the [tick
        types](#operation/tickTypes)

        endpoint.
      operationId: symbols
      parameters:
        - name: tick_type
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/TickTypes'
      responses:
        '200':
          description: Markets list
          content:
            application/json:
              schema:
                type: array
                items:
                  type: string
              example:
                - PI_XRPUSD
                - FI_XRPUSD_210625
                - FI_XBTUSD_210528
                - PI_XBTUSD
      security: []
components:
  schemas:
    TickTypes:
      title: Tick Types
      type: string
      enum:
        - spot
        - mark
        - trade

````
