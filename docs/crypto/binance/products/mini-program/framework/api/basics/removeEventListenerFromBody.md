---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/basics/removeEventListenerFromBody
api_type: Guide
updated_at: 2026-11-28 18:45:42.962154
---

# bn.removeEventListenerFromBody

▸ **removeEventListenerFromBody**(`type`, `callback`): `void`

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `type`     | `EventTypes` |
| `callback` | `MpFunction` |

Returns

`void`

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

# bn.removeEventListenerFromBody

▸ **removeEventListenerFromBody**(`type`, `callback`): `void`

Parameters

| Name       | Type         |
| :--------- | :----------- |
| `type`     | `EventTypes` |
| `callback` | `MpFunction` |

Returns

`void`

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