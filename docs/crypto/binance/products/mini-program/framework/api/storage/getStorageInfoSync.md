---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/storage/getStorageInfoSync
api_type: Guide
updated_at: 2026-11-26 18:44:45.339965
---

# bn.getStorageInfoSync

▸ **getStorageInfoSync**(): `StorageInfo`

**`description`** Gets information about the current storage synchronously.

**`example`**

```ts
try {
  const res = bn.getStorageInfoSync();
  console.log(res.keys);
  console.log(res.currentSize);
  console.log(res.limitSize);
} catch (error) {
  // From the something when catch error
}
```

Returns

`StorageInfo`

StorageInfo

---

## Interface: StorageInfo

| Name        | Type       | Description                     |
| :---------- | :--------- | :------------------------------ |
| keys        | `string`[] | All keys in the current storage |
| currentSize | `number`   | Current space occupied (in KB)  |
| limitSize   | `number`   | Space size limit (in KB)        |

---

# bn.getStorageInfoSync

▸ **getStorageInfoSync**(): `StorageInfo`

**`description`** Gets information about the current storage synchronously.

**`example`**

```ts
try {
  const res = bn.getStorageInfoSync();
  console.log(res.keys);
  console.log(res.currentSize);
  console.log(res.limitSize);
} catch (error) {
  // From the something when catch error
}
```

Returns

`StorageInfo`

StorageInfo

---

## Interface: StorageInfo

| Name        | Type       | Description                     |
| :---------- | :--------- | :------------------------------ |
| keys        | `string`[] | All keys in the current storage |
| currentSize | `number`   | Current space occupied (in KB)  |
| limitSize   | `number`   | Space size limit (in KB)        |