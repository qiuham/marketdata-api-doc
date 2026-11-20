---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/startGyroscope
api_type: Guide
updated_at: 2026-11-20 18:48:26.547703
---

# bn.startGyroscope

▸ **startGyroscope**(`options?`): `Promise`<`void`\>

**`description`** Start monitoring the gyroscope data.

**`example`**

```ts
bn.startGyroscope();
```

Parameters

| Name       | Type                   |
| :--------- | :--------------------- |
| `options?` | `StartGyroscopeOption` |

Returns

`Promise`<`void`\>

---

## Interface: StartGyroscopeOption

| Name      | Type                             | Description                                                                                                                                                                                                                                                                    |
| :-------- | :------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| interval? | `"normal"` \| `"game"` \| `"ui"` | Monitor the execution frequency of the gyro data callback function.; game: The callback frequency for updating the game, in 20ms/second About.; ui: Apply to update UI Callback frequency of 60ms/second About.; normal: Normal callback frequency, in the 200ms/second About. |

---

# bn.startGyroscope

▸ **startGyroscope**(`options?`): `Promise`<`void`\>

**`description`** Start monitoring the gyroscope data.

**`example`**

```ts
bn.startGyroscope();
```

Parameters

| Name       | Type                   |
| :--------- | :--------------------- |
| `options?` | `StartGyroscopeOption` |

Returns

`Promise`<`void`\>

---

## Interface: StartGyroscopeOption

| Name      | Type                             | Description                                                                                                                                                                                                                                                                    |
| :-------- | :------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| interval? | `"normal"` \| `"game"` \| `"ui"` | Monitor the execution frequency of the gyro data callback function.; game: The callback frequency for updating the game, in 20ms/second About.; ui: Apply to update UI Callback frequency of 60ms/second About.; normal: Normal callback frequency, in the 200ms/second About. |