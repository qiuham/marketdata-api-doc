---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/startAccelerometer
api_type: Guide
updated_at: 2026-11-26 18:47:56.160565
---

# bn.startAccelerometer

▸ **startAccelerometer**(`options?`): `Promise`<`void`\>

**`description`** Start monitoring the acceleration data.

**`example`**

```ts
bn.startAccelerometer({ interval: "game" });
```

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `options?` | `StartAccelerometerOption` |

Returns

`Promise`<`void`\>

---

## Interface: StartAccelerometerOption

| Name      | Type                             | Description                                                                                                                                                                                                                                                                            |
| :-------- | :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| interval? | `"normal"` \| `"game"` \| `"ui"` | Monitor the execution frequency of the acceleration data callback function.; game: The callback frequency for updating the game, in 20ms/second About.; ui: Apply to update UI Callback frequency of 60ms/second About.; normal: Normal callback frequency, in the 200ms/second About. |

---

# bn.startAccelerometer

▸ **startAccelerometer**(`options?`): `Promise`<`void`\>

**`description`** Start monitoring the acceleration data.

**`example`**

```ts
bn.startAccelerometer({ interval: "game" });
```

Parameters

| Name       | Type                       |
| :--------- | :------------------------- |
| `options?` | `StartAccelerometerOption` |

Returns

`Promise`<`void`\>

---

## Interface: StartAccelerometerOption

| Name      | Type                             | Description                                                                                                                                                                                                                                                                            |
| :-------- | :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| interval? | `"normal"` \| `"game"` \| `"ui"` | Monitor the execution frequency of the acceleration data callback function.; game: The callback frequency for updating the game, in 20ms/second About.; ui: Apply to update UI Callback frequency of 60ms/second About.; normal: Normal callback frequency, in the 200ms/second About. |