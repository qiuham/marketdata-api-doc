---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/media/onAudioInterruptionBegin
api_type: Guide
updated_at: 2026-11-25 18:45:39.865816
---

# bn.onAudioInterruptionBegin

▸ **onAudioInterruptionBegin**(`cb`): `void`

**`description`** Listen audio is interrupted by system occupation. Start event. The following
scenarios trigger this event: alarm clock, phone, FaceTime Call, voice chat, video chat. When this
event is triggered, all audio in the Mini Program will pause.

**`example`**

```js
bn.onAudioInterruptionBegin(() => {
  console.log("audio interruption begins");
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

# bn.onAudioInterruptionBegin

▸ **onAudioInterruptionBegin**(`cb`): `void`

**`description`** Listen audio is interrupted by system occupation. Start event. The following
scenarios trigger this event: alarm clock, phone, FaceTime Call, voice chat, video chat. When this
event is triggered, all audio in the Mini Program will pause.

**`example`**

```js
bn.onAudioInterruptionBegin(() => {
  console.log("audio interruption begins");
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