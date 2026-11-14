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
source_url: 'https://docs.kraken.com/api-reference/affiliate/get-payout-history'
updated_at: 2026-11-13
---

# Get Payout History

> Return one page of the authenticated affiliate's payout history, newest
first. Rows can include RevShare, Prop, CPA, Futures Accelerator Bonus,
sub-affiliate commission, retainer, and remediation payments. Retainer
and remediation rows appear only after approval.

The `summary` covers the whole history, not only the current page. Its
combined totals include all payout sources. Paid totals include
rows with public status `paid`; pending totals include rows with public
status `pending`. Rows with another status can appear in `items`, but do
not contribute to the totals or Prop and CPA counts.

Amounts are exact decimal strings. Combined totals add configured payout
assets, which are expected to be USD-pegged. `prop_purchase_id` is present
only for Prop commissions.

Successful responses are the object itself. Errors are a non-2xx
status with a typed error body, not a wrapped `{ "error", "result" }`.

**API Key Permissions Required:** select the **Query affiliate participants** checkbox.



## OpenAPI

````yaml /openapi/affiliate-rest.yaml get /affiliate/v1/payout-history
openapi: 3.0.0
info:
  title: Affiliate REST API
  version: 1.0.0
  description: >
    Referred-user activity, CPA qualification progress, and payout history for

    approved affiliates.


    Paths are on `https://api.kraken.com` (no `/0` prefix).

    Authentication uses the same API key and secret as the rest of the Kraken
    REST

    API. Requests sign each call and send `api-key`, `api-sign`, and `api-nonce`

    headers; the signed path includes the query string.


    Your affiliate plan must be active. When creating or editing your API key,

    select the Query affiliate participants checkbox and save the key.


    See the [Affiliate guide](/exchange/guides/affiliate/introduction).
servers:
  - url: https://api.kraken.com
    description: Production Server
security:
  - API-Key: []
    API-Sign: []
    API-Nonce: []
tags:
  - name: Affiliate
    x-group: Affiliate reporting
    x-displayName: Affiliate reporting
    description: |
      Referred-user activity, CPA progress, and payouts for approved affiliates.

      See the [Affiliate guide](/exchange/guides/affiliate/introduction).
paths:
  /affiliate/v1/payout-history:
    get:
      tags:
        - Affiliate
      summary: Get Payout History
      description: >-
        Return one page of the authenticated affiliate's payout history, newest

        first. Rows can include RevShare, Prop, CPA, Futures Accelerator Bonus,

        sub-affiliate commission, retainer, and remediation payments. Retainer

        and remediation rows appear only after approval.


        The `summary` covers the whole history, not only the current page. Its

        combined totals include all payout sources. Paid totals include

        rows with public status `paid`; pending totals include rows with public

        status `pending`. Rows with another status can appear in `items`, but do

        not contribute to the totals or Prop and CPA counts.


        Amounts are exact decimal strings. Combined totals add configured payout

        assets, which are expected to be USD-pegged. `prop_purchase_id` is
        present

        only for Prop commissions.


        Successful responses are the object itself. Errors are a non-2xx

        status with a typed error body, not a wrapped `{ "error", "result" }`.


        **API Key Permissions Required:** select the **Query affiliate
        participants** checkbox.
      operationId: getAffiliatePayoutHistory
      parameters:
        - in: query
          name: cursor
          schema:
            description: >-
              Opaque value from `next_cursor` in the previous response. Pass it

              unchanged to retrieve the next page. Omit it for the newest
              payouts.
            type: string
            minLength: 1
          style: form
        - in: query
          name: limit
          schema:
            description: Page size. Defaults to 50 when omitted.
            type: integer
            format: int32
            minimum: 1
            maximum: 200
            default: 50
          style: form
          example: 4
      responses:
        '200':
          description: One page of affiliate payout history with whole-history totals.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/affiliate.GetPayoutHistoryResponse'
              examples:
                payouts:
                  summary: Affiliate payouts including a remediation
                  value:
                    items:
                      - payout_id: RPAY-EXAMPLE-CPA
                        amount: '50.00'
                        asset: USDC
                        status: paid
                        created_at: '2026-09-30T15:04:12Z'
                        source: cpa
                      - payout_id: RPAY-EXAMPLE-REMEDIATION
                        amount: '75.00'
                        asset: USDC
                        status: paid
                        created_at: '2026-09-29T12:00:00Z'
                        source: remediation
                      - payout_id: RPAY-EXAMPLE-PROP
                        amount: '30.50'
                        asset: USDC
                        status: pending
                        created_at: '2026-09-29T09:10:00Z'
                        source: prop
                        prop_purchase_id: BRP-EXAMPLE-ORDER
                      - payout_id: RPAY-EXAMPLE-REVSHARE
                        amount: '12.00'
                        asset: USDC
                        status: paid
                        created_at: '2026-09-28T09:10:00Z'
                        source: revshare
                    next_cursor: RPAY-EXAMPLE-REVSHARE
                    summary:
                      paid: '312.00'
                      pending: '130.50'
                      prop:
                        paid: '80.00'
                        pending: '30.50'
                        order_count: 3
                      cpa:
                        paid: '220.00'
                        pending: '100.00'
                        bounty_count: 5
                    limit: 4
        '400':
          description: The cursor is invalid or the limit is outside 1 to 200.
        '401':
          description: Authentication failed.
        '403':
          description: The API key lacks permission or the affiliate plan is not eligible.
        '500':
          description: An internal error occurred.
      security:
        - API-Key: []
          API-Sign: []
          API-Nonce: []
        - API-Key: []
          API-Sign: []
          API-Nonce: []
          API-OTP: []
components:
  schemas:
    affiliate.GetPayoutHistoryResponse:
      description: One page of affiliate payout history, newest first.
      type: object
      required:
        - summary
        - limit
      properties:
        items:
          description: Payouts for this page. May be omitted when empty.
          type: array
          items:
            $ref: '#/components/schemas/affiliate.Payout'
        next_cursor:
          description: Present when more results exist. Pass it unchanged as `cursor`.
          type: string
        summary:
          $ref: '#/components/schemas/affiliate.PayoutSummary'
        limit:
          description: Page size used for this response, after applying the default of 50.
          type: integer
          format: int32
          minimum: 1
          maximum: 200
    affiliate.Payout:
      description: >-
        One affiliate payout. Internal review and failure reasons are not
        exposed.
      type: object
      required:
        - payout_id
        - amount
        - asset
        - status
        - created_at
        - source
      properties:
        payout_id:
          description: Opaque payout reference.
          type: string
        amount:
          description: Exact payout amount.
          allOf:
            - $ref: '#/components/schemas/affiliate.decimalAmount'
        asset:
          description: Asset in which the payout was or will be paid.
          type: string
        status:
          description: |-
            User-facing payout state. New values may be added; clients must
            tolerate values they do not yet recognize.
          type: string
          enum:
            - pending
            - paid
            - action_needed
            - on_hold
            - refunded
            - cancelled
        created_at:
          description: Time at which Rewards created the payout record.
          type: string
          format: date-time
        source:
          description: >-
            Product that generated this payout. `sub_affiliate` is a commission

            from sub-affiliate earnings, `retainer` is an approved retainer

            payment, and `remediation` is a one-off makeup payout added manually

            by Kraken. New values may be added; clients must tolerate values
            they

            do not yet recognize.
          type: string
          enum:
            - revshare
            - prop
            - cpa
            - futures_accelerator_bonus
            - sub_affiliate
            - retainer
            - remediation
        prop_purchase_id:
          description: Opaque Prop purchase reference. Present only for Prop commissions.
          type: string
    affiliate.PayoutSummary:
      description: >-
        Whole-history totals for all affiliate payout sources, including

        sub-affiliate commissions, approved retainers, and approved
        remediations,

        independent of the current page.
      type: object
      required:
        - paid
        - pending
        - prop
        - cpa
      properties:
        paid:
          description: Sum of included payouts with public status `paid`.
          allOf:
            - $ref: '#/components/schemas/affiliate.decimalAmount'
        pending:
          description: Sum of included payouts with public status `pending`.
          allOf:
            - $ref: '#/components/schemas/affiliate.decimalAmount'
        prop:
          $ref: '#/components/schemas/affiliate.PropPayoutSummary'
        cpa:
          $ref: '#/components/schemas/affiliate.CpaPayoutSummary'
    affiliate.decimalAmount:
      description: Decimal amount as a string.
      type: string
      pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
    affiliate.PropPayoutSummary:
      description: Whole-history Prop commission totals.
      type: object
      required:
        - paid
        - pending
        - order_count
      properties:
        paid:
          description: Sum of Prop commissions with public status `paid`.
          allOf:
            - $ref: '#/components/schemas/affiliate.decimalAmount'
        pending:
          description: Sum of Prop commissions with public status `pending`.
          allOf:
            - $ref: '#/components/schemas/affiliate.decimalAmount'
        order_count:
          description: >-
            Number of distinct Prop orders with public status `paid` or
            `pending`.
          type: integer
          format: int64
          minimum: 0
    affiliate.CpaPayoutSummary:
      description: Whole-history CPA bounty totals.
      type: object
      required:
        - paid
        - pending
        - bounty_count
      properties:
        paid:
          description: Sum of CPA bounties with public status `paid`.
          allOf:
            - $ref: '#/components/schemas/affiliate.decimalAmount'
        pending:
          description: Sum of CPA bounties with public status `pending`.
          allOf:
            - $ref: '#/components/schemas/affiliate.decimalAmount'
        bounty_count:
          description: Number of CPA bounties with public status `paid` or `pending`.
          type: integer
          format: int64
          minimum: 0
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
    API-Nonce:
      type: apiKey
      description: >-
        The "API-Nonce" header should contain an always-increasing 64-bit
        integer, most commonly a Unix timestamp in milliseconds. Each request
        must use a nonce greater than the nonce of the previous request signed
        with the same API key.
      name: API-Nonce
      in: header
    API-OTP:
      type: apiKey
      description: >-
        The "API-OTP" header should contain your two-factor authentication
        one-time password. Required only if 2FA is configured for the API key.
      name: API-OTP
      in: header

````
