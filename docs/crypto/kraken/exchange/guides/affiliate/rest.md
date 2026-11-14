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
source_url: 'https://docs.kraken.com/exchange/guides/affiliate/rest'
updated_at: 2026-11-13
---

# Affiliate REST

> Authentication, daily activity, CPA progress, and payout history for the Affiliate REST API

The Affiliate REST API reports referred-user activity, progress toward CPA
bounties, and your payout history.

Authentication uses the same API key and secret as the rest of the Kraken REST API.
For key setup, see [REST Authentication](https://docs.kraken.com/exchange/guides/rest/authentication.md).
Requests sign each call and send `api-key`, `api-sign`, and `api-nonce` headers
(the signed path includes the query string). When creating or editing your API key,
select the **Query affiliate participants** checkbox and save the key. See
[API key setup](https://docs.kraken.com/exchange/guides/rest/api-keys.md).

Schemas are in [Get Daily Activity](https://docs.kraken.com/api-reference/affiliate/get-daily-activity.md),
[Get CPA Progress](https://docs.kraken.com/api-reference/affiliate/get-cpa-progress.md), and
[Get Payout History](https://docs.kraken.com/api-reference/affiliate/get-payout-history.md).

All examples use synthetic identifiers, not customer account data. Replace example
dates with dates inside the current 90-day window.

### Shared Python helper

```python theme={null}
import base64
import hashlib
import hmac
import json
import time
import urllib.error
import urllib.parse
import urllib.request

BASE_URL = "https://api.kraken.com"
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"  # base64-encoded

_last_nonce = 0


class KrakenApiError(Exception):
    """Non-2xx Kraken API response with a typed error body."""

    def __init__(self, status: int, body: dict):
        self.status = status
        self.body = body
        super().__init__(f"{status}: {body}")


def _nonce() -> str:
    global _last_nonce
    candidate = int(time.time() * 1000)
    _last_nonce = max(candidate, _last_nonce + 1)
    return str(_last_nonce)


def _flat_query(params: dict | None) -> str:
    if not params:
        return ""
    return urllib.parse.urlencode(params, doseq=True)


def _nested_query(params: dict | None) -> str:
    if not params:
        return ""
    pairs: list[tuple[str, str]] = []

    def add(name: str, value) -> None:
        if isinstance(value, dict):
            for child_name, child_value in value.items():
                add(f"{name}[{child_name}]", child_value)
        elif isinstance(value, bool):
            pairs.append((name, "true" if value else "false"))
        elif value is not None:
            pairs.append((name, str(value)))

    for key, value in params.items():
        add(key, value)
    return urllib.parse.urlencode(pairs)


def signed_rest_request(
    method: str,
    path: str,
    params: dict | None = None,
    body: dict | None = None,
    *,
    nested_query: bool = False,
):
    """Send a signed Kraken REST API request."""
    nonce = _nonce()
    query = _nested_query(params) if nested_query else _flat_query(params)
    signed_path = f"{path}?{query}" if query else path
    body_bytes = (
        json.dumps(body, separators=(",", ":")).encode() if body is not None else b""
    )
    digest = hashlib.sha256(nonce.encode() + body_bytes).digest()
    signature = base64.b64encode(
        hmac.new(
            base64.b64decode(API_SECRET),
            signed_path.encode() + digest,
            hashlib.sha512,
        ).digest()
    ).decode()

    headers = {
        "api-key": API_KEY,
        "api-sign": signature,
        "api-nonce": nonce,
    }
    if body is not None:
        headers["content-type"] = "application/json"

    request = urllib.request.Request(
        f"{BASE_URL}{signed_path}",
        data=body_bytes or None,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        error_body = json.loads(exc.read().decode())
        raise KrakenApiError(exc.code, error_body) from exc


def funding_request(
    method: str,
    path: str,
    params: dict | None = None,
    body: dict | None = None,
):
    """Send a signed Funding API request."""
    return signed_rest_request(method, path, params, body, nested_query=True)
```

## CPA progress

Use the full IIBAN from Get Daily Activity to retrieve one referred trader's
progress. Each eligible bounty is returned separately with its reward, status,
requirements, exact measurable values, and percentage.

```python theme={null}
progress = signed_rest_request(
    "GET",
    "/affiliate/v1/cpa-progress",
    {"iiban": "AA45N84GQK2VUN7A"},
)
for bounty in progress.get("progress", {}).get("bounties", []):
    print(bounty.get("description"), bounty["status"], bounty["reward_amount"])
```

```http theme={null}
GET /affiliate/v1/cpa-progress?iiban=AA45N84GQK2VUN7A
```

A response can contain more than one bounty:

```json theme={null}
{
  "progress": {
    "bounties": [
      {
        "bounty_position": 0,
        "description": "Complete the first CPA requirements",
        "reward_amount": "50.00",
        "reward_asset": "USDC",
        "status": "in_progress",
        "progress_availability": "available",
        "conditions": [
          {
            "label": "Margin trading volume",
            "kind": "amount",
            "state": "incomplete",
            "measurement": {
              "current": "20.00",
              "target": "100.00",
              "unit": "USD",
              "percentage": "20"
            }
          },
          {
            "label": "Account verification",
            "kind": "binary",
            "state": "complete"
          }
        ]
      },
      {
        "bounty_position": 1,
        "description": "Complete the second CPA requirements",
        "reward_amount": "80.00",
        "reward_asset": "USDC",
        "status": "qualified_payment_pending",
        "qualified_at": "2026-09-30T14:22:09Z",
        "progress_availability": "available",
        "conditions": [
          {
            "label": "Futures trading volume",
            "kind": "amount",
            "state": "complete",
            "measurement": {
              "current": "1000.00",
              "target": "1000.00",
              "unit": "USD",
              "percentage": "100"
            }
          }
        ]
      }
    ]
  }
}
```

Qualified and paid bounties remain visible. A bounty can also be `expired`,
`no_longer_eligible`, or `not_tracked`. When `progress_availability` is
`unavailable`, measurements may be omitted. Unknown IIBANs, referrals belonging
to another affiliate, and traders who opted out return `404`.

CPA progress summarizes the bounty lifecycle. It is not a one-to-one copy of
the payment state in payout history. Use payout history to determine whether a
payment is pending, on hold, or needs action.

| Status | Meaning |
| - | - |
| `in_progress` | The trader has not completed every requirement. |
| `qualified_payment_pending` | Every requirement is complete, but the payout has not been paid. Its payout-history status can be `pending`, `on_hold`, or `action_needed`. |
| `paid` | The bounty was paid. |
| `expired` | The qualification window or associated payment expired. |
| `no_longer_eligible` | The bounty can no longer be paid. The underlying internal reason is not exposed. |
| `not_tracked` | Detailed progress is unavailable, for example when the bounty was added to the plan after the trader enrolled. |

Before a payment record exists, `reward_amount` is an estimate calculated from
the current plan amount, current conversion rate, and your affiliate share. It
can change between calls. After a payment record exists, the API returns that
record's amount.

Region-specific bounties that do not apply to the trader are omitted. The
`bounties` collection can therefore be empty.

## Payout history

Request your payout history without a cursor to start from the newest row. The
response can include `revshare`, `prop`, `cpa`, `futures_accelerator_bonus`,
`sub_affiliate`, `retainer`, and `remediation` sources. A `remediation` is a
one-off makeup payout added manually by Kraken. Retainer and remediation rows
appear only after approval.

```python theme={null}
page = signed_rest_request(
    "GET",
    "/affiliate/v1/payout-history",
    {"limit": 3},
)
for payout in page.get("items", []):
    print(payout["created_at"], payout["source"], payout["amount"], payout["status"])
```

```http theme={null}
GET /affiliate/v1/payout-history?limit=3
```

```json theme={null}
{
  "items": [
    {
      "payout_id": "RPAY-EXAMPLE-CPA",
      "amount": "50.00",
      "asset": "USDC",
      "status": "paid",
      "created_at": "2026-09-30T15:04:12Z",
      "source": "cpa"
    },
    {
      "payout_id": "RPAY-EXAMPLE-REMEDIATION",
      "amount": "75.00",
      "asset": "USDC",
      "status": "paid",
      "created_at": "2026-09-29T12:00:00Z",
      "source": "remediation"
    },
    {
      "payout_id": "RPAY-EXAMPLE-PROP",
      "amount": "30.50",
      "asset": "USDC",
      "status": "pending",
      "created_at": "2026-09-29T09:10:00Z",
      "source": "prop",
      "prop_purchase_id": "BRP-EXAMPLE-ORDER"
    }
  ],
  "next_cursor": "RPAY-EXAMPLE-PROP",
  "summary": {
    "paid": "312.00",
    "pending": "130.50",
    "prop": {
      "paid": "80.00",
      "pending": "30.50",
      "order_count": 3
    },
    "cpa": {
      "paid": "220.00",
      "pending": "100.00",
      "bounty_count": 5
    }
  },
  "limit": 3
}
```

`summary` covers all payout sources, including sub-affiliate commissions,
approved retainers, and approved remediations, not only the current page. It
includes rows whose public status is `paid` or `pending`. Other statuses can
appear in `items`, but do not contribute to the totals or Prop and CPA counts.

When `next_cursor` is present, pass it unchanged with the same page size. Stop
when it is absent:

```python theme={null}
cursor = page.get("next_cursor")
while cursor:
    page = signed_rest_request(
        "GET",
        "/affiliate/v1/payout-history",
        {"cursor": cursor, "limit": 3},
    )
    for payout in page.get("items", []):
        print(payout["created_at"], payout["source"], payout["amount"], payout["status"])
    cursor = page.get("next_cursor")
```

## Daily activity

Both variants are signed with your own API key. Dates are UTC calendar days
(`YYYY-MM-DD`) and must be **today or one of the previous 89 UTC days**. A future
date or a date older than that window is a `400`. A valid day with no matching activity or enrollments
is an empty page, not an error.

### By day

Give a trade date. You get referred users with reportable activity, plus quiet
users who enrolled that day and are still enrolled. Opted-out users are omitted
from this default listing; use the full roster or person history for existence
stubs. Activity is split by plan and product, with day-wide totals. A user who has
never traded still has an enrollment-day entry with `enrolled_at` and empty
`products`; this confirms enrollment, not trading activity.

```python theme={null}
page = signed_rest_request(
    "GET",
    "/affiliate/v1/daily-activity",
    {"activity_date": "2026-09-16", "limit": 50},
)
print(page["activity_date"], page.get("active_users", 0), page["currency"])
for item in page.get("items", []):
    print(item["referee_reference"], item.get("masked_iiban"), item.get("opted_out", False))
```

```http theme={null}
GET /affiliate/v1/daily-activity?activity_date=2026-09-16&limit=50
```

For a request with `activity_date=2026-09-15`, this enrollment-day item confirms
a signup before any trading. On September 16, this user appears only in the full roster:

```json theme={null}
{
  "iiban": "BB12N84GQK2VUN7B",
  "masked_iiban": "UN7B",
  "referee_reference": "example_quiet_user",
  "plans": [
    {
      "referral_code": "EXAMPLE1",
      "referral_level": 1,
      "enrolled_at": "2026-09-15T09:00:00Z",
      "status": "active",
      "earning": true
    }
  ]
}
```

The enrollment time is in `plans[].enrolled_at`. Empty `products` may be omitted.
This entry does not increase `active_users`.

### Full referral roster

Add `all_users=true` to a day request to include quiet users enrolled in your
affiliate plan by that date who are still enrolled, even if they signed up more
than 90 days ago. Their `products` object is empty when they have no reportable
activity that day. The requested activity date must still be within the last
90 UTC days.

```http theme={null}
GET /affiliate/v1/daily-activity?activity_date=2026-09-16&all_users=true&limit=50
```

With the Python helper, pass the query value as the lowercase string `"true"`:

```python theme={null}
page = signed_rest_request(
    "GET",
    "/affiliate/v1/daily-activity",
    {"activity_date": "2026-09-16", "all_users": "true", "limit": 50},
)
```

Follow `next_cursor` with the same date and `all_users=true` to retrieve the
whole roster. `active_users`, `totals`, and `revision` continue to describe
trading activity for the requested day; quiet users do not increase them.
`all_users` is available only for day requests, not person history requests.

This full-roster response includes a trading user, a quiet user, and an opted-out
user. Only the trading user contributes to `active_users` and `totals`.

```json theme={null}
{
  "activity_date": "2026-09-16",
  "currency": "USD",
  "revision": "2026-09-17T00:14:02Z",
  "generated_at": "2026-09-17T12:01:04Z",
  "active_users": 1,
  "totals": {
    "spot_trading": {
      "volume": "42110.20",
      "fees": "38.20",
      "commission": "11.46",
      "event_count": 12
    }
  },
  "items": [
    {
      "masked_iiban": "UN7A",
      "referee_reference": "jsd6ggr6qjrzmemn",
      "plans": [
        {
          "referral_code": "EXAMPLE1",
          "referral_level": 1,
          "enrolled_at": "2026-03-14T09:00:00Z",
          "status": "active",
          "earning": true,
          "products": {
            "spot_trading": {
              "volume": "42110.20",
              "fees": "38.20",
              "commission": "11.46",
              "event_count": 12
            }
          }
        }
      ],
      "iiban": "AA45N84GQK2VUN7A"
    },
    {
      "iiban": "BB12N84GQK2VUN7B",
      "masked_iiban": "UN7B",
      "referee_reference": "example_quiet_user",
      "plans": [
        {
          "referral_code": "EXAMPLE1",
          "referral_level": 1,
          "enrolled_at": "2026-09-15T09:00:00Z",
          "status": "active",
          "earning": true
        }
      ]
    },
    {
      "referee_reference": "example_opted_out_user",
      "opted_out": true,
      "enrolled_at": "2026-08-20T09:00:00Z",
      "plans": [
        {
          "referral_code": "EXAMPLE1"
        }
      ]
    }
  ],
  "limit": 50,
  "opted_out": {
    "suppressed": {}
  }
}
```

### By person

Give up to ten full IIBANs (Kraken account identifiers) returned by this API or shared by the people
you referred, plus an inclusive date range. You get per-day entries for those
people, never a total for the whole range. Day-wide fields (`totals`,
`active_users`, `revision`, `estimated`,
`opted_out`) are omitted.

```python theme={null}
page = signed_rest_request(
    "GET",
    "/affiliate/v1/daily-activity",
    {
        "iiban": "AA45N84GQK2VUN7A,CC34N84GQK2VUN7C",
        "start_date": "2026-08-20",
        "end_date": "2026-09-16",
        "limit": 50,
    },
)
for item in page.get("items", []):
    print(item.get("activity_date"), item["referee_reference"], item.get("opted_out", False))
```

```http theme={null}
GET /affiliate/v1/daily-activity?iiban=AA45N84GQK2VUN7A,CC34N84GQK2VUN7C&start_date=2026-08-20&end_date=2026-09-16&limit=50
```

Empty, duplicate, or malformed IIBAN tokens are a `400`. Validity is a format
check only, not account existence. A valid IIBAN that does not match a referred
user on your plan returns an empty result. An opted-out user who is still enrolled
and enrolled by the end of the requested range returns one existence stub without
`activity_date`. The stub does not reveal which days they traded.
Visible history entries include the matching full `iiban`; opted-out stubs omit it.

In this example, `CC34N84GQK2VUN7C` belongs to a user whose identifier you
obtained before they opted out. The response
contains dated activity for the trader and one undated stub for the opted-out user:

```json theme={null}
{
  "currency": "USD",
  "generated_at": "2026-09-17T12:01:04Z",
  "items": [
    {
      "masked_iiban": "UN7A",
      "referee_reference": "jsd6ggr6qjrzmemn",
      "plans": [
        {
          "referral_code": "EXAMPLE1",
          "referral_level": 1,
          "enrolled_at": "2026-03-14T09:00:00Z",
          "status": "active",
          "earning": true,
          "products": {
            "spot_trading": {
              "volume": "42110.20",
              "fees": "38.20",
              "commission": "11.46",
              "event_count": 12
            }
          }
        }
      ],
      "iiban": "AA45N84GQK2VUN7A",
      "activity_date": "2026-09-16"
    },
    {
      "referee_reference": "example_opted_out_user",
      "opted_out": true,
      "enrolled_at": "2026-08-20T09:00:00Z",
      "plans": [
        {
          "referral_code": "EXAMPLE1"
        }
      ]
    }
  ],
  "limit": 50
}
```

Sending both variants on one request is a `400`.

## Identifying a referred user

Use `referee_reference` to match a referred user across days. It is stable under
your account, but it is not a Kraken account ID and cannot be matched across
affiliate accounts. The same reference remains on an opted-out stub.

`iiban` is the full Kraken account identifier for a referred user sharing activity.
It is returned on daily, full-roster, and history entries, including quiet enrollments.
You can use it in person-history requests. Opted-out stubs omit it.

`masked_iiban` remains available for compatibility. It contains only the last four
characters and is not unique; use `iiban` to match a Kraken account or
`referee_reference` to track the enrollment. `enrolled_at` is truncated to the hour.

## Products

One key per product that had activity. The map is open-ended: ignore unknown
keys. For a visible activity entry, an absent key means no reported activity for
that product. Empty `products` may be omitted. For an opted-out stub, empty or omitted products
means data is withheld, not zero.

| Key | Meaning | `volume` | `maker` / `taker` |
| - | - | - | - |
| `spot_trading` | Order-book spot | yes | yes |
| `ptl_trading` | Instant buy/sell | yes | no |
| `margin_trading` | Margin trades | yes | yes |
| `margin_rollover` | Financing charge on open margin positions | no | no |
| `futures_order_fill` | Futures | yes | yes |
| `tokenized_equity_spot_trading` | xStocks, order book | yes | yes |
| `tokenized_equity_ptl_trading` | xStocks, instant | yes | no |

Options is not included. `maker` and `taker` appear only on execution products,
and only when that side had classified fills. When both are present they sum to
the classified portion; the difference from the product total is unclassified. Absence
means unclassified, not zero. Instant buy/sell and financing charges have no
liquidity side.

`geo_blocked` is present only when that product had blocked-region activity.
Activity from blocked regions pays zero commission. The product's `volume`,
`fees`, `event_count`, and `commission` cover payable activity only;
`geo_blocked` is shown separately and is not included in those product totals.

## Totals, opt-out, and payments

Day-wide `totals` include activity from referred users who have not opted out.
With `all_users=true` or person history, opted-out users appear in `items` as existence stubs:

```json theme={null}
{
  "referee_reference": "example_referee_reference",
  "opted_out": true,
  "enrolled_at": "2026-08-20T09:00:00Z",
  "plans": [
    {
      "referral_code": "EXAMPLE"
    }
  ]
}
```

The reference matches their visible entries before opt-out. `enrolled_at` is
truncated to the hour. The plan's `referral_code` preserves plan attribution;
it does not expose the person's account identifier. Stubs omit `iiban`, `masked_iiban`,
individual amounts, campaign, plan status, and earning details. Treat
`opted_out=true` as withheld data, never as zero activity. Stub presence does not
depend on trading. Ordinary daily requests omit these stubs.

People who are not enrolled in your plan are omitted from `items`, including on
past dates, but stay in `totals` so past totals remain consistent. They are not
counted in `opted_out`.

Combined opted-out activity may appear under the response's top-level `opted_out`:

* `{ "suppressed": {} }` when opted-out referees remain enrolled and zero or one has reportable activity
* `{ "summary": { "active_participants", "products" } }` when two or more have reportable activity

The top-level `opted_out` is omitted only when there are neither qualifying opted-out
enrollments nor reportable opted-out activity. Suppression does not tell you whether
anyone traded. This rule applies to both daily listings and full-roster requests.
The existence of a stub does not imply inclusion in an activity summary.

Payable for the day is `totals` plus `summary` when `summary` is present.

Daily figures will not match weekly payments exactly:

* Totals show activity eligible for commission
* Geo-blocked activity is shown separately and pays zero
* This API groups activity by trade date; weekly payments group it by when it was recorded

## Staleness

A trade day's figures can change when activity is reported later.

`revision` (day variant, first page) is when **your** figures for that UTC day
were last written. A later value on re-fetch means your figures moved. Another
partner's late event does not move this value. Re-check the trailing 35 days.

Enrollments and sharing-setting changes do not advance `revision`. Refresh the
roster even when `revision` has not changed to discover signups and opt-outs.

When `estimated` is `true` on the first page, amounts for that calendar day are
still an estimate, including the opted-out remainder.

## Pagination

`limit` defaults to 50 and rejects values over 200. When `next_cursor` is
present, pass it as `cursor` on the next request.

Treat `next_cursor` as an opaque value: pass it as `cursor` without changing it.
Keep the date or history range, identifiers, and `all_users` value unchanged.
A daily cursor cannot be reused for a full-roster request, or vice versa.

`active_users`, `totals`, `revision`, `estimated`, and `opted_out` are
first-page only. An empty `totals` map on a later page is omission, not a zero
day.

## Errors

| Endpoint | HTTP | When |
| - | - | - |
| All | `401` | The API key or signature is missing or invalid. |
| All | `403` | The key lacks Query affiliate participants permission, or the account does not have an active affiliate plan. |
| Daily activity | `400` | Both request variants are sent; a required history field is missing; a date is outside the 90-day window; `limit` is out of range; an `iiban` token is empty, duplicated, or malformed; `all_users=true` is combined with history; or a cursor is reused with the wrong request variant. |
| CPA progress | `400` | `iiban` is missing or malformed. |
| CPA progress | `404` | The trader is unknown, belongs to another affiliate, or opted out. |
| Payout history | `400` | `cursor` is invalid or `limit` is outside 1 to 200. |
| All | `500` | An internal error occurred. |

Empty collections and zero-valued fields may be omitted. Read missing `items` as
`[]`, missing `products` as `{}`, and missing first-page `active_users` as `0`.
For opted-out stubs, always use `opted_out=true` to distinguish withheld data from
no reported activity.

Successful bodies are the object itself. Errors are a non-2xx status with a typed
error body. The helper raises `KrakenApiError` with the parsed body on failure.
Throttling is covered in [Rate limits](https://docs.kraken.com/exchange/guides/affiliate/ratelimits.md).
