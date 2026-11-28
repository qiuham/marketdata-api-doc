---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/getRandomValues
api_type: Guide
updated_at: 2026-11-28 18:46:20.239254
---

# bn.getRandomValues

▸ **getRandomValues**(`options`): `GetRandomValuesResult`

**`description`** Obtaining cryptographically secure random numbers. This api is not excatly the
same as the web crypto api. But you can acheive the same goal. Check the example below.

**`remark`** supported jssdk > 4.27.0

**`example`**

```ts
const typedArray = new Uint8Array(10);
const buffer = await bn.getRandomValues({ length: typedArray.buffer.byteLength });
const resArr = new typedArray.constructor(buffer);
for (let i = 0; i < typedArray.length; i++) {
  typedArray[i] = resArr[i];
}
```

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `options` | `GetRandomValuesOptions` |

Returns

`GetRandomValuesResult`

## Interface: GetRandomValuesOptions

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| length | `number` |             |

## Interface: GetRandomValuesResult

| Name         | Type          | Description |
| :----------- | :------------ | :---------- |
| randomValues | `ArrayBuffer` |             |

---

# bn.getRandomValues

▸ **getRandomValues**(`options`): `GetRandomValuesResult`

**`description`** Obtaining cryptographically secure random numbers. This api is not excatly the
same as the web crypto api. But you can acheive the same goal. Check the example below.

**`remark`** supported jssdk > 4.27.0

**`example`**

```ts
const typedArray = new Uint8Array(10);
const buffer = await bn.getRandomValues({ length: typedArray.buffer.byteLength });
const resArr = new typedArray.constructor(buffer);
for (let i = 0; i < typedArray.length; i++) {
  typedArray[i] = resArr[i];
}
```

Parameters

| Name      | Type                     |
| :-------- | :----------------------- |
| `options` | `GetRandomValuesOptions` |

Returns

`GetRandomValuesResult`

## Interface: GetRandomValuesOptions

| Name   | Type     | Description |
| :----- | :------- | :---------- |
| length | `number` |             |

## Interface: GetRandomValuesResult

| Name         | Type          | Description |
| :----------- | :------------ | :---------- |
| randomValues | `ArrayBuffer` |             |