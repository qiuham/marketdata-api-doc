---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/showActionSheet
api_type: Guide
updated_at: 2026-11-18 02:40:31.895317
---

# bn.showActionSheet

▸ **showActionSheet**(`options`): `Promise`<`ActionSheetResult`\>

**`description`** Displays an action sheet.

**`example`**

```javascript
bn.showActionSheet({
  itemList: ["A", "B", "C"],
  success(res) {
    console.log(res.tapIndex);
  },
  fail(res) {
    console.log(res.errMsg);
  },
});
```

Parameters

| Name      | Type                 |
| :-------- | :------------------- |
| `options` | `ActionSheetOptions` |

Returns

`Promise`<`ActionSheetResult`\>

## ActionSheetOptions

Ƭ **ActionSheetOptions**: `Object`

Type declaration

| Name         | Type       | Description                                              |
| :----------- | :--------- | :------------------------------------------------------- |
| `alertText?` | `string`   | Alert text                                               |
| `itemList`   | `string`[] | The text array of the button, with a length limited to 6 |
| `itemColor?` | `string`   | The text color of the button                             |

---

## ActionSheetResult

Ƭ **ActionSheetResult**: `Object`

Type declaration

| Name       | Type     | Description                                                                                  |
| :--------- | :------- | :------------------------------------------------------------------------------------------- |
| `tapIndex` | `number` | The sequence number of the button tapped by the user, from top to bottom and starting from 0 |

---

---

# bn.showActionSheet

▸ **showActionSheet**(`options`): `Promise`<`ActionSheetResult`\>

**`description`** Displays an action sheet.

**`example`**

```javascript
bn.showActionSheet({
  itemList: ["A", "B", "C"],
  success(res) {
    console.log(res.tapIndex);
  },
  fail(res) {
    console.log(res.errMsg);
  },
});
```

Parameters

| Name      | Type                 |
| :-------- | :------------------- |
| `options` | `ActionSheetOptions` |

Returns

`Promise`<`ActionSheetResult`\>

## ActionSheetOptions

Ƭ **ActionSheetOptions**: `Object`

Type declaration

| Name         | Type       | Description                                              |
| :----------- | :--------- | :------------------------------------------------------- |
| `alertText?` | `string`   | Alert text                                               |
| `itemList`   | `string`[] | The text array of the button, with a length limited to 6 |
| `itemColor?` | `string`   | The text color of the button                             |

---

## ActionSheetResult

Ƭ **ActionSheetResult**: `Object`

Type declaration

| Name       | Type     | Description                                                                                  |
| :--------- | :------- | :------------------------------------------------------------------------------------------- |
| `tapIndex` | `number` | The sequence number of the button tapped by the user, from top to bottom and starting from 0 |

---