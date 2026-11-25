---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/framework/api/device/onMemoryWarning
api_type: Guide
updated_at: 2026-11-25 18:47:30.369508
---

# bn.onMemoryWarning

▸ **onMemoryWarning**(`cb`): `void`

Listens for out-of-memory warning events.

**`description`** On iOS/Android, This event is triggered when a memory warning is issued to the
Mini Programs process. Triggering the event does not mean that the Mini Program is killed. In most
cases, it is just an alarm. Developers can recover some unnecessary resources after receiving the
notification to avoid further aggravating memory strain.

Parameters

| Name | Type                      | Description                                       |
| :--- | :------------------------ | :------------------------------------------------ |
| `cb` | `OnMemoryWarningCallback` | Callback function for out-of-memory warning event |

Returns

`void`

---

## OnMemoryWarningCallback

Ƭ **OnMemoryWarningCallback**: (`result`: `OnMemoryWarningCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                            |
| :------- | :------------------------------ |
| `result` | `OnMemoryWarningCallbackResult` |

Returns

`void`

---

## Interface: OnMemoryWarningCallbackResult

| Name  | Type                | Description                                                                                                                                                                               |
| :---- | :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| level | `5` \| `10` \| `15` | Memory alert level, only Android There is, corresponding to the system macro definition - 5: TRIM_MEMORY_RUNNING_MODERATE; 10: TRIM_MEMORY_RUNNING_LOW; 15: TRIM_MEMORY_RUNNING_CRITICAL; |

---

# bn.onMemoryWarning

▸ **onMemoryWarning**(`cb`): `void`

Listens for out-of-memory warning events.

**`description`** On iOS/Android, This event is triggered when a memory warning is issued to the
Mini Programs process. Triggering the event does not mean that the Mini Program is killed. In most
cases, it is just an alarm. Developers can recover some unnecessary resources after receiving the
notification to avoid further aggravating memory strain.

Parameters

| Name | Type                      | Description                                       |
| :--- | :------------------------ | :------------------------------------------------ |
| `cb` | `OnMemoryWarningCallback` | Callback function for out-of-memory warning event |

Returns

`void`

---

## OnMemoryWarningCallback

Ƭ **OnMemoryWarningCallback**: (`result`: `OnMemoryWarningCallbackResult`) => `void`

Type declaration

▸ (`result`): `void`

Parameters

| Name     | Type                            |
| :------- | :------------------------------ |
| `result` | `OnMemoryWarningCallbackResult` |

Returns

`void`

---

## Interface: OnMemoryWarningCallbackResult

| Name  | Type                | Description                                                                                                                                                                               |
| :---- | :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| level | `5` \| `10` \| `15` | Memory alert level, only Android There is, corresponding to the system macro definition - 5: TRIM_MEMORY_RUNNING_MODERATE; 10: TRIM_MEMORY_RUNNING_LOW; 15: TRIM_MEMORY_RUNNING_CRITICAL; |