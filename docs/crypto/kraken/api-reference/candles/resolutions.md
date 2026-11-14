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
source_url: 'https://docs.kraken.com/api-reference/candles/resolutions'
updated_at: 2026-11-13
---

# Resolutions

> Candle resolutions available for specified tick type and market.

List of available tick types can be fetched from the [tick types](#operation/tickTypes)
endpoint. List of available markets can be fetched from the [markets](#operation/symbols)
endpoint.



## OpenAPI

````yaml /openapi/futures-charts-rest.yaml get /{tick_type}/{symbol}
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
  /{tick_type}/{symbol}:
    get:
      tags:
        - Candles
      summary: Resolutions
      description: >-
        Candle resolutions available for specified tick type and market.


        List of available tick types can be fetched from the [tick
        types](#operation/tickTypes)

        endpoint. List of available markets can be fetched from the
        [markets](#operation/symbols)

        endpoint.
      operationId: resolutions
      parameters:
        - name: tick_type
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/TickTypes'
        - name: symbol
          in: path
          required: true
          description: Market symbol
          schema:
            type: string
      responses:
        '200':
          description: All resolutions for the given `tick_type` and `symbol`
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Resolution'
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
    Resolution:
      title: Resolution
      type: string
      enum:
        - 1m
        - 5m
        - 15m
        - 30m
        - 1h
        - 4h
        - 12h
        - 1d
        - 1w

````
