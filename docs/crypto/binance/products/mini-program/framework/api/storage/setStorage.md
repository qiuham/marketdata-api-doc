---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/storage/setStorage
api_type: Guide
updated_at: 2026-11-25 18:44:05.173639
---

# bn.setStorage

▸ **setStorage**(`options`): `Promise`<`void`\>

**`description`** To store data in the local cache key In. Will overwrite the original key The
corresponding content. Data is always available unless the user actively deletes it or the system
cleans it for storage reasons. single key The maximum length of data allowed to be stored is 1 MB,
all data storage capped at 10MB.

**`example`**

```ts
bn.setStorage({
  key: "key",
  data: "value",
});
```

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `SetStorageOptions` |

Returns

`Promise`<`void`\>

---

## Interface: SetStorageOptions

| Name | Type      | Description                      |
| :--- | :-------- | :------------------------------- |
| key  | `string`  | Specified in the local cache key |
| data | `unknown` | Key corresponds to the content   |

---

# bn.setStorage

▸ **setStorage**(`options`): `Promise`<`void`\>

**`description`** To store data in the local cache key In. Will overwrite the original key The
corresponding content. Data is always available unless the user actively deletes it or the system
cleans it for storage reasons. single key The maximum length of data allowed to be stored is 1 MB,
all data storage capped at 10MB.

**`example`**

```ts
bn.setStorage({
  key: "key",
  data: "value",
});
```

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `SetStorageOptions` |

Returns

`Promise`<`void`\>

---

## Interface: SetStorageOptions

| Name | Type      | Description                      |
| :--- | :-------- | :------------------------------- |
| key  | `string`  | Specified in the local cache key |
| data | `unknown` | Key corresponds to the content   |