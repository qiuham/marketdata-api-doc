---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/network/createBufferURL
api_type: Guide
updated_at: 2026-11-27 18:44:24.309028
---

# bn.createBufferURL

▸ **createBufferURL**(`data`, `options?`): `string`

**`description`** Store arrayBuffer in memory and provide an URL to access it

**`example`**

```ts
const url = bn.createBuffer(buffer, { extension: "svg" });
```

Parameters

| Name       | Type                     |
| :--------- | :----------------------- |
| `data`     | `CreateBufferURLData`    |
| `options?` | `CreateBufferURLOptions` |

Returns

`string`

---

## CreateBufferURLData

Ƭ **CreateBufferURLData**: `ArrayBuffer` \| `Int8Array` \| `Uint8Array` \| `Uint8ClampedArray` \|
`Int16Array` \| `Uint16Array` \| `Int32Array` \| `Uint32Array` \| `Float32Array` \| `Float64Array`

---

## CreateBufferURLOptions

Ƭ **CreateBufferURLOptions**: `Object`

Type declaration

| Name         | Type     | Description                                                      |
| :----------- | :------- | :--------------------------------------------------------------- |
| `extension?` | `string` | the options of buffer url. Right now it supports 'svg' extension |

---

# bn.createBufferURL

▸ **createBufferURL**(`data`, `options?`): `string`

**`description`** Store arrayBuffer in memory and provide an URL to access it

**`example`**

```ts
const url = bn.createBuffer(buffer, { extension: "svg" });
```

Parameters

| Name       | Type                     |
| :--------- | :----------------------- |
| `data`     | `CreateBufferURLData`    |
| `options?` | `CreateBufferURLOptions` |

Returns

`string`

---

## CreateBufferURLData

Ƭ **CreateBufferURLData**: `ArrayBuffer` \| `Int8Array` \| `Uint8Array` \| `Uint8ClampedArray` \|
`Int16Array` \| `Uint16Array` \| `Int32Array` \| `Uint32Array` \| `Float32Array` \| `Float64Array`

---

## CreateBufferURLOptions

Ƭ **CreateBufferURLOptions**: `Object`

Type declaration

| Name         | Type     | Description                                                      |
| :----------- | :------- | :--------------------------------------------------------------- |
| `extension?` | `string` | the options of buffer url. Right now it supports 'svg' extension |