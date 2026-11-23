---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/caas/markup/integration-guide
api_type: Guide
updated_at: 2026-11-23 18:42:04.513391
---

# Markup Integration Guide

The Markup API lives under **`/sapi/v1/vip/caas/commission/*`**, in two groups:

- **Fee groups** — set the markup each of your sub-accounts pays on top of Binance's base
  commission.
- **Reportings** — read back the markup income those sub-accounts generated.

This guide covers both, in the order you would build them. Read
[Overview](/products/caas/markup/overview) for the commercial model and
[Getting Started](/products/caas/markup/getting-started) for base endpoints and signing first — this
page assumes both.

---

## Table of Contents

1. [Before You Begin](#1-before-you-begin)
2. [How the Model Works](#2-how-the-model-works)
3. [Integration Steps](#3-integration-steps)
4. [Parameter Placement and Content Types](#4-parameter-placement-and-content-types)
5. [Reporting](#5-reporting)
6. [Changing Rates Later](#6-changing-rates-later)
7. [Response Envelope](#7-response-envelope)
8. [Going Live](#8-going-live)

---

## 1. Before You Begin

### Prerequisites

- A **live CAAS integration**. Markup is enabled on top of one and uses the same master account —
  see [CAAS Getting Started](/products/caas/getting-started).
- **The markup model uplifted on your master account by the Link team.** This is an access gate, not
  only a commercial setting — until the uplift is applied, these endpoints are not available to your
  master account. Markups are granted case-by-case only, on application to
  [link@binance.com](mailto:link@binance.com). See [Overview](/products/caas/markup/overview).
- **Sub-accounts already created.** Fee groups are populated with sub-account user IDs, so the
  sub-accounts must exist before you can assign them.
- **Each sub-account's KYC passed** through [KYC SaaS](/products/kyc-saas/overview). A sub-account
  cannot trade until it has, so assigning it to a fee group has no effect before that point.

### API key

Every endpoint on this page is `SIGNED` and requires the **master account's** API key — not a
sub-account key. They split by security type:

- **`TRADE`** — Create Fee Group, Update Fee Group Commission, Assign Members, Unassign Members,
  Delete Fee Group. These need the key's **trade** permission enabled.
- **`USER_DATA`** — Query Fee Groups, Query Fee Group Members, Query One Member's Fee Group, and the
  reporting endpoints.

Every one of them carries an IP weight of **1**.

Note that **markup and revenue share cannot be combined**, and markup applies to the **spot order
book only**. If your account is on revenue share, nothing on this page takes effect until the model
is switched.

---

## 2. How the Model Works

Binance charges the sub-account a base commission. Your markup is added **on top** of it, and the
excess is yours. From [Overview](/products/caas/markup/overview): a partner marking up to 0.30%
maker/taker leaves 0.10% with Binance and keeps 0.20%.

Three properties of the model drive the whole integration:

| Property                         | Consequence for your integration                                             |
| -------------------------------- | ---------------------------------------------------------------------------- |
| Rates are set **per fee group**  | You never set a rate on a user. You put users in a group and rate the group. |
| Maker and taker are **separate** | `makerMarkup` and `takerMarkup` are independent fields on every write.       |
| A sub-account has **one** group  | `member-fee-group` takes a single `subUserId` and returns a single group.    |

So the unit of configuration is the group, and the unit of membership is the sub-account.

<!-- Sourced from Jordan Liu (VIP Products), 2026-09-10. The maximum markup rate is deliberately
     NOT published: Esmond's call, 2026-09-10 — it is internal, configured per broker, and
     communicated only by the Link team or the partner's Account Manager. Do not add a figure here
     even if one appears in a PRD. The settlement TIME is also absent, still pending Duy/Leo. -->

### Rules that affect your fees and income

| Rule                                                                                                    | Detail                                                                                              |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Markup replaces revenue share**                                                                       | Your referral rebate is switched off once markup is activated. The two never run together.          |
| **A sub-account in no fee group trades at base rate**                                                   | No markup, and no rebate. It is not rejected, so a missed assignment is silent.                     |
| **Spot order book only, filled and settled trades**                                                     | Unfilled or unsettled orders accrue nothing.                                                        |
| **The BNB fee discount does not apply**                                                                 | It is unavailable to sub-account trading under a markup fee group. Do not model it into your rates. |
| **Fee groups are capped**                                                                               | 3 per partner, raisable to 20 on request through the Link team.                                     |
| **Income is paid in USDT to your master account**                                                       | Converted at end of day and distributed to the broker master account. Always USDT.                  |
| **Non-USDT pairs convert at the 00:00 UTC daily close of the trade date, and you bear the FX movement** | This is what `markupConvertRate` and `markupConvertTime` record on each reporting row.              |

**The maximum markup rate available to you is set per partner and is not published.** Get it from
the Link team or your Account Manager before designing your fee tiers, along with confirmation of
how many fee groups you may create.

Reporting is **T-1**: data is available up to the previous day, so same-day trading is not
queryable. See [section 5](#5-reporting).

---

## 3. Integration Steps

### Step 1 — Create a fee group

`POST /sapi/v1/vip/caas/commission/fee-groups`

Required: `groupName` (max 32 characters), `makerMarkup`, `takerMarkup`, `timestamp`. Rates are
decimals, so `0.002` is 0.2%.

The response returns a **`groupCode`** — for example `FG001` — plus the name, both rates,
`subAccountCount`, `createdTime` and `updatedTime`.

**`groupCode` is assigned by Binance, not chosen by you**, and every later call identifies the group
by `groupCode` rather than `groupName`, so persist it when you create the group. No endpoint looks a
group up by name.

### Step 2 — Assign sub-accounts to the group

`POST /sapi/v1/vip/caas/commission/fee-groups/members`

`groupCode` goes in the **query string**; the sub-accounts go in a **JSON body** as `subUserIds`, an
array of integers.

:::warning

**`subUserIds` takes spot UIDs — not CAAS sub-account IDs.** Send each sub-account's **spot UID**,
not the longer `subAccountId` that the CAAS sub-account APIs return and accept.

This is easy to get wrong, because the field is called `subUserId` here and `subAccountId` in the
CAAS APIs, and the reference example value resembles neither. The same spot UID is what
`member-fee-group` and the `subUserId` reporting filters expect.

To retrieve a sub-account's spot UID, call `GET /api/v3/account` with **that sub-account's own API
key** and read the `uid` field.

:::

:::warning

**`subUserIds` takes at most 10 entries per request** — on both Assign Members and Unassign Members.
Batch your migration in chunks of 10.

Exceeding it returns
`-1102 Mandatory parameter 'subUserIds' was not sent, was empty/null, or malformed.` — which says
nothing about size, so it reads like a serialisation bug. If you get `-1102` on a well-formed array,
count the entries first. The limit is enforced before the `groupCode` is looked up, so an oversized
batch fails even when everything else is correct.

:::

**A `200` does not mean every sub-account was assigned.** The response reports partial success:

- `successCount` — how many were assigned
- `failedList` — one entry per failure, each with `subUserId` and `errorMessage` (for example
  `Sub-account does not belong to master`)

Read `failedList` and reconcile it. Treating the HTTP status as the outcome will silently leave
sub-accounts on the base rate.

### Step 3 — Verify membership

Two read paths, depending on the question:

| Question                            | Endpoint                                              | Key parameter        |
| ----------------------------------- | ----------------------------------------------------- | -------------------- |
| Which group is this sub-account in? | `GET /sapi/v1/vip/caas/commission/member-fee-group`   | `subUserId`          |
| Who is in this group?               | `GET /sapi/v1/vip/caas/commission/fee-groups/members` | `groupCode` + paging |
| What groups do I have?              | `GET /sapi/v1/vip/caas/commission/fee-groups`         | paging only          |

`member-fee-group` takes a single `subUserId` and needs no paging, which makes it the
straightforward call when reconciling a `failedList`. They all carry the same IP weight.

### Step 4 — Read markup income back

Once the sub-accounts trade, use the reporting endpoints in [section 5](#5-reporting).

---

## 4. Parameter Placement and Content Types

The write endpoints are **not** consistent with each other, so build against this table rather than
by analogy from one endpoint to the next:

| Endpoint                        | Method   | `groupCode` / `timestamp` | Payload                             |
| ------------------------------- | -------- | ------------------------- | ----------------------------------- |
| Create Fee Group                | `POST`   | in the body               | `application/x-www-form-urlencoded` |
| Update Fee Group Commission     | `PUT`    | in the **query string**   | `application/json` (rates only)     |
| Assign Members to Fee Group     | `POST`   | in the **query string**   | `application/json` (`subUserIds`)   |
| Unassign Members from Fee Group | `DELETE` | in the **query string**   | `application/json` (`subUserIds`)   |
| All read endpoints              | `GET`    | in the query string       | none                                |

Note in particular that **Create** puts everything in a form-encoded body, while the other three
writes split parameters across the query string and a JSON body. `recvWindow` follows `timestamp` in
each case and may not exceed `60000`.

:::warning

**On the three JSON-body endpoints, sign the query string only — do not include the request body in
the signed payload.** Signing the query string concatenated with the JSON body returns
`-1022 Signature for this request is not valid.`

This differs from the form-encoded convention, where body parameters are part of the signed string.
Verified live on `PUT .../fee-groups/commission`, 2026-09-09.

:::

Send the JSON body even when its values are irrelevant — omitting it altogether on
`PUT .../commission` returns **HTTP 500** with `-1000 An unknown error occurred`, rather than a
`-1102` for the missing required field.

---

## 5. Reporting

Both reporting endpoints are `USER_DATA`, and both are paginated with **`pageIndex`** (starting
at 1) and **`pageSize`** (1-100). `startTime`, `endTime`, `pageIndex` and `pageSize` are all
**required** on both — there is no default window.

### Aggregations — daily totals

`GET /sapi/v1/vip/caas/commission/markup-trade-aggregations`

One row per date, per sub-account, **per fee group**. Optional `groupCode` and `subUserId` filters.

| Field                                    | What it is                             |
| ---------------------------------------- | -------------------------------------- |
| `date`                                   | The aggregation date                   |
| `subUserId`, `groupCode`, `groupName`    | Who, and under which group's rates     |
| `totalVolumeUsdt`                        | Traded volume for the row, in USDT     |
| `markupMakerIncome`, `markupTakerIncome` | Your income, split by fill side        |
| `markupAsset`                            | The asset the markup is denominated in |

Maker and taker income are reported separately, matching the two rates you configured.

Rows are keyed by date, sub-account **and** fee group, so do not assume `subUserId` plus `date`
identifies a single row.

### Details — trade level

`GET /sapi/v1/vip/caas/commission/markup-trade-details`

One row per fill, with an additional optional `symbol` filter. Alongside the order and trade fields
(`orderId`, `product`, `symbol`, `tradeSide`, `tradeType`, `price`, `qty`, `quoteQty`), each row
carries the full fee breakdown:

| Field                                    | What it is                                 |
| ---------------------------------------- | ------------------------------------------ |
| `baseRate`                               | Binance's own commission rate on the fill  |
| `markupRate`                             | Your markup rate applied to that fill      |
| `totalFeeRate`                           | What the sub-account actually paid         |
| `markupAmount`                           | Your income on the fill, in `markupAsset`  |
| `markupAmountUsdt`                       | The same amount in USDT                    |
| `markupConvertRate`, `markupConvertTime` | The rate and time used for that conversion |

`markupAmount` is denominated in `markupAsset`; `markupAmountUsdt` is its USDT equivalent. Where the
two differ, `markupConvertRate` and `markupConvertTime` record the conversion that was applied —
reconcile against those two fields rather than recomputing from the fill price.

`totalFeeRate` is the sum of the two rates — in the reference example, `0.001` base plus `0.003`
markup gives `0.004`. Use `baseRate` and `markupRate` rather than deriving your share from
`totalFeeRate`, since only `markupRate` is yours.

:::note

**`tradeType` is the fill side that determined the rate**, not the order type you submitted. A limit
order fills as a taker if the book moves before it rests, so reconcile income against `tradeType` —
never against how the order was placed.

:::

---

## 6. Changing Rates Later

`PUT /sapi/v1/vip/caas/commission/fee-groups/commission` updates `makerMarkup` and `takerMarkup` for
a whole group, identified by `groupCode` in the query string. Both rates are required, so send the
unchanged one too.

Because rates live on the group, moving one sub-account onto different rates means unassigning it
and assigning it to another group, not editing anything on the user.

To retire a group:

1. `DELETE /sapi/v1/vip/caas/commission/fee-groups/members` for every member.
2. `DELETE /sapi/v1/vip/caas/commission/fee-groups` for the group itself.

:::warning

**A group cannot be deleted while it still has members.** The delete rejects until every sub-account
has been unassigned. Check `subAccountCount`, or page through `fee-groups/members`, before
attempting it.

:::

The API has **no rename endpoint** — `groupName` is set at creation and is not editable through any
of the endpoints on this page.

---

## 7. Response Envelope

A successful call wraps its result like this:

```json
{
  "status": "OK",
  "type": "GENERAL",
  "code": "000000000",
  "data": {}
}
```

:::warning

**Success is `"000000000"` — nine zeros.** Branching on `"000000"` treats every successful call as a
failure. There is also no `message` field on success, and `status` and `type` are present.

Verified live on `fee-groups`, `markup-trade-aggregations` and `markup-trade-details`, 2026-09-09.
If you built against an earlier version of the API Reference, which showed
`{"code": "000000", "message": "success"}`, re-check your success test — the examples have since
been corrected.

:::

Failures use the **standard Binance error envelope instead** — a negative numeric `code` and `msg`,
with a real HTTP status:

```json
{ "code": -9000, "msg": "Markup configuration not found" }
```

So a client has to handle two different response shapes on the same endpoint, and cannot simply read
`code` in one place.

| Observed                                 | Meaning                                                      |
| ---------------------------------------- | ------------------------------------------------------------ |
| `-9000` `Markup configuration not found` | Returned by `member-fee-group` for a sub-account in no group |
| `-31002` `illegal parameter`             | Seen on `PUT .../commission` with a non-existent `groupCode` |

:::warning

**Querying a sub-account that is in no fee group is an error, not an empty result.**
`member-fee-group` returns `-9000 Markup configuration not found` rather than a row indicating "no
group". Handle it as an expected outcome when reconciling, not as a failure.

**`-9000` does not tell you which of several things went wrong.** The same code comes back for a
sub-account that simply has no fee group, for one that is not under your master, and for an
identifier that is not a spot UID at all. If you get it unexpectedly, check the identifier before
concluding the sub-account is unassigned.

:::

This envelope is specific to the Markup endpoints. Most `/sapi/*` endpoints return the result object
directly, so a client written against those will read the response as empty — unwrap `data` before
parsing.

<!-- TODO(sulyn / Link eng): two items here.

     1. [RESOLVED 2026-09-10] the spec's response envelope was wrong on all 10 endpoints --
        code "000000" plus a message field, where the service returns "000000000" with status/type
        and no message. Fixed in docs/products/vip-caas/openapi/rest-api/**.yaml and re-bundled.
        NOTE the internal SAPI+API Confluence page carries the same defect and is its origin, so
        it will be re-copied unless that page is corrected too.

     2. The failure codes are still not enumerated. -9000 and -31002 above were observed, not
        documented, and -31002 "illegal parameter" is too generic to branch on -- it is not even
        certain whether it referred to the groupCode or to the body. Still needed: duplicate
        groupName, sub-account outside the master, deleting a non-empty group, and exceeding the
        markup cap. -->

---

## 8. Going Live

- [ ] Markup model approved for the account, and revenue share confirmed switched off.
- [ ] Master-account API key with **trade** permission; sub-account keys are not used here.
- [ ] Every fee group created, with its `groupCode` persisted on your side.
- [ ] Every sub-account assigned, and **`failedList` empty or reconciled** on each assign call.
- [ ] `member-fee-group` spot-checked for a sample of sub-accounts, confirming the group and rates.
- [ ] Maker and taker rates verified independently — they are separate fields and a single test fill
      only exercises one of them.
- [ ] Both reporting endpoints called with an explicit `startTime` / `endTime` and paging, and
      reconciled against your own records.
- [ ] Envelope unwrapping and `code` checking implemented.
- [ ] Reconciliation keyed on date **and** sub-account **and** fee group, not date plus sub-account
      alone.
- [ ] Where `markupAsset` is not USDT, income reconciled against `markupConvertRate` and
      `markupConvertTime`.
- [ ] Commercial parameters confirmed with your Account Manager — maximum markup rate, number of fee
      groups, settlement schedule, and how BNB fee discounts interact with markup.

<!-- SOURCING RULE FOR THIS PAGE (Esmond, 2026-09-09)

     Everything published here comes from ONE OF THREE sources only:
       (a) the shipped spec, docs/products/vip-caas/openapi/rest-api/**.yaml
       (b) behaviour tested live against api.binance.com on 2026-09-09
       (c) named product-owner confirmation, attributed and dated below
           -- added 2026-09-10 (Esmond) once the PRD's commercial rules were confirmed
           by the owning PM. A PRD, a Confluence page or an internal deck is STILL NOT
           a source; only a named person answering a specific question.
     plus the pre-existing Overview / Getting Started pages.

     PRD "CAAS Basic (Exchange Link) Commission Markup v1.0" (Confluence 499409522) is NOT used
     as a source for anything on this page, because it is demonstrably stale:

     1. Its whole API surface diverged. It specifies /sapi/v1/caas/fee/group and
        /sapi/v1/caas/fee/markupRecord with feeGroupId/subAccountId/limit/page and fields
        totalVolume/makerMarkupIncome/takerMarkupIncome/asset, plus a create response carrying
        baseSpotMaker/baseSpotTaker/totalSpotMaker/totalSpotTaker. The shipped API is
        /sapi/v1/vip/caas/commission/* with groupCode/subUserId/pageIndex/pageSize and
        totalVolumeUsdt/markupMakerIncome/markupTakerIncome/markupAsset, and none of those four
        base/total rate fields exist.
     2. At least one BUSINESS rule also failed to survive: the PRD says querying an unassigned
        sub-account returns a feeGroupId "DEFAULT" sentinel. Live returns -9000 "Markup
        configuration not found" (tested).

     These PRD-stated rules were therefore REMOVED from the page and need confirmation against the
     implementation before any of them is republished:
       - [NOT FOR PUBLICATION 2026-09-10] markup rate cap. Jordan Liu (VIP Products) confirms a
         max IS configured per broker, but did NOT confirm the PRD's 10% default. Esmond's call:
         treat the value as INTERNAL -- shared only by the Link team or the Account Manager. Do
         not publish a figure here. The error code returned when a group exceeds the cap is
         still unknown from every source.
       - [CONFIRMED 2026-09-10, Jordan Liu] fee groups per partner: 3 max, raisable to 20 on
         request. Published in section 2 without naming the internal admin surface.
       - [RESOLVED 2026-09-10] max subUserIds per assign/unassign request: the PRD's 100 is
         WRONG. The live limit is 10, confirmed three ways -- black-box bisection (10 accepted,
         11 rejected), the implementation's own @Size(max = 10) on
         AssignFeeGroupMembersRequest.subUserIds, and Duy (Spot-ES-Tech): capped at 10 for
         system performance, agreed before release. Now published in section 3 and added to the
         spec as maxItems: 10 on both endpoints.
       - [RESOLVED 2026-09-10] status enum: there is NO status field. The PRD's
         PENDING|DISTRIBUTED never shipped, and the field the spec declared on
         markup-trade-aggregations was a phantom -- Duy confirmed CaasSubCommissionInfo has no
         status, and the spec's row schema otherwise matched that VO field for field. The
         phantom field has been removed from the spec. Note the live envelope does carry a
         top-level status: "OK", which is a different thing and not per-row.
       - [CONFIRMED 2026-09-10, Jordan Liu] reporting is T-1 only. Published in section 2.
       - [PARTLY CONFIRMED 2026-09-10, Jordan Liu] income is converted at end of day and
         distributed to the broker master account, always in USDT. The exact distribution TIME
         is NOT confirmed -- Jordan deferred it to Duy/Leo, so the PRD's "T+1" stays
         unpublished. Mechanism published in section 2; no time given.
       - [CONFIRMED 2026-09-10, Jordan Liu] the BNB discount is NOT available under markup.
         Published in section 2. Note this remains the OPPOSITE of the Link & Trade OMS markup
         family, so it must never be inferred from that family.
       - [CONFIRMED 2026-09-10, Jordan Liu] non-USDT pairs convert at the 00:00 UTC daily close
         of the trade date and the broker bears the FX movement. Published in section 2.
         Jordan hedged with "should be", so re-confirm if a partner disputes a figure.
       - [CONFIRMED 2026-09-10, Jordan Liu] settlement asset is always USDT. Published in
         section 2.
       - [CONFIRMED 2026-09-10, Jordan Liu] a sub-account in no fee group trades at base rate
         with no markup AND no rebate -- silently, not rejected. Published in section 2.
       - [CONFIRMED 2026-09-10, Jordan Liu] filled and settled spot trades only. Published in
         section 2.
       - [CONFIRMED 2026-09-10, Jordan Liu] the referral rebate is turned OFF once markup is
         activated. Published in section 2.

     Also still unknown from every source: members per fee group, and the error code when a group
     exceeds the configured cap.

     All 13 are PARKED as numbered follow-up questions for the Link team / PM, with PRD line
     references and a priority order, in the TechOps working notes
     (20260909_caas_markup_open_questions_link_team). Republish each one only once it is
     confirmed against the implementation -- not against the PRD.

     TODO(sulyn): also still needed here are the commercial onboarding steps (application,
     approval, model switch) with their real owners and lead times -- this checklist is derived
     from the API surface, not from a runbook. -->

---

## Where to go next

| If you need                   | Go to                                                                   |
| ----------------------------- | ----------------------------------------------------------------------- |
| The endpoint reference        | [Markup REST API](/catalog/vip-and-institutional-vip-caas/api/rest-api) |
| Base endpoints and signing    | [Getting Started](/products/caas/markup/getting-started)                |
| The commercial model          | [Overview](/products/caas/markup/overview)                              |
| Sub-account and API key setup | [CAAS Getting Started](/products/caas/getting-started)                  |

---

# Markup Integration Guide

The Markup API lives under **`/sapi/v1/vip/caas/commission/*`**, in two groups:

- **Fee groups** — set the markup each of your sub-accounts pays on top of Binance's base
  commission.
- **Reportings** — read back the markup income those sub-accounts generated.

This guide covers both, in the order you would build them. Read
[Overview](/products/caas/markup/overview) for the commercial model and
[Getting Started](/products/caas/markup/getting-started) for base endpoints and signing first — this
page assumes both.

---

## Table of Contents

1. [Before You Begin](#1-before-you-begin)
2. [How the Model Works](#2-how-the-model-works)
3. [Integration Steps](#3-integration-steps)
4. [Parameter Placement and Content Types](#4-parameter-placement-and-content-types)
5. [Reporting](#5-reporting)
6. [Changing Rates Later](#6-changing-rates-later)
7. [Response Envelope](#7-response-envelope)
8. [Going Live](#8-going-live)

---

## 1. Before You Begin

### Prerequisites

- A **live CAAS integration**. Markup is enabled on top of one and uses the same master account —
  see [CAAS Getting Started](/products/caas/getting-started).
- **The markup model uplifted on your master account by the Link team.** This is an access gate, not
  only a commercial setting — until the uplift is applied, these endpoints are not available to your
  master account. Markups are granted case-by-case only, on application to
  [link@binance.com](mailto:link@binance.com). See [Overview](/products/caas/markup/overview).
- **Sub-accounts already created.** Fee groups are populated with sub-account user IDs, so the
  sub-accounts must exist before you can assign them.
- **Each sub-account's KYC passed** through [KYC SaaS](/products/kyc-saas/overview). A sub-account
  cannot trade until it has, so assigning it to a fee group has no effect before that point.

### API key

Every endpoint on this page is `SIGNED` and requires the **master account's** API key — not a
sub-account key. They split by security type:

- **`TRADE`** — Create Fee Group, Update Fee Group Commission, Assign Members, Unassign Members,
  Delete Fee Group. These need the key's **trade** permission enabled.
- **`USER_DATA`** — Query Fee Groups, Query Fee Group Members, Query One Member's Fee Group, and the
  reporting endpoints.

Every one of them carries an IP weight of **1**.

Note that **markup and revenue share cannot be combined**, and markup applies to the **spot order
book only**. If your account is on revenue share, nothing on this page takes effect until the model
is switched.

---

## 2. How the Model Works

Binance charges the sub-account a base commission. Your markup is added **on top** of it, and the
excess is yours. From [Overview](/products/caas/markup/overview): a partner marking up to 0.30%
maker/taker leaves 0.10% with Binance and keeps 0.20%.

Three properties of the model drive the whole integration:

| Property                         | Consequence for your integration                                             |
| -------------------------------- | ---------------------------------------------------------------------------- |
| Rates are set **per fee group**  | You never set a rate on a user. You put users in a group and rate the group. |
| Maker and taker are **separate** | `makerMarkup` and `takerMarkup` are independent fields on every write.       |
| A sub-account has **one** group  | `member-fee-group` takes a single `subUserId` and returns a single group.    |

So the unit of configuration is the group, and the unit of membership is the sub-account.

<!-- Sourced from Jordan Liu (VIP Products), 2026-09-10. The maximum markup rate is deliberately
     NOT published: Esmond's call, 2026-09-10 — it is internal, configured per broker, and
     communicated only by the Link team or the partner's Account Manager. Do not add a figure here
     even if one appears in a PRD. The settlement TIME is also absent, still pending Duy/Leo. -->

### Rules that affect your fees and income

| Rule                                                                                                    | Detail                                                                                              |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Markup replaces revenue share**                                                                       | Your referral rebate is switched off once markup is activated. The two never run together.          |
| **A sub-account in no fee group trades at base rate**                                                   | No markup, and no rebate. It is not rejected, so a missed assignment is silent.                     |
| **Spot order book only, filled and settled trades**                                                     | Unfilled or unsettled orders accrue nothing.                                                        |
| **The BNB fee discount does not apply**                                                                 | It is unavailable to sub-account trading under a markup fee group. Do not model it into your rates. |
| **Fee groups are capped**                                                                               | 3 per partner, raisable to 20 on request through the Link team.                                     |
| **Income is paid in USDT to your master account**                                                       | Converted at end of day and distributed to the broker master account. Always USDT.                  |
| **Non-USDT pairs convert at the 00:00 UTC daily close of the trade date, and you bear the FX movement** | This is what `markupConvertRate` and `markupConvertTime` record on each reporting row.              |

**The maximum markup rate available to you is set per partner and is not published.** Get it from
the Link team or your Account Manager before designing your fee tiers, along with confirmation of
how many fee groups you may create.

Reporting is **T-1**: data is available up to the previous day, so same-day trading is not
queryable. See [section 5](#5-reporting).

---

## 3. Integration Steps

### Step 1 — Create a fee group

`POST /sapi/v1/vip/caas/commission/fee-groups`

Required: `groupName` (max 32 characters), `makerMarkup`, `takerMarkup`, `timestamp`. Rates are
decimals, so `0.002` is 0.2%.

The response returns a **`groupCode`** — for example `FG001` — plus the name, both rates,
`subAccountCount`, `createdTime` and `updatedTime`.

**`groupCode` is assigned by Binance, not chosen by you**, and every later call identifies the group
by `groupCode` rather than `groupName`, so persist it when you create the group. No endpoint looks a
group up by name.

### Step 2 — Assign sub-accounts to the group

`POST /sapi/v1/vip/caas/commission/fee-groups/members`

`groupCode` goes in the **query string**; the sub-accounts go in a **JSON body** as `subUserIds`, an
array of integers.

:::warning

**`subUserIds` takes spot UIDs — not CAAS sub-account IDs.** Send each sub-account's **spot UID**,
not the longer `subAccountId` that the CAAS sub-account APIs return and accept.

This is easy to get wrong, because the field is called `subUserId` here and `subAccountId` in the
CAAS APIs, and the reference example value resembles neither. The same spot UID is what
`member-fee-group` and the `subUserId` reporting filters expect.

To retrieve a sub-account's spot UID, call `GET /api/v3/account` with **that sub-account's own API
key** and read the `uid` field.

:::

:::warning

**`subUserIds` takes at most 10 entries per request** — on both Assign Members and Unassign Members.
Batch your migration in chunks of 10.

Exceeding it returns
`-1102 Mandatory parameter 'subUserIds' was not sent, was empty/null, or malformed.` — which says
nothing about size, so it reads like a serialisation bug. If you get `-1102` on a well-formed array,
count the entries first. The limit is enforced before the `groupCode` is looked up, so an oversized
batch fails even when everything else is correct.

:::

**A `200` does not mean every sub-account was assigned.** The response reports partial success:

- `successCount` — how many were assigned
- `failedList` — one entry per failure, each with `subUserId` and `errorMessage` (for example
  `Sub-account does not belong to master`)

Read `failedList` and reconcile it. Treating the HTTP status as the outcome will silently leave
sub-accounts on the base rate.

### Step 3 — Verify membership

Two read paths, depending on the question:

| Question                            | Endpoint                                              | Key parameter        |
| ----------------------------------- | ----------------------------------------------------- | -------------------- |
| Which group is this sub-account in? | `GET /sapi/v1/vip/caas/commission/member-fee-group`   | `subUserId`          |
| Who is in this group?               | `GET /sapi/v1/vip/caas/commission/fee-groups/members` | `groupCode` + paging |
| What groups do I have?              | `GET /sapi/v1/vip/caas/commission/fee-groups`         | paging only          |

`member-fee-group` takes a single `subUserId` and needs no paging, which makes it the
straightforward call when reconciling a `failedList`. They all carry the same IP weight.

### Step 4 — Read markup income back

Once the sub-accounts trade, use the reporting endpoints in [section 5](#5-reporting).

---

## 4. Parameter Placement and Content Types

The write endpoints are **not** consistent with each other, so build against this table rather than
by analogy from one endpoint to the next:

| Endpoint                        | Method   | `groupCode` / `timestamp` | Payload                             |
| ------------------------------- | -------- | ------------------------- | ----------------------------------- |
| Create Fee Group                | `POST`   | in the body               | `application/x-www-form-urlencoded` |
| Update Fee Group Commission     | `PUT`    | in the **query string**   | `application/json` (rates only)     |
| Assign Members to Fee Group     | `POST`   | in the **query string**   | `application/json` (`subUserIds`)   |
| Unassign Members from Fee Group | `DELETE` | in the **query string**   | `application/json` (`subUserIds`)   |
| All read endpoints              | `GET`    | in the query string       | none                                |

Note in particular that **Create** puts everything in a form-encoded body, while the other three
writes split parameters across the query string and a JSON body. `recvWindow` follows `timestamp` in
each case and may not exceed `60000`.

:::warning

**On the three JSON-body endpoints, sign the query string only — do not include the request body in
the signed payload.** Signing the query string concatenated with the JSON body returns
`-1022 Signature for this request is not valid.`

This differs from the form-encoded convention, where body parameters are part of the signed string.
Verified live on `PUT .../fee-groups/commission`, 2026-09-09.

:::

Send the JSON body even when its values are irrelevant — omitting it altogether on
`PUT .../commission` returns **HTTP 500** with `-1000 An unknown error occurred`, rather than a
`-1102` for the missing required field.

---

## 5. Reporting

Both reporting endpoints are `USER_DATA`, and both are paginated with **`pageIndex`** (starting
at 1) and **`pageSize`** (1-100). `startTime`, `endTime`, `pageIndex` and `pageSize` are all
**required** on both — there is no default window.

### Aggregations — daily totals

`GET /sapi/v1/vip/caas/commission/markup-trade-aggregations`

One row per date, per sub-account, **per fee group**. Optional `groupCode` and `subUserId` filters.

| Field                                    | What it is                             |
| ---------------------------------------- | -------------------------------------- |
| `date`                                   | The aggregation date                   |
| `subUserId`, `groupCode`, `groupName`    | Who, and under which group's rates     |
| `totalVolumeUsdt`                        | Traded volume for the row, in USDT     |
| `markupMakerIncome`, `markupTakerIncome` | Your income, split by fill side        |
| `markupAsset`                            | The asset the markup is denominated in |

Maker and taker income are reported separately, matching the two rates you configured.

Rows are keyed by date, sub-account **and** fee group, so do not assume `subUserId` plus `date`
identifies a single row.

### Details — trade level

`GET /sapi/v1/vip/caas/commission/markup-trade-details`

One row per fill, with an additional optional `symbol` filter. Alongside the order and trade fields
(`orderId`, `product`, `symbol`, `tradeSide`, `tradeType`, `price`, `qty`, `quoteQty`), each row
carries the full fee breakdown:

| Field                                    | What it is                                 |
| ---------------------------------------- | ------------------------------------------ |
| `baseRate`                               | Binance's own commission rate on the fill  |
| `markupRate`                             | Your markup rate applied to that fill      |
| `totalFeeRate`                           | What the sub-account actually paid         |
| `markupAmount`                           | Your income on the fill, in `markupAsset`  |
| `markupAmountUsdt`                       | The same amount in USDT                    |
| `markupConvertRate`, `markupConvertTime` | The rate and time used for that conversion |

`markupAmount` is denominated in `markupAsset`; `markupAmountUsdt` is its USDT equivalent. Where the
two differ, `markupConvertRate` and `markupConvertTime` record the conversion that was applied —
reconcile against those two fields rather than recomputing from the fill price.

`totalFeeRate` is the sum of the two rates — in the reference example, `0.001` base plus `0.003`
markup gives `0.004`. Use `baseRate` and `markupRate` rather than deriving your share from
`totalFeeRate`, since only `markupRate` is yours.

:::note

**`tradeType` is the fill side that determined the rate**, not the order type you submitted. A limit
order fills as a taker if the book moves before it rests, so reconcile income against `tradeType` —
never against how the order was placed.

:::

---

## 6. Changing Rates Later

`PUT /sapi/v1/vip/caas/commission/fee-groups/commission` updates `makerMarkup` and `takerMarkup` for
a whole group, identified by `groupCode` in the query string. Both rates are required, so send the
unchanged one too.

Because rates live on the group, moving one sub-account onto different rates means unassigning it
and assigning it to another group, not editing anything on the user.

To retire a group:

1. `DELETE /sapi/v1/vip/caas/commission/fee-groups/members` for every member.
2. `DELETE /sapi/v1/vip/caas/commission/fee-groups` for the group itself.

:::warning

**A group cannot be deleted while it still has members.** The delete rejects until every sub-account
has been unassigned. Check `subAccountCount`, or page through `fee-groups/members`, before
attempting it.

:::

The API has **no rename endpoint** — `groupName` is set at creation and is not editable through any
of the endpoints on this page.

---

## 7. Response Envelope

A successful call wraps its result like this:

```json
{
  "status": "OK",
  "type": "GENERAL",
  "code": "000000000",
  "data": {}
}
```

:::warning

**Success is `"000000000"` — nine zeros.** Branching on `"000000"` treats every successful call as a
failure. There is also no `message` field on success, and `status` and `type` are present.

Verified live on `fee-groups`, `markup-trade-aggregations` and `markup-trade-details`, 2026-09-09.
If you built against an earlier version of the API Reference, which showed
`{"code": "000000", "message": "success"}`, re-check your success test — the examples have since
been corrected.

:::

Failures use the **standard Binance error envelope instead** — a negative numeric `code` and `msg`,
with a real HTTP status:

```json
{ "code": -9000, "msg": "Markup configuration not found" }
```

So a client has to handle two different response shapes on the same endpoint, and cannot simply read
`code` in one place.

| Observed                                 | Meaning                                                      |
| ---------------------------------------- | ------------------------------------------------------------ |
| `-9000` `Markup configuration not found` | Returned by `member-fee-group` for a sub-account in no group |
| `-31002` `illegal parameter`             | Seen on `PUT .../commission` with a non-existent `groupCode` |

:::warning

**Querying a sub-account that is in no fee group is an error, not an empty result.**
`member-fee-group` returns `-9000 Markup configuration not found` rather than a row indicating "no
group". Handle it as an expected outcome when reconciling, not as a failure.

**`-9000` does not tell you which of several things went wrong.** The same code comes back for a
sub-account that simply has no fee group, for one that is not under your master, and for an
identifier that is not a spot UID at all. If you get it unexpectedly, check the identifier before
concluding the sub-account is unassigned.

:::

This envelope is specific to the Markup endpoints. Most `/sapi/*` endpoints return the result object
directly, so a client written against those will read the response as empty — unwrap `data` before
parsing.

<!-- TODO(sulyn / Link eng): two items here.

     1. [RESOLVED 2026-09-10] the spec's response envelope was wrong on all 10 endpoints --
        code "000000" plus a message field, where the service returns "000000000" with status/type
        and no message. Fixed in docs/products/vip-caas/openapi/rest-api/**.yaml and re-bundled.
        NOTE the internal SAPI+API Confluence page carries the same defect and is its origin, so
        it will be re-copied unless that page is corrected too.

     2. The failure codes are still not enumerated. -9000 and -31002 above were observed, not
        documented, and -31002 "illegal parameter" is too generic to branch on -- it is not even
        certain whether it referred to the groupCode or to the body. Still needed: duplicate
        groupName, sub-account outside the master, deleting a non-empty group, and exceeding the
        markup cap. -->

---

## 8. Going Live

- [ ] Markup model approved for the account, and revenue share confirmed switched off.
- [ ] Master-account API key with **trade** permission; sub-account keys are not used here.
- [ ] Every fee group created, with its `groupCode` persisted on your side.
- [ ] Every sub-account assigned, and **`failedList` empty or reconciled** on each assign call.
- [ ] `member-fee-group` spot-checked for a sample of sub-accounts, confirming the group and rates.
- [ ] Maker and taker rates verified independently — they are separate fields and a single test fill
      only exercises one of them.
- [ ] Both reporting endpoints called with an explicit `startTime` / `endTime` and paging, and
      reconciled against your own records.
- [ ] Envelope unwrapping and `code` checking implemented.
- [ ] Reconciliation keyed on date **and** sub-account **and** fee group, not date plus sub-account
      alone.
- [ ] Where `markupAsset` is not USDT, income reconciled against `markupConvertRate` and
      `markupConvertTime`.
- [ ] Commercial parameters confirmed with your Account Manager — maximum markup rate, number of fee
      groups, settlement schedule, and how BNB fee discounts interact with markup.

<!-- SOURCING RULE FOR THIS PAGE (Esmond, 2026-09-09)

     Everything published here comes from ONE OF THREE sources only:
       (a) the shipped spec, docs/products/vip-caas/openapi/rest-api/**.yaml
       (b) behaviour tested live against api.binance.com on 2026-09-09
       (c) named product-owner confirmation, attributed and dated below
           -- added 2026-09-10 (Esmond) once the PRD's commercial rules were confirmed
           by the owning PM. A PRD, a Confluence page or an internal deck is STILL NOT
           a source; only a named person answering a specific question.
     plus the pre-existing Overview / Getting Started pages.

     PRD "CAAS Basic (Exchange Link) Commission Markup v1.0" (Confluence 499409522) is NOT used
     as a source for anything on this page, because it is demonstrably stale:

     1. Its whole API surface diverged. It specifies /sapi/v1/caas/fee/group and
        /sapi/v1/caas/fee/markupRecord with feeGroupId/subAccountId/limit/page and fields
        totalVolume/makerMarkupIncome/takerMarkupIncome/asset, plus a create response carrying
        baseSpotMaker/baseSpotTaker/totalSpotMaker/totalSpotTaker. The shipped API is
        /sapi/v1/vip/caas/commission/* with groupCode/subUserId/pageIndex/pageSize and
        totalVolumeUsdt/markupMakerIncome/markupTakerIncome/markupAsset, and none of those four
        base/total rate fields exist.
     2. At least one BUSINESS rule also failed to survive: the PRD says querying an unassigned
        sub-account returns a feeGroupId "DEFAULT" sentinel. Live returns -9000 "Markup
        configuration not found" (tested).

     These PRD-stated rules were therefore REMOVED from the page and need confirmation against the
     implementation before any of them is republished:
       - [NOT FOR PUBLICATION 2026-09-10] markup rate cap. Jordan Liu (VIP Products) confirms a
         max IS configured per broker, but did NOT confirm the PRD's 10% default. Esmond's call:
         treat the value as INTERNAL -- shared only by the Link team or the Account Manager. Do
         not publish a figure here. The error code returned when a group exceeds the cap is
         still unknown from every source.
       - [CONFIRMED 2026-09-10, Jordan Liu] fee groups per partner: 3 max, raisable to 20 on
         request. Published in section 2 without naming the internal admin surface.
       - [RESOLVED 2026-09-10] max subUserIds per assign/unassign request: the PRD's 100 is
         WRONG. The live limit is 10, confirmed three ways -- black-box bisection (10 accepted,
         11 rejected), the implementation's own @Size(max = 10) on
         AssignFeeGroupMembersRequest.subUserIds, and Duy (Spot-ES-Tech): capped at 10 for
         system performance, agreed before release. Now published in section 3 and added to the
         spec as maxItems: 10 on both endpoints.
       - [RESOLVED 2026-09-10] status enum: there is NO status field. The PRD's
         PENDING|DISTRIBUTED never shipped, and the field the spec declared on
         markup-trade-aggregations was a phantom -- Duy confirmed CaasSubCommissionInfo has no
         status, and the spec's row schema otherwise matched that VO field for field. The
         phantom field has been removed from the spec. Note the live envelope does carry a
         top-level status: "OK", which is a different thing and not per-row.
       - [CONFIRMED 2026-09-10, Jordan Liu] reporting is T-1 only. Published in section 2.
       - [PARTLY CONFIRMED 2026-09-10, Jordan Liu] income is converted at end of day and
         distributed to the broker master account, always in USDT. The exact distribution TIME
         is NOT confirmed -- Jordan deferred it to Duy/Leo, so the PRD's "T+1" stays
         unpublished. Mechanism published in section 2; no time given.
       - [CONFIRMED 2026-09-10, Jordan Liu] the BNB discount is NOT available under markup.
         Published in section 2. Note this remains the OPPOSITE of the Link & Trade OMS markup
         family, so it must never be inferred from that family.
       - [CONFIRMED 2026-09-10, Jordan Liu] non-USDT pairs convert at the 00:00 UTC daily close
         of the trade date and the broker bears the FX movement. Published in section 2.
         Jordan hedged with "should be", so re-confirm if a partner disputes a figure.
       - [CONFIRMED 2026-09-10, Jordan Liu] settlement asset is always USDT. Published in
         section 2.
       - [CONFIRMED 2026-09-10, Jordan Liu] a sub-account in no fee group trades at base rate
         with no markup AND no rebate -- silently, not rejected. Published in section 2.
       - [CONFIRMED 2026-09-10, Jordan Liu] filled and settled spot trades only. Published in
         section 2.
       - [CONFIRMED 2026-09-10, Jordan Liu] the referral rebate is turned OFF once markup is
         activated. Published in section 2.

     Also still unknown from every source: members per fee group, and the error code when a group
     exceeds the configured cap.

     All 13 are PARKED as numbered follow-up questions for the Link team / PM, with PRD line
     references and a priority order, in the TechOps working notes
     (20260909_caas_markup_open_questions_link_team). Republish each one only once it is
     confirmed against the implementation -- not against the PRD.

     TODO(sulyn): also still needed here are the commercial onboarding steps (application,
     approval, model switch) with their real owners and lead times -- this checklist is derived
     from the API surface, not from a runbook. -->

---

## Where to go next

| If you need                   | Go to                                                                   |
| ----------------------------- | ----------------------------------------------------------------------- |
| The endpoint reference        | [Markup REST API](/catalog/vip-and-institutional-vip-caas/api/rest-api) |
| Base endpoints and signing    | [Getting Started](/products/caas/markup/getting-started)                |
| The commercial model          | [Overview](/products/caas/markup/overview)                              |
| Sub-account and API key setup | [CAAS Getting Started](/products/caas/getting-started)                  |