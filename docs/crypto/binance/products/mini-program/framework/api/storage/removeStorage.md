---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/storage/removeStorage
api_type: Guide
updated_at: 2026-11-24 18:44:06.162659
---

# bn.removeStorage

▸ **removeStorage**(`options`): `Promise`<`void`\>

**`description`** Removes the specified item from the local cache key.

**`example`**

```ts
bn.removeStorage({
  key: "key",
  success(res) {
    console.log(res);
  },
});
```

Parameters

| Name      | Type                   |
| :-------- | :--------------------- |
| `options` | `RemoveStorageOptions` |

Returns

`Promise`<`void`\>

---

## Interface: RemoveStorageOptions

| Name | Type     | Description                      |
| :--- | :------- | :------------------------------- |
| key  | `string` | Specified in the local cache key |

---

# bn.removeStorage

▸ **removeStorage**(`options`): `Promise`<`void`\>

**`description`** Removes the specified item from the local cache key.

**`example`**

```ts
bn.removeStorage({
  key: "key",
  success(res) {
    console.log(res);
  },
});
```

Parameters

| Name      | Type                   |
| :-------- | :--------------------- |
| `options` | `RemoveStorageOptions` |

Returns

`Promise`<`void`\>

---

## Interface: RemoveStorageOptions

| Name | Type     | Description                      |
| :--- | :------- | :------------------------------- |
| key  | `string` | Specified in the local cache key |