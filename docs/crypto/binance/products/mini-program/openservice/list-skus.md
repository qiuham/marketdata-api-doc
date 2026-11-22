---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/list-skus
api_type: Guide
updated_at: 2026-11-22 18:35:34.934131
---

# ListSKUs

# <a name="_58jpgh2b0pya"></a>ListSKUs

**Host**: **dip-cb.binanceapi.com**

**GET** /mp-api/v1/apps/\{appId\}/skus?page=1&limit=20&auditStatus=

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**           |
| :------------ | :------------------------ |
| appId         | AppId of the mini program |

**Query Parameters**

| **Parameter** | **Required** | **Description**                                                    |
| :------------ | :----------- | :----------------------------------------------------------------- |
| page          | No           | Designated query page. Defaults to 1.                              |
| limit         | No           | Quantity limit per page. The maximum size is 50. Defaults to 50.   |
| auditStatus   | No           | SKU audit status filter. Can be 'TODO', 'APPROVED', or 'REJECTED'. |

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "skus": [
      {
        "id": "bn_point_100",
        "audit": {
          "info": {
            "id": "bn_point_100",
            "defaultName": "BN 100 points",
            "names": {
              "en": "BN 100 points",
              "zh-TW": "BN 100 點"
            },
            "category": "Games",
            "imageUrl": "https://bn.com/hnCWgai85XJwn7qSRXjiUt.png",
            "imageStatus": "UPLOADING",
            "originalPrice": "9.99",
            "sellingPrice": "6.99",
            "discountPercentage": 30,
            "path": "/pages/index/index?foo=bar&baz=qux",
            "description": "A virtual top-up item",
            "stocks": 100,
            "autoDelivery": true,
            "maxQuantity": 5,
            "countryWhitelist": ["TW", "JP"],
            "countryBlacklist": ["SG"],
            "currency": "USD",
            "pricingMode": "flat",
            "pricingTiers": []
          },
          "auditStatus": "APPROVED"
        },
        "online": {
          "info": {
            "id": "bn_point_100",
            "defaultName": "BN 100 points",
            "names": {
              "en": "BN 100 points",
              "zh-TW": "BN 100 點"
            },
            "category": "Games",
            "imageUrl": "https://bn.com/hnCWgai85XJwn7qSRXjiUt.png",
            "imageStatus": "UPLOADING",
            "originalPrice": "19.99",
            "sellingPrice": "17.99",
            "discountPercentage": 10,
            "path": "/pages/index/index?foo=bar&baz=qux",
            "description": "A virtual top-up item",
            "stocks": 100,
            "autoDelivery": true,
            "maxQuantity": 5,
            "countryWhitelist": ["TW", "JP", "ID"],
            "countryBlacklist": ["SG"],
            "currency": "USD",
            "pricingMode": "flat",
            "pricingTiers": []
          },
          "availableStatus": "ACTIVE"
        }
      }
    ]
  },
  "success": true
}
```

**Response Parameters**

| **Parameter**             | **Description**                                                                                                                                                                                                                                                                                           |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| skus                      | Array of SKU information                                                                                                                                                                                                                                                                                  |
| audit                     | Audit information for the SKU                                                                                                                                                                                                                                                                             |
| online                    | Online information for the SKU                                                                                                                                                                                                                                                                            |
| imageStatus               | Status of the SKU image, could be 'UPLOADING', 'SUCCESS', 'FAILED', or 'NONEXISTED'                                                                                                                                                                                                                       |
| auditStatus               | Audit status of the SKU, could be 'TODO', 'APPROVED', or 'REJECTED'                                                                                                                                                                                                                                       |
| availableStatus           | Availability status of the SKU, controlled by merchant. Can be 'ACTIVE' or 'DEACTIVE'                                                                                                                                                                                                                     |
| metadata                  | Pagination information. 'itemCount' is the total count for the current response, 'itemsPerPage' is the total count per page as per the given request                                                                                                                                                      |
| description               | Merchant-provided description for this SKU                                                                                                                                                                                                                                                                |
| stocks                    | Merchant-provided inventory quantity. Absent if not set.                                                                                                                                                                                                                                                  |
| autoDelivery              | Whether the SKU supports automatic delivery after purchase. Only SKUs with auto delivery enabled can complete the full purchase flow within Lifestyle; SKUs without it require the merchant to fulfill delivery out-of-band. Absent if not set.                                                           |
| maxQuantity               | Maximum quantity a buyer can purchase per order (1–99). Defaults to `99` when not explicitly set. When `1`, the UI hides the quantity input widget.                                                                                                                                                       |
| currency                  | ISO 4217 currency code that all monetary amounts on this SKU are denominated in (applies to **all** pricing modes). Defaults to `"USD"` when not set. Currently always `"USD"` — see [Currency availability](./create-sku-in-audit#currency-availability).                                                |
| originalPrice             | List price as a string, in `currency` major units (e.g. `"9.99"`). For `"tiered"` mode, the maximum `originalPrice` across all tiers.                                                                                                                                                                     |
| sellingPrice              | Actual selling price as a string, in `currency` major units. For `"tiered"` mode, the minimum `sellingPrice` across all tiers. For `"custom"` mode, equals `minSellingPrice`.                                                                                                                             |
| pricingMode               | Pricing mode: `"flat"` for a single price, `"tiered"` for multiple fixed denomination options, `"custom"` for user-entered amount within a range                                                                                                                                                          |
| pricingTiers              | Array of [PricingTier](./create-sku-in-audit#pricing-tier-object) objects. Present when `pricingMode` is `"tiered"`, empty array otherwise. Each tier carries `originalPrice`/`sellingPrice` in `currency` major units, and may include `autoDelivery`, `maxQuantity`, and `stocks` overrides.            |
| minSellingPrice           | Minimum amount the user may enter, in `currency` major units. Present when `pricingMode` is `"custom"`.                                                                                                                                                                                                   |
| maxSellingPrice           | Maximum amount the user may enter, in `currency` major units. Present when `pricingMode` is `"custom"`.                                                                                                                                                                                                   |
| customPriceOptions        | Preset amounts for buyer quick-select, each in `currency` major units. Present when `pricingMode` is `"custom"` and presets were configured; absent otherwise.                                                                                                                                            |
| minSellingPriceUsdCent    | ⚠️ **Deprecated.** Legacy minimum in **USD cents** (only meaningful when `currency == "USD"`). Back-filled from `minSellingPrice` (`round(major × 100)`) for USD SKUs; `0` for non-USD SKUs. Prefer `minSellingPrice`.                                                                                    |
| maxSellingPriceUsdCent    | ⚠️ **Deprecated.** Legacy maximum in USD cents. Back-filled from `maxSellingPrice` for USD SKUs; `0` for non-USD SKUs. Prefer `maxSellingPrice`.                                                                                                                                                          |
| customPriceOptionsUsdCent | ⚠️ **Deprecated.** Legacy presets in USD cents. Back-filled from `customPriceOptions` for USD SKUs; absent for non-USD SKUs. Prefer `customPriceOptions`.                                                                                                                                                 |
| discountPercentage        | Discount percentage displayed to buyers. For `"flat"` mode, always computed from `(originalPrice − sellingPrice) / originalPrice × 100` (any merchant-provided value is ignored). For `"custom"` mode, the merchant-provided value. For `"tiered"` mode, derived from the tier with the highest discount. |
| exchangeMargin            | Currency-exchange margin percentage applied when converting money from `currency` to another currency at checkout/settlement (e.g. `1.5` means a 1.5% margin). Absent (or `0`) when not configured on the SKU.                                                                                            |

> **Legacy price fields & backward compatibility.** The `*_usd_cent` response fields are
> **deprecated**: they are back-filled from the new major-unit fields for USD SKUs (so existing
> clients reading them still work) and are `0`/absent for non-USD SKUs (no USD-cents value exists
> without the platform exchange rate, which is not stored on the SKU). To render any SKU correctly —
> including non-USD — read `currency` +
> `originalPrice`/`sellingPrice`/`minSellingPrice`/`maxSellingPrice`/`customPriceOptions`. See
> [CreateSKUInAudit — Legacy price fields & backward compatibility](./create-sku-in-audit#legacy-price-fields--backward-compatibility)
> for the full contract.

## Changelog

| Date       | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-07-20 | **Exchange margin.** The response now returns an `exchangeMargin` field — the merchant-provided currency-exchange margin percentage (e.g. `1.5` = 1.5%) applied when converting money from `currency` to another currency at checkout/settlement. Absent (or `0`) when not configured.                                                                                                                                                                                                                                                                                                  |
| 2026-07-14 | **Multi-currency pricing.** The response now returns a `currency` field (ISO 4217, default `"USD"`) and currency-aware major-unit price fields (`originalPrice` / `sellingPrice` as `currency` major-unit strings; `minSellingPrice`, `maxSellingPrice`, `customPriceOptions` for custom mode; per-tier `originalPrice` / `sellingPrice`). **Deprecated** the legacy `*_usd_cent` response fields — back-filled from the major-unit fields for USD SKUs, `0`/absent for non-USD SKUs. See [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). |

---

# ListSKUs

# <a name="_58jpgh2b0pya"></a>ListSKUs

**Host**: **dip-cb.binanceapi.com**

**GET** /mp-api/v1/apps/\{appId\}/skus?page=1&limit=20&auditStatus=

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**           |
| :------------ | :------------------------ |
| appId         | AppId of the mini program |

**Query Parameters**

| **Parameter** | **Required** | **Description**                                                    |
| :------------ | :----------- | :----------------------------------------------------------------- |
| page          | No           | Designated query page. Defaults to 1.                              |
| limit         | No           | Quantity limit per page. The maximum size is 50. Defaults to 50.   |
| auditStatus   | No           | SKU audit status filter. Can be 'TODO', 'APPROVED', or 'REJECTED'. |

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "skus": [
      {
        "id": "bn_point_100",
        "audit": {
          "info": {
            "id": "bn_point_100",
            "defaultName": "BN 100 points",
            "names": {
              "en": "BN 100 points",
              "zh-TW": "BN 100 點"
            },
            "category": "Games",
            "imageUrl": "https://bn.com/hnCWgai85XJwn7qSRXjiUt.png",
            "imageStatus": "UPLOADING",
            "originalPrice": "9.99",
            "sellingPrice": "6.99",
            "discountPercentage": 30,
            "path": "/pages/index/index?foo=bar&baz=qux",
            "description": "A virtual top-up item",
            "stocks": 100,
            "autoDelivery": true,
            "maxQuantity": 5,
            "countryWhitelist": ["TW", "JP"],
            "countryBlacklist": ["SG"],
            "currency": "USD",
            "pricingMode": "flat",
            "pricingTiers": []
          },
          "auditStatus": "APPROVED"
        },
        "online": {
          "info": {
            "id": "bn_point_100",
            "defaultName": "BN 100 points",
            "names": {
              "en": "BN 100 points",
              "zh-TW": "BN 100 點"
            },
            "category": "Games",
            "imageUrl": "https://bn.com/hnCWgai85XJwn7qSRXjiUt.png",
            "imageStatus": "UPLOADING",
            "originalPrice": "19.99",
            "sellingPrice": "17.99",
            "discountPercentage": 10,
            "path": "/pages/index/index?foo=bar&baz=qux",
            "description": "A virtual top-up item",
            "stocks": 100,
            "autoDelivery": true,
            "maxQuantity": 5,
            "countryWhitelist": ["TW", "JP", "ID"],
            "countryBlacklist": ["SG"],
            "currency": "USD",
            "pricingMode": "flat",
            "pricingTiers": []
          },
          "availableStatus": "ACTIVE"
        }
      }
    ]
  },
  "success": true
}
```

**Response Parameters**

| **Parameter**             | **Description**                                                                                                                                                                                                                                                                                           |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| skus                      | Array of SKU information                                                                                                                                                                                                                                                                                  |
| audit                     | Audit information for the SKU                                                                                                                                                                                                                                                                             |
| online                    | Online information for the SKU                                                                                                                                                                                                                                                                            |
| imageStatus               | Status of the SKU image, could be 'UPLOADING', 'SUCCESS', 'FAILED', or 'NONEXISTED'                                                                                                                                                                                                                       |
| auditStatus               | Audit status of the SKU, could be 'TODO', 'APPROVED', or 'REJECTED'                                                                                                                                                                                                                                       |
| availableStatus           | Availability status of the SKU, controlled by merchant. Can be 'ACTIVE' or 'DEACTIVE'                                                                                                                                                                                                                     |
| metadata                  | Pagination information. 'itemCount' is the total count for the current response, 'itemsPerPage' is the total count per page as per the given request                                                                                                                                                      |
| description               | Merchant-provided description for this SKU                                                                                                                                                                                                                                                                |
| stocks                    | Merchant-provided inventory quantity. Absent if not set.                                                                                                                                                                                                                                                  |
| autoDelivery              | Whether the SKU supports automatic delivery after purchase. Only SKUs with auto delivery enabled can complete the full purchase flow within Lifestyle; SKUs without it require the merchant to fulfill delivery out-of-band. Absent if not set.                                                           |
| maxQuantity               | Maximum quantity a buyer can purchase per order (1–99). Defaults to `99` when not explicitly set. When `1`, the UI hides the quantity input widget.                                                                                                                                                       |
| currency                  | ISO 4217 currency code that all monetary amounts on this SKU are denominated in (applies to **all** pricing modes). Defaults to `"USD"` when not set. Currently always `"USD"` — see [Currency availability](./create-sku-in-audit#currency-availability).                                                |
| originalPrice             | List price as a string, in `currency` major units (e.g. `"9.99"`). For `"tiered"` mode, the maximum `originalPrice` across all tiers.                                                                                                                                                                     |
| sellingPrice              | Actual selling price as a string, in `currency` major units. For `"tiered"` mode, the minimum `sellingPrice` across all tiers. For `"custom"` mode, equals `minSellingPrice`.                                                                                                                             |
| pricingMode               | Pricing mode: `"flat"` for a single price, `"tiered"` for multiple fixed denomination options, `"custom"` for user-entered amount within a range                                                                                                                                                          |
| pricingTiers              | Array of [PricingTier](./create-sku-in-audit#pricing-tier-object) objects. Present when `pricingMode` is `"tiered"`, empty array otherwise. Each tier carries `originalPrice`/`sellingPrice` in `currency` major units, and may include `autoDelivery`, `maxQuantity`, and `stocks` overrides.            |
| minSellingPrice           | Minimum amount the user may enter, in `currency` major units. Present when `pricingMode` is `"custom"`.                                                                                                                                                                                                   |
| maxSellingPrice           | Maximum amount the user may enter, in `currency` major units. Present when `pricingMode` is `"custom"`.                                                                                                                                                                                                   |
| customPriceOptions        | Preset amounts for buyer quick-select, each in `currency` major units. Present when `pricingMode` is `"custom"` and presets were configured; absent otherwise.                                                                                                                                            |
| minSellingPriceUsdCent    | ⚠️ **Deprecated.** Legacy minimum in **USD cents** (only meaningful when `currency == "USD"`). Back-filled from `minSellingPrice` (`round(major × 100)`) for USD SKUs; `0` for non-USD SKUs. Prefer `minSellingPrice`.                                                                                    |
| maxSellingPriceUsdCent    | ⚠️ **Deprecated.** Legacy maximum in USD cents. Back-filled from `maxSellingPrice` for USD SKUs; `0` for non-USD SKUs. Prefer `maxSellingPrice`.                                                                                                                                                          |
| customPriceOptionsUsdCent | ⚠️ **Deprecated.** Legacy presets in USD cents. Back-filled from `customPriceOptions` for USD SKUs; absent for non-USD SKUs. Prefer `customPriceOptions`.                                                                                                                                                 |
| discountPercentage        | Discount percentage displayed to buyers. For `"flat"` mode, always computed from `(originalPrice − sellingPrice) / originalPrice × 100` (any merchant-provided value is ignored). For `"custom"` mode, the merchant-provided value. For `"tiered"` mode, derived from the tier with the highest discount. |
| exchangeMargin            | Currency-exchange margin percentage applied when converting money from `currency` to another currency at checkout/settlement (e.g. `1.5` means a 1.5% margin). Absent (or `0`) when not configured on the SKU.                                                                                            |

> **Legacy price fields & backward compatibility.** The `*_usd_cent` response fields are
> **deprecated**: they are back-filled from the new major-unit fields for USD SKUs (so existing
> clients reading them still work) and are `0`/absent for non-USD SKUs (no USD-cents value exists
> without the platform exchange rate, which is not stored on the SKU). To render any SKU correctly —
> including non-USD — read `currency` +
> `originalPrice`/`sellingPrice`/`minSellingPrice`/`maxSellingPrice`/`customPriceOptions`. See
> [CreateSKUInAudit — Legacy price fields & backward compatibility](./create-sku-in-audit#legacy-price-fields--backward-compatibility)
> for the full contract.

## Changelog

| Date       | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-07-20 | **Exchange margin.** The response now returns an `exchangeMargin` field — the merchant-provided currency-exchange margin percentage (e.g. `1.5` = 1.5%) applied when converting money from `currency` to another currency at checkout/settlement. Absent (or `0`) when not configured.                                                                                                                                                                                                                                                                                                  |
| 2026-07-14 | **Multi-currency pricing.** The response now returns a `currency` field (ISO 4217, default `"USD"`) and currency-aware major-unit price fields (`originalPrice` / `sellingPrice` as `currency` major-unit strings; `minSellingPrice`, `maxSellingPrice`, `customPriceOptions` for custom mode; per-tier `originalPrice` / `sellingPrice`). **Deprecated** the legacy `*_usd_cent` response fields — back-filled from the major-unit fields for USD SKUs, `0`/absent for non-USD SKUs. See [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). |