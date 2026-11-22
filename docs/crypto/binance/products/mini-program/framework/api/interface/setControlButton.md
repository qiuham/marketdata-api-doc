---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/setControlButton
api_type: Guide
updated_at: 2026-11-22 18:43:48.658364
---

# bn.setControlButton

▸ **setControlButton**(`params?`): `Promise`<{}\>

**`description`** Set Control Button Icon Color / Border Color / Background Color

**`remark`** supported jssdk > 4.33.0

**`example`**

```ts
await bn.setControlButton({
   iconColor: string
   borderColor: string
   backgroundColor: string
})
```

Parameters

| Name      | Type                         |
| :-------- | :--------------------------- |
| `params?` | `CmdSetControlButtonOptions` |

Returns

`Promise`<{}\>

---

## Interface: CmdSetControlButtonOptions

| Name            | Type     | Description |
| :-------------- | :------- | :---------- |
| iconColor       | `string` |             |
| borderColor     | `string` |             |
| backgroundColor | `string` |             |
| rendererId?     | `number` |             |

---

# bn.setControlButton

▸ **setControlButton**(`params?`): `Promise`<{}\>

**`description`** Set Control Button Icon Color / Border Color / Background Color

**`remark`** supported jssdk > 4.33.0

**`example`**

```ts
await bn.setControlButton({
   iconColor: string
   borderColor: string
   backgroundColor: string
})
```

Parameters

| Name      | Type                         |
| :-------- | :--------------------------- |
| `params?` | `CmdSetControlButtonOptions` |

Returns

`Promise`<{}\>

---

## Interface: CmdSetControlButtonOptions

| Name            | Type     | Description |
| :-------------- | :------- | :---------- |
| iconColor       | `string` |             |
| borderColor     | `string` |             |
| backgroundColor | `string` |             |
| rendererId?     | `number` |             |