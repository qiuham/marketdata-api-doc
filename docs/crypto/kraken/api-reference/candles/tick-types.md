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
source_url: 'https://docs.kraken.com/api-reference/candles/tick-types'
updated_at: 2026-11-13
---

# Tick Types

> Returns all available tick types to use with the [markets](#operation/symbols) endpoint.



## OpenAPI

````yaml /openapi/futures-charts-rest.yaml get /
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
  /:
    get:
      tags:
        - Candles
      summary: Tick Types
      description: >-
        Returns all available tick types to use with the
        [markets](#operation/symbols) endpoint.
      operationId: tickTypes
      responses:
        '200':
          description: Tick types list
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/TickTypes'
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
