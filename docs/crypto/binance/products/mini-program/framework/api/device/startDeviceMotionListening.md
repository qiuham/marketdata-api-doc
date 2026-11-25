---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/startDeviceMotionListening
api_type: Guide
updated_at: 2026-11-25 18:47:21.911120
---

# bn.startDeviceMotionListening

▸ **startDeviceMotionListening**(`options?`): `Promise`<`void`\>

**`description`** Start listening for changes in device orientation.

**`example`**

```ts
bn.startDeviceMotionListening();
```

Parameters

| Name       | Type                               |
| :--------- | :--------------------------------- |
| `options?` | `StartDeviceMotionListeningOption` |

Returns

`Promise`<`void`\>

---

## Interface: StartDeviceMotionListeningOption

| Name      | Type                             | Description                                                                                                                                                                                                                                                                       |
| :-------- | :------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| interval? | `"normal"` \| `"game"` \| `"ui"` | Monitor device direction change callback function execution frequency.; game: The callback frequency for updating the game, in 20ms/second About.; ui: Apply to update UI Callback frequency of 60ms/second About.; normal: Normal callback frequency, in the 200ms/second About. |

---

# bn.startDeviceMotionListening

▸ **startDeviceMotionListening**(`options?`): `Promise`<`void`\>

**`description`** Start listening for changes in device orientation.

**`example`**

```ts
bn.startDeviceMotionListening();
```

Parameters

| Name       | Type                               |
| :--------- | :--------------------------------- |
| `options?` | `StartDeviceMotionListeningOption` |

Returns

`Promise`<`void`\>

---

## Interface: StartDeviceMotionListeningOption

| Name      | Type                             | Description                                                                                                                                                                                                                                                                       |
| :-------- | :------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| interval? | `"normal"` \| `"game"` \| `"ui"` | Monitor device direction change callback function execution frequency.; game: The callback frequency for updating the game, in 20ms/second About.; ui: Apply to update UI Callback frequency of 60ms/second About.; normal: Normal callback frequency, in the 200ms/second About. |