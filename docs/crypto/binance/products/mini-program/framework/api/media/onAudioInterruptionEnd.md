---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/onAudioInterruptionEnd
api_type: Guide
updated_at: 2026-11-18 02:37:54.477298
---

# bn.onAudioInterruptionEnd

▸ **onAudioInterruptionEnd**(`cb`): `void`

**`description`** Listen for audio interrupt end event. Received. onAudioInterruptionBegin After the
event, all audio in the Mini Program will be suspended and can be played again after receiving this
event.

**`example`**

```js
bn.onAudioInterruptionEnd(() => {
  console.log("audio interruption ends");
});
```

Parameters

| Name | Type                        |
| :--- | :-------------------------- |
| `cb` | `AudioInterruptionCallback` |

Returns

`void`

---

## AudioInterruptionCallback

Ƭ **AudioInterruptionCallback**: () => `void`

Type declaration

▸ (): `void`

Returns

`void`

---

# bn.onAudioInterruptionEnd

▸ **onAudioInterruptionEnd**(`cb`): `void`

**`description`** Listen for audio interrupt end event. Received. onAudioInterruptionBegin After the
event, all audio in the Mini Program will be suspended and can be played again after receiving this
event.

**`example`**

```js
bn.onAudioInterruptionEnd(() => {
  console.log("audio interruption ends");
});
```

Parameters

| Name | Type                        |
| :--- | :-------------------------- |
| `cb` | `AudioInterruptionCallback` |

Returns

`void`

---

## AudioInterruptionCallback

Ƭ **AudioInterruptionCallback**: () => `void`

Type declaration

▸ (): `void`

Returns

`void`