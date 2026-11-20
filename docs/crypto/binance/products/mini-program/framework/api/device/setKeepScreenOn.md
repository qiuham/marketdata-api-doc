---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/setKeepScreenOn
api_type: Guide
updated_at: 2026-11-20 18:48:32.858947
---

# bn.setKeepScreenOn

▸ **setKeepScreenOn**(`options`): `Promise`<`void`\>

**`description`** Sets whether or not to always light. Only the current Mini Program is in effect
and the settings are disabled after leaving the Mini Program.

**`example`**

```ts
bn.setKeepScreenOn({ keepScreenOn: true });
```

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `options` | `SetKeepScreenOnOption` |

Returns

`Promise`<`void`\>

## Interface: SetKeepScreenOnOption

| Name         | Type      | Description            |
| :----------- | :-------- | :--------------------- |
| keepScreenOn | `boolean` | Keep the screen bright |

---

# bn.setKeepScreenOn

▸ **setKeepScreenOn**(`options`): `Promise`<`void`\>

**`description`** Sets whether or not to always light. Only the current Mini Program is in effect
and the settings are disabled after leaving the Mini Program.

**`example`**

```ts
bn.setKeepScreenOn({ keepScreenOn: true });
```

Parameters

| Name      | Type                    |
| :-------- | :---------------------- |
| `options` | `SetKeepScreenOnOption` |

Returns

`Promise`<`void`\>

## Interface: SetKeepScreenOnOption

| Name         | Type      | Description            |
| :----------- | :-------- | :--------------------- |
| keepScreenOn | `boolean` | Keep the screen bright |