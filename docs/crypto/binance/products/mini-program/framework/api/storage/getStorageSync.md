---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/storage/getStorageSync
api_type: Guide
updated_at: 2026-11-24 18:44:07.552746
---

# bn.getStorageSync

▸ **getStorageSync**<`T`\>(`key`): `T`

**`description`** Gets the specified object synchronously from the local cache key The content of.

**`example`**

```ts
try {
  const value = bn.getStorageSync("key");
  if (value) {
    // From the something with return value
  }
} catch (error) {
  // From the something when catch error
}
```

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name  | Type     |
| :---- | :------- |
| `key` | `string` |

Returns

`T`

---

---

# bn.getStorageSync

▸ **getStorageSync**<`T`\>(`key`): `T`

**`description`** Gets the specified object synchronously from the local cache key The content of.

**`example`**

```ts
try {
  const value = bn.getStorageSync("key");
  if (value) {
    // From the something with return value
  }
} catch (error) {
  // From the something when catch error
}
```

Type parameters

| Name | Type      |
| :--- | :-------- |
| `T`  | `unknown` |

Parameters

| Name  | Type     |
| :---- | :------- |
| `key` | `string` |

Returns

`T`

---