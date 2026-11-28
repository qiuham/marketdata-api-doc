---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/hideHomeButton
api_type: Guide
updated_at: 2026-11-28 18:44:55.741689
---

# bn.hideHomeButton

▸ **hideHomeButton**(`options?`): `Promise`<{}\>

**`description`** Hide Back HomeButton.When the bottom page of the mini program opened by the user
is not the homepage, the "Back to Homepage" button is displayed by default. Developers can use
`hideHomeButton` in the onShow/componentDidShow page to hide HomeButton.

**`example`**

```ts
await bn.hideHomeButton();
```

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `options?` | `CmdHideHomeButtonOptions` |

Returns

`Promise`<{}\>

---

## Interface: CmdHideHomeButtonOptions

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| rendererId | `number` |             |

---

# bn.hideHomeButton

▸ **hideHomeButton**(`options?`): `Promise`<{}\>

**`description`** Hide Back HomeButton.When the bottom page of the mini program opened by the user
is not the homepage, the "Back to Homepage" button is displayed by default. Developers can use
`hideHomeButton` in the onShow/componentDidShow page to hide HomeButton.

**`example`**

```ts
await bn.hideHomeButton();
```

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `options?` | `CmdHideHomeButtonOptions` |

Returns

`Promise`<{}\>

---

## Interface: CmdHideHomeButtonOptions

| Name       | Type     | Description |
| :--------- | :------- | :---------- |
| rendererId | `number` |             |