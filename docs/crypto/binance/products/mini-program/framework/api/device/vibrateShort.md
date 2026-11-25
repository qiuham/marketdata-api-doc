---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/vibrateShort
api_type: Guide
updated_at: 2026-11-25 18:47:11.500856
---

# bn.vibrateShort

▸ **vibrateShort**(`options?`): `Promise`<`void`\>

**`description`** Make the mobile phone vibrate for a short time (15 ms）. Only in iPhone 7 / 7 More
Above and Android Model entry into force.

**`example`**

```ts
bn.vibrateShort({ type: "light" });
```

Parameters

| Name       | Type                 |
| :--------- | :------------------- |
| `options?` | `VibrateShortOption` |

Returns

`Promise`<`void`\>

---

## Interface: VibrateShortOption

| Name | Type                                 | Description                                                      |
| :--- | :----------------------------------- | :--------------------------------------------------------------- |
| type | `"light"` \| `"medium"` \| `"heavy"` | Vibration intensity type, valid values are: heavy, medium, light |

---

# bn.vibrateShort

▸ **vibrateShort**(`options?`): `Promise`<`void`\>

**`description`** Make the mobile phone vibrate for a short time (15 ms）. Only in iPhone 7 / 7 More
Above and Android Model entry into force.

**`example`**

```ts
bn.vibrateShort({ type: "light" });
```

Parameters

| Name       | Type                 |
| :--------- | :------------------- |
| `options?` | `VibrateShortOption` |

Returns

`Promise`<`void`\>

---

## Interface: VibrateShortOption

| Name | Type                                 | Description                                                      |
| :--- | :----------------------------------- | :--------------------------------------------------------------- |
| type | `"light"` \| `"medium"` \| `"heavy"` | Vibration intensity type, valid values are: heavy, medium, light |