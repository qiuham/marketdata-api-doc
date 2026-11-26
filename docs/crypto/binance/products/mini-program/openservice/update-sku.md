---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/update-sku
api_type: Guide
updated_at: 2026-11-26 18:38:04.460607
---

# UpdateSKU

# <a name="UpdateSKU"></a>UpdateSKU

Updates one or more fields of an existing SKU. Only `names`, `coverImageFileId`, and `description`
require audit approval before taking effect. All other fields take effect immediately without audit.
Note: `sellingPrice` and `originalPrice` are ignored for `pricingMode = "tiered"` — the effective
values are always auto-calculated from `pricingTiers`.

**Host**: **dip-cb.binanceapi.com**

**PATCH** /mp-api/v1/apps/\{appId\}/skus/\{skuId\}

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**               |
| :------------ | :---------------------------- |
| appId         | The AppId of the mini program |
| skuId         | The skuId of the SKU          |

**Body Parameters**

| **Parameter**             | **Type**                                                          | **Required**                              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Example**                          |
| :------------------------ | :---------------------------------------------------------------- | :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------- |
| category                  | string                                                            | No                                        | Category of this SKU.<br/>See [Valid Categories](#valid-categories) for accepted values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | "Games"                              |
| coverImageFileId          | string                                                            | No                                        | Cover image for this SKU.<br/>Must be a file ID returned by [UploadFile](./upload-file). The file must have passed safety checks before use.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | f7574adb-0ccb-4281-9ed6-943f11a1e85a |
| names                     | \{[key: string]: string\}                                         | No                                        | Locale-keyed display name map for this SKU.<br/>**Rules:** `en` key is required. Maximum 128 characters per value. Values must not contain HTML markup (e.g. `<b>`, `<script>`) — such requests are rejected with `900001 Invalid Parameter`.<br/>Replaces the entire existing map when provided.                                                                                                                                                                                                                                                                                                 | {"en": "pubg 100 point"}             |
| originalPrice             | number                                                            | Required when `pricingMode` is `"flat"`   | List price in `currency` major units (e.g. `9.99` means 9.99 of `currency`; USD when `currency` is omitted).<br/>**`"flat"` mode:** Required. Must be > 0. Must be ≥ `sellingPrice`. Sub-cent amounts are truncated (e.g., 9.9999 → 9.99).<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the maximum `originalPrice` across all tiers.<br/>**`"custom"` mode:** Optional. Saved as-is if provided.                                                                                                                                                        | 9.99                                 |
| sellingPrice              | number                                                            | Required when `pricingMode` is `"flat"`   | Actual selling price in `currency` major units.<br/>**`"flat"` mode:** Required. Must be > 0. Must be ≤ `originalPrice`. Sub-cent amounts are truncated (e.g., 9.9999 → 9.99).<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the minimum `sellingPrice` across all tiers.<br/>**`"custom"` mode:** Optional. Saved as-is if provided.                                                                                                                                                                                                                     | 6                                    |
| discountPercentage        | int                                                               | Required when `pricingMode` is `"custom"` | Discount percentage shown to buyers.<br/>**Values:** 1–99.<br/>**`"custom"` mode:** Required. Used to back-calculate `originalPrice` from `minSellingPrice` (formula: `original = min / (1 − discount/100)`).<br/>**`"flat"` mode:** Ignored if provided — always auto-calculated from the price difference (`floor((originalPrice − sellingPrice) / originalPrice × 100)`) and shown as the price reduction badge.<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the maximum effective discount across all tiers.                                        | 32                                   |
| countryWhitelist          | Array\<String\>                                                   | No                                        | Countries where this SKU is eligible to be displayed.<br/>**Values:** [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) country codes.<br/>If empty, SKU can be displayed in all countries. Replaces the entire existing list when provided.                                                                                                                                                                                                                                                                                               | ["JP"]                               |
| countryBlacklist          | Array\<String\>                                                   | No                                        | Countries where this SKU must not be displayed.<br/>**Values:** [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) country codes.<br/>Replaces the entire existing list when provided.                                                                                                                                                                                                                                                                                                                                                      | ["CN", "GB"]                         |
| path                      | string                                                            | No                                        | Mini-program page path to open when the SKU is tapped.<br/>**Rules:** Must start with `/`. Maximum 1024 characters. Query parameters (after `?`) are parsed and stored separately.                                                                                                                                                                                                                                                                                                                                                                                                                | /hello/world?foo=bar                 |
| description               | string                                                            | Yes                                       | Description for this SKU.<br/>**Rules:** Must not contain HTML markup (e.g. `<b>`, `<script>`) — such requests are rejected with `900001 Invalid Parameter`.                                                                                                                                                                                                                                                                                                                                                                                                                                      | A virtual top-up item                |
| stocks                    | int                                                               | No                                        | Merchant-provided inventory quantity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 100                                  |
| autoDelivery              | bool                                                              | No                                        | Whether the SKU supports automatic delivery after purchase. Only SKUs with auto delivery enabled can complete the full purchase flow within Lifestyle; SKUs without it require the merchant to fulfill delivery out-of-band.                                                                                                                                                                                                                                                                                                                                                                      | true                                 |
| maxQuantity               | int                                                               | No                                        | Maximum quantity a buyer can purchase in a single order.<br/>**Values:** 1–99. Absent means no change to the current value.<br/>Set to `1` to hide the quantity input widget on the UI. Applies to all pricing modes.                                                                                                                                                                                                                                                                                                                                                                             | 5                                    |
| pricingMode               | string                                                            | No                                        | Determines how the SKU is priced. Absent means no change to the current mode.<br/>**Values:**<br/>- `"flat"` — single fixed price defined by `sellingPrice` / `originalPrice`.<br/>- `"tiered"` — multiple fixed denominations defined by `pricingTiers`.<br/>- `"custom"` — buyer enters any amount within the range defined by `minSellingPrice` / `maxSellingPrice`.                                                                                                                                                                                                                           | "tiered"                             |
| currency                  | string                                                            | No                                        | ISO 4217 currency code that all monetary amounts on this SKU are denominated in (applies to **all** pricing modes: `flat`, `tiered`, and `custom`). Absent means no change to the current currency.<br/>⚠️ **`"USD"` is currently the only accepted value** — any other currency is rejected. See [Currency availability](./create-sku-in-audit#currency-availability). Changing `currency` does **not** trigger audit — it takes effect immediately, like the other pricing fields.<br/>When omitted or `"USD"`, the legacy `*_usd_cent` fields continue to behave exactly as today (USD cents). | "USD"                                |
| pricingTiers              | Array\<[PricingTier](./create-sku-in-audit#pricing-tier-object)\> | No                                        | List of fixed denomination options for this SKU.<br/>**Rules:** 1–50 tiers. Each tier must have a unique `tierId`. Replaces all existing tiers when provided.<br/>**`"tiered"` mode:** Must be non-empty.<br/>**`"flat"` / `"custom"` mode:** Must be absent or empty.<br/>See [PricingTier Object](./create-sku-in-audit#pricing-tier-object) in CreateSKUInAudit. Each tier's prices are in `currency` major units (use `originalPrice` / `sellingPrice` on the tier object).                                                                                                                   | see CreateSKUInAudit                 |
| minSellingPrice           | number                                                            | No                                        | Minimum amount the buyer may enter, in `currency` major units.<br/>**Rules:** Must be > 0. Must be < `maxSellingPrice`.<br/>Required when changing `pricingMode` to `"custom"`. Only applies when `pricingMode` is `"custom"`.                                                                                                                                                                                                                                                                                                                                                                    | 3.00                                 |
| maxSellingPrice           | number                                                            | No                                        | Maximum amount the buyer may enter, in `currency` major units.<br/>**Rules:** Must be > `minSellingPrice`.<br/>Required when changing `pricingMode` to `"custom"`. Only applies when `pricingMode` is `"custom"`.                                                                                                                                                                                                                                                                                                                                                                                 | 200                                  |
| customPriceOptions        | Array\<number\>                                                   | No                                        | Preset quick-select amounts shown to the buyer, each in `currency` major units.<br/>**Rules:** Maximum 5 entries. Each value must be > 0 and within [`minSellingPrice`, `maxSellingPrice`].<br/>Only applies when `pricingMode` is `"custom"`. Replaces existing presets when provided; absent means no change.                                                                                                                                                                                                                                                                                   | [10, 20, 50, 100, 200]               |
| minSellingPriceUsdCent    | int                                                               | _Deprecated_                              | ⚠️ **Deprecated.** Use `minSellingPrice` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](./create-sku-in-audit#legacy-price-fields--backward-compatibility) in CreateSKUInAudit. When `minSellingPrice` is provided with a non-zero value, it takes precedence and this field is ignored.                                                                                                                                                                                         | 1000                                 |
| maxSellingPriceUsdCent    | int                                                               | _Deprecated_                              | ⚠️ **Deprecated.** Use `maxSellingPrice` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility. When `maxSellingPrice` is provided with a non-zero value, it takes precedence and this field is ignored.                                                                                                                                                                                                                                                                                                                                     | 50000                                |
| customPriceOptionsUsdCent | Array\<int\>                                                      | _Deprecated_                              | ⚠️ **Deprecated.** Use `customPriceOptions` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility. When `customPriceOptions` is provided and non-empty, it takes precedence and this field is ignored.                                                                                                                                                                                                                                                                                                                                       | [1000, 2500, 5000]                   |
| exchangeMargin            | number                                                            | No                                        | Optional currency-exchange margin percentage applied when converting money from `currency` (this SKU's currency) to another currency at checkout/settlement (e.g. `1.5` means a 1.5% margin). Absent means no change to the current value.<br/>**Rules:** Must be finite and in `[0, 100)`.<br/>⚠️ Once set, it cannot currently be cleared back to unset via this endpoint — omitting the field always retains the previous value, it never resets it.                                                                                                                                           | 1.5                                  |

Note:

1. The following fields require audit approval before taking effect: `names`, `coverImageFileId`,
   and `description`. All other fields — including `category`, `path`, `countryWhitelist`,
   `countryBlacklist`, `sellingPrice`, `originalPrice`, `discountPercentage`, `currency`,
   `pricingMode`, `pricingTiers`, `minSellingPrice`, `maxSellingPrice`, `customPriceOptions`,
   `minSellingPriceUsdCent` (_deprecated_), `maxSellingPriceUsdCent` (_deprecated_),
   `customPriceOptionsUsdCent` (_deprecated_), `stocks`, `autoDelivery`, `maxQuantity`, and
   `exchangeMargin` — take effect immediately without audit. When `pricingMode` is `"tiered"`,
   sending `sellingPrice` or `originalPrice` has no effect — those values are always derived from
   `pricingTiers` by the server.
2. Updating each field will overwrite its entire original value.

**Request Body**

```json
{
  "names": {
    "en": "PUBG 100 points",
    "zh-TW": "PUBG 100 點"
  },
  "countryWhitelist": ["JP"],
  "countryBlacklist": ["CN", "TW"]
}
```

**Response**

**HTTP 200 in JSON**

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

## Legacy price fields & backward compatibility

The `*_usd_cent` fields (`minSellingPriceUsdCent`, `maxSellingPriceUsdCent`,
`customPriceOptionsUsdCent`, and the per-tier `originalPriceUsdCent` / `sellingPriceUsdCent`) are
**deprecated**. They remain accepted on update so existing merchant integrations keep working. New
integrations should send `currency` plus the major-unit fields (`originalPrice`, `sellingPrice`,
`minSellingPrice`, `maxSellingPrice`, `customPriceOptions`). See
[CreateSKUInAudit — Legacy price fields & backward compatibility](./create-sku-in-audit#legacy-price-fields--backward-compatibility)
for the full normalize/backfill contract; the update-specific notes are:

1. **Precedence.** On update, if a new major-unit field is present with a non-zero value it wins;
   the legacy `*_usd_cent` value is ignored for that field. If the new field is absent or zero, the
   server falls back to the legacy field and converts it (`major = legacy_cent / 100`). This legacy
   conversion only happens when `currency == "USD"` — for a non-USD SKU any `*_usd_cent` value is
   ignored (dropped) and the corresponding `*_usd_cent` column is stored as `0`.
2. **Absent = no change.** As with all update fields, an omitted price field means "no change to the
   current value." This applies to both the legacy and the new fields.
3. **Currency change.** Changing `currency` does **not** trigger audit and takes effect immediately.
   It is a label change on the stored major-unit amounts, not an exchange-rate conversion: changing
   a `10.00` USD SKU to `PLN` makes it a `10.00` PLN SKU unless you also send replacement price
   values. If you change `currency` you should also send the major-unit price fields in the new
   currency. When `currency` is changed to a non-USD value, the legacy `*_usd_cent` fields are reset
   to `0`/absent because the backend does not store an exchange rate to derive USD cents.
4. **Response backfill.** On read (GetSKU / ListSKUs), USD SKUs have their legacy `*_usd_cent`
   fields back-filled from the major-unit values (`legacy_cent = round(major × 100)`); non-USD SKUs
   return `0`/absent for the legacy fields — read `currency` + the major-unit fields instead.

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

| Date       | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-07-20 | **Flat-mode discount is always derived.** In `"flat"` mode, `discountPercentage` is now always computed from `originalPrice` / `sellingPrice` (`floor((originalPrice − sellingPrice) / originalPrice × 100)`); any value supplied by the caller is ignored, matching `"tiered"` mode. `"custom"` mode is unchanged.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2026-07-20 | **Exchange margin.** Added the optional `exchangeMargin` field — a merchant-provided currency-exchange margin percentage (e.g. `1.5` = 1.5%) applied when converting money from `currency` to another currency at checkout/settlement. Absent means no change; nil cannot currently clear a previously-set value. Takes effect immediately without audit. Must be finite and in `[0, 100)`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 2026-07-15 | **HTML rejection.** `names` and `description` are now rejected outright (`900001 Invalid Parameter`) if they contain HTML markup (e.g. `<b>`, `<script>`), instead of being silently escaped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2026-07-14 | **Multi-currency pricing.** Added the `currency` field (ISO 4217; absent = no change to the current currency; takes effect immediately, does **not** trigger audit). Added currency-aware major-unit price fields (`minSellingPrice`, `maxSellingPrice`, `customPriceOptions`; `originalPrice` / `sellingPrice` now explicitly described as `currency` major units; per-tier `originalPrice` / `sellingPrice` per the [PricingTier](./create-sku-in-audit#pricing-tier-object) object). **Deprecated** the legacy USD-cents fields (`minSellingPriceUsdCent`, `maxSellingPriceUsdCent`, `customPriceOptionsUsdCent`) — still accepted (USD only; ignored when a major-unit field is also sent). See [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility) for the update-specific normalize/backfill contract and the CreateSKUInAudit page for the full contract. |

---

# UpdateSKU

# <a name="UpdateSKU"></a>UpdateSKU

Updates one or more fields of an existing SKU. Only `names`, `coverImageFileId`, and `description`
require audit approval before taking effect. All other fields take effect immediately without audit.
Note: `sellingPrice` and `originalPrice` are ignored for `pricingMode = "tiered"` — the effective
values are always auto-calculated from `pricingTiers`.

**Host**: **dip-cb.binanceapi.com**

**PATCH** /mp-api/v1/apps/\{appId\}/skus/\{skuId\}

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**               |
| :------------ | :---------------------------- |
| appId         | The AppId of the mini program |
| skuId         | The skuId of the SKU          |

**Body Parameters**

| **Parameter**             | **Type**                                                          | **Required**                              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Example**                          |
| :------------------------ | :---------------------------------------------------------------- | :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------- |
| category                  | string                                                            | No                                        | Category of this SKU.<br/>See [Valid Categories](#valid-categories) for accepted values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | "Games"                              |
| coverImageFileId          | string                                                            | No                                        | Cover image for this SKU.<br/>Must be a file ID returned by [UploadFile](./upload-file). The file must have passed safety checks before use.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | f7574adb-0ccb-4281-9ed6-943f11a1e85a |
| names                     | \{[key: string]: string\}                                         | No                                        | Locale-keyed display name map for this SKU.<br/>**Rules:** `en` key is required. Maximum 128 characters per value. Values must not contain HTML markup (e.g. `<b>`, `<script>`) — such requests are rejected with `900001 Invalid Parameter`.<br/>Replaces the entire existing map when provided.                                                                                                                                                                                                                                                                                                 | {"en": "pubg 100 point"}             |
| originalPrice             | number                                                            | Required when `pricingMode` is `"flat"`   | List price in `currency` major units (e.g. `9.99` means 9.99 of `currency`; USD when `currency` is omitted).<br/>**`"flat"` mode:** Required. Must be > 0. Must be ≥ `sellingPrice`. Sub-cent amounts are truncated (e.g., 9.9999 → 9.99).<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the maximum `originalPrice` across all tiers.<br/>**`"custom"` mode:** Optional. Saved as-is if provided.                                                                                                                                                        | 9.99                                 |
| sellingPrice              | number                                                            | Required when `pricingMode` is `"flat"`   | Actual selling price in `currency` major units.<br/>**`"flat"` mode:** Required. Must be > 0. Must be ≤ `originalPrice`. Sub-cent amounts are truncated (e.g., 9.9999 → 9.99).<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the minimum `sellingPrice` across all tiers.<br/>**`"custom"` mode:** Optional. Saved as-is if provided.                                                                                                                                                                                                                     | 6                                    |
| discountPercentage        | int                                                               | Required when `pricingMode` is `"custom"` | Discount percentage shown to buyers.<br/>**Values:** 1–99.<br/>**`"custom"` mode:** Required. Used to back-calculate `originalPrice` from `minSellingPrice` (formula: `original = min / (1 − discount/100)`).<br/>**`"flat"` mode:** Ignored if provided — always auto-calculated from the price difference (`floor((originalPrice − sellingPrice) / originalPrice × 100)`) and shown as the price reduction badge.<br/>**`"tiered"` mode:** Ignored if provided — auto-calculated from `pricingTiers` as the maximum effective discount across all tiers.                                        | 32                                   |
| countryWhitelist          | Array\<String\>                                                   | No                                        | Countries where this SKU is eligible to be displayed.<br/>**Values:** [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) country codes.<br/>If empty, SKU can be displayed in all countries. Replaces the entire existing list when provided.                                                                                                                                                                                                                                                                                               | ["JP"]                               |
| countryBlacklist          | Array\<String\>                                                   | No                                        | Countries where this SKU must not be displayed.<br/>**Values:** [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) country codes.<br/>Replaces the entire existing list when provided.                                                                                                                                                                                                                                                                                                                                                      | ["CN", "GB"]                         |
| path                      | string                                                            | No                                        | Mini-program page path to open when the SKU is tapped.<br/>**Rules:** Must start with `/`. Maximum 1024 characters. Query parameters (after `?`) are parsed and stored separately.                                                                                                                                                                                                                                                                                                                                                                                                                | /hello/world?foo=bar                 |
| description               | string                                                            | Yes                                       | Description for this SKU.<br/>**Rules:** Must not contain HTML markup (e.g. `<b>`, `<script>`) — such requests are rejected with `900001 Invalid Parameter`.                                                                                                                                                                                                                                                                                                                                                                                                                                      | A virtual top-up item                |
| stocks                    | int                                                               | No                                        | Merchant-provided inventory quantity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 100                                  |
| autoDelivery              | bool                                                              | No                                        | Whether the SKU supports automatic delivery after purchase. Only SKUs with auto delivery enabled can complete the full purchase flow within Lifestyle; SKUs without it require the merchant to fulfill delivery out-of-band.                                                                                                                                                                                                                                                                                                                                                                      | true                                 |
| maxQuantity               | int                                                               | No                                        | Maximum quantity a buyer can purchase in a single order.<br/>**Values:** 1–99. Absent means no change to the current value.<br/>Set to `1` to hide the quantity input widget on the UI. Applies to all pricing modes.                                                                                                                                                                                                                                                                                                                                                                             | 5                                    |
| pricingMode               | string                                                            | No                                        | Determines how the SKU is priced. Absent means no change to the current mode.<br/>**Values:**<br/>- `"flat"` — single fixed price defined by `sellingPrice` / `originalPrice`.<br/>- `"tiered"` — multiple fixed denominations defined by `pricingTiers`.<br/>- `"custom"` — buyer enters any amount within the range defined by `minSellingPrice` / `maxSellingPrice`.                                                                                                                                                                                                                           | "tiered"                             |
| currency                  | string                                                            | No                                        | ISO 4217 currency code that all monetary amounts on this SKU are denominated in (applies to **all** pricing modes: `flat`, `tiered`, and `custom`). Absent means no change to the current currency.<br/>⚠️ **`"USD"` is currently the only accepted value** — any other currency is rejected. See [Currency availability](./create-sku-in-audit#currency-availability). Changing `currency` does **not** trigger audit — it takes effect immediately, like the other pricing fields.<br/>When omitted or `"USD"`, the legacy `*_usd_cent` fields continue to behave exactly as today (USD cents). | "USD"                                |
| pricingTiers              | Array\<[PricingTier](./create-sku-in-audit#pricing-tier-object)\> | No                                        | List of fixed denomination options for this SKU.<br/>**Rules:** 1–50 tiers. Each tier must have a unique `tierId`. Replaces all existing tiers when provided.<br/>**`"tiered"` mode:** Must be non-empty.<br/>**`"flat"` / `"custom"` mode:** Must be absent or empty.<br/>See [PricingTier Object](./create-sku-in-audit#pricing-tier-object) in CreateSKUInAudit. Each tier's prices are in `currency` major units (use `originalPrice` / `sellingPrice` on the tier object).                                                                                                                   | see CreateSKUInAudit                 |
| minSellingPrice           | number                                                            | No                                        | Minimum amount the buyer may enter, in `currency` major units.<br/>**Rules:** Must be > 0. Must be < `maxSellingPrice`.<br/>Required when changing `pricingMode` to `"custom"`. Only applies when `pricingMode` is `"custom"`.                                                                                                                                                                                                                                                                                                                                                                    | 3.00                                 |
| maxSellingPrice           | number                                                            | No                                        | Maximum amount the buyer may enter, in `currency` major units.<br/>**Rules:** Must be > `minSellingPrice`.<br/>Required when changing `pricingMode` to `"custom"`. Only applies when `pricingMode` is `"custom"`.                                                                                                                                                                                                                                                                                                                                                                                 | 200                                  |
| customPriceOptions        | Array\<number\>                                                   | No                                        | Preset quick-select amounts shown to the buyer, each in `currency` major units.<br/>**Rules:** Maximum 5 entries. Each value must be > 0 and within [`minSellingPrice`, `maxSellingPrice`].<br/>Only applies when `pricingMode` is `"custom"`. Replaces existing presets when provided; absent means no change.                                                                                                                                                                                                                                                                                   | [10, 20, 50, 100, 200]               |
| minSellingPriceUsdCent    | int                                                               | _Deprecated_                              | ⚠️ **Deprecated.** Use `minSellingPrice` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility — see [Legacy price fields & backward compatibility](./create-sku-in-audit#legacy-price-fields--backward-compatibility) in CreateSKUInAudit. When `minSellingPrice` is provided with a non-zero value, it takes precedence and this field is ignored.                                                                                                                                                                                         | 1000                                 |
| maxSellingPriceUsdCent    | int                                                               | _Deprecated_                              | ⚠️ **Deprecated.** Use `maxSellingPrice` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility. When `maxSellingPrice` is provided with a non-zero value, it takes precedence and this field is ignored.                                                                                                                                                                                                                                                                                                                                     | 50000                                |
| customPriceOptionsUsdCent | Array\<int\>                                                      | _Deprecated_                              | ⚠️ **Deprecated.** Use `customPriceOptions` instead. Legacy USD-cents field; only meaningful when `currency == "USD"`. Kept for backward compatibility. When `customPriceOptions` is provided and non-empty, it takes precedence and this field is ignored.                                                                                                                                                                                                                                                                                                                                       | [1000, 2500, 5000]                   |
| exchangeMargin            | number                                                            | No                                        | Optional currency-exchange margin percentage applied when converting money from `currency` (this SKU's currency) to another currency at checkout/settlement (e.g. `1.5` means a 1.5% margin). Absent means no change to the current value.<br/>**Rules:** Must be finite and in `[0, 100)`.<br/>⚠️ Once set, it cannot currently be cleared back to unset via this endpoint — omitting the field always retains the previous value, it never resets it.                                                                                                                                           | 1.5                                  |

Note:

1. The following fields require audit approval before taking effect: `names`, `coverImageFileId`,
   and `description`. All other fields — including `category`, `path`, `countryWhitelist`,
   `countryBlacklist`, `sellingPrice`, `originalPrice`, `discountPercentage`, `currency`,
   `pricingMode`, `pricingTiers`, `minSellingPrice`, `maxSellingPrice`, `customPriceOptions`,
   `minSellingPriceUsdCent` (_deprecated_), `maxSellingPriceUsdCent` (_deprecated_),
   `customPriceOptionsUsdCent` (_deprecated_), `stocks`, `autoDelivery`, `maxQuantity`, and
   `exchangeMargin` — take effect immediately without audit. When `pricingMode` is `"tiered"`,
   sending `sellingPrice` or `originalPrice` has no effect — those values are always derived from
   `pricingTiers` by the server.
2. Updating each field will overwrite its entire original value.

**Request Body**

```json
{
  "names": {
    "en": "PUBG 100 points",
    "zh-TW": "PUBG 100 點"
  },
  "countryWhitelist": ["JP"],
  "countryBlacklist": ["CN", "TW"]
}
```

**Response**

**HTTP 200 in JSON**

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

## Legacy price fields & backward compatibility

The `*_usd_cent` fields (`minSellingPriceUsdCent`, `maxSellingPriceUsdCent`,
`customPriceOptionsUsdCent`, and the per-tier `originalPriceUsdCent` / `sellingPriceUsdCent`) are
**deprecated**. They remain accepted on update so existing merchant integrations keep working. New
integrations should send `currency` plus the major-unit fields (`originalPrice`, `sellingPrice`,
`minSellingPrice`, `maxSellingPrice`, `customPriceOptions`). See
[CreateSKUInAudit — Legacy price fields & backward compatibility](./create-sku-in-audit#legacy-price-fields--backward-compatibility)
for the full normalize/backfill contract; the update-specific notes are:

1. **Precedence.** On update, if a new major-unit field is present with a non-zero value it wins;
   the legacy `*_usd_cent` value is ignored for that field. If the new field is absent or zero, the
   server falls back to the legacy field and converts it (`major = legacy_cent / 100`). This legacy
   conversion only happens when `currency == "USD"` — for a non-USD SKU any `*_usd_cent` value is
   ignored (dropped) and the corresponding `*_usd_cent` column is stored as `0`.
2. **Absent = no change.** As with all update fields, an omitted price field means "no change to the
   current value." This applies to both the legacy and the new fields.
3. **Currency change.** Changing `currency` does **not** trigger audit and takes effect immediately.
   It is a label change on the stored major-unit amounts, not an exchange-rate conversion: changing
   a `10.00` USD SKU to `PLN` makes it a `10.00` PLN SKU unless you also send replacement price
   values. If you change `currency` you should also send the major-unit price fields in the new
   currency. When `currency` is changed to a non-USD value, the legacy `*_usd_cent` fields are reset
   to `0`/absent because the backend does not store an exchange rate to derive USD cents.
4. **Response backfill.** On read (GetSKU / ListSKUs), USD SKUs have their legacy `*_usd_cent`
   fields back-filled from the major-unit values (`legacy_cent = round(major × 100)`); non-USD SKUs
   return `0`/absent for the legacy fields — read `currency` + the major-unit fields instead.

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

| Date       | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-07-20 | **Flat-mode discount is always derived.** In `"flat"` mode, `discountPercentage` is now always computed from `originalPrice` / `sellingPrice` (`floor((originalPrice − sellingPrice) / originalPrice × 100)`); any value supplied by the caller is ignored, matching `"tiered"` mode. `"custom"` mode is unchanged.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2026-07-20 | **Exchange margin.** Added the optional `exchangeMargin` field — a merchant-provided currency-exchange margin percentage (e.g. `1.5` = 1.5%) applied when converting money from `currency` to another currency at checkout/settlement. Absent means no change; nil cannot currently clear a previously-set value. Takes effect immediately without audit. Must be finite and in `[0, 100)`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 2026-07-15 | **HTML rejection.** `names` and `description` are now rejected outright (`900001 Invalid Parameter`) if they contain HTML markup (e.g. `<b>`, `<script>`), instead of being silently escaped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 2026-07-14 | **Multi-currency pricing.** Added the `currency` field (ISO 4217; absent = no change to the current currency; takes effect immediately, does **not** trigger audit). Added currency-aware major-unit price fields (`minSellingPrice`, `maxSellingPrice`, `customPriceOptions`; `originalPrice` / `sellingPrice` now explicitly described as `currency` major units; per-tier `originalPrice` / `sellingPrice` per the [PricingTier](./create-sku-in-audit#pricing-tier-object) object). **Deprecated** the legacy USD-cents fields (`minSellingPriceUsdCent`, `maxSellingPriceUsdCent`, `customPriceOptionsUsdCent`) — still accepted (USD only; ignored when a major-unit field is also sent). See [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility) for the update-specific normalize/backfill contract and the CreateSKUInAudit page for the full contract. |