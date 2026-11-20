---
exchange: deribit
source_url: https://docs.deribit.com/api-reference/lsp/private-get_lsp_participant_config
api_type: JSON-RPC
updated_at: 2026-11-20 19:00:14.081998
---

# private/get_lsp_participant_config

> Retrieves the LSP (Liquidity Support Program) participant configuration for the authenticated account.

LSP participants are designated subaccounts that receive assigned positions from liquidated users as an alternative to auto-deleveraging (ADL). This method must be called with an API key belonging to the LSP participant subaccount itself — it returns an error if the authenticated account has no LSP configuration.

The response includes the participant's enable/disable state and any per-cooldown-group limit overrides. When the platform-side participant position lock is switched on, enrolling a subaccount as an LSP participant also locks it to reduce-only trading; this lock is off by default, so participation does not by itself restrict the subaccount to reduce-only.

**📖 Related Article:** [Liquidity Support Program (LSP) API Guide](https://docs.deribit.com/articles/lsp-api-guide)

**Scope:** `account:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_lsp_participant_config)


## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_lsp_participant_config
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
  /private/get_lsp_participant_config:
    get:
      tags:
        - lsp
        - Private
      description: >+
        Retrieves the LSP (Liquidity Support Program) participant configuration
        for the authenticated account.


        LSP participants are designated subaccounts that receive assigned
        positions from liquidated users as an alternative to auto-deleveraging
        (ADL). This method must be called with an API key belonging to the LSP
        participant subaccount itself — it returns an error if the authenticated
        account has no LSP configuration.


        The response includes the participant's enable/disable state and any
        per-cooldown-group limit overrides. When the platform-side participant
        position lock is switched on, enrolling a subaccount as an LSP
        participant also locks it to reduce-only trading; this lock is off by
        default, so participation does not by itself restrict the subaccount to
        reduce-only.


        **📖 Related Article:** [Liquidity Support Program (LSP) API
        Guide](https://docs.deribit.com/articles/lsp-api-guide)


        **Scope:** `account:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_lsp_participant_config)

      parameters: []
      requestBody:
        content:
          application/json:
            examples:
              request:
                summary: JSON-RPC Request Example
                value:
                  jsonrpc: '2.0'
                  id: 8801
                  method: private/get_lsp_participant_config
                  params: {}
        description: JSON-RPC request body
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PrivateGetLspParticipantConfigResponse'
              examples:
                response:
                  summary: Response example
                  value:
                    jsonrpc: '2.0'
                    id: 8801
                    result:
                      config:
                        enabled: true
                        group_limits:
                          '1': 15
                          '6': 0
          description: Success response
        '401':
          $ref: '#/components/responses/ErrorMessageResponse'
      x-codeSamples:
        - lang: bash
          label: cURL
          source: |-
            curl --request POST \
              --url https://test.deribit.com/api/v2/private/get_lsp_participant_config \
              --header 'Authorization: Bearer <ACCESS_TOKEN>' \
              --header 'Content-Type: application/json' \
              --data '{
              "jsonrpc": "2.0",
              "id": 8801,
              "method": "private/get_lsp_participant_config",
              "params": {}
            }'
components:
  schemas:
    PrivateGetLspParticipantConfigResponse:
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
            config:
              $ref: '#/components/schemas/lsp_config'
          required:
            - config
      required:
        - result
        - jsonrpc
      type: object
    lsp_config:
      properties:
        enabled:
          type: boolean
          description: >-
            Whether this subaccount is currently an active LSP participant
            eligible to receive assignments.
        group_limits:
          type: object
          additionalProperties:
            type: number
          description: >
            Per-participant overrides of the assignment limit for each cooldown
            group, expressed as a percentage of the participant's own equity.
            Keyed by group: `"1"` through `"6"` (crypto tiers, `"6"` is the
            catch-all tier) or `"rwa"` (real-world-asset instruments, e.g.
            tokenized equities/commodities).


            A group absent from this map inherits the platform-wide default for
            that group. A value of `0` disables assignments for that group
            entirely. The maximum allowed value for any group is
            `notional_capacity_factor * 100` (see the global LSP config) — that
            factor caps the total notional LSP may assign to a participant as a
            multiple of its equity, and does not change the participant
            account's own maximum leverage.
      required:
        - enabled
        - group_limits
      type: object
      description: >
        LSP participation configuration for a single subaccount.


        Note: designating a subaccount as an LSP participant also locks it to
        reduce-only trading platform-side. This lock is not automatically
        released when the participant is removed — an admin must clear it
        manually.
    ErrorMessageResponse:
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
            data:
              description: Optional error details.
          required:
            - code
            - message
      required:
        - error
        - jsonrpc
      type: object
  responses:
    ErrorMessageResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorMessageResponse'
      description: Success response

````

## Related topics

- [Liquidity Support Program (LSP) API Guide](https://docs.deribit.com/articles/lsp-api-guide.md)
- [private/get_lsp_participants](https://docs.deribit.com/api-reference/lsp/private-get_lsp_participants.md)
- [private/get_lsp_participants_usage](https://docs.deribit.com/api-reference/lsp/private-get_lsp_participants_usage.md)
- [private/get_lsp_usage](https://docs.deribit.com/api-reference/lsp/private-get_lsp_usage.md)
- [private/get_mmp_config](https://docs.deribit.com/api-reference/trading/private-get_mmp_config.md)