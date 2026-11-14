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
source_url: 'https://docs.kraken.com/exchange/guides/futures/assignment-program'
updated_at: 2026-11-13
---

# Assignment Program

> How to join the Derivatives Assignment Program, scope your preferences by wallet, currency pair or contract, and understand how assignments are priced and allocated

The Assignment Program lets an account volunteer to take over positions from accounts that are being liquidated, at a price better than the mark. You register standing preferences over REST; when a liquidation happens the engine books a qualifying position straight into your account.

## Overview

| | |
| :- | :- |
| **What you receive** | The liquidated position, transferred to you at a price below the mark for a long, or above the mark for a short |
| **Your edge** | The gap between the assignment price and the mark — at least your configured minimum, **75 bps** by default, and never more than **250 bps** under the current platform configuration |
| **Who can join** | Any Derivatives account that accepts the Assignment Program terms |
| **How to join** | Accept the terms on Kraken Pro, then configure preferences over REST |
| **Markets** | All Derivatives futures contracts. Options are never assigned |
| **Obligation** | None per assignment — your standing preferences are the only commitment, and you can withdraw them at any time |
| **Price** | Set by the engine, not quoted by you. You cannot bid for an individual assignment |

Assignments are pushed, not pulled. There is no request to answer and no window in which to accept: everything you control is configured in advance.

> [!NOTE]
>
> You may receive an assignment at any time your preferences are active, including outside your own trading hours, and the position arrives already open. Size your `maxSize` and `maxPosition` limits for a position you would be comfortable holding unattended.

Only a **full** liquidation produces assignments. While an account's equity sits in the partial-liquidation band the engine reduces its position into the order book instead, and no assignment is offered.

## Joining the program

**1. Accept the terms**

Open [Assignment Program settings](https://pro.kraken.com/app/settings/futures-assignments) on Kraken Pro and accept the Assignment Program terms and conditions. Until the account has accepted, every preference request is rejected with `assignmentProgramTermsNotAcceptedFrontend`.

**2. Add a preference**

Post one preference per scope you want to participate in — see [Preference scopes](#preference-scopes).

**3. Check what is live**

`GET /assignmentprogram/current` returns every active preference with its `id`. `GET /assignmentprogram/history` returns the full change history, including deletions. Remove a preference with `POST /assignmentprogram/delete?id=<id>`.

## Preference scopes

A preference is keyed by the scope you give it, and on the multi-collateral (`flex`) wallet there are three, from coarsest to finest:

| Scope | Set by | Covers |
| :- | :- | :- |
| **Wallet** | `contractType` alone | Every contract settled by that wallet |
| **Currency pair** | `contractType` + `baseCurrency` + `quoteCurrency` | Every contract on that pair — perpetual and all dated expiries together |
| **Contract** | `contractType` + `contract` | One contract |

`contract` and the `baseCurrency`/`quoteCurrency` pair are mutually exclusive. Sending both is rejected with `mustSpecifyAssignmentParticipantForExactlyOneOfContractOrCurrencyPair`.

Single-collateral wallets have only the wallet scope — the wallet *is* the contract. Sending `contract` or a currency pair with a single-collateral `contractType` is rejected with `cannotSpecifyAssignmentParticipantForContractOrCurrencyPair`.

### Wallet-wide

Covers everything the wallet settles, including contracts listed after you set it.

```bash theme={null}
curl -X POST "https://futures.kraken.com/derivatives/api/v3/assignmentprogram/add" \
  -d "contractType=flex" \
  -d "acceptLong=true" \
  -d "acceptShort=true" \
  -d "timeFrame=ALL" \
  -d "enabled=true" \
  -d "minimumProfitabilityPerAssignmentLongBps=120"
```

> [!WARNING]
>
> **A wallet-wide row on the `flex` wallet cannot carry `maxSize` or `maxPosition`.** Both are dropped on submission without an error, and `GET /assignmentprogram/current` reads back without them. The scope has nowhere to put a per-contract limit: it spans every flex contract at once. Bound a wallet-wide enrolment with the [off-book leverage cap](#limiting-your-exposure), or set the limits on a finer row.
>
> Single-collateral wallet rows are not affected — there `maxSize` and `maxPosition` apply normally.

A wallet-wide row is the broadest enrolment available, and it is forward-looking: a contract listed tomorrow enrols you the moment it goes live, with no further action. That is usually the point, but it does mean the scope grows without you touching it — carve out anything you do not want with a disabled pair or contract row.

### Currency pair

One row covers the perpetual and every dated expiry on the pair, which is usually what you want for an entire curve. The quote currency must be `USD`; anything else is rejected with `invalidCurrencyPair`.

```bash theme={null}
curl -X POST "https://futures.kraken.com/derivatives/api/v3/assignmentprogram/add" \
  -d "contractType=flex" \
  -d "baseCurrency=XBT" \
  -d "quoteCurrency=USD" \
  -d "acceptLong=true" \
  -d "acceptShort=true" \
  -d "timeFrame=ALL" \
  -d "enabled=true" \
  -d "maxSize=500000" \
  -d "maxPosition=2000000"
```

Both currencies must be sent together — sending one rejects with `invalidBaseCurrency` or `invalidQuoteCurrency` for whichever is missing. Each is accepted as either the unit code or the display name.

### Single contract

The finest scope, and the only one that can single out one expiry.

```bash theme={null}
curl -X POST "https://futures.kraken.com/derivatives/api/v3/assignmentprogram/add" \
  -d "contractType=flex" \
  -d "contract=PF_XBTUSD" \
  -d "acceptLong=true" \
  -d "acceptShort=false" \
  -d "timeFrame=WEEKDAYS" \
  -d "enabled=true" \
  -d "maxSize=250000" \
  -d "maxPosition=1000000"
```

The contract must settle to the wallet named in `contractType`, or the request is rejected with `contractNotFlexibleFutures`. An unknown contract rejects with `contractNotFound`.

### Single-collateral wallet

```bash theme={null}
curl -X POST "https://futures.kraken.com/derivatives/api/v3/assignmentprogram/add" \
  -d "contractType=fi_xbtusd" \
  -d "acceptLong=true" \
  -d "acceptShort=true" \
  -d "timeFrame=ALL" \
  -d "enabled=true" \
  -d "maxSize=1000" \
  -d "maxPosition=5000"
```

## What a preference controls

| Field | Meaning |
| :- | :- |
| `contractType` | The wallet the preference applies to, as it appears in `GET /accounts` — `flex` for the multi-collateral wallet, or a single-collateral wallet such as `fi_xbtusd` |
| `contract` | A single contract, e.g. `PF_XBTUSD`. Mutually exclusive with the currency pair |
| `baseCurrency` / `quoteCurrency` | A currency pair, e.g. `XBT` / `USD`. Both required together; quote must be `USD` |
| `acceptLong` / `acceptShort` | Which side you are willing to receive. A liquidated long is offered only to accounts with `acceptLong` |
| `maxSize` | The most you will take from **one** assignment |
| `maxPosition` | The most you will hold in the contract **in total**, including what you already have |
| `timeFrame` | `WEEKDAYS`, `WEEKEND` or `ALL`, evaluated in UTC. Saturday and Sunday are the weekend |
| `enabled` | `false` makes the row an opt-out rather than an opt-in. See [Turning assignments off](#turning-assignments-off) |
| `minimumProfitabilityPerAssignmentLongBps` / `…ShortBps` | Your minimum edge, per direction. See [Minimum profitability](#minimum-profitability) |

> [!WARNING]
>
> **`maxSize` and `maxPosition` are denominated differently per wallet.** On the multi-collateral (`flex`) wallet both are **quote-currency notional** — `maxSize=250000` on `PF_XBTUSD` means \$250,000, not 250,000 contracts. On single-collateral wallets both are in **contracts**. Getting this wrong silently sizes your exposure orders of magnitude away from what you intended.

Both limits are optional, and omitting them means no limit of that kind — only your margin and the platform caps stop you. Where they apply, both are validated on submission:

| Rule | Rejected with |
| :- | :- |
| `maxSize` at or above half the contract's maximum position | `assignmentParticipantOutsideMaxSizeBounds` |
| `maxPosition` at or above the contract's maximum position | `assignmentParticipantOutsideMaxSizeBounds` |
| `maxSize` zero or negative, or `maxPosition` negative | `assignmentParticipantOutsideMaxSizeBounds` |
| Either value too large or too precise to store — more than 17 digits before the decimal point or more than 11 after it | `assignmentParticipantOutsideMaxSizeBounds` |

> [!NOTE]
>
> Both limits report the same code on this API — a `maxPosition` breach is **not** distinguishable from a `maxSize` breach by the error alone. Check both values when you see it.

**`maxPosition=0` is accepted**, and it is the cleanest per-contract opt-out: every allocation is clamped against it, so you are never assigned that contract while it is set. `maxSize=0` is rejected — use `maxPosition` for this.

The `maxSize` ceiling is a platform parameter (currently half the contract maximum) and can be retuned. On a flex contract both bounds are evaluated as notional at the contract's current index price, so the ceiling moves with the market.

## How scopes combine

An account can hold rows at all three levels at once. For a given liquidation the engine resolves **one** effective preference per account, merging coarse into fine:

1. The **wallet** row supplies the base values.
2. The **currency pair** row for that contract's pair merges over it.
3. The **contract** row merges over that.

Merging is **field by field**: a field a finer row leaves unset falls through to the coarser row rather than being cleared. Where two levels set the same field, the finer one wins — contract beats pair, pair beats wallet.

```
wallet        maxSize=1000000   minLongBps=120   acceptShort=true
pair XBT/USD  maxSize=500000
contract PF_XBTUSD             minLongBps=90

effective for PF_XBTUSD:
              maxSize=500000    minLongBps=90    acceptShort=true
```

A row applies only inside its own `timeFrame`. A wallet row set to `WEEKDAYS` supplies nothing at the weekend, and the finer rows then resolve against no base at all.

### Turning assignments off

`enabled=false` is not a delete. Its meaning depends on the scope:

| Row | `enabled=false` means |
| :- | :- |
| Contract | **Opt out of that contract**, while coarser rows keep you enrolled everywhere else |
| Currency pair | **Opt out of every contract on that pair**, wallet row or not |
| Wallet | The wallet-wide enrolment stops — but any pair or contract row you have set stays active in its own right |

A disabled finer row wins over an enabled coarser one, so it is the way to carve one contract or one curve out of a broad enrolment without tearing the enrolment down.

To leave entirely, delete the rows (`POST /assignmentprogram/delete`), or use the off-book leverage cap below as a single switch.

## How an assignment is priced

The price is derived, not negotiated, from two numbers:

* **The mark price** — the fair value the engine holds the contract at.
* **The zero-equity price** — the price at which closing the position would take the liquidated account's equity to exactly zero, after the liquidation fee.

The gap between them, as a fraction of the mark, is what the liquidated account can afford to give away — call it the deliverable profitability. The engine clamps it between your own minimum and the platform maximum:

```
deliverable = (mark − zero-equity price) / mark        for a long being assigned
assignment price = mark × (1 − clamp(deliverable, your minimum, 250 bps))
```

Your minimum is the platform default of **75 bps** unless you have set one — see [Minimum profitability](#minimum-profitability). For a short the signs invert: the acceptor receives the short above the mark.

| Deliverable profitability | What happens | Your fill |
| :- | :- | :- |
| Below **your minimum** | The price is topped up to your minimum | Exactly your minimum |
| Between your minimum and 250 bps | The account can pay for it out of its own remaining equity | The full deliverable edge |
| Above **250 bps** | You fill at the cap and the surplus is retained | Exactly 250 bps of edge |

Worked through, on a long `PF_XBTUSD` position with the mark at \$100,000, for a participant on the default 75 bps:

| Zero-equity price | Deliverable | Assignment price | Note |
| :- | :- | :- | :- |
| \$99,900 | 10 bps | **\$99,250** | Below the floor — the remaining 65 bps is funded |
| \$99,000 | 100 bps | **\$99,000** | Inside the band — you fill at the zero-equity price itself |
| \$95,000 | 500 bps | **\$97,500** | Above the cap — you fill at 250 bps |

> [!NOTE]
>
> The 75 and 250 bps figures are platform parameters, not published in the API, and can be changed without a release. Treat them as the current configuration rather than a contractual band, and do not hard-code them.

Because the price is struck against the mark and never touches the book, **assignments do not consume order-book liquidity and your resting quotes are not involved**. An assignment can arrive while you are quoting both sides, and it neither fills nor cancels those quotes.

## Minimum profitability

By default every participant sits in one group at the platform floor. Setting `minimumProfitabilityPerAssignmentLongBps` or `…ShortBps` moves you into your own group and changes two things at once.

**It sets your place in the queue.** Groups are walked in ascending order of minimum — the participants asking for the least edge are offered the position first, and only what they cannot absorb passes to the next group. A *lower* minimum means *more* flow.

**It sets your price.** Your fill is the deliverable profitability, floored at your own minimum instead of the platform default. Where the liquidated account cannot deliver that much, the difference is funded — up to your minimum, and never past the platform maximum:

| Your preference | Deliverable is 20 bps | Deliverable is 150 bps |
| :- | :- | :- |
| Unset (platform default) | You fill at 75 bps | You fill at 150 bps |
| 50 bps | You fill at **50 bps** | You fill at 150 bps |
| 200 bps | You fill at **200 bps** — 180 of them funded | You fill at **200 bps** — 50 of them funded |

The two pull against each other, and that is the whole trade: a lower minimum buys flow at a worse price, a higher one buys price at the cost of flow. Neither is strictly better, and a preference is not a floor that only ever improves your fills.

> [!NOTE]
>
> **Your minimum is the price the engine targets, not a hard floor.** The top-up is funded from the liquidated account's remaining equity and the liquidity pool together. In the rare case that neither can cover it, the engine funds what it can and strikes at the best price available, which can be below your minimum.
>
> `GET /derivatives/api/v4/liquidity-pool` reports the pool's available funds, in total and per settlement currency, if you want to track the capacity behind the subsidy. It is a point-in-time figure and not a per-assignment guarantee.

Values are integer basis points and are validated on submission:

| Rule | Rejected with |
| :- | :- |
| Above the platform maximum (250 bps) | `minimumProfitabilityExceedsPlatformMaximum` |
| Exactly equal to the platform default | `minimumProfitabilityWouldHaveNoEffect` |
| Negative | `minimumProfitabilityNegative` |
| Set while the feature is switched off | `minimumProfitabilityPreferencesDisabled` |

The two directions are independent, and only the one matching the position you would receive is consulted — the long preference for a liquidated long, the short preference for a liquidated short.

## Who is eligible for a given assignment

At the moment of the liquidation the engine filters participants down to those that can actually take the position. You are skipped, silently, if any of these is true:

| Check | Skipped when |
| :- | :- |
| Direction | The position is a long and `acceptLong` is false, or a short and `acceptShort` is false |
| Time frame | The row's `WEEKDAYS` / `WEEKEND` window does not cover the current UTC day |
| Market restrictions | Your account is not permitted to trade that contract — jurisdiction, account restrictions, or the contract's own state |
| Margin | You do not have the margin to carry the additional position at the assignment price |
| `maxPosition` | Your existing position in the contract already sits at or above your cap |
| Off-book leverage cap | The fill would push your effective leverage past your configured cap |
| Live auction | The wallet has an in-account auction running — a wallet being auctioned is never assigned into |
| Self | You are the account being liquidated |

Nothing is published when you are skipped. Eligibility is re-evaluated for every assignment, so a participant that took one assignment can be skipped for the next one seconds later on margin alone.

## How a position is split

When several participants qualify, the position is divided in rounds rather than first-come-first-served:

1. Each participant is offered an equal share of what is left.
2. A participant who cannot take their whole share — because of `maxSize`, `maxPosition`, or margin — is filled as far as they can go, then dropped from later rounds.
3. What they could not take is redivided among the participants still standing, and the next round runs.

A participant that fails the margin check on its full share is offered **half** of it before being dropped, so a tight margin account still takes something rather than nothing.

Your share therefore depends on how many other participants are eligible at that instant, and is not predictable in advance. `maxSize` bounds it from above; nothing bounds it from below.

## Limiting your exposure

Beyond the per-preference limits there is an account-level cap that covers **all** off-book fills — assignments and RFQ offer fills together. It is the only bound available to a wallet-wide flex row.

```bash theme={null}
curl -X PUT "https://futures.kraken.com/derivatives/api/v3/rfq-assignment/max-leverage?maxLeverage=5"
```

The cap limits the effective leverage — gross open-position notional over margin equity — that off-book fills may take you to. Book orders are never affected.

| Value | Effect |
| :- | :- |
| A number in `[0, 100]` | Off-book fills may not push effective leverage past it |
| `0` | **The opt-out.** No exposure-increasing off-book fill at all, without withdrawing a single preference |
| Cleared (`DELETE`) | No account-level cap. Not the same as `0` |

Fills that *reduce* your gross open-position notional always go through, even at a cap of `0` and even when you are already over the cap, so opting out never traps you in existing exposure. The cap is set per master account and applies to the whole account.

## How assignments appear

There is no assignment-specific channel or state. An assignment reaches you as an ordinary fill, tagged so you can tell it apart:

| Where | Value |
| :- | :- |
| Fills (`fills` WebSocket feed, `GET /fills`) | `fillType: assignee` on the receiving side, `assignor` on the liquidated side |
| Order type in order and execution history | `assignment` |
| Public trade feed | `type: assignment` |
| Wallet history / account log | The position and balance changes, with the assignment execution referenced |

You are booked as the **maker** side of the trade, but assignments are charged at your **taker** fee rate.

> [!NOTE]
>
> Assignments print publicly at the assignment price, which is off the book by construction. On a quiet market this shows up in trade history and on candles as a print away from the prevailing bid and ask — up to 250 bps from the mark. It is not an erroneous trade, and no book liquidity traded at that price.

## Reference

### Endpoints

| Endpoint | Purpose |
| :- | :- |
| `GET /derivatives/api/v3/assignmentprogram/current` | List your active preferences with their ids |
| `POST /derivatives/api/v3/assignmentprogram/add` | Add a preference |
| `POST /derivatives/api/v3/assignmentprogram/delete` | Delete a preference by `id` |
| `GET /derivatives/api/v3/assignmentprogram/history` | Full change history, including deletions |
| `GET` / `PUT` / `DELETE /derivatives/api/v3/rfq-assignment/max-leverage` | Read, set, or clear the off-book leverage cap |
| `GET /derivatives/api/v4/liquidity-pool` | Available funds in the liquidity pool, in total and per settlement currency |

### Errors

| Code | Meaning |
| :- | :- |
| `assignmentProgramTermsNotAcceptedFrontend` | The account has not accepted the Assignment Program terms |
| `assignmentParticipantOutsideMaxSizeBounds` | `maxSize` or `maxPosition` is out of bounds — see [What a preference controls](#what-a-preference-controls) |
| `assignmentParticipantNotFound` | The `id` given to `delete` does not belong to your account |
| `mustSpecifyAssignmentParticipantForExactlyOneOfContractOrCurrencyPair` | Both `contract` and a currency pair were sent; pick one scope |
| `cannotSpecifyAssignmentParticipantForContractOrCurrencyPair` | A contract or currency pair was sent with a single-collateral `contractType` |
| `contractNotFound` / `contractNotFlexibleFutures` | The `contract` is unknown, or does not settle to the `contractType` given |
| `cashAccountTypeNotFound` | The `contractType` does not match any wallet on your account |
| `baseCurrencyNotFound` / `quoteCurrencyNotFound` | The currency is not a known asset |
| `invalidBaseCurrency` / `invalidQuoteCurrency` | One half of the currency pair was sent without the other |
| `invalidCurrencyPair` | The quote currency is not `USD`, or base and quote are the same |
| `minimumProfitabilityExceedsPlatformMaximum` | The preference is above the platform maximum and could never fill |
| `minimumProfitabilityWouldHaveNoEffect` | The preference equals the platform default; leave it unset instead |
| `minimumProfitabilityNegative` | Negative minimum profitability |
| `minimumProfitabilityPreferencesDisabled` | Minimum profitability preferences are not currently enabled |
| `rfqAssignmentMaxLeverageOutOfBounds` | `maxLeverage` is outside `[0, 100]`, or has more than two decimal places |
| `rfqAssignmentMaxLeverageDisabled` | The off-book leverage cap is not currently enabled |

### Things that are not true of assignments

A short list of assumptions worth discarding, because each one costs a debugging session:

* **You cannot decline one.** There is no accept or reject step; the position is booked and the first you know of it is the fill.
* **Your preference is not a quote.** You cannot price an individual assignment, and you are never asked.
* **A lower minimum is not a worse deal.** It moves you up the queue and lowers your floor at the same time — the two pull in opposite directions.
* **A higher minimum is not an off switch.** An assignment will be funded up to your minimum, so an above-default preference is reachable; what it costs you is queue position, not eligibility.
* **A finer row does not replace a coarser one.** Scopes merge field by field, so a contract row with one field set inherits everything else from the pair and wallet rows underneath it.
* **`maxSize` and `maxPosition` on a wallet-wide flex row do nothing.** They are dropped on submission — bound that scope with the off-book leverage cap.
* **Partial liquidations never assign.** Only a full liquidation offers a position to the program.
* **Assignments do not touch your orders.** No fill, no cancel, no self-trade interaction.
