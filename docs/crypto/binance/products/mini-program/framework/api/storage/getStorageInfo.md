---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/storage/getStorageInfo
api_type: Guide
updated_at: 2026-11-18 18:43:15.343720
---

# bn.getStorageInfo

▸ **getStorageInfo**(): `Promise`<`StorageInfo`\>

**`description`** Gets information about the current storage asynchronously.

**`example`**

```ts
bn.getStorageInfo({
  success(res) {
    console.log(res.keys);
    console.log(res.currentSize);
    console.log(res.limitSize);
  },
});
```

Returns

`Promise`<`StorageInfo`\>

StorageInfo

---

## Interface: StorageInfo

| Name        | Type       | Description                     |
| :---------- | :--------- | :------------------------------ |
| keys        | `string`[] | All keys in the current storage |
| currentSize | `number`   | Current space occupied (in KB)  |
| limitSize   | `number`   | Space size limit (in KB)        |

---

# bn.getStorageInfo

▸ **getStorageInfo**(): `Promise`<`StorageInfo`\>

**`description`** Gets information about the current storage asynchronously.

**`example`**

```ts
bn.getStorageInfo({
  success(res) {
    console.log(res.keys);
    console.log(res.currentSize);
    console.log(res.limitSize);
  },
});
```

Returns

`Promise`<`StorageInfo`\>

StorageInfo

---

## Interface: StorageInfo

| Name        | Type       | Description                     |
| :---------- | :--------- | :------------------------------ |
| keys        | `string`[] | All keys in the current storage |
| currentSize | `number`   | Current space occupied (in KB)  |
| limitSize   | `number`   | Space size limit (in KB)        |