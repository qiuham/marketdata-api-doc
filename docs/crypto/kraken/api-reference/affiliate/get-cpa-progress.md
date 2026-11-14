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
source_url: 'https://docs.kraken.com/api-reference/affiliate/get-cpa-progress'
updated_at: 2026-11-13
---

# Get CPA Progress

> Return CPA qualification progress for one referred trader belonging to
the authenticated affiliate.

Pass the full `iiban` returned by Get Daily Activity. The response lists
each CPA bounty separately with its reward, status, requirements, exact
measurable values, and completion percentage. A measurable requirement
can remain at `100` percent while an additional non-numeric step, such
as a hold period, is still incomplete.

Bounties that have qualified or paid remain visible. A bounty can also
report `expired`, `no_longer_eligible`, or `not_tracked`. When
`progress_availability` is `unavailable`, condition measurements may be
omitted.

Unknown IIBANs, referrals belonging to another affiliate, and traders
who opted out of activity sharing return `404`.

Region-specific bounties that do not apply to the trader are omitted,
so `bounties` can be empty.

Successful responses are the object itself. Errors are a non-2xx
status with a typed error body, not a wrapped `{ "error", "result" }`.

**API Key Permissions Required:** select the **Query affiliate participants** checkbox.



## OpenAPI

````yaml /openapi/affiliate-rest.yaml get /affiliate/v1/cpa-progress
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
  /affiliate/v1/cpa-progress:
    get:
      tags:
        - Affiliate
      summary: Get CPA Progress
      description: >-
        Return CPA qualification progress for one referred trader belonging to

        the authenticated affiliate.


        Pass the full `iiban` returned by Get Daily Activity. The response lists

        each CPA bounty separately with its reward, status, requirements, exact

        measurable values, and completion percentage. A measurable requirement

        can remain at `100` percent while an additional non-numeric step, such

        as a hold period, is still incomplete.


        Bounties that have qualified or paid remain visible. A bounty can also

        report `expired`, `no_longer_eligible`, or `not_tracked`. When

        `progress_availability` is `unavailable`, condition measurements may be

        omitted.


        Unknown IIBANs, referrals belonging to another affiliate, and traders

        who opted out of activity sharing return `404`.


        Region-specific bounties that do not apply to the trader are omitted,

        so `bounties` can be empty.


        Successful responses are the object itself. Errors are a non-2xx

        status with a typed error body, not a wrapped `{ "error", "result" }`.


        **API Key Permissions Required:** select the **Query affiliate
        participants** checkbox.
      operationId: getAffiliateCpaProgress
      parameters:
        - in: query
          name: iiban
          required: true
          schema:
            description: |-
              Full Kraken account identifier returned by Get Daily Activity.
              Spaced and compact forms are accepted.
            type: string
            minLength: 14
          style: form
          example: AA45N84GQK2VUN7A
      responses:
        '200':
          description: CPA progress for the requested referred trader.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/affiliate.GetCpaProgressResponse'
              examples:
                inProgress:
                  summary: Two independently tracked CPA bounties
                  description: >-
                    Exact measurable values and percentages are returned when
                    progress is available.
                  value:
                    progress:
                      bounties:
                        - bounty_position: 0
                          description: Complete the first CPA requirements
                          reward_amount: '50.00'
                          reward_asset: USDC
                          status: in_progress
                          progress_availability: available
                          conditions:
                            - label: Margin trading volume
                              kind: amount
                              state: incomplete
                              measurement:
                                current: '20.00'
                                target: '100.00'
                                unit: USD
                                percentage: '20'
                            - label: Account verification
                              kind: binary
                              state: complete
                        - bounty_position: 1
                          description: Complete the second CPA requirements
                          reward_amount: '80.00'
                          reward_asset: USDC
                          status: qualified_payment_pending
                          qualified_at: '2026-09-30T14:22:09Z'
                          progress_availability: available
                          conditions:
                            - label: Futures trading volume
                              kind: amount
                              state: complete
                              measurement:
                                current: '1000.00'
                                target: '1000.00'
                                unit: USD
                                percentage: '100'
        '400':
          description: The IIBAN is missing or malformed.
        '401':
          description: Authentication failed.
        '403':
          description: The API key lacks permission or the affiliate plan is not eligible.
        '404':
          description: The referred trader was not found for this affiliate or opted out.
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
    affiliate.GetCpaProgressResponse:
      description: CPA qualification progress for one referred trader.
      type: object
      required:
        - progress
      properties:
        progress:
          $ref: '#/components/schemas/affiliate.ReferralCpaProgress'
    affiliate.ReferralCpaProgress:
      description: CPA qualification progress for one referral relationship.
      type: object
      properties:
        bounties:
          description: >-
            Bounties that can pay or previously paid for this referral. Each

            eligible bounty is reported separately. Region-specific bounties

            that do not apply to the trader are omitted. May be omitted when
            empty.
          type: array
          items:
            $ref: '#/components/schemas/affiliate.CpaBountyProgress'
    affiliate.CpaBountyProgress:
      description: Progress toward one configured CPA bounty.
      type: object
      required:
        - reward_amount
        - reward_asset
        - status
        - progress_availability
      properties:
        bounty_position:
          description: |-
            Current zero-based position of the bounty in the affiliate plan. It
            can change when the plan changes. An omitted value means position 0.
          type: integer
          format: int32
          minimum: 0
        description:
          description: Customer-facing description, when configured.
          type: string
        reward_amount:
          description: >-
            Amount payable to you. Before a payment record exists, this is an

            estimate calculated from the current plan amount, current conversion

            rate, and your affiliate share, so it can change between calls.
            After

            a payment record exists, this is the recorded payment amount.
          allOf:
            - $ref: '#/components/schemas/affiliate.decimalAmount'
        reward_asset:
          description: Asset in which the reward is or will be paid.
          type: string
        status:
          description: |-
            Current qualification and payment state:

            - `in_progress`: not every requirement is complete.
            - `qualified_payment_pending`: every requirement is complete, but
              payment is not complete. The same payment can appear as `pending`,
              `on_hold`, or `action_needed` in payout history.
            - `paid`: the bounty was paid.
            - `expired`: the qualification window or associated payment expired.
            - `no_longer_eligible`: the bounty can no longer be paid; the
              underlying internal reason is not exposed.
            - `not_tracked`: detailed progress is unavailable, for example when
              the bounty was added to the plan after enrollment.

            New values may be added; clients must tolerate values they do not
            yet recognize.
          type: string
          enum:
            - in_progress
            - qualified_payment_pending
            - paid
            - expired
            - no_longer_eligible
            - not_tracked
        qualified_at:
          description: Time at which all requirements for this bounty were completed.
          type: string
          format: date-time
        progress_availability:
          description: |-
            Whether condition-level progress is available. New values may be
            added; clients must tolerate values they do not yet recognize.
          type: string
          enum:
            - available
            - unavailable
        conditions:
          description: Requirements for this bounty. May be omitted when empty.
          type: array
          items:
            $ref: '#/components/schemas/affiliate.CpaConditionProgress'
    affiliate.decimalAmount:
      description: Decimal amount as a string.
      type: string
      pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
    affiliate.CpaConditionProgress:
      description: One requirement for a CPA bounty.
      type: object
      required:
        - label
        - kind
        - state
      properties:
        label:
          description: Customer-facing requirement label.
          type: string
        kind:
          description: Rendering category for the requirement. New values may be added.
          type: string
          enum:
            - amount
            - count
            - verification
            - binary
        state:
          description: Whether this requirement is complete. New values may be added.
          type: string
          enum:
            - incomplete
            - complete
        measurement:
          description: Present for measurable requirements when progress is available.
          allOf:
            - $ref: '#/components/schemas/affiliate.CpaConditionMeasurement'
    affiliate.CpaConditionMeasurement:
      description: Exact progress for one measurable CPA requirement.
      type: object
      required:
        - current
        - target
        - percentage
      properties:
        current:
          description: Current value, capped between zero and the target.
          allOf:
            - $ref: '#/components/schemas/affiliate.decimalAmount'
        target:
          description: Value required to complete the measurable threshold.
          allOf:
            - $ref: '#/components/schemas/affiliate.decimalAmount'
        unit:
          description: Asset code for monetary or volume requirements. Omitted for counts.
          type: string
        percentage:
          description: >-
            Progress from 0 to 100 as a decimal string. A requirement can remain

            incomplete at 100 when it also includes a non-numeric step such as a
            hold period.
          type: string
          pattern: ^(100(\.0+)?|[0-9]{1,2}(\.[0-9]+)?)$
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
