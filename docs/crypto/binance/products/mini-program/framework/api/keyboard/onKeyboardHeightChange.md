---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/keyboard/onKeyboardHeightChange
api_type: Guide
updated_at: 2026-11-24 18:46:05.950116
---

# bn.onKeyboardHeightChange

▸ **onKeyboardHeightChange**(`cb`): `void`

**`description`** Listens on the keyboard height changes

**`example`**

```js
function callback(res) {
  console.log(res.height);
}
bn.onKeyboardHeightChange(callback);
```

Parameters

| Name | Type                             | Description                        |
| :--- | :------------------------------- | :--------------------------------- |
| `cb` | `onKeyboardHeightChangeCallback` | Callback on keyboard height change |

Returns

`void`

---

## onKeyboardHeightChangeCallback

Ƭ **onKeyboardHeightChangeCallback**: (`result`: `EventKeyboardHeightChangePayload`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                               |
| :------- | :--------------------------------- |
| `result` | `EventKeyboardHeightChangePayload` |

Returns

`void`

---

## Interface: EventKeyboardHeightChangePayload

| Name   | Type     | Description        |
| :----- | :------- | :----------------- |
| height | `number` | height of keyboard |

---

# bn.onKeyboardHeightChange

▸ **onKeyboardHeightChange**(`cb`): `void`

**`description`** Listens on the keyboard height changes

**`example`**

```js
function callback(res) {
  console.log(res.height);
}
bn.onKeyboardHeightChange(callback);
```

Parameters

| Name | Type                             | Description                        |
| :--- | :------------------------------- | :--------------------------------- |
| `cb` | `onKeyboardHeightChangeCallback` | Callback on keyboard height change |

Returns

`void`

---

## onKeyboardHeightChangeCallback

Ƭ **onKeyboardHeightChangeCallback**: (`result`: `EventKeyboardHeightChangePayload`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                               |
| :------- | :--------------------------------- |
| `result` | `EventKeyboardHeightChangePayload` |

Returns

`void`

---

## Interface: EventKeyboardHeightChangePayload

| Name   | Type     | Description        |
| :----- | :------- | :----------------- |
| height | `number` | height of keyboard |