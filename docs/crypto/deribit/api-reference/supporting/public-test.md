---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/supporting/public-test
api_type: JSON-RPC
updated_at: 2026-11-21 19:01:43.016705
---

# public/test

> Tests the connection to the API server, and returns its version. You can use this to make sure the API is reachable, and matches the expected version.

With `expected_result` set to `exception` the server returns error `11094` (`internal_server_error`) instead of the version, for example:

```json
{"jsonrpc": "2.0", "id": 8213, "error": {"message": "internal_server_error", "code": 11094}}
```

[Try in API console](https://test.deribit.com/api_console?method=%2Fpublic%2Ftest)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /public/test
openapi: 3.0.0
info:
  title: Deribit API
  version: 2.1.1
servers:
  - url: https://test.deribit.com/api/v2
security: []
tags:
  - name: WebSocket Only
    description: Can only be used over websockets.
  - name: Public
    description: Public methods can be used without authentication.
  - name: Private
    description: >-
      <p>Private methods require authentication. All requests must include a
      valid OAuth2 token.</p>

      <p>A token can be requested using the <a
      href="#public-auth">/public/auth</a> method.</p>

      <p>When using the websockets protocol, the token must be included as a
      parameter <code>access_token</code> in the message. When using REST (HTTP
      GET), the token may also be passed in the <code>Authorization</code>
      header.</p>
  - name: Authentication
  - name: Session Management
  - name: Subscription Management
    description: >-
      Subscription works as [notifications](#notifications), so users will
      automatically (after subscribing) receive messages from the server.
      Overview for each channel response format is described in
      [subscriptions](#subscriptions) section.
  - name: Account Management
  - name: Trading
  - name: Market Data
  - name: Wallet
  - name: Chat
  - name: lsp
    description: >-
      Methods and notifications for the Liquidity Support Program (LSP), the
      mechanism that assigns risk from liquidated positions to designated LSP
      participant subaccounts before falling back to auto-deleveraging (ADL).
paths:
  /public/test:
    get:
      tags:
        - Supporting
        - Public
      description: >+
        Tests the connection to the API server, and returns its version. You can
        use this to make sure the API is reachable, and matches the expected
        version.


        With `expected_result` set to `exception` the server returns error
        `11094` (`internal_server_error`) instead of the version, for example:


        ```json

        {"jsonrpc": "2.0", "id": 8213, "error": {"message":
        "internal_server_error", "code": 11094}}

        ```


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fpublic%2Ftest)

      parameters:
        - in: query
          name: expected_result
          required: false
          schema:
            type: string
            enum:
              - exception
          description: >-
            The value "exception" will trigger an error response with code
            `11094` (`internal_server_error`). This may be useful for testing
            wrapper libraries.
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 8212
                  method: public/test
                  params: {}
              exceptionRequest:
                summary: Exception Request
                value:
                  jsonrpc: '2.0'
                  id: 8213
                  method: public/test
                  params:
                    expected_result: exception
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PublicTestResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 8212
                    result:
                      version: 1.2.26
          description: Success response
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/test \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 8212,
              "method": "public/test",
              "params": {}
            }'
        - lang: bash
          label: cURL (Exception)
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/public/test \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 8213,
              "method": "public/test",
              "params": {
                "expected_result": "exception"
              }
            }'
components:
  schemas:
    PublicTestResponse:
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        result:
          type: object
          properties:
            version:
              example: 2.1.26
              type: string
              description: The API version
          required:
            - version
      required:
        - result
        - jsonrpc
      type: object

````

## Related topics

- [Connection Management](https://docs.deribit.com/articles/connection-management-best-practices.md)
- [public/set_heartbeat](https://docs.deribit.com/api-reference/session-management/public-set_heartbeat.md)
- [public/status](https://docs.deribit.com/api-reference/supporting/public-status.md)
- [public/hello](https://docs.deribit.com/api-reference/supporting/public-hello.md)
- [public/unsubscribe](https://docs.deribit.com/api-reference/subscription-management/public-unsubscribe.md)