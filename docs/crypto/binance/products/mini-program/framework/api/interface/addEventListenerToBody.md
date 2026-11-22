---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/interface/addEventListenerToBody
api_type: Guide
updated_at: 2026-11-22 18:44:06.096957
---

# bn.addEventListenerToBody

▸ **addEventListenerToBody**(`type`, `callback`): `void`

**`description`** Add/Remove event listener to body, it will automatically remove the listener when
the page is destroyed. Parameter schema: - \${API}.\${method}.\${param}.\${option}

**`example`**

```js
const handler = function (e) {
  console.log(e);
};
bn.addEventListenerToBody("click", handler);
bn.removeEventListenerFromBody("click", handler);
```

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `type`     | `EventTypes` |
| `callback` | `MpFunction` |

Returns

`void`

---

## EventTypes

Ƭ **EventTypes**: `"tap"` \| `"input"` \| `"focus"` \| `"blur"` \| `"confirm"` \| `"paste"` \|
`"keyboardheightchange"` \| `"keyboardaccessoryitemclick"` \| `"change"` \| `"changing"` \|
`"click"` \| `"touchstart"` \| `"touchmove"` \| `"touchend"` \| `"touchcancel"` \| `"longpress"` \|
`"submit"` \| `"reset"` \| `"linechange"` \| `"cancel"` \| `"pickstart"` \| `"pickend"` \| `"play"`
\| `"pause"` \| `"ended"` \| `"timeupdate"` \| `"fullscreenchange"` \| `"load"` \| `"error"` \|
`"scroll"` \| `"scrolltoupper"` \| `"scrolltolower"` \| `"success"` \| `"fail"` \| `"complete"` \|
`"message"` \| `"columnchange"` \| `"transition"` \| `"animationfinish"`

---

## MpFunction

Ƭ **MpFunction**: (`event`: `MPEvent`) => `void`

Type declaration

▸ (`event`): `void`

Parameters

| Name    | Type      |
| :------ | :-------- |
| `event` | `MPEvent` |

Returns

`void`

## Interface: MPEvent<T, D\>

| Name              | Type                          | Description |
| :---------------- | :---------------------------- | :---------- |
| type              | `T`                           |             |
| timeStamp         | `number`                      |             |
| target            | `MPEventTarget`               |             |
| currentTarget     | `MPEventTarget`               |             |
| detail            | `D`                           |             |
| \_currentTarget?  | `Element`                     |             |
| \_type?           | `T`                           |             |
| \_detail?         | `D`                           |             |
| touches?          | (`CanvasTouch` \| `ITouch`)[] |             |
| changedTouches?   | (`CanvasTouch` \| `ITouch`)[] |             |
| \_touches?        | (`CanvasTouch` \| `ITouch`)[] |             |
| \_changedTouches? | (`CanvasTouch` \| `ITouch`)[] |             |
| seqId?            | `number`                      |             |
| control?          | (`payload`): `void`           |             |

### control

▸ `Optional` **control**(`payload`): `void`

Parameters

| Name              | Type     |
| :---------------- | :------- |
| `payload`         | `Object` |
| `payload.value?`  | `string` |
| `payload.cursor?` | `number` |

Returns

`void`

---

# bn.addEventListenerToBody

▸ **addEventListenerToBody**(`type`, `callback`): `void`

**`description`** Add/Remove event listener to body, it will automatically remove the listener when
the page is destroyed. Parameter schema: - \${API}.\${method}.\${param}.\${option}

**`example`**

```js
const handler = function (e) {
  console.log(e);
};
bn.addEventListenerToBody("click", handler);
bn.removeEventListenerFromBody("click", handler);
```

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `type`     | `EventTypes` |
| `callback` | `MpFunction` |

Returns

`void`

---

## EventTypes

Ƭ **EventTypes**: `"tap"` \| `"input"` \| `"focus"` \| `"blur"` \| `"confirm"` \| `"paste"` \|
`"keyboardheightchange"` \| `"keyboardaccessoryitemclick"` \| `"change"` \| `"changing"` \|
`"click"` \| `"touchstart"` \| `"touchmove"` \| `"touchend"` \| `"touchcancel"` \| `"longpress"` \|
`"submit"` \| `"reset"` \| `"linechange"` \| `"cancel"` \| `"pickstart"` \| `"pickend"` \| `"play"`
\| `"pause"` \| `"ended"` \| `"timeupdate"` \| `"fullscreenchange"` \| `"load"` \| `"error"` \|
`"scroll"` \| `"scrolltoupper"` \| `"scrolltolower"` \| `"success"` \| `"fail"` \| `"complete"` \|
`"message"` \| `"columnchange"` \| `"transition"` \| `"animationfinish"`

---

## MpFunction

Ƭ **MpFunction**: (`event`: `MPEvent`) => `void`

Type declaration

▸ (`event`): `void`

Parameters

| Name    | Type      |
| :------ | :-------- |
| `event` | `MPEvent` |

Returns

`void`

## Interface: MPEvent<T, D\>

| Name              | Type                          | Description |
| :---------------- | :---------------------------- | :---------- |
| type              | `T`                           |             |
| timeStamp         | `number`                      |             |
| target            | `MPEventTarget`               |             |
| currentTarget     | `MPEventTarget`               |             |
| detail            | `D`                           |             |
| \_currentTarget?  | `Element`                     |             |
| \_type?           | `T`                           |             |
| \_detail?         | `D`                           |             |
| touches?          | (`CanvasTouch` \| `ITouch`)[] |             |
| changedTouches?   | (`CanvasTouch` \| `ITouch`)[] |             |
| \_touches?        | (`CanvasTouch` \| `ITouch`)[] |             |
| \_changedTouches? | (`CanvasTouch` \| `ITouch`)[] |             |
| seqId?            | `number`                      |             |
| control?          | (`payload`): `void`           |             |

### control

▸ `Optional` **control**(`payload`): `void`

Parameters

| Name              | Type     |
| :---------------- | :------- |
| `payload`         | `Object` |
| `payload.value?`  | `string` |
| `payload.cursor?` | `number` |

Returns

`void`