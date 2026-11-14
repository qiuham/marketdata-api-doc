---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/api-reference/trade/send-heartbeat'
updated_at: 2026-11-13
---

# Send heartbeat

> Sends one legacy order heartbeat for the authenticated API key.
The first accepted send enables timeout cancellation for all open orders
owned by that API key, across markets and processes. Keep sending accepted
heartbeats every 5 seconds. No scheduler or disarm operation is provided;
stopping sends or closing a client leaves the deadline active.
It shares the key's registration with POST /v1/heartbeats and resets the
expected modern heartbeat ID to an empty string.
After 10 seconds without an accepted send, a five-second scan removes the
registration and queues a best-effort cancel-all attempt. Cancellation
timing and success are not guaranteed. Later accepted sends register again.
A lost response may follow an accepted send. WebSocket keepalive does not
refresh this deadline. Stop placing orders and explicitly cancel/verify
orders you intend to remove before shutdown.




## OpenAPI

````yaml /api-spec/clob-openapi.yaml post /heartbeats
openapi: 3.1.0
info:
  title: Polymarket CLOB API
  description: Polymarket CLOB API Reference
  license:
    name: MIT
    identifier: MIT
  version: 1.0.0
servers:
  - url: https://clob.polymarket.com
    description: Production CLOB API
  - url: https://clob-staging.polymarket.com
    description: Staging CLOB API
security: []
tags:
  - name: Trade
    description: Trade endpoints
  - name: Markets
    description: Market data endpoints
  - name: Account
    description: Account and authentication endpoints
  - name: Notifications
    description: User notification endpoints
  - name: Rewards
    description: Rewards and earnings endpoints
  - name: Rebates
    description: Maker rebate endpoints
paths:
  /heartbeats:
    post:
      tags:
        - Trade
      summary: Send heartbeat
      description: >
        Sends one legacy order heartbeat for the authenticated API key.

        The first accepted send enables timeout cancellation for all open orders

        owned by that API key, across markets and processes. Keep sending
        accepted

        heartbeats every 5 seconds. No scheduler or disarm operation is
        provided;

        stopping sends or closing a client leaves the deadline active.

        It shares the key's registration with POST /v1/heartbeats and resets the

        expected modern heartbeat ID to an empty string.

        After 10 seconds without an accepted send, a five-second scan removes
        the

        registration and queues a best-effort cancel-all attempt. Cancellation

        timing and success are not guaranteed. Later accepted sends register
        again.

        A lost response may follow an accepted send. WebSocket keepalive does
        not

        refresh this deadline. Stop placing orders and explicitly cancel/verify

        orders you intend to remove before shutdown.
      operationId: sendHeartbeat
      responses:
        '200':
          description: Heartbeat acknowledged
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HeartbeatResponse'
              example:
                status: ok
        '401':
          description: Unauthorized - Invalid API key or authentication failed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Invalid API key
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Internal server error
      security:
        - polyApiKey: []
          polyAddress: []
          polySignature: []
          polyPassphrase: []
          polyTimestamp: []
components:
  schemas:
    HeartbeatResponse:
      type: object
      description: Response for heartbeat request
      required:
        - status
      properties:
        status:
          type: string
          description: Status of the heartbeat acknowledgment
          example: ok
    ErrorResponse:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message
        code:
          type: string
          description: Machine-readable error code, when provided
        retry_after_seconds:
          type: integer
          description: Number of seconds to wait before retrying, when provided
  securitySchemes:
    polyApiKey:
      type: apiKey
      in: header
      name: POLY_API_KEY
      description: Your API key
    polyAddress:
      type: apiKey
      in: header
      name: POLY_ADDRESS
      description: Ethereum address associated with the API key
    polySignature:
      type: apiKey
      in: header
      name: POLY_SIGNATURE
      description: HMAC signature of the request
    polyPassphrase:
      type: apiKey
      in: header
      name: POLY_PASSPHRASE
      description: API key passphrase
    polyTimestamp:
      type: apiKey
      in: header
      name: POLY_TIMESTAMP
      description: Unix timestamp of the request

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
