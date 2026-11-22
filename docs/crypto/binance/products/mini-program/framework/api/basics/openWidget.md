---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/openWidget
api_type: Guide
updated_at: 2026-11-22 18:44:50.202402
---

# bn.openWidget

▸ **openWidget**(`options`): `Promise`<{ `id`: `number` ; `extra?`: `Record`<`string`, `any`\> }\>

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `OpenWidgetOptions` |

Returns

`Promise`<{ `id`: `number` ; `extra?`: `Record`<`string`, `any`\> }\>

---

## Interface: OpenWidgetOptions

| Name          | Type                       | Description |
| :------------ | :------------------------- | :---------- |
| props?        | `Record`<`string`, `any`\> |             |
| appId         | `string`                   |             |
| path          | `string`                   |             |
| type          | `"alert"` \| `"sheet"`     |             |
| width?        | `number`                   |             |
| height?       | `number`                   |             |
| maskClosable? | `boolean`                  |             |
| onClose?      | (): `void`                 |             |

### onClose

▸ `Optional` **onClose**(): `void`

Returns

`void`

---

# bn.openWidget

▸ **openWidget**(`options`): `Promise`<{ `id`: `number` ; `extra?`: `Record`<`string`, `any`\> }\>

Parameters

| Name      | Type                |
| :-------- | :------------------ |
| `options` | `OpenWidgetOptions` |

Returns

`Promise`<{ `id`: `number` ; `extra?`: `Record`<`string`, `any`\> }\>

---

## Interface: OpenWidgetOptions

| Name          | Type                       | Description |
| :------------ | :------------------------- | :---------- |
| props?        | `Record`<`string`, `any`\> |             |
| appId         | `string`                   |             |
| path          | `string`                   |             |
| type          | `"alert"` \| `"sheet"`     |             |
| width?        | `number`                   |             |
| height?       | `number`                   |             |
| maskClosable? | `boolean`                  |             |
| onClose?      | (): `void`                 |             |

### onClose

▸ `Optional` **onClose**(): `void`

Returns

`void`