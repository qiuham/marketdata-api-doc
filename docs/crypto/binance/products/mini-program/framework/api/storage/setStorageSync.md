---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/storage/setStorageSync
api_type: Guide
updated_at: 2026-11-27 18:43:07.449842
---

# bn.setStorageSync

▸ **setStorageSync**(`key`, `data`): `void`

**`description`** To store data in the local cache key In. Will overwrite the original key The
corresponding content. Data is always available unless the user actively deletes it or the system
cleans it for storage reasons. single key The maximum length of data allowed to be stored is 1 MB,
all data storage capped at 10MB.

**`example`**

```ts
try {
  bn.setStorageSync("key", "value");
} catch (error) {
  // From the something when catch error
}
```

Parameters

| Name   | Type      |
| :----- | :-------- |
| `key`  | `string`  |
| `data` | `unknown` |

Returns

`void`

---

---

# bn.setStorageSync

▸ **setStorageSync**(`key`, `data`): `void`

**`description`** To store data in the local cache key In. Will overwrite the original key The
corresponding content. Data is always available unless the user actively deletes it or the system
cleans it for storage reasons. single key The maximum length of data allowed to be stored is 1 MB,
all data storage capped at 10MB.

**`example`**

```ts
try {
  bn.setStorageSync("key", "value");
} catch (error) {
  // From the something when catch error
}
```

Parameters

| Name   | Type      |
| :----- | :-------- |
| `key`  | `string`  |
| `data` | `unknown` |

Returns

`void`

---