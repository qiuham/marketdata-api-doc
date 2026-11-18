---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/getNetworkType
api_type: Guide
updated_at: 2026-11-18 18:46:52.503585
---

# bn.getNetworkType

▸ **getNetworkType**(): `Promise`<`GetNetworkTypeResult`\>

Gets the network type.

Returns

`Promise`<`GetNetworkTypeResult`\>

## GetNetworkTypeResult

Ƭ **GetNetworkTypeResult**: `Object`

Type declaration

| Name              | Type          | Description          |
| :---------------- | :------------ | :------------------- |
| `networkType`     | `NetworkType` | Network type         |
| `signalStrength?` | `number`      | Signal strength, dbm |

---

## NetworkType

Ƭ **NetworkType**: `"wifi"` \| `"2g"` \| `"3g"` \| `"4g"` \| `"5g"` \| `"unknown"` \| `"none"`

networkType- 'wifi': wifi;

- '2g': 2g;
- '3g': 3g;
- '4g': 4g;
- 'unknown': Android unknown type;
- 'none': offline;

---

# bn.getNetworkType

▸ **getNetworkType**(): `Promise`<`GetNetworkTypeResult`\>

Gets the network type.

Returns

`Promise`<`GetNetworkTypeResult`\>

## GetNetworkTypeResult

Ƭ **GetNetworkTypeResult**: `Object`

Type declaration

| Name              | Type          | Description          |
| :---------------- | :------------ | :------------------- |
| `networkType`     | `NetworkType` | Network type         |
| `signalStrength?` | `number`      | Signal strength, dbm |

---

## NetworkType

Ƭ **NetworkType**: `"wifi"` \| `"2g"` \| `"3g"` \| `"4g"` \| `"5g"` \| `"unknown"` \| `"none"`

networkType- 'wifi': wifi;

- '2g': 2g;
- '3g': 3g;
- '4g': 4g;
- 'unknown': Android unknown type;
- 'none': offline;