---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/onPageNotFound
api_type: Guide
updated_at: 2026-11-24 18:47:54.480856
---

# bn.onPageNotFound

• **onPageNotFound**: (`cb`: `PageNotFoundCallback`) => `void`

Type declaration

▸ (`cb`): `void`

Parameters

| Name | Type                   |
| :--- | :--------------------- |
| `cb` | `PageNotFoundCallback` |

Returns

`void`

---

## PageNotFoundCallback

Ƭ **PageNotFoundCallback**: (`result`: `OnPageNotFoundCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                           |
| :------- | :----------------------------- |
| `result` | `OnPageNotFoundCallbackResult` |

Returns

`void`

---

## Interface: OnPageNotFoundCallbackResult

| Name        | Type                           | Description |
| :---------- | :----------------------------- | :---------- |
| isEntryPage | `boolean`                      |             |
| path        | `string`                       |             |
| query       | `Record`<`string`, `unknown`\> |             |

---

# bn.onPageNotFound

• **onPageNotFound**: (`cb`: `PageNotFoundCallback`) => `void`

Type declaration

▸ (`cb`): `void`

Parameters

| Name | Type                   |
| :--- | :--------------------- |
| `cb` | `PageNotFoundCallback` |

Returns

`void`

---

## PageNotFoundCallback

Ƭ **PageNotFoundCallback**: (`result`: `OnPageNotFoundCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                           |
| :------- | :----------------------------- |
| `result` | `OnPageNotFoundCallbackResult` |

Returns

`void`

---

## Interface: OnPageNotFoundCallbackResult

| Name        | Type                           | Description |
| :---------- | :----------------------------- | :---------- |
| isEntryPage | `boolean`                      |             |
| path        | `string`                       |             |
| query       | `Record`<`string`, `unknown`\> |             |