---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/storage/getStorage
api_type: Guide
updated_at: 2026-11-22 18:41:38.770498
---

# bn.getStorage

▸ **getStorage**<`T`\>(`options`): `Promise`<{ `data`: `T` }\>

**`description`** Gets the specified object asynchronously from the local cache key The content of.

**`example`**

```ts
bn.getStorage({
  key: "key",
  success(res) {
    console.log(res.data);
  },
});
```

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `GetStorageOptions` |

Returns

`Promise`<{ `data`: `T` }\>

---

## Interface: GetStorageOptions

| Name | Type     | Description                      |
| :--- | :------- | :------------------------------- |
| key  | `string` | Specified in the local cache key |

---

# bn.getStorage

▸ **getStorage**<`T`\>(`options`): `Promise`<{ `data`: `T` }\>

**`description`** Gets the specified object asynchronously from the local cache key The content of.

**`example`**

```ts
bn.getStorage({
  key: "key",
  success(res) {
    console.log(res.data);
  },
});
```

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `GetStorageOptions` |

Returns

`Promise`<{ `data`: `T` }\>

---

## Interface: GetStorageOptions

| Name | Type     | Description                      |
| :--- | :------- | :------------------------------- |
| key  | `string` | Specified in the local cache key |