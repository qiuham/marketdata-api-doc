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
source_url: 'https://docs.kraken.com/api-reference/account-history/account-log-csv'
updated_at: 2026-11-13
---

# Account log (CSV)

> Lists recent account log entries in CSV format.




## OpenAPI

````yaml /openapi/futures-history-rest.yaml get /accountlogcsv
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
  /accountlogcsv:
    get:
      tags:
        - Account History
      summary: Account log (CSV)
      description: |
        Lists recent account log entries in CSV format.
      operationId: accountLogCsv
      parameters:
        - description: >-
            Include exchange rate, exchange rate from currency, and conversion
            fee for conversions.
          name: conversion_details
          in: query
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: A CSV formatted response of most recent account log entries.
          content:
            text/csv:
              schema:
                type: string
        '401':
          description: Credentials required.
        '429':
          $ref: '#/components/responses/RateLimited'
      security:
        - general-api-key-read-only: []
          authent: []
components:
  responses:
    RateLimited:
      description: Rate limited.
      content:
        text/plain:
          schema:
            type: string
      headers:
        rate-limit-reset:
          description: >-
            Time remaining (in seconds) until repeat request (i.e., same cost)
            will be accepted.
          schema:
            type: integer
            minimum: 1
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
