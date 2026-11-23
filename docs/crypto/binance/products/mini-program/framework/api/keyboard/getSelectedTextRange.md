---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/keyboard/getSelectedTextRange
api_type: Guide
updated_at: 2026-11-23 18:46:27.247563
---

# bn.getSelectedTextRange

▸ **getSelectedTextRange**(): `Promise`<`KeyboardGetSelectedTextRangeResponse`\>

**`description`** Obtains the cursor position of the input box after the focus of input, textarea,
etc. Note: This API works only when it is called during the focus process

**`example`**

```js
bn.getSelectedTextRange()
  .then((res) => {
    console.log("getSelectedTextRange res", res.start, res.end);
  })
  .catch((error) => {
    console.log("hideKeyboard error", error);
  });
```

Returns

`Promise`<`KeyboardGetSelectedTextRangeResponse`\>

## KeyboardGetSelectedTextRangeResponse

Ƭ **KeyboardGetSelectedTextRangeResponse**: `Object`

Type declaration

| Name    | Type     |
| :------ | :------- |
| `start` | `number` |
| `end`   | `number` |

---

---

# bn.getSelectedTextRange

▸ **getSelectedTextRange**(): `Promise`<`KeyboardGetSelectedTextRangeResponse`\>

**`description`** Obtains the cursor position of the input box after the focus of input, textarea,
etc. Note: This API works only when it is called during the focus process

**`example`**

```js
bn.getSelectedTextRange()
  .then((res) => {
    console.log("getSelectedTextRange res", res.start, res.end);
  })
  .catch((error) => {
    console.log("hideKeyboard error", error);
  });
```

Returns

`Promise`<`KeyboardGetSelectedTextRangeResponse`\>

## KeyboardGetSelectedTextRangeResponse

Ƭ **KeyboardGetSelectedTextRangeResponse**: `Object`

Type declaration

| Name    | Type     |
| :------ | :------- |
| `start` | `number` |
| `end`   | `number` |

---