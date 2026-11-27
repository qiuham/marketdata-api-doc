---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/openapis/scanCode
api_type: Guide
updated_at: 2026-11-27 18:43:39.480974
---

# bn.scanCode

▸ **scanCode**(`options?`): `Promise`<`ScanCodeResponse`\>

**`description`** Set up the client scan interface to scan the code

**`example`**

```ts
bn.scanCode({ success(res) {} });
```

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `options?` | `ScanCodeOptions` |

Returns

`Promise`<`ScanCodeResponse`\>

ScanCodeResponse

## Interface: ScanCodeOptions

| Name      | Type       | Description                                                                                                |
| :-------- | :--------- | :--------------------------------------------------------------------------------------------------------- |
| scanType? | `string`[] | Scan code type, eg: ['barCode', 'qrCode']. barCode: One-dimensional code, qrCode: two-dimensional barcode. |

## Interface: ScanCodeResponse

| Name     | Type     | Description                      |
| :------- | :------- | :------------------------------- |
| result   | `string` | The contents of the scanned code |
| scanType | `string` | Type of code scanned             |

---

# bn.scanCode

▸ **scanCode**(`options?`): `Promise`<`ScanCodeResponse`\>

**`description`** Set up the client scan interface to scan the code

**`example`**

```ts
bn.scanCode({ success(res) {} });
```

Parameters

| Name       | Type              |
| :--------- | :---------------- |
| `options?` | `ScanCodeOptions` |

Returns

`Promise`<`ScanCodeResponse`\>

ScanCodeResponse

## Interface: ScanCodeOptions

| Name      | Type       | Description                                                                                                |
| :-------- | :--------- | :--------------------------------------------------------------------------------------------------------- |
| scanType? | `string`[] | Scan code type, eg: ['barCode', 'qrCode']. barCode: One-dimensional code, qrCode: two-dimensional barcode. |

## Interface: ScanCodeResponse

| Name     | Type     | Description                      |
| :------- | :------- | :------------------------------- |
| result   | `string` | The contents of the scanned code |
| scanType | `string` | Type of code scanned             |