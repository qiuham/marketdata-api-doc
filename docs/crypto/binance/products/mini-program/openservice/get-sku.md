---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/get-sku
api_type: Guide
updated_at: 2026-11-28 18:36:20.668861
---

# GetSKU

# <a name="_58jpgh2b0pya"></a>GetSKU

**Host**: **dip-cb.binanceapi.com**

**GET** /mp-api/v1/apps/\{appId\}/skus/\{skuId\}

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**               |
| :------------ | :---------------------------- |
| appId         | The AppId of the mini program |
| skuId         | The skuId of the SKU          |

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "sku": {
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
  },
  "success": true
}
```

**Response with tiered pricing**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "sku": {
      "id": "jdcom-cn-giftcard",
      "audit": {
        "info": {
          "id": "jdcom-cn-giftcard",
          "defaultName": "JD.com CN Gift Card",
          "names": { "en": "JD.com CN Gift Card" },
          "category": "Shopping",
          "imageUrl": "https://bn.com/jdcn.png",
          "imageStatus": "SUCCESS",
          "originalPrice": "5.90",
          "sellingPrice": "4.72",
          "discountPercentage": 20,
          "path": "/pages/index/index",
          "description": "JD.com gift card redeemable in China",
          "stocks": 500,
          "autoDelivery": true,
          "maxQuantity": 99,
          "countryWhitelist": ["CN"],
          "countryBlacklist": [],
          "currency": "USD",
          "pricingMode": "tiered",
          "pricingTiers": [
            {
              "tierId": "tier_jdcn_30cny",
              "names": { "en": "JD.com CN 30 CNY" },
              "description": "",
              "originalPrice": "5.90",
              "sellingPrice": "4.72",
              "autoDelivery": true,
              "maxQuantity": 10,
              "stocks": 200
            },
            {
              "tierId": "tier_jdcn_50cny",
              "names": { "en": "JD.com CN 50 CNY" },
              "description": "",
              "originalPrice": "9.80",
              "sellingPrice": "7.84",
              "autoDelivery": true,
              "maxQuantity": 5,
              "stocks": 300
            }
          ]
        },
        "auditStatus": "APPROVED"
      },
      "online": null
    }
  },
  "success": true
}
```

**Response with custom pricing**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "sku": {
      "id": "custom-topup",
      "audit": {
        "info": {
          "id": "custom-topup",
          "defaultName": "Custom Top-up",
          "names": { "en": "Custom Top-up" },
          "category": "Games",
          "imageUrl": "https://bn.com/topup.png",
          "imageStatus": "SUCCESS",
          "path": "/pages/topup/index",
          "description": "Top up any amount between $10 and $500",
          "countryWhitelist": ["JP"],
          "countryBlacklist": [],
          "currency": "USD",
          "originalPrice": "9.99",
          "sellingPrice": "9.99",
          "pricingMode": "custom",
          "minSellingPrice": 10,
          "maxSellingPrice": 500,
          "customPriceOptions": [10, 25, 50],
          "pricingTiers": []
        },
        "auditStatus": "APPROVED"
      },
      "online": null
    }
  },
  "success": true
}
```

**Response Parameters**

| **Parameter**             | **Description**                                                                                                                                                                                                                                                                                           |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| audit                     | Audit information for this SKU                                                                                                                                                                                                                                                                            |
| online                    | Online information for this SKU                                                                                                                                                                                                                                                                           |
| imageStatus               | SKU image status could be either 'UPLOADING', 'SUCCESS', 'FAILED', or 'NONEXISTED'                                                                                                                                                                                                                        |
| auditStatus               | SKU audit status can be 'TODO', 'APPROVED', 'REJECTED'                                                                                                                                                                                                                                                    |
| availableStatus           | SKU available status, controlled by merchants, can be 'ACTIVE', or 'DEACTIVE'                                                                                                                                                                                                                             |
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

| ErrorCode | Remark                    |
| :-------- | :------------------------ |
| 000000    | Success                   |
| 900001    | Invalid Parameter         |
| 900002    | JWT Authentication Failed |
| 900003    | Unexpected Error          |
| 900004    | Invalid FileId            |
| 900260    | Invalid SkuId             |

## Changelog

| Date       | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-07-20 | **Exchange margin.** The response now returns an `exchangeMargin` field — the merchant-provided currency-exchange margin percentage (e.g. `1.5` = 1.5%) applied when converting money from `currency` to another currency at checkout/settlement. Absent (or `0`) when not configured.                                                                                                                                                                                                                                                                                                                  |
| 2026-07-14 | **Multi-currency pricing.** The response now returns a `currency` field (ISO 4217, default `"USD"`) and currency-aware major-unit price fields (`originalPrice` / `sellingPrice` as `currency` major-unit strings; `minSellingPrice`, `maxSellingPrice`, `customPriceOptions` for custom mode; per-tier `originalPrice` / `sellingPrice`). **Deprecated** the legacy `*_usd_cent` response fields — they are back-filled from the major-unit fields for USD SKUs and are `0`/absent for non-USD SKUs. See [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). |

---

# GetSKU

# <a name="_58jpgh2b0pya"></a>GetSKU

**Host**: **dip-cb.binanceapi.com**

**GET** /mp-api/v1/apps/\{appId\}/skus/\{skuId\}

**Header**

| **Parameter**       | **Required** | **Description**                                                                                                                                 |
| :------------------ | :----------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| X-Mp-Open-Api-Token | Yes          | JWT token. Please refer to [Description of External Interface Signature Authentication Algorithm](/products/mini-program/openservice/signature) |

**Path Parameters**

| **Parameter** | **Description**               |
| :------------ | :---------------------------- |
| appId         | The AppId of the mini program |
| skuId         | The skuId of the SKU          |

**Response**

**HTTP 200**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "sku": {
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
  },
  "success": true
}
```

**Response with tiered pricing**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "sku": {
      "id": "jdcom-cn-giftcard",
      "audit": {
        "info": {
          "id": "jdcom-cn-giftcard",
          "defaultName": "JD.com CN Gift Card",
          "names": { "en": "JD.com CN Gift Card" },
          "category": "Shopping",
          "imageUrl": "https://bn.com/jdcn.png",
          "imageStatus": "SUCCESS",
          "originalPrice": "5.90",
          "sellingPrice": "4.72",
          "discountPercentage": 20,
          "path": "/pages/index/index",
          "description": "JD.com gift card redeemable in China",
          "stocks": 500,
          "autoDelivery": true,
          "maxQuantity": 99,
          "countryWhitelist": ["CN"],
          "countryBlacklist": [],
          "currency": "USD",
          "pricingMode": "tiered",
          "pricingTiers": [
            {
              "tierId": "tier_jdcn_30cny",
              "names": { "en": "JD.com CN 30 CNY" },
              "description": "",
              "originalPrice": "5.90",
              "sellingPrice": "4.72",
              "autoDelivery": true,
              "maxQuantity": 10,
              "stocks": 200
            },
            {
              "tierId": "tier_jdcn_50cny",
              "names": { "en": "JD.com CN 50 CNY" },
              "description": "",
              "originalPrice": "9.80",
              "sellingPrice": "7.84",
              "autoDelivery": true,
              "maxQuantity": 5,
              "stocks": 300
            }
          ]
        },
        "auditStatus": "APPROVED"
      },
      "online": null
    }
  },
  "success": true
}
```

**Response with custom pricing**

```json
{
  "code": "000000",
  "message": null,
  "data": {
    "sku": {
      "id": "custom-topup",
      "audit": {
        "info": {
          "id": "custom-topup",
          "defaultName": "Custom Top-up",
          "names": { "en": "Custom Top-up" },
          "category": "Games",
          "imageUrl": "https://bn.com/topup.png",
          "imageStatus": "SUCCESS",
          "path": "/pages/topup/index",
          "description": "Top up any amount between $10 and $500",
          "countryWhitelist": ["JP"],
          "countryBlacklist": [],
          "currency": "USD",
          "originalPrice": "9.99",
          "sellingPrice": "9.99",
          "pricingMode": "custom",
          "minSellingPrice": 10,
          "maxSellingPrice": 500,
          "customPriceOptions": [10, 25, 50],
          "pricingTiers": []
        },
        "auditStatus": "APPROVED"
      },
      "online": null
    }
  },
  "success": true
}
```

**Response Parameters**

| **Parameter**             | **Description**                                                                                                                                                                                                                                                                                           |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| audit                     | Audit information for this SKU                                                                                                                                                                                                                                                                            |
| online                    | Online information for this SKU                                                                                                                                                                                                                                                                           |
| imageStatus               | SKU image status could be either 'UPLOADING', 'SUCCESS', 'FAILED', or 'NONEXISTED'                                                                                                                                                                                                                        |
| auditStatus               | SKU audit status can be 'TODO', 'APPROVED', 'REJECTED'                                                                                                                                                                                                                                                    |
| availableStatus           | SKU available status, controlled by merchants, can be 'ACTIVE', or 'DEACTIVE'                                                                                                                                                                                                                             |
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

| ErrorCode | Remark                    |
| :-------- | :------------------------ |
| 000000    | Success                   |
| 900001    | Invalid Parameter         |
| 900002    | JWT Authentication Failed |
| 900003    | Unexpected Error          |
| 900004    | Invalid FileId            |
| 900260    | Invalid SkuId             |

## Changelog

| Date       | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-07-20 | **Exchange margin.** The response now returns an `exchangeMargin` field — the merchant-provided currency-exchange margin percentage (e.g. `1.5` = 1.5%) applied when converting money from `currency` to another currency at checkout/settlement. Absent (or `0`) when not configured.                                                                                                                                                                                                                                                                                                                  |
| 2026-07-14 | **Multi-currency pricing.** The response now returns a `currency` field (ISO 4217, default `"USD"`) and currency-aware major-unit price fields (`originalPrice` / `sellingPrice` as `currency` major-unit strings; `minSellingPrice`, `maxSellingPrice`, `customPriceOptions` for custom mode; per-tier `originalPrice` / `sellingPrice`). **Deprecated** the legacy `*_usd_cent` response fields — they are back-filled from the major-unit fields for USD SKUs and are `0`/absent for non-USD SKUs. See [Legacy price fields & backward compatibility](#legacy-price-fields--backward-compatibility). |