---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/onUnhandledRejection
api_type: Guide
updated_at: 2026-11-21 18:47:28.654943
---

# bn.onUnhandledRejection

• **onUnhandledRejection**: (`cb`: `UnhandledRejectionCallback`) => `void`

Type declaration

▸ (`cb`): `void`

Parameters

| Name | Type                         |
| :--- | :--------------------------- |
| `cb` | `UnhandledRejectionCallback` |

Returns

`void`

---

## UnhandledRejectionCallback

Ƭ **UnhandledRejectionCallback**: (`payload`: `OnUnhandledRejectionCallbackResult`) => `void`

Type declaration

▸ (`payload`): `void`

Parameters

| Name      | Type                                 |
| :-------- | :----------------------------------- |
| `payload` | `OnUnhandledRejectionCallbackResult` |

Returns

`void`

---

## Interface: OnUnhandledRejectionCallbackResult

| Name    | Type                  | Description |
| :------ | :-------------------- | :---------- |
| promise | `Promise`<`unknown`\> |             |
| reason  | `string`              |             |

---

# bn.onUnhandledRejection

• **onUnhandledRejection**: (`cb`: `UnhandledRejectionCallback`) => `void`

Type declaration

▸ (`cb`): `void`

Parameters

| Name | Type                         |
| :--- | :--------------------------- |
| `cb` | `UnhandledRejectionCallback` |

Returns

`void`

---

## UnhandledRejectionCallback

Ƭ **UnhandledRejectionCallback**: (`payload`: `OnUnhandledRejectionCallbackResult`) => `void`

Type declaration

▸ (`payload`): `void`

Parameters

| Name      | Type                                 |
| :-------- | :----------------------------------- |
| `payload` | `OnUnhandledRejectionCallbackResult` |

Returns

`void`

---

## Interface: OnUnhandledRejectionCallbackResult

| Name    | Type                  | Description |
| :------ | :-------------------- | :---------- |
| promise | `Promise`<`unknown`\> |             |
| reason  | `string`              |             |