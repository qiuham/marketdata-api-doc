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
source_url: 'https://docs.polymarket.com/programs/taker-rebates'
updated_at: 2026-11-25
---

# Taker Rebate Program

> Climb the tiers and earn daily pUSD rebates as you trade

Polymarket Tiers reward you for trading as a **taker**. The more taker volume you do, the higher your tier, the bigger the rebate you earn back on every trade you make from that point on. Every fee-paying **taker** trade earns **Weighted Volume (wV)**. Your tier is based on your Weighted Volume over the last 30 days, and rebates are paid every day in pUSD.

There are five rebate tiers, from **Gold** to **Onyx**. The first standard rebate tier requires \$200,000 in 30-day Weighted Volume. Your tier shows on your profile.

***

## How Tiers Work

Your tier is set by how much **Weighted Volume (wV)** you earn over the last 30 days. You earn Weighted Volume on your fee-paying taker trades. Two things decide your base Weighted Volume:

1. How big the trade is.
2. The price you bought at.

The formula:

```text theme={null}
wV = Trade Size × (1 − Entry Price) × Bonuses
```

* **Trade Size** is how much you put into the trade (shares × the price you paid), in dollars.
* **(1 − Entry Price)** is the upside per share. A share bought at 40¢ can win 60¢, so its upside is `0.60`.
* **Bonuses** are extra multipliers Polymarket may run on certain categories or events. The multiplier is `1` when no bonus applies.

### Example 1: A Normal Taker Trade

You buy 1,000 shares of a Politics market at 40¢, and the order fills right away (a taker trade).

* Trade Size = 1,000 × \$0.40 = **\$400**
* Upside per share = 1 − 0.40 = **0.60**
* Weighted Volume earned = 400 × 0.60 = **\$240 wV**

### Example 2: Why Price Matters

Two trades, both \$50 in size, both in fee-enabled Crypto markets:

* A trade at 50¢ earns: 50 × 0.50 = **\$25 wV**
* A trade at 5¢ earns: 50 × 0.95 = **\$47.50 wV**

Both trades count, and your Weighted Volume from every trade adds up over 30 days to set your tier.

***

> [!NOTE]
>
> Only taker trades that pay a fee earn Weighted Volume. If a market's taker fee
> is 0 (including markets temporarily made fee-free during a fee holiday),
> trades on it earn **no Weighted Volume and no rebate**.

***

## Tiers and Rebates

Once your 30-day Weighted Volume reaches a tier's threshold, you unlock that tier's rebate at the daily update. The higher your tier, the bigger your rebate. The updated rate applies to subsequent trades; earlier trades are not recalculated.

| Name | 30-day wV Needed | Rebate |
| - | - | - |
| None | Under \$200,000 | 0% |
| Gold | \$200,000 to under \$1 million | 10% |
| Platinum | \$1 million to under \$4 million | 25% |
| Diamond | \$4 million to under \$10 million | 40% |
| Obsidian | \$10 million to under \$75 million | 50% |
| Onyx | \$75 million and above | 60% |

### Example: Your Rebate Starts When You Reach the Tier

When **Gold** becomes your active tier, the 10% Gold rebate turns on for every fee-paying taker trade you make from then on.

If you keep climbing and hit **Diamond**, your rebate moves up to 40%, and again it applies only to your trades going forward.

Your tier updates every day based on your last 30 days of Weighted Volume. The updated rebate rate applies to subsequent trades.

You can look up current taker tiers and 30-day Weighted Volume for up to 100 proxy-wallet or EOA addresses without authentication. See [Get taker tiers for addresses](https://docs.polymarket.com/api-reference/rebates/get-taker-tiers-for-addresses.md).

***

## Read Tier Upgrade Notifications

Read unread account notifications to update your app when a daily snapshot
raises the account's taker tier. Authenticate the account whose notifications
you want to read.

> [tab] TypeScript
>
> Call `fetchNotifications()` on a `SecureClient` and narrow by the notification
> type before reading the payload.
>
> ```ts theme={null}
> import { NotificationType } from "@polymarket/client";
>
> const notifications = await client.fetchNotifications();
>
> for (const notification of notifications) {
>   if (notification.type === NotificationType.TAKER_TIER_UPGRADED) {
>     const { previousTier, tier, rebateBps, snapshotDate } =
>       notification.payload;
>     console.log(previousTier, tier, rebateBps, snapshotDate);
>   }
> }
> ```
>
> `TakerTierUpgradedNotification` has integer `previousTier`, `tier`, and
> `rebateBps` in its payload. `snapshotDate` is a `YYYY-MM-DD` string identifying
> the UTC day covered by the snapshot.

> [tab] Python
>
> Call `get_notifications()` on an `AsyncSecureClient`. The synchronous
> `SecureClient` provides the same method.
>
> ```python theme={null}
> from polymarket import NotificationType
>
> notifications = await client.get_notifications()
>
> for notification in notifications:
>     if notification.type == NotificationType.TAKER_TIER_UPGRADED:
>         payload = notification.payload
>         print(payload.previous_tier, payload.tier, payload.rebate_bps, payload.snapshot_date)
> ```
>
> `TakerTierUpgradedNotification` has integer `previous_tier`, `tier`, and
> `rebate_bps` in its payload. `snapshot_date` is a `datetime.date` identifying the
> UTC day covered by the snapshot.

> [tab] API
>
> Read unread notifications using the account's CLOB L2 credentials.
>
> ```bash theme={null}
> curl "https://clob.polymarket.com/notifications" \
>   -H "POLY_ADDRESS: <signer_address>" \
>   -H "POLY_API_KEY: <clob_api_key>" \
>   -H "POLY_PASSPHRASE: <clob_api_passphrase>" \
>   -H "POLY_SIGNATURE: <clob_l2_signature>" \
>   -H "POLY_TIMESTAMP: <clob_request_timestamp>"
> ```
>
> A tier upgrade notification has `type: 11` and this payload:
>
> ```json theme={null}
> {
>   "previous_tier": 0,
>   "tier": 3,
>   "rebate_bps": 1000,
>   "snapshot_date": "2026-11-21"
> }
> ```
>
> The tier and rebate values are integers. `snapshot_date` identifies the UTC day
> covered by the snapshot, rather than the notification's creation time.

The rebate rate uses basis points: 1,000 basis points means 10%. Tier upgrades
are account notifications; they do not indicate that a rebate payout has occurred.

***

## Rebates

* You can watch your rebates add up **live** as you trade, the same way referral earnings work.
* Rebates are **paid every day** in pUSD, straight to your account.
* A minimum accrued rebate of **\$1 pUSD** is required for a payout.

***

## Your Tier on Your Profile

Your tier shows on your Polymarket profile and on the leaderboards. As you climb from Gold to Onyx, your badge updates to match your current tier.

***

## Notes

* Only fee-paying **taker** trades earn Weighted Volume and count toward your tier. Maker trades (resting orders that add liquidity) do not. Makers are rewarded separately through the [Maker Rebates Program](https://docs.polymarket.com/programs/maker-rebates.md).
* Your active tier determines your rebate on subsequent trades. Earlier trades are not recalculated.
* Some markets are free to trade, including Geopolitics markets. These markets earn no Weighted Volume and no rebate.
* Your tier is based on your **last 30 days** of Weighted Volume and is updated every day.
* Rebates are paid once a day in pUSD.
* Rebate rates, tier thresholds, and any bonus multipliers are set by Polymarket and can change at any time without notice.
* Polymarket reserves the right, at its sole discretion, to adjust rebates and tier status for users.
* Polymarket reserves the right, at its sole discretion, to adjust or remove rebates and tier status for activity that breaks our Terms of Service, including but not limited to wash trading, self-matching, or other inauthentic trading.

***

## FAQ

> [accordion] Do maker trades count toward my tier
>
> No. Only fee-paying taker trades earn Weighted Volume and count toward your tier.
> Maker fills are rewarded separately through the
> [Maker Rebates Program](https://docs.polymarket.com/programs/maker-rebates.md).

> [accordion] When does my rebate start applying
>
> Your tier updates daily. The updated rebate rate applies to subsequent trades.
> There is no backfill on earlier trades.

> [accordion] When are rebates paid
>
> Rebates are paid once a day in pUSD, directly to your account. You must accrue
> at least **\$1** in rebates before a payout is issued.

> [accordion] How often does my tier update
>
> Your tier is recalculated daily based on your last 30 days of Weighted Volume.
> The updated rebate rate applies to subsequent trades.

> [accordion] What happens if I slow down trading
>
> Your tier can move down at the daily update if your 30-day Weighted Volume
> drops below your current tier's threshold.

> [accordion] Which markets earn Weighted Volume
>
> All fee-enabled categories earn Weighted Volume using the same price-weighted
> formula. Geopolitics markets are free to trade and earn no Weighted Volume.

> [accordion] Are third-party integrations using omnibus wallets eligible
>
> No. Third-party integrations using omnibus wallets are not eligible for the
> Taker Rebate Program.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
