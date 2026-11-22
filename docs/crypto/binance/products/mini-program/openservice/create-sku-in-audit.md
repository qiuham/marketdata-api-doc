---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/create-sku-in-audit
api_type: Guide
updated_at: 2026-11-22 18:35:42.087314
---

# CreateSKUInAudit

# <a name="CreateSKUInAudit"></a>CreateSKUInAudit

Creates a new SKU for the given app and submits it for audit. The SKU is set as available and
enabled for sale by default, but will not be visible to users until it passes the audit process.

**Host**: **dip-cb.binanceapi.com**

**POST** /mp-api/v1/apps/\{appId\}/skus

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**           |
| :------------ | :------------------------ |
| appId         | AppId of the mini program |

**Body Parameters**

| **Parameter**             | **Type**                                     | **Required**                              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **Example**                          |
| :------------------------ | :------------------------------------------- | :---------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| category                  | string                                       | Yes                                       | Category of this SKU.<br/>See [Valid Categories](#valid-categories) for accepted values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | "Games"                              |
| coverImageFileId          | string                                       | Yes                                       | Cover image for this SKU.<br/>Must be a file ID returned by [UploadFile](./upload-file). The file must have passed safety checks before use.                                                                                                                                                                                                                                                                                                                                                                                                               | f7574adb-0ccb-4281-9ed6-943f11a1e85a |
| names                     | \{[key: string]: string\}                    | Yes                                       | Locale-keyed display name map for this SKU.<br/>**Rules:** `en` key is required. Maximum 128 characters per value. Values must not contain HTML markup (e.g. `<b>`, `<script>`) — such requests are rejected with `900001 Invalid Parameter`.<br/>See the [Language Code section](/products/mini-program/openservice/appendix) for accepted keys.                                                                                                                                                                                                          | \{"en": "PUBG 100 point"\}           |
| skuId                     | string                                       | Yes                                       | Merchant-assigned identifier for this SKU.<br/>**Rules:** Must be unique within your app. Maximum 255 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                          | pubg_point_100                       |
| originalPrice             | number                                       | Required when `pricingMode` is `"flat"`   | List price in `currency` major units (e.g. `9.99` means 9.99 of `currency`; USD when `currency` is omitted).<br/>**`"flat"` mode:** Required. Must be > 0. Must be ≥ `sellingPrice`. Sub-cent amounts are truncated (e.g., 9.9999 → 9.99).<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the maximum `originalPrice` across all tiers.<br/>**`"custom"` mode:** Optional. Saved as-is if provided; otherwise back-calculated from `discountPercentage`.                                                            | 9.99                                 |
| sellingPrice              | number                                       | Required when `pricingMode` is `"flat"`   | Actual selling price in `currency` major units.<br/>**`"flat"` mode:** Required. Must be > 0. Must be ≤ `originalPrice`. Sub-cent amounts are truncated (e.g., 9.9999 → 9.99).<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the minimum `sellingPrice` across all tiers.<br/>**`"custom"` mode:** Optional. Saved as-is if provided; otherwise set to `minSellingPrice`.                                                                                                                                          | 6                                    |
| discountPercentage        | int                                          | Required when `pricingMode` is `"custom"` | Discount percentage shown to buyers.<br/>**Values:** 1–99.<br/>**`"custom"` mode:** Required. Used to back-calculate `originalPrice` from `minSellingPrice` (formula: `original = min / (1 − discount/100)`).<br/>**`"flat"` mode:** Ignored if provided — always auto-calculated from the price difference (`floor((originalPrice − sellingPrice) / originalPrice × 100)`) and shown as the price reduction badge.<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the maximum effective discount across all tiers. | 32                                   |
| countryWhitelist          | Array\<String\>                              | No                                        | Countries where this SKU is eligible to be displayed.<br/>**Values:** [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) country codes.<br/>If omitted, the SKU is available in all countries.                                                                                                                                                                                                                                                                                                       | ["JP"]                               |
| countryBlacklist          | Array\<String\>                              | No                                        | Countries where this SKU must not be displayed.<br/>**Values:** [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) country codes.                                                                                                                                                                                                                                                                                                                                                                    | ["CN", "GB"]                         |
| path                      | string                                       | No                                        | Mini-program page path to open when the SKU is tapped.<br/>**Rules:** Must start with `/`. Maximum 1024 characters. Query parameters (after `?`) are parsed and stored separately.<br/>Defaults to `/pages/index/index` when omitted.                                                                                                                                                                                                                                                                                                                      | /pages/index/index?foo=bar&baz=qux   |
| description               | string                                       | Yes                                       | Description for this SKU.<br/>**Rules:** Must not contain HTML markup (e.g. `<b>`, `<script>`) — such requests are rejected with `900001 Invalid Parameter`.                                                                                                                                                                                                                                                                                                                                                                                               | A virtual top-up item                |
| stocks                    | int                                          | No                                        | Merchant-provided inventory quantity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 100                                  |
| autoDelivery              | bool                                         | No                                        | Whether the SKU supports automatic delivery after purchase. Only SKUs with auto delivery enabled can complete the full purchase flow within Lifestyle; SKUs without it require the merchant to fulfill delivery out-of-band.                                                                                                                                                                                                                                                                                                                               | true                                 |
| maxQuantity               | int                                          | No                                        | Maximum quantity a buyer can purchase in a single order.<br/>**Values:** 1–99. Defaults to `99` when omitted.<br/>Set to `1` to hide the quantity input widget on the UI entirely. Applies to all pricing modes.                                                                                                                                                                                                                                                                                                                                           | 5                                    |
| currency                  | string                                       | No                                        | ISO 4217 currency code that all monetary amounts on this SKU are denominated in (applies to **all** pricing modes: `flat`, `tiered`, and `custom`). Defaults to `"USD"` when omitted.<br/>⚠️ **`"USD"` is currently the only accepted value** — any other currency is rejected. See [Currency availability](#currency-availability). When omitted or `"USD"`, the legacy `*_usd_cent` fields continue to behave exactly as today (USD cents).                                                                                                              | "USD"                                |
| pricingMode               | string                                       | No                                        | Determines how the SKU is priced. Defaults to `"flat"` when omitted.<br/>**Values:**<br/>- `"flat"` — single fixed price defined by `sellingPrice` / `originalPrice`.<br/>- `"tiered"` — multiple fixed denominations defined by `pricingTiers`.<br/>- `"custom"` — buyer enters any amount within the range defined by `minSellingPrice` / `maxSellingPrice`.                                                                                                                                                                                             | "tiered"                             |
| pricingTiers              | Array\<[PricingTier](#pricing-tier-object)\> | Required when `pricingMode` is `"tiered"` | List of fixed denomination options for this SKU.<br/>**Rules:** 1–50 tiers. Each tier must have a unique `tierId`.<br/>**`"tiered"` mode:** Required.<br/>**`"flat"` / `"custom"` mode:** Must be absent or empty.<br/>See [PricingTier Object](#pricing-tier-object) below. Each tier's prices are in `currency` major units (use `originalPrice` / `sellingPrice` on the tier object).                                                                                                                                                                   | see example below                    |
| minSellingPrice           | number                                       | Required when `pricingMode` is `"custom"` | Minimum amount the buyer may enter, in `currency` major units (e.g. `3.00` means 3.00 of `currency`).<br/>**Rules:** Must be > 0. Must be < `maxSellingPrice`.<br/>Only applies when `pricingMode` is `"custom"`.                                                                                                                                                                                                                                                                                                                                          | 3.00                                 |
| maxSellingPrice           | number                                       | Required when `pricingMode` is `"custom"` | Maximum amount the buyer may enter, in `currency` major units.<br/>**Rules:** Must be > `minSellingPrice`.<br/>Only applies when `pricingMode` is `"custom"`.                                                                                                                                                                                                                                                                                                                                                                                              | 200                                  |
| customPriceOptions        | Array\<number\>                              | No                                        | Preset quick-select amounts shown to the buyer, each in `currency` major units.<br/>**Rules:** Maximum 5 entries. Each value must be > 0 and within [`minSellingPrice`, `maxSellingPrice`].<br/>Only applies when `pricingMode` is `"custom"`. When omitted, 5 evenly-spaced values between min and max are generated automatically.                                                                                                                                                                                                                       | [10, 20, 50, 100, 200]               |
| minSellingPriceUsdCent    | int                                          | _Deprecated_                              | ⚠️ **Deprecated.** Use `minSellingPrice` instead. Legacy field expressed in **USD cents** (not `currency`); only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). When `minSellingPrice` is provided with a non-zero value, it takes precedence and this field is ignored.                                                                                                                                                         | 1000                                 |
| maxSellingPriceUsdCent    | int                                          | _Deprecated_                              | ⚠️ **Deprecated.** Use `maxSellingPrice` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). When `maxSellingPrice` is provided with a non-zero value, it takes precedence and this field is ignored.                                                                                                                                                                                           | 50000                                |
| customPriceOptionsUsdCent | Array\<int\>                                 | _Deprecated_                              | ⚠️ **Deprecated.** Use `customPriceOptions` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). When `customPriceOptions` is provided and non-empty, it takes precedence and this field is ignored.                                                                                                                                                                                             | [1000, 2500, 5000]                   |
| exchangeMargin            | number                                       | No                                        | Optional currency-exchange margin percentage applied when converting money from `currency` (this SKU's currency) to another currency at checkout/settlement (e.g. `1.5` means a 1.5% margin).<br/>**Rules:** Must be finite and in `[0, 100)`.                                                                                                                                                                                                                                                                                                             | 1.5                                  |

**Request Body — flat pricing (default)**

```json
{
  "category": "Games",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": {
    "en": "PUBG 100 points",
    "zh-TW": "PUBG 100 點"
  },
  "skuId": "pubg_point_100",
  "currency": "USD",
  "originalPrice": 9.99,
  "sellingPrice": 6.99,
  "countryWhitelist": ["JP"],
  "countryBlacklist": ["CN", "GB"],
  "path": "/pages/index/index?foo=bar&baz=qux",
  "description": "A virtual top-up item",
  "stocks": 100,
  "autoDelivery": true,
  "maxQuantity": 5,
  "exchangeMargin": 1.5
}
```

**Request Body — tiered pricing**

```json
{
  "category": "Shopping",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "JD.com CN Gift Card" },
  "skuId": "jdcom-cn-giftcard",
  "description": "JD.com gift card redeemable in China",
  "countryWhitelist": ["CN"],
  "path": "/pages/index/index",
  "stocks": 500,
  "autoDelivery": true,
  "currency": "USD",
  "pricingMode": "tiered",
  "pricingTiers": [
    {
      "tierId": "tier_jdcn_30cny",
      "names": { "en": "JD.com CN 30 CNY" },
      "originalPrice": 5.9,
      "sellingPrice": 4.72,
      "autoDelivery": true,
      "maxQuantity": 10,
      "stocks": 200
    },
    {
      "tierId": "tier_jdcn_50cny",
      "names": { "en": "JD.com CN 50 CNY" },
      "originalPrice": 9.8,
      "sellingPrice": 7.84,
      "autoDelivery": true,
      "maxQuantity": 5,
      "stocks": 300
    }
  ]
}
```

**Request Body — custom pricing**

```json
{
  "category": "Games",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "Custom Top-up" },
  "skuId": "custom-topup",
  "description": "Top up any amount between $10 and $500",
  "countryWhitelist": ["JP"],
  "path": "/pages/topup/index",
  "currency": "USD",
  "pricingMode": "custom",
  "discountPercentage": 20,
  "minSellingPrice": 10,
  "maxSellingPrice": 500,
  "customPriceOptions": [10, 25, 50]
}
```

## <a name="currency-availability"></a>Currency availability

> ⚠️ **Read this before using the non-USD examples below.** `"USD"` is currently the **only**
> accepted `currency` value. A request specifying any other currency is rejected — the error arrives
> as `900003 Unexpected Error` with a message of the form
> `currency "<code>" is not supported; allowed: [USD]` (e.g.
> `currency "PLN" is not supported; allowed: [USD]`).
>
> The PLN, EUR and GBP examples that follow, and the non-USD behaviour described in
> [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility),
> document the **intended** multi-currency contract for forward compatibility. They will work once
> additional currencies are enabled on the platform; they fail today. Until then, omit `currency` or
> send `"USD"`.

**Request Body — flat pricing in PLN (non-USD denomination)**

When `currency` is a non-USD code, all monetary fields (`originalPrice`, `sellingPrice`,
`minSellingPrice`, `maxSellingPrice`, `customPriceOptions`, and each
[PricingTier](#pricing-tier-object)'s `originalPrice`/`sellingPrice`) are expressed in that
currency's major units. For a PLN-denominated fixed-price SKU:

```json
{
  "category": "Entertainment",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "Eneba PLN Gift Card" },
  "skuId": "eneba-pln-giftcard",
  "description": "Eneba PLN gift card, buyer picks the amount",
  "countryWhitelist": ["PL"],
  "path": "/pages/detail/index",
  "currency": "PLN",
  "pricingMode": "flat",
  "originalPrice": 200,
  "sellingPrice": 190
}
```

**Request Body — custom pricing in PLN**

A PLN-denominated custom-amount SKU. `minSellingPrice`/`maxSellingPrice`/`customPriceOptions` here
are in **PLN** (the major unit): `3` = 3.00 PLN, `200` = 200.00 PLN, presets
`[10, 20, 50, 100, 200]` = 10 / 20 / 50 / 100 / 200 PLN.

```json
{
  "category": "Entertainment",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "Eneba PLN Gift Card" },
  "skuId": "eneba-pln-giftcard-custom",
  "description": "Eneba PLN gift card, buyer enters the amount",
  "countryWhitelist": ["PL"],
  "path": "/pages/topup/index",
  "currency": "PLN",
  "pricingMode": "custom",
  "discountPercentage": 5,
  "minSellingPrice": 3,
  "maxSellingPrice": 200,
  "customPriceOptions": [10, 20, 50, 100, 200]
}
```

**Request Body — flat pricing with cross-currency exchange margin (eSIM)**

When a SKU's `currency` differs from a buyer's settlement currency, `exchangeMargin` lets you factor
in your own currency-conversion cost. Here a EUR-denominated eSIM plan applies a 2% margin:

```json
{
  "category": "eSIM",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "Europe 5GB Data eSIM" },
  "skuId": "esim-eu-5gb",
  "description": "5GB data eSIM valid for 30 days across the EU",
  "countryWhitelist": ["DE", "FR", "ES", "IT"],
  "path": "/pages/esim/index",
  "currency": "EUR",
  "originalPrice": 24.99,
  "sellingPrice": 19.99,
  "autoDelivery": true,
  "exchangeMargin": 2.0
}
```

**Request Body — manually-fulfilled physical SKU (`autoDelivery` disabled)**

Physical or otherwise manually-fulfilled goods should set `autoDelivery` to `false`. Buyers can
still complete checkout, but Lifestyle does not attempt automatic delivery — the merchant fulfills
the order out-of-band (e.g. shipping):

```json
{
  "category": "Shopping",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "Limited Edition Sneakers" },
  "skuId": "sneakers-ltd-42",
  "description": "Limited edition sneakers, size 42, shipped within 5 business days",
  "countryWhitelist": ["US", "CA"],
  "path": "/pages/shop/sneakers",
  "currency": "USD",
  "originalPrice": 189.99,
  "sellingPrice": 149.99,
  "stocks": 30,
  "autoDelivery": false,
  "maxQuantity": 3
}
```

**Request Body — single-purchase booking SKU (`maxQuantity` = 1)**

Set `maxQuantity` to `1` to hide the quantity selector entirely — useful for one-per-order items
such as travel bookings or event passes:

```json
{
  "category": "Travel",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "City Sightseeing Day Pass" },
  "skuId": "sightseeing-daypass",
  "description": "One-day hop-on hop-off sightseeing bus pass",
  "countryWhitelist": ["GB"],
  "path": "/pages/travel/daypass",
  "currency": "GBP",
  "originalPrice": 45,
  "sellingPrice": 39,
  "stocks": 500,
  "autoDelivery": false,
  "maxQuantity": 1
}
```

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {},
  "success": true
}
```

| ErrorCode | Remark                    |
| :-------- | :------------------------ |
| 000000    | Success                   |
| 900001    | Invalid Parameter         |
| 900002    | JWT Authentication Failed |
| 900003    | Unexpected Error          |
| 900004    | Invalid FileId            |
| 900260    | Invalid SkuId             |

## Pricing Tier Object

Each entry in `pricingTiers` is a `PricingTier` object with the following fields. `pricingTiers` is
only used when `pricingMode` is `"tiered"`.

| **Field**            | **Type**                  | **Required** | **Description**                                                                                                                                                                                                                                       |
| :------------------- | :------------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tierId               | string                    | Yes          | Stable merchant-assigned identifier for this tier. Must be unique within the SKU. Max 255 characters.                                                                                                                                                 |
| names                | \{[key: string]: string\} | Yes          | Locale-keyed display name map. `en` is required.                                                                                                                                                                                                      |
| description          | string                    | No           | Optional description for this tier.                                                                                                                                                                                                                   |
| originalPrice        | number                    | Yes          | List price in `currency` major units. Must be ≥ `sellingPrice`.                                                                                                                                                                                       |
| sellingPrice         | number                    | Yes          | Actual selling price in `currency` major units. Must be > 0 and ≤ `originalPrice`.                                                                                                                                                                    |
| autoDelivery         | bool                      | No           | Whether this tier supports automatic delivery after purchase. When set, overrides the SKU-level `autoDelivery` for orders of this tier.                                                                                                               |
| maxQuantity          | int                       | No           | Maximum quantity a buyer can purchase per order for this tier (1–99). When set, overrides the SKU-level `maxQuantity` for this tier.                                                                                                                  |
| stocks               | int                       | No           | Inventory quantity for this tier. When set, overrides the SKU-level `stocks` for this tier.                                                                                                                                                           |
| originalPriceUsdCent | int                       | _Deprecated_ | ⚠️ **Deprecated.** Use `originalPrice` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). |
| sellingPriceUsdCent  | int                       | _Deprecated_ | ⚠️ **Deprecated.** Use `sellingPrice` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility).  |

**Validation rules for `pricingTiers`:**

- At least one tier is required when `pricingMode` is `"tiered"`.
- Maximum 50 tiers per SKU.
- `tierId` must be unique within the request.
- `pricingTiers` must be absent or empty when `pricingMode` is `"flat"` or `"custom"`.

## Legacy price fields & backward compatibility

> **Note.** The non-USD rules in this section are forward-looking — see
> [Currency availability](#currency-availability). Every SKU is USD-denominated today, so only the
> USD rules below are currently in effect.

The `*_usd_cent` fields (`minSellingPriceUsdCent`, `maxSellingPriceUsdCent`,
`customPriceOptionsUsdCent`, and the `originalPriceUsdCent` / `sellingPriceUsdCent` on each
[PricingTier](#pricing-tier-object)) are **deprecated**. They are kept and still accepted so
existing merchant integrations that send USD-cents amounts keep working unchanged. New integrations
should send `currency` plus the major-unit fields (`originalPrice`, `sellingPrice`,
`minSellingPrice`, `maxSellingPrice`, `customPriceOptions`) instead.

**How the request is normalized (both new and legacy fields accepted):**

1. **Precedence.** If a new major-unit field is present with a non-zero value, it wins; the legacy
   `*_usd_cent` value is ignored for that field. If the new field is absent or zero, the server
   falls back to the legacy field and converts it to the new major-unit value:
   `major = legacy_cent / 100`. This legacy conversion only happens when `currency == "USD"` — a
   legacy field cannot represent a non-USD amount, so for a non-USD SKU any `*_usd_cent` value is
   ignored (dropped) and the corresponding `*_usd_cent` column is stored as `0`.
2. **Currency default.** If `currency` is omitted, it defaults to `"USD"`. Existing merchants that
   send neither `currency` nor the new major-unit fields therefore behave exactly as before — their
   `*_usd_cent` values are interpreted as USD cents and mirrored into the new major-unit fields.
3. **Persistence.** For a USD SKU the server stores **both** representations (legacy USD-cents and
   new major-unit) and keeps them in sync, so reads via either field set return consistent values.
   For a non-USD SKU only the new major-unit fields are populated; the legacy `*_usd_cent` fields
   are stored as `0` (there is no meaningful USD-cents value without the platform exchange rate,
   which is not stored on the SKU).

**How responses backfill the legacy fields (so existing readers keep working):**

- On read (GetSKU / ListSKUs), the response always populates the new major-unit fields from the
  stored major-unit values.
- For USD SKUs the legacy `*_usd_cent` response fields are **back-filled** from the major-unit
  values when not already present: `legacy_cent = round(major × 100)`. So a USD SKU written through
  the new major-unit fields still returns correct `*_usd_cent` values to clients reading the legacy
  fields.
- For non-USD SKUs the legacy `*_usd_cent` response fields are returned as `0`/absent — clients
  reading only the legacy fields see "no price" for a non-USD SKU (graceful degradation, not
  corruption). To display a non-USD SKU correctly, read `currency` + the major-unit fields.

> **Migration recommendation.** Move integrations to `currency` + the major-unit fields at your
> earliest convenience. The `*_usd_cent` fields will be removed in a future major version.

## Valid Categories

| Category            |
| :------------------ |
| AI Tools            |
| eSIM                |
| Fashion & Beauty    |
| Food & Grocery      |
| Entertainment       |
| Games               |
| Shopping            |
| Telecom & Utilities |
| Travel              |

## Changelog

| Date       | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-07-20 | **Flat-mode discount is always derived.** In `"flat"` mode, `discountPercentage` is now always computed from `originalPrice` / `sellingPrice` (`floor((originalPrice − sellingPrice) / originalPrice × 100)`); any value supplied by the caller is ignored, matching `"tiered"` mode. `"custom"` mode is unchanged — the field is still required there and drives the `originalPrice` back-calculation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2026-07-20 | **Exchange margin.** Added the optional `exchangeMargin` field — a merchant-provided currency-exchange margin percentage (e.g. `1.5` = 1.5%) applied when converting money from `currency` to another currency at checkout/settlement. Must be finite and in `[0, 100)`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 2026-07-15 | **HTML rejection.** `names` and `description` are now rejected outright (`900001 Invalid Parameter`) if they contain HTML markup (e.g. `<b>`, `<script>`), instead of being silently escaped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 2026-07-14 | **Multi-currency pricing.** Added the `currency` field (ISO 4217, default `"USD"`, applies to **all** pricing modes — `flat`, `tiered`, `custom`) so an SKU can be denominated in a non-USD currency (e.g. `PLN`). Added currency-aware major-unit price fields: `originalPrice` / `sellingPrice` (now explicitly described as `currency` major units), `minSellingPrice`, `maxSellingPrice`, `customPriceOptions`, and per-tier `originalPrice` / `sellingPrice` on the [PricingTier](#pricing-tier-object) object. **Deprecated** the legacy USD-cents fields (`minSellingPriceUsdCent`, `maxSellingPriceUsdCent`, `customPriceOptionsUsdCent`, per-tier `originalPriceUsdCent` / `sellingPriceUsdCent`) — they remain accepted for backward compatibility (USD only; ignored when a major-unit field is also sent). Added a PLN flat-pricing and a PLN custom-pricing request example. See [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility) for the full request-normalization and response-backfill contract. |

---

# CreateSKUInAudit

# <a name="CreateSKUInAudit"></a>CreateSKUInAudit

Creates a new SKU for the given app and submits it for audit. The SKU is set as available and
enabled for sale by default, but will not be visible to users until it passes the audit process.

**Host**: **dip-cb.binanceapi.com**

**POST** /mp-api/v1/apps/\{appId\}/skus

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**           |
| :------------ | :------------------------ |
| appId         | AppId of the mini program |

**Body Parameters**

| **Parameter**             | **Type**                                     | **Required**                              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **Example**                          |
| :------------------------ | :------------------------------------------- | :---------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| category                  | string                                       | Yes                                       | Category of this SKU.<br/>See [Valid Categories](#valid-categories) for accepted values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | "Games"                              |
| coverImageFileId          | string                                       | Yes                                       | Cover image for this SKU.<br/>Must be a file ID returned by [UploadFile](./upload-file). The file must have passed safety checks before use.                                                                                                                                                                                                                                                                                                                                                                                                               | f7574adb-0ccb-4281-9ed6-943f11a1e85a |
| names                     | \{[key: string]: string\}                    | Yes                                       | Locale-keyed display name map for this SKU.<br/>**Rules:** `en` key is required. Maximum 128 characters per value. Values must not contain HTML markup (e.g. `<b>`, `<script>`) — such requests are rejected with `900001 Invalid Parameter`.<br/>See the [Language Code section](/products/mini-program/openservice/appendix) for accepted keys.                                                                                                                                                                                                          | \{"en": "PUBG 100 point"\}           |
| skuId                     | string                                       | Yes                                       | Merchant-assigned identifier for this SKU.<br/>**Rules:** Must be unique within your app. Maximum 255 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                          | pubg_point_100                       |
| originalPrice             | number                                       | Required when `pricingMode` is `"flat"`   | List price in `currency` major units (e.g. `9.99` means 9.99 of `currency`; USD when `currency` is omitted).<br/>**`"flat"` mode:** Required. Must be > 0. Must be ≥ `sellingPrice`. Sub-cent amounts are truncated (e.g., 9.9999 → 9.99).<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the maximum `originalPrice` across all tiers.<br/>**`"custom"` mode:** Optional. Saved as-is if provided; otherwise back-calculated from `discountPercentage`.                                                            | 9.99                                 |
| sellingPrice              | number                                       | Required when `pricingMode` is `"flat"`   | Actual selling price in `currency` major units.<br/>**`"flat"` mode:** Required. Must be > 0. Must be ≤ `originalPrice`. Sub-cent amounts are truncated (e.g., 9.9999 → 9.99).<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the minimum `sellingPrice` across all tiers.<br/>**`"custom"` mode:** Optional. Saved as-is if provided; otherwise set to `minSellingPrice`.                                                                                                                                          | 6                                    |
| discountPercentage        | int                                          | Required when `pricingMode` is `"custom"` | Discount percentage shown to buyers.<br/>**Values:** 1–99.<br/>**`"custom"` mode:** Required. Used to back-calculate `originalPrice` from `minSellingPrice` (formula: `original = min / (1 − discount/100)`).<br/>**`"flat"` mode:** Ignored if provided — always auto-calculated from the price difference (`floor((originalPrice − sellingPrice) / originalPrice × 100)`) and shown as the price reduction badge.<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the maximum effective discount across all tiers. | 32                                   |
| countryWhitelist          | Array\<String\>                              | No                                        | Countries where this SKU is eligible to be displayed.<br/>**Values:** [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) country codes.<br/>If omitted, the SKU is available in all countries.                                                                                                                                                                                                                                                                                                       | ["JP"]                               |
| countryBlacklist          | Array\<String\>                              | No                                        | Countries where this SKU must not be displayed.<br/>**Values:** [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) country codes.                                                                                                                                                                                                                                                                                                                                                                    | ["CN", "GB"]                         |
| path                      | string                                       | No                                        | Mini-program page path to open when the SKU is tapped.<br/>**Rules:** Must start with `/`. Maximum 1024 characters. Query parameters (after `?`) are parsed and stored separately.<br/>Defaults to `/pages/index/index` when omitted.                                                                                                                                                                                                                                                                                                                      | /pages/index/index?foo=bar&baz=qux   |
| description               | string                                       | Yes                                       | Description for this SKU.<br/>**Rules:** Must not contain HTML markup (e.g. `<b>`, `<script>`) — such requests are rejected with `900001 Invalid Parameter`.                                                                                                                                                                                                                                                                                                                                                                                               | A virtual top-up item                |
| stocks                    | int                                          | No                                        | Merchant-provided inventory quantity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 100                                  |
| autoDelivery              | bool                                         | No                                        | Whether the SKU supports automatic delivery after purchase. Only SKUs with auto delivery enabled can complete the full purchase flow within Lifestyle; SKUs without it require the merchant to fulfill delivery out-of-band.                                                                                                                                                                                                                                                                                                                               | true                                 |
| maxQuantity               | int                                          | No                                        | Maximum quantity a buyer can purchase in a single order.<br/>**Values:** 1–99. Defaults to `99` when omitted.<br/>Set to `1` to hide the quantity input widget on the UI entirely. Applies to all pricing modes.                                                                                                                                                                                                                                                                                                                                           | 5                                    |
| currency                  | string                                       | No                                        | ISO 4217 currency code that all monetary amounts on this SKU are denominated in (applies to **all** pricing modes: `flat`, `tiered`, and `custom`). Defaults to `"USD"` when omitted.<br/>⚠️ **`"USD"` is currently the only accepted value** — any other currency is rejected. See [Currency availability](#currency-availability). When omitted or `"USD"`, the legacy `*_usd_cent` fields continue to behave exactly as today (USD cents).                                                                                                              | "USD"                                |
| pricingMode               | string                                       | No                                        | Determines how the SKU is priced. Defaults to `"flat"` when omitted.<br/>**Values:**<br/>- `"flat"` — single fixed price defined by `sellingPrice` / `originalPrice`.<br/>- `"tiered"` — multiple fixed denominations defined by `pricingTiers`.<br/>- `"custom"` — buyer enters any amount within the range defined by `minSellingPrice` / `maxSellingPrice`.                                                                                                                                                                                             | "tiered"                             |
| pricingTiers              | Array\<[PricingTier](#pricing-tier-object)\> | Required when `pricingMode` is `"tiered"` | List of fixed denomination options for this SKU.<br/>**Rules:** 1–50 tiers. Each tier must have a unique `tierId`.<br/>**`"tiered"` mode:** Required.<br/>**`"flat"` / `"custom"` mode:** Must be absent or empty.<br/>See [PricingTier Object](#pricing-tier-object) below. Each tier's prices are in `currency` major units (use `originalPrice` / `sellingPrice` on the tier object).                                                                                                                                                                   | see example below                    |
| minSellingPrice           | number                                       | Required when `pricingMode` is `"custom"` | Minimum amount the buyer may enter, in `currency` major units (e.g. `3.00` means 3.00 of `currency`).<br/>**Rules:** Must be > 0. Must be < `maxSellingPrice`.<br/>Only applies when `pricingMode` is `"custom"`.                                                                                                                                                                                                                                                                                                                                          | 3.00                                 |
| maxSellingPrice           | number                                       | Required when `pricingMode` is `"custom"` | Maximum amount the buyer may enter, in `currency` major units.<br/>**Rules:** Must be > `minSellingPrice`.<br/>Only applies when `pricingMode` is `"custom"`.                                                                                                                                                                                                                                                                                                                                                                                              | 200                                  |
| customPriceOptions        | Array\<number\>                              | No                                        | Preset quick-select amounts shown to the buyer, each in `currency` major units.<br/>**Rules:** Maximum 5 entries. Each value must be > 0 and within [`minSellingPrice`, `maxSellingPrice`].<br/>Only applies when `pricingMode` is `"custom"`. When omitted, 5 evenly-spaced values between min and max are generated automatically.                                                                                                                                                                                                                       | [10, 20, 50, 100, 200]               |
| minSellingPriceUsdCent    | int                                          | _Deprecated_                              | ⚠️ **Deprecated.** Use `minSellingPrice` instead. Legacy field expressed in **USD cents** (not `currency`); only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). When `minSellingPrice` is provided with a non-zero value, it takes precedence and this field is ignored.                                                                                                                                                         | 1000                                 |
| maxSellingPriceUsdCent    | int                                          | _Deprecated_                              | ⚠️ **Deprecated.** Use `maxSellingPrice` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). When `maxSellingPrice` is provided with a non-zero value, it takes precedence and this field is ignored.                                                                                                                                                                                           | 50000                                |
| customPriceOptionsUsdCent | Array\<int\>                                 | _Deprecated_                              | ⚠️ **Deprecated.** Use `customPriceOptions` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). When `customPriceOptions` is provided and non-empty, it takes precedence and this field is ignored.                                                                                                                                                                                             | [1000, 2500, 5000]                   |
| exchangeMargin            | number                                       | No                                        | Optional currency-exchange margin percentage applied when converting money from `currency` (this SKU's currency) to another currency at checkout/settlement (e.g. `1.5` means a 1.5% margin).<br/>**Rules:** Must be finite and in `[0, 100)`.                                                                                                                                                                                                                                                                                                             | 1.5                                  |

**Request Body — flat pricing (default)**

```json
{
  "category": "Games",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": {
    "en": "PUBG 100 points",
    "zh-TW": "PUBG 100 點"
  },
  "skuId": "pubg_point_100",
  "currency": "USD",
  "originalPrice": 9.99,
  "sellingPrice": 6.99,
  "countryWhitelist": ["JP"],
  "countryBlacklist": ["CN", "GB"],
  "path": "/pages/index/index?foo=bar&baz=qux",
  "description": "A virtual top-up item",
  "stocks": 100,
  "autoDelivery": true,
  "maxQuantity": 5,
  "exchangeMargin": 1.5
}
```

**Request Body — tiered pricing**

```json
{
  "category": "Shopping",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "JD.com CN Gift Card" },
  "skuId": "jdcom-cn-giftcard",
  "description": "JD.com gift card redeemable in China",
  "countryWhitelist": ["CN"],
  "path": "/pages/index/index",
  "stocks": 500,
  "autoDelivery": true,
  "currency": "USD",
  "pricingMode": "tiered",
  "pricingTiers": [
    {
      "tierId": "tier_jdcn_30cny",
      "names": { "en": "JD.com CN 30 CNY" },
      "originalPrice": 5.9,
      "sellingPrice": 4.72,
      "autoDelivery": true,
      "maxQuantity": 10,
      "stocks": 200
    },
    {
      "tierId": "tier_jdcn_50cny",
      "names": { "en": "JD.com CN 50 CNY" },
      "originalPrice": 9.8,
      "sellingPrice": 7.84,
      "autoDelivery": true,
      "maxQuantity": 5,
      "stocks": 300
    }
  ]
}
```

**Request Body — custom pricing**

```json
{
  "category": "Games",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "Custom Top-up" },
  "skuId": "custom-topup",
  "description": "Top up any amount between $10 and $500",
  "countryWhitelist": ["JP"],
  "path": "/pages/topup/index",
  "currency": "USD",
  "pricingMode": "custom",
  "discountPercentage": 20,
  "minSellingPrice": 10,
  "maxSellingPrice": 500,
  "customPriceOptions": [10, 25, 50]
}
```

## <a name="currency-availability"></a>Currency availability

> ⚠️ **Read this before using the non-USD examples below.** `"USD"` is currently the **only**
> accepted `currency` value. A request specifying any other currency is rejected — the error arrives
> as `900003 Unexpected Error` with a message of the form
> `currency "<code>" is not supported; allowed: [USD]` (e.g.
> `currency "PLN" is not supported; allowed: [USD]`).
>
> The PLN, EUR and GBP examples that follow, and the non-USD behaviour described in
> [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility),
> document the **intended** multi-currency contract for forward compatibility. They will work once
> additional currencies are enabled on the platform; they fail today. Until then, omit `currency` or
> send `"USD"`.

**Request Body — flat pricing in PLN (non-USD denomination)**

When `currency` is a non-USD code, all monetary fields (`originalPrice`, `sellingPrice`,
`minSellingPrice`, `maxSellingPrice`, `customPriceOptions`, and each
[PricingTier](#pricing-tier-object)'s `originalPrice`/`sellingPrice`) are expressed in that
currency's major units. For a PLN-denominated fixed-price SKU:

```json
{
  "category": "Entertainment",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "Eneba PLN Gift Card" },
  "skuId": "eneba-pln-giftcard",
  "description": "Eneba PLN gift card, buyer picks the amount",
  "countryWhitelist": ["PL"],
  "path": "/pages/detail/index",
  "currency": "PLN",
  "pricingMode": "flat",
  "originalPrice": 200,
  "sellingPrice": 190
}
```

**Request Body — custom pricing in PLN**

A PLN-denominated custom-amount SKU. `minSellingPrice`/`maxSellingPrice`/`customPriceOptions` here
are in **PLN** (the major unit): `3` = 3.00 PLN, `200` = 200.00 PLN, presets
`[10, 20, 50, 100, 200]` = 10 / 20 / 50 / 100 / 200 PLN.

```json
{
  "category": "Entertainment",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "Eneba PLN Gift Card" },
  "skuId": "eneba-pln-giftcard-custom",
  "description": "Eneba PLN gift card, buyer enters the amount",
  "countryWhitelist": ["PL"],
  "path": "/pages/topup/index",
  "currency": "PLN",
  "pricingMode": "custom",
  "discountPercentage": 5,
  "minSellingPrice": 3,
  "maxSellingPrice": 200,
  "customPriceOptions": [10, 20, 50, 100, 200]
}
```

**Request Body — flat pricing with cross-currency exchange margin (eSIM)**

When a SKU's `currency` differs from a buyer's settlement currency, `exchangeMargin` lets you factor
in your own currency-conversion cost. Here a EUR-denominated eSIM plan applies a 2% margin:

```json
{
  "category": "eSIM",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "Europe 5GB Data eSIM" },
  "skuId": "esim-eu-5gb",
  "description": "5GB data eSIM valid for 30 days across the EU",
  "countryWhitelist": ["DE", "FR", "ES", "IT"],
  "path": "/pages/esim/index",
  "currency": "EUR",
  "originalPrice": 24.99,
  "sellingPrice": 19.99,
  "autoDelivery": true,
  "exchangeMargin": 2.0
}
```

**Request Body — manually-fulfilled physical SKU (`autoDelivery` disabled)**

Physical or otherwise manually-fulfilled goods should set `autoDelivery` to `false`. Buyers can
still complete checkout, but Lifestyle does not attempt automatic delivery — the merchant fulfills
the order out-of-band (e.g. shipping):

```json
{
  "category": "Shopping",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "Limited Edition Sneakers" },
  "skuId": "sneakers-ltd-42",
  "description": "Limited edition sneakers, size 42, shipped within 5 business days",
  "countryWhitelist": ["US", "CA"],
  "path": "/pages/shop/sneakers",
  "currency": "USD",
  "originalPrice": 189.99,
  "sellingPrice": 149.99,
  "stocks": 30,
  "autoDelivery": false,
  "maxQuantity": 3
}
```

**Request Body — single-purchase booking SKU (`maxQuantity` = 1)**

Set `maxQuantity` to `1` to hide the quantity selector entirely — useful for one-per-order items
such as travel bookings or event passes:

```json
{
  "category": "Travel",
  "coverImageFileId": "f7574adb-0ccb-4281-9ed6-943f11a1e85a",
  "names": { "en": "City Sightseeing Day Pass" },
  "skuId": "sightseeing-daypass",
  "description": "One-day hop-on hop-off sightseeing bus pass",
  "countryWhitelist": ["GB"],
  "path": "/pages/travel/daypass",
  "currency": "GBP",
  "originalPrice": 45,
  "sellingPrice": 39,
  "stocks": 500,
  "autoDelivery": false,
  "maxQuantity": 1
}
```

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {},
  "success": true
}
```

| ErrorCode | Remark                    |
| :-------- | :------------------------ |
| 000000    | Success                   |
| 900001    | Invalid Parameter         |
| 900002    | JWT Authentication Failed |
| 900003    | Unexpected Error          |
| 900004    | Invalid FileId            |
| 900260    | Invalid SkuId             |

## Pricing Tier Object

Each entry in `pricingTiers` is a `PricingTier` object with the following fields. `pricingTiers` is
only used when `pricingMode` is `"tiered"`.

| **Field**            | **Type**                  | **Required** | **Description**                                                                                                                                                                                                                                       |
| :------------------- | :------------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| tierId               | string                    | Yes          | Stable merchant-assigned identifier for this tier. Must be unique within the SKU. Max 255 characters.                                                                                                                                                 |
| names                | \{[key: string]: string\} | Yes          | Locale-keyed display name map. `en` is required.                                                                                                                                                                                                      |
| description          | string                    | No           | Optional description for this tier.                                                                                                                                                                                                                   |
| originalPrice        | number                    | Yes          | List price in `currency` major units. Must be ≥ `sellingPrice`.                                                                                                                                                                                       |
| sellingPrice         | number                    | Yes          | Actual selling price in `currency` major units. Must be > 0 and ≤ `originalPrice`.                                                                                                                                                                    |
| autoDelivery         | bool                      | No           | Whether this tier supports automatic delivery after purchase. When set, overrides the SKU-level `autoDelivery` for orders of this tier.                                                                                                               |
| maxQuantity          | int                       | No           | Maximum quantity a buyer can purchase per order for this tier (1–99). When set, overrides the SKU-level `maxQuantity` for this tier.                                                                                                                  |
| stocks               | int                       | No           | Inventory quantity for this tier. When set, overrides the SKU-level `stocks` for this tier.                                                                                                                                                           |
| originalPriceUsdCent | int                       | _Deprecated_ | ⚠️ **Deprecated.** Use `originalPrice` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). |
| sellingPriceUsdCent  | int                       | _Deprecated_ | ⚠️ **Deprecated.** Use `sellingPrice` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility).  |

**Validation rules for `pricingTiers`:**

- At least one tier is required when `pricingMode` is `"tiered"`.
- Maximum 50 tiers per SKU.
- `tierId` must be unique within the request.
- `pricingTiers` must be absent or empty when `pricingMode` is `"flat"` or `"custom"`.

## Legacy price fields & backward compatibility

> **Note.** The non-USD rules in this section are forward-looking — see
> [Currency availability](#currency-availability). Every SKU is USD-denominated today, so only the
> USD rules below are currently in effect.

The `*_usd_cent` fields (`minSellingPriceUsdCent`, `maxSellingPriceUsdCent`,
`customPriceOptionsUsdCent`, and the `originalPriceUsdCent` / `sellingPriceUsdCent` on each
[PricingTier](#pricing-tier-object)) are **deprecated**. They are kept and still accepted so
existing merchant integrations that send USD-cents amounts keep working unchanged. New integrations
should send `currency` plus the major-unit fields (`originalPrice`, `sellingPrice`,
`minSellingPrice`, `maxSellingPrice`, `customPriceOptions`) instead.

**How the request is normalized (both new and legacy fields accepted):**

1. **Precedence.** If a new major-unit field is present with a non-zero value, it wins; the legacy
   `*_usd_cent` value is ignored for that field. If the new field is absent or zero, the server
   falls back to the legacy field and converts it to the new major-unit value:
   `major = legacy_cent / 100`. This legacy conversion only happens when `currency == "USD"` — a
   legacy field cannot represent a non-USD amount, so for a non-USD SKU any `*_usd_cent` value is
   ignored (dropped) and the corresponding `*_usd_cent` column is stored as `0`.
2. **Currency default.** If `currency` is omitted, it defaults to `"USD"`. Existing merchants that
   send neither `currency` nor the new major-unit fields therefore behave exactly as before — their
   `*_usd_cent` values are interpreted as USD cents and mirrored into the new major-unit fields.
3. **Persistence.** For a USD SKU the server stores **both** representations (legacy USD-cents and
   new major-unit) and keeps them in sync, so reads via either field set return consistent values.
   For a non-USD SKU only the new major-unit fields are populated; the legacy `*_usd_cent` fields
   are stored as `0` (there is no meaningful USD-cents value without the platform exchange rate,
   which is not stored on the SKU).

**How responses backfill the legacy fields (so existing readers keep working):**

- On read (GetSKU / ListSKUs), the response always populates the new major-unit fields from the
  stored major-unit values.
- For USD SKUs the legacy `*_usd_cent` response fields are **back-filled** from the major-unit
  values when not already present: `legacy_cent = round(major × 100)`. So a USD SKU written through
  the new major-unit fields still returns correct `*_usd_cent` values to clients reading the legacy
  fields.
- For non-USD SKUs the legacy `*_usd_cent` response fields are returned as `0`/absent — clients
  reading only the legacy fields see "no price" for a non-USD SKU (graceful degradation, not
  corruption). To display a non-USD SKU correctly, read `currency` + the major-unit fields.

> **Migration recommendation.** Move integrations to `currency` + the major-unit fields at your
> earliest convenience. The `*_usd_cent` fields will be removed in a future major version.

## Valid Categories

| Category            |
| :------------------ |
| AI Tools            |
| eSIM                |
| Fashion & Beauty    |
| Food & Grocery      |
| Entertainment       |
| Games               |
| Shopping            |
| Telecom & Utilities |
| Travel              |

## Changelog

| Date       | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-07-20 | **Flat-mode discount is always derived.** In `"flat"` mode, `discountPercentage` is now always computed from `originalPrice` / `sellingPrice` (`floor((originalPrice − sellingPrice) / originalPrice × 100)`); any value supplied by the caller is ignored, matching `"tiered"` mode. `"custom"` mode is unchanged — the field is still required there and drives the `originalPrice` back-calculation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2026-07-20 | **Exchange margin.** Added the optional `exchangeMargin` field — a merchant-provided currency-exchange margin percentage (e.g. `1.5` = 1.5%) applied when converting money from `currency` to another currency at checkout/settlement. Must be finite and in `[0, 100)`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 2026-07-15 | **HTML rejection.** `names` and `description` are now rejected outright (`900001 Invalid Parameter`) if they contain HTML markup (e.g. `<b>`, `<script>`), instead of being silently escaped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 2026-07-14 | **Multi-currency pricing.** Added the `currency` field (ISO 4217, default `"USD"`, applies to **all** pricing modes — `flat`, `tiered`, `custom`) so an SKU can be denominated in a non-USD currency (e.g. `PLN`). Added currency-aware major-unit price fields: `originalPrice` / `sellingPrice` (now explicitly described as `currency` major units), `minSellingPrice`, `maxSellingPrice`, `customPriceOptions`, and per-tier `originalPrice` / `sellingPrice` on the [PricingTier](#pricing-tier-object) object. **Deprecated** the legacy USD-cents fields (`minSellingPriceUsdCent`, `maxSellingPriceUsdCent`, `customPriceOptionsUsdCent`, per-tier `originalPriceUsdCent` / `sellingPriceUsdCent`) — they remain accepted for backward compatibility (USD only; ignored when a major-unit field is also sent). Added a PLN flat-pricing and a PLN custom-pricing request example. See [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility) for the full request-normalization and response-backfill contract. |