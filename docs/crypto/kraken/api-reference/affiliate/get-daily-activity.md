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
source_url: 'https://docs.kraken.com/api-reference/affiliate/get-daily-activity'
updated_at: 2026-11-13
---

# Get Daily Activity

> Return one page of referred-user activity for the authenticated affiliate.
The API returns activity for the account that owns the key, under its
affiliate plan eligible for this API.

Two ways to request activity (use one per request):

* **Day** — `activity_date` (`YYYY-MM-DD`). One page of enrolled referred
  users who had activity that UTC trade day and have not opted out, plus
  quiet users who enrolled that day and day-wide `totals`. Even a user who
  has never traded has an enrollment-day entry with `enrolled_at` and empty
  `products`. Set `all_users=true` to include all still-enrolled users enrolled by that day, regardless of trading.
  Opted-out users appear as existence stubs only with `all_users=true`; their
  individual activity is excluded from `items` and `totals`. Unenrolled users
  are omitted from `items` only; their activity stays in `totals`.
* **History** — `iiban` (one to ten full Kraken account identifiers,
  comma-delimited) with inclusive `start_date` and `end_date`. The same
  per-day entries for those people only. An opted-out user still enrolled by
  the end of the range returns one existence stub without `activity_date`.
  Day-wide fields (`totals`, `active_users`, `revision`, `estimated`,
  `opted_out`) are omitted.
  Figures are never summed across days.

Sending both variants is a `400`. Dates must be today or one of the previous 89 UTC
days. A future date or a date older than that window is a `400`. An in-window day
with no activity or matching enrollments returns an empty page.

Monetary figures are decimal strings in the top-level `currency` (always `USD`
today): the reporting currency, not the payout asset. `volume` is omitted on
fee-only products (`margin_rollover`). `maker` and `taker` appear only on
execution products (spot, margin, futures, tokenized spot). Instant buy/sell
(`ptl_trading`, `tokenized_equity_ptl_trading`) and financing charges have no
liquidity side. Absence of `maker`/`taker` means unclassified, not zero.
When both are present they cover only the classified portion; the
difference from the product total is unclassified activity.

The `products` map is open-ended: ignore unknown keys. An absent key on a visible
entry means no reported activity for that product. On an opted-out stub,
empty or omitted products means withheld data, not zero activity.
Current keys: `spot_trading`, `ptl_trading`,
`margin_trading`, `margin_rollover`, `futures_order_fill`,
`tokenized_equity_spot_trading`, `tokenized_equity_ptl_trading`. Options is not
included.

Day-wide `totals` include activity from referred users who have not opted out,
including users omitted from `items` because they are not enrolled in your plan.
Activity from people who opted out may appear under `opted_out` as `summary`;
smaller groups are `suppressed`. Daily figures may differ from weekly payments:
totals exclude activity that cannot earn commission, activity from blocked
regions is shown separately, and this API groups by trade date while payments
group by when activity was recorded.

Opted-out stubs retain `referee_reference`, hour-truncated `enrolled_at`,
`opted_out=true`, and the plan's `referral_code` with empty products.
They omit `iiban`, `masked_iiban`, and individual financial or plan-status details.
Stub presence is independent of trading; do not interpret a stub as zero activity.

Use `referee_reference` to match a referred user across days. `masked_iiban` is
the last four characters of the IIBAN and is not unique. Visible entries
also include the full `iiban`, which you can use for history requests. `enrolled_at` is
truncated to the hour.

`revision` (day variant, first page) is when this partner's figures for that UTC
day were last written. Enrollments and opt-out changes do not advance it;
poll the roster even when `revision` is unchanged. Re-check the trailing 35 days
for late events. `estimated` is `true` when amounts for that calendar day are still an estimate.

Examples use synthetic identifiers, not customer account data. Replace
example dates with dates inside the current 90-day window. Empty collections
and zero-valued fields may be omitted; treat missing items or products as empty.

Successful responses are the object itself. Errors are a non-2xx
status with a typed error body, not a wrapped `{ "error", "result" }`.

**API Key Permissions Required:** select the **Query affiliate participants** checkbox.



## OpenAPI

````yaml /openapi/affiliate-rest.yaml get /affiliate/v1/daily-activity
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
  /affiliate/v1/daily-activity:
    get:
      tags:
        - Affiliate
      summary: Get Daily Activity
      description: >-
        Return one page of referred-user activity for the authenticated
        affiliate.

        The API returns activity for the account that owns the key, under its

        affiliate plan eligible for this API.


        Two ways to request activity (use one per request):


        * **Day** — `activity_date` (`YYYY-MM-DD`). One page of enrolled
        referred
          users who had activity that UTC trade day and have not opted out, plus
          quiet users who enrolled that day and day-wide `totals`. Even a user who
          has never traded has an enrollment-day entry with `enrolled_at` and empty
          `products`. Set `all_users=true` to include all still-enrolled users enrolled by that day, regardless of trading.
          Opted-out users appear as existence stubs only with `all_users=true`; their
          individual activity is excluded from `items` and `totals`. Unenrolled users
          are omitted from `items` only; their activity stays in `totals`.
        * **History** — `iiban` (one to ten full Kraken account identifiers,
          comma-delimited) with inclusive `start_date` and `end_date`. The same
          per-day entries for those people only. An opted-out user still enrolled by
          the end of the range returns one existence stub without `activity_date`.
          Day-wide fields (`totals`, `active_users`, `revision`, `estimated`,
          `opted_out`) are omitted.
          Figures are never summed across days.

        Sending both variants is a `400`. Dates must be today or one of the
        previous 89 UTC

        days. A future date or a date older than that window is a `400`. An
        in-window day

        with no activity or matching enrollments returns an empty page.


        Monetary figures are decimal strings in the top-level `currency` (always
        `USD`

        today): the reporting currency, not the payout asset. `volume` is
        omitted on

        fee-only products (`margin_rollover`). `maker` and `taker` appear only
        on

        execution products (spot, margin, futures, tokenized spot). Instant
        buy/sell

        (`ptl_trading`, `tokenized_equity_ptl_trading`) and financing charges
        have no

        liquidity side. Absence of `maker`/`taker` means unclassified, not zero.

        When both are present they cover only the classified portion; the

        difference from the product total is unclassified activity.


        The `products` map is open-ended: ignore unknown keys. An absent key on
        a visible

        entry means no reported activity for that product. On an opted-out stub,

        empty or omitted products means withheld data, not zero activity.

        Current keys: `spot_trading`, `ptl_trading`,

        `margin_trading`, `margin_rollover`, `futures_order_fill`,

        `tokenized_equity_spot_trading`, `tokenized_equity_ptl_trading`. Options
        is not

        included.


        Day-wide `totals` include activity from referred users who have not
        opted out,

        including users omitted from `items` because they are not enrolled in
        your plan.

        Activity from people who opted out may appear under `opted_out` as
        `summary`;

        smaller groups are `suppressed`. Daily figures may differ from weekly
        payments:

        totals exclude activity that cannot earn commission, activity from
        blocked

        regions is shown separately, and this API groups by trade date while
        payments

        group by when activity was recorded.


        Opted-out stubs retain `referee_reference`, hour-truncated
        `enrolled_at`,

        `opted_out=true`, and the plan's `referral_code` with empty products.

        They omit `iiban`, `masked_iiban`, and individual financial or
        plan-status details.

        Stub presence is independent of trading; do not interpret a stub as zero
        activity.


        Use `referee_reference` to match a referred user across days.
        `masked_iiban` is

        the last four characters of the IIBAN and is not unique. Visible entries

        also include the full `iiban`, which you can use for history requests.
        `enrolled_at` is

        truncated to the hour.


        `revision` (day variant, first page) is when this partner's figures for
        that UTC

        day were last written. Enrollments and opt-out changes do not advance
        it;

        poll the roster even when `revision` is unchanged. Re-check the trailing
        35 days

        for late events. `estimated` is `true` when amounts for that calendar
        day are still an estimate.


        Examples use synthetic identifiers, not customer account data. Replace

        example dates with dates inside the current 90-day window. Empty
        collections

        and zero-valued fields may be omitted; treat missing items or products
        as empty.


        Successful responses are the object itself. Errors are a non-2xx

        status with a typed error body, not a wrapped `{ "error", "result" }`.


        **API Key Permissions Required:** select the **Query affiliate
        participants** checkbox.
      operationId: getDailyActivity
      parameters:
        - in: query
          name: activity_date
          schema:
            description: >-
              Day variant: UTC trade date. Today or one of the previous 89 UTC
              days.

              Mutually exclusive with `iiban`, `start_date`, and `end_date`.
            type: string
            pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$
            minLength: 10
            maxLength: 10
          style: form
          example: '2026-09-16'
        - in: query
          name: iiban
          schema:
            description: >-
              History variant: one to ten full IIBANs (Kraken account
              identifiers),

              comma-delimited. Empty, duplicate, or malformed values are a
              `400`.

              Validity is a format check only, not account existence. An
              opted-out

              user still enrolled by the end of the range returns one existence
              stub

              without `activity_date`. Unknown or unattributed identifiers
              return an

              empty result. Visible entries return the full iiban; opted-out
              stubs omit it.
            type: string
            minLength: 1
            maxLength: 350
          style: form
          example: AA45N84GQK2VUN7A,CC34N84GQK2VUN7C
        - in: query
          name: start_date
          schema:
            description: >-
              History variant: inclusive start, `YYYY-MM-DD`, in the last 90 UTC
              days.

              Required with `iiban` and `end_date`.
            type: string
            pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$
            minLength: 10
            maxLength: 10
          style: form
          example: '2026-08-20'
        - in: query
          name: end_date
          schema:
            description: >-
              History variant: inclusive end, `YYYY-MM-DD`, in the last 90 UTC
              days.

              Required with `iiban` and `start_date`. Must be on or after
              `start_date`.
            type: string
            pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$
            minLength: 10
            maxLength: 10
          style: form
          example: '2026-09-16'
        - in: query
          name: all_users
          schema:
            description: >-
              Day variant only. Include quiet users enrolled in your affiliate
              plan

              by the requested date who are still enrolled, including those
              enrolled

              more than 90 days ago. Users without reportable activity have
              empty

              products. Trading totals, active_users, and revision are
              unchanged.

              Using all_users=true with history returns 400.

              Keep this value unchanged when following next_cursor.
            type: boolean
            default: false
          style: form
        - in: query
          name: cursor
          schema:
            description: >-
              Value from `next_cursor` in a previous response. Pass it unchanged
              to

              request the next page; do not parse or construct it. A daily
              cursor

              used for a full-roster request, or vice versa, returns 400.
            type: string
            minLength: 1
          style: form
        - in: query
          name: limit
          schema:
            description: >-
              Page size. Defaults to 50 when omitted. Values over 200 are
              rejected.
            type: integer
            format: int32
            minimum: 1
            maximum: 200
            default: 50
          style: form
          example: 50
      responses:
        '200':
          description: One page of affiliate daily activity.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/affiliate.GetDailyActivityResponse'
              examples:
                daily:
                  summary: Daily trading activity
                  description: >-
                    Default day request. Opted-out users are omitted from items.
                    All identifiers are synthetic.
                  value:
                    activity_date: '2026-09-16'
                    currency: USD
                    revision: '2026-09-17T00:14:02Z'
                    generated_at: '2026-09-17T12:01:04Z'
                    active_users: 1
                    totals:
                      spot_trading:
                        volume: '42110.20'
                        fees: '38.20'
                        commission: '11.46'
                        event_count: 12
                        maker:
                          volume: '18400.00'
                          fees: '9.20'
                          commission: '2.76'
                          event_count: 5
                        taker:
                          volume: '23710.20'
                          fees: '29.00'
                          commission: '8.70'
                          event_count: 7
                    items:
                      - masked_iiban: UN7A
                        referee_reference: jsd6ggr6qjrzmemn
                        plans:
                          - referral_code: EXAMPLE1
                            campaign: tg-vip
                            referral_level: 1
                            enrolled_at: '2026-03-14T09:00:00Z'
                            status: active
                            earning: true
                            expires_at: '2027-03-14T09:21:07Z'
                            products:
                              spot_trading:
                                volume: '42110.20'
                                fees: '38.20'
                                commission: '11.46'
                                event_count: 12
                                maker:
                                  volume: '18400.00'
                                  fees: '9.20'
                                  commission: '2.76'
                                  event_count: 5
                                taker:
                                  volume: '23710.20'
                                  fees: '29.00'
                                  commission: '8.70'
                                  event_count: 7
                        iiban: AA45N84GQK2VUN7A
                    limit: 50
                    opted_out:
                      suppressed: {}
                enrollment:
                  summary: Enrollment without trading
                  description: >-
                    Default day request on the enrollment day, with no
                    reportable activity. Empty products and zero active_users
                    may be omitted.
                  value:
                    activity_date: '2026-09-15'
                    currency: USD
                    generated_at: '2026-09-15T12:01:04Z'
                    items:
                      - iiban: BB12N84GQK2VUN7B
                        masked_iiban: UN7B
                        referee_reference: example_quiet_user
                        plans:
                          - referral_code: EXAMPLE1
                            referral_level: 1
                            enrolled_at: '2026-09-15T09:00:00Z'
                            status: active
                            earning: true
                    limit: 50
                    opted_out:
                      suppressed: {}
                roster:
                  summary: 'Full roster: trading, quiet and opted-out users'
                  description: >-
                    Request activity_date=2026-09-16&all_users=true. Three users
                    are listed, but only one counts toward active_users. All
                    identifiers are synthetic.
                  value:
                    activity_date: '2026-09-16'
                    currency: USD
                    revision: '2026-09-17T00:14:02Z'
                    generated_at: '2026-09-17T12:01:04Z'
                    active_users: 1
                    totals:
                      spot_trading:
                        volume: '42110.20'
                        fees: '38.20'
                        commission: '11.46'
                        event_count: 12
                    items:
                      - masked_iiban: UN7A
                        referee_reference: jsd6ggr6qjrzmemn
                        plans:
                          - referral_code: EXAMPLE1
                            referral_level: 1
                            enrolled_at: '2026-03-14T09:00:00Z'
                            status: active
                            earning: true
                            products:
                              spot_trading:
                                volume: '42110.20'
                                fees: '38.20'
                                commission: '11.46'
                                event_count: 12
                        iiban: AA45N84GQK2VUN7A
                      - iiban: BB12N84GQK2VUN7B
                        masked_iiban: UN7B
                        referee_reference: example_quiet_user
                        plans:
                          - referral_code: EXAMPLE1
                            referral_level: 1
                            enrolled_at: '2026-09-15T09:00:00Z'
                            status: active
                            earning: true
                      - referee_reference: example_opted_out_user
                        opted_out: true
                        enrolled_at: '2026-08-20T09:00:00Z'
                        plans:
                          - referral_code: EXAMPLE1
                    limit: 50
                    opted_out:
                      suppressed: {}
                history:
                  summary: History with an opted-out user
                  description: >-
                    History for two known referred users. The opted-out user
                    appears once for the range, without an activity_date or
                    account identifier.
                  value:
                    currency: USD
                    generated_at: '2026-09-17T12:01:04Z'
                    items:
                      - masked_iiban: UN7A
                        referee_reference: jsd6ggr6qjrzmemn
                        plans:
                          - referral_code: EXAMPLE1
                            referral_level: 1
                            enrolled_at: '2026-03-14T09:00:00Z'
                            status: active
                            earning: true
                            products:
                              spot_trading:
                                volume: '42110.20'
                                fees: '38.20'
                                commission: '11.46'
                                event_count: 12
                        iiban: AA45N84GQK2VUN7A
                        activity_date: '2026-09-16'
                      - referee_reference: example_opted_out_user
                        opted_out: true
                        enrolled_at: '2026-08-20T09:00:00Z'
                        plans:
                          - referral_code: EXAMPLE1
                    limit: 50
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
    affiliate.GetDailyActivityResponse:
      description: One page of affiliate daily activity.
      type: object
      required:
        - currency
        - generated_at
        - limit
      properties:
        activity_date:
          description: Day variant only. The UTC trade date every item shares.
          type: string
          pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$
        currency:
          description: Reporting currency for every monetary figure. Always `USD` today.
          type: string
          example: USD
        revision:
          description: >-
            Day variant, first page only. When this partner's figures for that
            UTC day were

            last updated. Omitted when there is no activity, and on later pages.
            A later

            value on re-fetch means this partner's figures moved.
          type: string
          format: date-time
        generated_at:
          type: string
          format: date-time
        active_users:
          description: >-
            Day variant, first page only. Count of enrolled users sharing
            reportable

            trading activity that day. Excludes quiet users and opted-out users,
            even

            when they appear in the roster. May be omitted when zero. Omitted on

            later pages; not a roster size or remaining-page count.
          type: integer
          format: int64
          minimum: 0
        totals:
          description: >-
            Day variant, first page only. Totals for referred users who have not

            opted out, including people omitted from `items` because they are
            not

            enrolled in your plan. An empty map on a later page is omission, not

            a zero day.
          type: object
          additionalProperties:
            $ref: '#/components/schemas/affiliate.ProductActivity'
        next_cursor:
          description: >-
            Present when more results exist. Pass as `cursor` on the next
            request.
          type: string
        items:
          description: Referred users for this page. May be omitted when empty.
          type: array
          items:
            $ref: '#/components/schemas/affiliate.DailyActivityItem'
        estimated:
          description: >-
            Day variant, first page only. Amounts for this date are an estimate
            of that

            calendar day, including the opted-out remainder. Omitted when exact.
          type: boolean
        opted_out:
          $ref: '#/components/schemas/affiliate.GatedActivity'
          description: >-
            Day variant, first page only. Opted-out remainder. Day-wide payable
            is

            `totals` plus `summary` when `summary` is set.
        limit:
          description: >-
            Page size used for this response. Echo of request `limit` after the
            default of 50.
          type: integer
          format: int32
          minimum: 1
          maximum: 200
    affiliate.ProductActivity:
      description: >-
        Activity for one product. The map key names the product.

        The key set is open-ended: ignore unknown keys. An absent key on a
        visible

        entry means no reported activity; on an opted-out stub it means withheld
        data.

        The product's volume, fees, event_count, and commission cover payable

        activity only; geo_blocked is shown separately and is not included in

        those product totals.
      type: object
      required:
        - fees
        - commission
        - event_count
      properties:
        volume:
          $ref: '#/components/schemas/affiliate.decimalAmount'
          description: Absent for fee-only products such as `margin_rollover`.
        fees:
          $ref: '#/components/schemas/affiliate.decimalAmount'
        commission:
          $ref: '#/components/schemas/affiliate.decimalAmount'
        event_count:
          type: integer
          format: int32
          minimum: 0
        geo_blocked:
          $ref: '#/components/schemas/affiliate.GeoBlockedActivity'
        maker:
          $ref: '#/components/schemas/affiliate.MakerTakerActivity'
        taker:
          $ref: '#/components/schemas/affiliate.MakerTakerActivity'
    affiliate.DailyActivityItem:
      description: >-
        One referred user's activity by plan and product, or an opted-out
        existence

        stub with referee_reference, opted_out, enrolled_at, and plan
        referral_code.
      type: object
      required:
        - plans
        - referee_reference
      properties:
        activity_date:
          description: >-
            History variant only. Stamps this entry's own day. The day variant
            omits it

            because every item shares the top-level `activity_date`. Also
            omitted on

            opted-out history stubs, which do not represent a trading day.
          type: string
          pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$
        iiban:
          description: >-
            Full Kraken account identifier for a referred user sharing activity.

            Returned on daily, full-roster, and history entries, including quiet
            enrollments.

            Can be used in person-history requests. Omitted on opted-out stubs.
          type: string
        masked_iiban:
          description: >-
            Last four characters of the IIBAN, retained for compatibility. Not
            unique;

            use iiban to match a Kraken account or referee_reference to track
            the enrollment.

            Omitted on opted-out stubs.
          type: string
        plans:
          type: array
          items:
            $ref: '#/components/schemas/affiliate.ReferralPlan'
        referee_reference:
          description: |-
            Stable reference for the same referred user under your account. It
            cannot identify a Kraken account or be matched across affiliates.
            Retained unchanged on opted-out stubs.
          type: string
        opted_out:
          description: >-
            True for an existence stub. Empty products means withheld data, not
            zero.
          type: boolean
        enrolled_at:
          description: >-
            Enrollment time on opted-out stubs, truncated to the hour. Visible
            entries use `plans[].enrolled_at` instead.
          type: string
          format: date-time
        estimated:
          description: >-
            History variant: amounts for this date are an estimate of that
            calendar day.
          type: boolean
    affiliate.GatedActivity:
      description: >-
        Contains `suppressed` when qualifying opted-out enrollments exist and
        zero

        or one user has reportable activity; contains `summary` for two or more.

        The parent field is omitted when neither qualifying opted-out
        enrollments

        nor reportable opted-out activity exists. Applies to both ordinary day
        and

        full-roster requests, independently of which users fit on the page.
      type: object
      oneOf:
        - type: object
          required:
            - suppressed
          properties:
            suppressed:
              type: object
        - type: object
          required:
            - summary
          properties:
            summary:
              type: object
              required:
                - active_participants
              properties:
                active_participants:
                  type: integer
                  format: int64
                  minimum: 0
                products:
                  type: object
                  additionalProperties:
                    $ref: '#/components/schemas/affiliate.ProductActivity'
    affiliate.decimalAmount:
      description: Decimal amount as a string.
      type: string
      pattern: ^[+-]?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))$
    affiliate.GeoBlockedActivity:
      description: |-
        Activity from regions where commission cannot be paid. It is shown
        separately from payable activity and earns zero commission.
      type: object
      required:
        - fees
        - event_count
      properties:
        volume:
          $ref: '#/components/schemas/affiliate.decimalAmount'
          description: Absent for fee-only products, matching `ProductActivity.volume`.
        fees:
          $ref: '#/components/schemas/affiliate.decimalAmount'
        event_count:
          type: integer
          format: int32
          minimum: 0
    affiliate.MakerTakerActivity:
      description: >-
        Payable activity for one liquidity role. Present only on execution
        products.

        Maker plus taker cover the classified portion when both are present. The

        difference from the product total is unclassified activity.
      type: object
      required:
        - volume
        - fees
        - commission
        - event_count
      properties:
        volume:
          $ref: '#/components/schemas/affiliate.decimalAmount'
        fees:
          $ref: '#/components/schemas/affiliate.decimalAmount'
        commission:
          $ref: '#/components/schemas/affiliate.decimalAmount'
        event_count:
          type: integer
          format: int32
          minimum: 0
    affiliate.ReferralPlan:
      description: >-
        An affiliate plan through which this user was referred. On opted-out
        stubs,

        only referral_code is returned; empty products may be omitted.
      type: object
      required:
        - referral_code
      properties:
        referral_code:
          description: Your referral code for this plan.
          type: string
        campaign:
          description: Optional campaign tag from the referral code used at sign-up.
          type: string
        referral_level:
          description: Currently `1` for a user referred under your affiliate plan.
          type: integer
          format: int32
          minimum: 0
        enrolled_at:
          description: >-
            Enrollment time for a user sharing activity, truncated to the hour
            (RFC3339). On opted-out stubs, use item-level `enrolled_at` instead.
          type: string
          format: date-time
        status:
          description: |-
            Other values may be returned. `active` and `completed` can earn
            commission; check `earning` for the current result.
          type: string
        earning:
          description: >-
            Whether activity under this plan earns commission for you. True
            while

            `status` is `active` or `completed`.
          type: boolean
        expires_at:
          type: string
          format: date-time
        products:
          description: >-
            Reported activity by product. May be omitted when empty; on
            opted-out stubs, activity is withheld.
          type: object
          additionalProperties:
            $ref: '#/components/schemas/affiliate.ProductActivity'
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
